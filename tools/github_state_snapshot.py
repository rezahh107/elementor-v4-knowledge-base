#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import urllib.request
from typing import Any


def build_request(repository: str, token: str = "") -> urllib.request.Request:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/pulls?state=open"
    )
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    request.add_header("Accept", "application/vnd.github+json")
    return request


def normalize_pull_requests(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected API response format: {payload!r}")

    normalized: list[dict[str, Any]] = []
    for pull_request in payload:
        if not isinstance(pull_request, dict):
            continue
        head = pull_request.get("head") or {}
        if not isinstance(head, dict):
            head = {}
        normalized.append(
            {
                "number": pull_request.get("number"),
                "state": pull_request.get("state"),
                "draft": pull_request.get("draft"),
                "head_sha": head.get("sha"),
                "head_ref": head.get("ref"),
            }
        )
    return normalized


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    request = build_request(args.repository, os.environ.get("GITHUB_TOKEN", ""))
    with urllib.request.urlopen(request) as response:
        payload = json.load(response)

    data = {
        "pull_requests": normalize_pull_requests(payload),
        "workflow_runs": [],
    }
    with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
