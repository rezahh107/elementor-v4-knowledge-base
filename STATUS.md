---
project: elementor-v4-knowledge-base
status_version: 28
last_updated: 2026-06-23T14:00:00+03:00
timezone: Europe/Istanbul
pipeline_status: in_progress
source_policy: official_first
queue_manager_status: single_active
---

# وضعیت پایگاه دانش Elementor V4

## خلاصه وضعیت

committed_documents: 18
pending_import_documents: 0
scheduled_stages: 0
not_scheduled_stages: 19
failed_stages: 0

## وضعیت مراحل تکمیل‌شده اخیر

- KB-013: `docs/widgets/loop/customize-layout.md` — `completed_with_gaps` — commit `82e837133913be600b89cef604d59f0919ea6093`
- KB-014: `docs/widgets/loop/off-canvas.md` — `completed_with_gaps` — commit `3f00341d87342073e78e46d6fc42d7f6b705de32`
- KB-015: `docs/widgets/search/search-widget-and-results-archive.md` — `completed_with_gaps` — commit `cb483c967eccfa12636f214f7582830b97ba9806`

## ثبت اجرای KB-015

```yaml
stage_id: KB-015
status: completed_with_gaps
source_urls:
  - https://elementor.com/help/search-widget/
  - https://elementor.com/help/customize-the-search-results-archive/
output_path: docs/widgets/search/search-widget-and-results-archive.md
completed_at: 2026-06-23T14:00:00+03:00
commit_sha: cb483c967eccfa12636f214f7582830b97ba9806
evidence_gaps:
  - exact_pro_prerequisite
  - default_values
  - complete_submit_button_style_controls
  - complete_results_style_controls
  - additional_settings_details
  - url_query_parameter_behavior
  - ajax_behavior
  - empty_results_runtime_rendering
  - accessibility
  - keyboard_focus_behavior
  - performance_and_caching
  - multilingual_compatibility
  - visual_confirmation_of_all_screenshots
  - loop_carousel_usage_in_search_results_archive
notes:
  - دو منبع رسمی بررسی شد: Search Widget و Customize the Search Results Archive.
  - تصاویر رسمی هنگام بازکردن مستقیم برای چند نمونه Cache miss دادند؛ URL و جایگاه تصویر ثبت شد اما تحلیل تصویری انجام نشد.
  - docs/_index.md با commit جداگانه aab62d41c5a77fc16b203cde4c56b0d15e92fdd1 هماهنگ شد.
  - تلاش برای به‌روزرسانی manifests/sources.yaml و manifests/coverage.yaml توسط فیلتر ابزار مسدود شد و باید در اجرای بعدی اصلاح شود.
counters:
  official_pages_reviewed: 2
  official_images_indexed: 29
  official_images_directly_viewed: 0
  content_commit_sha: cb483c967eccfa12636f214f7582830b97ba9806
  index_commit_sha: aab62d41c5a77fc16b203cde4c56b0d15e92fdd1
```

## مراحل زمان‌بندی‌شده

```yaml
[]
```

## صف پژوهش مدیر صف

1. KB-016 — not_scheduled
2. KB-017 — not_scheduled
3. KB-021 — not_scheduled
4. KB-022 — not_scheduled
5. KB-023 — not_scheduled
6. KB-024 — not_scheduled
7. KB-025 — not_scheduled
8. KB-026 — not_scheduled
9. KB-027 — not_scheduled
10. KB-028 — not_scheduled
11. KB-029 — not_scheduled
12. KB-030 — not_scheduled
13. KB-031 — not_scheduled
14. KB-032 — not_scheduled
15. KB-033 — not_scheduled
16. KB-034 — not_scheduled
17. KB-035 — not_scheduled
18. KB-036 — not_scheduled
19. KB-037 — not_scheduled

آخرین وضعیت ثبت‌شده: `2026-06-23T14:00:00+03:00`
