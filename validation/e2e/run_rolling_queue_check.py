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
    if tasks["RQ-0003"]["runtime"]["status"] != "needs_review":
        raise AssertionError("RQ-0003 should remain active until exact-head review gates pass")
    if eligible_tasks(queue) != []:
        raise AssertionError("active RQ-0003 should block new eligible tasks")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
