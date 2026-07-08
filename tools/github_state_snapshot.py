#!/usr/bin/env python3
"""Capture deterministic GitHub state for the Work Package planner and lifecycle reconciler."""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

API = "https://api.github.com"
GRAPHQL = "https://api.github.com/graphql"
PER_PAGE = 100
MAX_PAGES = 1000
DECISIVE_REVIEW_STATES = {"APPROVED", "CHANGES_REQUESTED", "DISMISSED"}
STAGE_RE = re.compile(r"(KB-[0-9]{3})")


def build_request(repository: str, token: str = "", endpoint: str = "pulls?state=open&per_page=100") -> urllib.request.Request:
    url = f"{API}/repos/{repository}"
    if endpoint:
        url = f"{url}/{endpoint}"
    request = urllib.request.Request(url)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    return request


def api_get(repository: str, endpoint: str, token: str) -> Any:
    request = build_request(repository, token, endpoint)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def graphql_request(token: str, query: str, variables: dict[str, Any]) -> Any:
    body = json.dumps({"query": query, "variables": variables}, sort_keys=True, allow_nan=False).encode("utf-8")
    request = urllib.request.Request(GRAPHQL, data=body, method="POST")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("Content-Type", "application/json")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors"):
        raise RuntimeError(f"GitHub GraphQL errors: {payload['errors']!r}")
    return payload.get("data")


def _paged_endpoint(endpoint: str, page: int) -> str:
    path, _separator, raw_query = endpoint.partition("?")
    query = [
        (key, value)
        for key, value in urllib.parse.parse_qsl(raw_query, keep_blank_values=True)
        if key not in {"page", "per_page"}
    ]
    query.extend((("per_page", str(PER_PAGE)), ("page", str(page))))
    return f"{path}?{urllib.parse.urlencode(query)}"


def api_get_all_list(repository: str, endpoint: str, token: str) -> list[Any]:
    items: list[Any] = []
    for page in range(1, MAX_PAGES + 1):
        payload = api_get(repository, _paged_endpoint(endpoint, page), token)
        if not isinstance(payload, list):
            raise ValueError(f"Unexpected paginated response format: {payload!r}")
        items.extend(payload)
        if len(payload) < PER_PAGE:
            return items
    raise RuntimeError(f"GitHub pagination exceeded {MAX_PAGES} pages for {endpoint}")


def api_get_all_workflow_runs(repository: str, endpoint: str, token: str) -> dict[str, Any]:
    runs: list[Any] = []
    for page in range(1, MAX_PAGES + 1):
        payload = api_get(repository, _paged_endpoint(endpoint, page), token)
        page_runs = payload.get("workflow_runs") if isinstance(payload, dict) else None
        if not isinstance(page_runs, list):
            raise ValueError(f"Unexpected workflow response format: {payload!r}")
        runs.extend(page_runs)
        if len(page_runs) < PER_PAGE:
            return {"workflow_runs": runs}
    raise RuntimeError("GitHub workflow pagination exceeded 1000 pages")


def infer_stage(*values: Any) -> str | None:
    for value in values:
        if isinstance(value, str):
            match = STAGE_RE.search(value)
            if match:
                return match.group(1)
    return None


def normalize_workflow_runs(payload: Any, head_sha: str) -> list[dict[str, Any]]:
    runs = payload.get("workflow_runs") if isinstance(payload, dict) else None
    if not isinstance(runs, list):
        raise ValueError(f"Unexpected workflow response format: {payload!r}")
    fields = (
        "id",
        "name",
        "display_title",
        "event",
        "status",
        "conclusion",
        "head_sha",
        "run_attempt",
        "created_at",
        "updated_at",
    )
    result = [
        {field: run.get(field) for field in fields}
        for run in runs
        if isinstance(run, dict) and run.get("head_sha") == head_sha
    ]
    return sorted(result, key=lambda item: (item.get("name") or "", item.get("display_title") or "", item.get("id") or 0))


def normalize_reviews(payload: Any) -> list[dict[str, Any]]:
    """Preserve blocking review state until approval or dismissal."""
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected reviews response format: {payload!r}")
    ordered_reviews = sorted((review for review in payload if isinstance(review, dict)), key=lambda review: (review.get("submitted_at") or "", review.get("id") or 0))
    latest: dict[str, dict[str, Any]] = {}
    for review in ordered_reviews:
        user = review.get("user") or {}
        login = user.get("login") if isinstance(user, dict) else None
        state = review.get("state")
        if not isinstance(login, str) or not isinstance(state, str):
            continue
        item = {"user": login, "state": state, "submitted_at": review.get("submitted_at")}
        current = latest.get(login)
        if state in DECISIVE_REVIEW_STATES:
            latest[login] = item
        elif current is None or current.get("state") not in DECISIVE_REVIEW_STATES:
            latest[login] = item
    return [latest[key] for key in sorted(latest)]


def _required_graphql_object(value: Any, name: str, pr_number: int) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"GitHub GraphQL response lacks {name} for PR {pr_number}")
    return value


