---
project: elementor-v4-knowledge-base
status_version: 5
last_updated: 2026-06-22T13:36:00+03:00
timezone: Europe/Istanbul
pipeline_status: in_progress
source_policy: official_first
llm_entrypoint: LLM_GUIDE.md
---

# وضعیت پایگاه دانش Elementor V4

این فایل منبع وضعیت اجرایی پژوهش است. برای استفاده مدل زبانی، ابتدا `LLM_GUIDE.md` خوانده شود.

## خلاصه وضعیت

| شاخص | مقدار |
|---|---:|
| منابع بررسی‌شده | 8 |
| مراحل تکمیل‌شده و Commit‌شده در ریپو | 3 |
| مراحل تکمیل‌شده در گفتگو و در انتظار انتقال | 5 |
| مراحل زمان‌بندی‌شده باقی‌مانده | 2 |
| مراحل در حال اجرا | 0 |
| مراحل ناموفق | 0 |
| لایه مصرف توسط مدل زبانی | `initialized` |
| مدیر خودکار صف | `enabled` |
| وضعیت کلی | `in_progress` |

## زیرساخت مصرف توسط مدل زبانی

| فایل | نقش | Commit |
|---|---|---|
| `LLM_GUIDE.md` | نقطه شروع، سیاست حقیقت و ترتیب مطالعه | `7895c2ad385b44073a919ecc66524cb705db1141` |
| `docs/_index.md` | فهرست انسانی و مسیرهای محتوایی | `234c0ab41179068b2fccc2bc6a388b2b01cd0ffe` |
| `manifests/sources.yaml` | رجیستری ماشین‌خوان منابع و فایل‌ها | `b42913346faec8bac6656597830bc231da2e6a76` |
| `manifests/coverage.yaml` | نقشه پوشش و شکاف‌ها | `2e8bf3d2877e4842bd04864efb79b134e3cf0ed3` |
| `registries/evidence-states.yaml` | واژگان کنترل‌شده وضعیت شواهد | `2e0cf8107c7d0de4f2f238a943ad10c5b067d0ca` |
| `schemas/knowledge-note.schema.json` | قرارداد Front Matter جزوه‌ها | `8cb5143da039d3c106a61707740e9fc3594898a4` |

### ترتیب مطالعه مدل

```text
LLM_GUIDE.md
→ STATUS.md
→ manifests/coverage.yaml
→ manifests/sources.yaml
→ docs/_index.md
→ سند موضوعی
→ registries/evidence-states.yaml
```

## مدیر خودکار صف

یک Automation ساعتی از `2026-06-22 14:30 Europe/Istanbul` فعال است.

قواعد آن:

1. خود مدیر صف را جزو تسک‌های پژوهشی حساب نمی‌کند.
2. اگر سه یا بیشتر تسک پژوهشی فعال باشند، کاری انجام نمی‌دهد.
3. اگر تعداد تسک‌های پژوهشی فعال کمتر از سه باشد، فقط یک مرحله `not_scheduled` را بر اساس اولویت صف انتخاب می‌کند.
4. مرحله جدید را برای نزدیک‌ترین ساعت کامل آینده زمان‌بندی می‌کند.
5. پس از ساخت واقعی تسک، `STATUS.md` را به `scheduled` به‌روزرسانی می‌کند.
6. بدون نتیجه واقعی ابزار، ادعای ساخت تسک یا Commit نمی‌کند.

## مراحل تکمیل‌شده

