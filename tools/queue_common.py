"""Deterministic primitives for the EDIS rolling queue control plane."""
from __future__ import annotations

import hashlib
import json
import math
import os
import time
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "planning" / "ROLLING_QUEUE.json"
EVENTS_PATH = ROOT / "planning" / "ROLLING_QUEUE_EVENTS.jsonl"
QUEUE_STATUS_PATH = ROOT / "planning" / "QUEUE_STATUS.md"
QUEUE_SCHEMA_PATH = ROOT / "schemas" / "rolling-queue.schema.json"
EVENT_SCHEMA_PATH = ROOT / "schemas" / "queue-event.schema.json"
WORK_ITEMS_PATH = ROOT / "manifests" / "work-items.yaml"
STATUS_PATH = ROOT / "STATUS.md"

PRIORITY_RANK = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
_VALIDATOR_CACHE: dict[Path, Draft202012Validator] = {}
TERMINAL_STATES = {"completed", "superseded", "cancelled"}
MAX_CANONICAL_DEPTH = 128
ZERO_SHA256 = "0" * 64
ALLOWED_TRANSITIONS = {
    "pending": {"leased", "blocked", "cancelled"},
    "leased": {"executing", "pending", "blocked"},
    "executing": {"awaiting_external", "needs_review", "blocked", "completed"},
    "awaiting_external": {"executing", "needs_review", "blocked"},
    "needs_review": {"executing", "completed", "blocked"},
    "blocked": {"pending", "superseded", "cancelled"},
    "completed": set(),
    "superseded": set(),
    "cancelled": set(),
}


