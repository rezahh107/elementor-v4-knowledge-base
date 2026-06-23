# فهرست پایگاه دانش Elementor

این فایل فهرست انسانی اسناد است. مدل‌های زبانی ابتدا `LLM_GUIDE.md`، سپس `STATUS.md` و Manifestها را بخوانند.

## اسناد Commit‌شده

### Indexها و نمای کلی V4

- [Widgets index](indexes/widgets-index.md) — `KB-001` — `completed_with_gaps`
- [Editor V4 index](indexes/editor-v4-index.md) — `KB-002` — `completed_with_gaps`
- [Explore the V4 features](overview/explore-v4-features.md) — `KB-003` — `completed_with_gaps`

### Elementهای Editor V4

- [Button element](elements/v4/button.md) — `KB-004` — `completed_with_gaps`
- [Heading element](elements/v4/heading.md) — `KB-005` — `completed_with_gaps`
- [Image element](elements/v4/image.md) — `KB-018` — `completed_with_gaps`
- [Paragraph element](elements/v4/paragraph.md) — `KB-019` — `completed_with_gaps`
- [SVG element](elements/v4/svg.md) — `KB-020` — `completed_with_gaps`

### Loop و Query

- [Loop Grid widget](widgets/loop/loop-grid.md) — `KB-006` — `completed_with_gaps`
- [Build a query with the Loop Grid](widgets/loop/loop-grid-query.md) — `KB-007` — `completed_with_gaps`
- [Elementor Query Configuration](concepts/queries/create-queries.md) — `KB-008` — `completed_with_gaps`
- [Paginate your loop](widgets/loop/pagination.md) — `KB-009` — `completed_with_gaps`
- [Taxonomy Filter widget](widgets/loop/taxonomy-filter.md) — `KB-010` — `completed_with_gaps`
- [Loop Carousel](widgets/loop/loop-carousel.md) — `KB-011` — `completed_with_gaps`

## زمان‌بندی‌شده

- `KB-012` — Alternate Template in Loop Grid — 2026-06-23 12:00 Europe/Istanbul
- `KB-013` — Customize Layout in Loop Grid — 2026-06-23 13:00 Europe/Istanbul

## صف پژوهش منتظر ظرفیت

### تکمیل خانواده Loop و Elementهای پایه

1. `KB-014` — Off-Canvas in Loop Grid
2. `KB-015` — Search Widget and Search Results Archive
3. `KB-016` — Div Block element
4. `KB-017` — Flexbox element
5. `KB-021` — Tabs Element
6. `KB-022` — YouTube element

### Design System

7. `KB-023` — Classes in Elementor
8. `KB-024` — The Elementor Editor Class Manager
9. `KB-025` — Variables
10. `KB-026` — Variables Manager
11. `KB-027` — Import and export design systems

### Style System مشترک

12. `KB-028` — Style tab – Layout
13. `KB-029` — Style tab – Spacing
14. `KB-030` — Style tab – Size
15. `KB-031` — Style tab – Position
16. `KB-032` — Style tab – Typography
17. `KB-033` — Style tab – Background
18. `KB-034` — Style tab – Border
19. `KB-035` — Style tab – Effects
20. `KB-036` — Responsive editing
21. `KB-037` — Dynamic tags in V4

همه این مراحل `not_scheduled` هستند. مدیر صف یکتا پس از آزادشدن ظرفیت، فقط مرحله بعدی را بر اساس همین اولویت برای نزدیک‌ترین ساعت کامل آینده برنامه‌ریزی می‌کند.

## مسیرهای موضوعی

```text
docs/
├── elements/
│   └── v4/                   # Elementهای Editor V4
├── widgets/
│   ├── loop/                 # Loop Grid، Query، Pagination، Filter و Carousel
│   └── search/               # Search Widget و Search Results Archive
├── concepts/
│   └── queries/              # مفاهیم مشترک Query
├── design-system/            # Classes، Variables و Import/Export
├── style-system/             # Style tab، Responsive و Dynamic Tags
├── indexes/                  # Inventory صفحه‌های Index رسمی
├── overview/                 # نمای کلی و مفاهیم آغازین V4
└── evidence-gaps/            # تحلیل مستقل شکاف‌های شواهد
```

## قواعد نگهداری Index

- هر فایل جدید باید پس از Commit در این Index ثبت شود.
- عنوان، `stage_id` و وضعیت سند باید با Front Matter منطبق باشد.
- مرحله `not_scheduled` یا `scheduled` نباید لینک فایل جعلی داشته باشد.
- سند `superseded` باید به جایگزین خود پیوند بدهد.
- جزئیات ماشین‌خوان در `manifests/sources.yaml` نگهداری می‌شود.
