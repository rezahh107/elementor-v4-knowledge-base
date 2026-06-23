from __future__ import annotations

import pytest

from tools.pipeline_common import infer_stage, transition
from tools.source_capture import TextParser, official_url
from tools.work_item_validate import validate


def test_registered_work_items_are_valid() -> None:
    assert validate() == []


def test_stage_is_inferred_from_migration_branch() -> None:
    assert infer_stage("migration/KB-004-button") == "KB-004"


def test_invalid_state_transition_is_rejected() -> None:
    item = {"state": "not_started", "updated_at": "2026-06-23T00:00:00+03:00", "last_error": None}
    with pytest.raises(ValueError, match="invalid transition"):
        transition(item, "machine_validated")


def test_blocked_item_can_return_to_authoring() -> None:
    item = {"state": "blocked", "updated_at": "2026-06-23T00:00:00+03:00", "last_error": "prior failure"}
    transition(item, "authoring_running")
    assert item["state"] == "authoring_running"
    assert item["last_error"] is None


def test_official_url_allowlist_is_fail_closed() -> None:
    assert official_url("https://elementor.com/help/button-element/")
    assert official_url("https://developers.elementor.com/docs/")
    assert not official_url("http://elementor.com/help/button-element/")
    assert not official_url("https://elementor.com.example.test/help/")


def test_html_normalization_ignores_script_and_collects_https_images() -> None:
    parser = TextParser("https://elementor.com/help/example/")
    parser.feed("<title>Example</title><main>Hello   world<img src='/a.png'></main><script>ignored()</script>")
    assert parser.title == "Example"
    assert "Hello world" in parser.normalized_text
    assert "ignored" not in parser.normalized_text
    assert parser.image_urls == {"https://elementor.com/a.png"}
