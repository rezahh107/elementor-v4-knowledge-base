---
id: elementor.help.taxonomy-filter
title: "Taxonomy Filter widget — جزوه جامع فیلتر Taxonomy برای Loop Grid"
source_url: "https://elementor.com/help/taxonomy-filter/"
canonical_url: "https://elementor.com/help/taxonomy-filter-widget/"
source_title: "Taxonomy Filter widget"
source_type: official_help
version_scope: "rolling_documentation; exact_elementor_core_and_pro_versions_not_stated"
last_updated: "2026-06-04"
researched_at: "2026-06-22T15:01:58+03:00"
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-010
product_scope:
  - Elementor
  - Loop Grid widget
  - Taxonomy Filter widget
source_images:
  - "https://elementor.com/help/wp-content/uploads/2023/07/image-3.png"
  - "https://elementor.com/help/wp-content/uploads/2023/07/image-4.png"
  - "https://elementor.com/help/wp-content/uploads/2023/07/image-5.png"
  - "https://elementor.com/help/wp-content/uploads/2023/08/Content-Tab-Layout-1.png"
  - "https://elementor.com/help/wp-content/uploads/2023/08/Content-tab-Settings.jpg"
  - "https://elementor.com/help/wp-content/uploads/2023/08/Style-tab-Items.png"
---

# Taxonomy Filter widget — جزوه جامع فارسی

> **دامنه این جزوه:** متن کامل و تصاویر تعبیه‌شده در صفحه رسمی Elementor با عنوان `Taxonomy Filter widget`. آدرس ثبت‌شده اولیه `taxonomy-filter/` است، اما لینک جاری فهرست رسمی Widgets به `taxonomy-filter-widget/` می‌رسد. مطالب صفحات فرعی لینک‌شده، کد افزونه یا دانش عمومی WordPress بدون بررسی مستقل به این مقاله نسبت داده نشده‌اند.

## 1. مشخصات منبع

| فیلد | مقدار |
|---|---|
| عنوان جاری مقاله | `Taxonomy Filter widget` |
| URL ورودی/ثبت‌شده | <https://elementor.com/help/taxonomy-filter/> |
| URL جاری در فهرست رسمی Widgets | <https://elementor.com/help/taxonomy-filter-widget/> |
| ناشر | Elementor Knowledge Hub |
| آخرین به‌روزرسانی اعلام‌شده | `June 4, 2026` |
| تاریخ پژوهش | `2026-06-22` |
| نسخه دقیق Elementor Core | در صفحه اعلام نشده |
| نسخه دقیق Elementor Pro | در صفحه اعلام نشده |
| پیش‌نیاز صریح Elementor Pro | در صفحه اعلام نشده |
| وضعیت پوشش | `completed_with_gaps` |

### وضعیت URL

**[observed]** صفحه فهرست رسمی Widgets، لینک `Taxonomy Filter widget` را با مسیر `https://elementor.com/help/taxonomy-filter-widget/` ارائه می‌کند.

**[insufficient_evidence]** مقاله مشخص نمی‌کند URL ثبت‌شده قدیمی `taxonomy-filter/` با Redirect دائمی، موقت یا Canonical به مسیر جاری متصل است؛ تاریخچه تغییر مسیر نیز در صفحه وجود ندارد.

---

## 2. قرارداد وضعیت شواهد

- **documented:** مطلب به‌صورت صریح در متن رسمی مقاله آمده است.
- **observed:** مطلب مستقیماً در تصویر رسمی دیده شده، اما متن آن را به‌عنوان رفتار یا مقدار پیش‌فرض رسمی تعریف نکرده است.
- **derived:** نتیجه محدود و قابل ردیابی از شواهد موجود است؛ نباید به API contract یا حقیقت مستقل محصول ارتقا یابد.
- **insufficient_evidence:** صفحه برای نتیجه‌گیری دقیق یا کامل اطلاعات کافی ارائه نمی‌کند.

---

## 3. خلاصه اجرایی

**[documented]** `Taxonomy Filter widget` برای کنترل آیتم‌های نمایش‌داده‌شده در یک `Loop Grid` استفاده می‌شود و می‌تواند آن‌ها را بر اساس `Categories` — دسته‌ها یا `Tags` — برچسب‌ها فیلتر کند.

