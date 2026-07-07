#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def plan(state):
    catalog = load(ROOT/'planning/WORK_PACKAGE_CATALOG.json')
    queue = load(ROOT/'planning/WORK_PACKAGE_QUEUE.json')
    control = load(ROOT/'planning/CONTROL_STATE.json')
    prs = state.get('pull_requests', []) if isinstance(state, dict) else []
    open_prs = [p for p in prs if isinstance(p, dict) and p.get('state') == 'open']
    if len(open_prs) > 1:
        return {'action':'blocked','reason':'multiple_open_mutation_prs'}
    if open_prs:
        return {'action':'reconcile_existing_mutation_pr','work_package':control.get('active_work_package_id')}
    if queue.get('active_work_package_id'):
        return {'action':'continue_active_work_package','work_package':queue['active_work_package_id']}
    ready = queue.get('ready_work_packages', [])
    return {'action':'start_ready_work_package' if ready else 'no_executable_work','work_package':ready[0] if ready else None,'catalog_refresh_needed':len(ready)<catalog['policy']['refresh_when_ready_below']}

if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--repo-state',required=True,type=Path); args=ap.parse_args()
    print(json.dumps(plan(load(args.repo_state)),ensure_ascii=False,indent=2))
