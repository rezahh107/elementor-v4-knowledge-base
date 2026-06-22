---
id: elementor.help.loop-grid
title: "Loop Grid widget — جزوه جامع تنظیمات"
source_url: "https://elementor.com/help/loop-grid/"
source_type: official_help
version_scope: "rolling_documentation; exact_elementor_plugin_version_not_stated"
last_updated: "2026-06-19"
researched_at: "2026-06-22T11:31:27+03:30"
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-006
product_scope:
  - Elementor
  - Loop Grid widget
source_images:
  - "https://elementor.com/help/wp-content/uploads/2022/01/Content-Layout.png"
  - "https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Query.jpg"
  - "https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Pagination.jpg"
  - "https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Additional-Options.jpg"
  - "https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Pagination.jpg"
  - "https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Layout.jpg"
  - "https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Message-Not-found.jpg"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Advanced-tab.png"
---

# Loop Grid widget — جزوه جامع فارسی

> **دامنه این جزوه:** فقط محتوای صفحه رسمی «Loop Grid widget» و تصاویر تعبیه‌شده در همان صفحه. صفحات فرعی لینک‌شده، مانند Build a Loop Grid، Build a query، Paginate your loop و Add an alternate template، در این مرحله خوانده نشده‌اند و محتوای آن‌ها به این منبع نسبت داده نمی‌شود.

## 1. مشخصات منبع و وضعیت شواهد

| فیلد | مقدار |
|---|---|
| عنوان رسمی | `Loop Grid widget` |
| ناشر | Elementor Knowledge Hub |
| URL | <https://elementor.com/help/loop-grid/> |
| آخرین به‌روزرسانی اعلام‌شده در صفحه | `June 19, 2026` |
| تاریخ پژوهش | `2026-06-22` |
| نسخه دقیق افزونه | در صفحه اعلام نشده |
| وضعیت پوشش | `completed_with_gaps` |
| علت وجود شکاف | نبود نسخه دقیق، نبود تصریح Elementor Pro، نبود Skin options، نبود توضیح مستقل Dynamic Data و محدود بودن جزئیات Responsive controls |

### واژگان وضعیت شواهد

- **documented:** به‌صورت متنی و صریح در صفحه رسمی آمده است.
- **observed:** مستقیماً در تصویر رسمی همان صفحه دیده شده، اما متن صفحه آن را کامل توضیح نداده است.
- **derived:** برداشت محدود و منطقی از شواهد صفحه؛ حقیقت مستقل یا API contract محسوب نمی‌شود.
- **insufficient_evidence:** صفحه برای نتیجه‌گیری قابل اتکا اطلاعات کافی ندارد.

---

## 2. Loop Grid چیست؟

**[documented]** بسیاری از سایت‌ها صفحه‌هایی شامل فهرست نوشته‌ها دارند؛ این فهرست می‌تواند محصولات، خبرها یا پست‌های وبلاگ باشد. Loop Grid امکان سفارشی‌سازی ظاهر این فهرست‌ها را فراهم می‌کند تا طرحی متناسب با نیاز سایت ساخته شود.

### کاربردهای رسمی ذکرشده

**[documented]**

- ساخت صفحه‌های موضوعی برای نوشته‌های سفر در مناطق مختلف، با به‌روزرسانی خودکار هنگام انتشار نوشته جدید و قابلیت مرتب‌سازی.
- ساخت فهرست دستورهای آشپزی بر اساس سرآشپز یا ماده اصلی و به‌روزرسانی خودکار.
- نمایش خبرها بر اساس نوع، مانند Politics، Sports و Local.
- نمایش خطوط مختلف محصولات فروشگاه.
- نمایش انواع آثار در سایت Portfolio.

---

## 3. مدل کار Loop Grid

**[documented]** Loop Grid یک Widget است، اما روند آن با بسیاری از Widgetها تفاوت دارد:

1. Widget به Canvas اضافه می‌شود.
2. کاربر برای ساخت یا انتخاب یک Template هدایت می‌شود.
3. Template نمایش یکنواخت آیتم‌های مختلف را تعریف می‌کند.
4. خود Template در Canvas و با Widgetهای دیگر ویرایش می‌شود.
5. برای تنظیم Layout، Pagination و Content باید خود Loop Grid را در Canvas یا در `Structure window` انتخاب کرد تا Editing panel باز شود.

**[derived]** صفحه میان دو سطح طراحی تفکیک ایجاد می‌کند:

- **Template item design:** طراحی ظاهر یک آیتم تکرارشونده.
- **Loop Grid widget settings:** تعیین چیدمان، منبع داده، صفحه‌بندی و گزینه‌های کلی Grid.

این تفکیک از متن صفحه نتیجه می‌شود، اما صفحه آن را به‌عنوان اصطلاح رسمی دو‌سطحی نام‌گذاری نکرده است.

---

## 4. نقشه تب‌ها و بخش‌ها