**[documented]** این Widget فقط همراه یک Loop Grid قابل استفاده است. کاربر ابتدا Loop Grid را می‌سازد یا فعال نگه می‌دارد، سپس Taxonomy Filter را به Loop Grid متصل می‌کند.

**[documented]** مقاله قابلیت‌های اصلی زیر را توضیح می‌دهد:

1. انتخاب Loop Grid هدف؛
2. انتخاب Taxonomy از میان Category یا Tag؛
3. جهت افقی یا عمودی منوی فیلتر؛
4. تراز `Start`، `Center`، `End` یا `Stretch`؛
5. `Multiple Selection` با منطق `AND` یا `OR`؛
6. نمایش یا مخفی‌کردن آیتم‌های خالی؛
7. نمایش یا مخفی‌کردن فرزندان Taxonomy؛
8. نمایش، مخفی‌کردن و تغییر عنوان آیتم `All`؛
9. محدودکردن تعداد Taxonomyها؛
10. Wrap یا Horizontal Scroll برای آیتم‌های اضافی؛
11. Style states شامل `Normal`، `Hover` و `Active`.

**[documented]** `Current Query` پشتیبانی نمی‌شود. در Archive Page، اگر Loop Grid Query را از Display Conditions صفحه به ارث ببرد، فیلتر کار نمی‌کند؛ Query باید مستقیماً در خود Loop Grid تعریف شود.

---

# 4. پیش‌نیازها و محدودیت پایه

## 4.1. اتصال اجباری به Loop Grid

**[documented]** Taxonomy Filter فقط به‌عنوان بخشی از یک `Loop Grid` قابل استفاده است و مقاله صریحاً می‌گوید Loop Grid باید فعال باشد.

**[derived]** Taxonomy Filter در دامنه همین مقاله یک فیلتر مستقل برای هر نوع Widget دیگر معرفی نشده است.

**[insufficient_evidence]** صفحه مشخص نمی‌کند:

- چند Loop Grid باید در همان صفحه موجود باشد تا Dropdown انتخاب فعال شود؛
- آیا Loop Grid می‌تواند داخل Container، Template، Popup یا Nested structure دیگری باشد؛
- اتصال بین Filter و Grid بر اساس Widget ID، DOM relation یا سازوکار داخلی دیگری انجام می‌شود؛
- اتصال به `Loop Carousel` یا سایر Widgetها پشتیبانی می‌شود یا نه.

## 4.2. پیش‌نیازهای نسخه و مجوز

**[insufficient_evidence]** نسخه دقیق Elementor Core، نسخه دقیق Elementor Pro، حداقل نسخه WordPress و نوع Plan لازم در مقاله اعلام نشده‌اند.

---

# 5. ساخت و اتصال Taxonomy Filter

## 5.1. مراحل رسمی

**[documented]** روند مقاله:

1. یک `Loop Grid` بسازید.
2. `Taxonomy Filter widget` را به صفحه‌ای که Loop Grid در آن قرار دارد اضافه کنید.
3. در پنل، تب `Content` — محتوا را باز کنید.
4. بخش `Layout` — چیدمان را گسترش دهید.
5. از Dropdown با نام `Selected Loop Grid` — Loop Grid انتخاب‌شده، Grid هدف را انتخاب کنید.
6. از Dropdown با نام `Taxonomy` — طبقه‌بندی، `Category` یا `Tag` را انتخاب کنید.
7. پس از انتخاب، منویی از آیتم‌های Taxonomy در کنار/بالای Loop Grid ظاهر می‌شود.
8. بازدیدکننده با انتخاب یک Category یا Tag فقط آیتم‌های مرتبط را می‌بیند و با `All` می‌تواند نمایش کامل را بازگرداند.

## 5.2. آنچه در تصاویر رسمی دیده می‌شود

**[observed]** تصویر `image-3.png`، کنترل `Selected loop grid` را در `Content > Layout` نشان می‌دهد؛ مقدار اولیه قابل مشاهده `Select a widget` است.

**[observed]** تصویر `image-4.png`، Loop Grid با نام `Loop Grid 1` و Dropdown بازشده `Taxonomy` را نشان می‌دهد. گزینه‌های قابل مشاهده عبارت‌اند از:

- `Select a taxonomy`
- `Categories`
- `Tags`

