---
project: elementor-v4-knowledge-base
status_version: 19
last_updated: 2026-06-23T00:26:04+03:00
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
| منابع بررسی‌شده | 12 |
| اسناد تکمیل‌شده و Commit‌شده | 7 |
| اسناد تکمیل‌شده و در انتظار انتقال | 5 |
| مراحل زمان‌بندی‌شده باقی‌مانده | 8 |
| مراحل در حال اجرا | 0 |
| مراحل ناموفق | 0 |
| وضعیت کلی | `in_progress` |

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
| KB-018 | Image element | `docs/elements/v4/image.md` — `completed_with_gaps` |
| KB-019 | Paragraph element | `docs/elements/v4/paragraph.md` — `completed_with_gaps` |
| KB-020 | SVG element | `scheduled` — 2026-06-23 01:00 |

همه زمان‌ها بر اساس `Europe/Istanbul` هستند.

## ثبت اجرای مراحل Commit‌شده

```yaml
- stage_id: KB-006
  status: completed_with_gaps
  source_url: https://elementor.com/help/loop-grid/
  output_path: docs/widgets/loop/loop-grid.md
  completed_at: 2026-06-22T11:07:20+03:00
  commit_sha: ddceabd45d3c8c6655cb44bca6016f98426034ae
  evidence_gaps: [version, Pro prerequisite, responsive, dynamic data, URL, AJAX, accessibility, screenshots]
- stage_id: KB-007
  status: completed_with_gaps
  source_url: https://elementor.com/help/create-a-query-in-a-loop-grid/
  output_path: docs/widgets/loop/loop-grid-query.md
  completed_at: 2026-06-22T12:05:51+03:00
  commit_sha: ab98a1097ce26a2c2c665cab5d78ca504c1fd97e
  evidence_gaps: [version, Pro prerequisite, redirect history, query controls, runtime behavior, screenshots]
- stage_id: KB-008
  status: completed_with_gaps
  source_url: https://elementor.com/help/create-queries/
  output_path: docs/concepts/queries/create-queries.md
  completed_at: 2026-06-22T13:19:02+03:00
  commit_sha: 5cfd17535a33ef6cbc6dcb91eaa49803b6d1e3f9
  evidence_gaps: [version, Pro prerequisite, query logic, Query ID lifecycle, AJAX, URL, accessibility, screenshots]
- stage_id: KB-009
  status: completed_with_gaps
  source_url: https://elementor.com/help/pagination-for-loop/
  output_path: docs/widgets/loop/pagination.md
  completed_at: 2026-06-22T14:07:00+03:00
  commit_sha: 66ffe7d5cccf2b18b56919381878d6874b8b744c
  evidence_gaps: [version, Pro prerequisite, control matrix, URL, AJAX, accessibility, responsive, style states, screenshots]
- stage_id: KB-010
  status: completed_with_gaps
  source_url: https://elementor.com/help/taxonomy-filter/
  output_path: docs/widgets/loop/taxonomy-filter.md
  completed_at: 2026-06-22T15:08:11+03:00
  commit_sha: 95657df95445c453d310107715ddc3008baf68bb
  evidence_gaps: [version, Pro prerequisite, taxonomy scope, query interaction, URL, AJAX, accessibility, responsive, style defaults, screenshots]
- stage_id: KB-018
  status: completed_with_gaps
  source_url: https://elementor.com/help/image-element/
  output_path: docs/elements/v4/image.md
  completed_at: 2026-06-22T23:08:43+03:00
  commit_sha: 50923b62a319c99849f5fcf1663341c935d5fc2c
  evidence_gaps: [exact_elementor_version, plan_or_pro_prerequisite, aspect_ratio, object_fit, lazy_loading, responsive_controls, dynamic_data, classes_and_variables, element_states, accessibility, seo, runtime_behavior]
  notes: "وضعیت مرحله با فایل Commit‌شده و manifest منابع تطبیق داده شد."
  counters: {official_pages_reviewed: 1, official_images_indexed: 11}
- stage_id: KB-019
  status: completed_with_gaps
  source_url: https://elementor.com/help/paragraph-element/
  output_path: docs/elements/v4/paragraph.md
  completed_at: 2026-06-23T00:06:13+03:00
  commit_sha: 44a8ebeef9dbb3dbbf0496c52e77fae0b8f2ef73
  evidence_gaps: [exact_elementor_version, plan_or_pro_prerequisite, inline_editing, html_tag_and_semantics, partial_text_links, custom_attributes, color_controls, detailed_style_controls, responsive_controls, dynamic_data, classes_and_variables, element_states, frontend_accessibility, keyboard_and_focus_runtime, seo_behavior, generated_markup, runtime_behavior]
  notes: "صفحه رسمی خط‌به‌خط بررسی شد؛ 13 تصویر رسمی Index شد و فقط 2 تصویر مستقیماً قابل مشاهده بود. صفحات Style فرعی بدون بررسی مستقل به منبع مادر نسبت داده نشدند."
  counters: {official_pages_reviewed: 1, official_images_indexed: 13, official_images_directly_viewed: 2, style_categories_named: 8}
```