| Tab | Section/Accordion | وضعیت شواهد |
|---|---|---|
| `Content` — محتوا | `Layout` — چیدمان | documented + observed |
| `Content` — محتوا | `Query` — کوئری | documented + observed |
| `Content` — محتوا | `Pagination` — صفحه‌بندی | documented + observed |
| `Content` — محتوا | `Additional Options` — گزینه‌های اضافی | عنوان documented؛ محتوای متناظر با `Nothing Found Message` documented |
| `Style` — استایل | `Pagination` — صفحه‌بندی | documented |
| `Style` — استایل | `Layout` — چیدمان | documented |
| `Style` — استایل | `Nothing Found Message` — پیام نبود نتیجه | documented |
| `Advanced` — پیشرفته | `Advanced` | فقط معرفی و ارجاع به صفحه دیگر |

**[insufficient_evidence]** صفحه هیچ بخشی با نام `Skin` یا `Skin options` نشان نمی‌دهد و عبارت Skin نیز در متن اصلی مقاله وجود ندارد.

---

# 5. Content tab — تب محتوا

## 5.1. Layout — چیدمان

تصویر رسمی:

![Content > Layout](https://elementor.com/help/wp-content/uploads/2022/01/Content-Layout.png)

منبع تصویر: [Elementor — Content-Layout.png](https://elementor.com/help/wp-content/uploads/2022/01/Content-Layout.png)

### 5.1.1. Choose template type — انتخاب نوع قالب

**[documented]** هر Loop Grid باید یک Template داشته باشد. گزینه‌های Dropdown طبق صفحه:

| مقدار انگلیسی | ترجمه و کاربرد مستند |
|---|---|
| `Posts` | نمایش نوشته‌های معمولی، برگه‌ها یا محصولات |
| `Post Taxonomy` | نمایش Taxonomyها/دسته‌های نوشته‌ها |
| `Products` | نمایش محصولات WooCommerce |
| `Product Taxonomy` | نمایش Taxonomyها/دسته‌های محصولات |

### هشدار تطابق نوع Template

**[documented]** Template باید از نوع درست ساخته شود. مثال رسمی: محصولات در Loop Grid با Template type برابر `Posts` نمایش داده نمی‌شوند.

**[derived]** نوع Template و نوع محتوای مورد انتظار باید با هم سازگار باشند؛ با این حال صفحه جدول کامل سازگاری همه نوع‌ها را ارائه نمی‌کند.

### 5.1.2. Choose a template — انتخاب قالب

**[documented]** از Dropdown برای انتخاب Template موجود استفاده می‌شود.

### 5.1.3. Edit template — ویرایش قالب

**[documented]** این دکمه دو عملکرد دارد:

- اگر Template انتخاب شده باشد، همان Template ویرایش می‌شود.
- اگر Template انتخاب نشده باشد، Template جدید ساخته می‌شود.

### 5.1.4. Columns — ستون‌ها

**[documented]** در Text box تعداد ستون‌های Loop Grid وارد می‌شود.

**[observed]** در تصویر رسمی کنار عنوان `Columns` یک نماد دستگاه/Responsive دیده می‌شود.

**[insufficient_evidence]** متن صفحه مشخص نمی‌کند:

- مقدار پیش‌فرض رسمی برای تمام نصب‌ها چیست؛ تصویر مقدار `3` را نشان می‌دهد، اما تصویر به‌تنهایی قرارداد Default محسوب نمی‌شود.
- Breakpointهای پشتیبانی‌شده کدام‌اند.
- نحوه ارث‌بری مقدار Columns بین Desktop، Tablet و Mobile چیست.

### 5.1.5. Items Per Page — تعداد آیتم در هر صفحه

**[documented]** در Text box تعداد آیتم‌هایی که در هر صفحه Loop Grid نمایش داده می‌شود وارد می‌گردد.

**[observed]** تصویر رسمی مقدار `6` را نمایش می‌دهد.

**[insufficient_evidence]** صفحه مقدار `6` را به‌صراحت Default اعلام نمی‌کند؛ بنابراین این مقدار فقط وضعیت Screenshot است.

### 5.1.6. Masonry — چیدمان ماسونری

**[documented]** با Toggle روی `On`، آیتم‌ها به‌صورت خودکار چیده می‌شوند. صفحه Masonry را یک سیستم Dynamic layout grid معرفی می‌کند که آیتم‌ها را برای تعادل بصری و Responsive بودن مرتب می‌کند.

**[insufficient_evidence]** صفحه الگوریتم، ترتیب DOM، نحوه محاسبه ارتفاع، اثر بر Accessibility یا رفتار هنگام بارگذاری تصویر را توضیح نمی‌دهد.

### 5.1.7. Equal height — ارتفاع برابر

**[documented]** با Toggle روی `On`، ردیف‌های Loop هم‌ارتفاع می‌شوند.

**نکته رسمی:** اگر Loop بیش از یک Parent container داشته باشد، فعال‌کردن Equal height باعث هم‌ارتفاع شدن تمام Parent containerها می‌شود. در یک Loop نمی‌توان بعضی Parent containerها را Equal height و بعضی را غیرهم‌ارتفاع نگه داشت.

### 5.1.8. Apply an alternate template — اعمال قالب جایگزین

**[documented]** با Toggle روی `On` می‌توان بخشی از Loop را با Template متفاوت نمایش داد. مثال رسمی: در Loop محصولات فروشگاه، هر آیتم سوم یک تبلیغ فروش ویژه باشد.

**[insufficient_evidence]** جزئیات زیر در همین صفحه نیامده و به مقاله فرعی واگذار شده است:

- انتخاب Alternate Template.
- تعیین موقعیت یا Pattern.
- تعداد ستون/ردیف Span.
- شرایط تکرار.
- تعامل با Pagination و Query.

---

## 5.2. Query — کوئری

تصویر رسمی:

![Content > Query](https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Query.jpg)

منبع تصویر: [Elementor — Content-tab-Query.jpg](https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Query.jpg)

**[documented]** Query تعیین می‌کند چه آیتم‌هایی در Loop ظاهر شوند. مثال رسمی: Query شامل Shirts، Loop را به Shirts محدود می‌کند.

### 5.2.1. Source — منبع

صفحه Sourceهای زیر را فهرست می‌کند:

| Source | توضیح |
|---|---|
| `Posts` | نوشته‌ها |
| `Pages` | برگه‌ها |
| `Landing pages` | لندینگ‌پیج‌ها |
| `Manually selected pages` | برگه‌های انتخاب‌شده به‌صورت دستی |
| `The Current Query` | استفاده در Template مشترک برای دسته‌ها یا Tagهای مختلف تا برای هر دسته/Tag Query جدا نوشته نشود |
| `Related items` | آیتم‌های مرتبط؛ سازوکار تعیین ارتباط در این صفحه شرح داده نشده است |

**[observed]** Screenshot رسمی Source را روی `Posts` نشان می‌دهد.

### 5.2.2. Include / Exclude — شامل‌کردن / حذف‌کردن

**[documented]**

- `Include`: ساخت Query برای تعریف آیتم‌هایی که باید داخل Loop باشند.
- `Exclude`: عنوان کنترل برای تعریف آیتم‌هایی که نباید داخل Loop باشند.

**ناهماهنگی متن منبع:** توضیح زیر `Exclude` در صفحه دوباره می‌گوید «Click include». این عبارت به‌احتمال زیاد خطای نگارشی/Copy-paste است؛ این جزوه آن را به‌عنوان رفتار فنی معتبر بازتفسیر نمی‌کند.

### 5.2.3. Include By / Exclude By — شامل/حذف بر اساس

**[documented]** از Text box برای واردکردن نوع نوشته‌هایی که باید Include یا Exclude شوند استفاده می‌شود.

**[insufficient_evidence]** صفحه گزینه‌های دقیق قابل انتخاب، منطق AND/OR، رفتار چند انتخاب و نوع Entityهای قابل جست‌وجو را فهرست نمی‌کند.

### 5.2.4. Date — تاریخ

**[documented]** Dropdown برای Include یا Exclude کردن آیتم‌ها بر اساس زمان ایجاد آن‌ها استفاده می‌شود.

**[observed]** Screenshot مقدار `All` را نمایش می‌دهد.

**[insufficient_evidence]** دامنه گزینه‌های Date و معنای دقیق هر بازه در صفحه فهرست نشده است.

### 5.2.5. Hide Empty — پنهان‌کردن موارد خالی

**[documented]** با Toggle روی `Yes`، Category، Tag و Typeهایی که هیچ Post یا Product ندارند پنهان می‌شوند.

**شرط نمایش مستند:** فقط برای Loop Gridهایی ظاهر می‌شود که Taxonomyها و Typeها را نمایش می‌دهند.

### 5.2.6. Filter by depth — فیلتر بر اساس عمق

**[documented]** با Toggle روی `Yes` می‌توان عمق نمایش در درخت Category/Type را تعیین کرد. پس از فعال‌سازی، یک Dropdown برای انتخاب عمق ظاهر می‌شود.

مثال رسمی:

```text
Mens clothing > Sportswear > Outdoors > Shirts
```

با Depth برابر `2`، فقط `Mens clothing` و `Sportswear` نمایش داده می‌شوند و `Outdoors` و `Shirts` نمایش داده نمی‌شوند.

**شرط نمایش مستند:** فقط برای Loop Gridهایی در دسترس است که Taxonomy چندسطحی را نمایش می‌دهند.

### 5.2.7. Order By — مرتب‌سازی بر اساس

**[documented]** Dropdown معیار مرتب‌سازی آیتم‌ها را تعیین می‌کند.

**[observed]** Screenshot مقدار `Date` را نشان می‌دهد.

**[insufficient_evidence]** صفحه فهرست کامل معیارهای Order By را ارائه نمی‌کند.

### 5.2.8. Order — ترتیب

**[documented]** Dropdown جهت مرتب‌سازی را تعیین می‌کند:

- `DESC` — نزولی
- `ASC` — صعودی

**[observed]** Screenshot مقدار `DESC` را نشان می‌دهد.

### 5.2.9. Ignore Sticky Posts — نادیده‌گرفتن نوشته‌های سنجاق‌شده

**[documented]** Sticky post نوشته‌ای است که برای ماندن در ابتدای صفحه اصلی وبلاگ علامت‌گذاری شده، حتی اگر نوشته‌های جدیدتری منتشر شوند. با Toggle روی `Yes`، Sticky بودن هنگام مرتب‌سازی Query در نظر گرفته نمی‌شود.

**[observed]** Screenshot کنترل را روی `Yes` نشان می‌دهد و متن کمکی می‌گوید ترتیب Sticky posts فقط در Frontend قابل مشاهده است.

**[insufficient_evidence]** جمله کمکی Screenshot در متن مقاله توضیح داده نشده؛ دامنه دقیق اثر آن برای Archiveها یا Sourceهای غیر Posts روشن نیست.

### 5.2.10. Query ID — شناسه کوئری

**[observed]** Screenshot یک Text field برای `Query ID` نشان می‌دهد و متن کمکی آن را Custom unique ID برای Server-side filtering معرفی می‌کند.

**ناهماهنگی متن منبع:** توضیح متنی مقاله زیر عنوان Query ID، جمله مربوط به Date را تکرار کرده است («include or exclude items according to when they were created»). این توضیح با Screenshot سازگار نیست و به‌عنوان خطای مستندات ثبت می‌شود.

**[insufficient_evidence]** صفحه موارد زیر را مشخص نمی‌کند:

- قواعد نام‌گذاری Query ID.
- API/Hook مرتبط.
- نمونه کد Server-side filtering.
- یکتا بودن در سطح Page، Site یا Widget.

---

## 5.3. Pagination — صفحه‌بندی

تصویر رسمی:

![Content > Pagination](https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Pagination.jpg)

منبع تصویر: [Elementor — Content-tab-Pagination.jpg](https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Pagination.jpg)

### 5.3.1. Pagination type — نوع صفحه‌بندی

**[documented]** اگر Loop بیش از یک صفحه آیتم داشته باشد، گزینه‌های زیر قابل استفاده‌اند:

| مقدار | ترجمه |
|---|---|
| `Numbers` | شماره صفحات |
| `Previous/Next` | قبلی/بعدی |
| `Numbers + Previous/Next` | شماره‌ها به‌همراه قبلی/بعدی |
| `Load on Click` | بارگذاری با کلیک |
| `Infinite Scroll` | پیمایش بی‌نهایت |

**[observed]** Screenshot مقدار `Numbers` را نمایش می‌دهد.

**[insufficient_evidence]** رفتار جزئی هر نوع، Labelها، Accessibility و Triggerهای Infinite Scroll به مقاله فرعی واگذار شده‌اند.

### 5.3.2. Page Limit — محدودیت تعداد صفحه

**[documented]** Text box حداکثر تعداد صفحه‌هایی را که Loop می‌تواند داشته باشد تعیین می‌کند.

**[observed]** Screenshot مقدار `5` را نشان می‌دهد.

**[insufficient_evidence]** صفحه مقدار `5` را Default رسمی اعلام نمی‌کند.

### 5.3.3. Shorten — کوتاه‌سازی شماره صفحات

**[documented]** هنگام استفاده از Page numbering، برای جلوگیری از شلوغی می‌توان تعداد شماره‌های قابل مشاهده را محدود کرد.

**شرط کاربرد مستند:** مربوط به حالت شماره‌گذاری صفحات است.

### 5.3.4. Alignment — تراز

**[documented]** Pagination در سمت راست، مرکز یا چپ Loop تراز می‌شود.

**[observed]** Screenshot سه دکمه تراز و حالت Center انتخاب‌شده را نشان می‌دهد.

### 5.3.5. Load Type — نوع بارگذاری

**[documented]** هنگام رفتن بازدیدکننده به صفحه جدید، دو روش وجود دارد:

| مقدار | رفتار مستند |
|---|---|
| `Page Reload` | کل صفحه وب دوباره بارگذاری می‌شود |
| `AJAX` | فقط Widget مربوط به Loop Grid دوباره بارگذاری می‌شود |

**[observed]** Screenshot مقدار `Page Reload` را نشان می‌دهد.

**[insufficient_evidence]** صفحه درباره تغییر URL، History API، Focus management، Scroll position، Cache، SEO و Fallback بدون JavaScript توضیح نمی‌دهد.

### 5.3.6. Individual Pagination — صفحه‌بندی مستقل

**[documented]** به‌صورت پیش‌فرض، وقتی چند Loop Grid در یک صفحه وجود دارد، همه Loopها به شماره صفحه یکسان Refresh می‌شوند. مثال رسمی: رفتن به صفحه دوم یک Loop می‌تواند Loop دیگر را هم به صفحه دوم ببرد.

با Toggle روی `On`، هر Loop Grid مستقل Refresh می‌شود.

**محدودیت رسمی:** همه Loop Gridهای یک صفحه باید مقدار یکسانی برای `Individual Pagination` داشته باشند.

**[observed]** Screenshot این Toggle را روی `Off` نشان می‌دهد و یادداشت می‌کند که تنظیم بر ساختار URL صفحه اثر می‌گذارد.

**[insufficient_evidence]** شکل دقیق URL در حالت On/Off و پارامترهای Query string در صفحه شرح داده نشده است.

---

## 5.4. Additional Options — گزینه‌های اضافی

تصویر رسمی صفحه:

![Content > Additional Options](https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Additional-Options.jpg)

منبع تصویر: [Elementor — Content-tab-Additional-Options.jpg](https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Additional-Options.jpg)

**[documented]** عنوان `Additional Options` در فهرست بخش‌های Content tab آمده است. متن بعد از بخش Pagination، کنترل `Nothing Found Message` را شرح می‌دهد.

**[derived]** بر اساس ترتیب مقاله و نام فایل تصویر، Nothing Found Message محتوای اصلی Additional Options است. صفحه جمله صریحی مانند «Additional Options contains Nothing Found Message» ندارد؛ بنابراین این نگاشت Derived است.

### 5.4.1. Nothing Found Message — پیام نبود نتیجه

**[documented]** در برخی حالت‌ها Filter نتیجه‌ای برنمی‌گرداند؛ مثال رسمی ترکیب Categoryهای `Blue` و `Pants` است وقتی محصول Blue pants وجود ندارد.

با Toggle روی `On`، پیام نبود نتیجه نمایش داده می‌شود.

در صورت فعال‌بودن:

| کنترل | رفتار مستند |
|---|---|
| `Text box` | متن پیام بازدیدکننده |
| `Alignment` | تراز راست، مرکز یا چپ |
| `HTML tag` | انتخاب `H1` تا `H6`، `Div` یا `Span` |

صفحه اشاره می‌کند انتخاب HTML tag می‌تواند به موتورهای جست‌وجو برای یافتن و فهم پیام کمک کند.

**[insufficient_evidence]** صفحه Default text، رفتار خالی‌بودن Text box، ARIA live region و اثر Heading hierarchy را مشخص نمی‌کند.

---

# 6. Style tab — تب استایل

## 6.1. Pagination style — استایل صفحه‌بندی

تصویر رسمی:

![Style > Pagination](https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Pagination.jpg)

منبع تصویر: [Elementor — Style-tab-Pagination.jpg](https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Pagination.jpg)

### Typography — تایپوگرافی

**[documented]** اندازه، نوع و رنگ Font مورد استفاده در Pagination را تنظیم می‌کند.

### Colors — رنگ‌ها

**[documented]** رنگ شماره یا متن Pagination را تعیین می‌کند و Stateهای زیر را دارد:

| State | توضیح |
|---|---|
| `Normal` | رنگ پیش‌فرض |
| `Hover` | رنگ هنگام Mouseover |
| `Active` | رنگ مربوط به صفحه‌ای که بازدیدکننده در حال مشاهده آن است |

برای انتخاب رنگ می‌توان از Color picker یا Global color استفاده کرد.

### Space Between — فاصله بین آیتم‌ها

**[documented]** Slider فاصله میان شماره‌ها یا متن‌های Pagination را کنترل می‌کند.

### Spacing — فاصله از لبه‌ها

**[documented]** Slider فاصله شماره‌ها یا متن Pagination از لبه‌های Loop را کنترل می‌کند.

**[insufficient_evidence]** صفحه واحدهای اندازه‌گیری، Min/Max، Responsive بودن و تفاوت Spacing با Padding/Margin را مشخص نمی‌کند.

---

## 6.2. Layout style — استایل چیدمان

تصویر رسمی:

![Style > Layout](https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Layout.jpg)

منبع تصویر: [Elementor — Style-tab-Layout.jpg](https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Layout.jpg)

| کنترل | رفتار مستند |
|---|---|
| `Gap between columns` | Slider فاصله بین ستون‌های Loop را کنترل می‌کند |
| `Gap between rows` | Slider فاصله بین ردیف‌های Loop را کنترل می‌کند |

**[insufficient_evidence]** واحد، محدوده، Breakpointها، امکان مقدار منفی و روش محاسبه Gap در Masonry ذکر نشده است.

---

## 6.3. Nothing Found Message style — استایل پیام نبود نتیجه

تصویر رسمی:

![Style > Nothing Found Message](https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Message-Not-found.jpg)

منبع تصویر: [Elementor — Style-tab-Message-Not-found.jpg](https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Message-Not-found.jpg)

| کنترل | رفتار مستند |
|---|---|
| `Space from top` | فاصله پیام از بالای Loop |
| `Space from bottom` | فاصله پیام از پایین Loop؛ توضیح منبع به‌اشتباه دوباره «top» نوشته است |
| `Typography` | رنگ، اندازه و نوع Font پیام |
| `Color` | رنگ پیام |
| `Text Shadow` | افزودن سایه به متن |
| `Text Stroke` | رنگ‌کردن Outline متن |

**ناهماهنگی متن منبع:** توضیح `Space from bottom` می‌گوید پیام چه‌قدر از «top» فاصله بگیرد؛ با توجه به عنوان کنترل، این جمله به‌عنوان خطای نگارشی ثبت می‌شود و رفتار فنی از آن حدس زده نمی‌شود.

---

# 7. Advanced tab — تب پیشرفته

تصویر رسمی:

![Advanced tab](https://elementor.com/help/wp-content/uploads/2022/01/Advanced-tab.png)

منبع تصویر: [Elementor — Advanced-tab.png](https://elementor.com/help/wp-content/uploads/2022/01/Advanced-tab.png)

**[documented]** Advanced tab برای کنترل Placement، درج Link، افزودن Custom code و موارد بیشتر معرفی شده است.

**محدودیت منبع:** همین صفحه گزینه‌های Advanced را فهرست نمی‌کند و فقط به مقاله عمومی Advanced tab settings لینک می‌دهد. مطابق دامنه این مرحله، جزئیات صفحه فرعی وارد این جزوه نشده است.

---

# 8. Responsive controls — کنترل‌های واکنش‌گرا

## شواهد موجود

- **[documented]** Masonry در تعریف صفحه «visually balanced and responsive» توصیف شده است.
- **[observed]** در Screenshot بخش Layout، کنار `Columns` نماد Device/Responsive دیده می‌شود.

## موارد نامشخص

**[insufficient_evidence]** صفحه مشخص نمی‌کند:

- کدام‌یک از `Columns`، `Items Per Page`، Gapها، Alignment یا Spacingها Responsive هستند.
- Breakpointهای قابل تنظیم چیست.
- مقادیر چگونه Inherit می‌شوند.
- آیا Pagination type در هر Device قابل تغییر است.
- آیا Masonry یا Equal height رفتار Device-specific دارند.

نتیجه: فقط Responsive بودن کنترل Columns از Screenshot قابل مشاهده است؛ تعمیم آن به سایر کنترل‌ها مجاز نیست.

---

# 9. Dynamic data — داده پویا

**[documented]** Loop Grid از Query برای تعیین آیتم‌ها استفاده می‌کند و Template آیتم با Widgetهای دیگر روی Canvas ویرایش می‌شود. فهرست می‌تواند با انتشار محتوای جدید متناسب با Query به‌روزرسانی شود؛ این موضوع در Use caseهای صفحه توصیف شده است.

**[insufficient_evidence]** صفحه حاضر موارد زیر را توضیح نمی‌دهد:

- Dynamic Tags داخل Loop Item Template.
- ACF یا Custom fields.
- Dynamic Image، Dynamic Link یا Dynamic Terms.
- Context داده هر Widget داخل Loop.
- رفتار Fallback برای داده خالی.

بنابراین این جزوه وجود یا جزئیات کنترل‌های Dynamic Tags را از منابع دیگر به این صفحه نسبت نمی‌دهد.

---

# 10. Elementor Pro و پیش‌نیازها

## آنچه صفحه صریحاً می‌گوید

- Loop Grid یک Widget است.
- برای هر Loop Grid یک Template لازم است.
- نوع Template باید با نوع محتوای مورد نمایش سازگار باشد.
- برای گزینه‌های Products و Product Taxonomy، محتوای WooCommerce مطرح شده است.

## آنچه صفحه صریحاً نمی‌گوید

**[insufficient_evidence]** در بدنه مقاله عبارت صریحی مبنی بر این‌که `Elementor Pro` پیش‌نیاز Loop Grid است وجود ندارد. همچنین موارد زیر مشخص نشده‌اند:

- حداقل نسخه Elementor Core.
- حداقل نسخه Elementor Pro.
- نیاز به فعال‌بودن Feature/Experiment.
- حداقل نسخه WordPress یا PHP.
- الزام نصب WooCommerce برای نمایش Products، هرچند از ماهیت گزینه می‌توان ارتباط را فهمید.

**قانون این جزوه:** با وجود دانش عمومی محصول، چون دامنه پژوهش فقط همین صفحه است، Elementor Pro به‌عنوان پیش‌نیاز قطعی این منبع ثبت نمی‌شود.

---

# 11. Skin options

**[insufficient_evidence]**

- عبارت `Skin` در متن اصلی صفحه پیدا نشد.
- هیچ بخش یا کنترل مستندی با نام `Skin options` ارائه نشده است.
- تصاویر رسمی مرتبط با مقاله نیز در عناوین خود Layout، Query، Pagination، Additional Options، Style و Advanced را پوشش می‌دهند، نه Skin.

نتیجه: وجود، عدم وجود یا مقادیر Skin برای Loop Grid از این صفحه قابل اثبات نیست.

---

# 12. شروط نمایش کنترل‌ها

| کنترل | شرط مستند |
|---|---|
| `Hide Empty` | فقط در Loop Grid نمایش‌دهنده Taxonomyها و Typeها |
| `Filter by depth` | فقط برای Taxonomyهای چندسطحی |
| Depth dropdown | پس از فعال‌کردن `Filter by depth` |
| `Shorten` | در زمینه Page numbering کاربرد دارد |
| Nothing Found Message fields | پس از فعال‌کردن نمایش پیام |
| Alternate template settings | Toggle وجود قابلیت را فعال می‌کند؛ جزئیات شرطی در صفحه فرعی است |
| `Individual Pagination` | در صفحات دارای یک یا چند Loop قابل تنظیم است، اما همه Loopهای صفحه باید مقدار یکسان داشته باشند |

**[insufficient_evidence]** شرط نمایش کنترل‌های وابسته به نوع Pagination، Sourceهای مختلف، Product/Post Taxonomy و Alternate Template به‌طور کامل فهرست نشده است.

---

# 13. محدودیت‌ها و هشدارهای صریح

1. **Template type باید درست باشد.** Product در Posts template type نمایش داده نمی‌شود.
2. **Equal height روی همه Parent containerها اعمال می‌شود.** ترکیب Parentهای Equal و Unequal در یک Loop پشتیبانی نمی‌شود.
3. **Filter by depth فقط برای Taxonomy چندسطحی است.**
4. **Hide Empty فقط برای Taxonomyها و Typeهاست.**
5. **Individual Pagination باید برای همه Loop Gridهای یک صفحه یکسان تنظیم شود.**
6. **جزئیات بسیاری به مقاله‌های فرعی منتقل شده‌اند.** این صفحه برای رفتار کامل Query، Pagination، Layout customization و Alternate Template کافی نیست.

---

# 14. ناهماهنگی‌ها و خطاهای مستندات صفحه

| محل | متن/مشکل | نحوه برخورد این جزوه |
|---|---|---|
| Query > Exclude | توضیح دوباره می‌گوید `Click include` | خطای احتمالی Copy-paste؛ رفتار حدس زده نشده |
| Query > Query ID | توضیح Date تکرار شده است | Screenshot و متن با هم ناسازگار؛ جزئیات Query ID ناکافی |
| Hide Empty | عبارت `contain not posts or products` از نظر نگارشی نادرست است | مفهوم به‌صورت «هیچ Post/Product ندارند» ترجمه شده |
| Nothing Found Message > HTML tag | نشانه‌گذاری متن منبع شکسته است | فقط گزینه‌های صریح H1–H6، Div و Span ثبت شده |
| Style > Space from bottom | توضیح دوباره `top` را ذکر می‌کند | خطای نگارشی ثبت شده؛ رفتار بیشتر حدس زده نشده |
| تصویرها | مسیر بعضی Screenshotها متعلق به 2022/2023 است، در حالی که مقاله در 2026 به‌روزرسانی شده | تاریخ URL تصویر به‌عنوان نسخه UI تلقی نشده |

---

# 15. فهرست جامع کنترل‌ها

## Content > Layout

- `Choose template type`
  - `Posts`
  - `Post Taxonomy`
  - `Products`
  - `Product Taxonomy`
- `Choose a template`
- `Edit template`
- `Columns`
- `Items Per Page`
- `Masonry`
- `Equal height`
- `Apply an alternate template`

## Content > Query

- `Source`
  - Posts
  - Pages
  - Landing pages
  - Manually selected pages
  - Current Query
  - Related items
- `Include`
- `Exclude`
- `Include By / Exclude By`
- `Date`
- `Hide Empty`
- `Filter by depth`
- `Order By`
- `Order`
  - DESC
  - ASC
- `Ignore Sticky Posts`
- `Query ID`

## Content > Pagination

- `Pagination`
  - Numbers
  - Previous/Next
  - Numbers + Previous/Next
  - Load on Click
  - Infinite Scroll
- `Page Limit`
- `Shorten`
- `Alignment`
- `Load Type`
  - Page Reload
  - AJAX
- `Individual Pagination`

## Content > Additional Options

- `Nothing Found Message`
- `Text box`
- `Alignment`
- `HTML tag`
  - H1–H6
  - Div
  - Span

## Style > Pagination

- `Typography`
- `Colors`
  - Normal
  - Hover
  - Active
- `Color`
- `Space Between`
- `Spacing`

## Style > Layout

- `Gap between columns`
- `Gap between rows`

## Style > Nothing Found Message

- `Space from top`
- `Space from bottom`
- `Typography`
- `Color`
- `Text Shadow`
- `Text Stroke`

## Advanced

- جزئیات کنترل‌ها در صفحه حاضر فهرست نشده است.

---

# 16. ماتریس شواهد موردهای درخواستی

| موضوع درخواستی | نتیجه |
|---|---|
| همه Tabها و Sectionها | پوشش داده شد |
| Layout | documented |
| Query | documented، با شکاف در گزینه‌های دقیق |
| Pagination | documented، با شکاف در URL/A11y/رفتار کامل |
| Additional Options | عنوان documented؛ نگاشت به Nothing Found Message به‌صورت derived |
| Nothing Found Message | documented |
| Template selection | documented |
| Columns | documented؛ Responsive icon observed |
| Items Per Page | documented |
| Masonry | documented |
| Alternate Template | قابلیت documented؛ جزئیات insufficient |
| Skin options | insufficient_evidence |
| Responsive controls | محدود؛ Columns observed، سایر موارد insufficient |
| Dynamic data | Query/update behavior documented؛ Dynamic Tags insufficient |
| Elementor Pro prerequisite | insufficient_evidence در همین صفحه |
| تاریخ منبع | June 19, 2026 documented |
| نسخه دقیق افزونه | insufficient_evidence |

---

# 17. تصاویر رسمی و قابلیت استناد

| تصویر | URL رسمی | وضعیت بررسی |
|---|---|---|
| Content > Layout | <https://elementor.com/help/wp-content/uploads/2022/01/Content-Layout.png> | تصویر مستقیماً مشاهده شد |
| Content > Query | <https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Query.jpg> | تصویر مستقیماً مشاهده شد |
| Content > Pagination | <https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Pagination.jpg> | تصویر مستقیماً مشاهده شد |
| Content > Additional Options | <https://elementor.com/help/wp-content/uploads/2023/12/Content-tab-Additional-Options.jpg> | URL از Embed رسمی صفحه استخراج شد؛ Fetch تصویری در ابزار پژوهش ناموفق بود |
| Style > Pagination | <https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Pagination.jpg> | URL از Embed رسمی صفحه استخراج شد؛ Fetch تصویری در ابزار پژوهش ناموفق بود |
| Style > Layout | <https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Layout.jpg> | URL از Embed رسمی صفحه استخراج شد؛ Fetch تصویری در ابزار پژوهش ناموفق بود |
| Style > Message Not Found | <https://elementor.com/help/wp-content/uploads/2023/12/Style-tab-Message-Not-found.jpg> | URL از Embed رسمی صفحه استخراج شد؛ Fetch تصویری در ابزار پژوهش ناموفق بود |
| Advanced | <https://elementor.com/help/wp-content/uploads/2022/01/Advanced-tab.png> | URL از Embed رسمی صفحه استخراج شد؛ Fetch تصویری در ابزار پژوهش ناموفق بود |

> شکست Fetch چهار تصویر آخر به‌معنای نامعتبر بودن URL نیست؛ URLها مستقیماً از لینک Image داخل صفحه رسمی استخراج شده‌اند. با این حال Observationهای UI فقط بر سه تصویری تکیه می‌کنند که مستقیماً مشاهده شدند.

---

# 18. Insufficient evidence — موارد نیازمند منبع تکمیلی

- نسخه دقیق Elementor Core و Pro متناظر با مقاله.
- Pro-only بودن Widget از خود همین صفحه.
- فهرست کامل گزینه‌های `Order By` و `Date`.
- منطق چندگانه Include/Exclude.
- قواعد و نمونه کد `Query ID`.
- URL structure و Browser history در Pagination.
- Accessibility انواع Pagination و Nothing Found Message.
- Responsive controls تمام فیلدها.
- Dynamic Tags و Context داده داخل Loop Item.
- Skin options.
- جزئیات Alternate Template.
- جزئیات Advanced tab.
- Defaultهای قطعی؛ اعداد Screenshot به‌عنوان Default رسمی ثبت نشده‌اند.

---

# 19. ارجاعات رسمی بدون انتقال محتوا

صفحه اصلی برای مطالعه بیشتر به مقاله‌های رسمی زیر ارجاع می‌دهد، اما محتوای آن‌ها در این مرحله وارد نشده است:

- Build a Loop Grid
- Build a query with the Loop Grid
- Customize the layout of a Loop Grid
- Customize which items appear in a Loop Grid
- Paginate a Loop Grid
- Build a loop from an existing template
- Add an alternate template in a Loop Grid
- Taxonomy Filter widget

---

# 20. جمع‌بندی

Loop Grid بر پایه یک Template آیتم و یک Query کار می‌کند. تنظیمات اصلی صفحه رسمی شامل انتخاب نوع و خود Template، Columns، Items Per Page، Masonry، Equal height، Alternate Template، Source و فیلترهای Query، چند نوع Pagination، Page Reload/AJAX، Individual Pagination و Nothing Found Message است. Style tab نیز Pagination، فاصله‌های Layout و ظاهر پیام نبود نتیجه را پوشش می‌دهد.

این منبع برای Inventory کنترل‌های اصلی مناسب است، اما برای Specification کامل فنی کافی نیست. به‌ویژه Pro prerequisite، نسخه دقیق، Skin، Dynamic Tags، Responsive behavior کامل، Query ID و جزئیات URL/AJAX باید در مراحل مستقل و با منابع رسمی تکمیلی بررسی شوند.
