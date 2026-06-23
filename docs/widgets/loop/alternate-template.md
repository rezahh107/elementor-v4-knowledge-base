---
id: elementor.help.loop-alternate-template
title: Add an alternate template in a loop grid
source_url: https://elementor.com/help/how-do-i-add-an-alternate-template-in-a-loop-grid/
source_type: official_help
version_scope: loop_grid
last_updated: 2025-09-02
researched_at: 2026-06-23T12:00:00+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-012
---

# جزوه جامع Alternate Template در Loop Grid

## مشخصات منبع

- منبع رسمی: `Add an alternate template in a loop grid`
- آدرس: `https://elementor.com/help/how-do-i-add-an-alternate-template-in-a-loop-grid/`
- آخرین به‌روزرسانی اعلام‌شده در صفحه: `September 2, 2025`
- دامنه سند: آموزش افزودن Alternate Template به Loop Grid در Elementor.
- وضعیت شواهد: `completed_with_gaps`، چون صفحه برای چند موضوع مهم مانند نسخه دقیق، پیش‌نیاز Pro، رفتار Runtime، Accessibility و AJAX توضیح کافی نمی‌دهد.

## خلاصه اجرایی

Alternate loop templates برای قرار دادن Templateهای سفارشی داخل Loop استفاده می‌شوند. صفحه توضیح می‌دهد که Loop Grid برای نمایش فهرست یکنواختی از Postها، Productها، Listingها و موارد مشابه مناسب است، اما گاهی باید داخل Loop یک آیتم متفاوت قرار گیرد؛ مثال رسمی، طراحی خاص برای هر محصول سوم است. صفحه می‌گوید Alternate loop templates امکان قرار دادن Templateهای سفارشی داخل Loop را فراهم می‌کنند.

## documented — موارد صریحاً مستندشده

### هدف Alternate Template

- ایجاد تنوع داخل Loop Grid بدون اینکه همه آیتم‌ها یک طراحی واحد داشته باشند.
- قرار دادن Template سفارشی در جایگاه مشخص داخل Loop.
- استفاده نمونه برای طراحی خاص یک آیتم در الگوی تکرارشونده، مانند هر آیتم سوم یا آیتم پنجم.
- استفاده به‌عنوان Ads یا Announcements در حالت Static alternative templates، چون می‌توان آن‌ها را بدون حذف آیتم‌های اصلی فهرست وارد Loop کرد.

### پیش‌نیازهای صریح صفحه

صفحه فقط این پیش‌نیازهای عملیاتی را صریحاً نشان می‌دهد:

1. داشتن یا ساختن یک `Loop Item Template`.
2. باز کردن یک Page در `Elementor Editor`.
3. ساخت یک `Loop Grid` یا انتخاب یک Loop Grid موجود روی صفحه.
4. انتخاب `Loop grid Widget` از طریق `Structure window` یا Right-click روی گوشه بالای سمت راست Widget.

صفحه برای ساخت Loop Item به مقاله جداگانه Theme Builder لینک می‌دهد؛ محتوای آن مقاله در این سند به‌عنوان Fact وارد نشده، چون این مرحله فقط همین صفحه را بررسی می‌کند.

### ساخت یا انتخاب Loop Item Template

صفحه می‌گوید ابتدا باید برای Loop item یک Template بسازید. در مثال رسمی، Template با نام `Elementor Ad` ساخته شده است. سپس در تنظیمات Loop Grid، از کنترل `Alternate Template` می‌توان Loop Item موردنظر را برای درج در Loop انتخاب کرد.

### فعال‌سازی Alternate Template

مسیر مستندشده:

1. صفحه‌ای را در Elementor Editor باز کنید.
2. یک Loop Grid بسازید یا Loop Grid موجود را انتخاب کنید.
3. `Loop grid Widget` را انتخاب کنید.
4. در `Content tab`، Toggle مربوط به `Apply an alternate template` را روشن کنید.
5. روی `Alternate Template` کلیک کنید تا Loop Item موردنظر برای درج در Loop انتخاب شود.

### کنترل `Alternate Template`

