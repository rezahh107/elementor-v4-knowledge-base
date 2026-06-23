#!/usr/bin/env python3
"""Validate migration work items and their captured evidence references."""
from __future__ import annotations

import sys
from pathlib import Path

from tools.pipeline_common import (
    ROOT,
    find_stage,
    load_stages,
    load_work_items,
    load_yaml,
    validate_instance,
)


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
                    errors.append(f"{work_id}: missing captured source record {path.relative_to(ROOT)}")
                    continue
                record = load_yaml(path)
                errors.extend(
                    validate_instance(
                        record,
                        "source-record.schema.json",
                        str(path.relative_to(ROOT)),
                    )
                )
                if record.get("stage_id") != stage_id:
                    errors.append(f"{path.relative_to(ROOT)}: stage_id mismatch")

        if item["state"] in {"machine_validated", "merged"}:
            if item["source_capture_status"] != "captured":
                errors.append(f"{work_id}: validated state without captured source")
            if item["pr_number"] is None:
                errors.append(f"{work_id}: validated state without PR number")

    return errors


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"INFO: validated {len(load_work_items()['items'])} work items")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
