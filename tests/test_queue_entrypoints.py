from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = Path("tests/fixtures/queue/repo-state-current.json")


def run_entrypoint(*arguments: str) -> subprocess.CompletedProcess[str]:
    """Run a documented script as a user would, without PYTHONPATH assistance."""
    environment = os.environ.copy()
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    return subprocess.run(
        [sys.executable, "-I", *arguments],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )


def assert_success(result: subprocess.CompletedProcess[str]) -> None:
    assert result.returncode == 0, (
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}\n"
        f"returncode: {result.returncode}"
    )


def test_queue_validate_documented_entrypoint() -> None:
    result = run_entrypoint("tools/queue_validate.py", "all")
    assert_success(result)
    assert result.stdout.strip() == "ROLLING_QUEUE_VALID"


def test_queue_reconcile_documented_entrypoint() -> None:
    result = run_entrypoint(
        "tools/queue_reconcile.py",
        "--repo-state",
        str(STATE),
    )
    assert_success(result)
    payload = json.loads(result.stdout)
    codes = {item["code"] for item in payload["diagnostics"]}
    assert {
        "RQ_DUPLICATE_PR",
        "RQ_WORK_ITEM_DRIFT",
        "RQ_CI_MISSING_JOBS",
    } <= codes


def test_queue_controller_documented_entrypoint() -> None:
    result = run_entrypoint(
        "tools/queue_controller.py",
        "--repo-state",
        str(STATE),
    )
    assert_success(result)
    payload = json.loads(result.stdout)
    assert payload["mode"] == "dry_run"
    assert payload["selected_task"] is None
    assert payload["mutations_performed"] == []


def test_queue_e2e_documented_entrypoint() -> None:
    result = run_entrypoint("validation/e2e/run_rolling_queue_check.py")
    assert_success(result)
    payload = json.loads(result.stdout)
    assert payload["mode"] == "dry_run"
    assert payload["selected_task"] is None
    assert payload["mutations_performed"] == []
