"""Shared deterministic primitives for source capture and stage finalization."""
from __future__ import annotations

import json
import math
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
STAGES_PATH = ROOT / "manifests" / "stages.yaml"
WORK_ITEMS_PATH = ROOT / "manifests" / "work-items.yaml"
LEDGER_PATH = ROOT / "ledger" / "executions.jsonl"
SCHEMAS_DIR = ROOT / "schemas"
STAGE_RE = re.compile(r"KB-[0-9]{3}")

ALLOWED_STATES = {
    "not_started",
    "authoring_running",
    "evidence_draft",
    "finalization_pending",
    "ci_running",
    "ci_failed",
    "machine_validated",
    "merged",
    "blocked",
}
ALLOWED_TRANSITIONS = {
    "not_started": {"authoring_running", "blocked"},
    "authoring_running": {"evidence_draft", "blocked"},
    "evidence_draft": {"finalization_pending", "blocked"},
    "finalization_pending": {"ci_running", "blocked"},
    "ci_running": {"machine_validated", "ci_failed", "blocked"},
    "ci_failed": {"finalization_pending", "blocked"},
    "machine_validated": {"merged", "blocked"},
    "merged": set(),
    "blocked": {"authoring_running", "evidence_draft", "finalization_pending"},
}


class StringSafeLoader(yaml.SafeLoader):
    """Preserve YAML dates and timestamps as strings."""


for first_char, resolvers in list(StringSafeLoader.yaml_implicit_resolvers.items()):
    StringSafeLoader.yaml_implicit_resolvers[first_char] = [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return yaml.load(handle, Loader=StringSafeLoader)


def dump_yaml(value: Any) -> str:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        sort_keys=False,
        width=120,
        default_flow_style=False,
    )


def write_yaml(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_yaml(value), encoding="utf-8", newline="\n")


def now_istanbul() -> str:
    return datetime.now(ZoneInfo("Europe/Istanbul")).isoformat(timespec="seconds")


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMAS_DIR / name).read_text(encoding="utf-8"))


def validate_instance(instance: Any, schema_name: str, label: str) -> list[str]:
    validator = Draft202012Validator(
        load_schema(schema_name),
        format_checker=FormatChecker(),
    )
    errors: list[str] = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path)):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{label}:{location}: {error.message}")
    return errors


def load_stages() -> dict[str, Any]:
    value = load_yaml(STAGES_PATH)
    if not isinstance(value, dict) or not isinstance(value.get("stages"), list):
        raise ValueError("invalid manifests/stages.yaml")
    return value


def load_work_items() -> dict[str, Any]:
    value = load_yaml(WORK_ITEMS_PATH)
    if not isinstance(value, dict) or not isinstance(value.get("items"), list):
        raise ValueError("invalid manifests/work-items.yaml")
    return value


def find_stage(document: dict[str, Any], stage_id: str) -> dict[str, Any]:
    records = [item for item in document["stages"] if item.get("stage_id") == stage_id]
    if len(records) != 1:
        raise ValueError(f"expected one stage {stage_id}; found {len(records)}")
    return records[0]


def find_work_item(document: dict[str, Any], stage_id: str) -> dict[str, Any]:
    records = [item for item in document["items"] if item.get("stage_id") == stage_id]
    if len(records) != 1:
        raise ValueError(f"expected one work item for {stage_id}; found {len(records)}")
    return records[0]


def infer_stage(branch: str) -> str:
    match = STAGE_RE.search(branch)
    if not match:
        raise ValueError(f"cannot infer a stage from branch {branch!r}")
    stage_id = match.group(0)
    find_stage(load_stages(), stage_id)
    return stage_id


def transition(item: dict[str, Any], target: str, error: str | None = None) -> None:
    current = item["state"]
    if target not in ALLOWED_STATES:
        raise ValueError(f"unknown state {target}")
    if target != current and target not in ALLOWED_TRANSITIONS[current]:
        raise ValueError(f"invalid transition {current} -> {target}")
    item["state"] = target
    item["updated_at"] = now_istanbul()
    item["last_error"] = error


def canonical_json_line(value: Any) -> str:
    def reject_non_finite(item: Any) -> None:
        if isinstance(item, float) and not math.isfinite(item):
            raise ValueError("NaN and infinity are forbidden")
        if isinstance(item, dict):
            for key in sorted(item):
                reject_non_finite(item[key])
        elif isinstance(item, list):
            for child in item:
                reject_non_finite(child)

    reject_non_finite(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def append_ledger_event(event: dict[str, Any]) -> None:
    records: list[dict[str, Any]] = []
    if LEDGER_PATH.exists():
        records = [
            json.loads(line)
            for line in LEDGER_PATH.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    if any(record.get("event_id") == event["event_id"] for record in records):
        return
    records.append(event)
    LEDGER_PATH.write_text(
        "\n".join(canonical_json_line(record) for record in records) + "\n",
        encoding="utf-8",
        newline="\n",
    )
