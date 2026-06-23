---
id: elementor.help.button-element
title: Button element
source_url: https://elementor.com/help/button-element/
source_type: official_help
version_scope: editor_v4
last_updated: 2025-07-01
researched_at: 2026-06-23T10:47:13+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-004
---

# جزوه جامع Button element در Elementor Editor V4

## مشخصات منبع

- مقاله رسمی: `Button element`
- آخرین به‌روزرسانی: `July 1, 2025`
- دامنه صریح: مقاله برای کاربران `Editor v4` است و کاربران V3 را به مقاله جداگانه `Button Widget` ارجاع می‌دهد.

## هدف Element

Button element برای ایجاد دکمه‌های تعاملی و بصری معرفی شده است. کاربرد اصلی مستندشده، هدایت کاربر به یک Action یا مقصد از طریق Link است.

## افزودن و حذف

### افزودن

1. در Elementor Editor روی `+` کلیک کنید.
2. Element موردنظر را با کلیک یا Drag به Canvas اضافه کنید.

### حذف

1. Element را روی Canvas انتخاب کنید.
2. کلید Delete صفحه‌کلید را فشار دهید.

مقاله در چند بخش به اشتباه از واژه Widget برای Element استفاده می‌کند؛ این ناسازگاری اصطلاحی ثبت می‌شود و نباید به تغییر نوع محصول تفسیر شود.

## کاربردهای مستند

- CTA برای هدایت بازدیدکننده به صفحه ثبت‌نام؛
- لینک‌دادن از دکمه به صفحه پروژه یا نمای جزئیات؛
- استفاده در بنر یا پوستر رویداد و وبینار؛
- استفاده برای نمایش محتوای before/after.

## General tab

### Button text — متن دکمه

متنی که داخل دکمه نمایش داده می‌شود.

### Link — پیوند

با کلیک روی علامت Plus می‌توان Link را وارد کرد. بازدیدکننده با کلیک روی دکمه، مقصد Link را باز می‌کند.

#### Open in a new tab — بازکردن در تب جدید

اگر Button دارای Link باشد، این Toggle تعیین می‌کند مقصد در تب جدید باز شود.

### ID — شناسه

برای Tag کردن یک Element مشخص در صفحه استفاده می‌شود و می‌تواند مقصد لینک داخلی به همان Element باشد.

## مثال گام‌به‌گام رسمی

مقاله این مقادیر را فقط به‌عنوان مثال طراحی وارد می‌کند، نه Default محصول:

- `Button text`: Get Started
- `Width`: 200
- `Height`: 50
- `Font Family`: Sora
- `Font Weight`: 600
- `Font Size`: 16
- Background opacity: 0%
- Border radius همه Cornerها: 50
- Border width: 2
- Border color: `#FFFFFF`

این اعداد به‌عنوان `documented_example` ثبت می‌شوند و نباید Default تلقی شوند.

## Style tab

صفحه نام خانواده‌های Style زیر را ثبت می‌کند و برای جزئیات به مقاله‌های مستقل ارجاع می‌دهد:

- `Layout`
- `Spacing`
- `Size`
- `Position`
- `Typography`
- `Background`
- `Border`
- `Effects`

تنها جزئیاتی که خود مقاله مستقیماً در مثال نشان می‌دهد، تنظیم Width/Height، Typography، Background opacity، Border radius و Border است.

## Element states

مقاله یک نمونه صریح از State ارائه می‌دهد:

1. در `Classes text field` منوی Ellipsis کنار `local` باز می‌شود.
2. State برابر `Hover` انتخاب می‌شود.
3. واژه hover در Classes text box با رنگ صورتی ظاهر می‌شود.
4. Color و Opacity برای حالت Hover تغییر داده می‌شوند.

مقاله می‌گوید Element می‌تواند بسته به State ظاهر متفاوتی داشته باشد. در مثال، Button هنگام Mouse hover سفید می‌شود.

## observed

تصاویر رسمی مقاله مراحل زیر را نمایش می‌دهند:

- افزودن Element؛
- General panel؛
- Button text و Link؛
- Size؛
- Typography؛
- Background؛
- Border؛
- Hover state در Classes text box.

جزئیات تصویری که متن مقاله توضیح نداده، بدون مشاهده کنترل‌شده به‌عنوان Fact ثبت نمی‌شود.

## derived

- Button در V4 از Style system مشترک و local class استفاده می‌کند.
- مثال Hover نشان می‌دهد ویرایش State از Class context انجام می‌شود؛ اما این مقاله Schema یا ترتیب Cascade را اثبات نمی‌کند.
- `ID` در مقاله به‌عنوان مقصد لینک داخلی مطرح شده، ولی قواعد uniqueness یا escaping را توضیح نمی‌دهد.

## insufficient_evidence

شواهد این صفحه برای موارد زیر کافی نیست:

- Default واقعی همه کنترل‌ها؛
- مجموعه کامل Stateها غیر از Hover؛
- Keyboard focus و Focus-visible؛
- ARIA role/name و خروجی Markup؛
- رفتار Link protocolها و sanitization؛
- Dynamic Tags؛
- Responsive overrideها؛
- Variables و Global Classes؛
- Loading، disabled یا submit behavior؛
- Analytics و click tracking؛
- Free/Pro prerequisite؛
- نسخه دقیق افزونه سازگار؛
- رفتار Runtime در Browserها.

## وضعیت نهایی

```yaml
status: completed_with_gaps
verified_scope: official_article_text_and_listed_images
not_verified: runtime_markup_accessibility_defaults_responsive_dynamic_data
```
