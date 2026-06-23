#!/usr/bin/env python3
"""Finalize one evidence draft after source and record validation."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from tools.pipeline_common import (
    ROOT,
    append_ledger_event,
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

SHA256_RE = re.compile(r"^[a-f0-9]{64}$")


def records(path: Path, key: str) -> list[dict[str, Any]]:
    value = load_yaml(path)
    result = value.get(key) if isinstance(value, dict) else value
    if not isinstance(result, list) or not all(isinstance(item, dict) for item in result):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a {key} list")
    return result


def validate_evidence(stage_id: str) -> list[str]:
    errors: list[str] = []
    stage = find_stage(load_stages(), stage_id)
    claim_paths = sorted((ROOT / "evidence" / "claims").glob(f"{stage_id}*.yaml"))
    image_paths = sorted((ROOT / "evidence" / "images").glob(f"{stage_id}*.yaml"))
    if not claim_paths:
        errors.append(f"{stage_id}: no claim file")
    if not image_paths:
        errors.append(f"{stage_id}: no image evidence file")

    claim_count = 0
    claim_ids: set[str] = set()
    for path in claim_paths:
        try:
            items = records(path, "claims")
        except ValueError as exc:
            errors.append(str(exc))
            continue
        claim_count += len(items)
        for index, item in enumerate(items):
            label = f"{path.relative_to(ROOT)}[{index}]"
            errors.extend(validate_instance(item, "claim.schema.json", label))
            if item.get("stage_id") != stage_id:
                errors.append(f"{label}: stage_id mismatch")
            claim_id = item.get("claim_id")
            if claim_id in claim_ids:
                errors.append(f"duplicate claim_id: {claim_id}")
            if isinstance(claim_id, str):
                claim_ids.add(claim_id)
    if claim_paths and claim_count == 0:
        errors.append(f"{stage_id}: empty claim set")

    image_ids: set[str] = set()
    for path in image_paths:
        try:
            items = records(path, "images")
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for index, item in enumerate(items):
            label = f"{path.relative_to(ROOT)}[{index}]"
            errors.extend(validate_instance(item, "image-evidence.schema.json", label))
            if item.get("stage_id") != stage_id:
                errors.append(f"{label}: stage_id mismatch")
            image_id = item.get("image_id")
            if image_id in image_ids:
                errors.append(f"duplicate image_id: {image_id}")
            if isinstance(image_id, str):
                image_ids.add(image_id)
            for supported in item.get("claims_supported", []):
                if supported not in claim_ids:
                    errors.append(f"{label}: unknown supported claim {supported}")
            if item.get("inspection_status") == "inspected" and item.get("retrieval_status") != "retrieved":
                errors.append(f"{label}: inspected image must be retrieved")

    for source in stage["sources"]:
        path = ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml"
        if not path.exists():
            errors.append(f"{stage_id}: missing source record {path.relative_to(ROOT)}")
            continue
        value = load_yaml(path)
        errors.extend(validate_instance(value, "source-record.schema.json", str(path.relative_to(ROOT))))
        if value.get("stage_id") != stage_id:
            errors.append(f"{path.relative_to(ROOT)}: stage_id mismatch")
        if not SHA256_RE.fullmatch(str(value.get("response_bytes_sha256", ""))):
            errors.append(f"{path.relative_to(ROOT)}: invalid response byte hash")

    document_path = ROOT / stage["output_path"]
    if not document_path.exists():
        errors.append(f"{stage_id}: missing document {stage['output_path']}")
    return errors


def head_sha() -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def finalize(stage_id: str) -> int:
    errors = validate_evidence(stage_id)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    stages = load_stages()
    work_items = load_work_items()
    stage = find_stage(stages, stage_id)
    item = find_work_item(work_items, stage_id)
    if item["source_capture_status"] != "captured":
        print(f"ERROR: {stage_id}: source capture not complete", file=sys.stderr)
        return 1
    if item["state"] == "evidence_draft":
        transition(item, "finalization_pending")
    if item["state"] in {"finalization_pending", "ci_failed"}:
        transition(item, "ci_running")
    elif item["state"] != "ci_running":
        print(f"ERROR: {stage_id}: cannot finalize from {item['state']}", file=sys.stderr)
        return 1

    content_sha = head_sha()
    completed_at = now_istanbul()
    for source in stage["sources"]:
        value = load_yaml(ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml")
        source["url"] = value["canonical_url"]
        source["snapshot_status"] = "captured"
        source["content_fingerprint"] = value["normalized_document_sha256"]
    stage["provenance_status"] = "claim_level"
    stage["review_status"] = "machine_validated"
    stage["content_commit_sha"] = content_sha
    stage["completed_at"] = completed_at
    transition(item, "machine_validated")

    write_yaml(ROOT / "manifests" / "stages.yaml", stages)
    write_yaml(ROOT / "manifests" / "work-items.yaml", work_items)
    append_ledger_event(
        {
            "event_id": f"{item['cycle_id']}:{stage_id}:machine-validated:{content_sha[:12]}",
            "stage_id": stage_id,
            "event_type": stage["status"],
            "status": stage["status"],
            "recorded_at": completed_at,
            "content_commit_sha": content_sha,
            "output_path": stage["output_path"],
            "notes": [
                "source bytes and normalized text were hashed by GitHub Actions",
                "claim and image records passed schema validation",
                "review_status is machine_validated and not peer_reviewed",
            ],
        }
    )
    print(f"finalized {stage_id} at {content_sha}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True)
    return finalize(parser.parse_args().stage)


if __name__ == "__main__":
    raise SystemExit(main())
