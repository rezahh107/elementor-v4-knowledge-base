from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools.evidence_graph import claim_graph_errors
from tools.ledger_chain import append_chained_event, event_sha256
from tools.pipeline_common import canonical_json_line
from tools.source_capture import commit_payloads_atomically

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
