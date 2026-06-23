---
id: elementor.help.loop-carousel
title: Loop Carousel
source_url: https://elementor.com/help/loop-carousel/
source_type: official_help
version_scope: rolling_documentation
last_updated: 2024-01-14
researched_at: 2026-06-23T11:28:43+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-011
---

# جزوه جامع Loop Carousel در Elementor

## دامنه و وضعیت منبع

- منبع رسمی: مقاله Help Center با عنوان `Loop Carousel`
- آخرین به‌روزرسانی اعلام‌شده در صفحه: `January 14, 2024`
- این سند فقط ادعاهای صریح همان صفحه و تصاویر رسمی همان صفحه را پوشش می‌دهد.
- لینک‌های داخلی مثل `Learn about Loop Grids`، `Build a query`، `What is a Template?`، `Enable SVG support`، `Units of measurement`، `Choose a color`، `Typography` و `Advanced tab` بدون بررسی مستقل به این سند نسبت داده نمی‌شوند.

## تعریف documented

`Loop Carousel` در صفحه رسمی به‌عنوان چیزی معرفی شده که اساساً یک `Loop Grid` است، با این تفاوت که ورودی‌های منفرد به‌جای بالا و پایین، از کنار به کنار Scroll می‌شوند.

صفحه می‌گوید چون Carousel حرکت کناربه‌کنار دارد، تعدادی از کنترل‌ها با Loop Grid متفاوت هستند. این جمله فقط تفاوت در بخشی از کنترل‌ها را اثبات می‌کند، نه تفاوت کامل معماری یا Runtime.

## ساختار تنظیمات documented

صفحه برای `Loop Carousel widget` سه حوزه تنظیمات را فهرست می‌کند:

- `Content tab` — تب محتوا
- `Style tab` — تب استایل
- `Advanced tab` — تب پیشرفته

محتوای خود مقاله جزئیات Content و Style را توضیح می‌دهد. `Advanced tab` فقط به مقاله جداگانه لینک شده و در این سند تحلیل نمی‌شود.

## Content tab – Layout

`Layout` تعیین می‌کند Carousel چگونه برای بازدیدکنندگان نمایش داده شود.

### Choose a template — انتخاب Template

- از Dropdown می‌توان Template طراحی‌شده توسط کاربر یا Template آماده از Template Library را انتخاب کرد.
- سپس کاربر می‌تواند روی `Edit Template` کلیک کند.
- صفحه درباره شیوه ساخت Template، ساختار Loop Item، یا شرایط انتخاب Template توضیح مستقل نمی‌دهد و برای جزئیات به صفحه جداگانه Template لینک می‌دهد.

### Number of slides — تعداد اسلایدها

`Number of slides` تعداد آیتم‌های داخل Loop را مشخص می‌کند.

### Slides to display — اسلایدهای قابل نمایش

`Slides to display` تعداد آیتم‌هایی است که بازدیدکننده روی صفحه می‌بیند.

### Slides on Scroll — اسلاید در هر Scroll

`Slides on Scroll` تعیین می‌کند با کلیک کاربر روی فلش‌های قبلی و بعدی، چند اسلاید جلو برود. متن رسمی در این قسمت خطای تایپی دارد و عبارت را به‌صورت `is determines... when the use clicks...` آورده است؛ این خطا بدون اصلاح خاموش ثبت می‌شود.

### Equal Height — ارتفاع برابر

`Equal Height` برای حفظ تقارن Loop، آیتم‌ها را هم‌ارتفاع نگه می‌دارد.

## Content tab – Query

`Query` تعیین می‌کند چه آیتم‌هایی در Carousel ظاهر شوند. صفحه برای جزئیات ساخت Query به مقاله جداگانه لینک می‌دهد؛ بنابراین این سند فقط گزینه‌هایی را ثبت می‌کند که در همین صفحه آمده‌اند.

### Source — منبع

صفحه صریحاً می‌گوید Loop items محدود به Posts نیستند و Dropdown می‌تواند Loop را با موارد زیر پر کند:

- `Posts` — نوشته‌ها
- `Pages` — برگه‌ها
- `Landing Pages` — صفحات فرود
- `Manual Selection` — انتخاب دستی
- `Current Query` — Query فعلی
- `Related` — آیتم‌هایی که در همان Category قرار می‌گیرند

