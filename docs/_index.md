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

## زمان‌بندی‌شده

- `KB-011` — Loop Carousel — 2026-06-23 11:00 Europe/Istanbul
- `KB-012` — Alternate Template in Loop Grid — 2026-06-23 12:00 Europe/Istanbul
- `KB-013` — Customize Layout in Loop Grid — 2026-06-23 13:00 Europe/Istanbul

## در صف و منتظر ظرفیت

- `KB-014` — Off-Canvas in Loop Grid
- `KB-015` — Search Widget and Search Results Archive
- `KB-016` — Div Block element
- `KB-017` — Flexbox element

این چهار مرحله با وضعیت `not_scheduled` در `STATUS.md` نگهداری می‌شوند و مدیر صف یکتا پس از آزادشدن ظرفیت، آن‌ها را به ترتیب برنامه‌ریزی می‌کند.

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
