---
project: elementor-v4-knowledge-base
status_version: 21
last_updated: 2026-06-23T10:56:00+03:00
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
| مراحل منتظر ظرفیت (`not_scheduled`) | 21 |
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
| KB-021 | Tabs Element | `not_scheduled` |
| KB-022 | YouTube element | `not_scheduled` |
| KB-023 | Classes in Elementor | `not_scheduled` |
| KB-024 | The Elementor Editor Class Manager | `not_scheduled` |
| KB-025 | Variables | `not_scheduled` |
| KB-026 | Variables Manager | `not_scheduled` |
| KB-027 | Import and export design systems | `not_scheduled` |
| KB-028 | Style tab – Layout | `not_scheduled` |
| KB-029 | Style tab – Spacing | `not_scheduled` |
| KB-030 | Style tab – Size | `not_scheduled` |
| KB-031 | Style tab – Position | `not_scheduled` |
| KB-032 | Style tab – Typography | `not_scheduled` |
| KB-033 | Style tab – Background | `not_scheduled` |
| KB-034 | Style tab – Border | `not_scheduled` |
| KB-035 | Style tab – Effects | `not_scheduled` |
| KB-036 | Responsive editing | `not_scheduled` |
| KB-037 | Dynamic tags in V4 | `not_scheduled` |

همه زمان‌ها بر اساس `Europe/Istanbul` هستند.

## ثبت اجرای مراحل Commit‌شده

