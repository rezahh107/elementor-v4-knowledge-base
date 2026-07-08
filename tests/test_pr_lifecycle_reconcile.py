from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.pr_lifecycle_reconcile import canonical_json, lifecycle_plan, load_json

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "pr_lifecycle"
POLICY = ROOT / "config" / "pr-lifecycle-policy.json"


def _plan(name: str) -> dict[str, object]:
    return lifecycle_plan(load_json(FIXTURES / name), load_json(POLICY))


def test_superseded_draft_can_be_closed_only_with_strict_evidence() -> None:
    plan = _plan("superseded_draft.json")
    first = plan["actions"][0]
    assert first["pr"] == 62
    assert first["classification"] == "superseded_must_close"
    assert first["replacement_pr"] == 64
    assert first["allowed_mutations"] == ["comment", "resolve_thread", "close_pr"]
    assert first["review_dispositions"][0]["disposition"] == "accepted_superseded"
    assert plan["planner_gate"]["new_work_allowed"] is False


def test_unresolved_review_thread_blocks_ready_state() -> None:
    plan = _plan("unresolved_review.json")
    action = plan["actions"][0]
    assert action["classification"] == "blocked_by_review"
    assert action["review_dispositions"][0]["disposition"] == "unresolved_blocker"
    assert plan["planner_gate"]["new_work_allowed"] is False


def test_missing_final_gate_blocks_ready_state() -> None:
    plan = _plan("missing_final_gate.json")
    action = plan["actions"][0]
    assert action["classification"] == "blocked_by_ci"
    assert "Required CI state is missing" in action["reason"]


def test_canonical_json_rejects_non_finite_values() -> None:
    with pytest.raises(ValueError, match="non-finite"):
        canonical_json({"bad": float("nan")})


def test_plan_is_canonical_json_serializable() -> None:
    text = canonical_json(_plan("superseded_draft.json"))
    reparsed = json.loads(text)
    assert reparsed["schema_version"] == 1
    assert text.endswith("\n")
