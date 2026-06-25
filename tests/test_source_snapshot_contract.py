from __future__ import annotations

import hashlib

import pytest

import tools.source_capture as source_capture
import tools.stage_finalize as stage_finalize
from tools.pipeline_common import validate_instance


def test_official_canonical_url_aliases_are_versioned() -> None:
    assert source_capture.canonical_source_url(
        "SRC-KB-007-01", "https://elementor.com/help/create-a-query-in-a-loop-grid/"
    ) == "https://elementor.com/help/building-query-loop-grid/"
    assert source_capture.canonical_source_url(
        "SRC-KB-009-01", "https://elementor.com/help/pagination-for-loop/"
    ) == "https://elementor.com/help/paginate-loop/"
    assert source_capture.canonical_source_url(
        "SRC-KB-010-01", "https://elementor.com/help/taxonomy-filter/"
    ) == "https://elementor.com/help/taxonomy-filter-widget/"


def test_duplicate_alias_source_ids_are_rejected(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(source_capture, "ROOT", tmp_path)
    registry = tmp_path / "registries" / "source-url-aliases.yaml"
    registry.parent.mkdir(parents=True)
    registry.write_text(
        "schema_version: 1\naliases:\n"
        "- source_id: SRC-KB-007-01\n"
        "  legacy_urls: [https://elementor.com/help/a/]\n"
        "  canonical_url: https://elementor.com/help/b/\n"
        "  verification_state: verified_official_current_page\n"
        "- source_id: SRC-KB-007-01\n"
        "  legacy_urls: [https://elementor.com/help/c/]\n"
        "  canonical_url: https://elementor.com/help/d/\n"
        "  verification_state: verified_official_current_page\n",
        encoding="utf-8",
    )
    schemas = tmp_path / "schemas"
    schemas.mkdir()
    original_schema = source_capture.Path(__file__).resolve().parents[1] / "schemas" / "source-url-aliases.schema.json"
    (schemas / "source-url-aliases.schema.json").write_bytes(original_schema.read_bytes())
    with pytest.raises(ValueError, match="duplicate canonical URL alias"):
        source_capture._alias_registry()


def test_content_addressed_snapshot_paths_are_stable(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(source_capture, "ROOT", tmp_path)
    response_hash = "a" * 64
    normalized_hash = "b" * 64
    response, normalized = source_capture.content_addressed_paths(
        "SRC-KB-007-01", response_hash, normalized_hash, "text/html"
    )
    assert response.relative_to(tmp_path).as_posix() == (
        f"evidence/snapshots/SRC-KB-007-01/response-{response_hash}.html"
    )
    assert normalized.relative_to(tmp_path).as_posix() == (
        f"evidence/snapshots/SRC-KB-007-01/normalized-{normalized_hash}.txt"
    )


def test_immutable_snapshot_write_is_idempotent_and_collision_safe(
    tmp_path, monkeypatch
) -> None:
    monkeypatch.setattr(source_capture, "ROOT", tmp_path)
    path = tmp_path / "evidence" / "snapshots" / "SRC-KB-001-01" / "x"
    assert source_capture.write_immutable(path, b"same") is True
    assert source_capture.write_immutable(path, b"same") is False
    with pytest.raises(ValueError, match="snapshot collision"):
        source_capture.write_immutable(path, b"different")


def test_source_record_v3_requires_recoverable_snapshot_fields() -> None:
    record = {
        "schema_version": 3,
        "source_id": "SRC-KB-007-01",
        "stage_id": "KB-007",
        "source_type": "official_help",
        "requested_url": "https://elementor.com/help/create-a-query-in-a-loop-grid/",
        "canonical_url": "https://elementor.com/help/building-query-loop-grid/",
        "redirect_chain": [
            "https://elementor.com/help/create-a-query-in-a-loop-grid/",
            "https://elementor.com/help/building-query-loop-grid/",
        ],
        "retrieved_at": "2026-06-25T12:00:00+03:00",
        "http_status": 200,
        "content_type": "text/html",
        "charset": "utf-8",
        "content_length": 10,
        "etag": None,
        "last_modified": None,
        "page_title": "Build a query with the loop grid",
        "reported_last_updated": "2026-06-19",
        "content_sha256": "a" * 64,
        "response_bytes_sha256": "a" * 64,
        "normalized_document_sha256": "b" * 64,
        "parser_version": "html-text-v1",
        "image_evidence_ids": [],
        "discovered_image_urls": [],
        "notes": [],
    }
    errors = validate_instance(record, "source-record.schema.json", "fixture")
    assert any("response_snapshot_path" in error for error in errors)
    record.update(
        {
            "response_snapshot_path": "evidence/snapshots/SRC-KB-007-01/response-" + "a" * 64 + ".html",
            "normalized_snapshot_path": "evidence/snapshots/SRC-KB-007-01/normalized-" + "b" * 64 + ".txt",
            "snapshot_format_version": 1,
            "image_capture_status": "not_applicable",
            "missing_image_urls": [],
        }
    )
    assert validate_instance(record, "source-record.schema.json", "fixture") == []


def test_finalizer_detects_snapshot_tampering(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(stage_finalize, "ROOT", tmp_path)
    snapshot = tmp_path / "evidence" / "snapshots" / "SRC-KB-007-01" / ("normalized-" + "b" * 64 + ".txt")
    snapshot.parent.mkdir(parents=True)
    snapshot.write_bytes(b"original")
    record = {
        "normalized_snapshot_path": snapshot.relative_to(tmp_path).as_posix(),
        "normalized_document_sha256": hashlib.sha256(b"original").hexdigest(),
    }
    assert stage_finalize._validate_snapshot(
        record, "normalized_snapshot_path", "normalized_document_sha256", "fixture"
    ) == []
    snapshot.write_bytes(b"tampered")
    errors = stage_finalize._validate_snapshot(
        record, "normalized_snapshot_path", "normalized_document_sha256", "fixture"
    )
    assert any("does not match" in error for error in errors)


def test_snapshot_path_cannot_escape_evidence_directory(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(stage_finalize, "ROOT", tmp_path)
    with pytest.raises(ValueError, match="escapes evidence/snapshots"):
        stage_finalize._safe_snapshot_path("../outside.txt", "fixture")


def test_multi_source_image_inventory_may_be_a_stage_superset() -> None:
    assert stage_finalize._image_inventory_covers({"IMG-KB-015-001"}, {"IMG-KB-015-001", "IMG-KB-015-002"})
    assert not stage_finalize._image_inventory_covers({"IMG-KB-015-001"}, {"IMG-KB-015-002"})
