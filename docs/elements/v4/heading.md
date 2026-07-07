---
id: elementor.help.heading-element
title: Heading element
source_url: https://elementor.com/help/heading-element/
canonical_url: https://elementor.com/help/heading-element/
source_type: official_help
version_scope: editor_v4
last_updated: 2025-08-28
researched_at: 2026-07-06T15:31:27+03:30
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-005
review_status: unreviewed
provenance_status: document_level_legacy
---

# Heading element در Elementor Editor V4

این سند پیش‌نویس مهاجرت KB-005 از روی صفحه رسمی Elementor Help برای Heading element است. این سند peer reviewed نیست و هنوز Canonical source snapshot، Image inspection و Runtime fixture ندارد؛ بنابراین هیچ ادعای observed/runtime/authoritative از آن نتیجه‌گیری نمی‌شود.

## Source Context پیش‌نویس

این block هنوز Source Record schema-bound نیست و فقط context خوانش فعلی را نگه می‌دارد. Source Record نهایی باید پس از capture مخزنی، snapshot hash واقعی و ledger attestation ساخته شود.

```yaml
source_id: SRC-KB-005-01
stage_id: KB-005
requested_url: https://elementor.com/help/heading-element/
canonical_url: https://elementor.com/help/heading-element/
source_type: official_help
retrieved_at: 2026-07-06T15:31:27+03:30
http_status: 200
page_title: Heading element | Elementor
reported_last_updated: 2025-08-28
source_locator_version: 2
snapshot_binding_status: pending_repository_capture
normalized_document_sha256_status: pending_repository_capture
```

## دامنه مستند

صفحه رسمی عنوان `Heading element` دارد، تاریخ `Last Update: August 28, 2025` را نمایش می‌دهد و دامنه مقاله را برای کاربران Editor v4 اعلام می‌کند. برای کاربران Editor v3، صفحه به مقاله جداگانه `Heading widget` ارجاع می‌دهد.

## افزودن و حذف

برای افزودن element، کاربر در Elementor Editor روی `+` کلیک می‌کند و سپس element را با کلیک یا drag به canvas اضافه می‌کند. برای حذف، کاربر element را روی canvas انتخاب می‌کند و کلید Delete صفحه‌کلید را فشار می‌دهد.

## هدف Heading

منبع رسمی می‌گوید Headingها یا titleها توجه را به مهم‌ترین بخش‌های سایت جلب می‌کنند و Heading widget برای درج و سفارشی‌سازی headingهای صفحه بدون کدنویسی استفاده می‌شود.

## کاربردهای مستند

مثال رسمی یک وب‌سایت نانوایی را مطرح می‌کند که در بالای homepage، heading برجسته با متن `Baking With Love` اضافه می‌کند، HTML tag را به صورت `<h1>` برای SEO benefits انتخاب می‌کند و typography را با هویت برند هماهنگ می‌کند. کاربردهای اضافه‌ای که منبع نام می‌برد شامل عنوان‌ها و زیرعنوان‌های blog post، headingهای testimonial و عنوان‌های interactive Call-to-Action است.

## مراحل رسمی مثال

در مثال مرحله‌ای منبع، Heading widget به canvas اضافه می‌شود؛ در General tab و زیر Title، متن heading وارد می‌شود؛ برای clickable کردن heading، کاربر روی plus sign کنار Link کلیک می‌کند و URL مقصد را در Link field وارد می‌کند؛ سپس HTML Tag field برای تعیین نوع HTML tag استفاده می‌شود. متن مثال می‌گوید در همان مورد، heading به شکل H2 باقی می‌ماند تا اهمیت آن را نشان دهد.

## Style tab و Layout

در Style tab، کاربر Layout section را باز می‌کند. منبع رسمی `Align Self` را کنترلی معرفی می‌کند که تعیین می‌کند heading درون parent container کجا ظاهر شود. گزینه‌های مستند `Start`، `Center`، `End` و `Stretch` هستند. انتخاب `Center` در مقاله فقط مقدار مثال است و default محصول محسوب نمی‌شود.

## Typography

در مثال، Typography field برای تنظیم size و font type باز می‌شود و مقاله می‌گوید در همان مثال، heading فونت بزرگ‌تر و less formal می‌گیرد. جزئیات کامل Typography از همین صفحه استخراج نمی‌شود و باید از منبع مستقل Typography یا fixture جداگانه اثبات شود.

## General tab

General tab شامل بخش‌های Content و Settings است. در این صفحه، Title به‌عنوان متنی که در heading ظاهر می‌شود تعریف شده است. Tag برای انتخاب HTML tag heading توضیح داده شده و متن رسمی می‌گوید tag صحیح به search engines کمک می‌کند ساختار سایت را بفهمند و می‌تواند به SEO کمک کند. Link با plus sign وارد می‌شود. اگر link اضافه شود، گزینه `Open in a new tab` ظاهر می‌شود. ID برای tag کردن element منفرد در صفحه و link دادن به همان element توضیح داده شده است.

## ناسازگاری متن منبع

در بخش Link و Open in a new tab، منبع رسمی عبارت `Div Block` را در متن Heading element به کار می‌برد. این عبارت به‌عنوان anomaly منبع حفظ می‌شود و نباید به رفتار Div Block یا Heading نسبت داده شود مگر اینکه منبع یا fixture مستقل آن را تأیید کند.

## Style tab options

صفحه Heading element برای جزئیات Style options به مقاله‌های جداگانه `Layout`، `Spacing`، `Size`، `Position`، `Typography`، `Background`، `Border` و `Effects` ارجاع می‌دهد. این ارجاع‌ها وجود دسته‌های Style را نشان می‌دهند، اما جزئیات هر دسته در همین سند claim نمی‌شوند.

## شکاف‌های باقی‌مانده

- Canonical source snapshot و normalized document hash هنوز در مخزن ثبت نشده‌اند.
- Image inspection برای تصاویر مقاله انجام نشده است.
- Runtime fixture برای رفتار UI، selectorها، خروجی DOM یا defaultها وجود ندارد.
- Peer review انجام نشده و نباید به‌صورت خودکار ثبت شود.
