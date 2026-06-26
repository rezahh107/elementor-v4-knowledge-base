#!/usr/bin/env python3
"""Validate migration Work Items and their GitHub/evidence bindings."""
from __future__ import annotations

import re
import sys

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

        if item["source_capture_status"] == "captured":
            stage = find_stage(stages_document, stage_id)
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
    errors = validate()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"INFO: validated {len(load_work_items()['Items'])} work items")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
