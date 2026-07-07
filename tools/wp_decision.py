"""Deterministic Work Package decision core."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"^[a-f0-9]{40}$")
REQUIRED_PULL_REQUEST_KEYS = {
    "number",
    "state",
    "draft",
    "head_sha",
    "head_ref",
    "base_ref",
    "labels",
    "updated_at",
    "reviews",
    "workflow_runs",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _valid_pull_request(pull_request: Any) -> bool:
    if not isinstance(pull_request, dict):
        return False
    if not REQUIRED_PULL_REQUEST_KEYS <= pull_request.keys():
        return False
    if not isinstance(pull_request.get("number"), int):
        return False
    if pull_request.get("state") != "open":
        return False
    if not isinstance(pull_request.get("draft"), bool):
        return False
    if not SHA.fullmatch(str(pull_request.get("head_sha", ""))):
        return False
    if not isinstance(pull_request.get("head_ref"), str):
        return False
    if not isinstance(pull_request.get("base_ref"), str):
        return False
    return all(
        isinstance(pull_request[key], list)
        for key in ("labels", "reviews", "workflow_runs")
    )


def valid_state(state: Any) -> bool:
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        return False

    repository = state.get("repository")
    pull_requests = state.get("pull_requests")
    if not isinstance(repository, dict):
        return False
    if not SHA.fullmatch(str(repository.get("main_sha", ""))):
        return False
    if not isinstance(pull_requests, list):
        return False

    return all(_valid_pull_request(item) for item in pull_requests)


def mutation_pr(
    pull_request: dict[str, Any],
    config: dict[str, Any],
) -> bool:
    rules = config.get("pull_request_classification", {})
    automation_labels = set(rules.get("automation_labels", []))
    if set(pull_request.get("labels", [])) & automation_labels:
        return True

    head_ref = pull_request.get("head_ref")
    prefixes = rules.get("automation_branch_prefixes", [])
    return isinstance(head_ref, str) and any(
        head_ref.startswith(prefix)
        for prefix in prefixes
    )


def gate_state(
    pull_request: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    blocking_states = set(
        config.get("merge_gates", {}).get(
            "blocking_review_states",
            [],
        )
    )
    has_blocking_review = any(
        isinstance(review, dict)
        and review.get("state") in blocking_states
        for review in pull_request.get("reviews", [])
    )
    review_state = (
        "changes_requested"
        if has_blocking_review
        else "clear"
    )

    required_workflows = set(
        config.get("merge_gates", {}).get(
            "required_workflows",
            [],
        )
    )
    latest_runs: dict[str, dict[str, Any]] = {}

    for run in pull_request.get("workflow_runs", []):
        if not isinstance(run, dict):
            continue
        if run.get("head_sha") != pull_request.get("head_sha"):
            continue

        name = run.get("name")
        if not isinstance(name, str):
            continue

        current = latest_runs.get(name)
        if current is None or (run.get("id") or 0) > (
            current.get("id") or 0
        ):
            latest_runs[name] = run

    if not required_workflows <= latest_runs.keys():
        ci_state = "missing"
    elif any(
        latest_runs[name].get("status") != "completed"
        for name in required_workflows
    ):
        ci_state = "pending"
    elif all(
        latest_runs[name].get("conclusion") == "success"
        for name in required_workflows
    ):
        ci_state = "success"
    else:
        ci_state = "failed"

    return {
        "ci_state": ci_state,
        "review_state": review_state,
        "eligible_for_external_merge_reconciliation": (
            ci_state == "success"
            and review_state == "clear"
            and not pull_request.get("draft")
        ),
    }


def plan(
    state: dict[str, Any],
    root: Path = ROOT,
) -> dict[str, Any]:
    if not valid_state(state):
        return {
            "action": "blocked",
            "reason": "invalid_repository_state",
            "work_package": None,
        }

    catalog = load(root / "planning/WORK_PACKAGE_CATALOG.json")
    queue = load(root / "planning/WORK_PACKAGE_QUEUE.json")
    config = load(root / "config/work-package-planner.json")

    pull_requests = state["pull_requests"]
    mutation_pull_requests = [
        pull_request
        for pull_request in pull_requests
        if mutation_pr(pull_request, config)
    ]
    base = {
        "observed_main_sha": state["repository"]["main_sha"],
        "open_mutation_pull_request_count": len(
            mutation_pull_requests
        ),
        "open_non_mutation_pull_request_count": (
            len(pull_requests) - len(mutation_pull_requests)
        ),
    }

    if len(mutation_pull_requests) > 1:
        return {
            **base,
            "action": "blocked",
            "reason": "multiple_open_mutation_prs",
            "work_package": None,
        }

    if mutation_pull_requests:
        pull_request = mutation_pull_requests[0]
        return {
            **base,
            "action": "reconcile_existing_mutation_pr",
            "work_package": config.get("active_work_package_id"),
            "pull_request": pull_request["number"],
            "head_sha": pull_request["head_sha"],
            "gates": gate_state(pull_request, config),
        }

    packages = {
        item.get("id"): item
        for item in catalog.get("work_packages", [])
        if isinstance(item, dict)
    }
    active_id = queue.get("active_work_package_id")

    if active_id:
        active_package = packages.get(active_id)
        if (
            not isinstance(active_package, dict)
            or active_package.get("status") != "active"
        ):
            return {
                **base,
                "action": "blocked",
                "reason": "active_work_package_status_drift",
                "work_package": active_id,
            }
        return {
            **base,
            "action": "continue_active_work_package",
            "work_package": active_id,
        }

    ready_ids = queue.get("ready_work_packages", [])
    executable_ids = [
        work_package_id
        for work_package_id in ready_ids
        if isinstance(packages.get(work_package_id), dict)
        and packages[work_package_id].get("status") == "ready"
    ]
    drifted_ids = sorted(set(ready_ids) - set(executable_ids))

    if drifted_ids:
        return {
            **base,
            "action": "blocked",
            "reason": "ready_queue_catalog_status_drift",
            "work_package": None,
            "drifted_work_packages": drifted_ids,
        }

    refresh_threshold = catalog.get("policy", {}).get(
        "refresh_when_ready_below",
        0,
    )
    return {
        **base,
        "action": (
            "start_ready_work_package"
            if executable_ids
            else "no_executable_work"
        ),
        "work_package": (
            executable_ids[0]
            if executable_ids
            else None
        ),
        "catalog_refresh_needed": (
            len(executable_ids) < refresh_threshold
        ),
    }