### Date — تاریخ

برای محدودکردن Loop به آیتم‌های جدیدتر، Dropdown تاریخ شامل این گزینه‌هاست:

- `Past Day` — روز گذشته
- `Past Week` — هفته گذشته
- `Past Month` — ماه گذشته
- `Past Quarter` — سه‌ماهه گذشته
- `Past Year` — سال گذشته
- `A custom date range` — بازه تاریخ سفارشی

### Order By — مرتب‌سازی بر اساس

صفحه می‌گوید آیتم‌هایی که زودتر در Loop قرار می‌گیرند بیشتر احتمال دارد توجه جلب کنند. گزینه‌های `Order By` عبارت‌اند از:

- `Date` — تاریخ
- `Title` — عنوان
- `Menu Order` — ترتیب منو
- `Last Modified` — آخرین تغییر
- `Number of comments` — تعداد دیدگاه‌ها
- `Random` — تصادفی

### Order — ترتیب

`Order` ترتیب نمایش آیتم‌ها را با حالت نزولی یا صعودی سفارشی‌تر می‌کند.

### Ignore Sticky Posts — نادیده‌گرفتن Sticky Posts

اگر Toggle روی `No` قرار بگیرد، Query شامل نوشته‌های ثابت‌شده می‌شود. صفحه می‌گوید اثر این گزینه فقط هنگام Preview صفحه دیده می‌شود.

### Query ID — شناسه Query

کاربر می‌تواند به Query یک ID بدهد تا برای Filtering در Backend استفاده شود. صفحه درباره فرمت ID، چرخه عمر Query ID، Hookها، یا API سمت سرور توضیح نمی‌دهد.

## Content tab – Settings

### Autoplay — پخش خودکار

`Autoplay` تعیین می‌کند آیتم‌ها به‌صورت خودکار حرکت کنند یا فقط وقتی بازدیدکننده روی Navigation icon کلیک می‌کند جابه‌جا شوند.

اگر `Autoplay` خاموش شود، صفحه می‌گوید گزینه‌هایی برای این کارها وجود دارد:

- داشتن Scroll بی‌نهایت برای Loop؛
- تعیین زمان Transition بین آیتم‌ها هنگام Scroll؛
- تنظیم حرکت آیتم‌ها از چپ به راست یا از راست به چپ. صفحه توضیح می‌دهد این کار در اصل مشخص می‌کند کدام Navigation قبلی و کدام بعدی است.

### Scroll Speed — سرعت Scroll

`Scroll Speed` سرعت حرکت Loop هنگام فعال‌بودن Autoplay را کنترل می‌کند و واحد آن Millisecond است.

### Pause on hover — توقف هنگام Hover

`Pause on Hover` به کاربران اجازه می‌دهد Loop را متوقف کنند تا آیتم‌های مورد علاقه خود را انتخاب کنند.

### Pause on interaction — توقف هنگام تعامل

`Pause on interaction` نیز برای توقف Loop به کاربر هنگام انتخاب آیتم‌های مورد علاقه معرفی شده است. صفحه تفاوت عملی دقیق آن با Pause on hover را توضیح نمی‌دهد.

### Infinite scroll — Scroll بی‌نهایت

`Infinite scroll` برای ادامه‌دار نگه‌داشتن Loop معرفی شده است.

### Transition Duration (ms) — مدت Transition

`Transition Duration (ms)` مدت زمانی است که حرکت از یک آیتم به آیتم بعدی طول می‌کشد و واحد آن Millisecond است.

### Direction — جهت

`Direction` تعیین می‌کند آیتم‌ها از چپ به راست یا از راست به چپ حرکت کنند.

## Content tab – Navigation

`Navigation` تعیین می‌کند بازدیدکنندگان چگونه در Carousel حرکت کنند.

### Arrows — فلش‌ها

- `Arrows` آیکون پیش‌فرض Navigation هستند.
- با کلیک روی Arrows، کاربر به‌صورت دستی به اسلاید قبلی و بعدی می‌رود.
- Toggle مربوطه می‌تواند Arrows را غیرفعال کند.

