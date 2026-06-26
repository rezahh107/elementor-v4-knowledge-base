#!/usr/bin/env python3
"""Capture official source bytes and deterministic text fingerprints."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
from copy import deepcopy
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urljoin, urlparse

from tools.pipeline_common import (
    ROOT,
    dump_yaml,
    find_stage,
    find_work_item,
    load_stages,
    load_work_items,
    load_yaml,
    now_istanbul,
    validate_instance,
)

MAX_RESPONSE_BYTES = 8 * 1024 * 1024
PARSER_VERSION = "html-text-v2"
USER_AGENT = "elementor-evidence-kb-source-capture/2.0"
ALLOWED_HOSTS = {"elementor.com", "developers.elementor.com"}
DEFAULT_ARTIFACT_DIR = ROOT / ".capture-artifacts"


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


class TrackingRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Track every validated redirect instead of inferring only endpoints."""

    def __init__(self, initial_url: str) -> None:
        super().__init__()
        self.chain = [initial_url]

    def redirect_request(
        self,
        req: urllib.request.Request,
        fp: Any,
        code: int,
        msg: str,
        headers: Any,
        newurl: str,
    ) -> urllib.request.Request | None:
        absolute = urljoin(req.full_url, newurl)
        if not official_url(absolute):
            raise ValueError(f"redirect left the official allowlist: {absolute}")
        if absolute in self.chain:
            raise ValueError(f"redirect cycle detected at {absolute}")
        self.chain.append(absolute)
        return super().redirect_request(req, fp, code, msg, headers, absolute)


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


