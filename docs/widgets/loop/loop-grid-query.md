---
id: elementor.help.loop-grid-query
title: "Build a query with the Loop Grid — جزوه جامع فارسی"
source_url: "https://elementor.com/help/create-a-query-in-a-loop-grid/"
canonical_url: "https://elementor.com/help/building-query-loop-grid/"
source_type: official_help
version_scope: "rolling_documentation; exact_elementor_core_and_pro_versions_not_stated"
last_updated: "2026-06-19"
researched_at: "2026-06-22T12:02:45+03:00"
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-007
product_scope:
  - Elementor
  - Loop Grid widget
  - Query panel
source_images:
  - "https://elementor.com/help/wp-content/uploads/2022/01/Select-loop-grid-from-structure.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Select-the-Query-menu.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Leave-as-posts.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Leave-as-include.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Category-and-Tag.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Category-and-Tag-1.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Filtered-posts.png"
---

# Build a query with the Loop Grid — جزوه جامع فارسی

> **دامنه این جزوه:** فقط متن و تصاویر تعبیه‌شده در مقاله رسمی Elementor با عنوان فعلی `Build a query with the loop grid`. محتوای مقاله‌های مجاور مانند `Customize which items appearing your loop`، `Create queries`، `Loop Grid widget` و مستندات توسعه‌دهندگان، بدون بررسی مستقل به این صفحه نسبت داده نشده است.

## 1. مشخصات منبع و وضعیت URL

| فیلد | مقدار |
|---|---|
| عنوان فعلی مقاله | `Build a query with the loop grid` |
| ناشر | Elementor Knowledge Hub |
| URL درخواست‌شده | <https://elementor.com/help/create-a-query-in-a-loop-grid/> |
| URL فعلی مقاله در ناوبری رسمی | <https://elementor.com/help/building-query-loop-grid/> |
| آخرین به‌روزرسانی اعلام‌شده | `June 19, 2026` |
| تاریخ پژوهش | `2026-06-22` |
| نسخه دقیق Elementor Core | اعلام نشده |
| نسخه دقیق Elementor Pro | اعلام نشده |
| وضعیت پوشش | `completed_with_gaps` |

**[observed]** URL داده‌شده در مأموریت با Slug فعلی مقاله یکسان نیست. مقاله از فهرست رسمی Widgets در Help Center با عنوان `Build a query with the loop grid` و Slug `building-query-loop-grid` باز شد.

**[insufficient_evidence]** صفحه توضیح نمی‌دهد آیا URL قدیمی Redirect دائمی دارد، چه زمانی Slug تغییر کرده یا آیا محتوای نسخه پیشین دقیقاً یکسان بوده است.

## 2. قرارداد شواهد

- **documented:** مطلبی که در متن رسمی مقاله صریحاً نوشته شده است.
- **observed:** موردی که مستقیماً در Screenshot رسمی همان مقاله دیده شده، ولی متن مقاله آن را کامل شرح نداده است.
- **derived:** برداشت محدود از شواهد موجود؛ قرارداد فنی، API یا رفتار تضمین‌شده محسوب نمی‌شود.
- **insufficient_evidence:** صفحه برای نتیجه‌گیری معتبر درباره آن مورد شواهد کافی ندارد.

## 3. هدف Query در Loop Grid

**[documented]** Query در Loop Grid برای انتخاب دقیق محتوایی استفاده می‌شود که باید داخل Loop نمایش داده شود. مقاله این قابلیت را در کنار گزینه‌های طراحی، عامل انعطاف‌پذیری بالای Loop Grid معرفی می‌کند.

**[documented]** مقاله یک آموزش نمونه ارائه می‌دهد و ادعا نمی‌کند که مرجع کامل همه Sourceها، Operatorها و کنترل‌های Query است.

### سناریوی رسمی مثال

