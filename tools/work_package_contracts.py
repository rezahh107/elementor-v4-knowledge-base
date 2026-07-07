"""Deterministic Work Package contract validation."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DOCS = {
    "catalog": Path("planning/WORK_PACKAGE_CATALOG.json"),
    "queue": Path("planning/WORK_PACKAGE_QUEUE.json"),
    "control": Path("config/work-package-planner.json"),
}
SCHEMAS = {
    "catalog": Path("schemas/work-package-catalog.schema.json"),
    "queue": Path("schemas/work-package-queue.schema.json"),
    "control": Path("schemas/work-package-planner.schema.json"),
}
FORBIDDEN = {
    "keepalive", "placeholder", "reserve work package", "status update only",
    "status-only", "bookkeeping", "merge finalization only", "checkpoint only",
    "isolated guard", "micro-task",
}
REQUIRED_DELIVERABLES = {
    "source_inventory", "normalized_knowledge_entries", "version_scope",
    "provenance_metadata", "limitations_and_uncertainty",
    "validator_integration", "CI_integration",
}

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def load_documents(root: Path = ROOT) -> dict[str, Any]:
    return {name: load_json(root / path) for name, path in DOCS.items()}

def _schema_errors(value: Any, schema: dict[str, Any], code: str) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    result = []
    for error in sorted(validator.iter_errors(value), key=lambda e: (list(e.absolute_path), e.message)):
        location = "/".join(map(str, error.absolute_path)) or "<root>"
        result.append(f"{code}:{location}:{error.message}")
    return result

def validate_documents(documents: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for name in ("catalog", "queue", "control"):
        try:
            errors += _schema_errors(
                documents.get(name), load_json(root / SCHEMAS[name]),
                f"WP_SCHEMA_{name.upper()}",
            )
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"WP_SCHEMA_LOAD_FAILED:{name}:{exc}")
    if not all(isinstance(documents.get(name), dict) for name in DOCS):
        return sorted(set(errors))

    catalog = documents["catalog"]
    queue = documents["queue"]
    control = documents["control"]
    raw_packages = catalog.get("work_packages", [])
    packages: dict[str, dict[str, Any]] = {}
    for package in raw_packages if isinstance(raw_packages, list) else []:
        if not isinstance(package, dict) or not isinstance(package.get("id"), str):
            continue
        package_id = package["id"]
        if package_id in packages:
            errors.append(f"WP_DUPLICATE_ID:{package_id}")
        packages[package_id] = package

    policy = catalog.get("policy") if isinstance(catalog.get("policy"), dict) else {}
    thresholds = [policy.get(key) for key in (
        "refresh_when_ready_below", "ready_work_package_target", "max_ready_work_packages"
    )]
    if all(isinstance(value, int) for value in thresholds) and not thresholds[0] <= thresholds[1] <= thresholds[2]:
        errors.append("WP_REPLENISHMENT_THRESHOLDS_INVALID")
    if policy.get("state_driven_refresh") is not True:
        errors.append("WP_STATE_DRIVEN_REFRESH_REQUIRED")
    if policy.get("fixed_ordinal_refresh_forbidden") is not True:
        errors.append("WP_FIXED_ORDINAL_POLICY_REQUIRED")

    queue_policy = queue.get("policy") if isinstance(queue.get("policy"), dict) else {}
    if queue_policy.get("fixed_ordinal_refresh") is not False:
        errors.append("WP_FIXED_ORDINAL_REFRESH")
    if queue_policy.get("queue_depth_is_not_a_completion_metric") is not True:
        errors.append("WP_QUEUE_DEPTH_COMPLETION_METRIC_FORBIDDEN")

    ready = queue.get("ready_work_packages") if isinstance(queue.get("ready_work_packages"), list) else []
    blocked = queue.get("blocked_work_packages") if isinstance(queue.get("blocked_work_packages"), list) else []
    if set(ready) & set(blocked):
        errors.append("WP_QUEUE_READY_BLOCKED_OVERLAP")
    active_id = queue.get("active_work_package_id")
    if active_id != control.get("active_work_package_id"):
        errors.append("WP_CONTROL_QUEUE_ACTIVE_DRIFT")
    if control.get("active_work_package_limit") != 1:
        errors.append("WP_ACTIVE_LIMIT_INVALID")

    for package_id, package in packages.items():
        current = package.get("current_state") if isinstance(package.get("current_state"), dict) else {}
        target = package.get("target_state") if isinstance(package.get("target_state"), dict) else {}
        fields = [package.get("title"), package.get("capability_area"), current.get("verified_description"), target.get("measurable_description")]
        if any(term in field.casefold() for field in fields if isinstance(field, str) for term in FORBIDDEN):
            errors.append(f"WP_FORBIDDEN_OBJECTIVE:{package_id}")
        delivered = set(package.get("must_deliver", [])) if isinstance(package.get("must_deliver"), list) else set()
        missing = sorted(REQUIRED_DELIVERABLES - delivered)
        if missing:
            errors.append(f"WP_REQUIRED_DELIVERABLES_MISSING:{package_id}:{','.join(missing)}")
        if not isinstance(current.get("verified_description"), str) or not current["verified_description"].strip():
            errors.append(f"WP_CURRENT_STATE_MISSING:{package_id}")
        if not isinstance(target.get("measurable_description"), str) or not target["measurable_description"].strip():
            errors.append(f"WP_TARGET_STATE_MISSING:{package_id}")
        scope = package.get("source_scope") if isinstance(package.get("source_scope"), dict) else {}
        versions = scope.get("applicable_elementor_versions", [])
        for version in versions if isinstance(versions, list) else []:
            if isinstance(version, str) and version.casefold() == "latest":
                errors.append(f"WP_PERMANENT_LATEST_FORBIDDEN:{package_id}")
            if isinstance(version, dict) and version.get("verification_status") == "verified" and not version.get("evidence_refs"):
                errors.append(f"WP_VERIFIED_VERSION_EVIDENCE_MISSING:{package_id}")

    for package_id in ready:
        package = packages.get(package_id)
        if package is None:
            errors.append(f"WP_QUEUE_UNKNOWN:{package_id}")
        elif package.get("status") != "ready":
            errors.append(f"WP_READY_STATUS_DRIFT:{package_id}")
    for package_id in blocked:
        package = packages.get(package_id)
        if package is None:
            errors.append(f"WP_BLOCKED_UNKNOWN:{package_id}")
        elif package.get("status") != "blocked":
            errors.append(f"WP_BLOCKED_STATUS_DRIFT:{package_id}")
    if active_id is not None:
        package = packages.get(active_id)
        if package is None:
            errors.append(f"WP_ACTIVE_UNKNOWN:{active_id}")
        elif package.get("status") != "active":
            errors.append(f"WP_ACTIVE_STATUS_DRIFT:{active_id}")
    return sorted(set(errors))
