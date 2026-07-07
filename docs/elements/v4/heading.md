---
id: elementor.help.heading-element
title: Heading element
source_url: https://elementor.com/help/heading-element/
canonical_url: https://elementor.com/help/heading-element/
source_type: official_help
version_scope: editor_v4
last_updated: 2025-08-28
researched_at: 2026-07-07T16:59:47+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-005
review_status: unreviewed
provenance_status: document_level_legacy
claim_record: evidence/claims/KB-005-heading.yaml
source_record: evidence/sources/SRC-KB-005-01.yaml
image_evidence: evidence/images/KB-005-heading.yaml
gap_record: evidence/gaps/KB-005-heading.yaml
---

# جزوه جامع Heading element در Elementor Editor V4

## مشخصات منبع

- مقاله رسمی: `Heading element`
- آخرین به‌روزرسانی درج‌شده در متن صفحه: `August 28, 2025`
- HTTP `Last-Modified` در capture برابر `July 5, 2026` است؛ این transport metadata جایگزین تاریخ درج‌شده در متن صفحه یا تاریخ semantic edit محسوب نمی‌شود.
- دامنه صریح: Editor V4
- مقاله کاربران V3 را به `Heading widget` جداگانه ارجاع می‌دهد.

## هدف Element

Heading برای افزودن و سفارشی‌سازی عنوان‌ها و تیترهای صفحه بدون نوشتن کد معرفی شده است. مقاله تأکید می‌کند Headingها توجه را به بخش‌های مهم سایت جلب می‌کنند.

## افزودن و حذف

### افزودن

1. در Elementor Editor روی `+` کلیک کنید.
2. Heading را با کلیک یا Drag به Canvas اضافه کنید.

### حذف

1. Heading را روی Canvas انتخاب کنید.
2. کلید Delete صفحه‌کلید را فشار دهید.

## کاربردهای مستند

- عنوان اصلی صفحه؛
- عنوان یا زیرعنوان نوشته وبلاگ؛
- Heading برای Testimonial؛
- عنوان Call-to-Action.

مثال رسمی، عنوان `Baking With Love` را برای وب‌سایت نانوایی به‌کار می‌برد.

## General tab

### Title — عنوان

متنی که در Heading نمایش داده می‌شود.

### Tag / HTML Tag — تگ HTML

نوع HTML Tag عنوان را تعیین می‌کند. مقاله صریحاً می‌گوید Tag صحیح به موتورهای جستجو برای فهم ساختار سایت کمک می‌کند و می‌تواند برای SEO مفید باشد.

در مثال:

- متن اولیه درباره انتخاب `<h1>` برای عنوان مهم صحبت می‌کند؛
- مراحل عملی مقدار `H2` را حفظ می‌کنند.

این دو نمونه Contextهای متفاوت‌اند و Default محصول را ثابت نمی‌کنند.

### Link — پیوند

با علامت Plus می‌توان URL مقصد را وارد کرد و Heading را Clickable ساخت.

#### Open in a new tab — بازکردن در تب جدید

پس از افزودن Link، Toggle بازکردن مقصد در تب جدید ظاهر می‌شود.

متن مقاله در توضیح Link چند بار به‌اشتباه عبارت `Div Block` را به‌جای Heading به‌کار می‌برد. این یک ناسازگاری مستند در متن منبع است و نباید به رفتار Div Block نسبت داده شود.

### ID — شناسه

برای Tag کردن یک Element منفرد در صفحه است و امکان Link دادن به همان Element را فراهم می‌کند.

## Style tab

مقاله خانواده‌های Style زیر را نام می‌برد:

- `Layout`
- `Spacing`
- `Size`
- `Position`
- `Typography`
- `Background`
- `Border`
- `Effects`

جزئیات کامل آن‌ها در صفحات مستقل است و بدون بررسی مستقل به Heading نسبت داده نمی‌شود.

### Layout / Align Self

مقاله صریحاً `Align Self` را در بخش Layout توضیح می‌دهد. این کنترل محل Heading در Parent container را تعیین می‌کند.

گزینه‌های مستند:

- `Start`
- `Center`
- `End`
- `Stretch`

در مثال، Center انتخاب می‌شود. این مقدار مثال است، نه Default.

### Typography

مقاله می‌گوید بخش Typography برای تنظیم Size و Font type استفاده می‌شود. سایر کنترل‌های Typography در صفحه مستقل قرار دارند.

## documented

Claimهای documented در `evidence/claims/KB-005-heading.yaml` به Source Record و snapshot captured متصل شده‌اند.

## observed

هیچ observed claim در این مرحله ایجاد نشده است. URL تصاویر فقط discovered است و retrieval، hash و inspection آن‌ها انجام نشده است.

## derived

- انتخاب Tag یک تصمیم معنایی محتواست، اما مقاله فقط اثر کلی بر فهم موتور جستجو را مطرح می‌کند و ترتیب Headingها یا WCAG را مستند نمی‌کند.
- مقادیر `H1` و `H2` در Contextهای مثال آمده‌اند و Default محصول را ثابت نمی‌کنند.
- ناسازگاری `Div Block` به‌عنوان anomaly منبع حفظ می‌شود و رفتار Heading یا Div Block را ثابت نمی‌کند.

## insufficient_evidence

این منبع اطلاعات کافی درباره موارد زیر ندارد:

- فهرست کامل Tagهای قابل انتخاب؛
- Default Tag؛
- قواعد hierarchy یا یک‌باربودن H1؛
- Markup خروجی و nested link behavior؛
- Accessibility، Screen Reader و keyboard focus؛
- Responsive controls و inherited values؛
- Dynamic Tags؛
- Variables و Global Classes؛
- Stateها؛
- همه کنترل‌های Typography؛
- Free/Pro prerequisite؛
- نسخه دقیق افزونه؛
- Runtime DOM/CSS و Browser behavior؛
- inspection تصاویر رسمی.

## تعارض‌ها و خطاهای متن منبع

```yaml
- type: example_variation
  values: [H1, H2]
  interpretation: examples_not_defaults
- type: terminology_error
  text: "Visitors clicking the Div Block..."
  expected_subject: Heading
  action: preserve_and_do_not_propagate
- type: metadata_category_difference
  page_reported_last_update: 2025-08-28
  http_last_modified: 2026-07-05
  action: preserve_separately
```

## وضعیت نهایی

```yaml
status: completed_with_gaps
verified_scope: captured_official_article_text
missing_evidence: [image_inspection, defaults, complete_tag_list, responsive, dynamic_data, accessibility, runtime_markup, peer_review]
```