- با کلیک روی `Alternate Template`، کاربر Template/Loop Item جایگزین را انتخاب می‌کند.
- کاربر نام Template موردنظر را وارد می‌کند.
- در همان مرحله می‌توان با کلیک روی `Edit Template` یک Alternate Template جدید ساخت.
- طبق متن صفحه، کلیک روی `Edit Template` از Widget Panel کاربر را به `Theme Builder` می‌برد تا بتواند یک `Loop Item` جدید بسازد.

### کنترل `Position in grid`

- کنترل `Position in grid` برای تعیین موقعیت Alternative Template داخل Grid استفاده می‌شود.
- مثال رسمی صفحه: Alternate Template روی آیتم جایگاه پنجم اعمال شده است.
- صفحه مقدارهای مجاز کامل، حداقل/حداکثر، رفتار در صفحات بعدی یا ارتباط عدد Position با تعداد ستون‌ها را توضیح نمی‌دهد.

### چند Alternate Template

صفحه صریحاً می‌گوید کاربر به یک Alternative Template محدود نیست و دو روش برای افزودن Templateهای جایگزین بیشتر وجود دارد:

1. کلیک روی `copy icon` برای کپی کردن Alternative Template فعلی و سپس ویرایش آن.
2. کلیک روی `Add Item` برای افزودن یک Alternative Template جدید.

### Static alternative templates

صفحه این حالت را چنین تعریف می‌کند: `Static alternative templates` اجازه می‌دهند یک Alternate Template بدون Override کردن آیتم‌های موجود Loop داخل Loop تزریق شود. طبق صفحه، این رفتار برای Ads یا Announcements مفید است، چون می‌توان آن‌ها را بدون حذف آیتم‌های فهرست وارد کرد.

مراحل مستندشده:

1. ساخت Alternate Template همان‌طور که در بخش قبل توضیح داده شده است.
2. تعریف `Position in Grid` برای تعیین محل نمایش Alternative Item در Grid.
3. در صورت نیاز، خاموش کردن `Apply Once` اگر می‌خواهید Alternative Template در سراسر Loop Grid ظاهر شود.
4. روشن کردن `Static item position`.

### `Apply Once`

صفحه درباره رفتار پیش‌فرض چنین توضیح می‌دهد:

- به‌صورت پیش‌فرض، Alternative Template طبق Position تعیین‌شده در Grid در سراسر Loop ظاهر می‌شود.
- مثال رسمی: اگر Position برابر 5 باشد، Alternative Template به‌عنوان هر پنجمین Loop Item ظاهر می‌شود.
- Toggle مربوط به `Apply Once` این رفتار پیش‌فرض را تغییر می‌دهد و باعث می‌شود Alternative Template فقط یک بار در Loop ظاهر شود.

نکته مهم: صفحه هم در بخش Static alternative templates می‌گوید اگر می‌خواهید Alternative Template در سراسر Loop Grid ظاهر شود، `Apply Once` را خاموش کنید. بنابراین روشن بودن Apply Once برای نمایش یک‌باره و خاموش بودن آن برای تکرار در سراسر Loop Grid استفاده می‌شود.

### `Column Span`

- به‌صورت پیش‌فرض، Alternative Templates به اندازه عرض ستون یک آیتم در Grid فضا می‌گیرند.
- با Dropdown مربوط به `Column Span` می‌توان Alternative Template را طوری تنظیم کرد که فضای ستونی بیشتری بگیرد.
- صفحه مقدارهای موجود در Dropdown یا رفتار آن در Breakpointهای مختلف را توضیح نمی‌دهد.

## observed — شواهد تصویری رسمی قابل ارجاع

صفحه شامل ۱۴ تصویر رسمی در بدنه آموزش است. تصاویر از مسیرهای رسمی Elementor بارگذاری شده‌اند. در این اجرا، متن صفحه و لینک تصویرها استخراج شد؛ مشاهده مستقیم جزئیات تصویری توسط ابزار برای چند تصویر با خطای Cache miss روبه‌رو شد، بنابراین جزئیات داخل تصویرها فقط در حد جایگاه و ارتباطشان با متن رسمی ثبت می‌شود، نه به‌عنوان خوانش مستقل UI.

فهرست تصویرهای رسمی شناسایی‌شده:

