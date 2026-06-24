"""Deterministic primitives for the EDIS rolling queue control plane."""
from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "planning" / "ROLLING_QUEUE.json"
EVENTS_PATH = ROOT / "planning" / "ROLLING_QUEUE_EVENTS.jsonl"
QUEUE_SCHEMA_PATH = ROOT / "schemas" / "rolling-queue.schema.json"
EVENT_SCHEMA_PATH = ROOT / "schemas" / "queue-event.schema.json"

PRIORITY_RANK = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
TERMINAL_STATES = {"completed", "superseded", "cancelled"}
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


def _reject_non_finite(value: Any) -> None:
    if isinstance(value, bool) or value is None or isinstance(value, (str, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("NaN and infinity are forbidden")
        return
    if isinstance(value, list):
        for item in value:
            _reject_non_finite(item)
        return
    if isinstance(value, dict):
        for key in sorted(value):
            if not isinstance(key, str):
                raise TypeError("canonical JSON object keys must be strings")
            _reject_non_finite(value[key])
        return
    raise TypeError(f"unsupported canonical JSON type: {type(value).__name__}")


def canonical_json(value: Any) -> str:
    _reject_non_finite(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_prefixed(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_queue(path: Path = QUEUE_PATH) -> dict[str, Any]:
    value = load_json(path)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: queue root must be an object")
    return value


def validate_schema(instance: Any, schema_path: Path, label: str) -> list[str]:
    validator = Draft202012Validator(load_json(schema_path), format_checker=FormatChecker())
    errors: list[str] = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: tuple(str(part) for part in item.absolute_path)):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{label}:{location}: {error.message}")
    return errors


def validate_spec_hashes(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for task in queue.get("tasks", []):
        expected = sha256_prefixed(task.get("spec"))
        if task.get("spec_hash") != expected:
            errors.append(f"{task.get('id', '<unknown>')}: spec_hash mismatch; expected {expected}")
    return errors


def validate_identity(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    task_ids: set[str] = set()
    work_units: set[str] = set()
    for task in queue.get("tasks", []):
        task_id = task.get("id")
        work_unit = task.get("spec", {}).get("work_unit_id")
        if task_id in task_ids:
            errors.append(f"duplicate task id: {task_id}")
        if work_unit in work_units:
            errors.append(f"duplicate work unit id: {work_unit}")
        if isinstance(task_id, str):
            task_ids.add(task_id)
        if isinstance(work_unit, str):
            work_units.add(work_unit)
    for task in queue.get("tasks", []):
        for dependency in task.get("spec", {}).get("depends_on", []):
            if dependency not in task_ids:
                errors.append(f"{task.get('id')}: unknown dependency {dependency}")
            if dependency == task.get("id"):
                errors.append(f"{task.get('id')}: self dependency is forbidden")
    return errors


def validate_runtime_invariants(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    active_states = {"leased", "executing", "awaiting_external", "needs_review"}
    active = [task for task in queue.get("tasks", []) if task.get("runtime", {}).get("status") in active_states]
    if len(active) > queue.get("controller_policy", {}).get("max_active_tasks", 1):
        errors.append("RQ_ACTIVE_TASK_CONFLICT: more than one task is active")
    active_stage_ids = {
        task["spec"]["stage_id"] for task in active
        if task.get("spec", {}).get("stage_id") is not None
        and task.get("spec", {}).get("task_type") in {
            "stage_authoring", "source_capture", "gap_reconciliation",
            "stage_finalization", "stage_review", "stage_merge"
        }
    }
    if len(active_stage_ids) > queue.get("controller_policy", {}).get("max_active_stage_migrations", 1):
        errors.append("RQ_ACTIVE_STAGE_CONFLICT: multiple stage migrations are active")
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
            leased_at = datetime.fromisoformat(lease["leased_at"])
            expires_at = datetime.fromisoformat(lease["expires_at"])
            if expires_at <= leased_at:
                errors.append(f"{task.get('id')}: lease expiry must follow lease start")
            if state == "leased" and expires_at <= now:
                errors.append(f"{task.get('id')}: stale lease requires recovery")
        if state in TERMINAL_STATES and runtime.get("blockers"):
            errors.append(f"{task.get('id')}: terminal task cannot retain blockers")
    return errors


def validate_queue(queue: dict[str, Any]) -> list[str]:
    errors = validate_schema(queue, QUEUE_SCHEMA_PATH, "ROLLING_QUEUE.json")
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
    return all(tasks_by_id[item]["runtime"]["status"] == "completed" for item in task["spec"]["depends_on"])


def eligible_tasks(queue: dict[str, Any]) -> list[dict[str, Any]]:
    tasks_by_id = {task["id"]: task for task in queue["tasks"]}
    pending = [task for task in queue["tasks"] if task["runtime"]["status"] == "pending" and dependencies_completed(task, tasks_by_id)]
    return sorted(pending, key=lambda task: (PRIORITY_RANK[task["spec"]["priority"]], len(task["spec"]["depends_on"]), task["id"]))
