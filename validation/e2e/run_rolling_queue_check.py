#!/usr/bin/env python3
"""Deterministic offline end-to-end check for PR A.2."""
from __future__ import annotations

import json
from pathlib import Path

from tools.queue_common import eligible_tasks, load_queue, validate_queue
from tools.queue_controller import plan

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "tests" / "fixtures" / "queue" / "repo-state-current.json"


def main() -> int:
    queue = load_queue()
    errors = validate_queue(queue)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    state = json.loads(STATE.read_text(encoding="utf-8"))
    report = plan(queue, state)
    assert report["mode"] == "dry_run"
    assert report["selected_task"] == "RQ-0001"
    assert report["mutations_performed"] == []
    codes = {item["code"] for item in report["all_diagnostics"]}
    assert {"RQ_DUPLICATE_PR", "RQ_WORK_ITEM_DRIFT", "RQ_CI_MISSING_JOBS"} <= codes
    assert [task["id"] for task in eligible_tasks(queue)] == ["RQ-0001"]
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
