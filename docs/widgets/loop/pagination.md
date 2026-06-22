---
id: elementor.help.loop-pagination
title: "Paginate your loop — جزوه جامع صفحه‌بندی Loop Grid"
source_url: "https://elementor.com/help/pagination-for-loop/"
canonical_url: "https://elementor.com/help/paginate-loop/"
source_title: "Paginate your loop"
source_type: official_help
version_scope: "rolling_documentation; exact_elementor_core_and_pro_versions_not_stated"
last_updated: "2025-02-09"
researched_at: "2026-06-22T14:02:20+03:00"
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-009
product_scope:
  - Elementor
  - Loop Grid widget
  - Pagination
source_images:
  - "https://elementor.com/help/wp-content/uploads/2022/01/1-Loop-Grid-options.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/2-click-the-Content-tab.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/Open-pagination-section-1.png"
  - "https://elementor.com/help/wp-content/uploads/2022/01/4-The-Pagination-fropdown-menu.png"
  - "https://elementor.com/help/wp-content/uploads/2022/09/image-7.png"
  - "https://elementor.com/help/wp-content/uploads/2022/09/image-8.png"
  - "https://elementor.com/help/wp-content/uploads/2022/09/image-9.png"
  - "https://elementor.com/help/wp-content/uploads/2023/10/image-10.png"
  - "https://elementor.com/help/wp-content/uploads/2023/10/image-11-1024x157.png"
  - "https://elementor.com/help/wp-content/uploads/2023/10/image-12.png"
  - "https://elementor.com/help/wp-content/uploads/2023/10/image-13.png"
---

# Paginate your loop — جزوه جامع فارسی صفحه‌بندی Loop Grid

> **دامنه این جزوه:** متن و تصاویر تعبیه‌شده در صفحه رسمی Elementor با عنوان `Paginate your loop`. آدرس درخواست‌شده `pagination-for-loop/` بود، اما لینک جاری در فهرست رسمی Widgets به `paginate-loop/` می‌رسد. این جزوه محتوای صفحات فرعی یا مستندات توسعه‌دهندگان را به مقاله اصلی نسبت نمی‌دهد.

## 1. مشخصات منبع

| فیلد | مقدار |
|---|---|
| عنوان جاری مقاله | `Paginate your loop` |
| URL ورودی/ثبت‌شده | <https://elementor.com/help/pagination-for-loop/> |
| URL جاری کشف‌شده از فهرست رسمی | <https://elementor.com/help/paginate-loop/> |
| ناشر | Elementor Knowledge Hub |
| آخرین به‌روزرسانی اعلام‌شده | `February 9, 2025` |
| تاریخ پژوهش | `2026-06-22` |
| نسخه دقیق Elementor Core | در صفحه اعلام نشده |
| نسخه دقیق Elementor Pro | در صفحه اعلام نشده |
| پیش‌نیاز صریح Elementor Pro | در این صفحه اعلام نشده |
| وضعیت پوشش | `completed_with_gaps` |

### وضعیت URL

**[observed]** فهرست رسمی Widgets، مقاله `Paginate your loop` را با مسیر `https://elementor.com/help/paginate-loop/` معرفی می‌کند.

**[insufficient_evidence]** این بررسی ثابت نمی‌کند که URL قدیمی `pagination-for-loop/` در همه شرایط HTTP redirect دائمی، موقت یا canonical redirect دارد؛ تاریخچه تغییر مسیر نیز در مقاله مستند نشده است.

---

## 2. قرارداد وضعیت شواهد

- **documented:** مطلب به‌صورت صریح در متن رسمی مقاله آمده است.
- **observed:** مطلب مستقیماً در تصویر رسمی قابل مشاهده است، اما متن آن را به‌عنوان رفتار یا Default رسمی تعریف نکرده است.
- **derived:** برداشت محدود و قابل ردیابی از متن یا تصویر است و نباید به API contract یا حقیقت مستقل محصول ارتقا پیدا کند.
- **insufficient_evidence:** صفحه برای نتیجه‌گیری دقیق اطلاعات کافی ارائه نمی‌کند.

---

## 3. خلاصه اجرایی

**[documented]** تعداد آیتم‌هایی که در یک صفحه Loop نمایش داده می‌شوند به Layout بستگی دارد. وقتی تعداد آیتم‌ها از ظرفیت یک صفحه بیشتر باشد، باید یک Pagination style تعیین شود. حالت پیش‌فرض Loopها بدون Pagination است و فقط یک صفحه از آیتم‌ها نمایش داده می‌شود.

