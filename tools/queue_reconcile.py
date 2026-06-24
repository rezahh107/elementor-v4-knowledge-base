#!/usr/bin/env python3
"""Compare queue intent with local Work Items and an explicit GitHub snapshot."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from tools.queue_common import ROOT, load_queue, validate_queue


def local_work_items() -> dict[str, dict[str, Any]]:
    value = yaml.safe_load((ROOT / "manifests" / "work-items.yaml").read_text(encoding="utf-8"))
    return {item["stage_id"]: item for item in value.get("items", [])}


def reconcile(queue: dict[str, Any], external: dict[str, Any]) -> list[dict[str, Any]]:
    diagnostics: list[dict[str, Any]] = []
    work_items = local_work_items()
    pull_requests = external.get("pull_requests", [])
    workflows = external.get("workflow_runs", [])

    open_by_stage: dict[str, list[dict[str, Any]]] = {}
    for pull_request in pull_requests:
        stage_id = pull_request.get("stage_id")
        if stage_id and pull_request.get("state") == "open":
            open_by_stage.setdefault(stage_id, []).append(pull_request)
    for stage_id, records in sorted(open_by_stage.items()):
        if len(records) > 1:
            diagnostics.append({
                "code": "RQ_DUPLICATE_PR",
                "severity": "P0",
                "stage_id": stage_id,
                "message": f"{len(records)} open PRs reference {stage_id}",
                "evidence_refs": [f"pr:{item['number']}" for item in records],
            })

    reported_drift: set[tuple[str, int]] = set()
    for task in queue["tasks"]:
        stage_id = task["spec"]["stage_id"]
        expected = task["spec"].get("expected_work_item_attempt")
        if stage_id and expected is not None and stage_id in work_items:
            actual = work_items[stage_id].get("attempt")
            key = (stage_id, expected)
            if actual != expected and key not in reported_drift:
                reported_drift.add(key)
                diagnostics.append({
                    "code": "RQ_WORK_ITEM_DRIFT",
                    "severity": "P0",
                    "stage_id": stage_id,
                    "message": f"queue expects attempt {expected}; main records {actual}",
                    "evidence_refs": ["manifests/work-items.yaml", task["id"]],
                })

    for run in workflows:
        if run.get("conclusion") == "action_required" and not run.get("jobs"):
            diagnostics.append({
                "code": "RQ_CI_MISSING_JOBS",
                "severity": "P0",
                "stage_id": run.get("stage_id"),
                "message": f"workflow {run.get('name')} ended action_required without jobs",
                "evidence_refs": [f"workflow:{run.get('id')}"]
            })

    return sorted(diagnostics, key=lambda item: (item["severity"], item["code"], item.get("stage_id") or "", item["message"]))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-state", type=Path, required=True)
    args = parser.parse_args()
    queue = load_queue()
    errors = validate_queue(queue)
    if errors:
        raise SystemExit("\n".join(errors))
    external = json.loads(args.repo_state.read_text(encoding="utf-8"))
    print(json.dumps({"diagnostics": reconcile(queue, external)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
