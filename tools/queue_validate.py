#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from tools.queue_common import EVENTS_PATH, EVENT_SCHEMA_PATH, load_queue, validate_queue, validate_schema


def validate_events() -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    revision = -1
    for number, line in enumerate(EVENTS_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        event = json.loads(line)
        errors.extend(validate_schema(event, EVENT_SCHEMA_PATH, f"event:{number}"))
        if event["event_id"] in seen:
            errors.append(f"event:{number}: duplicate event id")
        seen.add(event["event_id"])
        if event["queue_revision"] < revision:
            errors.append(f"event:{number}: queue revision regressed")
        revision = event["queue_revision"]
    return errors


def main() -> int:
    errors = validate_queue(load_queue()) + validate_events()
    for error in sorted(set(errors)):
        print(f"ERROR: {error}", file=sys.stderr)
    if not errors:
        print("ROLLING_QUEUE_VALID")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
