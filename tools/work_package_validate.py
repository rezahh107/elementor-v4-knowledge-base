#!/usr/bin/env python3
"""Validate Work Package schemas, semantics, and invalid-case fixtures."""
from __future__ import annotations
import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.work_package_contracts import load_documents, load_json, validate_documents

CASES = Path("tests/fixtures/work_packages/negative_cases.json")

def validate(root: Path = ROOT) -> list[str]:
    try:
        return validate_documents(load_documents(root), root)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"WP_CONTROL_FILES_INVALID:{exc}"]

def _replace(document: Any, pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("case path must be a JSON Pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.split("/")[1:]]
    parent = document
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    leaf = parts[-1]
    if isinstance(parent, list):
        parent[int(leaf)] = value
    else:
        parent[leaf] = value

def apply_case(documents: dict[str, Any], operations: list[dict[str, Any]]) -> dict[str, Any]:
    result = copy.deepcopy(documents)
    for operation in operations:
        if operation.get("op") != "replace":
            raise ValueError(f"unsupported case operation: {operation.get('op')!r}")
        name = operation.get("document")
        if name not in result:
            raise ValueError(f"unknown case document: {name!r}")
        _replace(result[name], operation.get("path", ""), operation.get("value"))
    return result

def validate_invalid_cases(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    documents = load_documents(root)
    case_set = load_json(root / CASES)
    cases = case_set.get("cases") if isinstance(case_set, dict) else None
    if not isinstance(cases, list):
        return ["WP_NEGATIVE_FIXTURE_SET_INVALID"]
    seen: set[str] = set()
    for case in cases:
        case_id = case.get("id") if isinstance(case, dict) else None
        if not isinstance(case_id, str) or not case_id:
            errors.append("WP_NEGATIVE_FIXTURE_ID_INVALID")
            continue
        if case_id in seen:
            errors.append(f"WP_NEGATIVE_FIXTURE_DUPLICATE:{case_id}")
            continue
        seen.add(case_id)
        try:
            diagnostics = validate_documents(
                apply_case(documents, case.get("operations", [])), root
            )
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            errors.append(f"WP_NEGATIVE_FIXTURE_OPERATION_INVALID:{case_id}:{exc}")
            continue
        for expected in case.get("expected_error_codes", []):
            if not any(item == expected or item.startswith(f"{expected}:") for item in diagnostics):
                errors.append(f"WP_NEGATIVE_FIXTURE_NOT_REJECTED:{case_id}:{expected}")
    return sorted(set(errors))

def validate_negative_fixtures(root: Path = ROOT) -> list[str]:
    return validate_invalid_cases(root)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", default="all", choices=("all", "documents", "negative-fixtures"))
    mode = parser.parse_args().mode
    errors: list[str] = []
    if mode in {"all", "documents"}:
        errors += validate()
    if mode in {"all", "negative-fixtures"}:
        try:
            errors += validate_invalid_cases()
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"WP_NEGATIVE_FIXTURE_LOAD_FAILED:{exc}")
    errors = sorted(set(errors))
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print("WORK_PACKAGE_CONTROL_PLANE_VALID" if not errors else "WORK_PACKAGE_CONTROL_PLANE_INVALID")
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