def normalize_review_threads(repository: str, number: int, token: str) -> list[dict[str, Any]]:
    owner, name = repository.split("/", 1)
    query = """
    query($owner: String!, $name: String!, $number: Int!, $after: String) {
      repository(owner: $owner, name: $name) {
        pullRequest(number: $number) {
          reviewThreads(first: 100, after: $after) {
            nodes {
              id
              isResolved
              isOutdated
              path
              line
              startLine
              comments(first: 100) {
                nodes {
                  id
                  body
                  createdAt
                  author { login }
                  path
                  line
                  commit { oid }
                }
              }
            }
            pageInfo { hasNextPage endCursor }
          }
        }
      }
    }
    """
    after: str | None = None
    threads: list[dict[str, Any]] = []
    for _page in range(MAX_PAGES):
        data = graphql_request(token, query, {"owner": owner, "name": name, "number": number, "after": after})
        if not isinstance(data, dict):
            raise ValueError(f"GitHub GraphQL response is not an object for PR {number}")
        repository_node = _required_graphql_object(data.get("repository"), "repository", number)
        pull_request_node = _required_graphql_object(repository_node.get("pullRequest"), "pullRequest", number)
        block = pull_request_node.get("reviewThreads")
        if not isinstance(block, dict):
            raise ValueError(f"GitHub GraphQL response lacks reviewThreads for PR {number}")
        nodes = block.get("nodes") or []
        for node in nodes:
            if not isinstance(node, dict):
                continue
            comments = []
            for comment in (node.get("comments") or {}).get("nodes") or []:
                if not isinstance(comment, dict):
                    continue
                author = comment.get("author") or {}
                commit = comment.get("commit") or {}
                comments.append(
                    {
                        "comment_id": comment.get("id"),
                        "author_login": author.get("login") if isinstance(author, dict) else None,
                        "body": comment.get("body"),
                        "created_at": comment.get("createdAt"),
                        "path": comment.get("path"),
                        "line": comment.get("line"),
                        "commit_sha": commit.get("oid") if isinstance(commit, dict) else None,
                    }
                )
            first_body = comments[0].get("body") if comments else None
            threads.append(
                {
                    "thread_id": node.get("id"),
                    "is_resolved": bool(node.get("isResolved")),
                    "is_outdated": bool(node.get("isOutdated")),
                    "path": node.get("path"),
                    "line": node.get("line"),
                    "start_line": node.get("startLine"),
                    "body": first_body,
                    "comments": sorted(comments, key=lambda item: (item.get("created_at") or "", item.get("comment_id") or "")),
                }
            )
        page_info = block.get("pageInfo") or {}
        if not page_info.get("hasNextPage"):
            break
        after = page_info.get("endCursor")
    return sorted(threads, key=lambda item: item.get("thread_id") or "")


def normalize_pull_requests(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected API response format: {payload!r}")
    result = []
    for pull_request in payload:
        if not isinstance(pull_request, dict):
            continue
        head = pull_request.get("head") or {}
        base = pull_request.get("base") or {}
        raw_labels = pull_request.get("labels")
        labels = raw_labels if isinstance(raw_labels, list) else []
        head_ref = head.get("ref") if isinstance(head, dict) else None
        title = pull_request.get("title")
        body = pull_request.get("body")
        result.append(
            {
                "number": pull_request.get("number"),
                "state": pull_request.get("state"),
                "draft": bool(pull_request.get("draft")),
                "merged": bool(pull_request.get("merged")),
                "mergeable": pull_request.get("mergeable"),
                "head_sha": head.get("sha") if isinstance(head, dict) else None,
                "head_ref": head_ref,
                "base_ref": base.get("ref") if isinstance(base, dict) else None,
                "stage_id": infer_stage(head_ref, title, body),
                "labels": sorted(item.get("name") for item in labels if isinstance(item, dict) and isinstance(item.get("name"), str)),
                "updated_at": pull_request.get("updated_at"),
                "title": title,
                "body": body,
                "reviews": [],
                "review_threads": [],
                "workflow_runs": [],
            }
        )
    return sorted(result, key=lambda item: item.get("number") or 0)


def capture(repository: str, token: str) -> dict[str, Any]:
    repo = api_get(repository, "", token)
    default_branch = repo.get("default_branch")
    if not isinstance(default_branch, str) or not default_branch:
        raise ValueError("GitHub repository response lacks a default branch")
    branch = api_get(repository, f"branches/{urllib.parse.quote(default_branch, safe='')}", token)
    pull_requests = normalize_pull_requests(api_get_all_list(repository, "pulls?state=open", token))
    all_runs: list[dict[str, Any]] = []
    for pull_request in pull_requests:
        number = pull_request["number"]
        head_sha = pull_request["head_sha"]
        if not isinstance(number, int) or not isinstance(head_sha, str):
            raise ValueError(f"Open PR lacks stable number or head SHA: {pull_request!r}")
        pull_request["reviews"] = normalize_reviews(api_get_all_list(repository, f"pulls/{number}/reviews", token))
        pull_request["review_threads"] = normalize_review_threads(repository, number, token)
        query = urllib.parse.urlencode({"head_sha": head_sha})
        run_payload = api_get_all_workflow_runs(repository, f"actions/runs?{query}", token)
        pull_request["workflow_runs"] = normalize_workflow_runs(run_payload, head_sha)
        all_runs.extend(pull_request["workflow_runs"])
    return {
        "schema_version": 1,
        "captured_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": {
            "full_name": repository,
            "default_branch": default_branch,
            "main_sha": branch["commit"]["sha"],
        },
        "pull_requests": pull_requests,
        "workflow_runs": sorted(all_runs, key=lambda item: (item.get("name") or "", item.get("display_title") or "", item.get("id") or 0)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    data = capture(args.repository, os.environ.get("GITHUB_TOKEN", ""))
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
