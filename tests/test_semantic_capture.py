from tools.source_contract import semantic_capture_equal, transport_changed


def test_transport_only_difference_is_stable() -> None:
    old = {
        "source_id": "S",
        "stage_id": "K",
        "source_type": "official",
        "requested_url": "u",
        "canonical_url": "u",
        "parser_version": "p",
        "response_bytes_sha256": "a" * 64,
        "normalized_document_sha256": "b" * 64,
    }
    new = {**old, "response_bytes_sha256": "c" * 64}
    assert semantic_capture_equal(old, new)
    assert transport_changed(old, new)
