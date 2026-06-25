#!/usr/bin/env python3
"""Capture official source bytes, local snapshots, and deterministic fingerprints."""
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

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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
MAX_IMAGE_BYTES = 16 * 1024 * 1024
PARSER_VERSION = "html-text-v1"
SNAPSHOT_FORMAT_VERSION = 1
USER_AGENT = "elementor-evidence-kb-source-capture/2.0"
ALLOWED_HOSTS = {"elementor.com", "developers.elementor.com"}
IMAGE_EXTENSIONS = {
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/gif": "gif",
    "image/webp": "webp",
    "image/svg+xml": "svg",
}


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


def _alias_registry() -> list[dict[str, Any]]:
    path = ROOT / "registries" / "source-url-aliases.yaml"
    if not path.exists():
        return []
    value = load_yaml(path)
    errors = validate_instance(
        value, "source-url-aliases.schema.json", str(path.relative_to(ROOT))
    )
    if errors:
        raise ValueError("; ".join(errors))
    aliases = value.get("aliases", [])
    return aliases if isinstance(aliases, list) else []


def canonical_source_url(source_id: str, requested_url: str) -> str:
    matches = [
        item
        for item in _alias_registry()
        if item.get("source_id") == source_id
        and (
            requested_url == item.get("canonical_url")
            or requested_url in item.get("legacy_urls", [])
        )
    ]
    if len(matches) > 1:
        raise ValueError(f"conflicting canonical URL aliases for {source_id}")
    if not matches:
        return requested_url
    canonical = matches[0]["canonical_url"]
    if not official_url(canonical):
        raise ValueError(f"canonical URL is outside the official allowlist: {canonical}")
    return canonical


def _read_image_documents(stage_id: str) -> list[tuple[Path, Any, list[dict[str, Any]]]]:
    result: list[tuple[Path, Any, list[dict[str, Any]]]] = []
    directory = ROOT / "evidence" / "images"
    if not directory.exists():
        return result
    for path in sorted(directory.glob(f"{stage_id}*.yaml")):
        value = load_yaml(path)
        records = value.get("images", []) if isinstance(value, dict) else value
        if isinstance(records, list) and all(isinstance(item, dict) for item in records):
            result.append((path, value, records))
    return result


def image_ids(stage_id: str) -> list[str]:
    return sorted(
        {
            record["image_id"]
            for _path, _value, records in _read_image_documents(stage_id)
            for record in records
            if isinstance(record.get("image_id"), str)
        }
    )


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


def fetch_image(url: str) -> tuple[bytes, str]:
    if not official_url(url):
        raise ValueError(f"image URL is outside the official allowlist: {url}")
    request = urllib.request.Request(
        url,
        method="GET",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "image/png,image/jpeg,image/gif,image/webp,image/svg+xml",
            "Accept-Encoding": "identity",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            final_url = response.geturl()
            if not official_url(final_url):
                raise ValueError(f"image redirect left the official allowlist: {final_url}")
            content_type = response.headers.get_content_type()
            if content_type not in IMAGE_EXTENSIONS:
                raise ValueError(f"unexpected image content type: {content_type}")
            raw = response.read(MAX_IMAGE_BYTES + 1)
            if len(raw) > MAX_IMAGE_BYTES:
                raise ValueError("image exceeds the 16 MiB capture limit")
            if not 200 <= response.status < 300:
                raise ValueError(f"unexpected image HTTP status: {response.status}")
            return raw, content_type
    except urllib.error.HTTPError as exc:
        raise ValueError(f"HTTP {exc.code} for image {url}") from exc
    except urllib.error.URLError as exc:
        raise ValueError(f"network error for image {url}: {exc.reason}") from exc


def content_addressed_paths(
    source_id: str, response_hash: str, normalized_hash: str, content_type: str
) -> tuple[Path, Path]:
    suffix = "xhtml" if content_type == "application/xhtml+xml" else "html"
    root = ROOT / "evidence" / "snapshots" / source_id
    return (
        root / f"response-{response_hash}.{suffix}",
        root / f"normalized-{normalized_hash}.txt",
    )


def write_immutable(path: Path, data: bytes) -> bool:
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"snapshot collision at {path.relative_to(ROOT)}")
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    os.replace(temporary, path)
    return True


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _capture_tracked_images(stage_id: str, source_id: str) -> tuple[str, list[str]]:
    documents = _read_image_documents(stage_id)
    tracked = [
        record
        for _path, _value, records in documents
        for record in records
        if record.get("source_id") == source_id
    ]
    if not tracked:
        return "not_applicable", []
    missing: list[str] = []
    changed_documents: set[Path] = set()
    for path, _value, records in documents:
        for record in records:
            if record.get("source_id") != source_id:
                continue
            url = record.get("url")
            image_id = record.get("image_id")
            if not isinstance(url, str) or not isinstance(image_id, str):
                missing.append(str(url))
                continue
            try:
                raw, content_type = fetch_image(url)
                digest = hashlib.sha256(raw).hexdigest()
                extension = IMAGE_EXTENSIONS[content_type]
                snapshot = (
                    ROOT / "evidence" / "snapshots" / source_id / "images"
                    / f"{image_id}-{digest}.{extension}"
                )
                write_immutable(snapshot, raw)
                record.update(
                    {
                        "retrieval_status": "retrieved",
                        "sha256": digest,
                        "snapshot_format_version": SNAPSHOT_FORMAT_VERSION,
                        "snapshot_path": str(snapshot.relative_to(ROOT)).replace("\\", "/"),
                        "content_type": content_type,
                        "content_length": len(raw),
                    }
                )
                errors = validate_instance(record, "image-evidence.schema.json", image_id)
                if errors:
                    raise ValueError("; ".join(errors))
                changed_documents.add(path)
            except ValueError:
                record["retrieval_status"] = "failed"
                record["sha256"] = None
                for field in (
                    "snapshot_format_version", "snapshot_path", "content_type", "content_length"
                ):
                    record.pop(field, None)
                missing.append(url)
                changed_documents.add(path)
    for path, value, _records in documents:
        if path in changed_documents:
            write_yaml(path, value)
    return ("complete" if not missing else "partial", sorted(set(missing)))


