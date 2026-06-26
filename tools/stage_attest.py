#!/usr/bin/env python3
"""Append a v2 finalization attestation without importing repository code."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml
from jsonschema import Draft202012Validator, FormatChecker

COMMIT_RE = re.compile(r"^[a-f0-9]{40}$")
ZERO_SHA256 = "0" * 64


class StringSafeLoader(yaml.SafeLoader):
    pass


for first_char, resolvers in list(StringSafeLoader.yaml_implicit_resolvers.items()):
    StringSafeLoader.yaml_implicit_resolvers[first_char] = [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]


def canonical(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def event_hash(event: dict[str, object]) -> str:
    payload = {key: value for key, value in event.items() if key != "event_sha256"}
    return hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()


def load_yaml(path: Path) -> dict[str, object]:
    value = yaml.load(path.read_text(encoding="utf-8"), Loader=StringSafeLoader)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be an object")
    return value


def one(records: list[object], field: str, value: str) -> dict[str, object]:
    found = [item for item in records if isinstance(item, dict) and item.get(field) == value]
    if len(found) != 1:
        raise ValueError(f"expected one {field}={value}; found {len(found)}")
    return found[0]


def git_head(repo: Path) -> str:
    completed = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, capture_output=True, text=True, encoding="utf-8")
    return completed.stdout.strip()


def append_event(path: Path, event: dict[str, object], schema: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(path.name + ".lock")
    descriptor: int | None = None
    for _ in range(200):
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            break
        except FileExistsError:
            time.sleep(0.01)
    if descriptor is None:
        raise TimeoutError(f"could not lock {path}")
    try:
        raw = path.read_bytes() if path.exists() else b""
        records = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        if any(item.get("event_id") == event["event_id"] for item in records):
            return
        if records and records[-1].get("ledger_version") == 2:
            event["chain_scope"] = "event"
            event["previous_event_sha256"] = records[-1]["event_sha256"]
        elif raw:
            event["chain_scope"] = "legacy_prefix"
            event["previous_event_sha256"] = hashlib.sha256(raw).hexdigest()
        else:
            event["chain_scope"] = "genesis"
            event["previous_event_sha256"] = ZERO_SHA256
        event["ledger_version"] = 2
        event["event_sha256"] = event_hash(event)
        errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(event), key=lambda item: tuple(str(part) for part in item.absolute_path))
        if errors:
            raise ValueError("; ".join(error.message for error in errors))
        fd = os.open(path, os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o644)
        try:
            os.write(fd, (canonical(event) + "\n").encode("utf-8"))
            os.fsync(fd)
        finally:
            os.close(fd)
    finally:
        os.close(descriptor)
        lock.unlink(missing_ok=True)


def attest(repo: Path, stage_id: str, finalization_commit: str) -> None:
    repo = repo.resolve()
    if not COMMIT_RE.fullmatch(finalization_commit):
        raise ValueError("invalid finalization commit SHA")
    if git_head(repo) != finalization_commit:
        raise ValueError("checkout does not match finalization commit")
    stages = load_yaml(repo / "manifests" / "stages.yaml")
    work_items = load_yaml(repo / "manifests" / "work-items.yaml")
    stage = one(stages.get("stages", []), "stage_id", stage_id)
    item = one(work_items.get("items", []), "stage_id", stage_id)
    content_commit = stage.get("content_commit_sha")
    if not isinstance(content_commit, str) or not COMMIT_RE.fullmatch(content_commit):
        raise ValueError("missing valid content commit SHA")
    if item.get("state") != "machine_validated":
        raise ValueError("Work Item is not machine_validated")
    event: dict[str, object] = {
        "event_id": f"{item['cycle_id']}:{stage_id}:machine-validated:{finalization_commit[:12]}",
        "stage_id": stage_id,
        "event_type": stage["status"],
        "status": stage["status"],
        "recorded_at": datetime.now(ZoneInfo("Europe/Istanbul")).isoformat(timespec="seconds"),
        "content_commit_sha": content_commit,
        "finalization_commit_sha": finalization_commit,
        "output_path": stage["output_path"],
        "notes": [
            "content_commit_sha identifies the evidence input commit",
            "finalization_commit_sha identifies the commit carrying finalization artifacts",
            "review_status remains machine_validated",
        ],
    }
    schema = json.loads((Path(__file__).resolve().parents[1] / "schemas" / "execution-event.schema.json").read_text(encoding="utf-8"))
    append_event(repo / "ledger" / "executions.jsonl", event, schema)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--stage", required=True)
    parser.add_argument("--finalization-commit", required=True)
    args = parser.parse_args()
    try:
        attest(args.repo, args.stage, args.finalization_commit)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
