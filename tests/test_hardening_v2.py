from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools.evidence_graph import claim_graph_errors
from tools.ledger_chain import append_chained_event, event_sha256
from tools.pipeline_common import canonical_json_line
from tools.source_capture import SOURCE_LOCATOR_VERSION, commit_payloads_atomically, locator_fingerprint

ROOT = Path(__file__).resolve().parents[1]


def test_claim_graph_rejects_cycles_and_ungrounded_parents() -> None:
    claims = {
        "KB-004-C001": {
            "evidence_state": "derived",
            "derived_from": ["KB-004-C002"],
        },
        "KB-004-C002": {
            "evidence_state": "derived",
            "derived_from": ["KB-004-C001", "KB-004-C003"],
        },
        "KB-004-C003": {
            "evidence_state": "insufficient_evidence",
            "derived_from": [],
        },
    }

    errors = claim_graph_errors(claims)

    assert "derived claim cycle: KB-004-C001 -> KB-004-C002 -> KB-004-C001" in errors
    assert "KB-004-C002: derived_from claim KB-004-C003 is not grounded" in errors


def test_claim_schema_requires_snapshot_binding_for_documented_claim() -> None:
    schema = json.loads((ROOT / "schemas" / "claim.schema.json").read_text(encoding="utf-8"))
    claim = {
        "claim_id": "KB-004-C001",
        "stage_id": "KB-004",
        "claim_text": "Documented statement",
        "evidence_state": "documented",
        "source_locators": [],
        "derived_from": [],
        "verification_status": "unreviewed",
    }

    errors = list(Draft202012Validator(schema).iter_errors(claim))

    assert errors


def test_image_v2_requires_retrieved_inspected_bytes() -> None:
    schema = json.loads(
        (ROOT / "schemas" / "image-evidence-v2.schema.json").read_text(encoding="utf-8")
    )
    image = {
        "image_id": "IMG-KB-004-001",
        "stage_id": "KB-004",
        "source_id": "SRC-KB-004-01",
        "url": "https://elementor.com/image.png",
        "retrieval_status": "cache_miss",
        "inspection_status": "inspected",
        "sha256": None,
        "claims_supported": [],
        "notes": [],
    }

    errors = list(Draft202012Validator(schema).iter_errors(image))

    assert errors


def test_source_v3_requires_immutable_snapshot_metadata() -> None:
    schema = json.loads(
        (ROOT / "schemas" / "source-record-v3.schema.json").read_text(encoding="utf-8")
    )
    record = {"schema_version": 3}

    errors = list(Draft202012Validator(schema).iter_errors(record))

    assert errors
    assert any("snapshot" in error.message for error in errors)


def test_source_v3_snapshot_records_normalized_hash() -> None:
    schema = json.loads(
        (ROOT / "schemas" / "source-record-v3.schema.json").read_text(encoding="utf-8")
    )
    record = {
        "schema_version": 3,
        "source_id": "SRC-KB-004-01",
        "stage_id": "KB-004",
        "source_type": "official_help",
        "requested_url": "https://elementor.com/help/button-element/",
        "canonical_url": "https://elementor.com/help/button-element/",
        "redirect_chain": ["https://elementor.com/help/button-element/"],
        "redirect_chain_complete": True,
        "retrieved_at": "2026-06-27T12:00:00+03:00",
        "http_status": 200,
        "content_type": "text/html",
        "charset": "utf-8",
        "content_length": 1000,
        "etag": None,
        "last_modified": None,
        "page_title": "Button element | Elementor",
        "page_title_source": "html_title",
        "reported_last_updated": "2025-07-01",
        "reported_last_updated_source": "http_last_modified",
        "reported_last_updated_hint": "2025-07-01",
        "content_sha256": "a" * 64,
        "response_bytes_sha256": "a" * 64,
        "normalized_document_sha256": "b" * 64,
        "parser_version": "html-text-v2",
        "source_locator_version": SOURCE_LOCATOR_VERSION,
        "capture_id": "CAP-" + "c" * 64,
        "snapshot": {
            "storage": "local_ephemeral",
            "artifact_name": "source-snapshot-KB-004-local",
            "relative_path": "source-snapshots/SRC-KB-004-01/" + "a" * 64 + ".bin",
            "run_id": None,
            "response_bytes_sha256": "a" * 64,
            "normalized_document_sha256": "b" * 64,
        },
        "image_evidence_ids": [],
        "discovered_image_urls": [],
        "notes": [],
    }

    assert not list(Draft202012Validator(schema).iter_errors(record))


