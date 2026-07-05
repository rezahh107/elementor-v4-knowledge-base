from pathlib import Path


WORKFLOW_PATH = Path(__file__).parent.parent / ".github" / "workflows" / "finalize-stage.yml"


def test_finalizer_supports_reopen_same_head_recovery() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    for trigger in ["reopened", "ready_for_review", "edited"]:
        assert trigger in workflow
    assert "github.actor != 'github-actions[bot]'" in workflow


def test_finalizer_keeps_manual_dispatch_recovery() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "workflow_dispatch:" in workflow
    assert "cancel-in-progress: false" in workflow