**[documented]** مثال روی یک وبلاگ ساخته‌شده با Website Kit با نام `The Adventurers` اجرا می‌شود. پیش‌نیازهای موجود در سناریو عبارت‌اند از:

1. برای نوشته‌ها Category و Tag ساخته شده است.
2. Loop قبلاً ساخته و ذخیره شده است.
3. کاربر به ویرایش صفحه برگشته است.
4. هدف این است که فقط نوشته‌های مرتبط با سفر اقتصادی نمایش داده شوند.

**[derived]** این چهار مورد پیش‌نیاز عمومی همه Queryها نیستند؛ فقط وضعیت Fixture مثال رسمی‌اند.

## 4. نقشه Workflow رسمی

| مرحله | عمل رسمی | وضعیت شواهد |
|---:|---|---|
| 1 | انتخاب `Loop Grid`، ترجیحاً از `Structure window` | documented + observed |
| 2 | بازکردن منوی `Query` | documented + observed |
| 3 | نگه‌داشتن `Source` روی مقدار پیش‌فرض `Posts` | documented + observed |
| 4 | نگه‌داشتن حالت روی `Include` | documented + observed |
| 5 | انتخاب `Term` یا `Author` در `Include By` | documented |
| 6 | انتخاب `Term` برای فیلتر بر اساس Category و Tag | documented + observed |
| 7 | تعریف شرایط `Travel` و `Budget` | documented |
| 8 | تایپ `Travel` در Text box مربوط به Term و انتخاب از Dropdown پیشنهادی | documented |
| 9 | تایپ `Budget` و انتخاب از Dropdown پیشنهادی | documented |
| 10 | نمایش فقط نوشته‌های منطبق با شرایط | documented |

## 5. دسترسی به Query panel

### 5.1. Structure window — پنجره ساختار

**[documented]** برای انتخاب Loop Grid، مقاله استفاده از `Structure window` را معمولاً آسان‌ترین راه معرفی می‌کند.

