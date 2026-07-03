from __future__ import annotations

from tools.stage_finalize_v2 import reconcile_gap_records
from tools.work_item_validate import finalization_alignment_errors


def test_reconcile_gap_records_resolves_legacy_and_binds_current_gaps() -> None:
    stage = {
        "stage_id": "KB-004",
        "gap_ids": [
            "GAP-KB-004-PROVENANCE",
            "GAP-KB-004-SNAPSHOT",
            "GAP-KB-004-REVIEW",
        ],
    }
    global_document = {
        "schema_version": 1,
        "gaps": [
            {
                "gap_id": "GAP-KB-004-PROVENANCE",
                "stage_id": "KB-004",
                "status": "open",
            },
            {
                "gap_id": "GAP-KB-004-SNAPSHOT",
                "stage_id": "KB-004",
                "status": "open",
            },
            {
                "gap_id": "GAP-KB-004-REVIEW",
                "stage_id": "KB-004",
                "status": "open",
                "title": "legacy review record",
            },
        ],
    }
    local_review = {
        "gap_id": "GAP-KB-004-REVIEW",
        "stage_id": "KB-004",
        "status": "open",
        "title": "Human review pending",
    }
    local_image = {
        "gap_id": "GAP-KB-004-IMAGE-INSPECTION",
        "stage_id": "KB-004",
        "status": "open",
        "title": "Image inspection pending",
    }
    local_document = {
        "schema_version": 1,
        "gaps": [local_image, local_review],
    }

    reconcile_gap_records("KB-004", stage, global_document, local_document)

    by_id = {record["gap_id"]: record for record in global_document["gaps"]}
    assert by_id["GAP-KB-004-PROVENANCE"]["status"] == "resolved"
    assert by_id["GAP-KB-004-SNAPSHOT"]["status"] == "resolved"
    assert by_id["GAP-KB-004-REVIEW"] == local_review
    assert by_id["GAP-KB-004-IMAGE-INSPECTION"] == local_image
    assert stage["gap_ids"] == [
        "GAP-KB-004-IMAGE-INSPECTION",
        "GAP-KB-004-REVIEW",
    ]


def test_finalization_pending_rejects_already_finalized_stage() -> None:
    item = {
        "work_id": "migration-cycle-01:KB-004",
        "state": "finalization_pending",
    }
    stage = {
        "stage_id": "KB-004",
        "provenance_status": "claim_level",
        "review_status": "machine_validated",
        "sources": [
            {
                "snapshot_status": "captured",
                "content_fingerprint": "a" * 64,
            }
        ],
    }

    errors = finalization_alignment_errors(item, stage)

    assert errors == [
        "migration-cycle-01:KB-004: stale finalization_pending state after canonical stage finalization"
    ]


def test_finalize_workflow_allowlists_exact_document_and_gap_registry() -> None:
    workflow = open(".github/workflows/finalize-stage.yml", encoding="utf-8").read()
    assert "manifests/evidence-gaps.yaml" in workflow
    assert '"$DOCUMENT"' in workflow
    assert "unexpected finalization path" in workflow
