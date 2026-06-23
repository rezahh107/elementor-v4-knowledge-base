<!-- GENERATED FILE. Edit manifests/stages.yaml and run tools/kb.py generate. -->
---
project: elementor-v4-knowledge-base
status_version: 1
manifest_sha256: 8cf22477506faafae5d8422b47a5207ce029ccd2b6c9a18a27e48c23a158e903
timezone: Europe/Istanbul
pipeline_status: hardening
source_policy: official_first
queue_manager_status: paused_for_hardening
---

# وضعیت پایگاه دانش Elementor V4

این فایل از `manifests/stages.yaml` تولید شده و منبع حقیقت مستقل نیست.

## خلاصه

- مراحل تعریف‌شده: 37
- اسناد Commit‌شده: 18
- اسناد authoritative: 0
- مراحل منتظر صف: 19
- مراحل زمان‌بندی‌شده: 0
- مراحل failed/blocked: 0
- Evidence gapهای باز: 54
- آخرین زمان تکمیل ثبت‌شده: `2026-06-23T14:00:00+03:00`

## وضعیت مراحل

| Stage | عنوان | وضعیت | Review | Provenance | خروجی |
|---|---|---|---|---|---|
| KB-001 | Widgets index | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/indexes/widgets-index.md` |
| KB-002 | Editor V4 index | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/indexes/editor-v4-index.md` |
| KB-003 | Explore the V4 features | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/overview/explore-v4-features.md` |
| KB-004 | Button element | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/elements/v4/button.md` |
| KB-005 | Heading element | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/elements/v4/heading.md` |
| KB-006 | Loop Grid widget | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/loop-grid.md` |
| KB-007 | Build a query with the Loop Grid | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/loop-grid-query.md` |
| KB-008 | Create queries | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/concepts/queries/create-queries.md` |
| KB-009 | Paginate your loop | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/pagination.md` |
| KB-010 | Taxonomy Filter widget | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/taxonomy-filter.md` |
| KB-011 | Loop Carousel | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/loop-carousel.md` |
| KB-012 | Add an alternate template in a loop grid | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/alternate-template.md` |
| KB-013 | Customize the layout of a Loop Grid | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/customize-layout.md` |
| KB-014 | Add an Off Canvas widget to a Loop Grid | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/loop/off-canvas.md` |
| KB-015 | Search Widget and Search Results Archive | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/widgets/search/search-widget-and-results-archive.md` |
| KB-016 | Div Block element | `not_scheduled` | `not_started` | `not_started` | — |
| KB-017 | Flexbox element | `not_scheduled` | `not_started` | `not_started` | — |
| KB-018 | Image element | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/elements/v4/image.md` |
| KB-019 | Paragraph element | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/elements/v4/paragraph.md` |
| KB-020 | SVG element | `completed_with_gaps` | `unreviewed` | `document_level_legacy` | `docs/elements/v4/svg.md` |
| KB-021 | Tabs Element | `not_scheduled` | `not_started` | `not_started` | — |
| KB-022 | YouTube element | `not_scheduled` | `not_started` | `not_started` | — |
| KB-023 | Classes in Elementor | `not_scheduled` | `not_started` | `not_started` | — |
| KB-024 | The Elementor Editor Class Manager | `not_scheduled` | `not_started` | `not_started` | — |
| KB-025 | Variables | `not_scheduled` | `not_started` | `not_started` | — |
| KB-026 | Variables Manager | `not_scheduled` | `not_started` | `not_started` | — |
| KB-027 | Import and export design systems | `not_scheduled` | `not_started` | `not_started` | — |
| KB-028 | Style tab – Layout | `not_scheduled` | `not_started` | `not_started` | — |
| KB-029 | Style tab – Spacing | `not_scheduled` | `not_started` | `not_started` | — |
| KB-030 | Style tab – Size | `not_scheduled` | `not_started` | `not_started` | — |
| KB-031 | Style tab – Position | `not_scheduled` | `not_started` | `not_started` | — |
| KB-032 | Style tab – Typography | `not_scheduled` | `not_started` | `not_started` | — |
| KB-033 | Style tab – Background | `not_scheduled` | `not_started` | `not_started` | — |
| KB-034 | Style tab – Border | `not_scheduled` | `not_started` | `not_started` | — |
| KB-035 | Style tab – Effects | `not_scheduled` | `not_started` | `not_started` | — |
| KB-036 | Responsive editing | `not_scheduled` | `not_started` | `not_started` | — |
| KB-037 | Dynamic tags in V4 | `not_scheduled` | `not_started` | `not_started` | — |

## Gate ازسرگیری صف

صف فقط وقتی مجاز به ازسرگیری است که `python tools/kb.py validate --strict` و `python tools/kb.py generate --check` بدون خطا اجرا شوند و تغییر از طریق PR بررسی شود.
