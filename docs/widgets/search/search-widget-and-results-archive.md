---
id: elementor.help.search-widget-results-archive
title: Search Widget and Search Results Archive
source_urls:
  - https://elementor.com/help/search-widget/
  - https://elementor.com/help/customize-the-search-results-archive/
source_type: official_help
version_scope: "Search widget introduced in Elementor 3.24 per source; archive page version not specified"
last_updated:
  search_widget: 2026-06-19
  search_results_archive: 2024-11-11
researched_at: 2026-06-23T14:00:00+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-015
---

# جزوه فارسی Search Widget و Search Results Archive در Elementor

## 1. دامنه و روش پژوهش

این جزوه فقط بر پایه دو منبع رسمی زیر تهیه شده است:

1. `https://elementor.com/help/search-widget/`
2. `https://elementor.com/help/customize-the-search-results-archive/`

هر ادعای رفتاری در چهار سطح تفکیک شده است:

- `documented`: مستقیماً در متن رسمی آمده است.
- `observed`: از تصویر یا جایگاه تصویر رسمی قابل مشاهده/ثبت است؛ در این اجرا برخی تصویرها به دلیل `Cache miss` فقط به‌عنوان URL/جایگاه ثبت شده‌اند و تحلیل تصویری از آن‌ها انجام نشده است.
- `derived`: نتیجه‌گیری محدود از ترکیب چند گزاره مستند، بدون افزودن رفتار جدید.
- `insufficient_evidence`: موضوعی که در درخواست پژوهش مهم بوده اما در همین دو صفحه شاهد صریح کافی ندارد.

> قرارداد منبع: صفحات فرعی مانند Add elements to a page، Loop Grid widget، Responsive Design یا Create or edit a Search Results page فقط وقتی نامشان در این دو صفحه آمده، به عنوان ارجاع خارجی ثبت شده‌اند؛ محتوای آن‌ها بدون بررسی مستقل به این سند نسبت داده نشده است.

## 2. مشخصات منبع

| منبع | عنوان رسمی | آخرین به‌روزرسانی رسمی | نقش در این جزوه |
|---|---|---:|---|
| Search widget | `Search widget` | `June 19, 2026` | تعریف Search widget، مراحل افزودن، Live Results، Loop Item، Query، Pagination و Style controls |
| Search Results Archive | `Customize the Search Results Archive` | `November 11, 2024` | ساخت/ویرایش قالب Search Results، Preview Settings، No-results preview و Display Condition |

## 3. خلاصه اجرایی

### documented

- `Search widget` به بازدیدکننده امکان جستجو در سایت می‌دهد تا محصولات، خدمات یا افراد مورد نیاز را سریع پیدا کند.
- نتایج Search widget در یک `Search Results template` نمایش داده می‌شود؛ بنابراین برای استفاده از این ویجت باید Search Results template وجود داشته باشد.
- ویجت علاوه بر نمایش نتایج در قالب، گزینه `Live Results` دارد؛ برای نتایج زنده باید یک `Loop Item` ساخته شود تا نتایج جستجو را نمایش دهد.
- صفحه `Search Results Page` یک Archive است و نتایج را در یک Archive template نمایش می‌دهد.
- Search widget در Elementor `3.24` معرفی شده است؛ برای نسخه‌های قدیمی‌تر صفحه رسمی به `Search Form widget` ارجاع می‌دهد.

### derived

- اگر فقط صفحه نتایج معمولی لازم است، باید Search Results template آماده/منتشر شده باشد.
- اگر تجربه جستجوی فوری داخل همان UI لازم است، علاوه بر Search Results template، یک Loop Item برای Live Results لازم است.
- چون صفحه Search Results Archive شرط انتشار `Include` و `Search Results` دارد، این قالب فقط زمانی به نتایج جستجو وصل می‌شود که این شرط ذخیره شود.

### insufficient_evidence