def _valid_existing_record(
    record: Any,
    normalized_hash: str,
    canonical_url: str,
    image_status: str,
    missing_images: list[str],
) -> bool:
    if not isinstance(record, dict) or record.get("schema_version") != 3:
        return False
    if record.get("normalized_document_sha256") != normalized_hash:
        return False
    if record.get("canonical_url") != canonical_url:
        return False
    if record.get("image_capture_status") != image_status:
        return False
    if record.get("missing_image_urls") != missing_images:
        return False
    response_path = ROOT / str(record.get("response_snapshot_path", ""))
    normalized_path = ROOT / str(record.get("normalized_snapshot_path", ""))
    if not response_path.is_file() or not normalized_path.is_file():
        return False
    return (
        file_sha256(response_path) == record.get("response_bytes_sha256")
        and file_sha256(normalized_path) == normalized_hash
    )


def capture(stage_id: str) -> int:
    stages = load_stages()
    work_items = load_work_items()
    stage = find_stage(stages, stage_id)
    work_item = find_work_item(work_items, stage_id)
    pr_number = event_pr_number()
    if pr_number is not None:
        work_item["pr_number"] = pr_number
    captured_at = now_istanbul()
    any_change = False
    try:
        for source in stage["sources"]:
            requested_url = source["url"]
            configured_url = canonical_source_url(source["source_id"], requested_url)
            raw, headers, final_url, status = fetch(configured_url)
            if final_url != configured_url:
                raise ValueError(
                    f"unexpected canonical redirect for {source['source_id']}: "
                    f"{configured_url} -> {final_url}"
                )
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
            normalized_bytes = normalized.encode("utf-8")
            normalized_hash = hashlib.sha256(normalized_bytes).hexdigest()
            response_path, normalized_path = content_addressed_paths(
                source["source_id"], response_hash, normalized_hash, headers.get_content_type()
            )
            image_status, missing_images = _capture_tracked_images(stage_id, source["source_id"])
            record_path = ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml"
            existing = load_yaml(record_path) if record_path.exists() else None
            if _valid_existing_record(
                existing, normalized_hash, final_url, image_status, missing_images
            ):
                continue
            write_immutable(response_path, raw)
            write_immutable(normalized_path, normalized_bytes)
            redirect_chain = list(dict.fromkeys([requested_url, configured_url, final_url]))
            record = {
                "schema_version": 3,
                "source_id": source["source_id"],
                "stage_id": stage_id,
                "source_type": source["source_type"],
                "requested_url": requested_url,
                "canonical_url": final_url,
                "redirect_chain": redirect_chain,
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
                "response_snapshot_path": str(response_path.relative_to(ROOT)).replace("\\", "/"),
                "normalized_snapshot_path": str(normalized_path.relative_to(ROOT)).replace("\\", "/"),
                "snapshot_format_version": SNAPSHOT_FORMAT_VERSION,
                "image_evidence_ids": image_ids(stage_id),
                "discovered_image_urls": sorted(parser.image_urls),
                "image_capture_status": image_status,
                "missing_image_urls": missing_images,
                "notes": [
                    "response_bytes_sha256 hashes the committed content-addressed response snapshot",
                    "normalized_document_sha256 hashes the committed UTF-8 normalized snapshot",
                    "unchanged normalized content and image coverage reuse the existing record",
                ],
            }
            errors = validate_instance(record, "source-record.schema.json", source["source_id"])
            if errors:
                raise ValueError("; ".join(errors))
            write_yaml(record_path, record)
            any_change = True
        if (
            work_item.get("source_capture_status") != "captured"
            or work_item.get("last_error") is not None
        ):
            work_item["source_capture_status"] = "captured"
            work_item["updated_at"] = captured_at
            work_item["last_error"] = None
            write_yaml(ROOT / "manifests" / "work-items.yaml", work_items)
            any_change = True
    except Exception as exc:
        work_item["source_capture_status"] = "failed"
        work_item["updated_at"] = now_istanbul()
        work_item["last_error"] = str(exc)
        write_yaml(ROOT / "manifests" / "work-items.yaml", work_items)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        f"captured source evidence for {stage_id}"
        if any_change
        else f"source evidence unchanged for {stage_id}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True)
    return capture(parser.parse_args().stage)


if __name__ == "__main__":
    raise SystemExit(main())