def test_locator_v2_fingerprint_depends_on_snapshot_and_normalized_hash() -> None:
    first = locator_fingerprint(
        source_id="SRC-KB-004-01",
        locator="official page lines 1-2",
        snapshot_sha256="a" * 64,
        normalized_document_sha256="b" * 64,
    )
    changed_snapshot = locator_fingerprint(
        source_id="SRC-KB-004-01",
        locator="official page lines 1-2",
        snapshot_sha256="c" * 64,
        normalized_document_sha256="b" * 64,
    )
    changed_normalized = locator_fingerprint(
        source_id="SRC-KB-004-01",
        locator="official page lines 1-2",
        snapshot_sha256="a" * 64,
        normalized_document_sha256="d" * 64,
    )

    assert len(first) == 64
    assert first != changed_snapshot
    assert first != changed_normalized


def test_execution_chain_detects_tampering(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    event = {
        "event_id": "event-0001",
        "stage_id": "KB-004",
        "event_type": "completed_with_gaps",
        "status": "completed_with_gaps",
        "recorded_at": "2026-06-26T12:00:00+03:00",
        "content_commit_sha": "1" * 40,
        "finalization_commit_sha": "2" * 40,
        "output_path": "docs/elements/v4/button.md",
        "notes": [],
    }
    appended = append_chained_event(
        path=path,
        event=event,
        version_field="ledger_version",
        canonical=canonical_json_line,
        validate=lambda value: [],
    )
    tampered = copy.deepcopy(appended)
    tampered["notes"] = ["changed"]

    assert tampered["event_sha256"] != event_sha256(tampered, canonical_json_line)


def test_transactional_capture_rolls_back_partial_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first = tmp_path / "first"
    second = tmp_path / "second"
    first.write_bytes(b"original")
    real_write = __import__("tools.source_capture", fromlist=["_atomic_write_bytes"])._atomic_write_bytes
    calls = 0

    def fail_second(path: Path, data: bytes) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("synthetic write failure")
        real_write(path, data)

    monkeypatch.setattr("tools.source_capture._atomic_write_bytes", fail_second)
    with pytest.raises(OSError, match="synthetic write failure"):
        commit_payloads_atomically({first: b"new", second: b"new"})

    assert first.read_bytes() == b"original"
    assert not second.exists()


def test_workflows_pin_actions_and_separate_writeback() -> None:
    workflows = [
        ROOT / ".github" / "workflows" / "kb-quality.yml",
        ROOT / ".github" / "workflows" / "capture-source.yml",
        ROOT / ".github" / "workflows" / "finalize-stage.yml",
    ]
    for path in workflows:
        text = path.read_text(encoding="utf-8")
        assert "actions/checkout@v" not in text
        assert "actions/setup-python@v" not in text
    capture = workflows[1].read_text(encoding="utf-8")
    finalize = workflows[2].read_text(encoding="utf-8")
    assert "pull_request_target:" in capture
    assert "pull_request_target:" in finalize
    assert "contents: write" in capture
    assert "contents: write" in finalize
    assert "python tools/source_capture.py" not in capture.split("writeback:", 1)[1]
    assert "python tools/stage_finalize.py" not in finalize.split("writeback:", 1)[1]
    assert "python -I" in finalize
