#!/usr/bin/env python3
"""Validate the v2 suffix of the canonical execution ledger."""
from __future__ import annotations

import hashlib
import json
import sys

from tools.ledger_chain import ZERO_SHA256, event_sha256, load_jsonl
from tools.pipeline_common import LEDGER_PATH, canonical_json_line, validate_instance


def validate() -> list[str]:
    raw, _records = load_jsonl(LEDGER_PATH)
    errors: list[str] = []
    prefix = b""
    previous: str | None = None
    chain_started = False
    lines = raw.splitlines(keepends=True)

    for index, line in enumerate(lines, start=1):
        if not line.strip():
            prefix += line
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"ledger line {index}: invalid JSON: {exc.msg}")
            continue
        if event.get("ledger_version") != 2:
            if chain_started:
                errors.append(f"ledger line {index}: legacy event after v2 chain")
            prefix += line
            continue
        chain_started = True
        errors.extend(validate_instance(event, "execution-event.schema.json", f"ledger line {index}"))
        if event.get("event_sha256") != event_sha256(event, canonical_json_line):
            errors.append(f"ledger line {index}: event_sha256 mismatch")
        if previous is None:
            expected = hashlib.sha256(prefix).hexdigest() if prefix else ZERO_SHA256
            scope = "legacy_prefix" if prefix else "genesis"
        else:
            expected = previous
            scope = "event"
        if event.get("chain_scope") != scope:
            errors.append(f"ledger line {index}: invalid chain_scope")
        if event.get("previous_event_sha256") != expected:
            errors.append(f"ledger line {index}: previous hash mismatch")
        current = event.get("event_sha256")
        previous = current if isinstance(current, str) else previous
    return sorted(set(errors))


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print("EXECUTION_LEDGER_VALID" if not errors else "EXECUTION_LEDGER_INVALID")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