### Previous Icon — آیکون قبلی

برای جایگزینی آیکون فلش اسلاید قبلی، صفحه این امکان‌ها را نشان می‌دهد:

- انتخاب نکردن آیکون؛
- Upload کردن فایل SVG برای استفاده به‌عنوان Icon؛
- انتخاب Icon از Icon Library.

### Horizontal Orientation — جهت‌گیری افقی

`Horizontal Orientation` آیکون را در Start، Center یا End Carousel قرار می‌دهد.

### Position — موقعیت

`Position` با Slider محل دقیق Navigation icon را تعیین می‌کند.

### Vertical Orientation — جهت‌گیری عمودی

`Vertical Orientation` آیکون را در Top، Center یا Middle Carousel قرار می‌دهد.

### Next Icon — آیکون بعدی

برای جایگزینی آیکون اسلاید بعدی، صفحه این امکان‌ها را نشان می‌دهد:

- استفاده‌نکردن از Icon؛
- Upload کردن SVG؛
- انتخاب Icon از Icon Library.

در متن رسمی برای `Next Icon` عبارت `previous slide` آمده است. این احتمالاً خطای متنی صفحه است، اما در این سند فقط به‌عنوان ناسازگاری ثبت می‌شود و اصلاح فنی قطعی انجام نمی‌شود.

## Content tab – Pagination

`Pagination` تعیین می‌کند بازدیدکنندگان چگونه موقعیت خود را در Loop ببینند.

صفحه می‌گوید بسته به تعداد آیتم‌هایی که برای نمایش روی صفحه انتخاب می‌شود، آیتم‌های Loop به `pages` تقسیم می‌شوند. روش‌های نمایش Pagination عبارت‌اند از:

- `Dots` — نقطه‌ها؛ هر Dot نماینده یک Page است.
- `Fractions` — کسرها؛ با عدد نشان می‌دهد کاربر چقدر در Loop جلو رفته است.
- `Progress` — نوار پیشرفت؛ نوار نشان می‌دهد کاربر در Loop چقدر پیش رفته است.

## Style tab – Layout

`Layout` در Style tab فضای اطراف آیتم‌های Loop Carousel را کنترل می‌کند.

### Gap between slides — فاصله بین اسلایدها

`Gap between slides` مقدار فضای بین آیتم‌های Carousel را تعیین می‌کند.

## Style tab – Navigation

Style tab بخش Navigation برای برجسته‌تر یا کوچک‌تر کردن Navigation icons معرفی شده است.

### Size — اندازه

`Size` اندازه Navigation icons را تنظیم می‌کند.

### Normal/Hover — حالت عادی و Hover

- `Normal` ظاهر پیش‌فرض Navigation icons را تعیین می‌کند.
- `Hover` ظاهر Navigation icons هنگام Mouseover بازدیدکننده را تعیین می‌کند.

### Color — رنگ

`Color` رنگ Navigation icons را تنظیم می‌کند.

### Position — جایگاه

- `Inside` باعث می‌شود Navigation icons بخشی از Loop elements باشند.
- `Outside` آن‌ها را بیرون از Elements قرار می‌دهد.

## Style tab – Pagination

Style tab بخش Pagination ظاهر Pagination symbols را کنترل می‌کند. صفحه صریحاً می‌گوید این بخش فقط وقتی ظاهر می‌شود که Pagination در Content tab روشن باشد. بسته به نوع Pagination انتخاب‌شده، سه منو وجود دارد.

### Pagination by dots — صفحه‌بندی با نقطه‌ها

گزینه‌های مستند:

- `Size` — کنترل اندازه Pagination dots
- `Normal/Hover` — ظاهر پیش‌فرض و ظاهر هنگام Mouseover
- `Color` — رنگ Pagination icons
- `Position` — تنظیم جایگاه Dots
- `Inside` — قرارگرفتن Pagination icons درون Loop Carousel
- `Outside` — قرارگرفتن Pagination icons بیرون Carousel؛ در این حالت فاصله بین Carousel و Dots قابل ویرایش است
- `Spacing` — کم‌وزیادکردن فضای بین Loop items و Pagination dots

### Pagination by fraction — صفحه‌بندی کسری

