---
id: elementor.help.svg-element
title: SVG element
source_url: https://elementor.com/help/svg-element/
source_type: official_help
version_scope: rolling_documentation
last_updated: 2025-07-01
researched_at: 2026-06-23T01:04:00+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-020
---

# جزوه جامع SVG element در Elementor Editor V4

## 1. مشخصات منبع و دامنه سند

- **شناسه مرحله:** `KB-020`
- **موضوع:** `SVG element`
- **منبع رسمی:** `https://elementor.com/help/svg-element/`
- **نوع منبع:** مستند رسمی Elementor Help Center
- **دامنه نسخه‌ای:** `rolling_documentation`
- **آخرین به‌روزرسانی اعلام‌شده در صفحه:** `July 1, 2025`
- **مسیر ذخیره:** `docs/elements/v4/svg.md`
- **وضعیت شواهد:** `completed_with_gaps`

این سند فقط بر اساس صفحه رسمی `SVG element` ساخته شده است. هر چیزی که در خود این صفحه صریحاً نیامده، با وضعیت `insufficient_evidence` ثبت شده است؛ محتوای صفحات لینک‌شده مانند `Adding images and icons`، `Create a Grid container`، `Layout`، `Spacing`، `Size`، `Position`، `Typography`، `Background`، `Border` و `Effects` بدون بررسی مستقل به این سند نسبت داده نشده است.

## 2. خلاصه اجرایی

صفحه رسمی، `SVG element` را به‌عنوان عنصری در مسیر `Help Center > Build with the Editor > Editor V4` معرفی می‌کند. SVG مخفف `Scalable Vector Graphics` است و در صفحه به‌عنوان قالب تصویر XML-based برای ساخت گرافیک‌های برداری دوبعدی توضیح داده شده است. طبق متن رسمی، گرافیک‌های SVG بدون افت کیفیت scale می‌شوند و برای website graphics، icons و illustrations مناسب‌اند.

در این صفحه، Elementor می‌گوید `SVG widget` اجازه می‌دهد گرافیک‌های SVG را به‌عنوان یک عنصر جداگانه داخل صفحه قرار دهید. صفحه همچنین یک سناریوی رایج برای ساخت call to action section با SVG illustrations به‌عنوان icon ارائه می‌کند و دو مورد استفاده دیگر را نام می‌برد: `Infographs` و `Simple lightweight images that allow your page to load more quickly`.

## 3. وضعیت شواهد

| حوزه | وضعیت | توضیح |
|---|---|---|
| وجود صفحه در Editor V4 | documented | breadcrumb صفحه شامل `Editor V4` است. |
| تعریف SVG | documented | SVG به‌عنوان XML-based image format برای two-dimensional vector graphics تعریف شده است. |
| مقیاس‌پذیری بدون افت کیفیت | documented | صفحه می‌گوید SVG graphics can be scaled without losing quality. |
| کاربرد برای icons و illustrations | documented | در متن رسمی آمده است. |
| افزودن عنصر از دکمه `+` | documented | در بخش Add the element to the canvas آمده است. |
| حذف عنصر با Delete key | documented | در بخش Delete the element آمده است. |
| افزودن SVG از فیلد SVG/image field | documented | در step-by-step و General tab آمده است. |
| Link | documented | صفحه می‌گوید با plus sign لینک وارد می‌شود و کلیک روی SVG لینک را باز می‌کند. |
| `Open in a new tab` | documented | در مثال step-by-step به‌عنوان toggle اختیاری آمده است. |
| `ID` | documented | صفحه می‌گوید برای tag کردن element و لینک دادن به همان element استفاده می‌شود. |
| Style categories | documented | فقط نام دسته‌های Layout, Spacing, Size, Position, Typography, Background, Border, Effects آمده است. |
| رنگ SVG | documented | صفحه شرط خاصی برای رنگ‌پذیری SVG ذکر می‌کند. |
| امنیت / sanitization | insufficient_evidence | صفحه درباره sanitization یا ریسک امنیتی SVG توضیح صریح ندارد. |
| viewBox، width/height، aspect ratio، stroke | insufficient_evidence | صفحه درباره این جزئیات SVG توضیح صریح ندارد. |
| responsive controls | insufficient_evidence | صفحه جزئیات responsive را بیان نمی‌کند. |
| dynamic data | insufficient_evidence | صفحه dynamic data را برای SVG element مستند نمی‌کند. |
| accessibility و keyboard/focus behavior | insufficient_evidence | صفحه رفتار accessibility یا focus را توضیح نمی‌دهد. |
| runtime و markup خروجی | insufficient_evidence | صفحه markup، frontend runtime یا event behavior را مستند نمی‌کند. |