صفحه شش مقدار برای Dropdown صفحه‌بندی نام می‌برد:

1. `None` — بدون صفحه‌بندی
2. `Numbers` — شماره صفحات
3. `Previous/Next` — قبلی/بعدی
4. `Numbers + Previous/Next` — شماره‌ها همراه قبلی/بعدی
5. `Load on click` — بارگذاری با کلیک
6. `Infinite Scroll` — اسکرول بی‌نهایت

**[documented]** مقاله این سبک‌ها را در دو خانواده مفهومی قرار می‌دهد:

- **Book-type pagination styles:** جابه‌جایی صفحه‌به‌صفحه در محور افقی/مفهومی؛ کاربر ورق می‌زند یا صفحه مشخصی را انتخاب می‌کند.
- **Scrolling pagination:** مشاهده محتوا با حرکت عمودی؛ صفحه بعد با کلیک یا به‌صورت پیوسته اضافه می‌شود.

---

## 4. مسیر دسترسی به تنظیمات Pagination

**[documented]** روند مقاله:

1. `Loop Grid` را انتخاب کنید.
2. گزینه‌های Loop Grid در پنل سمت راست ظاهر می‌شوند.
3. به تب `Content` — محتوا بروید.
4. بخش `Pagination` — صفحه‌بندی را باز کنید.
5. از Dropdown با عنوان `Pagination`، سبک موردنظر را انتخاب کنید.
6. بر اساس سبک انتخاب‌شده، گزینه‌های وابسته ظاهر می‌شوند.

**[derived]** وجود گزینه‌های وابسته یعنی UI به‌صورت شرطی تغییر می‌کند؛ بااین‌حال مقاله ماتریس کامل «هر سبک ← تمام کنترل‌های ظاهرشونده» را ارائه نمی‌کند.

---

# 5. Pagination styles — سبک‌های صفحه‌بندی

## 5.1. `None` — بدون صفحه‌بندی

**[documented]** مقدار پیش‌فرض است و فقط یک صفحه از آیتم‌ها نمایش داده می‌شود.

### شرایط نمایش و نتیجه

- Pagination navigation نمایش داده نمی‌شود.
- آیتم‌های خارج از صفحه اول از طریق Pagination همین Loop قابل دسترسی نیستند.

**[insufficient_evidence]** مقاله مشخص نمی‌کند آیا آیتم‌های بیشتر به‌طور کامل از Query حذف می‌شوند، فقط در خروجی UI پنهان می‌مانند یا توسط تنظیم دیگری قابل بازیابی‌اند.

---

## 5.2. `Numbers` — شماره صفحات

**[documented]** شماره تمام صفحات Loop نمایش داده می‌شود و بازدیدکننده می‌تواند صفحه مشخصی را انتخاب کند.

### کنترل‌های صریحاً مرتبط

| Control | ترجمه | شرح مستند |
|---|---|---|
| `Page Limit` | محدودیت تعداد صفحات | تعداد صفحاتی را که بازدیدکننده می‌تواند به آن‌ها دسترسی داشته باشد محدود می‌کند. |
| `Shorten` | کوتاه‌سازی فهرست شماره‌ها | تعداد شماره‌های فهرست‌شده را کاهش می‌دهد. |
| `Alignment` | تراز | گزینه‌های `Left`، `Centered` و `Right` در مقاله آمده‌اند. |
| `Page Load` | روش بارگذاری صفحه | برای سبک‌های شماره‌ای می‌تواند `Page Reload` یا `AJAX` باشد. |

**[observed]** تصویر نمونه پنج شماره `1 2 3 4 5` را نشان می‌دهد. شماره `1` با رنگ تیره و شماره‌های بعدی با رنگ صورتی نمایش داده شده‌اند و زیر هر شماره خط وجود دارد.

**[insufficient_evidence]** رنگ، Typography، Underline، فاصله و حالت Active موجود در تصویر، Default رسمی یا Style contract اعلام نشده‌اند.

---

## 5.3. `Previous/Next` — قبلی/بعدی

**[documented]** دکمه‌ها یا لینک‌های `Previous` و `Next` باعث می‌شوند بازدیدکننده ورودی‌ها را یک صفحه در هر مرحله مرور کند.

