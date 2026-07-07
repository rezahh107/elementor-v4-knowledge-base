from __future__ import annotations
import json
from pathlib import Path
import pytest
from tools.github_state_snapshot import build_request, normalize_pull_requests, normalize_reviews, normalize_workflow_runs
from tools.work_package_controller import plan
from tools.work_package_validate import validate, validate_negative_fixtures

ROOT=Path(__file__).resolve().parents[1]; HEAD="1"*40; MAIN="2"*40

def run(name="KB Quality",conclusion="success",head=HEAD,status="completed",ident=1):
    return {"id":ident,"name":name,"event":"pull_request","status":status,"conclusion":conclusion,"head_sha":head,"run_attempt":1,"created_at":"2026-07-07T10:00:00Z","updated_at":"2026-07-07T10:01:00Z"}

def pr(number=1,ref="feature/x",labels=None,reviews=None,runs=None,draft=False):
    return {"number":number,"state":"open","draft":draft,"head_sha":HEAD,"head_ref":ref,"base_ref":"main","labels":labels or [],"updated_at":"2026-07-07T10:00:00Z","reviews":reviews or [],"workflow_runs":runs or []}

def state(prs=None):
    prs=prs or []
    return {"schema_version":1,"captured_at":"2026-07-07T10:00:00Z","repository":{"full_name":"owner/repo","default_branch":"main","main_sha":MAIN},"pull_requests":prs,"workflow_runs":[r for p in prs for r in p["workflow_runs"]]}

def test_contracts_and_invalid_cases_pass():
    assert validate()==[]
    assert validate_negative_fixtures()==[]

def test_ready_package_selected_and_main_sha_observed():
    result=plan(state())
    assert (result["action"],result["work_package"],result["observed_main_sha"])==("start_ready_work_package","KB-WP-001",MAIN)

def test_unrelated_pr_does_not_block():
    result=plan(state([pr()]))
    assert result["action"]=="start_ready_work_package"
    assert result["open_non_mutation_pull_request_count"]==1

def test_labeled_or_prefixed_mutation_pr_reconciles():
    for item in (pr(labels=["work-package"]),pr(ref="automation/wp-kb-wp-001")):
        assert plan(state([item]))["action"]=="reconcile_existing_mutation_pr"

def test_exact_head_success_and_review_gate():
    result=plan(state([pr(labels=["work-package"],runs=[run()])]))
    assert result["gates"]=={"ci_state":"success","review_state":"clear","eligible_for_external_merge_reconciliation":True}
    review={"user":"reviewer","state":"CHANGES_REQUESTED","submitted_at":"2026-07-07T10:02:00Z"}
    result=plan(state([pr(labels=["work-package"],runs=[run()],reviews=[review])]))
    assert result["gates"]["review_state"]=="changes_requested"
    assert result["gates"]["eligible_for_external_merge_reconciliation"] is False

def test_missing_or_wrong_head_ci_is_not_eligible():
    missing=plan(state([pr(labels=["work-package"])]))
    wrong=plan(state([pr(labels=["work-package"],runs=[run(head="3"*40)])]))
    assert missing["gates"]["ci_state"]==wrong["gates"]["ci_state"]=="missing"

def test_multiple_mutation_prs_block():
    result=plan(state([pr(1,labels=["work-package"]),pr(2,ref="migration/KB-002")]))
    assert result["action"]=="blocked" and result["reason"]=="multiple_open_mutation_prs"

def test_invalid_state_fails_closed():
    value=state();value["pull_requests"]=None
    assert plan(value)["reason"]=="invalid_repository_state"

def test_static_policy_has_no_current_main_sha():
    policy=json.loads((ROOT/"config/work-package-planner.json").read_text())
    assert policy["runtime_state_source"]=="github_api"
    assert "last_verified_main_sha" not in policy

def test_auth_header_is_conditional():
    assert build_request("owner/repo","").get_header("Authorization") is None
    assert build_request("owner/repo","token").get_header("Authorization")=="Bearer token"

def test_pull_normalization_handles_null_head_and_rejects_bad_root():
    item=normalize_pull_requests([{"number":1,"state":"open","draft":False,"head":None}])[0]
    assert item["head_sha"] is None and item["head_ref"] is None
    with pytest.raises(ValueError):normalize_pull_requests({"message":"bad"})

def test_runs_are_exact_head_only():
    result=normalize_workflow_runs({"workflow_runs":[run(ident=1),run(head="3"*40,ident=2)]},HEAD)
    assert [item["id"] for item in result]==[1]

def test_latest_review_per_user_wins():
    result=normalize_reviews([
        {"user":{"login":"r"},"state":"CHANGES_REQUESTED","submitted_at":"2026-07-07T10:00:00Z"},
        {"user":{"login":"r"},"state":"APPROVED","submitted_at":"2026-07-07T10:01:00Z"},
    ])
    assert result[0]["state"]=="APPROVED"
