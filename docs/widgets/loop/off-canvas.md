---
id: elementor.help.loop-off-canvas
title: Add an Off Canvas widget to a Loop Grid
source_url: https://elementor.com/help/add-an-off-canvas-widget-to-a-loop-grid/
source_type: official_help
version_scope: widgets_loop_grid
last_updated: 2026-06-08
researched_at: 2026-06-23T12:58:00+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-014
---

# جزوه جامع Add an Off Canvas widget to a Loop Grid در Elementor

## مشخصات منبع

- مقاله رسمی: `Add an Off Canvas widget to a Loop Grid`
- آخرین به‌روزرسانی رسمی صفحه: `June 8, 2026`
- نوع منبع: Elementor Help / Build with the Editor / Widgets
- دامنه بررسی: فقط متن همین صفحه و ارجاع‌های تصویری رسمی همین صفحه.
- وضعیت شواهد: `completed_with_gaps`

## خلاصه اجرایی

این صفحه توضیح می‌دهد که `Loop Grid` می‌تواند `Off Canvas widget` را داخل Loop Item خود به‌کار بگیرد. مثال رسمی صفحه یک فروشگاه آنلاین است: Loop Item ابتدا محصول و توضیح کوتاه محصول را نشان می‌دهد و یک دکمه `More info` یا در ادامه مثال `Learn More`، پنل Off Canvas را باز می‌کند تا توضیح کامل و قیمت محصول نمایش داده شود.

صفحه صراحتاً هشدار می‌دهد که `Off Canvas widgets` در `Loop Carousel` یا `nested carousels` قابل استفاده نیستند. بنابراین دامنه مستند این مقاله، استفاده در `Loop Grid` است نه Loop Carousel.

## documented — شواهد صریح متنی

### هدف و کاربرد

- `Loop Grids` می‌توانند `Off Canvas widgets` را در خود داشته باشند.
- مثال رسمی: در فروشگاه آنلاین، Loop Item می‌تواند محصول و توضیح کوتاه را نمایش دهد؛ سپس Off Canvas با یک دکمه اطلاعات بیشتر را باز کند.
- محتوای بازشده در مثال رسمی شامل توضیح کامل محصول و قیمت است.

### محدودیت صریح

- `Off canvas widgets cannot be used in loop carousels or nested carousels.`
- ترجمه: ویجت‌های Off Canvas در Loop Carousel یا Carouselهای تو در تو قابل استفاده نیستند.

### پیش‌نیازها

مقاله فقط این پیش‌نیازهای عملی را نشان می‌دهد:

1. ساخت یا داشتن `Loop Grid` و `template`.
2. اگر Loop Grid قرار است محصولات را نمایش دهد، `template type` باید روی `Products` باشد.
3. برای جزئیات ساخت Loop Grid، صفحه به مقاله `Build a loop grid` ارجاع می‌دهد، اما محتوای آن مقاله در این سند بدون بررسی مستقل نسبت داده نمی‌شود.

### مراحل رسمی افزودن Off Canvas به Loop Grid

1. `Create a loop grid and template` — یک Loop Grid و Template بسازید.
2. اگر Loop Grid محصولات را نمایش می‌دهد، `template type` را روی `Products` قرار دهید.
3. `Add Featured Image to the template` — Featured Image را به Template اضافه کنید.
4. `Add Product Title to the template` — Product Title را به Template اضافه کنید.
5. `Add Off Canvas widget to the template` — ویجت Off Canvas را به Template اضافه کنید.
6. `Add Product Content to the Off Canvas widget` — Product Content را داخل Off Canvas widget اضافه کنید.
7. `Add Product Price to the Off Canvas widget` — Product Price را داخل Off Canvas widget اضافه کنید.
8. روی بخش سایه‌دار سمت راست کلیک کنید تا گزینه‌های Off Canvas widget باز شود.
9. در `Off Canvas Name` مقدار `Expanded Display` را وارد کنید.
10. صفحه می‌گوید گزینه‌های متعددی در Off Canvas widget قابل تغییر است، اما برای جزئیات به مقاله `Off Canvas widget` ارجاع می‌دهد؛ در همین مثال رسمی از `default options` استفاده می‌شود.
11. در پنل، `Editing mode` را روی `Off` بگذارید.
12. این کار شما را به صفحه ویرایش معمولی برمی‌گرداند.
13. یک `Button widget` به Loop Grid اضافه کنید.
14. این Button برای Trigger کردن Off Canvas widget استفاده می‌شود.
15. در پنل، نام Button را به `Learn More` تغییر دهید.
16. در فیلد `Link` روی آیکون `dynamic tag` کلیک کنید.
17. از منوی کشویی، `Off Canvas` را انتخاب کنید.
18. روی آیکون `wrench` کلیک کنید تا options box باز شود.
19. Widget را از dropdown انتخاب کنید. در مثال رسمی، نام widget برابر `Off Canvas` است.
20. روی Canvas، گزینه `Save & Back` را بزنید.
21. نتیجه رسمی: Loop Grid اکنون Featured Images، Product Images و دکمه Learn More را نشان می‌دهد؛ کلیک روی Learn More توضیح محصول و قیمت را آشکار می‌کند.

