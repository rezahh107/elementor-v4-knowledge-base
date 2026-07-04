"""Stable source/locator contracts shared by capture, binding, and validation."""
from __future__ import annotations

import hashlib
import re
from typing import Any

LEGACY_LOCATOR_VERSION = 2
SEMANTIC_LOCATOR_VERSION = 3
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")


def _require_sha256(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ValueError(f"{label} must be a lowercase SHA-256 hex digest")
    return value


def canonical_snapshot_sha256(record: dict[str, Any]) -> str:
    """Return the semantic source fingerprint used by current claim locators.

    Source-record v3 stores the canonical visible-text fingerprint as
    ``normalized_document_sha256``. Future schemas may expose the same value
    explicitly as ``canonical_snapshot_sha256``. Consumers use this adapter so
    raw HTTP byte changes never invalidate semantic claim bindings by accident.
    """
    explicit = record.get("canonical_snapshot_sha256")
    if explicit is not None:
        return _require_sha256(explicit, "canonical_snapshot_sha256")
    return _require_sha256(
        record.get("normalized_document_sha256"),
        "normalized_document_sha256",
    )


def semantic_locator_fingerprint(
    *,
    source_id: str,
    locator: str,
    canonical_snapshot_sha256: str,
    version: int = SEMANTIC_LOCATOR_VERSION,
) -> str:
    """Bind a locator to semantic source content, never transport bytes."""
    if version != SEMANTIC_LOCATOR_VERSION:
        raise ValueError(f"unsupported semantic locator version: {version}")
    digest = _require_sha256(
        canonical_snapshot_sha256,
        "canonical_snapshot_sha256",
    )
    payload = "\0".join(
        [
            f"locator-v{version}",
            source_id,
            locator,
            digest,
        ]
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def semantic_capture_equal(existing: Any, candidate: dict[str, Any]) -> bool:
    """Return True when two captures represent the same reusable source truth.

    HTTP headers, retrieval timestamps, exact response bytes, artifact names,
    and response sizes are deliberately excluded. Those are transport telemetry.
    """
    if not isinstance(existing, dict):
        return False
    identity_fields = (
        "source_id",
        "stage_id",
        "source_type",
        "requested_url",
        "canonical_url",
        "parser_version",
    )
    if any(existing.get(field) != candidate.get(field) for field in identity_fields):
        return False
    try:
        return canonical_snapshot_sha256(existing) == canonical_snapshot_sha256(candidate)
    except ValueError:
        return False


def transport_changed(existing: Any, candidate: dict[str, Any]) -> bool:
    if not isinstance(existing, dict):
        return True
    return existing.get("response_bytes_sha256") != candidate.get("response_bytes_sha256")
