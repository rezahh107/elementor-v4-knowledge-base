from __future__ import annotations

import copy
from pathlib import Path

import tools.bind_claim_locators as binder
from tools.source_capture import locator_fingerprint


def test_bind_claim_file_upgrades_documented_locators(monkeypatch, tmp_path: Path) -> None:
    claim_path = tmp_path / "KB-004-button.yaml"
    claim_path.write_text(
        "claims:\n"
        "- claim_id: KB-004-C001\n"
        "  stage_id: KB-004\n"
        "  claim_text: Documented statement\n"
        "  evidence_state: documented\n"
        "  source_locators:\n"
        "  - source_id: SRC-KB-004-01\n"
        "    locator: official page lines 1-2\n"
        "  derived_from: []\n"
        "  verification_status: machine_validated\n"
        "- claim_id: KB-004-C002\n"
        "  stage_id: KB-004\n"
        "  claim_text: Derived statement\n"
        "  evidence_state: derived\n"
        "  source_locators: []\n"
        "  derived_from:\n"
        "  - KB-004-C001\n"
        "  verification_status: machine_validated\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(binder, "ROOT", tmp_path)

    changed = binder.bind_claim_file(
        claim_path,
        {
            "SRC-KB-004-01": {
                "snapshot_sha256": "a" * 64,
                "normalized_document_sha256": "b" * 64,
            }
        },
    )

    assert changed is True
    text = claim_path.read_text(encoding="utf-8")
    expected_fingerprint = locator_fingerprint(
        source_id="SRC-KB-004-01",
        locator="official page lines 1-2",
        snapshot_sha256="a" * 64,
        normalized_document_sha256="b" * 64,
    )
    assert "locator_version: 2" in text
    assert f"locator_fingerprint: {expected_fingerprint}" in text
    assert "evidence_state: derived\n  source_locators: []" in text


def test_bind_claim_file_is_idempotent(monkeypatch, tmp_path: Path) -> None:
    locator = "official page lines 1-2"
    expected = {
        "source_id": "SRC-KB-004-01",
        "locator": locator,
        "locator_version": 2,
        "snapshot_sha256": "a" * 64,
        "normalized_document_sha256": "b" * 64,
        "locator_fingerprint": locator_fingerprint(
            source_id="SRC-KB-004-01",
            locator=locator,
            snapshot_sha256="a" * 64,
            normalized_document_sha256="b" * 64,
        ),
    }
    document = {
        "claims": [
            {
                "claim_id": "KB-004-C001",
                "stage_id": "KB-004",
                "claim_text": "Documented statement",
                "evidence_state": "documented",
                "source_locators": [copy.deepcopy(expected)],
                "derived_from": [],
                "verification_status": "machine_validated",
            }
        ]
    }
    claim_path = tmp_path / "KB-004-button.yaml"
    claim_path.write_text(binder.dump_yaml(document), encoding="utf-8")
    before = claim_path.read_text(encoding="utf-8")
    monkeypatch.setattr(binder, "ROOT", tmp_path)

    changed = binder.bind_claim_file(
        claim_path,
        {
            "SRC-KB-004-01": {
                "snapshot_sha256": "a" * 64,
                "normalized_document_sha256": "b" * 64,
            }
        },
    )

    assert changed is False
    assert claim_path.read_text(encoding="utf-8") == before
