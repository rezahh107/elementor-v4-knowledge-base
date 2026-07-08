from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "capture-source.yml"


def test_source_capture_stages_new_records_before_patch_generation() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "git add -A -- evidence/sources manifests/work-items.yaml" in text
    assert "git diff --cached --name-only \"$TARGET_HEAD_SHA\"" in text
    assert "git diff --cached --binary \"$TARGET_HEAD_SHA\" -- evidence/sources manifests/work-items.yaml" in text


def test_source_capture_allowlist_uses_staged_diff() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    allowlist_index = text.index("git diff --cached --name-only \"$TARGET_HEAD_SHA\"")
    patch_index = text.index("git diff --cached --binary \"$TARGET_HEAD_SHA\"")
    assert allowlist_index < patch_index
    assert "unexpected capture path" in text
    assert "unexpected writeback path" in text
