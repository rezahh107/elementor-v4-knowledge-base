---
project: elementor-v4-knowledge-base
status_version: 15
last_updated: 2026-06-22T22:28:43+03:00
timezone: Europe/Istanbul
pipeline_status: in_progress
source_policy: official_first
llm_entrypoint: LLM_GUIDE.md
---

# وضعیت پایگاه دانش Elementor V4

این فایل منبع وضعیت اجرایی پژوهش است. مدل زبانی ابتدا `LLM_GUIDE.md` را بخواند.

## خلاصه وضعیت

| شاخص | مقدار |
|---|---:|
| منابع بررسی‌شده | 10 |
| اسناد تکمیل‌شده و Commit‌شده | 5 |
| اسناد تکمیل‌شده و در انتظار انتقال | 5 |
| مراحل زمان‌بندی‌شده باقی‌مانده | 8 |
| مراحل در حال اجرا | 0 |
| مراحل ناموفق | 0 |
| وضعیت کلی | `in_progress` |

## ترتیب مطالعه مدل

```text
LLM_GUIDE.md
→ STATUS.md
→ manifests/coverage.yaml
→ manifests/sources.yaml
→ docs/_index.md
→ سند موضوعی
→ registries/evidence-states.yaml
```

## وضعیت مراحل

| ID | عنوان | فایل/وضعیت |
|---|---|---|
| KB-001 | Widgets index | `pending_import` |
| KB-002 | Editor V4 index | `pending_import` |
| KB-003 | Explore the V4 features | `pending_import` |
| KB-004 | Button element | `pending_import` |
| KB-005 | Heading element | `pending_import` |
| KB-006 | Loop Grid widget | `docs/widgets/loop/loop-grid.md` — `completed_with_gaps` |
| KB-007 | Build a query with the Loop Grid | `docs/widgets/loop/loop-grid-query.md` — `completed_with_gaps` |
| KB-008 | Elementor query configuration | `docs/concepts/queries/create-queries.md` — `completed_with_gaps` |
| KB-009 | Paginate your loop | `docs/widgets/loop/pagination.md` — `completed_with_gaps` |
| KB-010 | Taxonomy Filter widget | `docs/widgets/loop/taxonomy-filter.md` — `completed_with_gaps` |
| KB-011 | Loop Carousel | `scheduled` — 2026-06-22 15:00 |
| KB-012 | Add an alternate template in a loop grid | `scheduled` — 2026-06-22 16:00 |
| KB-013 | Customize the layout of a Loop Grid | `scheduled` — 2026-06-22 17:00 |
| KB-014 | Add an Off Canvas widget to a Loop Grid | `scheduled` — 2026-06-22 18:00 |
| KB-015 | Search Widget and Search Results Archive | `scheduled` — 2026-06-22 20:00 |
| KB-016 | Div Block element | `scheduled` — 2026-06-22 21:00 |
| KB-017 | Flexbox element | `scheduled` — 2026-06-22 22:00 |
| KB-018 | Image element | `scheduled` — 2026-06-22 23:00 |

همه زمان‌ها بر اساس `Europe/Istanbul` هستند.

## ثبت اجرای مراحل Commit‌شده

