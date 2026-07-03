#!/usr/bin/env python3
"""Validate migration Work Items and their GitHub/evidence bindings."""
from __future__ import annotations

import re
import sys
from typing import Any

from tools.kb import parse_front_matter
from tools.pipeline_common import (
    ROOT,
    find_stage,
    load_stages,
    load_work_items,
    load_yaml,
    validate_instance,
)

COMMIT_RE = re.compile(r"^[a-f0-9]{40}$")
SUCCESS_FIELDS = {
    "python_3_11",
    "python_3_13",
    "strict_validation",
    "generated_artifacts",
    "pytest",
}
ACTIVE_GAP_STATUSES = {"open", "accepted_risk"}


def finalization_alignment_errors(
    item: dict[str, Any],
    stage: dict[str, Any],
) -> list[str]:
    """Reject self-inconsistent partial or completed finalization states."""
    errors: list[str] = []
    work_id = item["work_id"]
    state = item["state"]
    sources_captured = all(
        source.get("snapshot_status") == "captured"
        and isinstance(source.get("content_fingerprint"), str)
        for source in stage["sources"]
    )
    stage_finalized = (
        stage.get("provenance_status") == "claim_level"
        and stage.get("review_status")
        in {"machine_validated", "peer_reviewed", "verified_by_fixture"}
        and sources_captured
    )

    if state == "finalization_pending" and stage_finalized:
        errors.append(
            f"{work_id}: stale finalization_pending state after canonical stage finalization"
        )

    if state not in {"machine_validated", "merged"}:
        return errors

    if stage.get("provenance_status") != "claim_level":
        errors.append(f"{work_id}: validated Work Item requires claim-level provenance")
    if stage.get("review_status") not in {
        "machine_validated",
        "peer_reviewed",
        "verified_by_fixture",
    }:
        errors.append(f"{work_id}: validated Work Item requires machine trust or review")
    if not sources_captured:
        errors.append(f"{work_id}: validated Work Item requires captured manifest sources")

    legacy_ids = {
        f"GAP-{stage['stage_id']}-PROVENANCE",
        f"GAP-{stage['stage_id']}-SNAPSHOT",
    }
    stale = sorted(legacy_ids.intersection(stage.get("gap_ids", [])))
    if stale:
        errors.append(f"{work_id}: finalized stage retains legacy migration gaps: {stale}")

    document_path = ROOT / stage["output_path"]
    try:
        front_matter, _ = parse_front_matter(document_path)
    except (OSError, ValueError) as exc:
        errors.append(f"{work_id}: cannot inspect finalized document: {exc}")
        return errors
    if front_matter.get("provenance_status") != stage.get("provenance_status"):
        errors.append(f"{work_id}: finalized document provenance differs from stage")
    if front_matter.get("review_status") != stage.get("review_status"):
        errors.append(f"{work_id}: finalized document review state differs from stage")

    gap_record = front_matter.get("gap_record")
    if not isinstance(gap_record, str):
        errors.append(f"{work_id}: finalized document lacks gap_record")
        return errors
    local_path = ROOT / gap_record
    local_document = load_yaml(local_path)
    global_document = load_yaml(ROOT / "manifests" / "evidence-gaps.yaml")
    local_records = local_document.get("gaps", []) if isinstance(local_document, dict) else []
    global_records = global_document.get("gaps", []) if isinstance(global_document, dict) else []
    active_local_ids = [
        record.get("gap_id")
        for record in local_records
        if isinstance(record, dict) and record.get("status") in ACTIVE_GAP_STATUSES
    ]
    if stage.get("gap_ids") != active_local_ids:
        errors.append(
            f"{work_id}: stage gap_ids differ from active canonical stage gap record"
        )
    global_by_id = {
        record.get("gap_id"): record
        for record in global_records
        if isinstance(record, dict) and isinstance(record.get("gap_id"), str)
    }
    for record in local_records:
        if not isinstance(record, dict):
            continue
        gap_id = record.get("gap_id")
        if global_by_id.get(gap_id) != record:
            errors.append(f"{work_id}: global gap registry differs for {gap_id}")
    for gap_id in legacy_ids:
        record = global_by_id.get(gap_id)
        if record is not None and record.get("status") == "open":
            errors.append(f"{work_id}: resolved migration gap remains open: {gap_id}")
    return errors