## کنترل‌ها و گزینه‌های نام‌برده‌شده

| نام انگلیسی | ترجمه فارسی | وضعیت شواهد |
|---|---|---|
| `Loop Grid` | شبکه تکرارشونده | مستند در صفحه |
| `template` | قالب آیتم لوپ | مستند در صفحه |
| `template type` | نوع قالب | فقط در ارتباط با Products ذکر شده |
| `Products` | محصولات | مستند برای مثال فروشگاهی |
| `Featured Image` | تصویر شاخص | مستند در مرحله ۲ |
| `Product Title` | عنوان محصول | مستند در مرحله ۳ |
| `Off Canvas widget` | ویجت آف‌کَنواس | مستند در مرحله ۴ |
| `Product Content` | محتوای محصول | مستند در مرحله ۵ |
| `Product Price` | قیمت محصول | مستند در مرحله ۶ |
| `Off Canvas Name` | نام Off Canvas | مستند در مرحله ۸ |
| `Expanded Display` | نام نمونه واردشده | مقدار مثال رسمی |
| `Editing mode` | حالت ویرایش | مستند در مرحله ۹ |
| `Off` | خاموش | مستند برای خروج از Editing mode |
| `Button widget` | ویجت دکمه | مستند در مرحله ۱۰ |
| `Learn More` | متن نمونه دکمه | مقدار مثال رسمی |
| `Link` | لینک | مستند در مرحله ۱۲ |
| `dynamic tag icon` | آیکون تگ داینامیک | مستند در مرحله ۱۲ |
| `Off Canvas` | تگ داینامیک Off Canvas | مستند در مرحله ۱۳ |
| `wrench icon` | آیکون آچار | مستند در مرحله ۱۴ |
| `options box` | جعبه گزینه‌ها | مستند در مرحله ۱۴ |
| `dropdown menu` | منوی کشویی | مستند در مرحله ۱۵ |
| `Save & Back` | ذخیره و بازگشت | مستند در مرحله ۱۶ |

## ارتباط با Query، Pagination و Taxonomy Filter

صفحه هیچ کنترل یا رفتار مستقیمی درباره `Query`، `Pagination` یا `Taxonomy Filter` توضیح نمی‌دهد. ارتباط مستند فقط این است که Off Canvas داخل Loop Grid و Template آن استفاده می‌شود. هر نتیجه درباره اثر Query، صفحه‌بندی، فیلترهای Taxonomy، شمارش آیتم‌ها یا رفتار AJAX خارج از شواهد این صفحه است.

## ساختار Trigger و محتوای Off Canvas

### Trigger مستند

- Trigger رسمی در مثال، یک `Button widget` است.
- Button با نام `Learn More` تنظیم می‌شود.
- در `Link`، از `dynamic tag icon` استفاده می‌شود.
- Dynamic Tag انتخاب‌شده `Off Canvas` است.
- با آیکون `wrench`، جعبه گزینه‌ها باز می‌شود و از dropdown، ویجت Off Canvas هدف انتخاب می‌شود.

### محتوای Off Canvas مستند

در مثال رسمی، داخل Off Canvas این دو ویجت/محتوا اضافه می‌شود:

- `Product Content`
- `Product Price`

صفحه به شکل صریح توضیح نمی‌دهد که آیا هر نوع محتوای دیگری نیز قابل افزودن است یا نه. این موضوع در این سند به Off Canvas widget عمومی نسبت داده نمی‌شود، چون مقاله فرعی بررسی مستقل نشده است.

## observed — شواهد تصویری رسمی قابل فهرست‌کردن

صفحه چند تصویر یا GIF رسمی را در مراحل کار درج کرده است. ابزار مشاهده مستقیم تصاویر برای این اجرا چند مورد را با `Cache miss` برگرداند؛ بنابراین جزئیات بصری فقط در حد جایگاه تصویر و ارتباط آن با متن همان مرحله ثبت می‌شود، نه به‌عنوان Fact مستقل تصویری.

| ارجاع تصویر در صفحه | URL رسمی قابل استخراج | مرحله مرتبط |
|---|---|---|
| Image بعد از توضیح template type | `https://elementor.com/help/wp-content/uploads/2024/12/image-1.gif` | ساخت Loop Grid و Template / Products |
| Image بعد از Product Title | `https://elementor.com/help/wp-content/uploads/2024/12/image-2.gif` | افزودن Featured Image و Product Title |
| Image بعد از Add Off Canvas | `https://elementor.com/help/wp-content/uploads/2024/12/image-3.gif` | افزودن Off Canvas widget |
| Image بعد از Product Price | `https://elementor.com/help/wp-content/uploads/2024/12/image-72.png` | افزودن Product Content و Product Price |
| Image بعد از کلیک روی بخش سایه‌دار | `https://elementor.com/help/wp-content/uploads/2024/12/image-73.png` | دسترسی به گزینه‌های Off Canvas |
| Image بعد از Off Canvas Name | `https://elementor.com/help/wp-content/uploads/2024/12/image-74.png` | واردکردن Expanded Display |
| Image بعد از Editing mode Off | `https://elementor.com/help/wp-content/uploads/2024/12/image-4.gif` | بازگشت به صفحه ویرایش معمولی |
| Image بعد از Learn More | `https://elementor.com/help/wp-content/uploads/2024/12/image-75.png` | افزودن و نام‌گذاری Button |
| Image بعد از dynamic tag icon | `https://elementor.com/help/wp-content/uploads/2024/12/image-76.png` | انتخاب Dynamic Tag |
| Image بعد از Select Off Canvas | `https://elementor.com/help/wp-content/uploads/2024/12/image-77.png` | انتخاب Off Canvas از dropdown |
| Image بعد از wrench icon | `https://elementor.com/help/wp-content/uploads/2024/12/image-78.png` | بازکردن options box و انتخاب widget |