**[observed]** تصویر `image-5.png`، خروجی افقی با آیتم‌های `All`، `Funky`، `Glam` و `Sexy` را نشان می‌دهد. `Funky` با رنگ متفاوت دیده می‌شود و می‌تواند نمونه‌ای از State انتخاب‌شده باشد؛ تصویر مقدار پیش‌فرض رنگ را اثبات نمی‌کند.

**[observed]** تصویر `Content-Tab-Layout-1.png` مقادیر نمونه زیر را نشان می‌دهد:

- `Selected loop grid: Loop Grid 1`
- `Taxonomy: Categories`
- `Direction: Horizontal`
- چهار Icon برای `Item Alignment`
- Icon دستگاه کنار `Direction` و `Item Alignment`

**[insufficient_evidence]** مقادیر تصاویر، Default رسمی یا نسخه‌پایدار کنترل‌ها محسوب نمی‌شوند؛ مقاله نسخه UI تصاویر را اعلام نکرده است.

---

# 6. رفتار فیلتر در خروجی

## 6.1. انتخاب یک Category یا Tag

**[documented]** با کلیک روی Category یا Tag، فقط Postهایی که به همان Classification مرتبط‌اند در Loop Grid نمایش داده می‌شوند.

مثال رسمی:

- کاربر `Funky` را انتخاب می‌کند؛
- Loop Grid فقط Postهای مرتبط با Funky را نمایش می‌دهد؛
- کاربر برای بازگشت به همه Postها روی `All` کلیک می‌کند.

## 6.2. چند Taxonomy Filter برای یک Loop Grid

**[documented]** می‌توان بیش از یک Taxonomy Filter widget را به یک Loop Grid متصل کرد تا بازدیدکننده بر اساس چند ویژگی فیلتر کند.

مثال رسمی مقاله:

- Postهایی با Category برابر `How-to`؛
- و Tag برابر `Important`.

**[derived]** این مثال نشان می‌دهد چند Filter می‌توانند به‌طور هم‌زمان دامنه نتیجه را محدود کنند.

**[insufficient_evidence]** مقاله Boolean operator دقیق بین دو Widget مستقل را نام‌گذاری نمی‌کند؛ بنابراین نباید بدون Fixture نتیجه گرفت اتصال چند Widget همیشه `AND`، همیشه `OR` یا قابل تنظیم است.

---

# 7. Query interaction — تعامل با Query

## 7.1. Current Query

**[documented]** Taxonomy Filter در وضعیت فعلی `Current Query` را پشتیبانی نمی‌کند.

**[documented]** در Archive Page، اگر Loop Grid برای Query از Query به‌ارث‌رسیده از Display Conditions صفحه استفاده کند، Filter کار نمی‌کند.

**[documented]** برای استفاده از Taxonomy Filter، تنظیمات Query باید مستقیماً داخل خود `Loop Grid widget` تعریف شوند.

## 7.2. سایر تعامل‌های Query

**[insufficient_evidence]** مقاله موارد زیر را توضیح نمی‌دهد:

- تعامل با `Include` و `Exclude` در Query؛
- تعامل با Author، Date، Order، Offset، Related یا Manual Selection؛
- تقدم Filter بر Query یا برعکس؛
- رفتار با Post Typeهای سفارشی؛
- رفتار با Product Query و Product Taxonomy؛
- رفتار هنگام نبود نتیجه؛
- تعامل با Pagination، Load More یا Infinite Scroll؛
- Query ID یا Hookهای توسعه‌دهندگان؛
- Cache و بازخوانی Query.

---

# 8. Content tab — Layout

## 8.1. `Selected Loop Grid` — Loop Grid انتخاب‌شده

**[documented]** تعیین می‌کند کدام Loop Grid توسط این Filter کنترل شود.

**[insufficient_evidence]** مقاله شرایط فهرست‌شدن Gridها، رفتار Duplicate name، Grid نامعتبر یا حذف Grid متصل‌شده را توضیح نمی‌دهد.

## 8.2. `Taxonomy` — طبقه‌بندی

**[documented]** مقاله انتخاب میان Category و Tag را توضیح می‌دهد.

**[observed]** Dropdown تصویر رسمی گزینه‌های `Categories` و `Tags` را نشان می‌دهد.

### Filter type — نوع فیلتر

**[insufficient_evidence]** در متن و تصاویر بررسی‌شده، کنترل مستقلی با Label دقیق `Filter Type` معرفی نشده است. نزدیک‌ترین کنترل مستند، `Taxonomy` است که نوع Classification را میان Category و Tag انتخاب می‌کند.

