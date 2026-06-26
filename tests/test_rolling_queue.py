from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.queue_common import (
    EVENTS_PATH,
    append_event,
    canonical_json,
    eligible_tasks,
    load_queue,
    sha256_prefixed,
    transition_task,
    validate_identity,
    validate_queue,
)
from tools.queue_controller import plan
from tools.queue_reconcile import reconcile
from tools.queue_validate import validate_events

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "tests" / "fixtures" / "queue" / "repo-state-current.json"


def test_seed_queue_is_valid() -> None:
    assert validate_queue(load_queue()) == []


def test_event_ledger_is_valid() -> None:
    assert validate_events() == []


def test_spec_hashes_are_canonical() -> None:
    for task in load_queue()["tasks"]:
        assert task["spec_hash"] == sha256_prefixed(task["spec"])


def test_blocked_rq0001_leaves_no_task_eligible() -> None:
    queue = load_queue()
    tasks = {task["id"]: task for task in queue["tasks"]}
    assert tasks["RQ-0001"]["runtime"]["status"] == "blocked"
    assert [task["id"] for task in eligible_tasks(queue)] == []


def test_p0_reconciliation_blocks_an_otherwise_eligible_task() -> None:
    queue = copy.deepcopy(load_queue())
    tasks = {task["id"]: task for task in queue["tasks"]}
    tasks["RQ-0001"]["runtime"]["status"] = "completed"
    tasks["RQ-0001"]["runtime"]["blockers"] = []
    state = json.loads(CURRENT.read_text(encoding="utf-8"))

    result = plan(queue, state)

    assert result["blocking_diagnostics"]
    assert result["selected_task"] is None
    assert result["action"] == "blocked_by_reconciliation"
    assert result["mutations_performed"] == []


def test_illegal_direct_completion_is_rejected() -> None:
    task = copy.deepcopy(load_queue()["tasks"][0])
    with pytest.raises(ValueError, match="RQ_ILLEGAL_TRANSITION"):
        transition_task(task, "completed")


def test_current_snapshot_detects_known_drift() -> None:
    state = json.loads(CURRENT.read_text(encoding="utf-8"))
    diagnostics = reconcile(load_queue(), state)
    codes = {item["code"] for item in diagnostics}
    assert "RQ_DUPLICATE_PR" in codes
    assert "RQ_WORK_ITEM_DRIFT" in codes
    assert "RQ_CI_MISSING_JOBS" in codes
    missing_jobs = [item for item in diagnostics if item["code"] == "RQ_CI_MISSING_JOBS"]
    assert all(item["status"] == "insufficient_evidence" for item in missing_jobs)
    assert all(item["affected_conclusion"] == "exact_head_ci_acceptance" for item in missing_jobs)


def test_controller_mode_is_dry_run() -> None:
    assert load_queue()["controller_policy"]["mode"] == "dry_run"


def test_schema_invalid_queue_fails_without_crashing() -> None:
    assert validate_queue({"schema_version": 1})


def test_unknown_dependency_is_not_eligible() -> None:
    queue = load_queue()
    task = copy.deepcopy(queue["tasks"][0])
    task["spec"]["depends_on"] = ["RQ-9999"]
    assert eligible_tasks({
        "tasks": [task],
        "controller_policy": queue["controller_policy"],
    }) == []


def test_multi_task_dependency_cycle_is_rejected() -> None:
    queue = copy.deepcopy(load_queue())
    first, second = queue["tasks"][:2]
    first["spec"]["depends_on"] = [second["id"]]
    second["spec"]["depends_on"] = [first["id"]]
    errors = validate_identity(queue)
    assert any(
        error == f"dependency cycle: {first['id']} -> {second['id']} -> {first['id']}"
        for error in errors
    )


def test_canonical_json_rejects_reference_cycles() -> None:
    value: list[object] = []
    value.append(value)
    with pytest.raises(TypeError, match="reference cycle"):
        canonical_json(value)


def test_canonical_json_rejects_excessive_depth() -> None:
    value: list[object] = []
    cursor = value
    for _ in range(130):
        child: list[object] = []
        cursor.append(child)
        cursor = child
    with pytest.raises(TypeError, match="maximum depth"):
        canonical_json(value)


def test_malformed_external_snapshot_is_fail_closed() -> None:
    diagnostics = reconcile(
        load_queue(),
        {"pull_requests": "bad", "workflow_runs": None},
    )
    assert diagnostics
    assert {item["code"] for item in diagnostics} == {"RQ_REPOSITORY_SNAPSHOT_INVALID"}
    assert all(item["severity"] == "P0" for item in diagnostics)


def test_append_event_starts_chain_after_legacy_prefix(tmp_path: Path) -> None:
    path = tmp_path / "events.jsonl"
    legacy = json.loads(EVENTS_PATH.read_text(encoding="utf-8").splitlines()[0])
    path.write_text(canonical_json(legacy) + "\n", encoding="utf-8", newline="\n")
    new_event = copy.deepcopy(legacy)
    new_event["event_id"] = "RQEVT-test-chain-start"
    new_event["event_type"] = "dry_run_planned"

    append_event(new_event, path)

    assert validate_events(path) == []
    appended = json.loads(path.read_text(encoding="utf-8").splitlines()[-1])
    assert appended["schema_version"] == 2
    assert appended["chain_scope"] == "legacy_prefix"
    assert len(appended["event_sha256"]) == 64


def test_event_chain_tampering_is_detected(tmp_path: Path) -> None:
    path = tmp_path / "events.jsonl"
    legacy = json.loads(EVENTS_PATH.read_text(encoding="utf-8").splitlines()[0])
    path.write_text(canonical_json(legacy) + "\n", encoding="utf-8", newline="\n")
    event = copy.deepcopy(legacy)
    event["event_id"] = "RQEVT-test-chain-tamper"
    event["event_type"] = "dry_run_planned"
    append_event(event, path)
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = json.loads(lines[-1])
    changed["details"] = {"tampered": True}
    lines[-1] = canonical_json(changed)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    assert any("event_sha256 mismatch" in error for error in validate_events(path))


def test_finalize_workflow_is_scoped_to_migration_branches() -> None:
    workflow = (ROOT / ".github" / "workflows" / "finalize-stage.yml").read_text(
        encoding="utf-8"
    )
    assert "startsWith(github.event.pull_request.head.ref, 'migration/')" in workflow
    assert "startsWith(github.event.pull_request.head.ref, 'migration-')" in workflow
    assert "github.event.pull_request.head.repo.full_name == github.repository" in workflow


@pytest.mark.parametrize(
    "command",
    [
        [sys.executable, str(ROOT / "tools" / "queue_validate.py"), "all"],
        [
            sys.executable,
            str(ROOT / "tools" / "queue_reconcile.py"),
            "--repo-state",
            str(CURRENT),
        ],
        [
            sys.executable,
            str(ROOT / "tools" / "queue_controller.py"),
            "--repo-state",
            str(CURRENT),
        ],
        [sys.executable, str(ROOT / "validation" / "e2e" / "run_rolling_queue_check.py")],
    ],
    ids=["validate", "reconcile", "controller", "e2e"],
)
def test_documented_direct_entrypoints_run_from_outside_repo(
    command: list[str],
    tmp_path: Path,
) -> None:
    """Documented scripts must bootstrap imports without relying on cwd=repo root."""
    completed = subprocess.run(
        command,
        cwd=tmp_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert completed.returncode == 0, (
        f"command failed: {command}\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )
    assert "Traceback" not in completed.stderr