- صفحه‌ها مقدار پیش‌فرض هیچ‌یک از گزینه‌ها را به‌صورت کامل و قطعی مشخص نمی‌کنند.
- رفتار دقیق URL query parameter، نام پارامتر، AJAX، debounce، caching، accessibility، keyboard/focus، runtime markup، security، performance و empty-state rendering فقط در حد اشاره یا پیش‌نمایش آمده و جزئیات فنی ندارد.
- Pro prerequisite به‌صورت صریح در متن اصلی این دو صفحه اعلام نشده است؛ وجود Theme Builder/Loop Item می‌تواند نشانگر وابستگی عملی باشد اما بدون بررسی مستقل نمی‌توان آن را به‌عنوان الزام رسمی این سند ثبت کرد.

## 4. Search Widget چیست؟

### documented

`Search widget` برای جستجوی محتوای سایت توسط بازدیدکننده استفاده می‌شود. متن رسمی کاربرد را با پیدا کردن سریع محصولات، خدمات یا افراد توضیح می‌دهد.

برای نمایش نتایج، باید `Search Results template` وجود داشته باشد. در خود صفحه Search widget نوشته شده که نتایج با Search Results template نمایش داده می‌شوند.

`Live Results` یک قابلیت جداگانه است که نتایج را هنگام وارد کردن عبارت جستجو نمایش می‌دهد. برای این حالت باید `Loop Item` ساخته شود تا نتایج را نمایش دهد.

### insufficient_evidence

- صفحه توضیح نمی‌دهد Search widget دقیقاً چه post types یا taxonomies را در حالت پیش‌فرض جستجو می‌کند.
- صفحه توضیح نمی‌دهد الگوریتم جستجو، relevance، ترتیب نتایج پیش‌فرض یا سازگاری با جستجوی WooCommerce چگونه است.

## 5. پیش‌نیازها

### documented

| نیاز | شاهد رسمی |
|---|---|
| وجود Search Results template | صفحه Search widget می‌گوید نتایج در Search Results template نمایش داده می‌شوند و برای استفاده از ویجت باید این قالب وجود داشته باشد. |
| Loop Item برای Live Results | صفحه Search widget می‌گوید برای immediate/live search results باید Loop Item بسازید. |
| Theme Builder برای ساخت Loop Item | در مراحل ساخت Loop Item گفته شده از WP Admin به Theme Builder بروید و Loop Item را از آنجا بسازید. |
| Search Results Archive برای صفحه نتایج | صفحه Archive می‌گوید Search Results Page یک Archive است و نتایج را در archive template نمایش می‌دهد. |

### insufficient_evidence

- الزام نسخه دقیق Elementor Pro، نوع پلن، یا فعال بودن قابلیت خاص در همین دو صفحه با عبارت الزام‌آور ذکر نشده است.
- پیش‌نیازهای WordPress theme، permalink، server یا index search در این دو صفحه توضیح داده نشده‌اند.

## 6. افزودن Search Widget

### documented

مراحل عمومی افزودن ویجت:

1. در Elementor Editor روی `+` کلیک کنید.
2. همه widgetهای قابل دسترس نمایش داده می‌شوند.
3. ویجت را کلیک یا Drag کنید و به canvas ببرید.

در مثال رسمی، Search widget معمولاً در Header استفاده می‌شود. مثال صفحه درباره سایت فروشگاه جواهرات است که می‌خواهد Search bar را در Header بگذارد و Live Results نمایش دهد.

### documented — ساخت Loop Item برای Live Results

1. از `WP Admin` وارد `Theme Builder` شوید.
2. در پنل، کنار `Loop Item` روی علامت `+` کلیک کنید.
3. Archive Library در بخش Loop items باز می‌شود.
4. می‌توانید یکی از Loop Item templateها را انتخاب کنید یا Loop Item اختصاصی بسازید.
5. روی template مورد نظر Hover کنید و `Insert` را بزنید.
6. در popup روی `Apply` کلیک کنید.
7. Loop Item روی canvas ظاهر می‌شود.
8. از `Page Settings`، عنوان را به `Search Loop Item` تغییر دهید.
9. روی `Publish` کلیک کنید.
10. از Elementor Logo خارج شوید و به WP Admin برگردید.
11. دوباره به Theme Builder برگردید.
12. در پنل روی `Header` کلیک کنید و در بخش راست روی `Edit` بزنید.