![Select Loop Grid from Structure](https://elementor.com/help/wp-content/uploads/2022/01/Select-loop-grid-from-structure.png)

**[observed]** در تصویر، یک `Container` باز است و آیتم `Loop Grid` درون آن انتخاب شده است.

**[insufficient_evidence]** صفحه درباره میانبر صفحه‌کلید، مسیر بازکردن Structure window یا تفاوت نام این پنجره بین نسخه‌ها توضیح نمی‌دهد.

### 5.2. Query menu — منوی کوئری

**[documented]** پس از انتخاب Loop Grid باید بخش `Query` باز شود.

![Select the Query menu](https://elementor.com/help/wp-content/uploads/2022/01/Select-the-Query-menu.png)

**[observed]** Screenshot پنل `Edit Loop Grid` را در Tab `Content` نشان می‌دهد. Accordionهای `Layout`، `Query` و `Pagination` قابل مشاهده‌اند و `Query` باز است.

## 6. فهرست کنترل‌های Query بر اساس متن و تصاویر همین صفحه

| کنترل انگلیسی | ترجمه فارسی | وضعیت | مقدار/گزینه دیده‌شده | سطح پوشش مقاله |
|---|---|---|---|---|
| `Source` | منبع | documented + observed | `Posts` | فقط Posts توضیح داده شده |
| `Include / Exclude` | شامل / حذف | Include: documented؛ Exclude: observed | `Include` انتخاب‌شده | Exclude توضیح عملی ندارد |
| `Include By` | شامل‌کردن بر اساس | documented + observed | `Term` و `Author` | هر دو نام‌برده شده‌اند |
| `Author` | نویسنده | documented | Text box وابسته | روش تایپ نام توضیح داده شده |
| `Term` | اصطلاح/ترم | documented + observed | Category، Tag و ویژگی‌های CPT | Autocomplete توضیح داده شده |
| `Date` | تاریخ | observed | `All` | گزینه‌ها و منطق توضیح داده نشده |
| `Order By` | مرتب‌سازی بر اساس | observed | `Date` | گزینه‌ها توضیح داده نشده |
| `Order` | جهت ترتیب | observed | `DESC` | گزینه‌ها توضیح داده نشده |
| `Ignore Sticky Posts` | نادیده‌گرفتن نوشته‌های سنجاق‌شده | observed | `Yes` | فقط Label و Helper دیده می‌شود |
| `Query ID` | شناسه Query | observed | خالی | Helper مربوط به Server-side filtering دیده می‌شود |
| `Offset` | جابه‌جایی شروع نتایج | insufficient_evidence | دیده نشده | در متن و تصاویر صفحه نیست |
| `Avoid Duplicates` | جلوگیری از موارد تکراری | insufficient_evidence | دیده نشده | در متن و تصاویر صفحه نیست |
| `Current Query` | Query جاری | insufficient_evidence | دیده نشده | Source dropdown باز نشده است |
| `Related` | مرتبط | insufficient_evidence | دیده نشده | Source dropdown باز نشده است |

## 7. Source — منبع Query

![Leave Source as Posts](https://elementor.com/help/wp-content/uploads/2022/01/Leave-as-posts.png)

### 7.1. Posts — نوشته‌ها

**[documented]** برای ساخت Loop مربوط به نوشته‌ها، `Source` باید روی مقدار پیش‌فرض `Posts` باقی بماند.

**[observed]** مقدار `Posts` در Dropdown دیده می‌شود؛ Dropdown در تصاویر باز نشده است.

### 7.2. سایر Source options

**[insufficient_evidence]** صفحه هیچ فهرست متنی یا تصویری از تمام گزینه‌های Source ارائه نمی‌کند. بنابراین موارد زیر را نمی‌توان بر اساس این منبع تأیید کرد:

- `Current Query`
- `Related`
- Products یا سایر Post Typeها به‌عنوان Source مستقل
- Manual Selection
- هر Source سفارشی یا افزونه‌ای

**[derived]** وجود فلش Dropdown نشان می‌دهد `Source` احتمالاً بیش از یک مقدار دارد، اما تعداد، نام و شرط نمایش آن‌ها از این تصویر قابل استنتاج نیست.

## 8. Include / Exclude — شامل‌کردن یا حذف‌کردن

![Leave query as Include](https://elementor.com/help/wp-content/uploads/2022/01/Leave-as-include.png)

### 8.1. Include — شامل

**[documented]** برای سناریوی مقاله، Toggle باید روی `Include` باقی بماند تا نوشته‌های منطبق با شروط انتخاب شوند.

### 8.2. Exclude — حذف

**[observed]** گزینه `Exclude` در Segmented control کنار Include دیده می‌شود.

**[insufficient_evidence]** مقاله:

- Exclude را فعال نمی‌کند.
- رفتار آن را توضیح نمی‌دهد.
- مشخص نمی‌کند کنترل‌های وابسته بعد از انتخاب Exclude چه نامی می‌گیرند.
- درباره اولویت Include و Exclude، منطق تضاد یا ترکیب شروط توضیحی ندارد.

**[derived]** ترجمه «حذف» فقط بر مبنای Label رابط است؛ جزئیات Semantics باید از منبع مستقل بررسی شود.

## 9. Include By — شامل‌کردن بر اساس

**[documented]** با کلیک روی Text box مربوط به `Include By` دو انتخاب ارائه می‌شود:

| گزینه | رفتار مستند |
|---|---|
| `Term` | Text box دیگری باز می‌کند تا Category، Tag یا در صورت وجود Custom Post Type، سایر Propertyها انتخاب شوند |
| `Author` | Text box دیگری باز می‌کند تا نام نویسنده تایپ و انتخاب شود |

**[documented]** Caption رسمی تصویر می‌گوید Include By برای تعیین فیلتر بر اساس Term، Author یا هر دو استفاده می‌شود.

**[insufficient_evidence]** متن مراحل جمله‌ای دارد که عبارت «you can also select both» را پس از Category و Tag می‌آورد. Caption تصویر نیز «term, author or both» می‌گوید. صفحه منطق دقیق ترکیب را مشخص نمی‌کند؛ بنابراین روشن نیست «both» در همه Contextها دقیقاً به کدام جفت و با چه Operator منطقی اشاره دارد.

## 10. Author — نویسنده

**[documented]** انتخاب `Author` یک Text box باز می‌کند و کاربر می‌تواند نام نویسنده مورد نظر را تایپ کند.

**[insufficient_evidence]** صفحه مشخص نمی‌کند:

- پیشنهادها پس از چند نویسه ظاهر می‌شوند.
- انتخاب چند نویسنده ممکن است یا نه.
- منطق چند نویسنده `OR` است یا `AND`.
- جست‌وجو بر اساس Display Name، Username، ID یا فیلد دیگری انجام می‌شود.
- نویسندگان بدون نوشته نمایش داده می‌شوند یا نه.

## 11. Term — ترم، Category، Tag و Propertyهای CPT

![Choose Term in Include By](https://elementor.com/help/wp-content/uploads/2022/01/Category-and-Tag.png)

**[documented]** `Term` می‌تواند برای انتخاب موارد زیر استفاده شود:

- Category
- Tag
- در صورت وجود Custom Post Type، Propertyهای دیگر

**[observed]** در Screenshot، Token با نام `Term` داخل `Include By` دیده می‌شود و یک Text box وابسته با Label `Term` ظاهر شده است. Placeholder قابل مشاهده می‌گوید حداقل یک یا چند نویسه وارد شود.

### 11.1. رفتار جست‌وجوی Term

**[documented]** هنگام تایپ در Text box، یک Dropdown از Termهای منطبق با ورودی ظاهر می‌شود.

**[documented]** در مثال:

1. `Travel` تایپ و از نتایج انتخاب می‌شود.
2. `Budget` تایپ و از نتایج انتخاب می‌شود.
3. هدف، نوشته‌هایی است که Category آن‌ها Travel و Tag آن‌ها Budget بوده است.

### 11.2. منطق ترکیب Travel و Budget

**[documented]** نتیجه نهایی فقط نوشته‌های منطبق با شرایط مثال را نشان می‌دهد.

**[derived]** متن مثال از عبارت «marked with the category Travel and tagged as Budget» استفاده می‌کند و نتیجه را منطبق با Conditions می‌داند؛ این برای همان مثال نشان‌دهنده تقاطع عملی دو شرط است.

**[insufficient_evidence]** صفحه قرارداد عمومی `AND/OR` برای موارد زیر ارائه نمی‌کند:

- چند Term در یک Taxonomy
- Termهای Taxonomyهای مختلف
- ترکیب Term و Author
- ترکیب Include و Exclude
- Custom Taxonomyها

## 12. Date — تاریخ

**[observed]** کنترل `Date` در تصاویر Query panel دیده می‌شود و مقدار نمایش‌داده‌شده `All` است.

**[insufficient_evidence]** مقاله هیچ توضیح متنی درباره Date ندارد و Dropdown باز نشده است. بنابراین موارد زیر نامشخص‌اند:

- فهرست بازه‌های زمانی
- امکان Custom date range
- مبنای Publish date در برابر Modified date
- Timezone
- Include/Exclude زمانی
- شرط نمایش کنترل

## 13. Order By — مرتب‌سازی بر اساس

**[observed]** کنترل `Order By` دیده می‌شود و مقدار آن در Screenshot برابر `Date` است.

**[insufficient_evidence]** صفحه فهرست گزینه‌ها، Default قراردادی، رفتار Random، Menu Order، Title، ID یا Meta fieldها را توضیح نمی‌دهد.

## 14. Order — جهت ترتیب

**[observed]** کنترل `Order` دیده می‌شود و مقدار آن `DESC` است.

**[derived]** بر اساس اصطلاح رایج رابط، DESC به ترتیب نزولی اشاره دارد؛ اما مقاله تعریف مستقلی از آن ارائه نمی‌کند.

**[insufficient_evidence]** گزینه `ASC` در Dropdown بازشده دیده نشده و اثر Order برای هر نوع Order By توضیح داده نشده است.

## 15. Ignore Sticky Posts — نادیده‌گرفتن نوشته‌های سنجاق‌شده

**[observed]** Toggle با نام `Ignore Sticky Posts` روی `Yes` دیده می‌شود.

**[observed]** متن کمکی تصویر می‌گوید ترتیب Sticky posts فقط در Frontend قابل مشاهده است.

**[insufficient_evidence]** مقاله توضیح نمی‌دهد:

- مقدار Default رسمی چیست.
- Yes دقیقاً Sticky posts را حذف می‌کند یا فقط اولویت Sticky را نادیده می‌گیرد.
- این کنترل برای Sourceهای غیر Posts چه وضعیتی دارد.
- رفتار Preview با Frontend چه تفاوت دقیقی دارد.

## 16. Query ID — شناسه Query

**[observed]** یک Text field با Label `Query ID` در پایین Query panel دیده می‌شود.

**[observed]** Helper text آن Query ID را یک شناسه یکتای سفارشی برای امکان `server side filtering` معرفی می‌کند.

**[insufficient_evidence]** این صفحه هیچ‌کدام از موارد زیر را ارائه نمی‌کند:

- قواعد نام‌گذاری
- Scope یکتایی در Page، Document یا Site
- Hook یا API مرتبط
- نمونه PHP/JavaScript
- اثر روی Cache یا AJAX
- رفتار خطا برای ID تکراری

## 17. Offset — جابه‌جایی نقطه شروع

**[insufficient_evidence]** عبارت و کنترل `Offset` در متن مقاله و پنج Screenshot قابل مشاهده Query panel وجود ندارد. دو تصویر پایانی مقاله نیز فقط برای انتخاب Category/Tag و نتیجه فیلترشده Caption شده‌اند؛ شواهدی از Offset ارائه نمی‌کنند.

نتیجه: وجود، مقدار پیش‌فرض، واحد، رفتار با Pagination و شرط نمایش Offset از این منبع قابل ثبت نیست.

## 18. Avoid Duplicates — جلوگیری از تکرار

**[insufficient_evidence]** عبارت `Avoid Duplicates` در متن رسمی مقاله یافت نشد و در تصاویر قابل مشاهده نیز کنترل آن دیده نشد.

صفحه درباره موارد زیر ساکت است:

- جلوگیری از تکرار بین چند Loop Grid
- ارتباط با Queryهای قبلی صفحه
- Scope محاسبه Duplicate
- اثر Pagination یا AJAX

## 19. Current Query — Query جاری

**[insufficient_evidence]** `Current Query` در متن یا Screenshot بازشده Source وجود ندارد. از آنجا که Dropdown `Source` باز نشده، نمی‌توان وجود یا رفتار این گزینه را بر اساس همین صفحه تأیید کرد.

## 20. Related — محتوای مرتبط

**[insufficient_evidence]** `Related` در متن یا Screenshotها نمایش داده نشده است. صفحه معیار ارتباط بر اساس Term، Author، Manual selection یا Fallback را توضیح نمی‌دهد.

## 21. تصاویر رسمی و سطح بررسی

| تصویر | کاربرد | وضعیت بررسی |
|---|---|---|
| `Select-loop-grid-from-structure.png` | انتخاب Loop Grid در Structure | بصری بررسی شد |
| `Select-the-Query-menu.png` | بازکردن Query و نمای کامل پنل | بصری بررسی شد |
| `Leave-as-posts.png` | Source = Posts و کنترل‌های Query | بصری بررسی شد |
| `Leave-as-include.png` | Include انتخاب‌شده | بصری بررسی شد |
| `Category-and-Tag.png` | انتخاب Term و ظاهرشدن Text box وابسته | بصری بررسی شد |
| `Category-and-Tag-1.png` | انتخاب Travel و Budget طبق Caption/مرحله | URL و Caption رسمی استخراج شد؛ Fetch تصویری ابزار ناموفق بود |
| `Filtered-posts.png` | نتیجه نوشته‌های منطبق طبق Caption | URL و Caption رسمی استخراج شد؛ Fetch تصویری ابزار ناموفق بود |

### محدودیت استناد تصویری

**[insufficient_evidence]** چون دو تصویر آخر توسط ابزار به‌صورت بصری Fetch نشدند، جزئیات UI آن‌ها فراتر از Caption و متن مراحل ثبت نشده است.

## 22. شروط نمایش مستند یا قابل مشاهده

| شرط | نتیجه | نوع شاهد |
|---|---|---|
| انتخاب Loop Grid | دسترسی به پنل تنظیمات Widget | documented |
| بازکردن `Query` | نمایش کنترل‌های Query | documented + observed |
| `Source = Posts` | سناریوی Query نوشته‌ها | documented |
| `Include` فعال | مسیر شامل‌کردن نوشته‌ها | documented |
| انتخاب `Author` در Include By | ظاهرشدن Text box نام نویسنده | documented |
| انتخاب `Term` در Include By | ظاهرشدن Text box ترم | documented + observed |
| شروع تایپ در Term field | ظاهرشدن Dropdown از Termهای منطبق | documented |

**[insufficient_evidence]** هیچ شرط نمایشی برای Date، Order By، Order، Ignore Sticky Posts، Query ID، Offset، Avoid Duplicates، Current Query یا Related به‌صورت صریح توضیح داده نشده است.

## 23. خروجی مثال رسمی

**[documented]** پس از تعریف Category برابر Travel و Tag برابر Budget، Loop فقط نوشته‌هایی را نشان می‌دهد که شرایط تعریف‌شده را برآورده می‌کنند.

![Filtered posts](https://elementor.com/help/wp-content/uploads/2022/01/Filtered-posts.png)

**[insufficient_evidence]** مقاله تعداد دقیق نتایج، ترتیب آن‌ها، Query SQL، رفتار بدون نتیجه و اثر Pagination را اعلام نمی‌کند.

## 24. مواردی که این صفحه پوشش نمی‌دهد

این موارد نباید به‌عنوان حقیقت مستند این مقاله ثبت شوند:

- همه Source options
- رفتار کامل Exclude
- تمام Date presets
- فهرست کامل Order By
- Defaultهای قراردادی کنترل‌ها
- Offset
- Avoid Duplicates
- Current Query
- Related
- Query ID API و Hookها
- AJAX، URL، History API و Pagination interaction
- Accessibility و Keyboard navigation کنترل‌های Autocomplete
- منطق عمومی AND/OR
- رفتار Taxonomyهای سلسله‌مراتبی
- Pro prerequisite
- حداقل نسخه Elementor Core/Pro
- تغییرات نسخه‌به‌نسخه

## 25. پیش‌نیازها و نسخه

**[documented]** صفحه برای انجام مثال وجود Loop Grid، نوشته‌های دارای Category و Tag و Loop ذخیره‌شده را فرض می‌کند.

**[insufficient_evidence]** صفحه صریحاً نمی‌گوید:

- Elementor Pro لازم است یا نه.
- کدام Plan لازم است.
- حداقل نسخه Core/Pro چیست.
- Query feature در چه نسخه‌ای معرفی یا تغییر کرده است.

## 26. خطاها، ابهام‌ها و ریسک برداشت نادرست

1. **تغییر URL:** URL مأموریت با URL فعلی ناوبری رسمی متفاوت است.
2. **عنوان محدودتر از درخواست:** مقاله یک Walkthrough ساده است، نه مرجع کامل تمام Query controls.
3. **ابهام “both”:** متن و Caption درباره انتخاب هر دو، منطق ترکیب را تعریف نمی‌کنند.
4. **Screenshot قدیمی‌تر از تاریخ مقاله:** مسیر تصاویر `2022/01` است، در حالی که مقاله در 2026 به‌روزرسانی شده؛ صفحه اعلام نمی‌کند UI تصاویر دقیقاً متعلق به کدام نسخه است.
5. **Default در برابر وضعیت Screenshot:** فقط `Posts` به‌صراحت Default نامیده شده است. مقادیر `All`، `Date`، `DESC` و `Yes` صرفاً در Screenshot دیده می‌شوند و Default رسمی تلقی نمی‌شوند.
6. **کنترل‌های مشاهده‌شده اما توضیح‌نداده‌شده:** Date، Order By، Order، Ignore Sticky Posts و Query ID نباید با جزئیات منابع دیگر به این مقاله نسبت داده شوند.

## 27. جمع‌بندی شواهد

### Documented

- هدف Query: انتخاب دقیق محتوای Loop.
- مسیر انتخاب Loop Grid و بازکردن Query.
- Source پیش‌فرض Posts در مثال.
- استفاده از Include.
- گزینه‌های Term و Author در Include By.
- ایجاد Text box وابسته برای Author یا Term.
- پشتیبانی Term از Category، Tag و Propertyهای Custom Post Type.
- پیشنهاد Termهای منطبق هنگام تایپ.
- مثال Travel + Budget و نمایش نتایج منطبق.
- تاریخ آخرین به‌روزرسانی: 19 ژوئن 2026.

### Observed

- Exclude در کنار Include.
- Date = All.
- Order By = Date.
- Order = DESC.
- Ignore Sticky Posts = Yes و Helper مربوط به Frontend.
- Query ID و Helper مربوط به Server-side filtering.
- Accordion Pagination زیر Query.
- Token انتخاب‌شده Term و Text box وابسته.

### Derived

- تصویر Dropdown بسته نشان می‌دهد Source یک Select control است، اما گزینه‌های آن مشخص نیست.
- مثال Travel و Budget در همان سناریو به تقاطع شروط منجر شده است، ولی قانون عمومی Operatorها ثابت نشده است.
- اختلاف Slug احتمالاً ناشی از تغییر نام/ساختار مقاله است، اما نوع Redirect و تاریخ تغییر معلوم نیست.

### Insufficient Evidence

- همه Source options به‌جز Posts.
- جزئیات Exclude.
- گزینه‌های Date، Order By و Order.
- Offset، Avoid Duplicates، Current Query و Related.
- Defaultهای رسمی به‌جز Posts.
- منطق AND/OR عمومی.
- Query ID API.
- نسخه دقیق و Pro prerequisite.
- Accessibility، AJAX، URL و Pagination interaction.

## 28. ارجاعات داخلی پیشنهادی

- `docs/widgets/loop/loop-grid.md` — مرجع تنظیمات کلی Loop Grid و تصویر Query panel.
- `docs/concepts/queries/create-queries.md` — پس از تکمیل KB-008 برای پوشش Queryهای عمومی.
- `docs/widgets/loop/pagination.md` — پس از تکمیل KB-009 برای رفتار Pagination.

## 29. نتیجه مرحله

وضعیت این جزوه `completed_with_gaps` است؛ زیرا Workflow نمونه و کنترل‌های قابل مشاهده صفحه با دقت ثبت شده‌اند، اما منبع رسمی مورد بررسی مرجع جامع همه Query options نیست و چند کنترل خواسته‌شده اصلاً در متن یا تصاویر آن حضور ندارند.
