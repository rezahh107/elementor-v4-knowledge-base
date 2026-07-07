#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def plan(state: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    catalog = load(root / "planning" / "WORK_PACKAGE_CATALOG.json")
    queue = load(root / "planning" / "WORK_PACKAGE_QUEUE.json")
    control = load(root / "planning" / "CONTROL_STATE.json")

    pull_requests = state.get("pull_requests") if isinstance(state, dict) else None
    if not isinstance(pull_requests, list):
        pull_requests = []
    open_pull_requests = [
        item
        for item in pull_requests
        if isinstance(item, dict) and item.get("state") == "open"
    ]

    if len(open_pull_requests) > 1:
        return {
            "action": "blocked",
            "reason": "multiple_open_mutation_prs",
            "work_package": None,
        }
    if open_pull_requests:
        return {
            "action": "reconcile_existing_mutation_pr",
            "work_package": control.get("active_work_package_id"),
        }

    packages = {
        item.get("id"): item
        for item in catalog.get("work_packages", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }

    active_id = queue.get("active_work_package_id")
    if active_id:
        active = packages.get(active_id)
        if not isinstance(active, dict) or active.get("status") != "active":
            return {
                "action": "blocked",
                "reason": "active_work_package_status_drift",
                "work_package": active_id,
            }
        return {
            "action": "continue_active_work_package",
            "work_package": active_id,
        }

    queued_ready = queue.get("ready_work_packages")
    if not isinstance(queued_ready, list):
        queued_ready = []
    executable = [
        work_package_id
        for work_package_id in queued_ready
        if isinstance(packages.get(work_package_id), dict)
        and packages[work_package_id].get("status") == "ready"
    ]
    drifted = sorted(
        work_package_id
        for work_package_id in queued_ready
        if work_package_id not in executable
    )
    if drifted:
        return {
            "action": "blocked",
            "reason": "ready_queue_catalog_status_drift",
            "work_package": None,
            "drifted_work_packages": drifted,
        }

    refresh_threshold = (catalog.get("policy") or {}).get(
        "refresh_when_ready_below", 0
    )
    return {
        "action": "start_ready_work_package" if executable else "no_executable_work",
        "work_package": executable[0] if executable else None,
        "catalog_refresh_needed": len(executable) < refresh_threshold,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-state", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(plan(load(args.repo_state)), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
