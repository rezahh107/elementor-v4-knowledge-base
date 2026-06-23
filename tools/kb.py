#!/usr/bin/env python3
"""Deterministic validation and generation for the Elementor evidence knowledge base."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
STAGES_PATH = ROOT / "manifests" / "stages.yaml"
GAPS_PATH = ROOT / "manifests" / "evidence-gaps.yaml"
LEDGER_PATH = ROOT / "ledger" / "executions.jsonl"
SCHEMAS_DIR = ROOT / "schemas"

COMPLETED = {"completed", "completed_with_gaps"}
ALLOWED_OFFICIAL_HOSTS = {
    "elementor.com",
    "developers.elementor.com",
    "github.com",
    "raw.githubusercontent.com",
}
SHA1_RE = re.compile(r"^[a-f0-9]{40}$")


class StringSafeLoader(yaml.SafeLoader):
    """Safe loader that preserves ISO dates/timestamps as strings."""


for first_char, resolvers in list(StringSafeLoader.yaml_implicit_resolvers.items()):
    StringSafeLoader.yaml_implicit_resolvers[first_char] = [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]


class ValidationResult:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def note(self, message: str) -> None:
        self.info.append(message)

    def extend(self, other: "ValidationResult") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)
        self.info.extend(other.info)


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


def canonical_json_bytes(value: Any) -> bytes:
    """Return version-1 canonical JSON bytes and reject non-finite numbers."""

    def reject_non_finite(item: Any) -> None:
        if isinstance(item, float) and not math.isfinite(item):
            raise ValueError("NaN and infinities are forbidden in canonical content")
        if isinstance(item, dict):
            for key in sorted(item):
                reject_non_finite(item[key])
        elif isinstance(item, (list, tuple)):
            for child in item:
                reject_non_finite(child)

    reject_non_finite(value)
    text = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return text.encode("utf-8")


def canonical_sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def load_json_schema(name: str) -> dict[str, Any]:
    with (SCHEMAS_DIR / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_schema(
    instance: Any,
    schema_name: str,
    label: str,
    result: ValidationResult,
) -> None:
    schema = load_json_schema(schema_name)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path)):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        result.error(f"{label}:{location}: {error.message}")


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening front-matter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing front-matter delimiter")
    raw = text[4:end]
    data = yaml.load(raw, Loader=StringSafeLoader)
    if not isinstance(data, dict):
        raise ValueError("front matter must be a mapping")
    return data, text[end + 5 :]


def stage_number(stage_id: str) -> int:
    return int(stage_id.split("-", 1)[1])


def sorted_stages(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    return sorted(manifest["stages"], key=lambda item: stage_number(item["stage_id"]))


def load_ledger(result: ValidationResult) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    if not LEDGER_PATH.exists():
        result.error(f"missing ledger: {LEDGER_PATH.relative_to(ROOT)}")
        return events
    schema = load_json_schema("execution-event.schema.json")
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    with LEDGER_PATH.open("r", encoding="utf-8", newline="") as handle:
        for line_number, raw in enumerate(handle, start=1):
            if not raw.strip():
                continue
            try:
                event = json.loads(raw)
            except json.JSONDecodeError as exc:
                result.error(f"ledger line {line_number}: invalid JSON: {exc}")
                continue
            for error in validator.iter_errors(event):
                location = "/".join(str(part) for part in error.absolute_path) or "<root>"
                result.error(f"ledger line {line_number}:{location}: {error.message}")
            events.append(event)
    canonical_lines = [
        json.dumps(event, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
        for event in events
    ]
    current = LEDGER_PATH.read_text(encoding="utf-8").splitlines()
    if current != canonical_lines:
        result.error("ledger/executions.jsonl is not canonical JSONL or has unstable key order")
    event_ids = [event.get("event_id") for event in events]
    duplicates = sorted(key for key, count in Counter(event_ids).items() if count > 1)
    if duplicates:
        result.error(f"duplicate ledger event IDs: {duplicates}")
    return events


def git_commit_exists(sha: str) -> bool | None:
    if not (ROOT / ".git").exists():
        return None
    try:
        completed = subprocess.run(
            ["git", "-C", str(ROOT), "cat-file", "-e", f"{sha}^{{commit}}"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        return None
    return completed.returncode == 0


def authoritative(stage: dict[str, Any], open_gaps: set[str]) -> bool:
    if stage["status"] not in COMPLETED:
        return False
    if stage["review_status"] not in {"peer_reviewed", "verified_by_fixture"}:
        return False
    if stage["provenance_status"] != "claim_level":
        return False
    if any(gap_id in open_gaps for gap_id in stage["gap_ids"]):
        return False
    return all(source["snapshot_status"] == "captured" for source in stage["sources"])


def validate_repository(check_generated: bool = True) -> ValidationResult:
    result = ValidationResult()
    if not STAGES_PATH.exists():
        result.error("missing manifests/stages.yaml")
        return result
    manifest = load_yaml(STAGES_PATH)
    gaps_manifest = load_yaml(GAPS_PATH)
    validate_schema(manifest, "stages.schema.json", "manifests/stages.yaml", result)
    validate_schema(gaps_manifest, "evidence-gaps.schema.json", "manifests/evidence-gaps.yaml", result)

    stages = sorted_stages(manifest)
    gap_records = gaps_manifest.get("gaps", []) if isinstance(gaps_manifest, dict) else []
    gaps = {record.get("gap_id"): record for record in gap_records}
    open_gaps = {
        record["gap_id"]
        for record in gap_records
        if record.get("status") == "open"
    }

    for field in ("stage_id", "knowledge_id", "output_path"):
        values = [stage[field] for stage in stages]
        duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
        if duplicates:
            result.error(f"duplicate {field} values: {duplicates}")

    source_ids = [
        source["source_id"]
        for stage in stages
        for source in stage["sources"]
    ]
    duplicate_sources = sorted(value for value, count in Counter(source_ids).items() if count > 1)
    if duplicate_sources:
        result.error(f"duplicate source IDs: {duplicate_sources}")

    priorities = [
        stage["queue_priority"]
        for stage in stages
        if stage["status"] == "not_scheduled"
    ]
    if priorities and sorted(priorities) != list(range(1, len(priorities) + 1)):
        result.error("not_scheduled queue priorities must be contiguous starting at 1")

    for stage in stages:
        sid = stage["stage_id"]
        for source in stage["sources"]:
            host = (urlparse(source["url"]).hostname or "").lower()
            if source["source_type"].startswith("official") and host not in ALLOWED_OFFICIAL_HOSTS:
                result.error(f"{sid}: official source uses an unapproved host: {host}")
        for gap_id in stage["gap_ids"]:
            if gap_id not in gaps:
                result.error(f"{sid}: references missing evidence gap {gap_id}")
            elif gaps[gap_id].get("stage_id") != sid:
                result.error(f"{sid}: evidence gap {gap_id} belongs to another stage")

        document = ROOT / stage["output_path"]
        if stage["status"] in COMPLETED:
            if not document.exists():
                result.error(f"{sid}: completed stage is missing {stage['output_path']}")
                continue
            try:
                front_matter, _body = parse_front_matter(document)
            except (OSError, ValueError, yaml.YAMLError) as exc:
                result.error(f"{stage['output_path']}: {exc}")
                continue
            validate_schema(
                front_matter,
                "document-frontmatter.schema.json",
                stage["output_path"],
                result,
            )
            if front_matter.get("stage_id") != sid:
                result.error(f"{sid}: front matter stage_id mismatch")
            if front_matter.get("id") != stage["knowledge_id"]:
                result.error(f"{sid}: knowledge_id/front-matter id mismatch")
            if front_matter.get("storage_status") != "committed":
                result.error(f"{sid}: completed document must have storage_status committed")
            if front_matter.get("evidence_status") != stage["evidence_status"]:
                result.error(f"{sid}: evidence_status mismatch between document and canonical manifest")
            sha = stage["content_commit_sha"]
            if not isinstance(sha, str) or not SHA1_RE.fullmatch(sha):
                result.error(f"{sid}: invalid content commit SHA")
            else:
                exists = git_commit_exists(sha)
                if exists is False:
                    result.error(f"{sid}: content commit does not exist in fetched Git history: {sha}")
                elif exists is None:
                    result.warning(f"{sid}: Git executable unavailable; commit existence was not checked")
        elif document.exists():
            result.error(f"{sid}: non-completed stage unexpectedly has an output document")

        if stage["provenance_status"] == "document_level_legacy":
            required = f"GAP-{sid}-PROVENANCE"
            if required not in open_gaps:
                result.error(f"{sid}: legacy document-level provenance lacks open migration gap")
        if stage["review_status"] == "unreviewed":
            required = f"GAP-{sid}-REVIEW"
            if required not in open_gaps:
                result.error(f"{sid}: unreviewed document lacks an open review gap")
        if any(source["snapshot_status"] == "missing_legacy_snapshot" for source in stage["sources"]):
            required = f"GAP-{sid}-SNAPSHOT"
            if required not in open_gaps:
                result.error(f"{sid}: missing legacy snapshot lacks an open gap")

    for gap_id, gap in gaps.items():
        if not any(stage["stage_id"] == gap.get("stage_id") for stage in stages):
            result.error(f"orphan evidence gap {gap_id}")

    events = load_ledger(result)
    latest: dict[str, dict[str, Any]] = {}
    for event in sorted(events, key=lambda item: (item["recorded_at"], item["event_id"])):
        latest[event["stage_id"]] = event
    for stage in stages:
        if stage["status"] in COMPLETED:
            event = latest.get(stage["stage_id"])
            if event is None:
                result.error(f"{stage['stage_id']}: completed stage has no ledger event")
                continue
            if event["status"] != stage["status"]:
                result.error(f"{stage['stage_id']}: ledger status differs from canonical stage status")
            if event["content_commit_sha"] != stage["content_commit_sha"]:
                result.error(f"{stage['stage_id']}: ledger content SHA differs from canonical stage")
            if event["output_path"] != stage["output_path"]:
                result.error(f"{stage['stage_id']}: ledger output path differs from canonical stage")

    if check_generated:
        expected = render_generated(manifest, gaps_manifest)
        for relative_path, content in expected.items():
            path = ROOT / relative_path
            if not path.exists():
                result.error(f"missing generated artifact: {relative_path}")
            elif path.read_text(encoding="utf-8") != content:
                result.error(f"stale generated artifact: {relative_path}; run `python tools/kb.py generate`")

    result.note(f"validated {len(stages)} stages")
    result.note(f"registered {len(gap_records)} evidence gaps")
    result.note(f"authoritative documents: {sum(authoritative(stage, open_gaps) for stage in stages)}")
    return result


def render_status(
    manifest: dict[str, Any],
    gaps_manifest: dict[str, Any],
    manifest_sha: str,
) -> str:
    stages = sorted_stages(manifest)
    counts = Counter(stage["status"] for stage in stages)
    open_gaps = {
        gap["gap_id"]
        for gap in gaps_manifest["gaps"]
        if gap["status"] == "open"
    }
    latest = max(
        (stage["completed_at"] for stage in stages if stage["completed_at"]),
        default="not_available",
    )
    lines = [
        "<!-- GENERATED FILE. Edit manifests/stages.yaml and run tools/kb.py generate. -->",
        "---",
        "project: elementor-v4-knowledge-base",
        "status_version: 1",
        f"manifest_sha256: {manifest_sha}",
        "timezone: Europe/Istanbul",
        "pipeline_status: hardening",
        "source_policy: official_first",
        "queue_manager_status: paused_for_hardening",
        "---",
        "",
        "# وضعیت پایگاه دانش Elementor V4",
        "",
        "این فایل از `manifests/stages.yaml` تولید شده و منبع حقیقت مستقل نیست.",
        "",
        "## خلاصه",
        "",
        f"- مراحل تعریف‌شده: {len(stages)}",
        f"- اسناد Commit‌شده: {sum(stage['status'] in COMPLETED for stage in stages)}",
        f"- اسناد authoritative: {sum(authoritative(stage, open_gaps) for stage in stages)}",
        f"- مراحل منتظر صف: {counts['not_scheduled']}",
        f"- مراحل زمان‌بندی‌شده: {counts['scheduled']}",
        f"- مراحل failed/blocked: {counts['failed'] + counts['blocked']}",
        f"- Evidence gapهای باز: {len(open_gaps)}",
        f"- آخرین زمان تکمیل ثبت‌شده: `{latest}`",
        "",
        "## وضعیت مراحل",
        "",
        "| Stage | عنوان | وضعیت | Review | Provenance | خروجی |",
        "|---|---|---|---|---|---|",
    ]
    for stage in stages:
        output = f"`{stage['output_path']}`" if stage["status"] in COMPLETED else "—"
        lines.append(
            f"| {stage['stage_id']} | {stage['title']} | `{stage['status']}` | "
            f"`{stage['review_status']}` | `{stage['provenance_status']}` | {output} |"
        )
    lines += [
        "",
        "## Gate ازسرگیری صف",
        "",
        "صف فقط وقتی مجاز به ازسرگیری است که `python tools/kb.py validate --strict` و "
        "`python tools/kb.py generate --check` بدون خطا اجرا شوند و تغییر از طریق PR بررسی شود.",
        "",
    ]
    return "\n".join(lines)


def render_index(manifest: dict[str, Any], manifest_sha: str) -> str:
    stages = sorted_stages(manifest)
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for stage in stages:
        groups[stage["category"]].append(stage)
    labels = {
        "index": "Indexها",
        "overview": "نمای کلی",
        "element_v4": "Elementهای Editor V4",
        "loop": "Loop",
        "query": "Query",
        "search": "Search",
        "design_system": "Design System",
        "style_system": "Style System",
    }
    lines = [
        "<!-- GENERATED FILE. Edit manifests/stages.yaml and run tools/kb.py generate. -->",
        "# فهرست پایگاه دانش Elementor",
        "",
        f"`manifest_sha256: {manifest_sha}`",
        "",
        "اسناد `unreviewed` یا دارای `document_level_legacy` پژوهش‌نامه‌اند و نباید authoritative تلقی شوند.",
        "",
    ]
    for category in labels:
        records = groups.get(category, [])
        if not records:
            continue
        lines += [f"## {labels[category]}", ""]
        for stage in records:
            if stage["status"] in COMPLETED:
                relative = stage["output_path"].removeprefix("docs/")
                lines.append(
                    f"- [{stage['title']}]({relative}) — `{stage['stage_id']}` — "
                    f"`{stage['status']}` — `{stage['review_status']}`"
                )
            else:
                lines.append(
                    f"- {stage['title']} — `{stage['stage_id']}` — `{stage['status']}` — "
                    f"اولویت `{stage['queue_priority']}`"
                )
        lines.append("")
    return "\n".join(lines)


def render_coverage(manifest: dict[str, Any], gaps_manifest: dict[str, Any], manifest_sha: str) -> str:
    stages = sorted_stages(manifest)
    counts = Counter(stage["status"] for stage in stages)
    open_gaps = {
        gap["gap_id"]
        for gap in gaps_manifest["gaps"]
        if gap["status"] == "open"
    }
    categories: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for stage in stages:
        categories[stage["category"]][stage["status"]].append(stage["stage_id"])
    document = {
        "manifest_version": 4,
        "generated_from_sha256": manifest_sha,
        "summary": {
            "total_stages": len(stages),
            "committed_documents": sum(stage["status"] in COMPLETED for stage in stages),
            "authoritative_documents": sum(authoritative(stage, open_gaps) for stage in stages),
            "not_scheduled_stages": counts["not_scheduled"],
            "scheduled_stages": counts["scheduled"],
            "failed_or_blocked_stages": counts["failed"] + counts["blocked"],
            "open_evidence_gaps": len(open_gaps),
        },
        "coverage": {
            category: {
                status: sorted(ids, key=stage_number)
                for status, ids in sorted(statuses.items())
            }
            for category, statuses in sorted(categories.items())
        },
    }
    return "# GENERATED FILE. Edit manifests/stages.yaml.\n" + dump_yaml(document)


def render_sources(manifest: dict[str, Any], manifest_sha: str) -> str:
    records = []
    for stage in sorted_stages(manifest):
        for source in stage["sources"]:
            records.append(
                {
                    "source_id": source["source_id"],
                    "stage_id": stage["stage_id"],
                    "knowledge_id": stage["knowledge_id"],
                    "title": stage["title"],
                    "url": source["url"],
                    "source_type": source["source_type"],
                    "last_updated": source["last_updated"],
                    "snapshot_status": source["snapshot_status"],
                    "content_fingerprint": source["content_fingerprint"],
                    "output_path": stage["output_path"],
                    "stage_status": stage["status"],
                    "content_commit_sha": stage["content_commit_sha"],
                }
            )
    document = {
        "manifest_version": 4,
        "generated_from_sha256": manifest_sha,
        "sources": records,
    }
    return "# GENERATED FILE. Edit manifests/stages.yaml.\n" + dump_yaml(document)


def render_generated(
    manifest: dict[str, Any] | None = None,
    gaps_manifest: dict[str, Any] | None = None,
) -> dict[str, str]:
    if manifest is None:
        manifest = load_yaml(STAGES_PATH)
    if gaps_manifest is None:
        gaps_manifest = load_yaml(GAPS_PATH)
    manifest_sha = canonical_sha256(manifest)
    return {
        "STATUS.md": render_status(manifest, gaps_manifest, manifest_sha),
        "docs/_index.md": render_index(manifest, manifest_sha),
        "manifests/coverage.yaml": render_coverage(manifest, gaps_manifest, manifest_sha),
        "manifests/sources.yaml": render_sources(manifest, manifest_sha),
    }


def generate(check: bool) -> int:
    expected = render_generated()
    stale = []
    for relative_path, content in expected.items():
        path = ROOT / relative_path
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(relative_path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        for item in stale:
            print(f"STALE: {item}", file=sys.stderr)
        return 1
    if not check:
        for item in expected:
            print(f"generated {item}")
    return 0


def check_links(strict_http: bool = False) -> int:
    manifest = load_yaml(STAGES_PATH)
    errors: list[str] = []
    warnings: list[str] = []
    for stage in sorted_stages(manifest):
        for source in stage["sources"]:
            request = urllib.request.Request(
                source["url"],
                method="HEAD",
                headers={"User-Agent": "elementor-kb-source-health/1.0"},
            )
            try:
                with urllib.request.urlopen(request, timeout=20) as response:
                    status = response.status
            except urllib.error.HTTPError as exc:
                status = exc.code
            except (urllib.error.URLError, TimeoutError) as exc:
                warnings.append(f"{source['source_id']}: network check unavailable: {exc}")
                continue
            if status in {404, 410}:
                errors.append(f"{source['source_id']}: source returned HTTP {status}")
            elif status >= 400:
                message = f"{source['source_id']}: source returned HTTP {status}"
                (errors if strict_http else warnings).append(message)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


def print_result(result: ValidationResult, strict: bool) -> int:
    for message in result.info:
        print(f"INFO: {message}")
    for message in result.warnings:
        print(f"WARNING: {message}")
    for message in result.errors:
        print(f"ERROR: {message}", file=sys.stderr)
    if result.errors or (strict and result.warnings):
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate_parser = subparsers.add_parser("validate", help="validate schemas and repository consistency")
    validate_parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    generate_parser = subparsers.add_parser("generate", help="generate derived control-plane artifacts")
    generate_parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    link_parser = subparsers.add_parser("check-links", help="check source URL health")
    link_parser.add_argument("--strict-http", action="store_true", help="treat all HTTP 4xx/5xx as errors")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    if args.command == "validate":
        return print_result(validate_repository(check_generated=True), strict=args.strict)
    if args.command == "generate":
        return generate(check=args.check)
    if args.command == "check-links":
        return check_links(strict_http=args.strict_http)
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
