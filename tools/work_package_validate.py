#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "planning" / "WORK_PACKAGE_CATALOG.json"
QUEUE = ROOT / "planning" / "WORK_PACKAGE_QUEUE.json"
CONTROL = ROOT / "planning" / "CONTROL_STATE.json"

FORBIDDEN_TERMS = {
    "keepalive", "placeholder", "reserve work package", "status update only",
    "status-only", "bookkeeping", "merge finalization only", "checkpoint only"
}
REQUIRED_DELIVER = {"source_inventory", "normalized_knowledge_entries", "version_scope", "provenance_metadata", "limitations_and_uncertainty", "validator_integration", "CI_integration"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate() -> list[str]:
    errors: list[str] = []
    catalog = load(CATALOG)
    queue = load(QUEUE)
    control = load(CONTROL)
    packages = {item["id"]: item for item in catalog["work_packages"]}
    ready = set(queue["ready_work_packages"])
    if len(ready) > catalog["policy"]["max_ready_work_packages"]:
        errors.append("WP_READY_DEPTH_EXCEEDED")
    if queue.get("active_work_package_id") and queue["active_work_package_id"] not in packages:
        errors.append("WP_ACTIVE_UNKNOWN")
    if control.get("active_work_package_id") != queue.get("active_work_package_id"):
        errors.append("WP_CONTROL_QUEUE_ACTIVE_DRIFT")
    if control["execution_policy"]["active_work_package_limit"] != 1:
        errors.append("WP_ACTIVE_LIMIT_INVALID")
    for wp in catalog["work_packages"]:
        fields_to_check = [
            wp.get("title", ""),
            wp.get("capability_area", ""),
            (wp.get("current_state") or {}).get("verified_description", ""),
            (wp.get("target_state") or {}).get("measurable_description", "")
        ]
        if any(any(term in field.lower() for term in FORBIDDEN_TERMS) for field in fields_to_check):
            errors.append(f"{wp['id']}: forbidden artificial or bookkeeping objective")
        missing = REQUIRED_DELIVER - set(wp["must_deliver"])
        if missing:
            errors.append(f"{wp['id']}: missing deliverables {sorted(missing)}")
        if not wp["current_state"]["verified_description"] or not wp["target_state"]["measurable_description"]:
            errors.append(f"{wp['id']}: missing measurable transition")
        for version in wp["source_scope"]["applicable_elementor_versions"]:
            if isinstance(version, dict) and version.get("verification_status") == "verified" and not version.get("evidence_refs"):
                errors.append(f"{wp['id']}: verified version lacks evidence")
            if isinstance(version, str) and version.lower() == "latest":
                errors.append(f"{wp['id']}: permanent latest claim forbidden")
    for wp_id in ready:
        if wp_id not in packages:
            errors.append(f"queue references unknown work package {wp_id}")
    return sorted(set(errors))


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    print("WORK_PACKAGE_CATALOG_VALID" if not problems else "WORK_PACKAGE_CATALOG_INVALID")
    raise SystemExit(1 if problems else 0)