گزینه‌های مستند:

- `Typography` — فونت عددهای Fraction
- `Color` — رنگ عددهای Fraction
- `Position` — جایگاه Fraction
- `Inside` — قرارگرفتن Fraction درون Loop Carousel
- `Outside` — قرارگرفتن Fraction بیرون Carousel؛ در این حالت فاصله بین Carousel و Fraction قابل ویرایش است
- `Spacing` — کم‌وزیادکردن فضای بین Loop items و Fraction

### Progress bar — نوار پیشرفت

گزینه‌های مستند:

- `Progress Bar` — کنترل فاصله بین محتوای Loop Carousel و Progress bar
- `Normal/Hover` — صفحه می‌گوید Progress bar می‌تواند بسته به محل Cursor رنگ عوض کند، سپس از عبارت‌های Normal و Hover استفاده می‌کند.

در متن رسمی برای توضیح Progress bar دوباره عبارت‌های `pagination dots` و `pagination dot` آمده است. این احتمالاً خطای کپی متن است و بدون اصلاح خاموش ثبت می‌شود.

## تصاویر رسمی observed

صفحه تصاویر رسمی زیر را در بدنه مقاله ارجاع می‌دهد:

1. `loop-carousel-1.png` — تصویر Content tab / Layout. در تصویر قابل مشاهده، `Choose a template` با نمونه `Elementor Loop Item #219 (Template)`، دکمه `EDIT TEMPLATE`، `Number of slides` با مقدار نمونه `6`، `Slides to display` با مقدار نمونه `3`، `Slides on Scroll` با مقدار نمونه `1`، و Toggle روشن `Equal height` دیده می‌شود.
2. `Content-tab-query-2.png` — تصویر Query. در تصویر قابل مشاهده، `Source: Posts`، تب‌های `INCLUDE` و `EXCLUDE`، `Date: All`، `Order By: Date`، `Order: DESC`، Toggle روشن `Ignore Sticky Posts` و فیلد `Query ID` دیده می‌شود.
3. `Content-tab-settings-2.png` — تصویر Settings. در تصویر قابل مشاهده، `Autoplay: YES`، `Scroll Speed (ms): 5000`، `Pause on hover: YES`، `Pause on interaction: YES`، `Infinite scroll: YES`، `Transition Duration (ms): 500` و `Direction: Left` دیده می‌شود.
4. `Content-tab-navigation-1.png` — تصویر رسمی Navigation در صفحه فهرست شده است؛ در این اجرا Fetch تصویری مستقیم با خطای Cache miss روبه‌رو شد، بنابراین فقط وجود تصویر و محل آن در صفحه ثبت می‌شود.
5. تصاویر آیکون‌های `Previous Icon` و `Next Icon` برای حالت بدون Icon، Upload SVG و Icon Library در صفحه فهرست شده‌اند؛ جزئیات تصویری آن‌ها بدون مشاهده مستقیم مستقل به Fact تبدیل نمی‌شود.
6. `Content-tab-pagination-1.png` — تصویر رسمی Pagination در صفحه فهرست شده است؛ Fetch مستقیم در این اجرا با Cache miss روبه‌رو شد.
7. `Style-tab-layout-1.png` — تصویر Style tab / Layout. در تصویر قابل مشاهده، `Gap between slides` با مقدار نمونه `10` دیده می‌شود.
8. `Style-tab-Navigation-1.png`، `Style-tab-pagination-dots.png`، `Style-tab-pagination-fraction.png` و `Style-tab-pagination-progress.png` در صفحه فهرست شده‌اند؛ Fetch مستقیم برخی از آن‌ها در این اجرا با Cache miss روبه‌رو شد و جزئیات فراتر از متن صفحه ثبت نمی‌شود.

اعداد موجود در تصاویر رسمی، مانند 6، 3، 1، 5000، 500 و 10، فقط `observed_example` هستند و به‌عنوان Default محصول ثبت نمی‌شوند.

## derived

