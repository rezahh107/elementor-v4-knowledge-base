"""Deterministic Work Package decision core."""
from __future__ import annotations
import json,re
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1]
SHA=re.compile(r"^[a-f0-9]{40}$")

def load(path:Path)->Any:
    return json.loads(path.read_text(encoding="utf-8"))

def valid_state(state:Any)->bool:
    if not isinstance(state,dict) or state.get("schema_version")!=1:return False
    repo=state.get("repository"); prs=state.get("pull_requests")
    if not isinstance(repo,dict) or not SHA.fullmatch(str(repo.get("main_sha",""))) or not isinstance(prs,list):return False
    keys={"number","state","draft","head_sha","head_ref","base_ref","labels","updated_at","reviews","workflow_runs"}
    return all(isinstance(p,dict) and keys<=p.keys() and all(isinstance(p[k],list) for k in ("labels","reviews","workflow_runs")) for p in prs)

def mutation_pr(pr:dict[str,Any],cfg:dict[str,Any])->bool:
    rules=cfg.get("pull_request_classification",{})
    if set(pr.get("labels",[]))&set(rules.get("automation_labels",[])):return True
    ref=pr.get("head_ref")
    return isinstance(ref,str) and any(ref.startswith(x) for x in rules.get("automation_branch_prefixes",[]))

def gate_state(pr:dict[str,Any],cfg:dict[str,Any])->dict[str,Any]:
    blocked=set(cfg.get("merge_gates",{}).get("blocking_review_states",[]))
    review="changes_requested" if any(isinstance(x,dict) and x.get("state") in blocked for x in pr.get("reviews",[])) else "clear"
    required=set(cfg.get("merge_gates",{}).get("required_workflows",[])); latest={}
    for run in pr.get("workflow_runs",[]):
        if not isinstance(run,dict) or run.get("head_sha")!=pr.get("head_sha"):continue
        name=run.get("name")
        if isinstance(name,str) and (name not in latest or (run.get("id") or 0)>(latest[name].get("id") or 0)):latest[name]=run
    if not required<=latest.keys():ci="missing"
    elif any(latest[n].get("status")!="completed" for n in required):ci="pending"
    elif all(latest[n].get("conclusion")=="success" for n in required):ci="success"
    else:ci="failed"
    return {"ci_state":ci,"review_state":review,"eligible_for_external_merge_reconciliation":ci=="success" and review=="clear" and not pr.get("draft")}

def plan(state:dict[str,Any],root:Path=ROOT)->dict[str,Any]:
    if not valid_state(state):return {"action":"blocked","reason":"invalid_repository_state","work_package":None}
    catalog=load(root/"planning/WORK_PACKAGE_CATALOG.json"); queue=load(root/"planning/WORK_PACKAGE_QUEUE.json"); cfg=load(root/"config/work-package-planner.json")
    prs=state["pull_requests"]; mutation=[p for p in prs if mutation_pr(p,cfg)]
    base={"observed_main_sha":state["repository"]["main_sha"],"open_mutation_pull_request_count":len(mutation),"open_non_mutation_pull_request_count":len(prs)-len(mutation)}
    if len(mutation)>1:return {**base,"action":"blocked","reason":"multiple_open_mutation_prs","work_package":None}
    if mutation:
        pr=mutation[0]
        return {**base,"action":"reconcile_existing_mutation_pr","work_package":cfg.get("active_work_package_id"),"pull_request":pr["number"],"head_sha":pr["head_sha"],"gates":gate_state(pr,cfg)}
    packages={x.get("id"):x for x in catalog.get("work_packages",[]) if isinstance(x,dict)}; active=queue.get("active_work_package_id")
    if active:
        if not isinstance(packages.get(active),dict) or packages[active].get("status")!="active":return {**base,"action":"blocked","reason":"active_work_package_status_drift","work_package":active}
        return {**base,"action":"continue_active_work_package","work_package":active}
    ready=queue.get("ready_work_packages",[]); executable=[x for x in ready if isinstance(packages.get(x),dict) and packages[x].get("status")=="ready"]
    drift=sorted(set(ready)-set(executable))
    if drift:return {**base,"action":"blocked","reason":"ready_queue_catalog_status_drift","work_package":None,"drifted_work_packages":drift}
    threshold=catalog.get("policy",{}).get("refresh_when_ready_below",0)
    return {**base,"action":"start_ready_work_package" if executable else "no_executable_work","work_package":executable[0] if executable else None,"catalog_refresh_needed":len(executable)<threshold}