```yaml
- stage_id: KB-006
  status: completed_with_gaps
  source_url: https://elementor.com/help/loop-grid/
  source_last_updated: 2026-06-19
  output_path: docs/widgets/loop/loop-grid.md
  completed_at: 2026-06-22T11:07:20+03:00
  commit_sha: ddceabd45d3c8c6655cb44bca6016f98426034ae
  evidence_gaps:
    - exact versions and Pro prerequisite are not stated
    - responsive, Dynamic Tags, URL, AJAX and accessibility details are incomplete
    - four embedded screenshots were not visually retrievable

- stage_id: KB-007
  status: completed_with_gaps
  source_url: https://elementor.com/help/create-a-query-in-a-loop-grid/
  canonical_url: https://elementor.com/help/building-query-loop-grid/
  source_last_updated: 2026-06-19
  output_path: docs/widgets/loop/loop-grid-query.md
  completed_at: 2026-06-22T12:05:51+03:00
  commit_sha: ab98a1097ce26a2c2c665cab5d78ca504c1fd97e
  evidence_gaps:
    - exact versions, Pro prerequisite and redirect history are not stated
    - several query controls and runtime behaviors are absent or partial
    - two official screenshots were not visually retrievable

- stage_id: KB-008
  status: completed_with_gaps
  source_url: https://elementor.com/help/create-queries/
  source_last_updated: 2025-06-30
  output_path: docs/concepts/queries/create-queries.md
  completed_at: 2026-06-22T13:19:02+03:00
  commit_sha: 5cfd17535a33ef6cbc6dcb91eaa49803b6d1e3f9
  evidence_gaps:
    - exact versions and Pro prerequisite are not stated
    - query logic, Query ID lifecycle, AJAX, URL and accessibility are incomplete
    - embedded screenshots were not visually retrievable

- stage_id: KB-009
  status: completed_with_gaps
  source_url: https://elementor.com/help/pagination-for-loop/
  canonical_url: https://elementor.com/help/paginate-loop/
  source_last_updated: 2025-02-09
  output_path: docs/widgets/loop/pagination.md
  completed_at: 2026-06-22T14:07:00+03:00
  commit_sha: 66ffe7d5cccf2b18b56919381878d6874b8b744c
  evidence_gaps:
    - exact Elementor Core and Pro versions are not stated
    - Elementor Pro prerequisite is not explicitly stated
    - the requested URL differs from the current official index URL and redirect history is not documented
    - the full conditional control matrix for every pagination style is not provided
    - Page Limit applicability and validation rules are incomplete
    - Shorten edge cases, ellipsis behavior and RTL behavior are not documented
    - Previous and Next endpoint behavior and disabled states are not documented
    - Button ID semantics and reuse mechanism are unclear
    - AJAX hooks, loading states, error handling, focus management and history behavior are not documented
    - URL parameters, deep linking, browser history and SEO behavior are not documented
    - accessibility semantics and keyboard or screen-reader behavior are not documented
    - responsive controls and breakpoint behavior are not documented
    - the Style tab inventory and visual states are not documented
    - most editor screenshots could not be fetched visually by the research tool
  notes:
    - documented styles are None, Numbers, Previous/Next, Numbers + Previous/Next, Load on click and Infinite Scroll
    - three output-example images were visually inspected
    - docs/_index.md, manifests/sources.yaml and manifests/coverage.yaml were updated

- stage_id: KB-010
  status: completed_with_gaps
  source_url: https://elementor.com/help/taxonomy-filter/
  canonical_url: https://elementor.com/help/taxonomy-filter-widget/
  source_last_updated: 2026-06-04
  output_path: docs/widgets/loop/taxonomy-filter.md
  completed_at: 2026-06-22T15:08:11+03:00
  commit_sha: 95657df95445c453d310107715ddc3008baf68bb
  evidence_gaps:
    - exact Elementor Core and Pro versions and the required plan are not stated
    - the requested URL differs from the current official index URL and redirect history is not documented
    - no separate control named Filter Type is documented; the page only documents choosing Categories or Tags through Taxonomy
    - custom taxonomies and product taxonomies are not documented
    - the Excluding categories and tags heading has no retrievable instructions beneath it
    - boolean logic between multiple separate Taxonomy Filter widgets is not specified
    - Current Query is explicitly unsupported and interaction with other query controls is incomplete
    - hierarchy behavior is only documented as showing or hiding Taxonomy Children
    - ordering and validation for Number of taxonomies are not documented
    - AJAX, loading, error handling, hooks and interaction with pagination are not documented
    - URL parameters, deep links, browser history and SEO behavior are not documented
    - accessibility semantics, keyboard behavior, focus management and ARIA are not documented
    - responsive behavior is only partially observable through device icons for Direction and Item Alignment
    - style defaults, units and the complete conditional control matrix are not documented
    - two official Settings and Style screenshots could not be fetched visually
    - the exact Elementor version represented by the 2023 image assets is not stated
  notes:
    - documented controls include Selected Loop Grid, Taxonomy, Direction, Item Alignment, Multiple Selection with AND or OR, Empty Items, Taxonomy Children, First Item, First item title, Number of taxonomies and Horizontal Scroll
    - documented style states are Normal, Hover and Active
    - four official screenshots were visually inspected and two image URLs were extracted but not fetched
    - docs/_index.md, manifests/sources.yaml and manifests/coverage.yaml were updated
```

## مراحل زمان‌بندی‌شده

