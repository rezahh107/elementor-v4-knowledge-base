---
id: elementor.help.query-configuration
title: "Elementor Query Configuration — جزوه جامع فارسی"
source_url: "https://elementor.com/help/create-queries/"
source_title: "Create&nbsp;queries"
source_type: official_help
version_scope: "rolling_documentation; exact_elementor_versions_not_stated"
last_updated: "2025-06-30"
researched_at: "2026-06-22T13:01:23+03:00"
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-008
product_scope:
  - Elementor query-capable widgets and elements
  - Loop Grid examples
  - Archive queries
  - WooCommerce product queries
  - Post and Product Taxonomy queries
---

# Elementor Query Configuration — جزوه جامع فارسی

> دامنه: فقط مقاله رسمی Elementor در URL بالا و تصاویر تعبیه‌شده همان صفحه. محتوای صفحات لینک‌شده مانند `Custom Query Filter` یا مثال مستقل Taxonomy به این منبع نسبت داده نشده است.

## 1. مشخصات منبع و قرارداد شواهد

| فیلد | مقدار |
|---|---|
| عنوان نمایشی منبع | `Create&nbsp;queries` |
| URL | <https://elementor.com/help/create-queries/> |
| آخرین به‌روزرسانی اعلام‌شده | `June 30, 2025` |
| نسخه دقیق Core/Pro | اعلام نشده |
| وضعیت | `completed_with_gaps` |

- **documented:** در متن رسمی صریح است.
- **observed:** مستقیماً در تصویر رسمی دیده شده است.
- **derived:** برداشت محدود از شواهد موجود است.
- **insufficient_evidence:** صفحه برای نتیجه قطعی کافی نیست.

تصاویر رسمی صفحه شناسایی و در بخش‌های مرتبط Embed شده‌اند. ابزار پژوهش نتوانست فایل‌های تصویر را به‌صورت بصری Fetch کند؛ بنابراین ادعاهای جزئی صرفاً تصویری به `observed` ارتقا داده نشده‌اند.

## 2. تعریف و دامنه

**[documented]** Query درخواست اطلاعات از Database وب‌سایت است. نمونه رسمی: نمایش همه Posts مرتبط با European travel.

موارد استفاده صریح:

1. Loop Grid برای دسته‌های مشخص Products
2. Archive page برای Posts بر اساس Date
3. Archive page برای Posts بر اساس Category

**[documented]** برای ساخت Query باید وارد `Content` tab یک Widget دارای Query شد. مثال‌های عملی مقاله با Loop Grid هستند؛ Current Query در Archive، Related در Single Post، و Related Products/Upsells/Cross-Sells در Single Product نیز نام برده شده‌اند.

**[insufficient_evidence]** مقاله فهرست جامع Widgetها و Elementهای Query-capable را ارائه نمی‌کند.

## 3. Workflow عمومی و Template Type

1. `Content` tab را باز کنید.
2. در `Layout` یک Template Type انتخاب کنید.
3. بخش `Query` را باز کنید.
4. `Source` و سپس Include/Exclude و کنترل‌های وابسته را تنظیم کنید.

