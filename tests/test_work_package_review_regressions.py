from __future__ import annotations

from tools.github_state_snapshot import build_request, normalize_reviews
from tools.work_package_contracts import load_documents, validate_documents


def review(ident: int, state: str, submitted_at: str) -> dict:
    return {
        "id": ident,
        "user": {"login": "reviewer"},
        "state": state,
        "submitted_at": submitted_at,
    }


def test_repository_request_omits_trailing_slash_for_empty_endpoint():
    request = build_request("owner/repository", endpoint="")
    assert request.full_url == "https://api.github.com/repos/owner/repository"


def test_comment_does_not_clear_requested_changes():
    result = normalize_reviews(
        [
            review(1, "CHANGES_REQUESTED", "2026-07-07T10:00:00Z"),
            review(2, "COMMENTED", "2026-07-07T10:01:00Z"),
        ]
    )
    assert result[0]["state"] == "CHANGES_REQUESTED"


def test_approval_clears_requested_changes():
    result = normalize_reviews(
        [
            review(1, "CHANGES_REQUESTED", "2026-07-07T10:00:00Z"),
            review(2, "COMMENTED", "2026-07-07T10:01:00Z"),
            review(3, "APPROVED", "2026-07-07T10:02:00Z"),
        ]
    )
    assert result[0]["state"] == "APPROVED"


def test_dismissal_clears_requested_changes():
    result = normalize_reviews(
        [
            review(1, "CHANGES_REQUESTED", "2026-07-07T10:00:00Z"),
            review(2, "DISMISSED", "2026-07-07T10:01:00Z"),
        ]
    )
    assert result[0]["state"] == "DISMISSED"


def test_source_scope_schema_rejects_empty_preferred_sources():
    documents = load_documents()
    documents["catalog"]["work_packages"][0]["source_scope"][
        "preferred_source_types"
    ] = []

    errors = validate_documents(documents)

    assert any(
        error.startswith(
            "WP_SCHEMA_CATALOG:work_packages/0/source_scope/"
            "preferred_source_types"
        )
        for error in errors
    )


def test_verified_version_schema_requires_evidence():
    documents = load_documents()
    documents["catalog"]["work_packages"][0]["source_scope"][
        "applicable_elementor_versions"
    ] = [
        {
            "value": "4.0",
            "verification_status": "verified",
            "evidence_refs": [],
        }
    ]

    errors = validate_documents(documents)

    assert any(
        error.startswith(
            "WP_SCHEMA_CATALOG:work_packages/0/source_scope/"
            "applicable_elementor_versions"
        )
        for error in errors
    )