- Loop Carousel از نظر مفهوم به خانواده Loop Grid مرتبط است، اما با حرکت افقی و کنترل‌های Carousel ارائه می‌شود.
- برای ساخت Carousel واقعی، وجود یک Template انتخاب‌شده یا Premade Template لازم به نظر می‌رسد، چون Layout با `Choose a template` آغاز می‌شود؛ با این حال صفحه درباره الزام فنی، خطاهای نبود Template یا فرایند کامل ساخت Template توضیح نمی‌دهد.
- Query در Loop Carousel از همان خانواده مفهومی Queryهای Loop است، اما جزئیات Backend filtering، Query ID و منطق Include/Exclude باید از منابع مستقل بررسی شود.
- Navigation و Pagination دو مسیر جدا برای حرکت و آگاهی از موقعیت کاربر در Carousel هستند: Navigation برای حرکت قبلی/بعدی و Pagination برای نمایش موقعیت در Loop.
- مقادیر نمونه تصاویر احتمالاً نمونه UI هستند و نباید Default قطعی تلقی شوند.

## insufficient_evidence

این صفحه به‌تنهایی شواهد کافی برای موارد زیر ندارد:

- نسخه دقیق Elementor یا Elementor Pro که این Widget را ارائه می‌کند؛
- Pro prerequisite یا محدودیت Plan؛
- وضعیت Stable، Beta یا Experimental؛
- فرایند کامل ساخت Loop Template از صفر؛
- قوانین انتخاب Template، خطاهای نبود Template یا سازگاری Templateها؛
- Default واقعی کنترل‌ها، حتی اگر در تصاویر نمونه مقدار دیده شود؛
- رفتار کامل Responsive controls و inheritance بین Breakpointها؛
- URL behavior، AJAX، Pagination URL، History API یا reload behavior؛
- Accessibility، Keyboard navigation، ARIA، Focus management و Screen reader behavior؛
- Runtime DOM، CSS output، JS carousel library یا Performance behavior؛
- Dynamic content جزئی، Dynamic Tags، ACF، WooCommerce یا Custom Post Type behavior؛
- Display Conditions؛ صفحه فقط لینک عمومی Display Conditions را در Navigation سایت دارد و درباره Loop Carousel توضیحی نمی‌دهد؛
- ارتباط دقیق با Taxonomy Filter، Search Results Archive یا Loop Grid خارج از تعریف مفهومی اولیه؛
- رفتار Manual Selection، Current Query و Related در سناریوهای واقعی؛
- محدودیت تعداد آیتم‌ها، محدودیت اسلایدها یا اثر Queryهای بزرگ؛
- رفتار Pause on hover در دستگاه‌های Touch؛
- تفاوت دقیق Pause on hover و Pause on interaction؛
- نحوه Sanitization و امنیت SVGهای Upload شده برای Icon؛
- رفتار RTL فراتر از گزینه `Direction`.

## مثال‌های قابل اتکا از همین صفحه

### مثال Layout

اگر در تصویر رسمی Layout مقدارهای نمونه دیده‌شده را فقط به‌عنوان مثال در نظر بگیریم، یک Carousel می‌تواند 6 آیتم در Loop داشته باشد، 3 آیتم را هم‌زمان نمایش دهد، و با هر Scroll یک آیتم جلو برود. این مثال از تصویر مشاهده می‌شود، نه از متن به‌عنوان Default محصول.

### مثال Settings

در تصویر رسمی Settings، Autoplay روشن، Scroll Speed برابر 5000 ms، Pause on hover روشن، Pause on interaction روشن، Infinite scroll روشن، Transition Duration برابر 500 ms و Direction برابر Left دیده می‌شود. این‌ها `observed_example` هستند و نباید Default تلقی شوند.

### مثال Query

در تصویر رسمی Query، Source روی Posts، Date روی All، Order By روی Date، Order روی DESC و Ignore Sticky Posts روی YES دیده می‌شود. این‌ها نمونه تصویری‌اند و متن صفحه Default بودن آن‌ها را اثبات نمی‌کند.

## وضعیت نهایی

```yaml
status: completed_with_gaps
verified_scope: official_article_text_and_listed_official_images
official_pages_reviewed: 1
official_images_indexed: 16
official_images_directly_viewed: 4
not_verified: version_pro_prerequisite_defaults_responsive_url_ajax_accessibility_runtime_dynamic_content_display_conditions
```