### documented — افزودن ویجت به Header و اتصال Live Results

1. یک `Search widget` به Header اضافه کنید.
2. در پنل بخش `Results` را باز کنید.
3. گزینه `Live Results` را روی `Show` بگذارید.
4. منوی `Choose a template` ظاهر می‌شود.
5. در `Choose a template`، قالب `Search Loop Item` را انتخاب کنید.

### insufficient_evidence

- صفحه بیان نمی‌کند Live Results بدون Search Results Archive چه رفتاری دارد.
- صفحه رفتار صفحه جستجو در حالت نبود Header یا نبود Theme Builder را توضیح نمی‌دهد.

## 7. تنظیمات Content tab

صفحه رسمی Content tab را شامل این بخش‌ها معرفی می‌کند:

- `Search Field`
- `Results`
- `Query`
- `Additional Settings`

### 7.1 Search Field / Input

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Placeholder` | متن جای‌نگهدار | documented | متنی که به‌صورت پیش‌فرض در کادر جستجو ظاهر می‌شود. |
| `Icon` | آیکون | documented | امکان افزودن آیکون به Search box وجود دارد. |
| `Autocomplete` | تکمیل خودکار | documented | اگر روی `Show` باشد، سایت هنگام وارد کردن متن، عبارت‌های احتمالی جستجو را پیشنهاد می‌دهد. |

### 7.2 Clear

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Icon` | آیکون پاک‌کردن | documented | آیکونی در search bar نمایش داده می‌شود که با کلیک روی آن تمام متن کادر جستجو حذف می‌شود. امکان انتخاب نکردن آیکون نیز ذکر شده است. |

### 7.3 Submit

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Trigger` | محرک اجرای جستجو | documented | عمل شروع جستجو را تعیین می‌کند. گزینه‌ها: `Submit button`، `Enter key`، `Both`. |
| `Submit button` | دکمه ارسال | documented | یکی از گزینه‌های Trigger. |
| `Enter key` | کلید Enter | documented | یکی از گزینه‌های Trigger. |
| `Both` | هر دو | documented | دکمه ارسال و کلید Enter هر دو می‌توانند جستجو را شروع کنند. |
| `Text` | متن دکمه | documented | متنی که روی Submit button نمایش داده می‌شود؛ وقتی از Submit button استفاده شود. |
| `Icon` | آیکون دکمه | documented | آیکون می‌تواند به جای متن یا همراه متن روی Submit button نمایش داده شود. |

### 7.4 Results / Live Results

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Live Results` | نتایج زنده | documented | اگر روی `Show` باشد، ویجت هنگام تایپ کاربر نتایج جستجو را نمایش می‌دهد. |
| `Choose a template` | انتخاب قالب | documented | اگر Loop item template آماده دارید، اینجا انتخاب می‌شود. |
| `Create Template` | ساخت قالب | documented | اگر Loop item آماده ندارید، برای ساخت Loop item استفاده می‌شود. |
| `Edit template` | ویرایش قالب | documented | اگر Loop item آماده وجود داشته باشد، دکمه Create template به Edit template تغییر می‌کند. |

### 7.5 Query