### Labels — برچسب‌ها

**[documented]** برچسب‌های Previous و Next قابل سفارشی‌سازی‌اند.

**[insufficient_evidence]** مقاله موارد زیر را اعلام نمی‌کند:

- نام دقیق فیلدهای ویرایش Label در UI؛
- مقدار Default قابل اتکا برای تمام زبان‌ها؛
- امکان خالی‌کردن Label؛
- ترجمه خودکار یا ارتباط با زبان سایت؛
- امکان افزودن Icon به Previous/Next؛
- رفتار دکمه Previous در صفحه اول و Next در صفحه آخر؛
- اینکه کنترل انتهایی حذف، مخفی یا Disabled می‌شود.

**[observed]** تصویر نمونه دو Label انگلیسی `Previous` و `Next` را با Underline نشان می‌دهد؛ Previous تیره و Next صورتی است.

**[insufficient_evidence]** رنگ و Underline تصویر فقط Example state هستند و به‌عنوان تنظیم پیش‌فرض مستند نشده‌اند.

---

## 5.4. `Numbers + Previous/Next` — شماره صفحات همراه قبلی/بعدی

**[documented]** بازدیدکننده هم می‌تواند مستقیماً به یک شماره صفحه برود و هم صفحه قبلی یا بعدی را انتخاب کند.

### کنترل‌های قابل انتساب از متن

- `Shorten` فقط برای `Numbers` و `Numbers + Previous/Next` صریحاً مرتبط اعلام شده است.
- `Page Load` برای این سبک می‌تواند `Page Reload` یا `AJAX` باشد.
- قابلیت سفارشی‌سازی Previous/Next labels در بخش Previous/Next توضیح داده شده است؛ مقاله به‌طور مستقل تکرار نمی‌کند که همان فیلدها در حالت ترکیبی چگونه ظاهر می‌شوند.

**[derived]** چون نام سبک شامل Previous/Next است، احتمالاً Labels مرتبط نیز در UI حضور دارند؛ اما مقاله ماتریس کنترل‌های حالت ترکیبی را کامل ارائه نکرده و این مورد نباید بدون مشاهده UI به‌عنوان قرارداد قطعی ثبت شود.

---

## 5.5. `Load on click` — بارگذاری با کلیک

**[documented]** این سبک برای مرور عمودی و صفحه‌به‌صفحه است:

1. ابتدا یک صفحه محتوا نمایش داده می‌شود.
2. یک دکمه قابل سفارشی‌سازی در پایین محتوا قرار می‌گیرد.
3. با کلیک روی دکمه، صفحه بعدی در خروجی درج می‌شود.
4. محتوای صفحه قبلی همچنان قابل مشاهده باقی می‌ماند.

### کنترل‌های صریح مقاله

| Control | ترجمه | رفتار مستند |
|---|---|---|
| Button text | متن دکمه | متن دکمه قابل تغییر است. |
| Alignment | تراز دکمه | تراز دکمه قابل تغییر است. |
| Icon | آیکون | می‌توان به دکمه آیکون افزود. |
| Icon spacing | فاصله آیکون | فاصله آیکون قابل سفارشی‌سازی است. |
| `Button ID` | شناسه دکمه | مقاله می‌گوید امکان ذخیره دکمه برای استفاده مجدد را فراهم می‌کند. |
| `No More Posts Message` | پیام پایان محتوا | پیام سفارشی هنگام رسیدن به انتهای فهرست نمایش داده می‌شود. |

### نکته درباره `Button ID`

**[documented]** متن مقاله `Button ID` را به امکان ذخیره دکمه برای reuse مرتبط می‌کند.

**[insufficient_evidence]** مقاله توضیح نمی‌دهد:

- Button ID دقیقاً در DOM، Saved Style، CSS selector یا سیستم دیگری چگونه مصرف می‌شود؛
- قواعد مجاز برای مقدار ID چیست؛
- یکتایی ID چگونه کنترل می‌شود؛
- reuse در همان صفحه، سایت یا Template چگونه انجام می‌شود.

### تصویر نمونه

**[observed]** تصویر رسمی سه کارت نوشته را در یک ردیف نشان می‌دهد و یک دکمه مشکی `LOAD MORE` تقریباً در مرکز پایین Loop قرار دارد.

