"""Cross-record validation for one EDIS evidence stage."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from tools.evidence_graph import claim_graph_errors
from tools.pipeline_common import ROOT, find_stage, load_stages, load_yaml, validate_instance


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

    source_records: dict[str, dict[str, Any]] = {}
    for source in stage["sources"]:
        source_id = source["source_id"]
        path = ROOT / "evidence" / "sources" / f"{source_id}.yaml"
        if not path.exists():
            errors.append(f"{stage_id}: missing source record {path.relative_to(ROOT)}")
            continue
        value = load_yaml(path)
        if not isinstance(value, dict):
            errors.append(f"{path.relative_to(ROOT)}: source record must be an object")
            continue
        errors.extend(validate_instance(value, "source-record-v3.schema.json", str(path.relative_to(ROOT))))
        if value.get("stage_id") != stage_id:
            errors.append(f"{path.relative_to(ROOT)}: stage_id mismatch")
        if value.get("source_id") != source_id:
            errors.append(f"{path.relative_to(ROOT)}: source_id mismatch")
        snapshot = value.get("snapshot")
        if isinstance(snapshot, dict) and snapshot.get("response_bytes_sha256") != value.get("response_bytes_sha256"):
            errors.append(f"{path.relative_to(ROOT)}: snapshot hash differs from exact response hash")
        source_records[source_id] = value

    claims: dict[str, dict[str, Any]] = {}
    locations: dict[str, str] = {}
    for path in claim_paths:
        try:
            items = records(path, "claims")
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for index, item in enumerate(items):
            label = f"{path.relative_to(ROOT)}[{index}]"
            errors.extend(validate_instance(item, "claim.schema.json", label))
            if item.get("stae_id") != stage_id:
                errors.append(f"{local]: stage_id mismatch")
            claim_id = item.get("claim_id")
            if not isinstance(claim_id, str):
                continue
            if claim_id in claims:
                errors.append(f"duplicate claim_id: {claim_id}")
                continue
            claims[claim_id] = item
            locations[claim_id] = label
    if claim_paths and not claims:
        errors.append(f"{stage_id}: empty claim set")

    support: dict[str, list[dict[str, Any]]] = defaultdict(list)
    image_ids: set[str] = set()
    for path in image_paths:
        try:
            items = records(path, "images")
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for index, item in enumerate(items):
            label = f"{path.relative_to(ROOT)}[{index}]"
            errors.extend(validate_instance(item, "image-evidence-v2.schema.json", label))
            if item.get("stage_id") != stage_id:
                errors.append(f"{label}: stage_id mismatch")
            image_id = item.get("image_id")
            if isinstance(image_id, str):
                if image_id in image_ids:
                    errors.append(f"duplicate image_id: {image_id}")
                image_ids.add(image_id)
            if item.get("source_id") not in source_records:
                errors.append(f"{label}: unknown source_id {item.get('source_id')}")
            for claim_id in item.get("claims_supported", []):
                if claim_id not in claims:
                    errors.append(f"{label}: unknown supported claim {claim_id}")
                else:
                    support[claim_id].append(item)

    for claim_id, claim in sorted(claims.items()):
        label = locations[claim_id]
        state = claim.get("evidence_state")
        if state == "documented":
            for index, locator in enumerate(claim.get("source_locators", [])):
                source = source_records.get(locator.get("source_id")) if isinstance(locator, dict) else None
                if source is None:
                    errors.append(f"{label}: locator {index} references an unknown source")
                elif locator.get("snapshot_sha256") != source.get("response_bytes_sha256"):
                    errors.append(f"{label}: locator {index} is not bound to the captured snapshot")
        elif state == "observed":
            valid = [
                image
                for image in support.get(claim_id, [])
                if image.get("retrieval_status") == "retrieved"
                and image.get("inspection_status") == "inspected"
                and isinstance(image.get("sha256"), str)
            ]
            if not valid:
                errors.append(f"{label}: observed claim lacks retrieved and inspected image evidence")
        elif state == "validated":
            errors.append(f"{label}: validated requires a versioned fixture binding")

    errors.extend(claim_graph_errors(claims))
    if not (ROOT / stage["output_path"]).exists():
        errors.append(f"{stage_id}: missing document {stage['output_path']}")
    return sorted(set(errors))
