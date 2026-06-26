#!/usr/bin/env python3
"""Validate the optional append-only v2 execution ledger."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from tools.ledger_chain import ZERO_SHA256, event_sha256
from tools.pipeline_common import ROOT, canonical_json_line, validate_instance

LEDGER_V2_PATH = ROOT / "ledger" / "executions-v2.jsonl"


def validate(path: Path = LEDGER_V2_PATH) -> list[str]:
    if not path.exists():
        return []
    errors: list[str] = []
    events: list[dict[str, object]] = []
    for line_number, raw in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw.strip():
            continue
        try:
            event = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(event, dict):
            errors.append(f"{path}:{line_number}: event must be an object")
            continue
        errors.extend(
            validate_instance(
                event,
                "ledger-event-v2.schema.json",
                f"{path}:{line_number}",
            )
        )
        if canonical_json_line(event) != raw:
            errors.append(f"{path}:{line_number}: event is not canonical JSON")
        if event.get("event_sha256") != event_sha256(event, canonical_json_line):
            errors.append(f"{path}:{line_number}: event_sha256 mismatch")
        events.append(event)

    ids = [event.get("event_id") for event in events]
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"{path}: duplicate event IDs: {duplicates}")

    previous = ZERO_SHA256
    for index, event in enumerate(events):
        expected_scope = "genesis" if index == 0 else "event"
        if event.get("chain_scope") != expected_scope:
            errors.append(f"{path}:{index + 1}: invalid chain_scope")
        if event.get("previous_event_sha256") != previous:
            errors.append(f"{path}:{index + 1}: previous event hash mismatch")
        current = event.get("event_sha256")
        if isinstance(current, str):
            previous = current
    return sorted(set(errors))


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if not errors:
        print("LEDGER_V2_VALID")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