`Query` برای محدود کردن نوع محتوایی است که نتایج جستجو نمایش می‌دهند.

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Source` | منبع | documented | با dropdown، نوع محتوای قابل جستجو محدود می‌شود. |
| `Products` | محصولات | documented | یکی از گزینه‌های Source. |
| `Posts` | نوشته‌ها | documented | یکی از گزینه‌های Source. |
| `Pages` | برگه‌ها | documented | یکی از گزینه‌های Source. |
| `Landing Pages` | صفحات فرود | documented | یکی از گزینه‌های Source. |
| `Floating Buttons` | دکمه‌های شناور | documented | یکی از گزینه‌های Source. |
| `Include` | شامل کردن | documented | برای ساخت Query جهت تعیین آیتم‌های مورد نظر استفاده می‌شود. متن رسمی به Loop Grid اشاره می‌کند. |
| `Exclude` | حذف کردن | documented | برای ساخت Query جهت کنار گذاشتن آیتم‌ها استفاده می‌شود؛ متن رسمی در این قسمت احتمالاً عبارت `Click include` را تکرار کرده که به‌عنوان متن خام منبع ثبت می‌شود. |
| `Include By/Exclude By` | شامل/حذف بر اساس | documented | با textbox نوع postهایی که می‌خواهید include یا exclude شوند وارد می‌شود. |
| `Date` | تاریخ | documented | با dropdown، آیتم‌ها بر اساس زمان ایجاد include یا exclude می‌شوند. |
| `Order By` | مرتب‌سازی بر اساس | documented | معیار ترتیب آیتم‌ها را تعیین می‌کند. |
| `Order` | جهت ترتیب | documented | تعیین می‌کند آیتم‌ها به صورت `DESC` یا `ASC` مرتب شوند. |
| `DESC` | نزولی | documented | ترتیب نزولی. |
| `ASC` | صعودی | documented | ترتیب صعودی. |
| `Posts Per Page` | تعداد نوشته در هر صفحه | documented | تعداد آیتم‌های نمایش‌داده‌شده در هر صفحه نتایج جستجو را تعیین می‌کند. |
| `Query ID` | شناسه Query | documented_with_source_conflict | متن رسمی می‌گوید با dropdown برای include/exclude طبق زمان ایجاد استفاده می‌شود؛ این توصیف با عنوان Query ID ناسازگار به نظر می‌رسد، بنابراین بدون اصلاح ثبت شده است. |

### 7.6 Pagination

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Type` | نوع صفحه‌بندی | documented | انتخاب بین `Numbers`، `Previous/Next` یا `Numbers + Previous/Next`. |
| `Numbers` | شماره‌ها | documented | حالت شماره صفحات. |
| `Shorten` | کوتاه‌سازی | documented | اگر صفحات زیاد باشند، چند لینک صفحه و ellipsis `…` نشان می‌دهد، نه همه شماره‌ها. |
| `Page Limit` | محدودیت تعداد صفحات | documented | برای Numbers، Previous/Next و ترکیبی قابل تنظیم ذکر شده است. |
| `Previous/Next` | قبلی/بعدی | documented | حالت برچسب‌های قبلی و بعدی. |
| `Previous` label | برچسب قبلی | documented | برچسب Previous قابل تغییر است. |
| `Next` label | برچسب بعدی | documented | برچسب Next قابل تغییر است. |
| `Numbers + Previous/Next` | شماره‌ها + قبلی/بعدی | documented | حالت ترکیبی با Page Limit، Previous، Next و Shorten. |

### insufficient_evidence برای Content tab

- `Additional Settings` در متن استخراج‌شده نام برده شده اما جزئیات گزینه‌های آن در همین صفحه، در بخش قابل استناد حاضر، توضیح داده نشده است.
- رفتار دقیق AJAX و URL در Pagination یا Live Results توضیح داده نشده است.
- Empty/no-results برای Search widget به صورت UI control توضیح داده نشده است؛ فقط در صفحه Archive پیش‌نمایش No-results آمده است.

## 8. Responsive controls

### documented

در مثال رسمی، بعد از فعال‌سازی Live Results، نتایج ابتدا در یک column نمایش داده شده‌اند. سپس برای Desktop مقدار `Columns` روی `3` گذاشته شده و با responsive icons به mobile editing رفته‌اند و مقدار `Columns` روی `1` قرار گرفته است. نتیجه رسمی: Live results روی PC در سه ستون و روی mobile در یک ستون نمایش داده می‌شود.

### insufficient_evidence

- صفحه جزئیات breakpointها، inherited responsive values، یا رفتار tablet را توضیح نمی‌دهد.
- فقط کنترل `Columns` در مثال responsive ذکر شده است؛ سایر responsive controls برای Search widget به‌صورت کامل مستند نشده‌اند.

## 9. Style tab

صفحه رسمی Style tab را برای تعیین ظاهر menu items و controls معرفی می‌کند و بخش‌های زیر را نام می‌برد:

- `Search Field`
- `Clear`
- `Submit Button`
- `Results`
- `Additional Settings`

### 9.1 Search Field

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Typography` | تایپوگرافی | documented | انتخاب font و size متن در search box. |
| `Placeholder Color` | رنگ Placeholder | documented | رنگ متن پیش‌فرض در کادر جستجو. |
| `Normal` | حالت عادی | documented | ظاهر پیش‌فرض متن. |
| `Focus` | حالت فوکوس | documented | ظاهر زمانی که search box انتخاب شده است. |
| `Background Type` | نوع پس‌زمینه | documented | انتخاب background برای search box. |
| `Text Color` | رنگ متن | documented | رنگ متن واردشده توسط بازدیدکننده. |
| `Icon Color` | رنگ آیکون | documented | رنگ آیکون در submit button طبق متن منبع؛ در بخش Search Field آمده است. |
| `Border Type` | نوع حاشیه | documented | افزودن border دور search box؛ در صورت افزودن border، Border Color و Border Width قابل افزودن‌اند. |
| `Border Color` | رنگ حاشیه | documented | رنگ border کادر جستجو. |
| `Box Shadow` | سایه جعبه | documented | افزودن depth با shadow. |
| `Border Radius` | گردی گوشه‌ها | documented | گرد کردن گوشه‌های text box. |
| `Padding` | فاصله داخلی | documented | فاصله داخلی. |
| `Gap between input and button` | فاصله بین ورودی و دکمه | documented | اندازه search box را با افزایش فاصله بین box و submit button کنترل می‌کند. |

### 9.2 Clear

| گزینه انگلیسی | ترجمه فارسی | وضعیت شاهد | شرح |
|---|---|---|---|
| `Icon Size` | اندازه آیکون | documented | اندازه search/clear icon را تنظیم می‌کند. |
| `Normal` | عادی | documented | حالت پیش‌فرض icon یا text. |
| `Hover` | هاور | documented | حالت وقتی بازدیدکننده mouse را روی icon/text می‌برد. |
| `Icon Color` | رنگ آیکون | documented | در متن رسمی برای buttons that contain text به رنگ متن button اشاره شده است؛ عیناً ثبت می‌شود. |

### 9.3 Submit Button / Results / Additional Settings

### insufficient_evidence

- صفحه عنوان `Submit Button`، `Results` و `Additional Settings` را در Style tab نام می‌برد، اما در متن قابل استناد استخراج‌شده جزئیات کامل همه گزینه‌های آن‌ها دیده نشد.
- بنابراین جزئیات رنگ، فاصله، typography یا stateهای Submit Button و Results فقط در صورت بررسی تصویری/متنی کامل‌تر قابل تکمیل است.

## 10. تنظیم ارتفاع Search widget

### documented

برای narrow یا widen کردن اندازه Search widget:

1. ویجت را انتخاب کنید.
2. وارد `Style tab` شوید.
3. فیلد `Submit Button` را باز کنید.
4. در `Padding`، مقدار `Top` و `Bottom` را `0` قرار دهید.
5. فیلد `Search Field` را باز کنید.
6. در `Padding`، مقدار `Top` و `Bottom` را تنظیم کنید تا ارتفاع Search widget تعیین شود.

### derived

- صفحه ارتفاع را از طریق Padding کنترل می‌کند، نه از طریق گزینه‌ای به نام Height.

## 11. Search Results Archive

### documented

`Search Results Page` یک `Archive` است و نتایج را در `Archive template` نمایش می‌دهد.

مراحل رسمی ساخت/ویرایش:

1. به `WP Admin` بروید.
2. به `Templates > Theme Builder` بروید.
3. در پنل روی `Search Results` کلیک کنید.
4. اگر Search Results template از قبل وجود دارد، می‌توانید همان template را ویرایش کنید.
5. برای ساخت template جدید، در بالا سمت راست روی `Add New` کلیک کنید.
6. `Template Library` باز می‌شود.
7. برای ساخت Search Results archive بر اساس template، یک template انتخاب کنید و `Insert` را بزنید.
8. برای ساخت archive طراحی‌شده با AI بر اساس یک طراحی موجود، روی `Generate Variations` کلیک کنید.
9. برای ساخت Search Results archive از صفر، روی `X` گوشه راست کلیک کنید و Template Library را ببندید.
10. بعد از انتخاب مسیر ساخت، Elementor Editor باز می‌شود.
11. صفحه را در Elementor Editor ویرایش کنید.
12. برای preview این Archive به‌عنوان Search Results page، روی `Settings icon` در top bar کلیک کنید.
13. در پنل، `Preview Settings` را باز کنید.
14. در `Search Term`، واژه‌ای وارد کنید که می‌دانید دست‌کم در یک post سایت استفاده شده و روی `Apply & Preview` کلیک کنید.
15. برای دیدن حالت بدون نتیجه، search termی وارد کنید که می‌دانید در سایت استفاده نشده و روی `Apply and Preview` کلیک کنید.
16. برای ذخیره template، روی `Publish` در top bar کلیک کنید.
17. مطمئن شوید شرط روی `Include` و `Search Results` تنظیم شده است.
18. پایین سمت چپ، روی `Save & Close` کلیک کنید.
19. صفحه Search Results سفارشی شده است.

## 12. Display Conditions

### documented

در صفحه Search Results Archive، پس از Publish باید condition روی `Include` و `Search Results` تنظیم شود و سپس `Save & Close` انجام شود.

### insufficient_evidence

- صفحه درباره شرایط چندگانه، exclude condition، اولویت templateها، conflict با theme یا fallback theme توضیح نمی‌دهد.

## 13. Empty / No-results states

### documented

صفحه Search Results Archive می‌گوید برای دیدن ظاهر صفحه وقتی نتیجه‌ای وجود ندارد، در Preview Settings یک search term وارد کنید که می‌دانید در سایت استفاده نشده و سپس `Apply and Preview` را بزنید.

### insufficient_evidence

- صفحه گزینه طراحی اختصاصی No Results، پیام پیش‌فرض، یا رفتار runtime در نبود نتیجه را توضیح نمی‌دهد.

## 14. URL/AJAX، accessibility و keyboard/focus

### insufficient_evidence

- `URL` یا search query parameter behavior در این دو صفحه توضیح فنی ندارد.
- `AJAX behavior` برای Live Results یا Pagination صریحاً توضیح داده نشده است.
- `accessibility`، `ARIA`، screen reader behavior، keyboard navigation و focus order به‌صورت فنی توضیح داده نشده‌اند.
- تنها شواهد مرتبط با keyboard این است که Trigger می‌تواند `Enter key` باشد و Style tab حالت `Focus` برای Search Field دارد؛ این‌ها برای نتیجه‌گیری کامل accessibility کافی نیستند.

## 15. Dynamic content و ارتباط با Loop Grid/Loop Item

### documented

- Live Results نیازمند `Loop Item` است.
- صفحه Search widget برای اطلاعات بیشتر درباره Loop Items به `Loop Grid widget` ارجاع می‌دهد.
- Query بخش Search widget اصطلاح `Loop Grid` را در توضیح Include/Exclude به‌کار می‌برد.

### derived

- Search widget در حالت Live Results از Loop Item برای قالب‌بندی هر نتیجه استفاده می‌کند.
- Query controls مشابه منطق Query خانواده Loop هستند، اما این سند بدون بررسی صفحه فرعی Loop Grid، رفتار دقیق آن را فراتر از متن Search widget نسبت نمی‌دهد.

### insufficient_evidence

- صفحه درباره Loop Carousel در Search Results Archive فقط در درخواست پژوهش مطرح شده بود؛ در متن رسمی این دو صفحه شاهد صریحی برای استفاده از Loop Carousel در Search Results Archive پیدا نشد.
- صفحه درباره dynamic tags یا dynamic fields در قالب Loop Item جزئیات نمی‌دهد.

## 16. تصاویر رسمی و شواهد تصویری

در متن رسمی، تصاویر متعددی با label عمومی `Image` آمده‌اند. هنگام تلاش برای بازکردن مستقیم چند نمونه تصویر، ابزار با `Cache miss` مواجه شد؛ بنابراین این سند از تصاویر، فقط جایگاه و URL استخراج‌شده را ثبت می‌کند و تحلیل تصویری انجام نمی‌دهد.

### نمونه URLهای تصویری ثبت‌شده

| منبع | جایگاه | URL/نام فایل استخراج‌شده | وضعیت |
|---|---|---|---|
| Search widget | Add the widget | `https://elementor.com/help/wp-content/uploads/2026/04/The-widget-icon.png` | observed_url_only_cache_miss |
| Search widget | Content tab / Search Field | `https://elementor.com/help/wp-content/uploads/2024/07/Content-Search-Field.webp` | observed_url_only_cache_miss |
| Search Results Archive | Step 1 | `https://elementor.com/help/wp-content/uploads/2023/08/1-Go-to-templates-theme-builder-1.png` | observed_url_only_cache_miss |

