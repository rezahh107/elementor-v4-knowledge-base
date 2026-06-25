from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.queue_common import (
    eligible_tasks,
    load_queue,
    sha256_prefixed,
    transition_task,
    validate_queue,
)
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


def test_malformed_external_snapshot_is_fail_closed() -> None:
    diagnostics = reconcile(
        load_queue(),
        {"pull_requests": "bad", "workflow_runs": None},
    )
    assert isinstance(diagnostics, list)


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