| ID | منبع | نوع خروجی | وضعیت ذخیره در ریپو |
|---|---|---|---|
| KB-001 | Widgets index | جزوه Index و Inventory | `pending_import` |
| KB-002 | Editor V4 index | جزوه Index و Inventory | `pending_import` |
| KB-003 | Explore the V4 features | جزوه رسمی V4 | `pending_import` |
| KB-004 | Button element | جزوه Element V4 | `pending_import` |
| KB-005 | Heading element | جزوه Element V4 | `pending_import` |
| KB-006 | Loop Grid widget | جزوه جامع Widget | `committed` — `ddceabd45d3c8c6655cb44bca6016f98426034ae` |
| KB-007 | Build a query with the Loop Grid | جزوه Workflow و کنترل‌های Query | `committed` — `ab98a1097ce26a2c2c665cab5d78ca504c1fd97e` |
| KB-008 | Elementor query configuration | جزوه جامع Query و Taxonomy | `committed` — `5cfd17535a33ef6cbc6dcb91eaa49803b6d1e3f9` |

> پنج مرحله اول در گفتگو تکمیل شده‌اند، اما فایل Markdown نهایی آن‌ها هنوز به ریپو منتقل نشده است؛ بنابراین `pending_import` باقی می‌مانند.

## صف زمان‌بندی‌شده امروز

| ID | زمان اجرا | منبع | فایل هدف | وضعیت |
|---|---|---|---|---|
| KB-006 | 2026-06-22 11:00 | Loop Grid | `docs/widgets/loop/loop-grid.md` | `completed_with_gaps` |
| KB-007 | 2026-06-22 12:00 | Query in Loop Grid | `docs/widgets/loop/loop-grid-query.md` | `completed_with_gaps` |
| KB-008 | 2026-06-22 13:00 | Elementor query configuration | `docs/concepts/queries/create-queries.md` | `completed_with_gaps` |
| KB-009 | 2026-06-22 14:00 | Pagination for Loop | `docs/widgets/loop/pagination.md` | `scheduled` |
| KB-010 | 2026-06-22 15:00 | Taxonomy Filter | `docs/widgets/loop/taxonomy-filter.md` | `scheduled` |

همه زمان‌ها بر اساس `Europe/Istanbul` هستند.

## ثبت اجرای مراحل

```yaml
- stage_id: KB-006
  status: completed_with_gaps
  source_url: https://elementor.com/help/loop-grid/
  source_last_updated: 2026-06-19
  output_path: docs/widgets/loop/loop-grid.md
  completed_at: 2026-06-22T11:07:20+03:00
  commit_sha: ddceabd45d3c8c6655cb44bca6016f98426034ae
  evidence_gaps:
    - exact Elementor Core and Pro versions are not stated
    - Elementor Pro prerequisite is not explicitly stated on the source page
    - Skin options are absent from the source page
    - responsive controls are only partially observable
    - Dynamic Tags and dynamic field behavior are not documented
    - complete Query ID, URL, AJAX and accessibility behavior is not documented
    - four embedded screenshots could not be fetched visually by the research tool, though their official URLs were extracted
  notes:
    - source documentation contains several apparent copy-editing inconsistencies, recorded in the note

- stage_id: KB-007
  status: completed_with_gaps
  source_url: https://elementor.com/help/create-a-query-in-a-loop-grid/
  canonical_url: https://elementor.com/help/building-query-loop-grid/
  source_last_updated: 2026-06-19
  output_path: docs/widgets/loop/loop-grid-query.md
  completed_at: 2026-06-22T12:05:51+03:00
  commit_sha: ab98a1097ce26a2c2c665cab5d78ca504c1fd97e
  evidence_gaps:
    - the requested URL differs from the current canonical article URL and redirect history is not documented
    - the article is a simple walkthrough rather than a complete query-control reference
    - Source options beyond Posts are not shown because the dropdown is never opened
    - Exclude is visible but not explained
    - Date, Order By, Order, Ignore Sticky Posts and Query ID are visible but only partially documented
    - Offset, Avoid Duplicates, Current Query and Related are absent from the article text and inspected screenshots
    - general AND/OR logic, Query ID API, AJAX, URL, accessibility and pagination interaction are not documented
    - exact Elementor Core/Pro versions and Pro prerequisite are not stated
    - two official screenshots could not be fetched visually, though their URLs and captions were extracted
  notes:
    - screenshot paths use 2022/01 while the article was updated in 2026; the page does not state the UI version represented
    - values All, Date, DESC and Yes are recorded as screenshot state, not official defaults

- stage_id: KB-008
  status: completed_with_gaps
  source_url: https://elementor.com/help/create-queries/
  source_last_updated: 2025-06-30
  output_path: docs/concepts/queries/create-queries.md
  completed_at: 2026-06-22T13:19:02+03:00
  commit_sha: 5cfd17535a33ef6cbc6dcb91eaa49803b6d1e3f9
  evidence_gaps:
    - exact Elementor Core and Pro versions are not stated
    - Elementor Pro prerequisite is not explicitly stated
    - the complete inventory of query-capable widgets and elements is not provided
    - embedded image URLs were extracted but visual fetches failed with cache misses
    - general AND/OR logic and precedence between Include and Exclude are not documented
    - Query ID hooks, syntax and runtime lifecycle are delegated to a separate developer page
    - AJAX, URL, pagination and accessibility behavior are not documented
    - the source does not identify the provider or version requirement for the Brand taxonomy
    - multiple copy-editing inconsistencies leave some Product and Taxonomy labels ambiguous
  notes:
    - the article covers Posts, Products, Post Taxonomy and Product Taxonomy contexts
    - content from linked subpages was not attributed to the main article
```

