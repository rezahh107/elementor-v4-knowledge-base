#!/usr/bin/env python3
"""Plan exactly one safe rolling-queue action. PR A.2 is dry-run only."""
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


def plan(queue: dict[str, Any], repo_state: dict[str, Any]) -> dict[str, Any]:
    diagnostics = reconcile(queue, repo_state)
    blocking = [item for item in diagnostics if item["severity"] == "P0"]
    eligible = eligible_tasks(queue)
    selected = eligible[0] if eligible else None
    return {
        "mode": queue["controller_policy"]["mode"],
        "queue_revision": queue["queue_revision"],
        "selected_task": selected["id"] if selected else None,
        "action": "report_and_plan_only",
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
        print("ERROR: PR A.2 controller only supports dry_run", file=sys.stderr)
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
