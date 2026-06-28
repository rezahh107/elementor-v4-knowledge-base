#!/usr/bin/env python3
"""Deterministic offline end-to-end check for PR A.2."""
from __future__ import annotations

import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import json

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
    if report["mode"] != "dry_run":
        raise AssertionError("controller mode changed")
    if report["selected_task"] is not None:
        raise AssertionError("P0 reconciliation diagnostics should leave no selected task")
    if report["mutations_performed"] != []:
        raise AssertionError("dry-run performed mutations")
    codes = {item["code"] for item in report["all_diagnostics"]}
    required = {"RQ_DUPLICATE_PR", "RQ_CI_MISSING_JOBS"}
    if not required.issubset(codes):
        raise AssertionError("expected drift diagnostics are missing")
    tasks = {task["id"]: task for task in queue["tasks"]}
    if tasks["RQ-0003"]["runtime"]["status"] != "completed":
        raise AssertionError("RQ-0003 should be completed after merged hardening evidence")
    if tasks["RQ-0004"]["runtime"]["status"] != "pending":
        raise AssertionError("RQ-0004 should remain the next pending task")
    if eligible_tasks(queue)[0]["id"] != "RQ-0004":
        raise AssertionError("RQ-0004 should be the next queue-eligible task before reconciliation diagnostics")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
