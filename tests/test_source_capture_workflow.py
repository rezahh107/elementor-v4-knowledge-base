from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "capture-source.yml"
ALLOWLIST = ("evidence/sources/", "manifests/work-items.yaml")


def _git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
    )
    return completed.stdout


def _init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / "evidence" / "sources").mkdir(parents=True)
    (repo / "manifests").mkdir(parents=True)
    (repo / "manifests" / "work-items.yaml").write_text("items: []\n", encoding="utf-8")
    _git(repo, "init")
    _git(repo, "config", "user.name", "Test")
    _git(repo, "config", "user.email", "test@example.invalid")
    _git(repo, "add", "manifests/work-items.yaml")
    _git(repo, "commit", "-m", "baseline")
    return repo


def _assert_allowlisted(paths: list[str]) -> None:
    unexpected = [path for path in paths if not (path.startswith("evidence/sources/") or path == "manifests/work-items.yaml")]
    if unexpected:
        raise AssertionError("unexpected capture path: " + ", ".join(unexpected))


def test_source_capture_stages_new_records_before_patch_generation() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "git add -A -- evidence/sources manifests/work-items.yaml" in text
    assert "git diff --cached --name-only \"$TARGET_HEAD_SHA\"" in text
    assert "git diff --cached --binary \"$TARGET_HEAD_SHA\" -- evidence/sources manifests/work-items.yaml" in text


def test_untracked_source_record_is_included_in_generated_patch(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    source = repo / "evidence" / "sources" / "SRC-KB-999-01.yaml"
    source.write_text("schema_version: 3\nsource_id: SRC-KB-999-01\n", encoding="utf-8")
    (repo / "manifests" / "work-items.yaml").write_text("items:\n  - stage_id: KB-999\n", encoding="utf-8")

    _git(repo, "add", "-A", "--", "evidence/sources", "manifests/work-items.yaml")
    staged_paths = _git(repo, "diff", "--cached", "--name-only", "HEAD").splitlines()
    _assert_allowlisted(staged_paths)
    patch = _git(repo, "diff", "--cached", "--binary", "HEAD", "--", "evidence/sources", "manifests/work-items.yaml")

    assert "evidence/sources/SRC-KB-999-01.yaml" in staged_paths
    assert "diff --git a/evidence/sources/SRC-KB-999-01.yaml b/evidence/sources/SRC-KB-999-01.yaml" in patch
    assert "+source_id: SRC-KB-999-01" in patch


def test_source_capture_allowlist_fails_closed_on_unexpected_staged_path(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    (repo / "tools").mkdir()
    (repo / "tools" / "unexpected.py").write_text("print('no')\n", encoding="utf-8")
    _git(repo, "add", "tools/unexpected.py")
    staged_paths = _git(repo, "diff", "--cached", "--name-only", "HEAD").splitlines()

    with pytest.raises(AssertionError, match="unexpected capture path"):
        _assert_allowlisted(staged_paths)
