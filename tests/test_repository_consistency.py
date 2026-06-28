from __future__ import annotations

from tools.repository_consistency_validate import (
    _capture_id,
    document_alignment_errors,
    queue_alignment_errors,
    source_record_binding_errors,
    validate,
)


def test_registered_repository_cross_file_contracts() -> None:
    assert validate() == []


def test_document_trust_drift_is_rejected() -> None:
    stage = {
        "stage_id": "KB-004",
        "review_status": "unreviewed",
        "provenance_status": "document_level_legacy",
        "sources": [
            {
                "source_id": "SRC-KB-004-01",
                "url": "https://elementor.com/help/button-element/",
            }
        ],
    }
    front_matter = {
        "source_url": "https://elementor.com/help/button-element/",
        "review_status": "machine_validated",
        "provenance_status": "claim_level",
    }

    errors = document_alignment_errors(stage, front_matter)

    assert any("review_status mismatch" in error for error in errors)
    assert any("provenance_status mismatch" in error for error in errors)


def _valid_source_record() -> tuple[dict, dict]:
    response_hash = "a" * 64
    normalized_hash = "b" * 64
    canonical_url = "https://elementor.com/help/button-element/"
    source = {
        "source_id": "SRC-KB-004-01",
        "source_type": "official_help",
        "url": canonical_url,
        "snapshot_status": "captured",
        "content_fingerprint": normalized_hash,
    }
    record = {
        "schema_version": 3,
        "source_id": source["source_id"],
        "stage_id": "KB-004",
        "source_type": source["source_type"],
        "requested_url": canonical_url,
        "canonical_url": canonical_url,
        "redirect_chain": [canonical_url],
        "redirect_chain_complete": True,
        "retrieved_at": "2026-06-28T08:00:00+03:00",
        "http_status": 200,
        "content_type": "text/html",
        "charset": "utf-8",
        "content_length": 1024,
        "etag": None,
        "last_modified": None,
        "page_title": "Button element | Elementor",
        "page_title_source": "html_title",
        "reported_last_updated": None,
        "reported_last_updated_source": "unavailable",
        "reported_last_updated_hint": None,
        "content_sha256": response_hash,
        "response_bytes_sha256": response_hash,
        "normalized_document_sha256": normalized_hash,
        "parser_version": "html-text-v2",
        "source_locator_version": 2,
        "capture_id": _capture_id(source["source_id"], response_hash, canonical_url),
        "snapshot": {
            "storage": "local_ephemeral",
            "artifact_name": "source-snapshot-KB-004-local",
            "relative_path": f"source-snapshots/{source['source_id']}/{response_hash}.bin",
            "run_id": None,
            "response_bytes_sha256": response_hash,
            "normalized_document_sha256": normalized_hash,
        },
        "image_evidence_ids": [],
        "discovered_image_urls": [],
        "notes": [],
    }
    return source, record


def test_source_record_snapshot_tampering_is_rejected() -> None:
    source, record = _valid_source_record()
    assert source_record_binding_errors("KB-004", source, record) == []

    record["snapshot"]["normalized_document_sha256"] = "c" * 64
    errors = source_record_binding_errors("KB-004", source, record)

    assert any("snapshot normalized hash mismatch" in error for error in errors)


def test_active_queue_task_must_match_work_item() -> None:
    queue = {
        "controller_policy": {"max_active_tasks": 1},
        "tasks": [
            {
                "id": "RQ-0004",
                "spec": {"stage_id": "KB-004"},
                "runtime": {
                    "status": "executing",
                    "active_branch": "migration/KB-004-wrong",
                    "active_pr": 99,
                    "lease": None,
                },
            }
        ],
    }
    work_items = {
        "items": [
            {
                "stage_id": "KB-004",
                "branch": "migration/KB-004-rq0004-finalize",
                "pr_number": 25,
            }
        ]
    }

    errors = queue_alignment_errors(queue, work_items)

    assert any("active_branch differs" in error for error in errors)
    assert any("active_pr differs" in error for error in errors)