1. `alternate-template-1.png` — همراه مرحله باز کردن صفحه در Elementor Editor.
2. `alt-temp-loop-2-1.png` — همراه انتخاب Loop Grid Widget.
3. `alt-temp-loop-3-1.png` — همراه Toggle مربوط به `Apply an alternate template`.
4. `alt-temp-loop-4.png` — همراه کنترل `Alternate Template`.
5. `Alternate-template-position-number.png` — همراه وارد کردن/انتخاب Template و `Edit Template`.
6. `alt-temp-loop-5.png` — همراه `Position in grid` و مثال جایگاه پنجم.
7. `alt-temp-loop-6.png` — همراه بخش ساخت چند Alternative Template.
8. `alt-temp-loop-7.png` — همراه Copy icon و Add Item.
9. `01-Create-an-alternative-template-cropped.jpg` — همراه شروع Static alternative templates.
10. `02-Add-position-in-grid-cropped.jpg` — همراه تعیین Position in Grid برای Static item.
11. `image-21.jpeg` — همراه مرحله مربوط به Apply Once در Static item.
12. `04-Turn-on-Static-item-position.jpg` — همراه روشن کردن `Static item position`.
13. `alt-temp-loop-12.png` — همراه توضیح `Apply Once`.
14. `alt-temp-loop-13.png` — همراه توضیح `Column Span`.

## derived — برداشت‌های محدود و مستند از همین صفحه

- Alternate Template به Loop Grid وابسته است، چون مراحل رسمی روی انتخاب یا ساخت Loop Grid و سپس انتخاب Loop grid Widget بنا شده‌اند.
- `Alternate Template` در این صفحه به Loop Item Template اشاره دارد، نه به یک Widget مستقل.
- `Position in grid` نقطه ورود Template جایگزین را کنترل می‌کند، اما صفحه الگوریتم دقیق تکرار در Pagination یا در Queryهای مختلف را توضیح نمی‌دهد.
- اگر `Apply Once` فعال باشد، Template فقط یک بار ظاهر می‌شود؛ اگر خاموش باشد، طبق مثال صفحه می‌تواند در سراسر Loop با Position تعیین‌شده تکرار شود.
- `Static item position` برای تزریق آیتم بدون Override کردن آیتم‌های اصلی معرفی شده است؛ بنابراین از نظر مفهومی با حالت جایگزینی معمول متفاوت است، اما صفحه جزئیات پیاده‌سازی فنی آن را توضیح نمی‌دهد.
- `Column Span` فقط روی فضای ستونی Alternative Template در Grid اثر مستند دارد؛ اثر آن روی Layoutهای Responsive یا Masonry از این صفحه قابل اثبات نیست.

## ارتباط با Loop Grid و Query

### Loop Grid

ارتباط با Loop Grid صریح است:

- کاربر باید یک Loop Grid بسازد یا Loop Grid موجود را انتخاب کند.
- تنظیمات از داخل `Loop grid Widget` و `Content tab` انجام می‌شوند.
- Alternate Template داخل همان Loop Grid قرار می‌گیرد.

### Query

صفحه از Query configuration یا کنترل‌های Query نام نمی‌برد. از آنجا که Loop Grid ذاتاً آیتم‌های لیست را نمایش می‌دهد، وجود Query در سطح Loop Grid قابل انتظار است، اما این صفحه نحوه تعامل Alternate Template با Query را توضیح نمی‌دهد. بنابراین جزئیات Query در این سند `insufficient_evidence` است.

## Pagination

صفحه درباره Pagination، صفحه‌های بعدی، Load More، Infinite Scroll، یا رفتار Alternate Template در Pagination توضیحی نمی‌دهد. تنها مورد نزدیک به این موضوع، تکرار Template در سراسر Loop بر اساس Position است. رفتار آن نسبت به Pagination از این صفحه قابل نتیجه‌گیری قطعی نیست.

## Responsive controls

صفحه هیچ کنترل Responsive، Breakpoint، Device-specific Position، Column Span per device یا رفتار Mobile/Tablet/Desktop را توضیح نمی‌دهد. هرگونه رفتار Responsive باید در پژوهش جداگانه یا Fixture کنترل‌شده بررسی شود.

## Style/Layout behavior

موارد مستند Style/Layout در این صفحه محدود است به:

- جایگاه Template با `Position in grid`.
- امکان تزریق Static item با `Static item position`.
- کنترل عرض ستونی با `Column Span`.

صفحه درباره Typography، Background، Border، Spacing، Effects، Equal Height، Masonry، Columns، Gap یا سایر Style controls توضیحی نمی‌دهد.

## Dynamic content و Display conditions

- صفحه از Dynamic content نام نمی‌برد.
- صفحه از Display conditions نام نمی‌برد.
- چون Template جایگزین از Loop Item Template استفاده می‌کند، ممکن است محتوای Template از داده‌های Loop استفاده کند؛ اما این صفحه چنین رفتاری را صریحاً توضیح نداده و نباید به‌عنوان Fact ثبت شود.

## محدودیت‌های مستند یا قابل استنتاج محدود

### مستند

- صفحه نشان می‌دهد که برای کار با Alternate Template باید Loop Grid انتخاب شود.
- صفحه می‌گوید برای ایجاد Alternate Template ابتدا باید Loop Item Template ساخته شود یا از کنترل Alternate Template انتخاب شود.
- صفحه می‌گوید کاربر محدود به یک Alternative Template نیست.

### شواهد ناکافی برای محدودیت‌های دیگر

صفحه موارد زیر را اثبات نمی‌کند:

- اینکه این قابلیت فقط برای Elementor Pro است یا در نسخه رایگان نیز موجود است.
- اینکه حداقل نسخه Elementor یا Elementor Pro چیست.
- اینکه چند Alternate Template می‌توان اضافه کرد.
- اینکه Position در Grid چه محدوده عددی دارد.
- اینکه Column Span چه مقادیر مجازی دارد.
- اینکه Apply Once در Pagination یا Queryهای صفحه‌بندی‌شده دقیقاً چگونه رفتار می‌کند.
- اینکه Static item position در خروجی DOM یا Query count چه اثری دارد.
- اینکه Dynamic Tags، Display Conditions یا AJAX با این قابلیت چگونه تعامل دارند.

## مثال رسمی بازسازی‌شده از صفحه

سناریوی مستند رسمی:

1. یک Loop Item Template ساخته شده و در مثال، نام آن `Elementor Ad` است.
2. یک صفحه در Elementor Editor باز می‌شود.
3. یک Loop Grid ساخته یا Loop Grid موجود انتخاب می‌شود.
4. از `Content tab` گزینه `Apply an alternate template` روشن می‌شود.
5. از `Alternate Template`، Template موردنظر انتخاب می‌شود.
6. با `Position in grid` جایگاه Template تعیین می‌شود.
7. در مثال، Template جایگزین در جایگاه پنجم قرار گرفته است.
8. اگر نیاز به چند Template جایگزین باشد، از Copy icon یا `Add Item` استفاده می‌شود.
9. اگر هدف تزریق آیتم بدون حذف آیتم‌های اصلی باشد، از `Static item position` استفاده می‌شود.
10. اگر قرار است Template فقط یک بار ظاهر شود، از `Apply Once` استفاده می‌شود.
11. اگر Template باید بیش از یک ستون را اشغال کند، از `Column Span` استفاده می‌شود.

## insufficient_evidence — مواردی که صفحه برای آن‌ها کافی نیست

```yaml
insufficient_evidence:
  - exact_elementor_version
  - pro_or_plan_prerequisite
  - complete_default_values
  - complete_control_matrix
  - query_interaction
  - pagination_behavior
  - ajax_behavior
  - url_behavior
  - responsive_controls
  - breakpoint_behavior
  - display_conditions
  - dynamic_content
  - accessibility
  - keyboard_and_focus_behavior
  - frontend_runtime_markup
  - dom_order
  - template_creation_details
  - theme_builder_details
  - static_item_query_count_effect
  - column_span_allowed_values
  - max_alternative_templates
  - interaction_with_masonry_or_custom_layouts
```

## وضعیت نهایی

```yaml
status: completed_with_gaps
verified_scope: official_article_text_and_indexed_official_images
not_verified: defaults_version_pro_requirement_query_pagination_ajax_accessibility_runtime_responsive_display_conditions_dynamic_content
official_pages_reviewed: 1
official_images_indexed: 14
official_images_directly_viewed: 0
```