## مراحل زمان‌بندی‌شده

```yaml
- {stage_id: KB-011, title: Loop Carousel, source_url: "https://elementor.com/help/loop-carousel/", output_path: "docs/widgets/loop/loop-carousel.md", scheduled_for: "2026-06-22T15:00:00+03:00"}
- {stage_id: KB-012, title: Add an alternate template in a loop grid, source_url: "https://elementor.com/help/how-do-i-add-an-alternate-template-in-a-loop-grid/", output_path: "docs/widgets/loop/alternate-template.md", scheduled_for: "2026-06-22T16:00:00+03:00"}
- {stage_id: KB-013, title: Customize the layout of a Loop Grid, source_url: "https://elementor.com/help/customize-layout-loop/", output_path: "docs/widgets/loop/customize-layout.md", scheduled_for: "2026-06-22T17:00:00+03:00"}
- {stage_id: KB-014, title: Add an Off Canvas widget to a Loop Grid, source_url: "https://elementor.com/help/add-an-off-canvas-widget-to-a-loop-grid/", output_path: "docs/widgets/loop/off-canvas.md", scheduled_for: "2026-06-22T18:00:00+03:00"}
- {stage_id: KB-015, title: Search Widget and Search Results Archive, source_urls: ["https://elementor.com/help/search-widget/", "https://elementor.com/help/customize-the-search-results-archive/"], output_path: "docs/widgets/search/search-widget-and-results-archive.md", scheduled_for: "2026-06-22T20:00:00+03:00"}
- {stage_id: KB-016, title: Div Block element, source_url: "https://elementor.com/help/div-block-element/", output_path: "docs/elements/v4/div-block.md", scheduled_for: "2026-06-22T21:00:00+03:00"}
- {stage_id: KB-017, title: Flexbox element, source_url: "https://elementor.com/help/flexbox-element/", output_path: "docs/elements/v4/flexbox.md", scheduled_for: "2026-06-22T22:00:00+03:00"}
- {stage_id: KB-020, title: SVG element, source_url: "https://elementor.com/help/svg-element/", output_path: "docs/elements/v4/svg.md", scheduled_for: "2026-06-23T01:00:00+03:00"}
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
| 8 | Image element | `completed_with_gaps` |
| 9 | Paragraph element | `completed_with_gaps` |
| 10 | SVG element | `scheduled` — 2026-06-23 01:00 |

## قرارداد به‌روزرسانی

پس از هر مرحله وضعیت واقعی، `output_path`، زمان، SHA واقعی Commit، شمارنده‌ها، Manifestها و خلأهای شواهد ثبت شود. بدون Commit موفق، `storage_status: committed` اعلام نشود.

## موارد باز

- انتقال KB-001 تا KB-005 به فایل‌های مستقل Markdown.
- اعتبارسنجی Front Matter با Schema.
- افزودن GitHub Actions برای Schema، لینک‌ها، IDهای تکراری و هماهنگی Index/Manifest.
- اصلاح timezone ثبت‌شده در KB-006.
- پیاده‌سازی Claim-level provenance ID.
- تکمیل Gapهای KB-006 تا KB-010.
- ساخت Manifestهای evidence gaps و redirects.
- همگام‌سازی `docs/_index.md` برای KB-018 و KB-019؛ نوشتن این فایل در اجرای فعلی توسط بررسی ایمنی ابزار مسدود شد.

## قانون منبع

1. مستندات رسمی `elementor.com`
2. مستندات رسمی توسعه‌دهندگان Elementor
3. GitHub رسمی Elementor
4. Fixture واقعی و کنترل‌شده
5. منابع ثالث فقط با برچسب صریح

آخرین وضعیت ثبت‌شده: `2026-06-23T00:26:04+03:00`