**[insufficient_evidence]** Custom Taxonomyها، Product Categories، Product Tags، Hierarchical Custom Taxonomy و Non-hierarchical Custom Taxonomy در این صفحه فهرست نشده‌اند.

## 8.3. `Direction` — جهت

**[documented]** جهت منوی Taxonomy را تعیین می‌کند:

- `Horizontal` — افقی
- `Vertical` — عمودی

**[observed]** مقدار `Horizontal` در تصویر Layout دیده می‌شود.

## 8.4. `Item Alignment` — تراز آیتم‌ها

**[documented]** گزینه‌ها:

| گزینه | ترجمه | شرح مقاله |
|---|---|---|
| `Start` | ابتدا | منو در ابتدای Loop Grid ظاهر می‌شود. |
| `Center` | مرکز | منو در میانه Loop Grid ظاهر می‌شود. |
| `End` | انتها | منو در انتهای Loop Grid ظاهر می‌شود. |
| `Stretch` | کشیده | منو در طول Loop Grid گسترده می‌شود. |

**[insufficient_evidence]** صفحه مشخص نمی‌کند `Start` و `End` در RTL چگونه نگاشت می‌شوند یا `Stretch` عرض خود آیتم‌ها، فاصله بین آن‌ها یا Container را تغییر می‌دهد.

---

# 9. Content tab — Settings

## 9.1. `Filter Logic` — منطق فیلتر

### `Multiple Selection` — انتخاب چندگانه

**[documented]** Toggle انتخاب چند Category را برای بازدیدکننده فعال می‌کند.

**[documented]** وقتی `Multiple Selection` روی `Yes` باشد، Dropdown منطق با دو گزینه ظاهر می‌شود:

- `AND`
- `OR`

### منطق `AND`

**[documented]** فقط آیتم‌هایی نمایش داده می‌شوند که با همه Categoryهای انتخاب‌شده مرتبط باشند.

مثال رسمی:

- `blue`
- `pants`
- نتیجه: آیتم‌های blue pants.

### منطق `OR`

**[documented]** آیتمی نمایش داده می‌شود که حداقل به یکی از Categoryهای انتخاب‌شده مرتبط باشد.

مثال رسمی:

- `blue`
- `pants`
- نتیجه: تمام pants و تمام آیتم‌های blue.

**[insufficient_evidence]** مقاله روشن نمی‌کند:

- این منطق برای Tagها نیز دقیقاً با همان UI فعال است یا مثال فقط Categoryها را پوشش می‌دهد؛
- Default Toggle و Default operator چیست؛
- ترتیب انتخاب‌ها در Query اثر دارد یا نه؛
- امکان Deselect همه انتخاب‌ها چگونه است؛
- محدودیت تعداد انتخاب هم‌زمان وجود دارد یا نه؛
- منطق داخل یک Filter با منطق میان چند Filter widget چگونه ترکیب می‌شود.

## 9.2. `Displayed Elements` — عناصر نمایش‌داده‌شده

**[documented]** این بخش تعیین می‌کند چه آیتم‌هایی در منوی Taxonomy ظاهر شوند.

### `Empty Items` — آیتم‌های خالی

**[documented]** Toggle دارای حالت‌های `Show` و `Hide` برای Category/Tagهای خالی است.

**[documented]** با انتخاب `Hide`، Classification بدون آیتم مرتبط در منو ظاهر نمی‌شود.

مثال رسمی: اگر هیچ Post در Category با نام `Funky` نباشد، Funky نمایش داده نمی‌شود.

**[insufficient_evidence]** رفتار `Show` پس از کلیک روی یک Taxonomy خالی، Disabled state، پیام نتیجه خالی و Count آیتم‌ها مستند نشده‌اند.

### `Taxonomy Children` — فرزندان Taxonomy

**[documented]** Toggle با حالت `Show` یا `Hide` تعیین می‌کند Subcategoryها در منوی Taxonomy نمایش داده شوند یا نه.

**[derived]** این کنترل سطحی از پشتیبانی Hierarchy را نشان می‌دهد، اما فقط نمایش یا عدم نمایش فرزندان را اثبات می‌کند.

**[insufficient_evidence]** مقاله موارد زیر را توضیح نمی‌دهد:

- عمق Hierarchy پشتیبانی‌شده؛
- نمایش Grandchildها؛
- Indentation یا Tree UI؛
- ترتیب Parent و Child؛
- انتخاب Parent و اثر آن بر Postهای Child؛
- Collapse/Expand؛
- رفتار Tagها که معمولاً Hierarchical نیستند؛
- انتخاب هم‌زمان Parent و Child با AND/OR.

### `First Item` — آیتم اول

**[documented]** `First Item` آیتمی برای بازگرداندن نمایش همه Postها است و متن مقاله آن را با عنوان `All` معرفی می‌کند.

**[documented]** Toggle می‌تواند `First Item` را `Show` یا `Hide` کند.

### `First item title` — عنوان آیتم اول

**[documented]** نام پیش‌فرض First Item برابر `All` است و می‌توان آن را در Text Box تغییر داد.

**[observed]** در تصویر خروجی، `All` هم‌زمان با سایر Categoryها در منو دیده می‌شود.

**[insufficient_evidence]** متن مقاله می‌گوید «After filtering, a new menu item, All appears»، اما تصویر All را در خود منوی نمونه نشان می‌دهد. صفحه زمان دقیق ظاهرشدن All در Runtime را به‌شکل سازگار و آزمایش‌پذیر توضیح نمی‌دهد.

**[insufficient_evidence]** ترجمه خودکار، Dynamic Tag، امکان خالی‌کردن Label، HTML مجاز، طول مجاز و رفتار Accessibility عنوان سفارشی مستند نشده‌اند.

### `Number of taxonomies` — تعداد Taxonomyها

**[documented]** تعداد آیتم‌های Taxonomy قابل نمایش در منو را با ورود عدد محدود می‌کند.

مثال رسمی:

- 25 آیتم موجود؛
- مقدار واردشده 4؛
- نتیجه: نمایش 4 آیتم از 25 آیتم.

**[insufficient_evidence]** مقاله مشخص نمی‌کند چهار مورد بر اساس چه Ordering انتخاب می‌شوند، حداقل/حداکثر و Validation فیلد چیست یا `0` و مقدار خالی چه رفتاری دارند.

### `Horizontal Scroll` — اسکرول افقی

**[documented]** وقتی Taxonomy itemها بیش از فضای موجود باشند:

- `Disable` — آیتم‌ها به خط بعد Wrap می‌شوند.
- `Enable` — بازدیدکننده برای مشاهده همه آیتم‌ها باید افقی Scroll کند.

**[insufficient_evidence]** نوع Scrollbar، Drag، Wheel، Touch، RTL، Snap، Keyboard scrolling و Focus visibility مستند نشده‌اند.

---

# 10. Style tab — Items

## 10.1. `Space between items` — فاصله بین آیتم‌ها

**[documented]** Slider فاصله میان متن‌های منوی Taxonomy را تعیین می‌کند.

**[insufficient_evidence]** Unit، دامنه، Default و Responsive بودن آن در متن مقاله مشخص نشده‌اند.

## 10.2. `Typography` — تایپوگرافی

**[documented]** Font متن منوی Taxonomy را تعیین می‌کند؛ مقاله برای جزئیات به صفحه Typography لینک می‌دهد.

**[insufficient_evidence]** فهرست کامل Sub-controlهای Typography در مقاله Taxonomy Filter تکرار نشده است؛ محتوای صفحه فرعی نباید بدون بررسی مستقل به این صفحه نسبت داده شود.

## 10.3. Style states — حالت‌های استایل

**[documented]** سه State معرفی شده‌اند:

| State | ترجمه | زمان کاربرد مستند |
|---|---|---|
| `Normal` | عادی | حالت پیش‌فرض |
| `Hover` | شناور | وقتی Pointer روی آیتم قرار دارد |
| `Active` | فعال | وقتی آیتم انتخاب شده است |

**[documented]** برای هر State می‌توان موارد زیر را تعریف کرد:

- `Text Color` — رنگ متن
- `Text Shadow` — سایه متن
- `Background Type` — نوع پس‌زمینه
- `Border Type` — نوع Border
- `Box Shadow` — سایه Box

## 10.4. سایر کنترل‌های Style

### `Text Color` — رنگ متن

**[documented]** رنگ متن منوی Taxonomy را تعیین می‌کند.

### `Text Shadow` — سایه متن

**[documented]** به متن عمق بصری می‌دهد.