## 4. تعریف و هدف SVG element

### documented

- `SVG` مخفف `Scalable Vector Graphics` است.
- صفحه رسمی SVG را یک `XML-based image format` برای ساخت `two-dimensional vector graphics` معرفی می‌کند.
- SVG graphics می‌توانند بدون از دست دادن کیفیت scale شوند.
- صفحه رسمی SVG را برای `website graphics`، `icons` و `illustrations` مناسب می‌داند.
- `SVG widget` اجازه می‌دهد SVG graphics را به‌عنوان `separate element` در webpage وارد کنید.

### derived

چون صفحه SVG را separate element معرفی می‌کند، در این پایگاه دانش می‌توان آن را در گروه عناصر تصویری/گرافیکی Editor V4 قرار داد؛ اما این فقط دسته‌بندی تحلیلی داخلی است و نباید به‌عنوان taxonomy رسمی Elementor معرفی شود.

## 5. افزودن و حذف عنصر

### Add the element to the canvas — افزودن عنصر به بوم

#### documented

برای دسترسی و استفاده از element:

1. در Elementor Editor روی `+` کلیک کنید.
2. همه elementهای موجود نمایش داده می‌شوند.
3. element را click یا drag کنید و روی canvas قرار دهید.
4. برای جزئیات بیشتر، صفحه به مقاله `Add elements to a page` لینک می‌دهد.

#### observed

در صفحه یک تصویر رسمی برای بخش `Add the element to the canvas` درج شده است. این تصویر به‌عنوان شاهد بصری رسمی ثبت می‌شود، اما چون متن جایگزین یا جزئیات کنترل‌های داخل تصویر به‌صورت کامل در متن استخراج‌شده نیامده، جزئیات بیشتر از آن استنباط نمی‌شود.

### Delete the element — حذف عنصر

#### documented

برای حذف element:

1. روی canvas، عنصر را با کلیک انتخاب کنید.
2. کلید `Delete` روی keyboard را فشار دهید.
3. صفحه برای جزئیات بیشتر به مقاله `Delete elements from a page` لینک می‌دهد.

### insufficient_evidence

- صفحه مشخص نمی‌کند آیا حذف از طریق context menu، navigator، structure panel یا shortcutهای دیگر هم ممکن است یا نه.
- صفحه درباره undo/redo پس از حذف چیزی نمی‌گوید.
- صفحه درباره تفاوت رفتار Delete در سیستم‌عامل‌ها یا مرورگرها شواهدی نمی‌دهد.

## 6. موارد استفاده

### Common use case — مورد استفاده رایج

#### documented

مثال رسمی صفحه: شخصی به نام Hunter در حال ساخت یک `call to action section` است و می‌خواهد از `SVG illustrations` به‌عنوان icon استفاده کند.

### Additional use cases — موارد استفاده افزوده

#### documented

صفحه دو مورد استفاده دیگر را فهرست می‌کند:

- `Infographs` — اینفوگرافیک‌ها
- `Simple lightweight images that allow your page to load more quickly` — تصاویر ساده و سبک که به بارگذاری سریع‌تر صفحه کمک می‌کنند

### derived

