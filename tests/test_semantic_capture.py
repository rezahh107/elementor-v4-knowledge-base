from tools.source_contract import semantic_capture_equal, transport_changed


def _record(raw_hash: str, normalized_hash: str) -> dict[str, str]:
    return {
        "source_id": "S",
        "stage_id": "K",
        "source_type": "official",
        "requested_url": "u",
        "canonical_url": "u",
        "parser_version": "p",
        "response_bytes_sha256": raw_hash,
        "normalized_document_sha256": normalized_hash,
    }


def test_transport_only_difference_is_stable() -> None:
    old = _record("a" * 64, "b" * 64)
    new = _record("c" * 64, "b" * 64)
    assert semantic_capture_equal(old, new)
    assert transport_changed(old, new)


def test_malformed_candidate_is_rejected_without_exception() -> None:
    old = _record("a" * 64, "b" * 64)
    assert not semantic_capture_equal(old, None)
    assert transport_changed(old, None)
    assert not transport_changed(None, None)
