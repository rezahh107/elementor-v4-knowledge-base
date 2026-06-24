#!/usr/bin/env python3
"""Plan exactly one safe rolling-queue action. PR A.2 is dry-run only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from tools.queue_common import eligible_tasks, load_queue, validate_queue
from tools.queue_reconcile import reconcile


def plan(queue: dict[str, Any], repo_state: dict[str, Any]) -> dict[str, Any]:
    diagnostics = reconcile(queue, repo_state)
    selected = eligible_tasks(queue)
    return {
        "mode": queue["controller_policy"]["mode"],
        "queue_revision": queue["queue_revision"],
        "selected_task": selected[0]["id"] if selected else None,
        "action": "report_and_plan_only",
        "blocking_diagnostics": [item for item in diagnostics if item["severity"] == "P0"],
        "all_diagnostics": diagnostics,
        "mutations_performed": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-state", type=Path, required=True)
    args = parser.parse_args()
    queue = load_queue()
    errors = validate_queue(queue)
    if errors:
        raise SystemExit("\n".join(errors))
    if queue["controller_policy"]["mode"] != "dry_run":
        raise SystemExit("PR A.2 permits dry_run only")
    repo_state = json.loads(args.repo_state.read_text(encoding="utf-8"))
    print(json.dumps(plan(queue, repo_state), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