در حد شواهد همین صفحه، SVG برای آیکون‌ها، illustrationهای ساده و infographها مناسب معرفی شده است. از این گزاره نمی‌توان نتیجه گرفت که SVG برای هر نوع محتوای تصویری، لوگو، انیمیشن، آیکون تعاملی یا فایل پیچیده بهترین گزینه است.

### insufficient_evidence

- صفحه درباره استفاده از SVG برای لوگو، mask، sprite، animation، inline SVG، symbol یا icon system توضیح نمی‌دهد.
- صفحه عملکرد واقعی فایل SVG را با PNG/WebP/JPG مقایسه نمی‌کند.
- صفحه درباره محدودیت حجم فایل، پیچیدگی pathها یا اثر SVGهای بزرگ روی performance چیزی نمی‌گوید.

## 7. آموزش گام‌به‌گام رسمی

صفحه یک سناریوی step-by-step برای ساخت بخش call-to-action با چند SVG ارائه می‌کند.

### documented steps

1. روی canvas یک `grid container` با یک row و سه column بسازید. برای جزئیات، صفحه به مقاله `Create a Grid container` ارجاع می‌دهد.
2. یک `SVG widget` به leftmost column اضافه کنید. برای جزئیات، صفحه به مقاله `Add elements to a page` ارجاع می‌دهد.
3. در panel روی `image field` کلیک کنید.
4. یک SVG image به widget اضافه کنید. برای جزئیات، صفحه به مقاله `Adding images and icons` ارجاع می‌دهد.
5. این کار را برای هر کدام از widgetها تکرار کنید.
6. برای clickable کردن iconها، روی envelope icon کلیک کنید.
7. در panel روی plus symbol کنار `Link` کلیک کنید.
8. `mailto link` را در text box وارد کنید.
9. به‌صورت اختیاری، اگر می‌خواهید link در تب جدید باز شود، toggle `Open in a new tab` را روشن کنید.
10. صفحه می‌گوید call-to-action section آماده است.

### observed images index

صفحه رسمی در این بخش چند تصویر پشت‌سرهم دارد. در متن استخراج‌شده، تصاویر با شناسه‌های داخلی زیر دیده شدند:

| ترتیب | جایگاه در صفحه | وضعیت |
|---:|---|---|
| 1 | Add the element to the canvas | observed |
| 2 | Common use case | observed |
| 3 | ساخت grid container | observed |
| 4 | آماده بودن محل افزودن elements به grid | observed |
| 5 | افزودن SVG widget به ستون چپ | observed |
| 6 | کلیک روی image field | observed |
| 7 | افزودن SVG image | observed |
| 8 | تکرار برای widgetهای دیگر | observed |
| 9 | clickable کردن iconها | observed |
| 10 | انتخاب envelope icon | observed |
| 11 | plus symbol کنار Link | observed |
| 12 | mailto link در text box | observed |
| 13 | toggle Open in a new tab | observed |
| 14 | نتیجه نهایی call-to-action section | observed |
| 15 | General tab screenshot | observed |
| 16 | Link screenshot | observed |
| 17 | Style tab screenshot | observed |

> نکته شواهدی: چون تصاویر در متن استخراج‌شده به‌صورت marker دیده شدند و جزئیات کامل پیکسل‌به‌پیکسل آن‌ها خوانده نشد، فقط وجود و جایگاه آن‌ها به‌عنوان `observed` ثبت می‌شود؛ جزئیات غیرمتنی کنترل‌ها از آن‌ها حدس زده نشده است.

## 8. General tab — تب General

صفحه در بخش `Settings for the SVG element` می‌گوید می‌توانید elementها را با content و style سفارشی کنید و سپس `General tab` را نشان می‌دهد.

### 8.1 Content / Settings

#### documented

در General tab، صفحه دو سربرگ یا ناحیه `Content` و `Settings` را نشان می‌دهد.

### 8.2 SVG

#### documented

- گزینه `SVG` برای افزودن SVG file است.
- متن رسمی: روی آن کلیک کنید تا یک SVG file اضافه شود.
- برای جزئیات، صفحه به مقاله `Adding images and icons` ارجاع می‌دهد.