def fetch(url: str) -> tuple[bytes, Any, str, int, list[str]]:
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
    redirect_handler = TrackingRedirectHandler(url)
    opener = urllib.request.build_opener(redirect_handler)
    try:
        with opener.open(request, timeout=30) as response:
            final_url = response.geturl()
            if not official_url(final_url):
                raise ValueError(f"redirect left the official allowlist: {final_url}")
            if redirect_handler.chain[-1] != final_url:
                redirect_handler.chain.append(final_url)
            content_type = response.headers.get_content_type()
            if content_type not in {"text/html", "application/xhtml+xml"}:
                raise ValueError(f"unexpected content type: {content_type}")
            raw = response.read(MAX_RESPONSE_BYTES + 1)
            if len(raw) > MAX_RESPONSE_BYTES:
                raise ValueError("source exceeds the 8 MiB capture limit")
            if not 200 <= response.status < 300:
                raise ValueError(f"unexpected HTTP status: {response.status}")
            return raw, response.headers, final_url, response.status, redirect_handler.chain
    except urllib.error.HTTPError as exc:
        raise ValueError(f"HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise ValueError(f"network error for {url}: {exc.reason}") from exc


def _http_last_updated(headers: Any) -> tuple[str | None, str]:
    raw = headers.get("Last-Modified")
    if not raw:
        return None, "unavailable"
    try:
        value = parsedate_to_datetime(raw).date().isoformat()
    except (TypeError, ValueError, OverflowError):
        return None, "unavailable"
    return value, "http_last_modified"


def _capture_id(source_id: str, response_hash: str, canonical_url: str) -> str:
    payload = f"{source_id}\0{response_hash}\0{canonical_url}".encode("utf-8")
    return "CAP-" + hashlib.sha256(payload).hexdigest()


def build_record(
    *,
    stage: dict[str, Any],
    source: dict[str, Any],
    raw: bytes,
    headers: Any,
    final_url: str,
    status: int,
    redirect_chain: list[str],
    captured_at: str,
    artifact_dir: Path,
) -> tuple[dict[str, Any], Path, bytes]:
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
    run_id = os.environ.get("GITHUB_RUN_ID")
    storage = "workflow_artifact" if run_id else "local_ephemeral"
    artifact_name = f"source-snapshot-{stage['stage_id']}-{run_id or 'local'}"
    relative_snapshot = Path("source-snapshots") / source["source_id"] / f"{response_hash}.bin"
    snapshot_path = artifact_dir / relative_snapshot
    reported_last_updated, updated_source = _http_last_updated(headers)
    page_title = parser.title or stage["title"]
    record = {
        "schema_version": 3,
        "source_id": source["source_id"],
        "stage_id": stage["stage_id"],
        "source_type": source["source_type"],
        "requested_url": source["url"],
        "canonical_url": final_url,
        "redirect_chain": redirect_chain,
        "redirect_chain_complete": True,
        "retrieved_at": captured_at,
        "http_status": status,
        "content_type": headers.get_content_type(),
        "charset": charset.lower(),
        "content_length": len(raw),
        "etag": headers.get("ETag"),
        "last_modified": headers.get("Last-Modified"),
        "page_title": page_title,
        "page_title_source": "html_title" if parser.title else "stage_fallback",
        "reported_last_updated": reported_last_updated,
        "reported_last_updated_source": updated_source,
        "reported_last_updated_hint": source.get("last_updated"),
        "content_sha256": response_hash,
        "response_bytes_sha256": response_hash,
        "normalized_document_sha256": normalized_hash,
        "parser_version": PARSER_VERSION,
        "source_locator_version": 1,
        "capture_id": _capture_id(source["source_id"], response_hash, final_url),
        "snapshot": {
            "storage": storage,
            "artifact_name": artifact_name,
            "relative_path": relative_snapshot.as_posix(),
            "run_id": run_id,
            "response_bytes_sha256": response_hash,
        },
        "image_evidence_ids": image_ids(stage["stage_id"]),
        "discovered_image_urls": sorted(parser.image_urls),
        "notes": [
            "response_bytes_sha256 hashes exact HTTP response bytes",
            "normalized_document_sha256 hashes deterministic visible-ish HTML text",
            "reported_last_updated_hint is unverified manifest input and is not an observed date",
        ],
    }
    errors = validate_instance(record, "source-record-v3.schema.json", source["source_id"])
    if errors:
        raise ValueError("; ".join(errors))
    return record, snapshot_path, raw


def _same_capture(existing: Any, candidate: dict[str, Any]) -> bool:
    if not isinstance(existing, dict) or existing.get("schema_version") != 3:
        return False
    stable_keys = {
        "source_id",
        "stage_id",
        "source_type",
        "requested_url",
        "canonical_url",
        "redirect_chain",
        "redirect_chain_complete",
        "http_status",
        "content_type",
        "charset",
        "content_length",
        "etag",
        "last_modified",
        "page_title",
        "page_title_source",
        "reported_last_updated",
        "reported_last_updated_source",
        "reported_last_updated_hint",
        "content_sha256",
        "response_bytes_sha256",
        "normalized_document_sha256",
        "parser_version",
        "source_locator_version",
        "capture_id",
        "image_evidence_ids",
        "discovered_image_urls",
        "notes",
    }
    return all(existing.get(key) == candidate.get(key) for key in stable_keys)


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def commit_payloads_atomically(payloads: dict[Path, bytes]) -> None:
    """Publish a prepared capture set and roll back every destination on failure."""
    originals = {path: path.read_bytes() if path.exists() else None for path in payloads}
    published: list[Path] = []
    try:
        for path in sorted(payloads, key=lambda item: item.as_posix()):
            _atomic_write_bytes(path, payloads[path])
            published.append(path)
    except Exception:
        for path in reversed(published):
            original = originals[path]
            if original is None:
                try:
                    path.unlink()
                except FileNotFoundError:
                    pass
            else:
                _atomic_write_bytes(path, original)
        raise


def capture(
    stage_id: str,
    *,
    artifact_dir: Path = DEFAULT_ARTIFACT_DIR,
    fetcher: Callable[[str], tuple[bytes, Any, str, int, list[str]]] = fetch,
) -> int:
    stages = load_stages()
    work_items = load_work_items()
    stage = find_stage(stages, stage_id)
    work_item = find_work_item(work_items, stage_id)
    pr_number = event_pr_number()
    if pr_number is not None:
        work_item["pr_number"] = pr_number
    target_head = os.environ.get("TARGET_HEAD_SHA")
    if target_head:
        work_item["expected_head_sha"] = target_head
    captured_at = now_istanbul()

    try:
        payloads: dict[Path, bytes] = {}
        for source in stage["sources"]:
            raw, headers, final_url, status, redirects = fetcher(source["url"])
            record, snapshot_path, snapshot_bytes = build_record(
                stage=stage,
                source=source,
                raw=raw,
                headers=headers,
                final_url=final_url,
                status=status,
                redirect_chain=redirects,
                captured_at=captured_at,
                artifact_dir=artifact_dir,
            )
            record_path = ROOT / "evidence" / "sources" / f"{source['source_id']}.yaml"
            if record_path.exists():
                existing = load_yaml(record_path)
                if _same_capture(existing, record):
                    record = existing
            payloads[record_path] = dump_yaml(record).encode("utf-8")
            payloads[snapshot_path] = snapshot_bytes

        work_item["source_capture_status"] = "captured"
        work_item["updated_at"] = captured_at
        work_item["github_state_observed_at"] = captured_at if target_head else work_item.get("github_state_observed_at")
        work_item["last_error"] = None
        payloads[ROOT / "manifests" / "work-items.yaml"] = dump_yaml(work_items).encode("utf-8")
        commit_payloads_atomically(payloads)
    except Exception as exc:
        failed = deepcopy(work_items)
        failed_item = find_work_item(failed, stage_id)
        failed_item["source_capture_status"] = "failed"
        failed_item["updated_at"] = now_istanbul()
        failed_item["last_error"] = str(exc)
        commit_payloads_atomically(
            {ROOT / "manifests" / "work-items.yaml": dump_yaml(failed).encode("utf-8")}
        )
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"captured source evidence for {stage_id}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True)
    parser.add_argument("--artifact-dir", type=Path, default=DEFAULT_ARTIFACT_DIR)
    args = parser.parse_args()
    return capture(args.stage, artifact_dir=args.artifact_dir)


if __name__ == "__main__":
    raise SystemExit(main())
