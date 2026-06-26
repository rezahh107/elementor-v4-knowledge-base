#!/usr/bin/env python3
"""Reconcile queue intent with a supplied GitHub/EDIS repository-state snapshot."""
from __future__ import annotations

import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import argparse
import json
import re
from typing import Any

import yaml

from tools.queue_common import ROOT, load_queue, validate_queue, validate_schema

STATUS_STAGE_RE = re.compile(
    r"^\| (?P<stage>KB-[0-9]{3}) \|.*\| `(?P<status>[^`]+)` \| "
    r"`(?P<review>[^`]+)` \| `(?P<provenance>[^`]+)` \|",
    re.MULTILINE,
)
REPOSITORY_STATE_SCHEMA = ROOT / "schemas" / "repository-state.schema.json"


def diagnostic(
    *,
    code: str,
    severity: str,
    message: str,
    evidence_refs: list[str],
    stage_id: str | None = None,
    status: str = "validated",
    affected_conclusion: str,
    required_action: str,
    retry_condition: str,
    missing_evidence: list[str] | None = None,
) -> dict[str, Any]:
    value: dict[str, Any] = {
        "code": code,
        "severity": severity,
        "stage_id": stage_id,
        "status": status,
        "message": message,
        "affected_conclusion": affected_conclusion,
        "required_action": required_action,
        "retry_condition": retry_condition,
        "evidence_refs": sorted(set(evidence_refs)),
    }
    if missing_evidence:
        value["missing_evidence"] = sorted(set(missing_evidence))
    return value