#### insufficient_evidence

- صفحه مشخص نمی‌کند فایل از Media Library انتخاب می‌شود، upload مستقیم دارد یا URL خارجی می‌پذیرد؛ فقط به مقاله دیگر ارجاع می‌دهد.
- صفحه فرمت‌های مجاز، MIME type، محدودیت حجم، خطای آپلود یا مجوزهای WordPress را توضیح نمی‌دهد.
- صفحه درباره sanitize شدن SVG، حذف script، policy امنیتی یا roleهای لازم برای upload SVG توضیح نمی‌دهد.
- صفحه درباره alt text، title، caption یا metadata فایل SVG چیزی نمی‌گوید.

### 8.3 Link

#### documented

- گزینه `Link` با plus sign فعال/باز می‌شود.
- با وارد کردن link، بازدیدکننده با کلیک روی SVG file آن link را باز می‌کند.
- در مثال step-by-step، مقدار link از نوع `mailto link` است.
- در مثال، toggle اختیاری `Open in a new tab` وجود دارد.

#### insufficient_evidence

- صفحه درباره protocolهای مجاز، `rel` attributes، `nofollow`، `sponsored`، `noopener` یا `Custom Link Attributes` توضیح نمی‌دهد.
- صفحه نمی‌گوید `Open in a new tab` دقیقاً چه attributesی در HTML تولید می‌کند.
- صفحه درباره nested links، focus state یا keyboard activation برای SVG لینک‌شده چیزی نمی‌گوید.

### 8.4 ID

#### documented

- گزینه `ID` اجازه می‌دهد individual elements روی page را tag کنید.
- هدف ذکرشده: بتوانید به همان specific element لینک بدهید.

#### insufficient_evidence

- صفحه درباره syntax مجاز ID، یکتایی ID، case sensitivity، conflict با CSS/JS یا anchor behavior توضیح نمی‌دهد.
- صفحه نمی‌گوید ID روی کدام tag خروجی اعمال می‌شود.

## 9. Style tab — تب Style

### documented

در `Style tab`، صفحه فقط می‌گوید Style options در مقالات جداگانه توضیح داده شده‌اند و این دسته‌ها را فهرست می‌کند:

- `Layout` — چیدمان
- `Spacing` — فاصله‌گذاری
- `Size` — اندازه
- `Position` — موقعیت
- `Typography` — تایپوگرافی
- `Background` — پس‌زمینه
- `Border` — کادر/مرز
- `Effects` — افکت‌ها

### documented note درباره رنگ SVG

صفحه یک Note مهم درباره رنگ SVG دارد:

- `SVG widget` اجازه می‌دهد به SVG files رنگ اضافه کنید.
- فایل باید properly formatted باشد.
- `fill color` باید روی pure black یعنی `#000000` تنظیم شود.
- فایل باید با `no fill property` export شود.
- سپس می‌توانید با `color field` در بخش `Typography` از `Style tab`، fill color دلخواه خود را اضافه کنید.

### derived

در محدوده همین صفحه، کنترل رنگ SVG از مسیر Typography در Style tab معرفی شده است، اما جزئیات Typography article در این سند بررسی نشده‌اند. بنابراین فقط وجود رابطه بین SVG color و `color field` در `Typography section` ثبت می‌شود.

### insufficient_evidence

- صفحه درباره stroke color، stroke width، multi-color SVG یا gradients توضیح نمی‌دهد.
- صفحه مشخص نمی‌کند اگر SVG fill غیرمشکی باشد یا fill property داشته باشد دقیقاً چه اتفاقی می‌افتد.
- صفحه درباره CSS variables، global colors، hover color، active/focus state، responsive color یا dynamic color شواهدی نمی‌دهد.
- صفحه جزئیات `Layout`, `Spacing`, `Size`, `Position`, `Background`, `Border`, `Effects` را در همین مقاله توضیح نمی‌دهد.

