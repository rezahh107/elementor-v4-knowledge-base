#!/usr/bin/env python3
"""Capture official source evidence without transport-only repository churn."""
from __future__ import annotations

import argparse
import os
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Callable

from tools import source_capture_legacy as legacy
from tools.pipeline_common import (
    ROOT,
    dump_yaml,
    find_stage,
    find_work_item,
    load_stages,
    load_work_items,
    load_yaml,
    now_istanbul,
)
from tools.source_contract import semantic_capture_equal

MAX_RESPONSE_BYTES = legacy.MAX_RESPONSE_BYTES
PARSER_VERSION = legacy.PARSER_VERSION
SOURCE_LOCATOR_VERSION = legacy.SOURCE_LOCATOR_VERSION
USER_AGENT = legacy.USER_AGENT
ALLOWED_HOSTS = legacy.ALLOWED_HOSTS
DEFAULT_ARTIFACT_DIR = legacy.DEFAULT_ARTIFACT_DIR
TextParser = legacy.TextParser
TrackingRedirectHandler = legacy.TrackingRedirectHandler
official_url = legacy.official_url
event_pr_number = legacy.event_pr_number
image_ids = legacy.image_ids
fetch = legacy.fetch
locator_fingerprint = legacy.locator_fingerprint
build_record = legacy.build_record
_http_last_updated = legacy._http_last_updated
_capture_id = legacy._capture_id
_atomic_write_bytes = legacy._atomic_write_bytes
_same_capture = semantic_capture_equal


def commit_payloads_atomically(payloads: dict[Path, bytes]) -> None:
    """Delegate publication while preserving the patchable rollback primitive."""
    original = legacy._atomic_write_bytes
    legacy._atomic_write_bytes = _atomic_write_bytes
    try:
        legacy.commit_payloads_atomically(payloads)
    finally:
        legacy._atomic_write_bytes = original


def _publish_record(existing: Any, candidate: dict[str, Any]) -> bool:
    return not semantic_capture_equal(existing, candidate)


def _update_work_item(item: dict[str, Any], semantic_changed: bool) -> bool:
    return (
        semantic_changed
        or item.get("source_capture_status") != "captured"
        or item.get("last_error") is not None
    )


def _publish_failure(original_status: Any) -> bool:
    return original_status not in {"captured", "failed"}


def capture(
    stage_id: str,
    *,
    artifact_dir: Path = DEFAULT_ARTIFACT_DIR,
    fetcher: Callable[[str], tuple[bytes, Any, str, int, list[str]]] = fetch,
) -> int:
    """Capture exact bytes while publishing only reusable semantic truth."""
    stages = load_stages()
    work_items = load_work_items()
    stage = find_stage(stages, stage_id)
    work_item = find_work_item(work_items, stage_id)
    original_status = work_item.get("source_capture_status")
    captured_at = now_istanbul()

    try:
        payloads: dict[Path, bytes] = {}
        semantic_changed = False
        for source in stage["sources"]:
            raw, headers, final_url, status, redirects = fetcher(source["url"])
            candidate, snapshot_path, snapshot_bytes = build_record(
                stage=stage,
                source=source,
                raw=raw,
                headers=headers,
                final_url=final_url,
                status=status,
                redirect_chain=redirects,
                captured_at=captured_at,
                artifact_dir=artifact_dir,
            )
            record_path = ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml"
            existing = load_yaml(record_path) if record_path.exists() else None
            if _publish_record(existing, candidate):
                payloads[record_path] = dump_yaml(candidate).encode("utf-8")
                semantic_changed = True
            payloads[snapshot_path] = snapshot_bytes

        if _update_work_item(work_item, semantic_changed):
            pr_number = event_pr_number()
            if pr_number is not None:
                work_item["pr_number"] = pr_number
            target_head = os.environ.get("TARGET_HEAD_SHA")
            if target_head:
                work_item["expected_head_sha"] = target_head
                work_item["github_state_observed_at"] = captured_at
            work_item["source_capture_status"] = "captured"
            work_item["updated_at"] = captured_at
            work_item["last_error"] = None
            payloads[ROOT / "manifests" / "work-items.yaml"] = dump_yaml(work_items).encode("utf-8")

        commit_payloads_atomically(payloads)
    except Exception as exc:
        if _publish_failure(original_status):
            failed = deepcopy(work_items)
            failed_item = find_work_item(failed, stage_id)
            failed_item["source_capture_status"] = "failed"
            failed_item["updated_at"] = now_istanbul()
            failed_item["last_error"] = str(exc)
            commit_payloads_atomically(
                {ROOT / "manifests" / "work-items.yaml": dump_yaml(failed).encode("utf-8")}
            )
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if semantic_changed:
        print(f"captured new semantic source evidence for {stage_id}")
    else:
        print(f"source semantics unchanged for {stage_id}; repository truth was not churned")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True)
    parser.add_argument("--artifact-dir", type=Path, default=DEFAULT_ARTIFACT_DIR)
    args = parser.parse_args()
    return capture(args.stage, artifact_dir=args.artifact_dir)


if __name__ == "__main__":
    raise SystemExit(main())
