from pathlib import Path


WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "kb-quality.yml"


def test_pull_request_validation_uses_exact_head_sha() -> None:
    content = WORKFLOW.read_text(encoding="utf-8")
    assert "github.event.pull_request.head.sha" in content
    assert content.count("github.event.pull_request.head.sha") >= 3
    assert "persist-credentials: false" in content
    assert 'python-version: ["3.11", "3.13"]' in content


def test_manual_same_head_dispatch_remains_available() -> None:
    content = WORKFLOW.read_text(encoding="utf-8")
    assert "workflow_dispatch:" in content
    assert "expected_sha:" in content
    assert "Checked-out SHA $actual_sha does not match expected SHA $expected_sha" in content