```yaml
- {stage_id: KB-001, status: completed_with_gaps, source_url: "https://elementor.com/help/build-with-the-editor/widgets/", output_path: "docs/indexes/widgets-index.md", completed_at: "2026-06-23T10:51:16+03:00", commit_sha: d59a28d614e93221f5737df277f78fea0b6b42a2, evidence_gaps: [source_last_updated, complete_204_article_inventory, version_mapping, plan_requirements, runtime_behavior]}
- {stage_id: KB-002, status: completed_with_gaps, source_url: "https://elementor.com/help/build-with-the-editor/v4-editor/", output_path: "docs/indexes/editor-v4-index.md", completed_at: "2026-06-23T10:51:16+03:00", commit_sha: d028238125554e9fd35e4e31900f0fe97ddf96a4, evidence_gaps: [source_last_updated, complete_41_article_inventory, version_and_stability, dependencies, plan_requirements]}
- {stage_id: KB-003, status: completed_with_gaps, source_url: "https://elementor.com/help/explore-the-v4-features/", output_path: "docs/overview/explore-v4-features.md", completed_at: "2026-06-23T10:51:16+03:00", commit_sha: 4d2486d5997a642e994583cedf1a716aff2084b1, evidence_gaps: [exact_elementor_version, opt_in_conditions, class_storage, class_precedence, responsive, accessibility, runtime_dom]}
- {stage_id: KB-004, status: completed_with_gaps, source_url: "https://elementor.com/help/button-element/", output_path: "docs/elements/v4/button.md", completed_at: "2026-06-23T10:51:16+03:00", commit_sha: 7108a82dde4e446ac5cc88cd5ffbfb13bd08575d, evidence_gaps: [defaults, complete_states, focus_behavior, aria_and_markup, responsive, dynamic_tags, variables, plan_requirements, runtime_behavior]}
- {stage_id: KB-005, status: completed_with_gaps, source_url: "https://elementor.com/help/heading-element/", output_path: "docs/elements/v4/heading.md", completed_at: "2026-06-23T10:51:16+03:00", commit_sha: 7b0dd87368ae50bdd444f085cd268c3193c13bac, evidence_gaps: [complete_tag_list, default_tag, heading_hierarchy, accessibility, responsive, dynamic_tags, variables, runtime_markup]}
- {stage_id: KB-006, status: completed_with_gaps, source_url: "https://elementor.com/help/loop-grid/", output_path: "docs/widgets/loop/loop-grid.md", completed_at: "2026-06-22T11:07:20+03:00", commit_sha: ddceabd45d3c8c6655cb44bca6016f98426034ae, evidence_gaps: [version, Pro prerequisite, responsive, dynamic data, URL, AJAX, accessibility, screenshots]}
- {stage_id: KB-007, status: completed_with_gaps, source_url: "https://elementor.com/help/create-a-query-in-a-loop-grid/", output_path: "docs/widgets/loop/loop-grid-query.md", completed_at: "2026-06-22T12:05:51+03:00", commit_sha: ab98a1097ce26a2c2c665cab5d78ca504c1fd97e, evidence_gaps: [version, Pro prerequisite, redirect history, query controls, runtime behavior, screenshots]}
- {stage_id: KB-008, status: completed_with_gaps, source_url: "https://elementor.com/help/create-queries/", output_path: "docs/concepts/queries/create-queries.md", completed_at: "2026-06-22T13:19:02+03:00", commit_sha: 5cfd17535a33ef6cbc6dcb91eaa49803b6d1e3f9, evidence_gaps: [version, Pro prerequisite, query logic, Query ID lifecycle, AJAX, URL, accessibility, screenshots]}
- {stage_id: KB-009, status: completed_with_gaps, source_url: "https://elementor.com/help/pagination-for-loop/", output_path: "docs/widgets/loop/pagination.md", completed_at: "2026-06-22T14:07:00+03:00", commit_sha: 66ffe7d5cccf2b18b56919381878d6874b8b744c, evidence_gaps: [version, Pro prerequisite, control matrix, URL, AJAX, accessibility, responsive, style states, screenshots]}
- {stage_id: KB-010, status: completed_with_gaps, source_url: "https://elementor.com/help/taxonomy-filter/", output_path: "docs/widgets/loop/taxonomy-filter.md", completed_at: "2026-06-22T15:08:11+03:00", commit_sha: 95657df95445c453d310107715ddc3008baf68bb, evidence_gaps: [version, Pro prerequisite, taxonomy scope, query interaction, URL, AJAX, accessibility, responsive, style defaults, screenshots]}
- {stage_id: KB-018, status: completed_with_gaps, source_url: "https://elementor.com/help/image-element/", output_path: "docs/elements/v4/image.md", completed_at: "2026-06-22T23:08:43+03:00", commit_sha: 50923b62a319c99849f5fcf1663341c935d5fc2c, evidence_gaps: [exact_elementor_version, plan_or_pro_prerequisite, aspect_ratio, object_fit, lazy_loading, responsive_controls, dynamic_data, classes_and_variables, element_states, accessibility, seo, runtime_behavior]}
- {stage_id: KB-019, status: completed_with_gaps, source_url: "https://elementor.com/help/paragraph-element/", output_path: "docs/elements/v4/paragraph.md", completed_at: "2026-06-23T00:06:13+03:00", commit_sha: 44a8ebeef9dbb3dbbf0496c52e77fae0b8f2ef73, evidence_gaps: [exact_elementor_version, plan_or_pro_prerequisite, inline_editing, html_tag_and_semantics, partial_text_links, custom_attributes, color_controls, detailed_style_controls, responsive_controls, dynamic_data, classes_and_variables, element_states, frontend_accessibility, keyboard_and_focus_runtime, seo_behavior, generated_markup, runtime_behavior]}
- {stage_id: KB-020, status: completed_with_gaps, source_url: "https://elementor.com/help/svg-element/", output_path: "docs/elements/v4/svg.md", completed_at: "2026-06-23T01:04:00+03:00", commit_sha: 05cc163db725b1f79f2664bd6eede28a736a23bf, evidence_gaps: [sanitization, viewbox, dimensions, aspect_ratio, stroke, responsive_controls, dynamic_data, accessibility, keyboard_and_focus_runtime, runtime_markup]}
```

## مراحل زمان‌بندی‌شده

```yaml
- {stage_id: KB-011, title: Loop Carousel, source_url: "https://elementor.com/help/loop-carousel/", output_path: "docs/widgets/loop/loop-carousel.md", scheduled_for: "2026-06-23T11:00:00+03:00"}
- {stage_id: KB-012, title: Add an alternate template in a loop grid, source_url: "https://elementor.com/help/how-do-i-add-an-alternate-template-in-a-loop-grid/", output_path: "docs/widgets/loop/alternate-template.md", scheduled_for: "2026-06-23T12:00:00+03:00"}
- {stage_id: KB-013, title: Customize the layout of a Loop Grid, source_url: "https://elementor.com/help/customize-layout-loop/", output_path: "docs/widgets/loop/customize-layout.md", scheduled_for: "2026-06-23T13:00:00+03:00"}
```

