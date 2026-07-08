#!/usr/bin/env python3
"""Deterministically classify and reconcile automation pull-request lifecycle state.

The reconciler owns lifecycle-only mutations. It does not execute Work Packages,
modify evidence, approve, or merge pull requests.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POLICY = ROOT / "config" / "pr-lifecycle-policy.json"
API = "https://api.github.com"
STAGE_RE = re.compile(r"(KB-[0-9]{3})")
DISPOSITION_RE = re.compile(r"pr-lifecycle-disposition\s*:\s*(?P<value>[a-z_]+)", re.IGNORECASE)

CLASSIFICATIONS = {
    "active_mutation",
    "draft_in_progress",
    "superseded_must_close",
    "blocked_by_review",
    "blocked_by_ci",
    "blocked_by_missing_final_gate",
    "repair_required",
    "ready_for_human_review",
    "ready_to_merge",
    "must_not_merge",
    "insufficient_evidence",
}

DISPOSITIONS = {
    "accepted_fixed",
    "accepted_superseded",
    "accepted_deferred",
    "rejected_with_contract",
    "rejected_with_evidence",
    "insufficient_evidence",
    "unresolved_blocker",
}

MUTATIONS = {"comment", "resolve_thread", "close_pr", "label"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _reject_non_finite(value: Any, path: str = "$", seen: set[int] | None = None) -> None:
    if seen is None:
        seen = set()
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"non-finite JSON number at {path}")
    if isinstance(value, dict):
        ident = id(value)
        if ident in seen:
            raise ValueError(f"cycle detected at {path}")
        seen.add(ident)
        for key in sorted(value):
            _reject_non_finite(value[key], f"{path}.{key}", seen)
        seen.remove(ident)
    elif isinstance(value, list):
        ident = id(value)
        if ident in seen:
            raise ValueError(f"cycle detected at {path}")
        seen.add(ident)
        for index, item in enumerate(value):
            _reject_non_finite(item, f"{path}[{index}]", seen)
        seen.remove(ident)


def canonical_json(value: Any) -> str:
    _reject_non_finite(value)
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def infer_stage(pr: dict[str, Any]) -> str | None:
    explicit = pr.get("stage_id")
    if isinstance(explicit, str) and STAGE_RE.fullmatch(explicit):
        return explicit
    for field in ("head_ref", "title", "body"):
        value = pr.get(field)
        if isinstance(value, str):
            match = STAGE_RE.search(value)
            if match:
                return match.group(1)
    return None


def labels(pr: dict[str, Any]) -> set[str]:
    raw = pr.get("labels")
    if not isinstance(raw, list):
        return set()
    return {item for item in raw if isinstance(item, str)}


def is_mutation_pr(pr: dict[str, Any], policy: dict[str, Any]) -> bool:
    lifecycle = policy["lifecycle"]
    if labels(pr) & set(lifecycle["mutation_labels"]):
        return True
    head_ref = pr.get("head_ref")
    return isinstance(head_ref, str) and any(head_ref.startswith(prefix) for prefix in lifecycle["mutation_branch_prefixes"])


def pr_sort_key(pr: dict[str, Any]) -> tuple[str, int]:
    return (str(pr.get("updated_at") or ""), int(pr.get("number") or 0))


def workflow_run_names(run: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    for key in ("name", "display_title", "displayTitle", "workflow_name", "workflowName"):
        value = run.get(key)
        if isinstance(value, str) and value.strip():
            names.add(value.strip())
    return names


def run_matches_required_workflow(run: dict[str, Any], required_name: str, head_sha: str) -> bool:
    names = workflow_run_names(run)
    return required_name in names or f"{required_name} {head_sha}" in names


def latest_required_run(pr: dict[str, Any], required_name: str) -> dict[str, Any] | None:
    head_sha = pr.get("head_sha")
    if not isinstance(head_sha, str):
        return None
    latest: dict[str, Any] | None = None
    for run in pr.get("workflow_runs", []):
        if not isinstance(run, dict):
            continue
        if run.get("head_sha") != head_sha:
            continue
        if not run_matches_required_workflow(run, required_name, head_sha):
            continue
        if latest is None or int(run.get("id") or 0) > int(latest.get("id") or 0):
            latest = run
    return latest


def ci_state(pr: dict[str, Any], policy: dict[str, Any]) -> str:
    required = policy["gates"]["required_workflows"]
    if not required:
        return "success"
    runs = {name: latest_required_run(pr, name) for name in required}
    if any(run is None for run in runs.values()):
        return "missing"
    if any(run.get("status") != "completed" for run in runs.values() if run is not None):
        return "pending"
    if all(run.get("conclusion") == "success" for run in runs.values() if run is not None):
        return "success"
    return "failed"


def final_gate_state(pr: dict[str, Any], policy: dict[str, Any]) -> str:
    gate = policy["gates"].get("final_exact_head_gate", {})
    required = gate.get("required", True)
    if not required:
        return "not_required"
    name = gate.get("workflow_name", "KB Quality")
    run = latest_required_run(pr, name)
    if run is None:
        return "missing"
    if run.get("status") != "completed":
        return "pending"
    return "passed" if run.get("conclusion") == "success" else "failed"


def review_thread_items(pr: dict[str, Any]) -> list[dict[str, Any]]:
    raw = pr.get("review_threads", [])
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, dict)]


def explicit_disposition(text: str) -> str | None:
    match = DISPOSITION_RE.search(text)
    if not match:
        return None
    value = match.group("value").lower()
    return value if value in DISPOSITIONS else None


def thread_text(thread: dict[str, Any]) -> str:
    parts: list[str] = []
    body = thread.get("body")
    if isinstance(body, str):
        parts.append(body)
    comments = thread.get("comments")
    if isinstance(comments, list):
        for comment in comments:
            if isinstance(comment, dict) and isinstance(comment.get("body"), str):
                parts.append(comment["body"])
    return "\n".join(parts)


def thread_id(thread: dict[str, Any]) -> str | None:
    value = thread.get("thread_id") or thread.get("id")
    return value if isinstance(value, str) and value else None


def thread_resolved(thread: dict[str, Any]) -> bool:
    return bool(thread.get("is_resolved") or thread.get("resolved"))


def thread_disposition(thread: dict[str, Any], *, superseded: bool) -> dict[str, Any]:
    tid = thread_id(thread) or "missing-thread-id"
    resolved = thread_resolved(thread)
    text = thread_text(thread)
    marker = explicit_disposition(text)
    if superseded:
        disposition = "accepted_superseded"
        reason = "PR is superseded; review feedback is preserved by closing this superseded PR."
    elif marker is not None:
        disposition = marker
        reason = "Explicit lifecycle disposition marker was found in review discussion."
    elif resolved:
        disposition = "accepted_fixed"
        reason = "GitHub reports the review thread as resolved."
    else:
        disposition = "unresolved_blocker"
        reason = "No explicit disposition or resolved-state evidence exists for this thread."
    return {"thread_id": tid, "is_resolved": resolved, "disposition": disposition, "reason": reason}


def all_threads_disposed(dispositions: list[dict[str, Any]]) -> bool:
    return all(item.get("disposition") in DISPOSITIONS for item in dispositions)


def has_unresolved_blocker(dispositions: list[dict[str, Any]]) -> bool:
    return any(item.get("disposition") == "unresolved_blocker" for item in dispositions)


def replacement_for(pr: dict[str, Any], candidates: list[dict[str, Any]]) -> dict[str, Any] | None:
    stage = infer_stage(pr)
    if stage is None:
        return None
    newer = [item for item in candidates if item is not pr and item.get("state") == "open" and infer_stage(item) == stage and pr_sort_key(item) > pr_sort_key(pr)]
    if not newer:
        return None
    return sorted(newer, key=pr_sort_key)[-1]


def strict_superseded_conditions(pr: dict[str, Any], replacement: dict[str, Any] | None, dispositions: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    missing: list[str] = []
    if pr.get("state") != "open":
        missing.append("PR is not open")
    if pr.get("merged") is True:
        missing.append("PR is already merged")
    if not (pr.get("draft") is True or "superseded" in labels(pr)):
        missing.append("PR is neither draft nor explicitly marked superseded")
    if replacement is None:
        missing.append("replacement PR was not identified")
    if replacement is not None and infer_stage(replacement) != infer_stage(pr):
        missing.append("replacement PR does not cover the same stage")
    unique_event = pr.get("unique_completed_ledger_event")
    if unique_event is not False and "no-unique-ledger-event" not in labels(pr):
        missing.append("absence of unique completed ledger event is not evidenced")
    if not all_threads_disposed(dispositions):
        missing.append("one or more review threads lack a disposition")
    if has_unresolved_blocker(dispositions):
        missing.append("one or more review threads remain unresolved blockers")
    return (not missing, missing)


def classify_pr(pr: dict[str, Any], mutation_prs: list[dict[str, Any]], policy: dict[str, Any]) -> dict[str, Any]:
    stage = infer_stage(pr)
    replacement = replacement_for(pr, mutation_prs)
    superseded = replacement is not None and (pr.get("draft") is True or "superseded" in labels(pr))
    dispositions = [thread_disposition(thread, superseded=superseded) for thread in sorted(review_thread_items(pr), key=lambda item: thread_id(item) or "")]
    ci = ci_state(pr, policy)
    final_gate = final_gate_state(pr, policy)

    classification = "active_mutation"
    allowed: list[str] = []
    reason = "Open mutation PR requires lifecycle tracking."
    missing_evidence: list[str] = []

    if superseded:
        can_close, missing = strict_superseded_conditions(pr, replacement, dispositions)
        if can_close:
            classification = "superseded_must_close"
            allowed = ["comment", "resolve_thread", "close_pr"]
            reason = f"Replaced by PR #{replacement['number']} for the same stage or scope."
        else:
            classification = "insufficient_evidence"
            allowed = ["comment", "label"]
            reason = "PR appears superseded, but strict auto-close conditions are not fully evidenced."
            missing_evidence = missing
    elif pr.get("draft") is True:
        classification = "draft_in_progress"
        reason = "Draft PR remains in progress and cannot be treated as ready."
    elif has_unresolved_blocker(dispositions):
        classification = "blocked_by_review"
        reason = "At least one review thread has unresolved_blocker disposition."
    elif ci in {"missing", "pending", "failed"}:
        classification = "blocked_by_ci"
        reason = f"Required CI state is {ci}."
    elif final_gate in {"missing", "pending", "failed"}:
        classification = "blocked_by_missing_final_gate"
        reason = f"Final exact-head gate state is {final_gate}."
    elif pr.get("mergeable") is False:
        classification = "repair_required"
        reason = "GitHub reports the PR is not mergeable."
    else:
        classification = "ready_for_human_review"
        reason = "Lifecycle gates are clear; human review can proceed."
        if policy["gates"].get("ready_to_merge_when_human_approved", False):
            classification = "ready_to_merge"
            reason = "All lifecycle gates are clear and policy permits ready_to_merge state."

    action: dict[str, Any] = {
        "pr": pr.get("number"),
        "stage_id": stage,
        "head_sha": pr.get("head_sha"),
        "classification": classification,
        "reason": reason,
        "review_dispositions": dispositions,
        "allowed_mutations": allowed,
    }
    if replacement is not None:
        action["replacement_pr"] = replacement.get("number")
    if missing_evidence:
        action["missing_evidence"] = sorted(set(missing_evidence))
    return action


def lifecycle_plan(state: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    repository = state.get("repository") if isinstance(state.get("repository"), dict) else {}
    repo_name = repository.get("full_name") or state.get("repository_full_name") or "unknown"
    prs = [item for item in state.get("pull_requests", []) if isinstance(item, dict)]
    open_prs = [item for item in prs if item.get("state") == "open"]
    mutation_prs = [item for item in open_prs if is_mutation_pr(item, policy)]
    actions = [classify_pr(pr, mutation_prs, policy) for pr in sorted(mutation_prs, key=lambda item: int(item.get("number") or 0))]

    blockers = [item for item in actions if item["classification"] not in {"ready_for_human_review", "ready_to_merge"}]
    new_work_allowed = not mutation_prs
    reason = "no open mutation PRs"
    if mutation_prs:
        reason = "open mutation PRs must be reconciled first"
    if any(item["classification"] == "superseded_must_close" for item in actions):
        reason = "safe superseded PR cleanup must run before planning new work"
    if blockers and len(mutation_prs) > 1:
        reason = "multiple open mutation PRs require lifecycle reconciliation before planning"

    return {
        "schema_version": 1,
        "observed_at": state.get("captured_at") if isinstance(state.get("captured_at"), str) else utc_now(),
        "repository": repo_name,
        "actions": actions,
        "planner_gate": {"new_work_allowed": new_work_allowed, "reason": reason},
    }


def api_request(repository: str, endpoint: str, token: str, *, method: str = "GET", body: dict[str, Any] | None = None) -> Any:
    data = None if body is None else json.dumps(body, sort_keys=True, allow_nan=False).encode("utf-8")
    request = urllib.request.Request(f"{API}/repos/{repository}/{endpoint}", data=data, method=method)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    request.add_header("Authorization", f"Bearer {token}")
    if body is not None:
        request.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(request, timeout=30) as response:
        text = response.read().decode("utf-8")
    return json.loads(text) if text else None


def graphql(token: str, query: str, variables: dict[str, Any]) -> Any:
    data = json.dumps({"query": query, "variables": variables}, sort_keys=True, allow_nan=False).encode("utf-8")
    request = urllib.request.Request("https://api.github.com/graphql", data=data, method="POST")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("Authorization", f"Bearer {token}")
    request.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if payload.get("errors"):
        raise RuntimeError(f"GraphQL error: {payload['errors']!r}")
    return payload.get("data")


def comment_body(action: dict[str, Any], plan: dict[str, Any]) -> str:
    body = {
        "schema_version": plan["schema_version"],
        "pr": action["pr"],
        "classification": action["classification"],
        "reason": action["reason"],
        "review_dispositions": action["review_dispositions"],
        "allowed_mutations": action["allowed_mutations"],
    }
    return "PR Lifecycle Reconciler disposition:\n\n```json\n" + canonical_json(body) + "```"


def apply_plan(plan: dict[str, Any], token: str) -> list[dict[str, Any]]:
    repository = plan["repository"]
    if repository == "unknown":
        raise ValueError("cannot apply lifecycle mutations without repository full_name")
    results: list[dict[str, Any]] = []
    for action in plan["actions"]:
        pr_number = action.get("pr")
        if not isinstance(pr_number, int):
            continue
        allowed = set(action.get("allowed_mutations", []))
        if not allowed <= MUTATIONS:
            raise ValueError(f"unsupported lifecycle mutation set for PR {pr_number}: {sorted(allowed)}")
        result: dict[str, Any] = {"pr": pr_number, "mutations": []}
        if "comment" in allowed:
            api_request(repository, f"issues/{pr_number}/comments", token, method="POST", body={"body": comment_body(action, plan)})
            result["mutations"].append("comment")
        if "label" in allowed:
            label = "lifecycle-insufficient-evidence" if action["classification"] == "insufficient_evidence" else f"lifecycle-{action['classification'].replace('_', '-')}"
            api_request(repository, f"issues/{pr_number}/labels", token, method="POST", body={"labels": [label]})
            result["mutations"].append("label")
        if "resolve_thread" in allowed:
            resolved_count = 0
            for disposition in action.get("review_dispositions", []):
                tid = disposition.get("thread_id")
                if disposition.get("is_resolved") is True:
                    continue
                if isinstance(tid, str) and tid != "missing-thread-id":
                    graphql(token, "mutation($threadId: ID!) { resolveReviewThread(input: {threadId: $threadId}) { thread { id isResolved } } }", {"threadId": tid})
                    resolved_count += 1
            result["mutations"].append({"resolve_thread": resolved_count})
        if "close_pr" in allowed:
            api_request(repository, f"pulls/{pr_number}", token, method="PATCH", body={"state": "closed"})
            result["mutations"].append("close_pr")
        results.append(result)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-state", required=True, type=Path)
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    args = parser.parse_args()

    policy = load_json(args.policy)
    state = load_json(args.repo_state)
    plan = lifecycle_plan(state, policy)
    if args.apply:
        token = os.environ.get(args.token_env, "")
        if not token:
            raise SystemExit(f"ERROR: {args.token_env} is required for --apply")
        plan["mutation_results"] = apply_plan(plan, token)
        plan["applied_at"] = utc_now()
    output = canonical_json(plan)
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")
    if not plan["planner_gate"]["new_work_allowed"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