## derived — برداشت‌های محدود و مشروط

- چون Trigger از طریق `Link` و `dynamic tag` روی Button انجام می‌شود، این صفحه نشان می‌دهد که Off Canvas در این سناریو از طریق یک Dynamic Tag به یک عنصر محرک وصل می‌شود. این برداشت به همین مثال محدود است.
- چون مقاله ابتدا Off Canvas را داخل Template اضافه می‌کند و سپس Button را برای Trigger همان Off Canvas تنظیم می‌کند، ترتیب عملی مستند این است: اول محتوای Off Canvas ساخته می‌شود، سپس Trigger به آن وصل می‌شود.
- چون صفحه درباره محصولات مثال می‌زند، استفاده مستند شامل سناریوی WooCommerce/Product است؛ اما صفحه اثبات نمی‌کند که تنها سناریوی ممکن همین است.
- چون صفحه می‌گوید Off Canvas در Loop Carousel و nested carousel قابل استفاده نیست، استفاده در Loop Grid یک تفاوت محدود و صریح با Loop Carousel دارد.

## insufficient_evidence — مواردی که این صفحه اثبات نمی‌کند

شواهد این صفحه برای موارد زیر کافی نیست:

- نسخه دقیق Elementor یا Elementor Pro که این قابلیت را معرفی یا پشتیبانی می‌کند؛
- نیازمندی Free/Pro یا Plan خاص؛
- تنظیمات کامل `Off Canvas widget` مانند position، direction، overlay، animation، close behavior، close button، size، entrance/exit behavior؛
- مقدارهای default واقعی Off Canvas؛ صفحه فقط می‌گوید در مثال از default options استفاده شده، اما ماتریس Defaultها را ثبت نمی‌کند؛
- رفتار responsive، breakpointها یا تفاوت نمایش Desktop/Tablet/Mobile؛
- ارتباط مستقیم با Query، Pagination، Taxonomy Filter، AJAX یا URL parameters؛
- رفتار runtime، Markup خروجی، DOM order، event binding یا script loading؛
- accessibility، keyboard focus، focus trap، ARIA role/name، Esc-to-close یا screen reader behavior؛
- display conditions؛ صفحه در مسیر قبلی/بعدی به مقاله‌ای درباره Display Conditions نزدیک است، اما برای Off Canvas در Loop Grid شرط نمایش توضیح نمی‌دهد؛
- stateها، hover/focus/active stateهای Button یا Off Canvas؛
- امکان استفاده از چند Off Canvas در یک Loop Item یا یک Loop Grid؛
- رفتار در صورت تکرار آیتم‌های Loop و یکتا بودن نام Off Canvas؛
- رفتار با nested elements، nested carousels جز همان منع صریح؛
- رفتار cache، performance، lazy loading یا SEO؛
- محتوای کامل مقاله‌های فرعی `Build a loop grid` و `Off Canvas widget`؛ این سند فقط وجود لینک به آن‌ها را ثبت می‌کند.

## چک‌لیست اجرای مستند بر اساس مقاله

1. Loop Grid و Template بسازید.
2. برای محصولات، Template Type را `Products` انتخاب کنید.
3. `Featured Image` و `Product Title` را در Template قرار دهید.
4. `Off Canvas widget` را به Template اضافه کنید.
5. `Product Content` و `Product Price` را داخل Off Canvas قرار دهید.
6. از ناحیه سایه‌دار سمت راست، تنظیمات Off Canvas را باز کنید.
7. در `Off Canvas Name` مقدار `Expanded Display` را وارد کنید.
8. `Editing mode` را روی `Off` بگذارید.
9. یک `Button widget` اضافه کنید.
10. متن/نام Button را `Learn More` قرار دهید.
11. در `Link`، Dynamic Tag با عنوان `Off Canvas` را انتخاب کنید.
12. از طریق `wrench icon`، widget هدف را از dropdown انتخاب کنید.
13. `Save & Back` را بزنید.

## وضعیت نهایی

```yaml
status: completed_with_gaps
verified_scope: official_article_text_and_image_references
not_verified: child_articles_runtime_accessibility_ajax_responsive_full_off_canvas_controls
official_pages_reviewed: 1
official_images_indexed: 11
official_images_directly_viewed: 0
```