def _reject_non_finite(
    value: Any,
    *,
    active: set[int] | None = None,
    depth: int = 0,
) -> None:
    if depth > MAX_CANONICAL_DEPTH:
        raise TypeError(f"canonical JSON exceeds maximum depth {MAX_CANONICAL_DEPTH}")
    if isinstance(value, bool) or value is None or isinstance(value, (str, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("NaN and infinity are forbidden")
        return
    if not isinstance(value, (list, dict)):
        raise TypeError(f"unsupported canonical JSON type: {type(value).__name__}")

    if active is None:
        active = set()
    identity = id(value)
    if identity in active:
        raise TypeError("canonical JSON contains a reference cycle")
    active.add(identity)
    try:
        if isinstance(value, list):
            for item in value:
                _reject_non_finite(item, active=active, depth=depth + 1)
        else:
            for key in sorted(value):
                if not isinstance(key, str):
                    raise TypeError("canonical JSON object keys must be strings")
                _reject_non_finite(value[key], active=active, depth=depth + 1)
    finally:
        active.remove(identity)


def canonical_json(value: Any) -> str:
    """Serialize version-1 canonical JSON used for hashing and JSONL."""
    _reject_non_finite(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def sha256_prefixed(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def event_sha256(event: dict[str, Any]) -> str:
    payload = {key: value for key, value in event.items() if key != "event_sha256"}
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def load_queue(path: Path = QUEUE_PATH) -> dict[str, Any]:
    value = load_json(path)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: queue root must be an object")
    return value


def load_schema(path: Path) -> dict[str, Any]:
    value = load_json(path)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: schema root must be an object")
    return value


def validate_schema(instance: Any, schema_path: Path, label: str) -> list[str]:
    validator = _VALIDATOR_CACHE.get(schema_path)
    if validator is None:
        validator = Draft202012Validator(
            load_schema(schema_path),
            format_checker=FormatChecker(),
        )
        _VALIDATOR_CACHE[schema_path] = validator
    errors: list[str] = []
    for error in sorted(
        validator.iter_errors(instance),
        key=lambda item: tuple(str(part) for part in item.absolute_path),
    ):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{label}:{location}: {error.message}")
    return errors


def validate_spec_hashes(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for task in queue.get("tasks", []):
        expected = sha256_prefixed(task.get("spec"))
        if task.get("spec_hash") != expected:
            errors.append(
                f"{task.get('id', '<unknown>')}: spec_hash mismatch; "
                f"expected {expected}, got {task.get('spec_hash')}"
            )
    return errors


def _canonical_cycle(nodes: list[str]) -> tuple[str, ...]:
    """Return a stable rotation for one closed dependency cycle."""
    ring = nodes[:-1]
    rotations = [tuple(ring[index:] + ring[:index]) for index in range(len(ring))]
    chosen = min(rotations)
    return chosen + (chosen[0],)


def _dependency_cycles(tasks_by_id: dict[str, dict[str, Any]]) -> list[tuple[str, ...]]:
    state: dict[str, int] = {task_id: 0 for task_id in tasks_by_id}
    stack: list[str] = []
    position: dict[str, int] = {}
    cycles: set[tuple[str, ...]] = set()

    def visit(task_id: str) -> None:
        state[task_id] = 1
        position[task_id] = len(stack)
        stack.append(task_id)
        dependencies = tasks_by_id[task_id].get("spec", {}).get("depends_on", [])
        for dependency in sorted(item for item in dependencies if item in tasks_by_id):
            if state[dependency] == 0:
                visit(dependency)
            elif state[dependency] == 1:
                start = position[dependency]
                cycles.add(_canonical_cycle(stack[start:] + [dependency]))
        stack.pop()
        position.pop(task_id, None)
        state[task_id] = 2

    for task_id in sorted(tasks_by_id):
        if state[task_id] == 0:
            visit(task_id)
    return sorted(cycles)


def validate_identity(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    task_ids: set[str] = set()
    work_unit_ids: set[str] = set()
    tasks_by_id: dict[str, dict[str, Any]] = {}
    for task in queue.get("tasks", []):
        task_id = task.get("id")
        work_unit_id = task.get("spec", {}).get("work_unit_id")
        if task_id in task_ids:
            errors.append(f"duplicate task id: {task_id}")
        if work_unit_id in work_unit_ids:
            errors.append(f"duplicate work unit id: {work_unit_id}")
        if isinstance(task_id, str):
            task_ids.add(task_id)
            tasks_by_id.setdefault(task_id, task)
        if isinstance(work_unit_id, str):
            work_unit_ids.add(work_unit_id)
    for task in queue.get("tasks", []):
        task_id = task.get("id", "<unknown>")
        for dependency in task.get("spec", {}).get("depends_on", []):
            if dependency not in task_ids:
                errors.append(f"{task_id}: unknown dependency {dependency}")
            if dependency == task_id:
                errors.append(f"{task_id}: self dependency is forbidden")
    for cycle in _dependency_cycles(tasks_by_id):
        errors.append("dependency cycle: " + " -> ".join(cycle))
    return errors


def validate_runtime_invariants(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    active = [
        task
        for task in queue.get("tasks", [])
        if task.get("runtime", {}).get("status")
        in {"leased", "executing", "awaiting_external", "needs_review"}
    ]
    if len(active) > queue.get("controller_policy", {}).get("max_active_tasks", 1):
        errors.append("RQ_ACTIVE_TASK_CONFLICT: more than one task is active")

    active_stage_tasks = [
        task
        for task in active
        if task.get("spec", {}).get("stage_id") is not None
        and task.get("spec", {}).get("task_type")
        in {
            "stage_authoring",
            "source_capture",
            "gap_reconciliation",
            "stage_finalization",
            "stage_review",
            "stage_merge",
        }
    ]
    stage_ids = [task["spec"]["stage_id"] for task in active_stage_tasks]
    if len(set(stage_ids)) > queue.get("controller_policy", {}).get(
        "max_active_stage_migrations", 1
    ):
        errors.append("RQ_ACTIVE_STAGE_CONFLICT: multiple stage migrations are active")

    timezone_name = queue.get("controller_policy", {}).get("timezone", "Europe/Istanbul")
    try:
        now = datetime.now(ZoneInfo(timezone_name))
    except (KeyError, TypeError, ValueError):
        errors.append(f"RQ_TIMEZONE_INVALID: {timezone_name!r}")
        now = datetime.now(ZoneInfo("Europe/Istanbul"))
    for task in queue.get("tasks", []):
        runtime = task.get("runtime", {})
        state = runtime.get("status")
        lease = runtime.get("lease")
        if state == "leased" and lease is None:
            errors.append(f"{task.get('id')}: leased task has no lease")
        if state != "leased" and lease is not None:
            errors.append(f"{task.get('id')}: non-leased task retains a lease")
        if lease:
            try:
                leased_at = datetime.fromisoformat(lease["leased_at"])
                expires_at = datetime.fromisoformat(lease["expires_at"])
            except (KeyError, TypeError, ValueError):
                errors.append(f"{task.get('id')}: lease timestamps must be valid ISO-8601 strings")
            else:
                if leased_at.tzinfo is None or expires_at.tzinfo is None:
                    errors.append(f"{task.get('id')}: lease timestamps need offsets")
                elif expires_at <= leased_at:
                    errors.append(f"{task.get('id')}: lease expiry must follow lease start")
                if state == "leased" and expires_at <= now:
                    errors.append(f"{task.get('id')}: stale lease requires recovery")
        if state in TERMINAL_STATES and runtime.get("blockers"):
            errors.append(f"{task.get('id')}: terminal task cannot retain blockers")
    return errors


def validate_queue(queue: dict[str, Any]) -> list[str]:
    errors = validate_schema(queue, QUEUE_SCHEMA_PATH, "ROLLING_QUEUE.json")
    if errors:
        return sorted(set(errors))
    errors.extend(validate_spec_hashes(queue))
    errors.extend(validate_identity(queue))
    errors.extend(validate_runtime_invariants(queue))
    return sorted(set(errors))


def transition_task(task: dict[str, Any], target: str) -> None:
    current = task["runtime"]["status"]
    if target == current:
        return
    if target not in ALLOWED_TRANSITIONS.get(current, set()):
        raise ValueError(f"RQ_ILLEGAL_TRANSITION: {current} -> {target}")
    task["runtime"]["status"] = target
    if current == "leased":
        task["runtime"]["lease"] = None


def dependencies_completed(task: dict[str, Any], tasks_by_id: dict[str, dict[str, Any]]) -> bool:
    return all(
        tasks_by_id.get(dependency, {}).get("runtime", {}).get("status") == "completed"
        for dependency in task.get("spec", {}).get("depends_on", [])
    )


def eligible_tasks(queue: dict[str, Any]) -> list[dict[str, Any]]:
    tasks_by_id = {task["id"]: task for task in queue["tasks"]}
    pending = [
        task
        for task in queue["tasks"]
        if task["runtime"]["status"] == "pending"
        and dependencies_completed(task, tasks_by_id)
    ]
    return sorted(
        pending,
        key=lambda task: (
            PRIORITY_RANK[task["spec"]["priority"]],
            len(task["spec"]["depends_on"]),
            task["id"],
        ),
    )


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


def _load_event_lines(path: Path) -> tuple[bytes, list[dict[str, Any]]]:
    raw = path.read_bytes() if path.exists() else b""
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: event must be an object")
        records.append(value)
    return raw, records


def append_event(event: dict[str, Any], path: Path = EVENTS_PATH) -> None:
    """Append one schema-v2 hash-chained event under an exclusive file lock."""
    descriptor = _acquire_lock(path)
    try:
        raw, existing = _load_event_lines(path)
        if any(item.get("event_id") == event.get("event_id") for item in existing):
            raise ValueError(f"duplicate queue event id: {event.get('event_id')}")

        chained = deepcopy(event)
        chained["schema_version"] = 2
        if existing and existing[-1].get("schema_version") == 2:
            previous = existing[-1].get("event_sha256")
            if not isinstance(previous, str) or len(previous) != 64:
                raise ValueError("last queue event has an invalid event_sha256")
            chained["chain_scope"] = "event"
            chained["previous_event_sha256"] = previous
        elif raw:
            chained["chain_scope"] = "legacy_prefix"
            chained["previous_event_sha256"] = hashlib.sha256(raw).hexdigest()
        else:
            chained["chain_scope"] = "genesis"
            chained["previous_event_sha256"] = ZERO_SHA256
        chained["event_sha256"] = event_sha256(chained)

        errors = validate_schema(chained, EVENT_SCHEMA_PATH, "queue event")
        if errors:
            raise ValueError("; ".join(errors))
        line = (canonical_json(chained) + "\n").encode("utf-8")
        path.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(path, os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o644)
        try:
            os.write(fd, line)
            os.fsync(fd)
        finally:
            os.close(fd)
    finally:
        _release_lock(path, descriptor)