### `Background Type` — نوع پس‌زمینه

**[documented]** برای منوی Taxonomy پس‌زمینه ایجاد می‌کند.

### `Border Type` — نوع Border

**[documented]** به منوی Taxonomy Border اضافه می‌کند.

### `Box Shadow` — سایه Box

**[documented]** به فضای اطراف Menu itemها عمق بصری می‌دهد.

### `Border Radius` — شعاع گوشه

**[documented]** گوشه‌های Border را گرد می‌کند.

### `Padding` — فاصله داخلی

**[documented]** فضای اطراف منوی Taxonomy را اضافه یا کم می‌کند.

**[insufficient_evidence]** مقاله ماتریس دقیق اینکه `Border Radius` و `Padding` برای هر State جدا هستند یا Shared، تمام Unitها، Responsive behavior، Defaultها، Global values و Reset behavior را اعلام نمی‌کند.

---

# 11. Responsive controls

**[observed]** در تصویر رسمی `Content-Tab-Layout-1.png`، Icon دستگاه کنار `Direction` و `Item Alignment` دیده می‌شود. این مشاهده نشان می‌دهد UI تصویر برای این دو کنترل نشانه Responsive دارد.

**[insufficient_evidence]** متن مقاله Responsive controlها را توضیح نمی‌دهد و موارد زیر اثبات نشده‌اند:

- نام Deviceها یا Breakpointها؛
- Inheritance میان Desktop، Tablet و Mobile؛
- Responsive بودن Space between items، Padding یا Typography؛
- Default هر Device؛
- رفتار `Horizontal Scroll` در Breakpointهای مختلف؛
- RTL responsive behavior.

---

# 12. URL و AJAX behavior

## 12.1. AJAX

**[insufficient_evidence]** مقاله نمی‌گوید تغییر Filter با AJAX، Page reload یا روش دیگری انجام می‌شود.

موارد نامشخص:

- Endpoint یا Request type؛
- Loading indicator؛
- Disabled state هنگام Request؛
- Error handling و Retry؛
- Race condition در کلیک‌های سریع؛
- Cache؛
- Custom events یا Hooks؛
- تعامل با Pagination و Infinite Scroll.

## 12.2. URL و History

**[insufficient_evidence]** مقاله موارد زیر را مستند نمی‌کند:

- افزودن Taxonomy selection به Query string یا Fragment؛
- Deep link به حالت فیلترشده؛
- Back/Forward browser history؛
- حفظ انتخاب پس از Refresh؛
- Shareable URL؛
- Canonical URL و SEO؛
- Indexing نتایج فیلترشده.

---

# 13. Accessibility

**[insufficient_evidence]** مقاله Accessibility semantics را مستند نمی‌کند.

موارد نامشخص:

- نوع Element خروجی؛
- `button`، `a` یا Element سفارشی؛
- Keyboard navigation؛
- Focus indicator و Focus management بعد از فیلتر؛
- `aria-pressed`، `aria-selected`، `aria-current` یا Live Region؛
- اعلام تعداد نتایج به Screen Reader؛
- ترتیب Tab؛
- وضعیت Disabled برای آیتم خالی؛
- دسترس‌پذیری Horizontal Scroll؛
- Contrast requirements برای Normal/Hover/Active؛
- Reduced Motion یا Loading announcement.

**[derived]** وجود Stateهای بصری `Hover` و `Active` به‌تنهایی Accessibility behavior را اثبات نمی‌کند.

---

# 14. Excluding categories and tags

**[documented]** مقاله Heading با عنوان `Excluding categories and tags from a filter` دارد.

**[insufficient_evidence]** زیر این Heading در محتوای متنی بازیابی‌شده هیچ دستورالعمل، کنترل یا توضیح صریحی درج نشده و بلافاصله بخش `Taxonomy filter settings` آغاز می‌شود.

بنابراین صفحه روش قابل استنادی برای موارد زیر ارائه نمی‌کند:

- Exclude کردن Category خاص؛
- Exclude کردن Tag خاص؛
- Include-only list؛
- Exclude by ID یا Slug؛
- Exclude children؛
- ارتباط Exclusion با Query settings.

---

# 15. Advanced tab

**[documented]** مقاله `Advanced tab` را در فهرست Tabهای Widget ذکر و به صفحه عمومی Advanced tab لینک می‌دهد.

