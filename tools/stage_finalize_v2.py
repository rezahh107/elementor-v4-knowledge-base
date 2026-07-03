#!/usr/bin/env python3
"""Two-phase, non-self-referential finalization for one evidence stage."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from tools.evidence_validate import validate_evidence
from tools.kb import parse_front_matter
from tools.ledger_chain import append_chained_event
from tools.pipeline_common import (
    LEDGER_PATH,
    ROOT,
    canonical_json_line,
    dump_yaml,
    find_stage,
    find_work_item,
    load_stages,
    load_work_items,
    load_yaml,
    now_istanbul,
    transition,
    validate_instance,
    write_yaml,
)

COMMIT_RE = re.compile(r"^[a-f0-9]{40}$")
GAPS_PATH = ROOT / "manifests" / "evidence-gaps.yaml"
ACTIVE_GAP_STATUSES = {"open", "accepted_risk"}


def git_head() -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    value = result.stdout.strip()
    if not COMMIT_RE.fullmatch(value):
        raise ValueError(f"invalid git HEAD: {value!r}")
    return value


def _fail(errors: list[str]) -> int:
    for error in sorted(set(errors)):
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


def _safe_repo_path(value: Any) -> Path:
    if not isinstance(value, str) or not value:
        raise ValueError("missing repository path")
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"unsafe repository path: {value!r}")
    resolved = (ROOT / relative).resolve()
    resolved.relative_to(ROOT.resolve())
    return resolved


def rewrite_document_trust(stage: dict[str, Any]) -> dict[str, Any]:
    """Promote only machine trust fields while preserving document body."""
    path = ROOT / stage["output_path"]
    front_matter, body = parse_front_matter(path)
    front_matter["review_status"] = "machine_validated"
    front_matter["provenance_status"] = "claim_level"
    path.write_text(
        "---\n" + dump_yaml(front_matter) + "---\n" + body,
        encoding="utf-8",
        newline="\n",
    )
    return front_matter


def reconcile_gap_records(
    stage_id: str,
    stage: dict[str, Any],
    global_document: dict[str, Any],
    local_document: dict[str, Any],
) -> None:
    """Resolve legacy migration gaps and bind current stage gaps canonically."""
    global_records = global_document["gaps"]
    local_records = local_document["gaps"]
    local_ids = [record["gap_id"] for record in local_records]
    if len(local_ids) != len(set(local_ids)):
        raise ValueError(f"{stage_id}: duplicate local gap IDs")
    if any(record.get("stage_id") != stage_id for record in local_records):
        raise ValueError(f"{stage_id}: local gap record contains another stage")

    replacements = {record["gap_id"]: record for record in local_records}
    legacy_ids = {
        f"GAP-{stage_id}-PROVENANCE",
        f"GAP-{stage_id}-SNAPSHOT",
    }
    seen: set[str] = set()
    reconciled: list[dict[str, Any]] = []
    for record in global_records:
        gap_id = record["gap_id"]
        if gap_id in replacements:
            reconciled.append(replacements[gap_id])
            seen.add(gap_id)
            continue
        if gap_id in legacy_ids:
            record = dict(record)
            record["status"] = "resolved"
        reconciled.append(record)

    for record in local_records:
        if record["gap_id"] not in seen:
            reconciled.append(record)

    global_document["gaps"] = reconciled
    stage["gap_ids"] = [
        record["gap_id"]
        for record in local_records
        if record["status"] in ACTIVE_GAP_STATUSES
    ]


def sync_gap_truth(
    stage_id: str,
    stage: dict[str, Any],
    front_matter: dict[str, Any],
) -> None:
    gap_path = _safe_repo_path(front_matter.get("gap_record"))
    local_document = load_yaml(gap_path)
    global_document = load_yaml(GAPS_PATH)
    errors = []
    errors.extend(
        validate_instance(
            local_document,
            "evidence-gaps.schema.json",
            str(gap_path.relative_to(ROOT)),
        )
    )
    errors.extend(
        validate_instance(
            global_document,
            "evidence-gaps.schema.json",
            "manifests/evidence-gaps.yaml",
        )
    )
    if errors:
        raise ValueError("; ".join(errors))
    reconcile_gap_records(stage_id, stage, global_document, local_document)
    errors = validate_instance(
        global_document,
        "evidence-gaps.schema.json",
        "manifests/evidence-gaps.yaml",
    )
    if errors:
        raise ValueError("; ".join(errors))
    write_yaml(GAPS_PATH, global_document)


def prepare(stage_id: str, expected_head: str | None = None) -> int:
    errors = validate_evidence(stage_id)
    if errors:
        return _fail(errors)

    content_commit = git_head()
    if expected_head is not None and content_commit != expected_head:
        return _fail(
            [
                f"{stage_id}: expected content head {expected_head}, "
                f"but checkout is {content_commit}"
            ]
        )

    stages = load_stages()
    work_items = load_work_items()
    stage = find_stage(stages, stage_id)
    item = find_work_item(work_items, stage_id)
    if item["source_capture_status"] != "captured":
        return _fail([f"{stage_id}: source capture not complete"])

    if item["state"] == "evidence_draft":
        transition(item, "finalization_pending")
    if item["state"] in {"finalization_pending", "ci_failed"}:
        transition(item, "ci_running")
    if item["state"] == "ci_running":
        transition(item, "machine_validated")
    elif item["state"] != "machine_validated":
        return _fail([f"{stage_id}: cannot finalize from {item['state']}"])

    completed_at = now_istanbul()
    for source in stage["sources"]:
        record = load_yaml(
            ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml"
        )
        source["url"] = record["canonical_url"]
        source["snapshot_status"] = "captured"
        source["content_fingerprint"] = record["normalized_document_sha256"]

    stage["provenance_status"] = "claim_level"
    stage["review_status"] = "machine_validated"
    stage["content_commit_sha"] = content_commit
    stage["completed_at"] = completed_at
    try:
        front_matter = rewrite_document_trust(stage)
        sync_gap_truth(stage_id, stage, front_matter)
    except (OSError, ValueError) as exc:
        return _fail([f"{stage_id}: finalization truth reconciliation failed: {exc}"])

    item["expected_head_sha"] = content_commit
    item["github_state_observed_at"] = completed_at
    item["required_check_runs"] = {
        "head_sha": content_commit,
        "python_3_11": "pending",
        "python_3_13": "pending",
        "strict_validation": "pending",
        "generated_artifacts": "pending",
        "pytest": "pending",
    }
    write_yaml(ROOT / "manifests" / "stages.yaml", stages)
    write_yaml(ROOT / "manifests" / "work-items.yaml", work_items)
    print(f"prepared {stage_id} from content commit {content_commit}")
    return 0


def attest(stage_id: str, finalization_commit: str) -> int:
    if not COMMIT_RE.fullmatch(finalization_commit):
        return _fail([f"{stage_id}: invalid finalization commit SHA"])
    current = git_head()
    if current != finalization_commit:
        return _fail(
            [
                f"{stage_id}: finalization attestation must run at "
                f"{finalization_commit}; checkout is {current}"
            ]
        )

    stages = load_stages()
    work_items = load_work_items()
    stage = find_stage(stages, stage_id)
    item = find_work_item(work_items, stage_id)
    content_commit = stage.get("content_commit_sha")
    if not isinstance(content_commit, str) or not COMMIT_RE.fullmatch(content_commit):
        return _fail([f"{stage_id}: missing valid content commit SHA"])
    if item["state"] != "machine_validated":
        return _fail([f"{stage_id}: Work Item is not machine_validated"])

    recorded_at = now_istanbul()
    event = {
        "event_id": (
            f"{item['cycle_id']}:{stage_id}:machine-validated:"
            f"{finalization_commit[:12]}"
        ),
        "stage_id": stage_id,
        "event_type": stage["status"],
        "status": stage["status"],
        "recorded_at": recorded_at,
        "content_commit_sha": content_commit,
        "finalization_commit_sha": finalization_commit,
        "output_path": stage["output_path"],
        "notes": [
            "content_commit_sha identifies the evidence input commit",
            "finalization_commit_sha identifies the commit carrying finalization artifacts",
            "review_status is machine_validated and not peer_reviewed",
        ],
    }
    append_chained_event(
        path=LEDGER_PATH,
        event=event,
        version_field="ledger_version",
        canonical=canonical_json_line,
        validate=lambda value: validate_instance(
            value,
            "ledger-event-v2.schema.json",
            "ledger event",
        ),
    )
    print(
        f"attested {stage_id}: content={content_commit} "
        f"finalization={finalization_commit}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True)
    parser.add_argument("--phase", choices=["prepare", "attest"], default="prepare")
    parser.add_argument("--expected-head")
    parser.add_argument("--finalization-commit")
    args = parser.parse_args()
    if args.phase == "prepare":
        return prepare(args.stage, args.expected_head)
    if args.finalization_commit is None:
        parser.error("--finalization-commit is required for --phase attest")
    return attest(args.stage, args.finalization_commit)


if __name__ == "__main__":
    raise SystemExit(main())
