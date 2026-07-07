from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.github_state_snapshot import build_request, normalize_pull_requests
from tools.work_package_controller import plan
from tools.work_package_validate import validate

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_is_valid():
    assert validate() == []


def test_open_pr_blocks_new_work():
    result = plan({"pull_requests": [{"state": "open"}]})
    assert result["action"] == "reconcile_existing_mutation_pr"


def test_null_pull_request_collection_is_safe():
    result = plan({"pull_requests": None})
    assert result["action"] == "start_ready_work_package"


def test_ready_queue_selects_capability_package():
    result = plan({"pull_requests": []})
    assert result["action"] == "start_ready_work_package"
    assert result["work_package"] == "KB-WP-001"


def test_fixed_ordinal_policy_is_not_used():
    queue = json.loads((ROOT / "planning/WORK_PACKAGE_QUEUE.json").read_text())
    assert queue["policy"]["fixed_ordinal_refresh"] is False


def test_snapshot_request_omits_empty_authorization_header():
    request = build_request("owner/repository", "")
    assert request.get_header("Authorization") is None


def test_snapshot_request_includes_nonempty_authorization_header():
    request = build_request("owner/repository", "token")
    assert request.get_header("Authorization") == "Bearer token"


def test_snapshot_normalization_handles_null_head():
    result = normalize_pull_requests(
        [{"number": 1, "state": "open", "draft": False, "head": None}]
    )
    assert result[0]["head_sha"] is None
    assert result[0]["head_ref"] is None


def test_snapshot_normalization_rejects_non_list_payload():
    with pytest.raises(ValueError, match="Unexpected API response format"):
        normalize_pull_requests({"message": "Not Found"})


def test_catalog_status_drift_blocks_planning(tmp_path: Path):
    planning = tmp_path / "planning"
    planning.mkdir()
    catalog = json.loads(
        (ROOT / "planning/WORK_PACKAGE_CATALOG.json").read_text(encoding="utf-8")
    )
    queue = json.loads(
        (ROOT / "planning/WORK_PACKAGE_QUEUE.json").read_text(encoding="utf-8")
    )
    control = json.loads(
        (ROOT / "planning/CONTROL_STATE.json").read_text(encoding="utf-8")
    )
    catalog["work_packages"][0]["status"] = "blocked"
    (planning / "WORK_PACKAGE_CATALOG.json").write_text(json.dumps(catalog))
    (planning / "WORK_PACKAGE_QUEUE.json").write_text(json.dumps(queue))
    (planning / "CONTROL_STATE.json").write_text(json.dumps(control))

    result = plan({"pull_requests": []}, root=tmp_path)

    assert result["action"] == "blocked"
    assert result["reason"] == "ready_queue_catalog_status_drift"
    assert result["drifted_work_packages"] == ["KB-WP-001"]
