from pathlib import Path


def test_finalizer_binds_locators_before_stage_validation() -> None:
    workflow = Path(".github/workflows/finalize-stage.yml").read_text(encoding="utf-8")
    bind = "python tools/bind_claim_locators.py"
    finalize = "python tools/stage_finalize.py"
    assert bind in workflow
    assert finalize in workflow
    assert workflow.index(bind) < workflow.index(finalize)


def test_finalizer_allowlists_only_the_registered_claim_record() -> None:
    workflow = Path(".github/workflows/finalize-stage.yml").read_text(encoding="utf-8")
    assert "claim_record" in workflow
    assert '"$CLAIM"' in workflow
    assert "git add" in workflow
    assert "evidence/claims" not in workflow.split("git add", 1)[1].split("\n", 1)[0]


def test_finalizer_runs_full_pytest_after_ledger_attestation() -> None:
    workflow = Path(".github/workflows/finalize-stage.yml").read_text(encoding="utf-8")
    ledger_commit = 'git commit -m "ledger: attest finalization for $STAGE"'
    pytest = "python -m pytest -q"
    push = "git push"
    assert ledger_commit in workflow
    assert pytest in workflow
    assert push in workflow
    assert workflow.index(ledger_commit) < workflow.index(pytest) < workflow.index(push)
