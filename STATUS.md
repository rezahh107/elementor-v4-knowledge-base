---
project: elementor-v4-knowledge-base
status_version: 20
last_updated: 2026-06-23T10:51:16+03:00
timezone: Europe/Istanbul
pipeline_status: in_progress
source_policy: official_first
llm_entrypoint: LLM_GUIDE.md
queue_manager_status: single_active
---

# وضعیت پایگاه دانش Elementor V4

این فایل منبع وضعیت اجرایی پژوهش است. مدل زبانی ابتدا `LLM_GUIDE.md` را بخواند. این فایل منبع حقیقت رفتار Elementor نیست.

## خلاصه وضعیت

| شاخص | مقدار |
|---|---:|
| منابع رسمی بررسی‌شده | 13 |
| اسناد تکمیل‌شده و Commit‌شده | 13 |
| اسناد در انتظار انتقال | 0 |
| مراحل پژوهشی زمان‌بندی‌شده | 3 |
| مراحل منتظر ظرفیت (`not_scheduled`) | 4 |
| مراحل در حال اجرا | 0 |
| مراحل ناموفق | 0 |
| مدیر صف فعال | 1 |
| وضعیت کلی | `in_progress` |

## وضعیت مراحل

| ID | عنوان | فایل/وضعیت |
|---|---|---|
| KB-001 | Widgets index | `docs/indexes/widgets-index.md` — `completed_with_gaps` |
| KB-002 | Editor V4 index | `docs/indexes/editor-v4-index.md` — `completed_with_gaps` |
| KB-003 | Explore the V4 features | `docs/overview/explore-v4-features.md` — `completed_with_gaps` |
| KB-004 | Button element | `docs/elements/v4/button.md` — `completed_with_gaps` |
| KB-005 | Heading element | `docs/elements/v4/heading.md` — `completed_with_gaps` |
| KB-006 | Loop Grid widget | `docs/widgets/loop/loop-grid.md` — `completed_with_gaps` |
| KB-007 | Build a query with the Loop Grid | `docs/widgets/loop/loop-grid-query.md` — `completed_with_gaps` |
| KB-008 | Elementor query configuration | `docs/concepts/queries/create-queries.md` — `completed_with_gaps` |
| KB-009 | Paginate your loop | `docs/widgets/loop/pagination.md` — `completed_with_gaps` |
| KB-010 | Taxonomy Filter widget | `docs/widgets/loop/taxonomy-filter.md` — `completed_with_gaps` |
| KB-011 | Loop Carousel | `scheduled` — 2026-06-23 11:00 |
| KB-012 | Add an alternate template in a loop grid | `scheduled` — 2026-06-23 12:00 |
| KB-013 | Customize the layout of a Loop Grid | `scheduled` — 2026-06-23 13:00 |
| KB-014 | Add an Off Canvas widget to a Loop Grid | `not_scheduled` |
| KB-015 | Search Widget and Search Results Archive | `not_scheduled` |
| KB-016 | Div Block element | `not_scheduled` |
| KB-017 | Flexbox element | `not_scheduled` |
| KB-018 | Image element | `docs/elements/v4/image.md` — `completed_with_gaps` |
| KB-019 | Paragraph element | `docs/elements/v4/paragraph.md` — `completed_with_gaps` |
| KB-020 | SVG element | `docs/elements/v4/svg.md` — `completed_with_gaps` |

همه زمان‌ها بر اساس `Europe/Istanbul` هستند.

## ثبت اجرای مراحل Commit‌شده

