# فهرست پایگاه دانش Elementor

این فایل فهرست انسانی اسناد است. مدل‌های زبانی ابتدا `LLM_GUIDE.md`، سپس `STATUS.md` و Manifestها را بخوانند.

## اسناد Commit‌شده

### Loop و Query

- [Loop Grid widget](widgets/loop/loop-grid.md) — `KB-006` — `completed_with_gaps`
- [Build a query with the Loop Grid](widgets/loop/loop-grid-query.md) — `KB-007` — `completed_with_gaps`
- [Elementor Query Configuration](concepts/queries/create-queries.md) — `KB-008` — `completed_with_gaps`
- [Paginate your loop](widgets/loop/pagination.md) — `KB-009` — `completed_with_gaps`
- [Taxonomy Filter widget](widgets/loop/taxonomy-filter.md) — `KB-010` — `completed_with_gaps`

## در انتظار انتقال از گفتگو

- `KB-001` — Widgets index
- `KB-002` — Editor V4 index
- `KB-003` — Explore the V4 features
- `KB-004` — Button element
- `KB-005` — Heading element

این موارد تا ایجاد فایل مستقل نباید به‌عنوان اسناد Commit‌شده یا قابل استناد ریپو معرفی شوند.

## زمان‌بندی‌شده

- `KB-011` — Loop Carousel

## مسیرهای موضوعی

```text
docs/
├── elements/               # Elementهای Editor V4
├── widgets/                # Widgetها و خانواده‌های Widget
│   └── loop/               # Loop Grid، Query، Pagination، Filter و Carousel
├── concepts/               # مفاهیم مشترک مانند Query، Classes و Variables
│   └── queries/
├── indexes/                # Inventory صفحه‌های Index رسمی
└── evidence-gaps/          # تحلیل مستقل شکاف‌های شواهد
```

## قواعد نگهداری Index

- هر فایل جدید باید پس از Commit در این Index ثبت شود.
- عنوان، `stage_id` و وضعیت سند باید با Front Matter منطبق باشد.
- سند `pending_import` نباید لینک فایل جعلی داشته باشد.
- سند `superseded` باید به جایگزین خود پیوند بدهد.
- جزئیات ماشین‌خوان در `manifests/sources.yaml` نگهداری می‌شود.