## صف بعدی پیشنهادی

| اولویت | موضوع | وضعیت |
|---:|---|---|
| 1 | Loop Carousel | `not_scheduled` |
| 2 | Alternate Template in Loop Grid | `not_scheduled` |
| 3 | Customize Layout in Loop Grid | `not_scheduled` |
| 4 | Off-Canvas in Loop Grid | `not_scheduled` |
| 5 | Search Widget and Search Results Archive | `not_scheduled` |
| 6 | Div Block element | `not_scheduled` |
| 7 | Flexbox element | `not_scheduled` |
| 8 | Image element | `not_scheduled` |
| 9 | Paragraph element | `not_scheduled` |
| 10 | SVG element | `not_scheduled` |

## قرارداد به‌روزرسانی وضعیت

پس از پایان هر مرحله، مجری باید:

1. وضعیت مرحله را به `completed`، `completed_with_gaps`، `failed`، `blocked` یا `insufficient_evidence` تغییر دهد.
2. مسیر فایل خروجی و شناسه Commit واقعی را ثبت کند.
3. زمان پایان را با timezone صریح درج کند.
4. شمارنده‌های خلاصه و Manifestهای مرتبط را اصلاح کند.
5. خلأهای شواهد را ثبت کند.
6. `docs/_index.md`، `manifests/sources.yaml` و `manifests/coverage.yaml` را در صورت تغییر پوشش به‌روزرسانی کند.
7. بدون Commit موفق، وضعیت ذخیره‌سازی را `committed` اعلام نکند.

## موارد باز

- انتقال KB-001 تا KB-005 از گفتگو به فایل‌های مستقل Markdown.
- اعتبارسنجی تمام Front Matterها با `schemas/knowledge-note.schema.json`.
- افزودن GitHub Actions برای Schema، لینک‌ها، ID تکراری و هماهنگی Index/Manifest.
- اصلاح timezone ثبت‌شده در KB-006 از `+03:30` به `Europe/Istanbul/+03:00`.
- پیاده‌سازی Claim-level provenance ID.
- تکمیل شواهد KB-006 تا KB-008 طبق Gapهای ثبت‌شده.
- ساخت `manifests/evidence-gaps.yaml` و `manifests/redirects.yaml`.

## قانون منبع

1. مستندات رسمی `elementor.com`
2. مستندات توسعه‌دهندگان `developers.elementor.com`
3. GitHub رسمی Elementor
4. Fixture واقعی و کنترل‌شده
5. منابع ثالث فقط با برچسب صریح و بدون ارتقای آن‌ها به حقیقت رسمی

آخرین وضعیت ثبت‌شده: `2026-06-22T13:36:00+03:00`
