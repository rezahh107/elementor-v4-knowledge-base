#!/usr/bin/env python3
"""Fail closed on cross-file EDIS, evidence, Work Item, and queue drift."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from tools.kb import COMPLETED, parse_front_matter
from tools.pipeline_common import (
    ROOT,
    load_stages,
    load_work_items,
    load_yaml,
    validate_instance,
)

QUEUE_PATH = ROOT / "planning" / "ROLLING_QUEUE.json"
ACTIVE_QUEUE_STATUSES = {"leased", "executing", "awaiting_external", "needs_review"}
OFFICIAL_HOSTS = {"elementor.com", "developers.elementor.com"}


def _official_https(url: Any) -> bool:
    if not isinstance(url, str):
        return False
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    return parsed.scheme == "https" and (
        host in OFFICIAL_HOSTS
        or any(host.endswith("." + allowed) for allowed in OFFICIAL_HOSTS)
    )


def _safe_repo_path(value: Any) -> Path | None:
    if not isinstance(value, str) or not value:
        return None
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        return None
    candidate = (ROOT / relative).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return None
    return candidate


def _capture_id(source_id: str, response_hash: str, canonical_url: str) -> str:
    payload = f"{source_id}\0{response_hash}\0{canonical_url}".encode("utf-8")
    return "CAP-" + hashlib.sha256(payload).hexdigest()


def document_alignment_errors(
    stage: dict[str, Any],
    front_matter: dict[str, Any],
) -> list[str]:
    """Return deterministic document/manifest drift diagnostics."""
    stage_id = stage["stage_id"]
    errors: list[str] = []

    for field in ("review_status", "provenance_status"):
        if field in front_matter and front_matter[field] != stage[field]:
            errors.append(
                f"{stage_id}: {field} mismatch between document "
                f"({front_matter[field]!r}) and canonical manifest ({stage[field]!r})"
            )

    migrated = (
        stage["review_status"] != "unreviewed"
        or stage["provenance_status"] != "document_level_legacy"
    )
    if migrated:
        for field in ("review_status", "provenance_status"):
            if field not in front_matter:
                errors.append(f"{stage_id}: migrated document must declare {field}")

    manifest_urls = [source["url"] for source in stage["sources"]]
    if "source_url" in front_matter:
        document_urls = [front_matter["source_url"]]
    elif "source_urls" in front_matter:
        document_urls = front_matter["source_urls"]
    else:
        document_urls = []
    if document_urls and document_urls != manifest_urls:
        errors.append(
            f"{stage_id}: document source URLs differ from canonical manifest: "
            f"document={document_urls!r}, manifest={manifest_urls!r}"
        )

    canonical_url = front_matter.get("canonical_url")
    if canonical_url is not None and not _official_https(canonical_url):
        errors.append(f"{stage_id}: document canonical_url is not an approved HTTPS URL")

    if stage["provenance_status"] == "claim_level":
        for field in ("claim_record", "source_record", "gap_record"):
            path = _safe_repo_path(front_matter.get(field))
            if path is None:
                errors.append(f"{stage_id}: claim-level document lacks a safe {field}")
            elif not path.is_file():
                errors.append(
                    f"{stage_id}: claim-level {field} does not exist: "
                    f"{path.relative_to(ROOT)}"
                )

    if stage["review_status"] == "peer_reviewed":
        path = _safe_repo_path(front_matter.get("review_record"))
        if path is None or not path.is_file():
            errors.append(
                f"{stage_id}: peer_reviewed requires an explicit repository review_record"
            )

    return errors


def source_record_binding_errors(
    stage_id: str,
    source: dict[str, Any],
    record: dict[str, Any],
) -> list[str]:
    """Return source-record-v3 binding and attestation diagnostics."""
    label = source["source_id"]
    errors = validate_instance(record, "source-record-v3.schema.json", label)

    expected = {
        "source_id": source["source_id"],
        "stage_id": stage_id,
        "source_type": source["source_type"],
    }
    for field, value in expected.items():
        if record.get(field) != value:
            errors.append(
                f"{label}: {field} mismatch: record={record.get(field)!r}, expected={value!r}"
            )

    requested = record.get("requested_url")
    canonical = record.get("canonical_url")
    if source.get("url") not in {requested, canonical}:
        errors.append(
            f"{label}: manifest URL must equal requested_url or canonical_url"
        )
    if not _official_https(requested) or not _official_https(canonical):
        errors.append(f"{label}: requested/canonical URL left the official HTTPS allowlist")

    chain = record.get("redirect_chain")
    if isinstance(chain, list) and chain:
        if chain[0] != requested:
            errors.append(f"{label}: redirect_chain must start at requested_url")
        if chain[-1] != canonical:
            errors.append(f"{label}: redirect_chain must end at canonical_url")

    response_hash = record.get("response_bytes_sha256")
    normalized_hash = record.get("normalized_document_sha256")
    if record.get("content_sha256") != response_hash:
        errors.append(f"{label}: content_sha256 must equal exact response_bytes_sha256")

    snapshot = record.get("snapshot")
    if isinstance(snapshot, dict):
        if snapshot.get("response_bytes_sha256") != response_hash:
            errors.append(f"{label}: snapshot response hash mismatch")
        if snapshot.get("normalized_document_sha256") != normalized_hash:
            errors.append(f"{label}: snapshot normalized hash mismatch")

    if isinstance(response_hash, str) and isinstance(canonical, str):
        expected_capture_id = _capture_id(source["source_id"], response_hash, canonical)
        if record.get("capture_id") != expected_capture_id:
            errors.append(f"{label}: capture_id is not bound to source, bytes, and canonical URL")

    if source.get("snapshot_status") == "captured":
        if source.get("content_fingerprint") != normalized_hash:
            errors.append(
                f"{label}: captured manifest fingerprint must equal normalized_document_sha256"
            )

    return errors


def queue_alignment_errors(
    queue: dict[str, Any],
    work_items: dict[str, Any],
) -> list[str]:
    """Return local queue/Work Item drift diagnostics without inventing GitHub state."""
    errors: list[str] = []
    items = {
        item["stage_id"]: item
        for item in work_items.get("items", [])
        if isinstance(item, dict) and isinstance(item.get("stage_id"), str)
    }
    active: list[str] = []

    for task in queue.get("tasks", []):
        if not isinstance(task, dict):
            continue
        task_id = task.get("id", "<unknown>")
        spec = task.get("spec") if isinstance(task.get("spec"), dict) else {}
        runtime = task.get("runtime") if isinstance(task.get("runtime"), dict) else {}
        status = runtime.get("status")
        if status in ACTIVE_QUEUE_STATUSES:
            active.append(str(task_id))
            if not isinstance(runtime.get("active_branch"), str):
                errors.append(f"{task_id}: active task lacks active_branch")
            if not isinstance(runtime.get("active_pr"), int):
                errors.append(f"{task_id}: active task lacks active_pr")

            stage_id = spec.get("stage_id")
            item = items.get(stage_id)
            if item is not None:
                branch = runtime.get("active_branch")
                pr_number = runtime.get("active_pr")
                if branch is not None and branch != item.get("branch"):
                    errors.append(
                        f"{task_id}: active_branch differs from Work Item {stage_id}"
                    )
                if pr_number is not None and pr_number != item.get("pr_number"):
                    errors.append(
                        f"{task_id}: active_pr differs from Work Item {stage_id}"
                    )

        if status == "completed" and runtime.get("lease") is not None:
            errors.append(f"{task_id}: completed task retains a lease")

    max_active = queue.get("controller_policy", {}).get("max_active_tasks", 1)
    if len(active) > max_active:
        errors.append(f"active queue tasks exceed max_active_tasks: {active}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    stages_document = load_stages()
    work_items = load_work_items()
    stages = {
        stage["stage_id"]: stage
        for stage in stages_document.get("stages", [])
        if isinstance(stage, dict) and isinstance(stage.get("stage_id"), str)
    }

    for stage in stages.values():
        if stage.get("status") not in COMPLETED:
            continue
        document_path = ROOT / stage["output_path"]
        try:
            front_matter, _ = parse_front_matter(document_path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{stage['stage_id']}: cannot read document front matter: {exc}")
            continue
        errors.extend(document_alignment_errors(stage, front_matter))

    for item in work_items.get("items", []):
        if not isinstance(item, dict):
            continue
        stage_id = item.get("stage_id")
        stage = stages.get(stage_id)
        if stage is None:
            continue
        needs_capture = item.get("source_capture_status") == "captured"
        validated_state = item.get("state") in {"machine_validated", "merged"}
        if not (needs_capture or validated_state):
            continue

        for source in stage["sources"]:
            path = ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml"
            if not path.is_file():
                errors.append(
                    f"{item['work_id']}: missing source record {path.relative_to(ROOT)}"
                )
                continue
            record = load_yaml(path)
            if not isinstance(record, dict):
                errors.append(f"{path.relative_to(ROOT)}: source record must be a mapping")
                continue
            errors.extend(source_record_binding_errors(stage_id, source, record))
            if validated_state and source.get("snapshot_status") != "captured":
                errors.append(
                    f"{item['work_id']}: validated state requires captured manifest source"
                )

    if QUEUE_PATH.is_file():
        try:
            queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"planning/ROLLING_QUEUE.json: cannot parse queue: {exc}")
        else:
            if isinstance(queue, dict):
                errors.extend(queue_alignment_errors(queue, work_items))
            else:
                errors.append("planning/ROLLING_QUEUE.json: queue must be an object")

    return sorted(set(errors))


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print("INFO: validated document, source-capture, Work Item, and queue bindings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
