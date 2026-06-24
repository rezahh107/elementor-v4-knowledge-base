#!/usr/bin/env python3
"""Validate the EDIS rolling queue, event ledger, and deterministic task specs."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.queue_common import (
    EVENTS_PATH,
    EVENT_SCHEMA_PATH,
    QUEUE_PATH,
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
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid JSON: {exc.msg}")
            continue
        schema_errors = validate_schema(
            event, EVENT_SCHEMA_PATH, f"{path}:{line_number}"
        )
        if schema_errors:
            errors.extend(schema_errors)
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