## 10. ماتریس کنترل‌ها

| کنترل / بخش | نام انگلیسی | ترجمه فارسی | evidence_state | توضیح |
|---|---|---|---|---|
| افزودن عنصر | `+` | افزودن | documented | در Elementor Editor برای نمایش عناصر موجود استفاده می‌شود. |
| کشیدن/کلیک | click or drag | کلیک یا کشیدن | documented | برای قرار دادن element روی canvas. |
| حذف | Delete key | کلید حذف | documented | بعد از انتخاب عنصر روی canvas. |
| فایل SVG | `SVG` | فایل SVG | documented | با کلیک، SVG file اضافه می‌شود. |
| لینک | `Link` | لینک | documented | با plus sign لینک وارد می‌شود. |
| تب جدید | `Open in a new tab` | باز کردن در تب جدید | documented | اختیاری در مثال step-by-step. |
| شناسه | `ID` | شناسه | documented | برای tag کردن element و لینک دادن به آن. |
| Style | `Style` | استایل | documented | دسته‌های Style را فهرست می‌کند. |
| Layout | `Layout` | چیدمان | documented_name_only | فقط نام و لینک مقاله مستقل آمده است. |
| Spacing | `Spacing` | فاصله‌گذاری | documented_name_only | فقط نام و لینک مقاله مستقل آمده است. |
| Size | `Size` | اندازه | documented_name_only | فقط نام و لینک مقاله مستقل آمده است. |
| Position | `Position` | موقعیت | documented_name_only | فقط نام و لینک مقاله مستقل آمده است. |
| Typography | `Typography` | تایپوگرافی | documented_name_only | برای color field مرتبط با SVG هم ذکر شده است. |
| Background | `Background` | پس‌زمینه | documented_name_only | فقط نام و لینک مقاله مستقل آمده است. |
| Border | `Border` | کادر | documented_name_only | فقط نام و لینک مقاله مستقل آمده است. |
| Effects | `Effects` | افکت‌ها | documented_name_only | فقط نام و لینک مقاله مستقل آمده است. |

## 11. موضوعات خواسته‌شده که صفحه شواهد کافی برای آن‌ها ندارد

| موضوع | وضعیت | دلیل |
|---|---|---|
| viewBox | insufficient_evidence | در متن صفحه نیامده است. |
| dimensions | insufficient_evidence | جزئیات dimensionهای SVG مستند نشده است. |
| width و height | insufficient_evidence | صفحه کنترل‌های width/height را توضیح نمی‌دهد. |
| aspect ratio | insufficient_evidence | شواهدی در صفحه نیست. |
| stroke | insufficient_evidence | فقط fill color مطرح شده، نه stroke. |
| source و media-library behavior | insufficient_evidence | صفحه فقط به افزودن SVG file و مقاله دیگر اشاره دارد. |
| sanitization | insufficient_evidence | هیچ توضیح امنیتی صریحی وجود ندارد. |
| responsive controls | insufficient_evidence | مقاله جزئیات responsive را نمی‌دهد. |
| dynamic data | insufficient_evidence | اشاره صریح ندارد. |
| classes و variables | insufficient_evidence | اشاره صریح ندارد. |
| element states | insufficient_evidence | hover/focus/active ذکر نشده است. |
| accessibility | insufficient_evidence | alt/title/aria/focus behavior ذکر نشده است. |
| keyboard/focus behavior | insufficient_evidence | رفتار frontend یا editor focus توضیح داده نشده است. |
| SEO behavior | insufficient_evidence | صفحه درباره SEO توضیح نمی‌دهد. |
| generated markup | insufficient_evidence | خروجی HTML/SVG یا wrapper مشخص نشده است. |
| runtime behavior | insufficient_evidence | event handling یا frontend runtime توضیح داده نشده است. |

## 12. قواعد استفاده امن در پایگاه دانش