**[insufficient_evidence]** هیچ Inventory اختصاصی از کنترل‌های Advanced برای Taxonomy Filter در همین مقاله ارائه نشده است. محتوای صفحه عمومی Advanced tab در دامنه این جزوه بررسی نشده و نباید به این Widget نسبت داده شود.

---

# 16. شرایط نمایش کنترل‌ها

| Control/Section | شرط نمایش مستند | وضعیت |
|---|---|---|
| `Selected Loop Grid` | Taxonomy Filter باید همراه Loop Grid استفاده شود | documented |
| `Taxonomy` | پس از انتخاب Grid، Category یا Tag انتخاب می‌شود | documented؛ ترتیب دقیق Enable شدن نامشخص |
| `AND/OR` dropdown | وقتی `Multiple Selection` روی `Yes` باشد | documented |
| `First item title` | First Item قابل تغییر نام است | documented؛ شرط UI دقیق نسبت به Show/Hide نامشخص |
| `Horizontal Scroll` | برای مدیریت اضافه‌شدن Taxonomy itemها توضیح داده شده | documented؛ شرط خودکار ظاهرشدن Control نامشخص |
| State controls | بعد از انتخاب Normal/Hover/Active Style تعریف می‌شود | documented |

**[insufficient_evidence]** مقاله ماتریس کامل Conditional UI را ارائه نمی‌کند؛ از جمله روشن نیست با `First Item: Hide` فیلد Title مخفی، Disabled یا همچنان قابل ویرایش می‌ماند.

---

# 17. مثال‌های کاربردی مستند

## مثال 1: Category واحد

- Taxonomy: `Categories`
- انتخاب بازدیدکننده: `Funky`
- نتیجه: نمایش Postهای مرتبط با Funky
- Reset: کلیک روی `All`

## مثال 2: Multiple Selection با AND

- انتخاب‌ها: `blue` و `pants`
- Logic: `AND`
- نتیجه: فقط blue pants

## مثال 3: Multiple Selection با OR

- انتخاب‌ها: `blue` و `pants`
- Logic: `OR`
- نتیجه: تمام pants و تمام آیتم‌های blue

## مثال 4: چند Widget برای چند مشخصه

- Category: `How-to`
- Tag: `Important`
- هدف مقاله: فیلتر بر اساس چند مشخصه
- Boolean operator دقیق میان Widgetها: insufficient_evidence

## مثال 5: آیتم خالی

- Category: `Funky`
- هیچ Post مرتبطی وجود ندارد
- `Empty Items: Hide`
- نتیجه: Funky در Menu ظاهر نمی‌شود

## مثال 6: محدودیت تعداد

- تعداد Taxonomy itemها: 25
- `Number of taxonomies`: 4
- نتیجه: نمایش 4 آیتم
- Ordering چهار آیتم: insufficient_evidence

---

# 18. تصاویر رسمی و وضعیت مشاهده

| تصویر | وضعیت | مشاهده قابل استناد |
|---|---|---|
| `2023/07/image-3.png` | observed | Selected Loop Grid با Placeholder `Select a widget` |
| `2023/07/image-4.png` | observed | Dropdown Taxonomy با Categories و Tags |
| `2023/07/image-5.png` | observed | منوی افقی All/Funky/Glam/Sexy و نمونه Active بصری |
| `2023/08/Content-Tab-Layout-1.png` | observed | Selected Grid، Taxonomy، Direction، Item Alignment و Device iconها |
| `2023/08/Content-tab-Settings.jpg` | insufficient_evidence | URL استخراج شد، اما تصویر توسط ابزار پژوهش Fetch نشد |
| `2023/08/Style-tab-Items.png` | insufficient_evidence | URL استخراج شد، اما تصویر توسط ابزار پژوهش Fetch نشد |

**[insufficient_evidence]** مسیر Upload تصاویر به پوشه‌های `2023/07` و `2023/08` اشاره دارد، درحالی‌که مقاله در 2026 به‌روزرسانی شده است. صفحه نسخه Elementor یا تاریخ واقعی Capture رابط را اعلام نمی‌کند؛ بنابراین تصاویر نباید نماینده قطعی UI همه نسخه‌های جاری تلقی شوند.

---

# 19. ناسازگاری‌ها و ابهام‌های خود منبع