def local_state() -> dict[str, Any]:
    errors: list[str] = []
    try:
        status_text = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    except OSError as exc:
        status_text = ""
        errors.append(f"STATUS.md unavailable: {exc}")

    work_items_path = ROOT / "manifests" / "work-items.yaml"
    try:
        value = yaml.safe_load(work_items_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        value = {}
        errors.append(f"manifests/work-items.yaml unavailable or malformed: {exc}")
    if not isinstance(value, dict):
        value = {}
        errors.append("manifests/work-items.yaml root is not an object")
    items = value.get("items", [])
    if not isinstance(items, list):
        items = []
        errors.append("manifests/work-items.yaml items is not a list")

    return {
        "errors": errors,
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
    for error in local["errors"]:
        diagnostics.append(
            diagnostic(
                code="RQ_LOCAL_STATE_INVALID",
                severity="P0",
                message=error,
                evidence_refs=["STATUS.md", "manifests/work-items.yaml"],
                affected_conclusion="repository_consistency",
                required_action="restore and validate the canonical local state files",
                retry_condition="local state parses and validates without errors",
            )
        )

    if not isinstance(external, dict):
        external = {}
    snapshot_errors = validate_schema(
        external,
        REPOSITORY_STATE_SCHEMA,
        "repository-state snapshot",
    )
    if snapshot_errors:
        for error in snapshot_errors:
            diagnostics.append(
                diagnostic(
                    code="RQ_REPOSITORY_SNAPSHOT_INVALID",
                    severity="P0",
                    message=error,
                    evidence_refs=["repository-state snapshot"],
                    status="insufficient_evidence",
                    affected_conclusion="github_state_reconciliation",
                    required_action="capture a schema-valid GitHub repository-state snapshot",
                    retry_condition="snapshot passes schemas/repository-state.schema.json",
                    missing_evidence=["schema-valid current GitHub snapshot"],
                )
            )
        return sorted(
            diagnostics,
            key=lambda item: (
                item["severity"],
                item["code"],
                item.get("stage_id") or "",
                item["message"],
            ),
        )

    prs = [item for item in external["pull_requests"] if isinstance(item, dict)]
    workflows = [item for item in external["workflow_runs"] if isinstance(item, dict)]
    prs_by_number = {
        pr["number"]: pr for pr in prs if isinstance(pr.get("number"), int)
    }

    active_by_stage: dict[str, list[dict[str, Any]]] = {}
    for pr in prs:
        stage_id = pr.get("stage_id")
        if isinstance(stage_id, str) and pr.get("state") == "open":
            active_by_stage.setdefault(stage_id, []).append(pr)

    for stage_id, stage_prs in sorted(active_by_stage.items()):
        if len(stage_prs) > 1:
            diagnostics.append(
                diagnostic(
                    code="RQ_DUPLICATE_PR",
                    severity="P0",
                    stage_id=stage_id,
                    message=f"{len(stage_prs)} open PRs reference {stage_id}",
                    evidence_refs=[
                        f"pr:{pr['number']}"
                        for pr in stage_prs
                        if isinstance(pr.get("number"), int)
                    ],
                    affected_conclusion="single_active_stage_migration",
                    required_action="retain one canonical active PR and explicitly supersede duplicates",
                    retry_condition="exactly one open PR references the stage",
                )
            )

    reported_work_item_drift: set[tuple[str, int]] = set()
    for task in queue["tasks"]:
        task_id = task["id"]
        stage_id = task["spec"]["stage_id"]
        runtime = task["runtime"]
        work_item = local["work_items"].get(stage_id) if stage_id else None
        if stage_id and work_item is not None:
            expected_attempt = task["spec"].get("expected_work_item_attempt")
            if (
                expected_attempt is not None
                and work_item.get("attempt") != expected_attempt
                and (stage_id, expected_attempt) not in reported_work_item_drift
            ):
                reported_work_item_drift.add((stage_id, expected_attempt))
                diagnostics.append(
                    diagnostic(
                        code="RQ_WORK_ITEM_DRIFT",
                        severity="P0",
                        stage_id=stage_id,
                        message=(
                            f"queue expects attempt {expected_attempt}; "
                            f"main records {work_item.get('attempt')}"
                        ),
                        evidence_refs=["manifests/work-items.yaml", task_id],
                        affected_conclusion="active_migration_attempt",
                        required_action="reconcile queue intent with the canonical Work Item",
                        retry_condition="queue and Work Item record the same attempt",
                    )
                )

            work_pr_number = work_item.get("pr_number")
            work_pr = prs_by_number.get(work_pr_number) if isinstance(work_pr_number, int) else None
            stage_prs = active_by_stage.get(stage_id, [])
            if len(stage_prs) == 1 and work_pr_number != stage_prs[0].get("number"):
                diagnostics.append(
                    diagnostic(
                        code="RQ_WORK_ITEM_PR_DRIFT",
                        severity="P0",
                        stage_id=stage_id,
                        message=(
                            f"Work Item references PR {work_pr_number}; "
                            f"GitHub has active PR {stage_prs[0].get('number')}"
                        ),
                        evidence_refs=["manifests/work-items.yaml", f"pr:{stage_prs[0].get('number')}"],
                        affected_conclusion="canonical_active_pull_request",
                        required_action="update the Work Item only after verifying the canonical PR",
                        retry_condition="Work Item and GitHub reference the same active PR",
                    )
                )
            if isinstance(work_pr_number, int) and work_pr is None:
                diagnostics.append(
                    diagnostic(
                        code="RQ_WORK_ITEM_PR_MISSING",
                        severity="P0",
                        stage_id=stage_id,
                        message=f"Work Item PR {work_pr_number} is absent from the snapshot",
                        evidence_refs=["manifests/work-items.yaml", f"pr:{work_pr_number}"],
                        status="insufficient_evidence",
                        affected_conclusion="canonical_active_pull_request",
                        required_action="capture the referenced PR or repair the Work Item from verified GitHub state",
                        retry_condition="the referenced PR is present in a current snapshot",
                        missing_evidence=[f"GitHub state for PR {work_pr_number}"],
                    )
                )
            if work_pr is not None:
                if isinstance(work_pr.get("head_ref"), str) and work_pr["head_ref"] != work_item.get("branch"):
                    diagnostics.append(
                        diagnostic(
                            code="RQ_WORK_ITEM_BRANCH_DRIFT",
                            severity="P0",
                            stage_id=stage_id,
                            message=(
                                f"Work Item branch {work_item.get('branch')} differs from "
                                f"PR branch {work_pr.get('head_ref')}"
                            ),
                            evidence_refs=["manifests/work-items.yaml", f"pr:{work_pr_number}"],
                            affected_conclusion="canonical_active_branch",
                            required_action="reconcile the Work Item branch with verified PR metadata",
                            retry_condition="Work Item and PR branch names match",
                        )
                    )
                if work_pr.get("merged") is True and work_item.get("state") != "merged":
                    diagnostics.append(
                        diagnostic(
                            code="RQ_MERGE_STATE_DRIFT",
                            severity="P0",
                            stage_id=stage_id,
                            message="GitHub reports a merged PR while the Work Item is not merged",
                            evidence_refs=["manifests/work-items.yaml", f"pr:{work_pr_number}"],
                            affected_conclusion="stage_merge_transition",
                            required_action="verify merge SHA and update the Work Item through the accepted transition",
                            retry_condition="GitHub and Work Item merge states agree",
                        )
                    )
                if work_pr.get("state") == "open" and work_item.get("state") == "merged":
                    diagnostics.append(
                        diagnostic(
                            code="RQ_MERGE_STATE_DRIFT",
                            severity="P0",
                            stage_id=stage_id,
                            message="Work Item is merged while GitHub PR remains open",
                            evidence_refs=["manifests/work-items.yaml", f"pr:{work_pr_number}"],
                            affected_conclusion="stage_merge_transition",
                            required_action="repair the unsupported Work Item transition",
                            retry_condition="GitHub and Work Item merge states agree",
                        )
                    )

        if runtime["active_pr"] is not None:
            pr = prs_by_number.get(runtime["active_pr"])
            if pr is None:
                diagnostics.append(
                    diagnostic(
                        code="RQ_PR_MISSING",
                        severity="P0",
                        stage_id=stage_id,
                        message=f"active PR {runtime['active_pr']} is absent",
                        evidence_refs=[task_id],
                        status="insufficient_evidence",
                        affected_conclusion="queue_task_github_binding",
                        required_action="capture current metadata for the referenced PR",
                        retry_condition="the active PR is present in the snapshot",
                        missing_evidence=[f"GitHub state for PR {runtime['active_pr']}"],
                    )
                )
            else:
                if runtime["status"] == "awaiting_external" and pr.get("draft") is False:
                    diagnostics.append(
                        diagnostic(
                            code="RQ_PR_STATE_DRIFT",
                            severity="P1",
                            stage_id=stage_id,
                            message="queue awaits draft work but PR is ready for review",
                            evidence_refs=[f"pr:{pr['number']}", task_id],
                            affected_conclusion="queue_task_state",
                            required_action="reconcile the queue runtime with the current PR review state",
                            retry_condition="queue and PR review states agree",
                        )
                    )
                last_head = runtime.get("last_ci_head_sha")
                current_head = pr.get("head_sha")
                if isinstance(last_head, str) and isinstance(current_head, str) and last_head != current_head:
                    diagnostics.append(
                        diagnostic(
                            code="RQ_STALE_CI_HEAD",
                            severity="P0",
                            stage_id=stage_id,
                            message=f"queue CI head {last_head} differs from PR head {current_head}",
                            evidence_refs=[task_id, f"pr:{pr['number']}", f"head:{current_head}"],
                            affected_conclusion="exact_head_ci_acceptance",
                            required_action="run and record all required checks on the exact current PR head",
                            retry_condition="queue last_ci_head_sha equals the current PR head",
                        )
                    )

    for run in workflows:
        jobs = run.get("jobs")
        if not isinstance(jobs, list):
            jobs = []
        if run.get("conclusion") == "action_required" and not jobs:
            reason = run.get("action_required_reason")
            has_reason = isinstance(reason, str) and bool(reason.strip())
            message = f"workflow {run.get('name')} ended action_required without jobs"
            if has_reason:
                message += f": {reason.strip()}"
            diagnostics.append(
                diagnostic(
                    code="RQ_CI_MISSING_JOBS",
                    severity="P0",
                    stage_id=run.get("stage_id")
                    if isinstance(run.get("stage_id"), str)
                    else None,
                    message=message,
                    evidence_refs=[f"workflow:{run.get('id')}"],
                    status="validated" if has_reason else "insufficient_evidence",
                    affected_conclusion="exact_head_ci_acceptance",
                    required_action=(
                        "apply the evidenced repository or organization action requirement"
                        if has_reason
                        else "obtain the GitHub action-required reason or approval metadata"
                    ),
                    retry_condition="the exact-head run creates the required jobs and no longer concludes action_required",
                    missing_evidence=None if has_reason else ["GitHub action_required reason or approval metadata"],
                )
            )

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