**[insufficient_evidence]** متن `LOAD MORE`، رنگ مشکی، اندازه، مرکز بودن و حروف بزرگ Default رسمی اعلام نشده‌اند.

---

## 5.6. `Infinite Scroll` — اسکرول بی‌نهایت

**[documented]** با پایین‌رفتن پیوسته بازدیدکننده، آیتم‌های جدید به فهرست اضافه می‌شوند. مقاله این تجربه را seamless‌تر توصیف می‌کند، اما هشدار می‌دهد که حرکت کاربر ممکن است هنگام انتظار برای بارگذاری آیتم‌های جدید قطع یا مختل شود.

### کنترل‌های صریح مقاله

| Control | ترجمه | رفتار مستند |
|---|---|---|
| Spinner/loading icon | آیکون بارگذاری/Spinner | هنگام بارگذاری آیتم‌های جدید نمایش داده می‌شود و قابل سفارشی‌سازی است. |
| `No More Posts Message` | پیام پایان محتوا | هنگام رسیدن به انتهای فهرست، پیام سفارشی نمایش داده می‌شود. |

**[insufficient_evidence]** مقاله مشخص نمی‌کند:

- Trigger distance یا نقطه فعال‌شدن بارگذاری چقدر است؛
- Intersection Observer یا روش فنی دیگری استفاده می‌شود؛
- بارگذاری در صورت توقف شبکه چگونه Retry می‌شود؛
- Spinner از کدام Icon library انتخاب می‌شود؛
- اندازه، رنگ، Animation speed یا Position آیکون چه کنترل‌هایی دارند؛
- Infinite Scroll چگونه برای Keyboard-only و Screen Reader users قابل کنترل است؛
- آیا گزینه توقف یا Load manually وجود دارد.

---

# 6. `Page Limit` — محدودیت تعداد صفحات

**[documented]** واردکردن مقدار Page Limit اختیاری است و حداکثر تعداد صفحات Loop را مشخص می‌کند.

### معنای دقیق قابل اتکا

- این مقدار سقف تعداد صفحات قابل ارائه را تعیین می‌کند.
- مقاله در معرفی `Numbers` صریحاً Page Limit را به محدودکردن صفحات قابل دسترسی برای بازدیدکننده مرتبط می‌کند.

**[insufficient_evidence]** صفحه اعلام نمی‌کند:

- Page Limit برای دقیقاً کدام‌یک از شش Pagination style نمایش داده می‌شود؛
- مقدار خالی، صفر، منفی، اعشاری یا بزرگ چگونه اعتبارسنجی می‌شود؛
- Page Limit بر Query count، SQL limit، URLهای قابل بازشدن یا فقط Navigation UI اثر می‌گذارد؛
- مقدار Default چیست؛
- وقتی تعداد واقعی صفحات کمتر از Limit است چه UI اضافه‌ای نمایش داده می‌شود؛
- وقتی کاربر URL صفحه‌ای بالاتر از Limit را مستقیماً باز کند چه رخ می‌دهد.

---

# 7. `Shorten` — کوتاه‌سازی شماره صفحات

## شرایط فعال‌بودن

**[documented]** Shorten فقط برای این سبک‌ها مرتبط است:

- `Numbers`
- `Numbers + Previous/Next`

**[documented]** مقاله سناریوی Loop Grid با بیش از چهار صفحه را مطرح می‌کند. برای محدودکردن شماره‌های نمایشی، Toggle با عنوان `Shorten` روی `Yes` قرار می‌گیرد.

## خروجی مستند

**[documented]** فقط چهار شماره نمایش داده می‌شوند:

1. صفحه جاری؛
2. دو صفحه بعدی؛
3. آخرین صفحه.

### مثال منطقی محدود

**[derived]** اگر صفحه جاری `3` و آخرین صفحه `10` باشد، الگوی توصیف‌شده می‌تواند `3، 4، 5، 10` باشد. این مثال در مقاله نیامده و فقط تبدیل مستقیم قاعده متنی به نمونه است.

**[insufficient_evidence]** رفتار Shorten در وضعیت‌های مرزی مستند نیست، از جمله:

- صفحه اول، دوم یا نزدیک انتهای فهرست؛
- نمایش یا عدم نمایش Ellipsis؛
- نمایش صفحات قبلی صفحه جاری؛
- نحوه تعامل با RTL؛
- رفتار در کمتر یا مساوی چهار صفحه؛
- تعامل دقیق با `Page Limit`.