1. صفحه گاهی نام `Taxonomy widget` و گاهی `Taxonomy Filter` یا `Taxonomy Filter widget` را به‌کار می‌برد.
2. در مرحله ساخت، عبارت «categories or tabs» آمده که با بقیه متن و Dropdown تصویر سازگار نیست؛ تصویر `Tags` را نشان می‌دهد و احتمال خطای ویرایشی وجود دارد.
3. Heading مربوط به Excluding categories/tags بدون محتوای توضیحی قابل بازیابی است.
4. متن می‌گوید `All` «بعد از filtering» ظاهر می‌شود، اما تصویر آن را از قبل در منو نشان می‌دهد.
5. مقاله `Contents tab` و `Content tab` را با نگارش متفاوت به‌کار می‌برد.
6. تصاویر قدیمی‌تر از تاریخ به‌روزرسانی مقاله‌اند و Version stamp ندارند.

این موارد بدون شاهد تکمیلی اصلاح یا تفسیر قطعی نشده‌اند.

---

# 20. پوشش خط‌به‌خط مقاله

| بخش مقاله | پوشش در جزوه |
|---|---|
| معرفی Widget و هدف | بخش 3 |
| Prerequisite | بخش 4 |
| Current Query note | بخش 7 |
| Create a Taxonomy filter | بخش 5 و 6 |
| Multiple Taxonomy Filter widgets | بخش 6.2 |
| Selected Loop Grid | بخش 8.1 |
| Taxonomy | بخش 8.2 |
| Direction | بخش 8.3 |
| Item Alignment | بخش 8.4 |
| Filter Logic / Multiple Selection | بخش 9.1 |
| Empty Items | بخش 9.2 |
| Taxonomy Children | بخش 9.2 |
| First Item / First item title | بخش 9.2 |
| Number of taxonomies | بخش 9.2 |
| Horizontal Scroll | بخش 9.2 |
| Style tab – Items | بخش 10 |
| Normal / Hover / Active | بخش 10.3 |
| Text Color / Shadow / Background / Border / Box Shadow | بخش 10.4 |
| Border Radius / Padding | بخش 10.4 |
| Excluding categories and tags | بخش 14؛ gap ثبت شد |
| Related article links | خارج از دامنه factual این سند |

---

# 21. Evidence gaps نهایی

- نسخه دقیق Elementor Core و Pro و Plan لازم اعلام نشده است.
- URL ورودی با Canonical جاری فهرست رسمی متفاوت است و Redirect history مستند نیست.
- کنترل مستقلی با نام `Filter Type` مستند نشده است.
- Custom Taxonomy و Product Taxonomy در صفحه توضیح داده نشده‌اند.
- Excluding categories/tags Heading دارد اما روش اجرایی ندارد.
- Boolean logic میان چند Filter widget مشخص نشده است.
- Current Query صریحاً پشتیبانی نمی‌شود؛ تعامل با سایر Query controls ناقص است.
- Hierarchy فقط در حد Show/Hide کردن Taxonomy Children مستند شده است.
- Ordering و Validation مربوط به Number of taxonomies نامشخص است.
- URL، Deep Link، Browser History و SEO behavior مستند نشده‌اند.
- AJAX، Loading، Error handling و Hooks مستند نشده‌اند.
- Accessibility، Keyboard، Focus و ARIA مستند نشده‌اند.
- Responsive behavior فقط در دو Device icon تصویر قابل مشاهده است و متن توضیحی ندارد.
- Style defaults، Unitها و Conditional control matrix کامل نیستند.
- دو تصویر Settings و Style توسط ابزار پژوهش Fetch نشدند.
- UI version تصاویر رسمی اعلام نشده است.

---

# 22. جمع‌بندی

صفحه رسمی `Taxonomy Filter widget` یک مرجع نسبتاً کامل برای کنترل‌های Content و Style پایه است و صریحاً اتصال به Loop Grid، Category/Tag، Multiple Selection با AND/OR، Empty Items، Taxonomy Children، First Item، تعداد آیتم‌ها، Horizontal Scroll و Style states را توضیح می‌دهد.

مهم‌ترین محدودیت عملی مستند، عدم پشتیبانی از `Current Query` است. بااین‌حال صفحه برای Runtime behaviorهای فنی مانند AJAX، URL state، Browser history، Accessibility، Focus management، Query precedence و منطق میان چند Filter widget شواهد کافی ارائه نمی‌کند. به همین دلیل وضعیت سند `completed_with_gaps` است.