```yaml
- stage_id: KB-001
  status: completed_with_gaps
  source_url: https://elementor.com/help/build-with-the-editor/widgets/
  output_path: docs/indexes/widgets-index.md
  completed_at: 2026-06-23T10:51:16+03:00
  commit_sha: d59a28d614e93221f5737df277f78fea0b6b42a2
  evidence_gaps: [source_last_updated, complete_204_article_inventory, version_mapping, plan_requirements, runtime_behavior]
  notes: "محتوای قبلی pending_import از منبع رسمی بازسازی و به فایل مستقل منتقل شد."
- stage_id: KB-002
  status: completed_with_gaps
  source_url: https://elementor.com/help/build-with-the-editor/v4-editor/
  output_path: docs/indexes/editor-v4-index.md
  completed_at: 2026-06-23T10:51:16+03:00
  commit_sha: d028238125554e9fd35e4e31900f0fe97ddf96a4
  evidence_gaps: [source_last_updated, complete_41_article_inventory, version_and_stability, dependencies, plan_requirements]
  notes: "Index رسمی Editor V4 به سند مستقل تبدیل شد."
- stage_id: KB-003
  status: completed_with_gaps
  source_url: https://elementor.com/help/explore-the-v4-features/
  output_path: docs/overview/explore-v4-features.md
  completed_at: 2026-06-23T10:51:16+03:00
  commit_sha: 4d2486d5997a642e994583cedf1a716aff2084b1
  evidence_gaps: [exact_elementor_version, opt_in_conditions, class_storage, class_precedence, responsive, accessibility, runtime_dom]
  notes: "تعارض متنی General/Content در برابر General/Style بدون اصلاح خاموش ثبت شد."
- stage_id: KB-004
  status: completed_with_gaps
  source_url: https://elementor.com/help/button-element/
  output_path: docs/elements/v4/button.md
  completed_at: 2026-06-23T10:51:16+03:00
  commit_sha: 7108a82dde4e446ac5cc88cd5ffbfb13bd08575d
  evidence_gaps: [defaults, complete_states, focus_behavior, aria_and_markup, responsive, dynamic_tags, variables, plan_requirements, runtime_behavior]
  notes: "مقادیر مثال رسمی از Defaultهای محصول تفکیک شدند."
- stage_id: KB-005
  status: completed_with_gaps
  source_url: https://elementor.com/help/heading-element/
  output_path: docs/elements/v4/heading.md
  completed_at: 2026-06-23T10:51:16+03:00
  commit_sha: 7b0dd87368ae50bdd444f085cd268c3193c13bac
  evidence_gaps: [complete_tag_list, default_tag, heading_hierarchy, accessibility, responsive, dynamic_tags, variables, runtime_markup]
  notes: "خطای اصطلاحی Div Block در توضیح Link و تفاوت مثال‌های H1/H2 ثبت شد."
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
  counters: {official_pages_reviewed: 1, official_images_indexed: 11}
- stage_id: KB-019
  status: completed_with_gaps
  source_url: https://elementor.com/help/paragraph-element/
  output_path: docs/elements/v4/paragraph.md
  completed_at: 2026-06-23T00:06:13+03:00
  commit_sha: 44a8ebeef9dbb3dbbf0496c52e77fae0b8f2ef73
  evidence_gaps: [exact_elementor_version, plan_or_pro_prerequisite, inline_editing, html_tag_and_semantics, partial_text_links, custom_attributes, color_controls, detailed_style_controls, responsive_controls, dynamic_data, classes_and_variables, element_states, frontend_accessibility, keyboard_and_focus_runtime, seo_behavior, generated_markup, runtime_behavior]
  counters: {official_pages_reviewed: 1, official_images_indexed: 13, official_images_directly_viewed: 2, style_categories_named: 8}
- stage_id: KB-020
  status: completed_with_gaps
  source_url: https://elementor.com/help/svg-element/
  output_path: docs/elements/v4/svg.md
  completed_at: 2026-06-23T01:04:00+03:00
  commit_sha: 05cc163db725b1f79f2664bd6eede28a736a23bf
  evidence_gaps: [sanitization, viewbox, dimensions, aspect_ratio, stroke, responsive_controls, dynamic_data, accessibility, keyboard_and_focus_runtime, runtime_markup]
  notes: "فایل و Commit واقعی KB-020 با مخزن تطبیق داده شد."
```

## مراحل زمان‌بندی‌شده

```yaml
- {stage_id: KB-011, title: Loop Carousel, source_url: "https://elementor.com/help/loop-carousel/", output_path: "docs/widgets/loop/loop-carousel.md", scheduled_for: "2026-06-23T11:00:00+03:00"}
- {stage_id: KB-012, title: Add an alternate template in a loop grid, source_url: "https://elementor.com/help/how-do-i-add-an-alternate-template-in-a-loop-grid/", output_path: "docs/widgets/loop/alternate-template.md", scheduled_for: "2026-06-23T12:00:00+03:00"}
- {stage_id: KB-013, title: Customize the layout of a Loop Grid, source_url: "https://elementor.com/help/customize-layout-loop/", output_path: "docs/widgets/loop/customize-layout.md", scheduled_for: "2026-06-23T13:00:00+03:00"}
```

## صف بعدی مدیر صف

| اولویت | ID | موضوع | وضعیت |
|---:|---|---|---|
| 1 | KB-014 | Off-Canvas in Loop Grid | `not_scheduled` |
| 2 | KB-015 | Search Widget and Search Results Archive | `not_scheduled` |
| 3 | KB-016 | Div Block element | `not_scheduled` |
| 4 | KB-017 | Flexbox element | `not_scheduled` |

مدیر صف یکتا پس از کاهش تعداد تسک‌های پژوهشی فعال به کمتر از 3، فقط مرحله بعدی این جدول را برای نزدیک‌ترین ساعت کامل آینده برنامه‌ریزی می‌کند.

## وضعیت مدیر صف

```yaml
active_queue_managers: 1
duplicate_manager_disabled_at: 2026-06-23T10:46:54+03:00
active_research_tasks: 3
queue_policy: keep_at_most_3_active_research_tasks
```

## قرارداد به‌روزرسانی

پس از هر مرحله وضعیت واقعی، `output_path`، زمان، SHA واقعی Commit، شمارنده‌ها، Manifestها و خلأهای شواهد ثبت شود. بدون Commit موفق، `storage_status: committed` اعلام نشود.

## موارد باز

- اعتبارسنجی Front Matter با Schema.
- افزودن GitHub Actions برای Schema، لینک‌ها، IDهای تکراری و هماهنگی Index/Manifest/STATUS.
- اصلاح timezone تاریخی ثبت‌شده در KB-006 بر اساس شواهد اجرای اولیه.
- پیاده‌سازی Claim-level provenance ID.
- تکمیل Gapهای اسناد `completed_with_gaps` با منابع مستقل یا Fixture کنترل‌شده.
- ساخت Manifestهای `evidence-gaps.yaml` و `redirects.yaml`.
- پژوهش Design System: Classes، Class Manager، Variables، Variables Manager و Import/Export.
- پژوهش Style system مشترک: Layout، Spacing، Size، Position، Typography، Background، Border، Effects، Responsive Editing و Dynamic Tags.
- پژوهش Elementهای باقی‌مانده در Index V4 مانند Tabs و YouTube پس از پایان KB-011 تا KB-017.

## قانون منبع

1. مستندات رسمی `elementor.com`
2. مستندات رسمی توسعه‌دهندگان Elementor
3. GitHub رسمی Elementor
4. Fixture واقعی و کنترل‌شده
5. منابع ثالث فقط با برچسب صریح

آخرین وضعیت ثبت‌شده: `2026-06-23T10:51:16+03:00`
