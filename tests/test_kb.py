from __future__ import annotations

import math

import pytest

from tools.kb import canonical_json_bytes, load_yaml, render_generated, validate_repository, STAGES_PATH


def test_canonical_json_rejects_non_finite_numbers() -> None:
    with pytest.raises(ValueError):
        canonical_json_bytes({"value": math.nan})
    with pytest.raises(ValueError):
        canonical_json_bytes({"value": math.inf})


def test_generated_artifacts_are_deterministic() -> None:
    manifest = load_yaml(STAGES_PATH)
    first = render_generated(manifest)
    second = render_generated(manifest)
    assert first == second


def test_repository_consistency() -> None:
    result = validate_repository(check_generated=True)
    assert result.errors == []
    assert result.warnings == []
