#!/usr/bin/env python3
"""Plan one primary queue task plus bounded, disjoint preparation work."""
from __future__ import annotations

import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import argparse
import json
from typing import Any

from tools.queue_common import eligible_tasks, load_queue, validate_queue
from tools.queue_reconcile import reconcile

PREPARATION_TASK_TYPES = {
    "fixture_collection",
    "manual_evidence_request",
    "documentation_sync",
}


def _is_preparation(task: dict[str, Any]) -> bool:
    return task.get("spec", {}).get("task_type") in PREPARATION_TASK_TYPES


def select_execution_slice(
    queue: dict[str, Any],
    eligible: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Select one primary task and bounded non-overlapping preparation tasks.

    Only the primary task may be a shared-state or stage-mutation work unit.
    Additional selections are preparation-only and must target a different stage
    (or no stage) so an hourly executor can keep useful research moving without
    opening a second shared-truth mutation path.
    """
    if not eligible:
        return []

    primary = eligible[0]
    selected = [primary]
    preparation_limit = queue.get("controller_policy", {}).get(
        "max_planned_preparation_tasks", 3
    )
    primary_stage = primary.get("spec", {}).get("stage_id")

    for task in eligible[1:]:
        if len(selected) - 1 >= preparation_limit:
            break
        if not _is_preparation(task):
            continue
        task_stage = task.get("spec", {}).get("stage_id")
        if primary_stage is not None and task_stage == primary_stage:
            continue
        selected.append(task)
    return selected


def plan(queue: dict[str, Any], repo_state: dict[str, Any]) -> dict[str, Any]:
    diagnostics = reconcile(queue, repo_state)
    blocking = [item for item in diagnostics if item["severity"] == "P0"]

    # Fail closed: reconciliation truth outranks queue execution intent. A P0
    # diagnostic must never be bypassed by an otherwise independent task.
    eligible = [] if blocking else eligible_tasks(queue)
    selected = select_execution_slice(queue, eligible)
    selected_ids = [task["id"] for task in selected]
    return {
        "mode": queue["controller_policy"]["mode"],
        "queue_revision": queue["queue_revision"],
        "selected_task": selected_ids[0] if selected_ids else None,
        "selected_tasks": selected_ids,
        "action": (
            "blocked_by_reconciliation"
            if blocking
            else "report_and_plan_batch"
        ),
        "blocking_diagnostics": blocking,
        "all_diagnostics": diagnostics,
        "mutations_performed": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-state", required=True, type=Path)
    args = parser.parse_args()
    queue = load_queue()
    errors = validate_queue(queue)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if queue["controller_policy"]["mode"] != "dry_run":
        print("ERROR: repository controller only supports dry_run", file=sys.stderr)
        return 1
    try:
        repo_state = json.loads(args.repo_state.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid repository-state snapshot: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(plan(queue, repo_state), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