## 17. محدودیت‌های مستند

### documented

- Search widget گزینه full screen مستقیم ندارد؛ متن رسمی می‌گوید می‌توان full screen search را با Off Canvas widget ساخت و به ویدئو ارجاع می‌دهد.
- برای Live Results باید Loop Item وجود داشته باشد.
- برای استفاده از Search widget باید Search Results template وجود داشته باشد.

### insufficient_evidence

- محدودیت تعداد نتایج، محدودیت Post Type، سازگاری WooCommerce، سازگاری با multilingual، caching، indexing، و behavior در سایت‌های بزرگ در این دو صفحه توضیح داده نشده است.

## 18. مثال رسمی بازسازی‌شده

### documented

سناریوی رسمی: Jan در حال ساخت سایت فروشگاه جواهرات است و می‌خواهد مشتریان راحت‌تر آیتم‌های فروشگاه را جستجو کنند؛ بنابراین search bar را به Header اضافه می‌کند.

در مثال Live Results:

1. Search widget در Header قرار می‌گیرد.
2. برای نمایش immediate results، یک Loop Item ساخته می‌شود.
3. `Live Results` روی `Show` قرار می‌گیرد.
4. `Choose a template` ظاهر می‌شود.
5. قالب `Search Loop Item` انتخاب می‌شود.
6. تعداد Columns برای PC روی `3` و برای Mobile روی `1` تنظیم می‌شود.