def validate() -> list[str]:
    document = load_work_items()
    errors = validate_instance(
        document,
        "work-item.schema.json",
        "manifests/work-items.yaml",
    )
    stages_document = load_stages()
    stages = {stage["stage_id"]: stage for stage in stages_document["stages"]}
    seen_work_ids: set[str] = set()
    seen_stage_ids: set[str] = set()
    seen_keys: set[str] = set()

    for item in document["items"]:
        work_id = item["work_id"]
        stage_id = item["stage_id"]
        key = item["idempotency_key"]
        if work_id in seen_work_ids:
            errors.append(f"duplicate work_id: {work_id}")
        if stage_id in seen_stage_ids:
            errors.append(f"duplicate work-item stage_id: {stage_id}")
        if key in seen_keys:
            errors.append(f"duplicate idempotency_key: {key}")
        seen_work_ids.add(work_id)
        seen_stage_ids.add(stage_id)
        seen_keys.add(key)

        if stage_id not in stages:
            errors.append(f"{work_id}: unknown stage {stage_id}")
            continue
        if stage_id not in item["branch"]:
            errors.append(f"{work_id}: branch must contain {stage_id}")

        stage = find_stage(stages_document, stage_id)
        if item["source_capture_status"] == "captured":
            for source in stage["sources"]:
                path = ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml"
                if not path.exists():
                    errors.append(
                        f"{work_id}: missing captured source record "
                        f"{path.relative_to(ROOT)}"
                    )
                    continue
                record = load_yaml(path)
                errors.extend(
                    validate_instance(
                        record,
                        "source-record-v3.schema.json",
                        str(path.relative_to(ROOT)),
                    )
                )
                if record.get("stage_id") != stage_id:
                    errors.append(f"{path.relative_to(ROOT)}: stage_id mismatch")
                snapshot = record.get("snapshot")
                if not isinstance(snapshot, dict):
                    errors.append(f"{path.relative_to(ROOT)}: missing snapshot attestation")
                elif snapshot.get("response_bytes_sha256") != record.get(
                    "response_bytes_sha256"
                ):
                    errors.append(f"{path.relative_to(ROOT)}: snapshot hash mismatch")

        errors.extend(finalization_alignment_errors(item, stage))

        if item["state"] in {"machine_validated", "merged"}:
            if item["source_capture_status"] != "captured":
                errors.append(f"{work_id}: validated state without captured source")
            if item["pr_number"] is None:
                errors.append(f"{work_id}: validated state without PR number")
            observed = item.get("expected_head_sha")
            if not isinstance(observed, str) or not COMMIT_RE.fullmatch(observed):
                errors.append(f"{work_id}: validated state without observed head SHA")
            if item.get("github_state_observed_at") is None:
                errors.append(f"{work_id}: validated state without observation time")
            checks = item.get("required_check_runs")
            if not isinstance(checks, dict):
                errors.append(f"{work_id}: validated state without check-run record")
            elif checks.get("head_sha") != observed:
                errors.append(f"{work_id}: check-run head differs from observed head")

        if item["state"] == "merged":
            merged = item.get("merged_commit_sha")
            if not isinstance(merged, str) or not COMMIT_RE.fullmatch(merged):
                errors.append(f"{work_id}: merged state without merge commit SHA")
            checks = item.get("required_check_runs")
            if isinstance(checks, dict):
                failed = sorted(
                    field for field in SUCCESS_FIELDS if checks.get(field) != "success"
                )
                if failed:
                    errors.append(
                        f"{work_id}: merged state without successful checks: {failed}"
                    )

    return sorted(set(errors))


def main() -> int:
    document = load_work_items()
    errors = validate()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"INFO: validated {len(document['items'])} work items")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
