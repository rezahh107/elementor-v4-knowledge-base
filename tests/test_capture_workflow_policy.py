from pathlib import Path


def test_automatic_capture_skips_already_captured_work_items() -> None:
    workflow = Path(".github/workflows/capture-source.yml").read_text(encoding="utf-8")
    assert "Determine capture policy" in workflow
    assert 'item["source_capture_status"] == "captured"' in workflow
    assert "workflow_dispatch" in workflow
    assert "capture_needed" in workflow


def test_capture_writeback_runs_only_when_needed() -> None:
    workflow = Path(".github/workflows/capture-source.yml").read_text(encoding="utf-8")
    assert "if: steps.policy.outputs.value == 'true'" in workflow
    assert "if: needs.compute.outputs.capture_needed == 'true'" in workflow