## 19. چک‌لیست اجرایی بر اساس شواهد همین دو صفحه

1. مطمئن شوید Search Results template دارید یا آن را از Theme Builder بسازید.
2. اگر Live Results می‌خواهید، یک Loop Item بسازید یا انتخاب کنید.
3. Search widget را به Header یا محل مورد نظر اضافه کنید.
4. در بخش Results، `Live Results` را در صورت نیاز روی `Show` بگذارید.
5. در `Choose a template`، Loop Item مرتبط را انتخاب کنید.
6. در Query، Source و Include/Exclude و Order و Posts Per Page را فقط بر اساس نیاز محتوایی تنظیم کنید.
7. در Pagination، Type و Page Limit و labels را تنظیم کنید.
8. برای responsive، حداقل Columns را برای Desktop و Mobile بررسی کنید.
9. در Style tab، Search Field، Clear، Submit Button و Results را مطابق طراحی تنظیم کنید.
10. Search Results Archive را با Preview Settings و Search Term تست کنید.
11. حالت no-results را با یک term ناموجود پیش‌نمایش کنید.
12. پس از Publish، condition را روی `Include` و `Search Results` بگذارید و Save & Close کنید.

## 20. شکاف‌های شواهد برای تکمیل آینده

- exact Pro prerequisite / plan requirement
- default values for all controls
- complete Submit Button style controls
- complete Results style controls
- Additional Settings details
- URL query parameter name and behavior
- AJAX/live results transport details
- empty/no-results runtime rendering
- accessibility and ARIA behavior
- keyboard navigation and focus order
- performance/caching/indexing behavior
- multilingual/search plugin compatibility
- visual confirmation of all official screenshots
- Loop Carousel usage in Search Results Archive
