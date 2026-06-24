#!/usr/bin/env python3
"""Reconcile queue intent with a supplied GitHub/EDIS repository-state snapshot."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from tools.queue_common import ROOT, load_queue, validate_queue

STATUS_STAGE_RE = re.compile(
    r"^\| (?P<stage>KB-[0-9]{3}) \|.*\| `(?P<status>[^`]+)` \| "
    r"`(?P<review>[^`]+)` \| `(?P<provenance>[^`]+)` \|",
    re.MULTILINE,
)


def local_state() -> dict[str, Any]:
    status_text = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    work_items_path = ROOT / "manifests" / "work-items.yaml"
    import yaml

    value = yaml.safe_load(work_items_path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        value = {}
    items = value.get("items", [])
    if not isinstance(items, list):
        items = []
    return {
        "status_stages": {
            match.group("stage"): {
                "status": match.group("status"),
                "review": match.group("review"),
                "provenance": match.group("provenance"),
            }
            for match in STATUS_STAGE_RE.finditer(status_text)
        },
        "work_items": {
            item["stage_id"]: item
            for item in items
            if isinstance(item, dict) and isinstance(item.get("stage_id"), str)
        },
    }


def reconcile(queue: dict[str, Any], external: dict[str, Any]) -> list[dict[str, Any]]:
    diagnostics: list[dict[str, Any]] = []
    local = local_state()
    if not isinstance(external, dict):
        external = {}
    prs = external.get("pull_requests", [])
    workflows = external.get("workflow_runs", [])
    if not isinstance(prs, list):
        prs = []
    if not isinstance(workflows, list):
        workflows = []
    prs = [item for item in prs if isinstance(item, dict)]
    workflows = [item for item in workflows if isinstance(item, dict)]
    prs_by_number = {
        pr["number"]: pr for pr in prs if isinstance(pr.get("number"), int)
    }
    active_by_stage: dict[str, list[dict[str, Any]]] = {}
    for pr in prs:
        stage_id = pr.get("stage_id")
        if stage_id and pr.get("state") == "open":
            active_by_stage.setdefault(stage_id, []).append(pr)

    for stage_id, stage_prs in sorted(active_by_stage.items()):
        if len(stage_prs) > 1:
            diagnostics.append({
                "code": "RQ_DUPLICATE_PR",
                "severity": "P0",
                "stage_id": stage_id,
                "message": f"{len(stage_prs)} open PRs reference {stage_id}",
                "evidence_refs": [f"pr:{pr['number']}" for pr in stage_prs],
            })

    reported_work_item_drift: set[tuple[str, int]] = set()
    for task in queue["tasks"]:
        stage_id = task["spec"]["stage_id"]
        runtime = task["runtime"]
        if stage_id and stage_id in local["work_items"]:
            work_item = local["work_items"][stage_id]
            expected_attempt = task["spec"].get("expected_work_item_attempt")
            if expected_attempt is not None and work_item.get("attempt") != expected_attempt:
                key = (stage_id, expected_attempt)
                if key not in reported_work_item_drift:
                    reported_work_item_drift.add(key)
                    diagnostics.append({
                        "code": "RQ_WORK_ITEM_DRIFT",
                        "severity": "P0",
                        "stage_id": stage_id,
                        "message": (
                            f"queue expects attempt {expected_attempt}; "
                            f"main records {work_item.get('attempt')}"
                        ),
                        "evidence_refs": ["manifests/work-items.yaml", task["id"]],
                    })
        if runtime["active_pr"] is not None:
            pr = prs_by_number.get(runtime["active_pr"])
            if pr is None:
                diagnostics.append({
                    "code": "RQ_PR_MISSING",
                    "severity": "P0",
                    "stage_id": stage_id,
                    "message": f"active PR {runtime['active_pr']} is absent",
                    "evidence_refs": [task["id"]],
                })
            elif runtime["status"] == "awaiting_external" and pr.get("draft") is False:
                diagnostics.append({
                    "code": "RQ_PR_STATE_DRIFT",
                    "severity": "P1",
                    "stage_id": stage_id,
                    "message": "queue awaits draft work but PR is ready for review",
                    "evidence_refs": [f"pr:{pr['number']}", task["id"]],
                })

    for run in workflows:
        jobs = run.get("jobs")
        if not isinstance(jobs, list):
            jobs = []
        if run.get("conclusion") == "action_required" and not jobs:
            diagnostics.append({
                "code": "RQ_CI_MISSING_JOBS",
                "severity": "P0",
                "stage_id": run.get("stage_id"),
                "message": (
                    f"workflow {run.get('name')} ended action_required without jobs"
                ),
                "evidence_refs": [f"workflow:{run.get('id')}"],
            })

    return sorted(
        diagnostics,
        key=lambda item: (
            item["severity"],
            item["code"],
            item.get("stage_id") or "",
            item["message"],
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-state", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    queue = load_queue()
    errors = validate_queue(queue)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    try:
        external = json.loads(args.repo_state.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid repository-state snapshot: {exc}", file=sys.stderr)
        return 1
    diagnostics = reconcile(queue, external)
    print(json.dumps({"diagnostics": diagnostics}, ensure_ascii=False, indent=2))
    if args.strict and any(item["severity"] == "P0" for item in diagnostics):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
