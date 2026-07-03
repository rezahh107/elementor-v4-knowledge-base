#!/usr/bin/env python3
"""Bind documented claim locators to captured source snapshots.

This tool upgrades documented claim locators to the current locator v2 contract by
copying immutable snapshot hashes from the source record and computing the
locator fingerprint with the same primitive used by evidence validation.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from tools.pipeline_common import ROOT, dump_yaml, find_stage, load_stages, load_yaml
from tools.source_capture import SOURCE_LOCATOR_VERSION, locator_fingerprint


CLAIMS_DIR = ROOT / "evidence" / "claims"
SOURCES_DIR = ROOT / "evidence" / "sources"


def _source_bindings(stage_id: str) -> dict[str, dict[str, str]]:
    stage = find_stage(load_stages(), stage_id)
    bindings: dict[str, dict[str, str]] = {}
    for source in stage["sources"]:
        source_id = source["source_id"]
        record_path = SOURCES_DIR / f"{source_id}.yaml"
        if not record_path.exists():
            raise FileNotFoundError(f"missing source record: {record_path.relative_to(ROOT)}")
        record = load_yaml(record_path)
        if not isinstance(record, dict):
            raise ValueError(f"source record is not a mapping: {record_path.relative_to(ROOT)}")
        response_hash = record.get("response_bytes_sha256")
        normalized_hash = record.get("normalized_document_sha256")
        if not isinstance(response_hash, str) or not isinstance(normalized_hash, str):
            raise ValueError(f"source record lacks immutable hashes: {record_path.relative_to(ROOT)}")
        bindings[source_id] = {
            "snapshot_sha256": response_hash,
            "normalized_document_sha256": normalized_hash,
        }
    return bindings


def bind_claim_file(path: Path, bindings: dict[str, dict[str, str]]) -> bool:
    document = load_yaml(path)
    if not isinstance(document, dict) or not isinstance(document.get("claims"), list):
        raise ValueError(f"claim file must contain a claims list: {path.relative_to(ROOT)}")

    changed = False
    for claim in document["claims"]:
        if not isinstance(claim, dict) or claim.get("evidence_state") != "documented":
            continue
        locators = claim.get("source_locators")
        if not isinstance(locators, list):
            raise ValueError(f"claim has invalid source_locators: {claim.get('claim_id')}")
        for locator in locators:
            if not isinstance(locator, dict):
                raise ValueError(f"claim has non-mapping locator: {claim.get('claim_id')}")
            source_id = locator.get("source_id")
            text = locator.get("locator")
            if not isinstance(source_id, str) or not isinstance(text, str):
                raise ValueError(f"claim locator lacks source_id or locator text: {claim.get('claim_id')}")
            binding = bindings.get(source_id)
            if binding is None:
                raise ValueError(f"unknown source_id {source_id!r} in {claim.get('claim_id')}")
            expected = {
                "source_id": source_id,
                "locator": text,
                "locator_version": SOURCE_LOCATOR_VERSION,
                "snapshot_sha256": binding["snapshot_sha256"],
                "normalized_document_sha256": binding["normalized_document_sha256"],
                "locator_fingerprint": locator_fingerprint(
                    source_id=source_id,
                    locator=text,
                    snapshot_sha256=binding["snapshot_sha256"],
                    normalized_document_sha256=binding["normalized_document_sha256"],
                ),
            }
            if locator != expected:
                locator.clear()
                locator.update(expected)
                changed = True

    if changed:
        path.write_text(dump_yaml(document), encoding="utf-8", newline="\n")
    return changed


def bind_stage(stage_id: str) -> list[Path]:
    bindings = _source_bindings(stage_id)
    changed: list[Path] = []
    for path in sorted(CLAIMS_DIR.glob(f"{stage_id}*.yaml")):
        if bind_claim_file(path, bindings):
            changed.append(path)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Bind documented claim locators to source snapshots")
    parser.add_argument("stage_id", help="Stage id such as KB-004")
    parser.add_argument("--check", action="store_true", help="Fail if files would change")
    args = parser.parse_args()

    changed = bind_stage(args.stage_id)
    if args.check and changed:
        for path in changed:
            print(f"would update {path.relative_to(ROOT)}")
        return 1
    for path in changed:
        print(f"updated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
