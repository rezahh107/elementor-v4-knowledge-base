#!/usr/bin/env python3
"""Finalize one evidence draft after snapshot, source, claim, and image validation."""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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


def _safe_snapshot_path(value: Any, label: str) -> Path | None:
    if not isinstance(value, str):
        return None
    path = (ROOT / value).resolve()
    snapshots_root = (ROOT / "evidence" / "snapshots").resolve()
    if path != snapshots_root and snapshots_root not in path.parents:
        raise ValueError(f"{label}: snapshot path escapes evidence/snapshots")
    return path


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _validate_snapshot(
    value: dict[str, Any], path_field: str, hash_field: str, label: str
) -> list[str]:
    errors: list[str] = []
    try:
        path = _safe_snapshot_path(value.get(path_field), label)
    except ValueError as exc:
        return [str(exc)]
    if path is None:
        return [f"{label}: missing {path_field}"]
    if not path.is_file():
        return [f"{label}: missing snapshot {path.relative_to(ROOT)}"]
    expected = value.get(hash_field)
    if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
        errors.append(f"{label}: invalid {hash_field}")
    elif _sha256(path) != expected:
        errors.append(f"{label}: {hash_field} does not match {path.relative_to(ROOT)}")
    return errors


def _image_inventory_covers(tracked: set[str], recorded: set[str]) -> bool:
    """Allow a stage-wide inventory while requiring every source-owned image."""
    return tracked.issubset(recorded)


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
    image_ids_by_source: dict[str, set[str]] = {}
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
                source_id = item.get("source_id")
                if isinstance(source_id, str):
                    image_ids_by_source.setdefault(source_id, set()).add(image_id)
            for supported in item.get("claims_supported", []):
                if supported not in claim_ids:
                    errors.append(f"{label}: unknown supported claim {supported}")
            must_be_recoverable = bool(item.get("claims_supported")) or (
                item.get("inspection_status") == "inspected"
            )
            if must_be_recoverable:
                if item.get("retrieval_status") != "retrieved":
                    errors.append(f"{label}: claim-bearing image must be retrieved")
                if item.get("snapshot_format_version") != 1:
                    errors.append(f"{label}: claim-bearing image lacks snapshot format v1")
                errors.extend(_validate_snapshot(item, "snapshot_path", "sha256", label))
                snapshot = _safe_snapshot_path(item.get("snapshot_path"), label)
                if snapshot and snapshot.is_file():
                    if item.get("content_length") != snapshot.stat().st_size:
                        errors.append(f"{label}: image content_length mismatch")

    for source in stage["sources"]:
        source_id = source["source_id"]
        path = ROOT / "evidence" / "sources" / f"{source_id}.yaml"
        label = str(path.relative_to(ROOT))
        if not path.exists():
            errors.append(f"{stage_id}: missing source record {label}")
            continue
        value = load_yaml(path)
        errors.extend(validate_instance(value, "source-record.schema.json", label))
        if value.get("stage_id") != stage_id:
            errors.append(f"{label}: stage_id mismatch")
        if value.get("schema_version") != 3:
            errors.append(f"{label}: finalization requires recoverable source record v3")
            continue
        if value.get("snapshot_format_version") != 1:
            errors.append(f"{label}: unsupported snapshot format")
        errors.extend(
            _validate_snapshot(
                value, "response_snapshot_path", "response_bytes_sha256", label
            )
        )
        errors.extend(
            _validate_snapshot(
                value,
                "normalized_snapshot_path",
                "normalized_document_sha256",
                label,
            )
        )
        tracked = image_ids_by_source.get(source_id, set())
        recorded = set(value.get("image_evidence_ids", []))
        if not _image_inventory_covers(tracked, recorded):
            errors.append(f"{label}: image_evidence_ids omit source-owned image records")
        if tracked:
            if value.get("image_capture_status") != "complete":
                errors.append(f"{label}: tracked image capture is incomplete")
            if value.get("missing_image_urls"):
                errors.append(f"{label}: missing_image_urls must be empty")
        elif value.get("image_capture_status") != "not_applicable":
            errors.append(f"{label}: image capture must be not_applicable without records")

    document_path = ROOT / stage["output_path"]
    if not document_path.exists():
        errors.append(f"{stage_id}: missing document {stage['output_path']}")
    return sorted(set(errors))


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
                "source and claim-bearing image snapshots were recovered and hash-verified",
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
