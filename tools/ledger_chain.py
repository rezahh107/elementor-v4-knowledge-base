"""Append-only SHA-256 chaining for deterministic JSONL ledgers."""
from __future__ import annotations

import hashlib
import json
import os
import time
from copy import deepcopy
from pathlib import Path
from typing import Any, Callable

ZERO_SHA256 = "0" * 64


def event_sha256(event: dict[str, Any], canonical: Callable[[Any], str]) -> str:
    payload = {key: value for key, value in event.items() if key != "event_sha256"}
    return hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()


def _lock_path(path: Path) -> Path:
    return path.with_name(path.name + ".lock")


def _acquire_lock(path: Path) -> int:
    lock = _lock_path(path)
    lock.parent.mkdir(parents=True, exist_ok=True)
    for _ in range(200):
        try:
            return os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            time.sleep(0.01)
    raise TimeoutError(f"could not acquire append lock for {path}")


def _release_lock(path: Path, descriptor: int) -> None:
    os.close(descriptor)
    try:
        _lock_path(path).unlink()
    except FileNotFoundError:
        pass


def load_jsonl(path: Path) -> tuple[bytes, list[dict[str, Any]]]:
    raw = path.read_bytes() if path.exists() else b""
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL") from exc
        if not isinstance(event, dict):
            raise ValueError(f"{path}:{line_number}: event must be an object")
        records.append(event)
    return raw, records


def append_chained_event(
    *,
    path: Path,
    event: dict[str, Any],
    version_field: str,
    canonical: Callable[[Any], str],
    validate: Callable[[dict[str, Any]], list[str]],
) -> dict[str, Any]:
    """Append one chained event without rewriting existing bytes."""
    descriptor = _acquire_lock(path)
    try:
        raw, records = load_jsonl(path)
        duplicates = [record for record in records if record.get("event_id") == event.get("event_id")]
        if duplicates:
            if len(duplicates) == 1:
                return duplicates[0]
            raise ValueError(f"duplicate ledger event id: {event.get('event_id')}")

        chained = deepcopy(event)
        chained[version_field] = 2
        if records and records[-1].get(version_field) == 2:
            previous = records[-1].get("event_sha256")
            if not isinstance(previous, str) or len(previous) != 64:
                raise ValueError("last event has an invalid event_sha256")
            chained["chain_scope"] = "event"
            chained["previous_event_sha256"] = previous
        elif raw:
            chained["chain_scope"] = "legacy_prefix"
            chained["previous_event_sha256"] = hashlib.sha256(raw).hexdigest()
        else:
            chained["chain_scope"] = "genesis"
            chained["previous_event_sha256"] = ZERO_SHA256
        chained["event_sha256"] = event_sha256(chained, canonical)

        errors = validate(chained)
        if errors:
            raise ValueError("; ".join(errors))
        line = (canonical(chained) + "\n").encode("utf-8")
        path.parent.mkdir(parents=True, exist_ok=True)
        file_descriptor = os.open(path, os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o644)
        try:
            os.write(file_descriptor, line)
            os.fsync(file_descriptor)
        finally:
            os.close(file_descriptor)
        return chained
    finally:
        _release_lock(path, descriptor)