---

# 8. Alignment — تراز صفحه‌بندی

**[documented]** سه مقدار در مقاله نام برده شده‌اند:

- `Left` — چپ
- `Centered` — وسط‌چین
- `Right` — راست

مقاله می‌گوید Pagination را می‌توان در سمت راست، مرکز یا سمت چپ Loop نمایش داد.

**[insufficient_evidence]** صفحه روشن نمی‌کند:

- Alignment برای تمام سبک‌هاست یا فقط سبک‌های خاص؛
- تراز نسبت به خود Widget، Container، Grid track یا Viewport محاسبه می‌شود؛
- گزینه Responsive است یا نه؛
- در RTL معنای Left/Right فیزیکی است یا Logical start/end؛
- تراز Spinner و `No More Posts Message` جداگانه تنظیم می‌شود یا خیر.

---

# 9. Labels، Icons و پیام‌ها

## 9.1. Previous/Next labels

**[documented]** متن دکمه‌ها/لینک‌های Previous و Next قابل سفارشی‌سازی است.

## 9.2. Load on click button

**[documented]** موارد قابل تغییر:

- متن دکمه؛
- تراز دکمه؛
- افزودن Icon؛
- Icon spacing؛
- `Button ID`؛
- `No More Posts Message`.

## 9.3. Infinite Scroll indicator

**[documented]** Spinner icon قابل تغییر است و `No More Posts Message` قابل سفارشی‌سازی است.

## 9.4. موارد نامستند

**[insufficient_evidence]** صفحه اطلاعاتی درباره موارد زیر ندارد:

- Icon position قبل یا بعد از Label؛
- Icon size، color، rotation یا animation؛
- Typography و color برچسب‌ها؛
- Normal، Hover، Focus، Active و Disabled states؛
- ترجمه یا Localization پیام‌ها؛
- امکان استفاده از HTML در Label یا Message؛
- Sanitization و محدودیت طول؛
- Empty-state جدا از No More Posts Message.

---

# 10. Page load method — روش بارگذاری صفحه

## دامنه نمایش کنترل

**[documented]** انتخاب روش بارگذاری فقط برای این سبک‌ها مرتبط است:

- `Numbers`
- `Previous/Next`
- `Numbers + Previous/Next`

## 10.1. `Page Reload` — بارگذاری مجدد کامل صفحه

**[documented]** با تغییر صفحه Loop، کل Webpage مجدداً بارگذاری می‌شود.

## 10.2. `AJAX` — بارگذاری فقط Loop Grid

**[documented]** فقط Widget مربوط به Loop Grid مجدداً بارگذاری می‌شود و کل صفحه Reload نمی‌شود.

## دامنه دقیق AJAX که مقاله اثبات می‌کند

مقاله فقط تفاوت Scope بارگذاری را اثبات می‌کند:

| Method | بخش Reloadشونده |
|---|---|
| `Page Reload` | کل صفحه وب |
| `AJAX` | فقط Loop Grid widget |

**[insufficient_evidence]** مقاله درباره جزئیات زیر سکوت دارد:

- Endpoint و HTTP method؛
- Request parameters و Response schema؛
- Loading state، error state و Retry؛
- Cache behavior؛
- حفظ Scroll position؛
- Focus management بعد از بارگذاری؛
- اجرای Scriptهای آیتم‌های تازه؛
- Eventها یا Hookهای JavaScript/PHP؛
- تعامل با Browser history؛
- SEO و crawlability؛
- رفتار با چند Loop Grid و Queryهای متفاوت؛
- لغو Request قبلی در کلیک‌های سریع.

**[derived]** `Load on click` و `Infinite Scroll` بدون ترک صفحه، آیتم‌های تازه را اضافه می‌کنند؛ بنابراین نوعی بارگذاری پویا لازم است. بااین‌حال مقاله آن‌ها را صریحاً زیر کنترل `AJAX` قرار نمی‌دهد و نباید نام پروتکل یا API داخلی برای آن‌ها فرض شود.

---

# 11. URL behavior — رفتار URL

**[insufficient_evidence]** مقاله هیچ قرارداد صریحی برای URL ارائه نمی‌کند. موارد نامشخص:

- نام Query parameter شماره صفحه؛
- تغییر URL در `AJAX`؛
- عدم تغییر URL در `Load on click` یا `Infinite Scroll`؛
- استفاده از `history.pushState` یا `replaceState`؛
- Back/Forward browser navigation؛
- Deep linking به یک صفحه Loop؛
- Canonical URL و SEO؛
- URL مستقل برای چند Loop Grid در یک صفحه؛
- حفظ صفحه انتخاب‌شده پس از Refresh؛
- Shareable بودن وضعیت Pagination.

**[derived]** در حالت `Page Reload` احتمال تغییر Navigation state مرورگر وجود دارد، اما مقاله شکل URL یا تضمین Shareable بودن آن را اعلام نمی‌کند؛ بنابراین هیچ الگوی URL نباید از این صفحه استخراج شود.

---

# 12. `Individual Pagination` — صفحه‌بندی مستقل Loop Gridها

## رفتار پیش‌فرض

**[documented]** وقتی چند Loop Grid در یک صفحه وجود دارند، به‌طور پیش‌فرض همه Loopها به همان شماره صفحه Refresh می‌شوند.

### مثال رسمی مقاله

- یک Loop شامل خبرها؛
- Loop دیگر شامل خبرهای ورزشی؛
- با رفتن بازدیدکننده به صفحه دوم Loop مربوط به سیاست، Loop ورزشی نیز خودکار به صفحه دوم Refresh می‌شود.

> در متن مثال، نام‌گذاری اولیه «news stories» و سپس «politics loop» یک ناهماهنگی نگارشی دارد؛ مفهوم اصلی، همگام‌بودن شماره صفحه چند Loop است.

## فعال‌سازی استقلال

**[documented]** Toggle با عنوان `Individual Pagination` را روی `On` قرار دهید تا Loop Gridهای یک صفحه به‌طور مستقل Refresh شوند.

## هشدار سازگاری

**[documented]** تمام Loop Gridهای موجود در یک صفحه باید مقدار یکسانی برای `Individual Pagination` داشته باشند.

**[insufficient_evidence]** مقاله مشخص نمی‌کند:

- اگر تنظیم‌ها متفاوت باشند دقیقاً چه خطا یا رفتار ناپایداری رخ می‌دهد؛
- این تنظیم برای کدام Pagination styles قابل استفاده است؛
- استقلال شامل URL parameter، AJAX request و Browser history نیز می‌شود یا فقط Refresh state؛
- Loop Carousel یا Widgetهای Query-based دیگر مشمول این قانون هستند یا خیر؛
- Loopهای Nested چگونه رفتار می‌کنند.

---

# 13. شرایط نمایش کنترل‌ها

| کنترل/رفتار | شرط صریح در مقاله | وضعیت شواهد |
|---|---|---|
| نیاز به Pagination | تعداد آیتم‌ها از ظرفیت یک صفحه بیشتر باشد | documented |
| `None` | حالت پیش‌فرض | documented |
| گزینه‌های وابسته به Style | پس از انتخاب Style ظاهر می‌شوند | documented |
| `Shorten` | فقط `Numbers` یا `Numbers + Previous/Next` | documented |
| منطق بیش از چهار صفحه برای Shorten | مقاله این سناریو را شرط کاربرد معرفی می‌کند | documented |
| `Page Load` | فقط `Numbers`، `Previous/Next` یا حالت ترکیبی | documented |
| Previous/Next labels | در سبک Previous/Next قابل سفارشی‌سازی | documented |
| Load button controls | در `Load on click` | documented |
| Spinner controls | در `Infinite Scroll` | documented |
| `No More Posts Message` | برای Load on click و Infinite Scroll | documented |
| `Individual Pagination` | وجود بیش از یک Loop Grid در یک صفحه، کاربرد آن را معنادار می‌کند | documented + derived |
| Responsive controls | هیچ شرطی ارائه نشده | insufficient_evidence |
| Style-tab controls | هیچ ماتریس یا Section مستقلی ارائه نشده | insufficient_evidence |

---

# 14. Accessibility — دسترس‌پذیری

**[insufficient_evidence]** مقاله هیچ توضیح صریحی درباره Accessibility صفحه‌بندی ارائه نمی‌کند، از جمله:

- استفاده از عنصر `nav` یا Landmark؛
- `aria-label` برای Pagination؛
- `aria-current="page"` برای شماره فعال؛
- Accessible name برای Icon-only controls؛
- ترتیب Tab و Keyboard activation؛
- Focus visibility؛
- انتقال Focus پس از AJAX؛
- اعلام محتوای تازه با `aria-live`؛
- اعلام Loading و پایان محتوا برای Screen Reader؛
- Skip link یا راه خروج از Infinite Scroll؛
- Reduced motion برای Spinner؛
- Contrast و اندازه Target؛
- رفتار RTL و زبان Labels؛
- تطابق با WCAG.

**[derived]** سفارشی‌بودن Labels و `No More Posts Message` می‌تواند برای وضوح متن مفید باشد، اما صفحه هیچ تضمین Accessibility یا دستورالعمل نگارشی ارائه نمی‌کند.

---

# 15. Responsive controls — کنترل‌های واکنش‌گرا

**[insufficient_evidence]** متن مقاله:

- هیچ کنترل دارای Device icon را معرفی نمی‌کند؛
- Breakpointهای Desktop، Tablet یا Mobile را نام نمی‌برد؛
- برای Alignment، Page Limit، Shorten، Labels، Icon spacing یا Spinner مقدار Per-device تعریف نمی‌کند؛
- ارث‌بری Responsive یا تغییر نوع Pagination بر اساس Device را توضیح نمی‌دهد.

چند Screenshot تنظیمات Editor در صفحه وجود دارد، اما تصاویر پنل اولیه و تصاویر کنترل‌های سال 2023 در ابزار پژوهش با Cache miss قابل مشاهده نبودند؛ بنابراین از آن‌ها ادعای `observed` درباره Device icons استخراج نشده است.

---

# 16. Style controls — کنترل‌های ظاهری

## کنترل‌های ظاهری که متن صریحاً نام می‌برد

- Alignment عمومی Pagination؛
- Previous/Next label text؛
- Load on click button text؛
- Load button alignment؛
- افزودن Icon؛
- Icon spacing؛
- Spinner icon؛
- No More Posts Message text.

## کنترل‌های Style که در مقاله مستند نشده‌اند

**[insufficient_evidence]** صفحه فهرست مستقلی از کنترل‌های تب `Style` ارائه نمی‌کند و موارد زیر را توضیح نمی‌دهد:

- Text color و Link color؛
- Active color؛
- Hover/Focus color؛
- Typography؛
- Space between numbers؛
- Gap میان Previous/Next و Numbers؛
- Border، Border radius و Background؛
- Padding و Margin؛
- Button size؛
- Spinner size و color؛
- Message typography؛
- Transition؛
- Normal/Hover/Active/Disabled state controls؛
- Responsive style controls.

سه تصویر قابل مشاهده فقط نمونه خروجی هستند و برای استخراج Default یا Inventory تنظیمات Style کافی نیستند.

---

# 17. تصاویر و شواهد مشاهده‌ای

## 17.1. Number pagination example