```yaml
- stage_id: KB-011
  title: Loop Carousel
  status: scheduled
  source_url: https://elementor.com/help/loop-carousel/
  output_path: docs/widgets/loop/loop-carousel.md
  scheduled_for: 2026-06-22T15:00:00+03:00

- stage_id: KB-012
  title: Add an alternate template in a loop grid
  status: scheduled
  source_url: https://elementor.com/help/how-do-i-add-an-alternate-template-in-a-loop-grid/
  output_path: docs/widgets/loop/alternate-template.md
  scheduled_for: 2026-06-22T16:00:00+03:00

- stage_id: KB-013
  title: Customize the layout of a Loop Grid
  status: scheduled
  source_url: https://elementor.com/help/customize-layout-loop/
  output_path: docs/widgets/loop/customize-layout.md
  scheduled_for: 2026-06-22T17:00:00+03:00

- stage_id: KB-014
  title: Add an Off Canvas widget to a Loop Grid
  status: scheduled
  source_url: https://elementor.com/help/add-an-off-canvas-widget-to-a-loop-grid/
  output_path: docs/widgets/loop/off-canvas.md
  scheduled_for: 2026-06-22T18:00:00+03:00

- stage_id: KB-015
  title: Search Widget and Search Results Archive
  status: scheduled
  source_urls:
    - https://elementor.com/help/search-widget/
    - https://elementor.com/help/customize-the-search-results-archive/
  output_path: docs/widgets/search/search-widget-and-results-archive.md
  scheduled_for: 2026-06-22T20:00:00+03:00

- stage_id: KB-016
  title: Div Block element
  status: scheduled
  source_url: https://elementor.com/help/div-block-element/
  output_path: docs/elements/v4/div-block.md
  scheduled_for: 2026-06-22T21:00:00+03:00

- stage_id: KB-017
  title: Flexbox element
  status: scheduled
  source_url: https://elementor.com/help/flexbox-element/
  output_path: docs/elements/v4/flexbox.md
  scheduled_for: 2026-06-22T22:00:00+03:00

- stage_id: KB-018
  title: Image element
  status: scheduled
  source_url: https://elementor.com/help/image-element/
  output_path: docs/elements/v4/image.md
  scheduled_for: 2026-06-22T23:00:00+03:00
```

## صف بعدی پیشنهادی

| اولویت | موضوع | وضعیت |
|---:|---|---|
| 1 | Loop Carousel | `scheduled` — 2026-06-22 15:00 |
| 2 | Alternate Template in Loop Grid | `scheduled` — 2026-06-22 16:00 |
| 3 | Customize Layout in Loop Grid | `scheduled` — 2026-06-22 17:00 |
| 4 | Off-Canvas in Loop Grid | `scheduled` — 2026-06-22 18:00 |
| 5 | Search Widget and Search Results Archive | `scheduled` — 2026-06-22 20:00 |
| 6 | Div Block element | `scheduled` — 2026-06-22 21:00 |
| 7 | Flexbox element | `scheduled` — 2026-06-22 22:00 |
| 8 | Image element | `scheduled` — 2026-06-22 23:00 |
| 9 | Paragraph element | `not_scheduled` |
| 10 | SVG element | `not_scheduled` |

## قرارداد به‌روزرسانی

پس از هر مرحله:

1. وضعیت واقعی مرحله ثبت شود.
2. `output_path`، زمان پایان و SHA واقعی Commit درج شود.
3. شمارنده‌ها و Manifestها اصلاح شوند.
4. خلأهای شواهد ثبت شوند.
5. بدون Commit موفق، `storage_status: committed` اعلام نشود.

## موارد باز

- انتقال KB-001 تا KB-005 به فایل‌های مستقل Markdown.
- اعتبارسنجی Front Matter با Schema.
- افزودن GitHub Actions برای Schema، لینک‌ها، IDهای تکراری و هماهنگی Index/Manifest.
- اصلاح timezone ثبت‌شده در KB-006.
- پیاده‌سازی Claim-level provenance ID.
- تکمیل Gapهای KB-006 تا KB-010.
- ساخت Manifestهای evidence gaps و redirects.

## قانون منبع

1. مستندات رسمی `elementor.com`
2. مستندات رسمی توسعه‌دهندگان Elementor
3. GitHub رسمی Elementor
4. Fixture واقعی و کنترل‌شده
5. منابع ثالث فقط با برچسب صریح

آخرین وضعیت ثبت‌شده: `2026-06-22T22:28:43+03:00`
