from __future__ import annotations

import json
from pathlib import Path

from tools.work_package_controller import plan
from tools.work_package_validate import validate

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_is_valid():
    assert validate() == []


def test_open_pr_blocks_new_work():
    result = plan({"pull_requests": [{"state": "open"}]})
    assert result["action"] == "reconcile_existing_mutation_pr"


def test_ready_queue_selects_capability_package():
    result = plan({"pull_requests": []})
    assert result["action"] == "start_ready_work_package"
    assert result["work_package"] == "KB-WP-001"


def test_fixed_ordinal_policy_is_not_used():
    queue = json.loads((ROOT / "planning/WORK_PACKAGE_QUEUE.json").read_text())
    assert queue["policy"]["fixed_ordinal_refresh"] is False
