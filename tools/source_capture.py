#!/usr/bin/env python3
"""Capture official source bytes and deterministic text fingerprints."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

from tools.pipeline_common import (
    ROOT,
    find_stage,
    find_work_item,
    load_stages,
    load_work_items,
    load_yaml,
    now_istanbul,
    validate_instance,
    write_yaml,
)

MAX_RESPONSE_BYTES = 8 * 1024 * 1024
PARSER_VERSION = "html-text-v1"
USER_AGENT = "elementor-evidence-kb-source-capture/1.0"
ALLOWED_HOSTS = {"elementor.com", "developers.elementor.com"}


class TextParser(HTMLParser):
    SKIP = {"script", "style", "noscript", "template", "svg"}

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.skip_depth = 0
        self.in_title = False
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.image_urls: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in self.SKIP:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "title":
            self.in_title = True
        elif tag == "img":
            values = dict(attrs)
            source = values.get("src") or values.get("data-src")
            if source:
                absolute = urljoin(self.base_url, source.strip())
                if absolute.startswith("https://"):
                    self.image_urls.add(absolute)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self.SKIP and self.skip_depth:
            self.skip_depth -= 1
        elif tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        value = " ".join(data.split())
        if not value:
            return
        if self.in_title:
            self.title_parts.append(value)
        self.text_parts.append(value)

    @property
    def title(self) -> str:
        return " ".join(self.title_parts).strip()

    @property
    def normalized_text(self) -> str:
        return "\n".join(self.text_parts).strip() + "\n"


def official_url(url: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    return parsed.scheme == "https" and (
        host in ALLOWED_HOSTS
        or any(host.endswith("." + allowed) for allowed in ALLOWED_HOSTS)
    )


def event_pr_number(event_path: str | None = None) -> int | None:
    """Return a positive PR number from the trusted GitHub event payload."""
    raw_path = event_path or os.environ.get("GITHUB_EVENT_PATH")
    if not raw_path:
        return None
    path = Path(raw_path)
    if not path.is_file():
        return None
    try:
        event = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    pull_request = event.get("pull_request") if isinstance(event, dict) else None
    number = pull_request.get("number") if isinstance(pull_request, dict) else None
    return number if isinstance(number, int) and not isinstance(number, bool) and number > 0 else None


def image_ids(stage_id: str) -> list[str]:
    found: set[str] = set()
    directory = ROOT / "evidence" / "images"
    if not directory.exists():
        return []
    for path in sorted(directory.glob(f"{stage_id}*.yaml")):
        value = load_yaml(path)
        records = value.get("images", []) if isinstance(value, dict) else value
        if isinstance(records, list):
            found.update(
                record["image_id"]
                for record in records
                if isinstance(record, dict) and isinstance(record.get("image_id"), str)
            )
    return sorted(found)


def fetch(url: str) -> tuple[bytes, Any, str, int]:
    if not official_url(url):
        raise ValueError(f"URL is outside the official allowlist: {url}")
    request = urllib.request.Request(
        url,
        method="GET",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Encoding": "identity",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            final_url = response.geturl()
            if not official_url(final_url):
                raise ValueError(f"redirect left the official allowlist: {final_url}")
            content_type = response.headers.get_content_type()
            if content_type not in {"text/html", "application/xhtml+xml"}:
                raise ValueError(f"unexpected content type: {content_type}")
            raw = response.read(MAX_RESPONSE_BYTES + 1)
            if len(raw) > MAX_RESPONSE_BYTES:
                raise ValueError("source exceeds the 8 MiB capture limit")
            if not 200 <= response.status < 300:
                raise ValueError(f"unexpected HTTP status: {response.status}")
            return raw, response.headers, final_url, response.status
    except urllib.error.HTTPError as exc:
        raise ValueError(f"HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise ValueError(f"network error for {url}: {exc.reason}") from exc


def capture(stage_id: str) -> int:
    stages = load_stages()
    work_items = load_work_items()
    stage = find_stage(stages, stage_id)
    work_item = find_work_item(work_items, stage_id)
    pr_number = event_pr_number()
    if pr_number is not None:
        work_item["pr_number"] = pr_number
    captured_at = now_istanbul()
    try:
        for source in stage["sources"]:
            raw, headers, final_url, status = fetch(source["url"])
            charset = headers.get_content_charset() or "utf-8"
            text = raw.decode(charset, errors="replace")
            first_chunk = text[:20000].lower()
            if (
                len(text) < 1000
                or "just a moment" in first_chunk
                or "cf-chl-" in first_chunk
                or "captcha" in first_chunk
            ):
                raise ValueError("response appears to be empty or a challenge page")
            parser = TextParser(final_url)
            parser.feed(text)
            normalized = parser.normalized_text
            if len(normalized) < 500:
                raise ValueError("normalized document text is unexpectedly short")
            response_hash = hashlib.sha256(raw).hexdigest()
            normalized_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
            record = {
                "schema_version": 2,
                "source_id": source["source_id"],
                "stage_id": stage_id,
                "source_type": source["source_type"],
                "requested_url": source["url"],
                "canonical_url": final_url,
                "redirect_chain": [source["url"]]
                if source["url"] == final_url
                else [source["url"], final_url],
                "retrieved_at": captured_at,
                "http_status": status,
                "content_type": headers.get_content_type(),
                "charset": charset.lower(),
                "content_length": len(raw),
                "etag": headers.get("ETag"),
                "last_modified": headers.get("Last-Modified"),
                "page_title": parser.title or stage["title"],
                "reported_last_updated": source.get("last_updated"),
                "content_sha256": response_hash,
                "response_bytes_sha256": response_hash,
                "normalized_document_sha256": normalized_hash,
                "parser_version": PARSER_VERSION,
                "image_evidence_ids": image_ids(stage_id),
                "discovered_image_urls": sorted(parser.image_urls),
                "notes": [
                    "response_bytes_sha256 hashes exact HTTP response bytes",
                    "normalized_document_sha256 hashes deterministic visible-ish HTML text",
                ],
            }
            errors = validate_instance(
                record, "source-record.schema.json", source["source_id"]
            )
            if errors:
                raise ValueError("; ".join(errors))
            write_yaml(
                ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml",
                record,
            )
        work_item["source_capture_status"] = "captured"
        work_item["updated_at"] = captured_at
        work_item["last_error"] = None
        write_yaml(ROOT / "manifests" / "work-items.yaml", work_items)
    except Exception as exc:
        work_item["source_capture_status"] = "failed"
        work_item["updated_at"] = now_istanbul()
        work_item["last_error"] = str(exc)
        write_yaml(ROOT / "manifests" / "work-items.yaml", work_items)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"captured source evidence for {stage_id}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True)
    return capture(parser.parse_args().stage)


if __name__ == "__main__":
    raise SystemExit(main())