- از این صفحه می‌توان گفت: SVG element در Editor V4 برای افزودن SVG graphics به‌عنوان separate element استفاده می‌شود.
- از این صفحه می‌توان گفت: برای افزودن عنصر، در Editor روی `+` کلیک می‌شود و element با click یا drag به canvas افزوده می‌شود.
- از این صفحه می‌توان گفت: SVG file از کنترل `SVG` اضافه می‌شود.
- از این صفحه می‌توان گفت: `Link` باعث می‌شود کلیک بازدیدکننده روی SVG، link را باز کند.
- از این صفحه می‌توان گفت: `Open in a new tab` در مثال رسمی یک toggle اختیاری است.
- از این صفحه می‌توان گفت: `ID` برای tag کردن individual elements و لینک دادن به همان specific element است.
- از این صفحه نمی‌توان درباره امنیت SVG، sanitize شدن، roleها، dynamic tags، accessibility، SEO یا HTML output نتیجه قطعی گرفت.

## 13. نمونه کاربردی بر اساس منبع رسمی

### سناریو

ساخت call-to-action section با سه آیکون SVG.

### مراحل مستند

1. ایجاد grid container با یک row و سه column.
2. افزودن SVG widget به ستون چپ.
3. کلیک روی image field در panel.
4. افزودن SVG image.
5. تکرار برای widgetهای دیگر.
6. کلیک روی envelope icon.
7. باز کردن `Link` با plus symbol.
8. وارد کردن mailto link.
9. روشن کردن اختیاری `Open in a new tab`.

### محدودیت استنادی

مقاله جزئیات ساخت grid container، نحوه upload SVG، جزئیات media library، رفتار mailto در مرورگر، accessibility لینک یا خروجی HTML را توضیح نمی‌دهد؛ برای هر کدام باید منبع مستقل خوانده شود.

## 14. Front matter پیشنهادی برای استفاده ماشینی

```yaml
id: elementor.help.svg-element
title: SVG element
source_url: https://elementor.com/help/svg-element/
source_type: official_help
version_scope: rolling_documentation
last_updated: 2025-07-01
researched_at: 2026-06-23T01:04:00+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-020
```

## 15. Claim-level notes

```text
SVG is an XML-based image format for two-dimensional vector graphics.
- knowledge_id: elementor.help.svg-element
- document: docs/elements/v4/svg.md
- evidence_state: documented
- source_url: https://elementor.com/help/svg-element/

SVG graphics can be scaled without losing quality.
- knowledge_id: elementor.help.svg-element
- document: docs/elements/v4/svg.md
- evidence_state: documented
- source_url: https://elementor.com/help/svg-element/

The SVG widget incorporates SVG graphics into a webpage as a separate element.
- knowledge_id: elementor.help.svg-element
- document: docs/elements/v4/svg.md
- evidence_state: documented
- source_url: https://elementor.com/help/svg-element/

The Link control lets visitors open a link by clicking the SVG file.
- knowledge_id: elementor.help.svg-element
- document: docs/elements/v4/svg.md
- evidence_state: documented
- source_url: https://elementor.com/help/svg-element/

The article does not document SVG sanitization behavior.
- knowledge_id: elementor.help.svg-element
- document: docs/elements/v4/svg.md
- evidence_state: insufficient_evidence
- source_url: https://elementor.com/help/svg-element/
```

## 16. جمع‌بندی

صفحه رسمی `SVG element` برای Editor V4 یک مستند کوتاه اما مهم است. شواهد کافی برای تعریف SVG، کاربردهای اصلی، روند افزودن/حذف عنصر، نمونه ساخت CTA با SVG icons، کنترل‌های `SVG`، `Link` و `ID`، دسته‌های کلی Style و شرط رنگ‌پذیری SVG ارائه می‌کند. در مقابل، برای بسیاری از جزئیات فنی مورد انتظار مانند `viewBox`، dimensions، stroke، sanitization، responsive behavior، dynamic data، accessibility، SEO، generated markup و runtime behavior شواهد کافی ندارد؛ بنابراین وضعیت این مرحله `completed_with_gaps` است.