![Content tab](https://elementor.com/help/wp-content/uploads/2025/06/image-21.png)

Template Typeهای نام‌برده‌شده:

| گزینه | ترجمه | کاربرد |
|---|---|---|
| `Posts` | نوشته‌ها | داده‌های Posts |
| `Products` | محصولات | داده‌های Products |
| `Post Taxonomy` | طبقه‌بندی نوشته | Categories، Tags و Types |
| `Product Taxonomy` | طبقه‌بندی محصول | Product categories، tags و brands |

**[documented]** گزینه‌ها با نصب WooCommerce تغییر می‌کنند.

## 4. Post queries

### 4.1. Source

| Source | ترجمه | رفتار مستند |
|---|---|---|
| `Posts` | نوشته‌ها | Posts و داده‌های Post؛ بدون Products |
| `Pages` | برگه‌ها | Pages سایت |
| `Products` | محصولات | فقط در صورت نصب WooCommerce |
| `Manual Selection` | انتخاب دستی | نمایش Pages، Posts و Products انتخاب‌شده |
| `Current Query` | Query جاری | فیلتر Query موجود برای Archive pages |
| `Related` | مرتبط | آیتم‌های دارای Category یا Tag مشترک |

![Post Source](https://elementor.com/help/wp-content/uploads/2025/06/image-23.png)

### 4.2. Current Query و Related

**[documented]** Current Query روی Query موجود در Archive فیلتر اضافه می‌کند؛ مثال: از همه Pants فقط Red Pants.

**[documented]** Related آیتم‌های هم‌Taxonomy را نشان می‌دهد؛ مثال: در Single Post مربوط به News، سایر News posts. مقاله پیشنهاد می‌کند Current post با Exclude حذف شود.

**[insufficient_evidence]** Context دقیق Preview، الگوریتم Related و تقدم Taxonomyها توضیح داده نشده است.

### 4.3. Include / Exclude، Terms و Author

![Include or Exclude](https://elementor.com/help/wp-content/uploads/2025/06/Choose-include-Exclude-.png)

- `Terms`: Categories، Tags، Formats و Custom taxonomies
- `Author`: Include بر اساس نام نویسنده
- امکان افزودن چند Variable؛ مثال: Category برابر Fashion و Tag برابر Modern

**[insufficient_evidence]** Operator عمومی AND/OR و تقدم Include/Exclude صریح نیست.

### 4.4. Date

گزینه‌ها:

- `Past day`
- `Past week`
- `Past month`
- `Past quarter`
- `Past Year`
- `Custom` برای Date range

**[insufficient_evidence]** Timezone، مرز بازه و فرمت Custom بیان نشده است.

### 4.5. Order By و Order

`Order By` برای Posts:

- `Date`
- `Title`
- `Menu order`
- `Last modified`
- `Comment count`
- `Random`

`Order`:

- `ASC`: کمترین به بیشترین؛ برای Date یعنی Oldest ابتدا.
- `DESC`: بیشترین به کمترین؛ برای Title یعنی آخر الفبایی ابتدا.

### 4.6. Ignore Sticky Posts و Query ID

- `Ignore Sticky Posts`: انتخاب نمایش یا پنهان‌کردن Sticky posts.
- `Query ID`: برای Modify کردن Main Query و Advanced filtering؛ صفحه به مستند جداگانه Custom Query Filter لینک می‌دهد.

**[insufficient_evidence]** Hook، Syntax، نوع مقدار و نمونه کد Query ID در این صفحه وجود ندارد.

### 4.7. Exclude by options

| کنترل | رفتار |
|---|---|
| `Current post` | حذف نوشته جاری |
| `Manual Selection` | انتخاب Posts مشخص برای حذف |
| `Avoid duplicates` | جلوگیری از تکرار آیتم منطبق با چند معیار |
| `Offset` | Skip کردن تعداد مشخصی از Posts ابتدای نتیجه |

**[insufficient_evidence]** ارتباط Offset با Pagination و ترتیب اجرای Exclude مشخص نیست.

### 4.8. Manual Selection source

- `Search & Select`: ورود نام Pages، Posts یا Products
- `Order by`: Date، Title، Menu order، Last modified، Comment count، Random
- `Order`: ASC یا DESC
- `Query ID`: Unique number برای Advanced filtering

![Manual Selection](https://elementor.com/help/wp-content/uploads/2025/06/image-26.png)

### 4.9. مثال Post

هدف: Posts در Category برابر `Fashion` به‌جز Posts دارای Tag برابر `Green info`.

1. Loop Grid بسازید.
2. Template Type را Posts بگذارید.
3. Query را باز کنید.
4. Source را Posts نگه دارید.
5. Fashion را Include کنید.
6. Exclude tab را باز کنید.
7. Green info را Exclude کنید.

![Post example start](https://elementor.com/help/wp-content/uploads/2025/06/image-27.png)
![Post example query](https://elementor.com/help/wp-content/uploads/2025/06/image-28.png)
![Post example include](https://elementor.com/help/wp-content/uploads/2025/06/image-29.png)
![Post example exclude](https://elementor.com/help/wp-content/uploads/2025/06/image-1.gif)

## 5. Product queries

**[documented]** WooCommerce برای Product queries لازم است.

### 5.1. Product Sources

| Source | رفتار |
|---|---|
| `Current Query` | فیلتر Query موجود در Archive |
| `Latest Products` | جدیدترین Products WooCommerce |
| `Sale` | Products دارای Sale price |
| `Featured` | Products علامت‌خورده به‌عنوان Featured |
| `Manual Selection` | آیتم‌های انتخاب‌شده |
| `Related Products` | Products هم‌Taxonomy |
| `Upsells` | گزینه Higher-end لینک‌شده در Linked Products |
| `Cross-Sells` | محصول مکمل لینک‌شده در Linked Products |

![Product Source](https://elementor.com/help/wp-content/uploads/2025/06/image-32.png)

**[documented]** Related Products معمولاً همراه Exclude برای حذف Current product استفاده می‌شود. Upsells و Cross-Sells در Single Product template کاربرد دارند.

### 5.2. Include/Exclude و Ordering محصول

برای Latest Products، Sale و Featured:

- `Terms`: Categories، Tags، Formats، Custom taxonomies
- `Author`: فردی که Product را اضافه کرده است
- چند Variable قابل افزودن است

`Order By`:

- Date
- Title
- Price
- Popularity
- Rating
- Random
- Menu order

`Order`: ASC یا DESC.

![Product filters](https://elementor.com/help/wp-content/uploads/2025/06/image-34.png)

### 5.3. Product Exclude و Manual Selection

- `Manual Selection` برای حذف Product مشخص نام برده شده است.
- مقاله Bullet دیگری با Label `Search & Select` دارد، اما توضیح آن درباره جلوگیری از Duplicate است؛ نام صحیح کنترل از همین متن قطعی نیست.
- بخش Manual Selection موارد Search & Select، Terms، Author، Order By و Order را فهرست می‌کند، ولی ساختار صفحه روشن نمی‌کند همه این کنترل‌ها هم‌زمان ظاهر می‌شوند یا متن تکراری است.

**[insufficient_evidence]** این دو ناسازگاری بدون مشاهده موفق تصویر قابل رفع قطعی نیستند.

### 5.4. مثال Product

هدف: Products در Category برابر `Eco` با ترتیب الفبایی.

1. Products را در Layout انتخاب کنید.
2. Query را باز کنید.
3. Source را Latest Products نگه دارید.
4. Include by را Term بگذارید.
5. Term را Eco وارد کنید.
6. Order By را Title و Order را ASC بگذارید.

![Product example Source](https://elementor.com/help/wp-content/uploads/2025/06/image-39.png)
![Product example Term](https://elementor.com/help/wp-content/uploads/2025/06/image-41.png)
![Product example Order](https://elementor.com/help/wp-content/uploads/2025/06/image-42.png)

## 6. Post Taxonomy queries

Sourceها:

- `Categories`
- `Tags`

![Post Taxonomy](https://elementor.com/help/wp-content/uploads/2025/06/image-44.png)

### 6.1. Category filter

| کنترل | گزینه/رفتار |
|---|---|
| `Filter` | Show All یا Manual Selection |
| `Order by` | Name یا ID |
| `Order` | ASC یا DESC |
| `Hide Empty` | با Yes، Categories بدون Content مخفی می‌شوند |
| `Filter by depth` | تعداد Sublevelها |
| `Query ID` | Unique number برای Advanced filtering |

### 6.2. Tag filter

- Include یا Exclude tabs
- `Include by`: Show All یا Manual Selection
- `Order by`: Name یا ID
- `Order`: ASC یا DESC
- `Hide Empty`
- `Query ID`

در Exclude:

- `Search & Select`
- `Avoid Duplicates`
- `Skip Taxonomy`: Skip کردن تعداد عددی از Taxonomies/Terms

**[insufficient_evidence]** تقدم Skip Taxonomy نسبت به Sort و Exclude مشخص نیست.

## 7. Product Taxonomy queries

**[documented]** WooCommerce برای Product Taxonomy لازم است.

Sourceها:

- `Brand`
- `Product categories`
- `Product tags`

![Product Taxonomy](https://elementor.com/help/wp-content/uploads/2025/06/image-46.png)

### 7.1. Product Category and Brands

- Filter: Show All یا Manual Selection
- Order by: Name یا ID
- Order: ASC یا DESC
- Hide Empty
- Filter by depth
- Query ID

### 7.2. Product Tag

- Include/Exclude
- Include by: Show All یا Manual Selection
- Order by: Name یا ID
- Order: ASC یا DESC
- Hide Empty
- Query ID
- در Exclude: Search & Select، Avoid Duplicates، Skip Taxonomy

**[insufficient_evidence]** مقاله مشخص نمی‌کند Brand از WooCommerce Core، Elementor یا Extension دیگری تأمین می‌شود.

## 8. ماتریس خلاصه کنترل‌ها

| کنترل | Posts | Products | Post Taxonomy | Product Taxonomy |
|---|---:|---:|---:|---:|
| Source | بله | بله | بله | بله |
| Include/Exclude | بله | بله | برای Tags | برای Tags |
| Terms | بله | بله | Taxonomy-specific | Taxonomy-specific |
| Author | بله | بله | خیر | خیر |
| Date filter | بله | صریحاً فهرست نشده | خیر | خیر |
| Order By | شش گزینه | هفت گزینه | Name/ID | Name/ID |
| Order | ASC/DESC | ASC/DESC | ASC/DESC | ASC/DESC |
| Ignore Sticky Posts | بله | خیر | خیر | خیر |
| Avoid Duplicates | Exclude | متن مبهم | Exclude | Exclude |
| Offset | Exclude | ذکر نشده | خیر | خیر |
| Hide Empty | خیر | خیر | بله | بله |
| Filter by depth | خیر | خیر | Category | Category/Brand |
| Skip Taxonomy | خیر | خیر | Exclude Tag | Exclude Tag |
| Query ID | بله | کامل فهرست نشده | بله | بله |

«خیر» یعنی مقاله در آن Context ثبت نکرده است، نه اینکه نبودن کنترل در محصول اثبات شده باشد.

## 9. شرط‌ها، محدودیت‌ها و ناهماهنگی‌های منبع

### شرط‌های مستند

- نصب WooCommerce باعث دسترسی به Products و Product Taxonomy می‌شود.
- انتخاب Exclude کنترل‌های اضافی را ظاهر می‌کند.
- Source و Template Type مجموعه کنترل‌های بعدی را تغییر می‌دهند.
- Hide Empty روی Yes، Terms بدون Content را پنهان می‌کند.

### ناهماهنگی‌های متن

1. Product Exclude section از عبارت «excluding posts» استفاده می‌کند.
2. Bullet با Label Search & Select توضیح Avoid Duplicates دارد.
3. مثال Related Products عبارت `other pants posts` دارد.
4. مثال چند Variable محصول هنوز از Posts سخن می‌گوید.
5. Tag filter در توضیح Show All از Categories نام می‌برد.
6. Query ID یک‌بار Modify main query و بار دیگر Assign unique number توصیف شده است.
7. Product selection یک‌بار Template Type و جای دیگر Source field در Layout نامیده شده است.

## 10. insufficient_evidence

- نسخه دقیق Elementor Core/Pro
- پیش‌نیاز صریح Elementor Pro
- فهرست جامع Widgetها/Elementها
- Default values
- منطق عمومی AND/OR و تقدم Include/Exclude
- رفتار Runtime و Preview برای Current Query
- الگوریتم Related
- Timezone و Boundaryهای Date
- Query ID hooks و API
- تعامل Offset/Avoid Duplicates با Pagination
- AJAX، URL و Accessibility
- Brand provider
- جزئیات تصویری صرف که Fetch نشدند

## 11. تصاویر رسمی تکمیلی

فایل‌های رسمی مقاله در مسیر `https://elementor.com/help/wp-content/uploads/2025/06/` قرار دارند و شامل `image-21.png` تا `image-46.png`، فایل `Choose-include-Exclude-.png` و دو GIF مثال هستند. تصاویر در ترتیب مقاله، مراحل Post، Product، Post Taxonomy و Product Taxonomy را همراهی می‌کنند. محتوای Pixel-level آن‌ها در این نسخه Claim نشده است.

## 12. جمع‌بندی

**[documented]** مقاله چهار خانواده Post/Page/Related، Product، Post Taxonomy و Product Taxonomy را پوشش می‌دهد و Source، Include/Exclude، Terms، Author، Date، Ordering، Current Query، Related، Manual Selection، Query ID، Offset و Avoid Duplicates را در Contextهای مشخص معرفی می‌کند.

**[derived]** صفحه مرجع گسترده UI است، اما Specification فنی Query engine نیست.

**[insufficient_evidence]** برای API، منطق ترکیب شروط، نسخه‌بندی، AJAX، Pagination و Accessibility باید منابع رسمی مستقل جداگانه بررسی شوند.
