---
project: elementor-v4-knowledge-base
status_version: 2
last_updated: 2026-06-22T11:07:20+03:00
timezone: Europe/Istanbul
pipeline_status: in_progress
source_policy: official_first
---

# وضعیت پایگاه دانش Elementor V4

این فایل منبع وضعیت اجرایی پژوهش است و باید پس از پایان هر مرحله به‌روزرسانی شود.

## خلاصه وضعیت

| شاخص | مقدار |
|---|---:|
| منابع بررسی‌شده | 6 |
| مراحل تکمیل‌شده و Commit‌شده در ریپو | 1 |
| مراحل تکمیل‌شده در گفتگو و در انتظار انتقال | 5 |
| مراحل زمان‌بندی‌شده باقی‌مانده | 4 |
| مراحل در حال اجرا | 0 |
| مراحل ناموفق | 0 |
| وضعیت کلی | `in_progress` |

## مراحل تکمیل‌شده

| ID | منبع | نوع خروجی | وضعیت ذخیره در ریپو |
|---|---|---|---|
| KB-001 | Widgets index | جزوه Index و Inventory | `pending_import` |
| KB-002 | Editor V4 index | جزوه Index و Inventory | `pending_import` |
| KB-003 | Explore the V4 features | جزوه رسمی V4 | `pending_import` |
| KB-004 | Button element | جزوه Element V4 | `pending_import` |
| KB-005 | Heading element | جزوه Element V4 | `pending_import` |
| KB-006 | Loop Grid widget | جزوه جامع Widget | `committed` — `ddceabd45d3c8c6655cb44bca6016f98426034ae` |

> پنج مرحله اول در گفتگو تکمیل شده‌اند، اما فایل Markdown نهایی آن‌ها هنوز به ریپو منتقل نشده است؛ بنابراین `pending_import` باقی می‌مانند.

## صف زمان‌بندی‌شده امروز

| ID | زمان اجرا | منبع | فایل هدف | وضعیت |
|---|---|---|---|---|
| KB-006 | 2026-06-22 11:00 | Loop Grid | `docs/widgets/loop/loop-grid.md` | `completed_with_gaps` |
| KB-007 | 2026-06-22 12:00 | Query in Loop Grid | `docs/widgets/loop/loop-grid-query.md` | `scheduled` |
| KB-008 | 2026-06-22 13:00 | Create Queries | `docs/concepts/queries/create-queries.md` | `scheduled` |
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
    - docs/_index.md did not exist, so no index update was performed
    - source documentation contains several apparent copy-editing inconsistencies, recorded in the note
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

1. وضعیت مرحله را به یکی از مقادیر زیر تغییر دهد:
   - `completed`
   - `completed_with_gaps`
   - `failed`
   - `blocked`
   - `insufficient_evidence`
2. مسیر فایل خروجی و شناسه Commit واقعی را ثبت کند.
3. زمان پایان را با timezone صریح درج کند.
4. تعداد منابع بررسی‌شده و مراحل زمان‌بندی‌شده را اصلاح کند.
5. خلأهای شواهد را در بخش «موارد باز» اضافه کند.
6. بدون Commit موفق، وضعیت ذخیره‌سازی را `committed` اعلام نکند.

## الگوی ثبت نتیجه مرحله

```yaml
stage_id: KB-000
status: completed_with_gaps
source_url: https://example.com/
output_path: docs/example.md
completed_at: 2026-06-22T00:00:00+03:00
commit_sha: null
evidence_gaps: []
notes: null
```

## موارد باز

- انتقال پنج جزوه تکمیل‌شده اولیه از گفتگو به فایل‌های مستقل Markdown.
- ساخت `docs/_index.md` پس از ایجاد نخستین مجموعه Indexها.
- ساخت `manifests/sources.yaml` و `manifests/coverage.yaml`.
- تعیین نسخه دقیق Elementor برای مقالاتی که نسخه Plugin را اعلام نمی‌کنند.
- حفظ تفکیک `documented`، `observed`، `derived` و `insufficient_evidence` در همه جزوه‌ها.
- تکمیل شواهد KB-006 برای Pro prerequisite، Skin، Dynamic Tags، Responsive controls و Accessibility.
- بررسی مستقل صفحات فرعی Loop Grid بدون نسبت‌دادن محتوای آن‌ها به صفحه اصلی Widget.

## قانون منبع

اولویت منابع:

1. مستندات رسمی `elementor.com`
2. مستندات توسعه‌دهندگان `developers.elementor.com`
3. GitHub رسمی Elementor
4. Fixture واقعی و کنترل‌شده
5. منابع ثالث فقط با برچسب صریح و بدون ارتقای آن‌ها به حقیقت رسمی

آخرین وضعیت ثبت‌شده: `2026-06-22T11:07:20+03:00`