![نمونه Numbers pagination](https://elementor.com/help/wp-content/uploads/2022/09/image-7.png)

**[observed]** پنج شماره، رنگ متمایز صفحه اول و Underline زیر اعداد دیده می‌شود.

## 17.2. Previous/Next example

![نمونه Previous و Next](https://elementor.com/help/wp-content/uploads/2022/09/image-8.png)

**[observed]** دو Label انگلیسی و Underline دیده می‌شود.

## 17.3. Load on click example

![نمونه Load on click](https://elementor.com/help/wp-content/uploads/2022/09/image-9.png)

**[observed]** سه کارت نوشته و یک دکمه `LOAD MORE` در پایین Loop دیده می‌شود.

## 17.4. تصاویر غیرقابل مشاهده در ابزار پژوهش

URL تصاویر استخراج شد، اما Fetch تصویری آن‌ها با Cache miss شکست خورد:

- `1-Loop-Grid-options.png`
- `2-click-the-Content-tab.png`
- `Open-pagination-section-1.png`
- `4-The-Pagination-fropdown-menu.png`
- `image-10.png`
- `image-11-1024x157.png`
- `image-12.png`
- `image-13.png`
- تصویر Alignment که در صفحه از دامنه Googleusercontent بارگذاری شده است.

بنابراین جزئیات UI داخل این تصاویر در این جزوه به‌عنوان `observed` ثبت نشده‌اند.

---

# 18. پوشش خط‌به‌خط مقاله

| ترتیب مطلب منبع | نتیجه ثبت‌شده در جزوه | وضعیت |
|---:|---|---|
| مقدمه: Layout تعداد آیتم هر صفحه را تعیین می‌کند | بخش 3 | documented |
| نیاز به Pagination در صورت وجود آیتم‌های بیشتر | بخش 3 و 13 | documented |
| Default بدون Pagination و نمایش یک صفحه | بخش 3 و 5.1 | documented |
| انتخاب Loop Grid و پنل راست | بخش 4 | documented |
| رفتن به Content tab | بخش 4 | documented |
| بازکردن Pagination area | بخش 4 | documented |
| انتخاب Style از Dropdown | بخش 4 | documented |
| ظهور گزینه‌های وابسته به Style | بخش 4 | documented |
| تقسیم سبک‌ها به Book-type و Scrolling | بخش 3 | documented |
| `None` | بخش 5.1 | documented |
| `Numbers` | بخش 5.2 | documented + observed |
| `Page Limit` در Numbers | بخش 5.2 و 6 | documented |
| `Shorten` در Numbers | بخش 5.2 و 7 | documented |
| `Previous/Next` | بخش 5.3 | documented + observed |
| سفارشی‌سازی Labels | بخش 5.3 و 9 | documented |
| `Numbers + Previous/Next` | بخش 5.4 | documented |
| `Load on click` و حفظ صفحات قبلی | بخش 5.5 | documented |
| Button text و alignment | بخش 5.5 و 9 | documented |
| Icon و icon spacing | بخش 5.5 و 9 | documented |
| `Button ID` | بخش 5.5 | documented + gap |
| `No More Posts Message` برای Load on click | بخش 5.5 و 9 | documented |
| `Infinite Scroll` | بخش 5.6 | documented |
| وقفه احتمالی هنگام Loading | بخش 5.6 | documented |
| Spinner icon | بخش 5.6 و 9 | documented |
| `No More Posts Message` برای Infinite Scroll | بخش 5.6 و 9 | documented |
| Page Limit اختیاری | بخش 6 | documented |
| Shorten فقط در دو سبک شماره‌ای | بخش 7 | documented |
| شرط بیش از چهار صفحه | بخش 7 | documented |
| Toggle Shorten = Yes | بخش 7 | documented |
| نمایش current + next two + last | بخش 7 | documented |
| Alignment: Left/Centered/Right | بخش 8 | documented |
| Page Load فقط برای سه سبک Book-type | بخش 10 | documented |
| `Page Reload` | بخش 10 | documented |
| `AJAX` | بخش 10 | documented |
| رفتار همگام چند Loop در Default | بخش 12 | documented |
| `Individual Pagination` = On | بخش 12 | documented |
| الزام یکسان‌بودن تنظیم تمام Loopها | بخش 12 | documented |

---

# 19. شکاف‌های شواهد

```yaml
evidence_gaps:
  - exact Elementor Core and Pro versions are not stated
  - Elementor Pro prerequisite is not explicitly stated
  - the requested URL differs from the current official index URL and redirect history is not documented
  - the full conditional control matrix for every pagination style is not provided
  - Page Limit applicability and validation rules are incomplete
  - Shorten edge cases, ellipsis behavior and RTL behavior are not documented
  - Previous and Next endpoint behavior and disabled states are not documented
  - Button ID semantics and reuse mechanism are unclear
  - AJAX endpoint, hooks, loading states, error handling, focus management and history behavior are not documented
  - URL parameters, deep linking, browser history and SEO behavior are not documented
  - accessibility semantics and keyboard or screen-reader behavior are not documented
  - responsive controls and breakpoint behavior are not documented
  - the Style tab inventory and visual states are not documented
  - most editor screenshots could not be fetched visually by the research tool
```

---

# 20. نتیجه نهایی

**[documented]** صفحه رسمی، Inventory اصلی Pagination types و Workflow عمومی تنظیم آن‌ها را به‌خوبی مشخص می‌کند. همچنین Page Limit، Shorten، Alignment، دو روش Page Load و Individual Pagination را معرفی می‌کند.

**[completed_with_gaps]** برای ساخت یک قرارداد فنی کامل هنوز شواهد کافی درباره URL، AJAX lifecycle، Accessibility، Responsive controls، Style controls، Defaults، RTL و Edge caseها وجود ندارد. این موارد نباید بر اساس حافظه مدل یا رفتار نسخه‌های دیگر Elementor تکمیل شوند.
