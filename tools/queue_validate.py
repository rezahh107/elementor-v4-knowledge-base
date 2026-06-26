#!/usr/bin/env python3
"""Validate the EDIS rolling queue, event ledger, and deterministic task specs."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.queue_common import (
    EVENTS_PATH,
    EVENT_SCHEMA_PATH,
    QUEUE_PATH,
    ZERO_SHA256,
    event_sha256,
    load_queue,
    validate_queue,
    validate_schema,
)


def validate_events(path: Path = EVENTS_PATH) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    previous_revision = -1
    if not path.exists():
        return [f"{path}: missing event ledger"]

    raw_lines = path.read_bytes().splitlines(keepends=True)
    prefix = b""
    previous_chained_hash: str | None = None
    chain_started = False
    for line_number, raw_line in enumerate(raw_lines, 1):
        try:
            line = raw_line.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid UTF-8: {exc}")
            prefix += raw_line
            continue
        if not line.strip():
            prefix += raw_line
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid JSON: {exc.msg}")
            prefix += raw_line
            continue
        schema_errors = validate_schema(
            event, EVENT_SCHEMA_PATH, f"{path}:{line_number}"
        )
        if schema_errors:
            errors.extend(schema_errors)
            prefix += raw_line
            continue
        event_id = event.get("event_id")
        if event_id in seen:
            errors.append(f"{path}:{line_number}: duplicate event_id {event_id}")
        if isinstance(event_id, str):
            seen.add(event_id)
        revision = event.get("queue_revision")
        if isinstance(revision, int) and revision < previous_revision:
            errors.append(f"{path}:{line_number}: queue revision regressed")
        if isinstance(revision, int):
            previous_revision = revision

        if event.get("schema_version") == 2:
            chain_scope = event.get("chain_scope")
            previous = event.get("previous_event_sha256")
            if event.get("event_sha256") != event_sha256(event):
                errors.append(f"{path}:{line_number}: event_sha256 mismatch")
            if chain_scope == "genesis":
                if prefix or previous != ZERO_SHA256:
                    errors.append(f"{path}:{line_number}: invalid genesis chain anchor")
            elif chain_scope == "legacy_prefix":
                expected = hashlib.sha256(prefix).hexdigest()
                if chain_started or previous != expected:
                    errors.append(f"{path}:{line_number}: invalid legacy-prefix chain anchor")
            elif chain_scope == "event":
                if previous_chained_hash is None or previous != previous_chained_hash:
                    errors.append(f"{path}:{line_number}: previous event hash mismatch")
            chain_started = True
            previous_chained_hash = event.get("event_sha256")
        elif chain_started:
            errors.append(f"{path}:{line_number}: legacy event appears after chain start")
        prefix += raw_line
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        choices=["all", "queue", "events"],
        nargs="?",
        default="all",
    )
    args = parser.parse_args()
    errors: list[str] = []
    if args.target in {"all", "queue"}:
        errors.extend(validate_queue(load_queue(QUEUE_PATH)))
    if args.target in {"all", "events"}:
        errors.extend(validate_events(EVENTS_PATH))
    for error in sorted(set(errors)):
        print(f"ERROR: {error}", file=sys.stderr)
    if not errors:
        print("ROLLING_QUEUE_VALID")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
