#!/usr/bin/env python3
"""Capture deterministic GitHub state for the Work Package planner."""
from __future__ import annotations
import argparse
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

API = "https://api.github.com"

def build_request(repository: str, token: str = "", endpoint: str = "pulls?state=open&per_page=100") -> urllib.request.Request:
    request = urllib.request.Request(f"{API}/repos/{repository}/{endpoint}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    return request

def api_get(repository: str, endpoint: str, token: str) -> Any:
    with urllib.request.urlopen(build_request(repository, token, endpoint), timeout=30) as response:
        return json.load(response)

def normalize_workflow_runs(payload: Any, head_sha: str) -> list[dict[str, Any]]:
    runs = payload.get("workflow_runs") if isinstance(payload, dict) else None
    if not isinstance(runs, list):
        raise ValueError(f"Unexpected workflow response format: {payload!r}")
    fields = ("id", "name", "event", "status", "conclusion", "head_sha", "run_attempt", "created_at", "updated_at")
    result = [
        {field: run.get(field) for field in fields}
        for run in runs
        if isinstance(run, dict) and run.get("head_sha") == head_sha
    ]
    return sorted(result, key=lambda item: (item.get("name") or "", item.get("id") or 0))

def normalize_reviews(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected reviews response format: {payload!r}")
    latest: dict[str, dict[str, Any]] = {}
    for review in payload:
        if not isinstance(review, dict):
            continue
        user = review.get("user") or {}
        login = user.get("login") if isinstance(user, dict) else None
        state = review.get("state")
        if not isinstance(login, str) or not isinstance(state, str):
            continue
        item = {"user": login, "state": state, "submitted_at": review.get("submitted_at")}
        current = latest.get(login)
        if current is None or (item["submitted_at"] or "") >= (current["submitted_at"] or ""):
            latest[login] = item
    return [latest[key] for key in sorted(latest)]

def normalize_pull_requests(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected API response format: {payload!r}")
    result = []
    for pr in payload:
        if not isinstance(pr, dict):
            continue
        head = pr.get("head") or {}
        base = pr.get("base") or {}
        labels = pr.get("labels") if isinstance(pr.get("labels"), list) else []
        result.append({
            "number": pr.get("number"), "state": pr.get("state"),
            "draft": bool(pr.get("draft")),
            "head_sha": head.get("sha") if isinstance(head, dict) else None,
            "head_ref": head.get("ref") if isinstance(head, dict) else None,
            "base_ref": base.get("ref") if isinstance(base, dict) else None,
            "labels": sorted(item.get("name") for item in labels if isinstance(item, dict) and isinstance(item.get("name"), str)),
            "updated_at": pr.get("updated_at"), "reviews": [], "workflow_runs": [],
        })
    return sorted(result, key=lambda item: item.get("number") or 0)

def capture(repository: str, token: str) -> dict[str, Any]:
    repo = api_get(repository, "", token)
    default_branch = repo.get("default_branch")
    branch = api_get(repository, f"branches/{urllib.parse.quote(default_branch, safe='')}", token)
    pull_requests = normalize_pull_requests(api_get(repository, "pulls?state=open&per_page=100", token))
    all_runs: list[dict[str, Any]] = []
    for pr in pull_requests:
        number, head_sha = pr["number"], pr["head_sha"]
        pr["reviews"] = normalize_reviews(api_get(repository, f"pulls/{number}/reviews?per_page=100", token))
        query = urllib.parse.urlencode({"head_sha": head_sha, "per_page": 100})
        pr["workflow_runs"] = normalize_workflow_runs(api_get(repository, f"actions/runs?{query}", token), head_sha)
        all_runs.extend(pr["workflow_runs"])
    return {
        "schema_version": 1,
        "captured_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": {"full_name": repository, "default_branch": default_branch, "main_sha": branch["commit"]["sha"]},
        "pull_requests": pull_requests,
        "workflow_runs": sorted(all_runs, key=lambda item: (item.get("name") or "", item.get("id") or 0)),
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    data = capture(args.repository, os.environ.get("GITHUB_TOKEN", ""))
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