## صف پژوهش مدیر صف

| اولویت | ID | موضوع | URL رسمی | وضعیت |
|---:|---|---|---|---|
| 1 | KB-014 | Off-Canvas in Loop Grid | `https://elementor.com/help/add-an-off-canvas-widget-to-a-loop-grid/` | `not_scheduled` |
| 2 | KB-015 | Search Widget and Search Results Archive | دو URL ثبت‌شده در Manifest | `not_scheduled` |
| 3 | KB-016 | Div Block element | `https://elementor.com/help/div-block-element/` | `not_scheduled` |
| 4 | KB-017 | Flexbox element | `https://elementor.com/help/flexbox-element/` | `not_scheduled` |
| 5 | KB-021 | Tabs Element | `https://elementor.com/help/tabs-element/` | `not_scheduled` |
| 6 | KB-022 | YouTube element | `https://elementor.com/help/youtube-element/` | `not_scheduled` |
| 7 | KB-023 | Classes in Elementor | `https://elementor.com/help/classes-in-elementor-2/` | `not_scheduled` |
| 8 | KB-024 | Class Manager | `https://elementor.com/help/the-elementor-editor-class-manager/` | `not_scheduled` |
| 9 | KB-025 | Variables | `https://elementor.com/help/variables/` | `not_scheduled` |
| 10 | KB-026 | Variables Manager | `https://elementor.com/help/variables-manager/` | `not_scheduled` |
| 11 | KB-027 | Design System import/export | `https://elementor.com/help/how-to-import-and-export-design-systems/` | `not_scheduled` |
| 12 | KB-028 | Style tab – Layout | `https://elementor.com/help/style-tab-layout/` | `not_scheduled` |
| 13 | KB-029 | Style tab – Spacing | `https://elementor.com/help/style-tab-spacing/` | `not_scheduled` |
| 14 | KB-030 | Style tab – Size | `https://elementor.com/help/style-tab-size/` | `not_scheduled` |
| 15 | KB-031 | Style tab – Position | `https://elementor.com/help/style-tab-position/` | `not_scheduled` |
| 16 | KB-032 | Style tab – Typography | `https://elementor.com/help/style-tab-typography/` | `not_scheduled` |
| 17 | KB-033 | Style tab – Background | `https://elementor.com/help/style-tab-background/` | `not_scheduled` |
| 18 | KB-034 | Style tab – Border | `https://elementor.com/help/style-tab-border/` | `not_scheduled` |
| 19 | KB-035 | Style tab – Effects | `https://elementor.com/help/style-tab-effects/` | `not_scheduled` |
| 20 | KB-036 | Responsive editing | `https://elementor.com/help/responsive-editing/` | `not_scheduled` |
| 21 | KB-037 | Dynamic tags in V4 | `https://elementor.com/help/dynamic-tags-in-v4/` | `not_scheduled` |

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

## موارد باز غیرصف پژوهش

- اعتبارسنجی Front Matter با Schema.
- افزودن GitHub Actions برای Schema، لینک‌ها، IDهای تکراری و هماهنگی Index/Manifest/STATUS.
- اصلاح timezone تاریخی ثبت‌شده در KB-006 بر اساس شواهد اجرای اولیه.
- پیاده‌سازی Claim-level provenance ID.
- تکمیل Gapهای اسناد `completed_with_gaps` با منابع مستقل یا Fixture کنترل‌شده.
- ساخت Manifestهای `evidence-gaps.yaml` و `redirects.yaml`.

## قانون منبع

1. مستندات رسمی `elementor.com`
2. مستندات رسمی توسعه‌دهندگان Elementor
3. GitHub رسمی Elementor
4. Fixture واقعی و کنترل‌شده
5. منابع ثالث فقط با برچسب صریح

آخرین وضعیت ثبت‌شده: `2026-06-23T10:56:00+03:00`
