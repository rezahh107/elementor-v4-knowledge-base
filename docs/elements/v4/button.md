---
id: elementor.help.button-element
title: Button element
source_url: https://elementor.com/help/button-element/
canonical_url: https://elementor.com/help/button-element/
source_title: Button element | Elementor
source_type: official_help
version_scope: editor_v4
last_updated: 2025-07-01
researched_at: 2026-06-23T16:53:00+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-004
review_status: machine_validated
provenance_status: claim_level
claim_record: evidence/claims/KB-004-button.yaml
source_record: evidence/sources/SRC-KB-004-01.yaml
image_evidence: evidence/images/KB-004-button.yaml
---

# Button element در Elementor Editor V4

> وضعیت این سند: claim-level migration انجام شده، اما به‌دلیل نبود دسترسی خام به HTML در این اجرای Automation، `content_sha256` صفحه رسمی جعل نشده و به‌عنوان Evidence Gap باز مانده است. سند `peer_reviewed` نیست و فقط در حد `machine_validated` علامت‌گذاری شده است.

## دامنه و منبع

این سند فقط بر اساس صفحه رسمی `Button element` در Elementor Help نوشته شده است. خود صفحه در مسیر `Help Center > Build with the Editor > Editor V4 > Button element` قرار دارد، تاریخ `Last Update: July 1, 2025` را نشان می‌دهد و صریحاً می‌گوید برای کاربران `Editor v4` است؛ کاربران `Editor v3` به مقاله جداگانه `Button Widget` ارجاع داده شده‌اند.  
Claimها: `KB-004-C001`, `KB-004-C002`, `KB-004-C003`

## کاربرد Button element

در متن رسمی، Buttonها برای هدایت Action کاربر، ایجاد Call to Action و افزودن دکمه‌های تعاملی و بصری به سایت توضیح داده شده‌اند. نمونه اصلی صفحه، دکمه‌ای در Hero section یک سایت باشگاه است که بازدیدکننده را به صفحه ثبت‌نام می‌برد. صفحه رسمی همچنین سه کاربرد اضافه را ذکر می‌کند: لینک دادن Buttonها به صفحه پروژه یا نمای جزئیات در Portfolio gallery، استفاده در بنر یا پوستر رویداد/وبینار، و نمایش before/after transformation.  
Claimها: `KB-004-C004`, `KB-004-C005`, `KB-004-C006`, `KB-004-C007`

نکته کیفیت: متن رسمی در بخش Common use case یک جمله ناسازگار درباره dollar signs/hearts و rating دارد که با موضوع Button element همخوان نیست. این جمله در Claimها به‌عنوان `documented_source_anomaly` ثبت شده و در این سند به‌عنوان قابلیت Button تفسیر نشده است.  
Claim: `KB-004-C008`

## افزودن و حذف Element

برای افزودن Button element، صفحه رسمی می‌گوید در Elementor Editor روی `+` کلیک کنید تا همه Elementهای موجود نمایش داده شوند، سپس Element را با Click یا Drag به Canvas اضافه کنید. برای حذف، Element روی Canvas انتخاب می‌شود و کلید `Delete` صفحه‌کلید فشار داده می‌شود.  
Claimها: `KB-004-C009`, `KB-004-C010`

اصطلاح‌شناسی: متن رسمی در همین بخش از عبارت `widget` استفاده می‌کند، اما عنوان و مسیر صفحه `Button element` و `Editor V4` است. بنابراین این سند اصطلاح اصلی را `Button element` نگه می‌دارد و ناسازگاری واژه `widget` را به‌عنوان خطای منبع ثبت می‌کند، نه تغییر نوع محصول.  
Claim: `KB-004-C011`

## Step-by-step رسمی

صفحه رسمی یک سناریوی طراحی را مرحله‌به‌مرحله نشان می‌دهد. مقدارهای زیر فقط مقدارهای مثال هستند و در این سند به‌عنوان Default محصول ثبت نشده‌اند:

| کنترل انگلیسی | ترجمه فارسی | مقدار مثال رسمی | Claim |
|---|---|---:|---|
| `Button text` | متن دکمه | `Get Started` | `KB-004-C012` |
| `Link` | پیوند | URL صفحه مقصد | `KB-004-C013` |
| `Size > Width` | اندازه > عرض | `200` | `KB-004-C014` |
| `Size > Height` | اندازه > ارتفاع | `50` | `KB-004-C014` |
| `Typography > Font Family` | تایپوگرافی > خانواده فونت | `Sora` | `KB-004-C015` |
| `Typography > Font Weight` | تایپوگرافی > وزن فونت | `600` | `KB-004-C015` |
| `Typography > Font Size` | تایپوگرافی > اندازه فونت | `16` | `KB-004-C015` |
| `Background > Opacity` | پس‌زمینه > شفافیت | `0%` | `KB-004-C016` |
| `Border > Radius` | حاشیه > گردی گوشه‌ها | `50` برای همه Cornerها | `KB-004-C017` |
| `Border > Width` | حاشیه > ضخامت | `2` | `KB-004-C018` |
| `Border > Color` | حاشیه > رنگ | `#FFFFFF` | `KB-004-C019` |

## تنظیمات General tab

در بخش Settings، صفحه رسمی برای `General tab` سه کنترل/گزینه محتوایی را مستند می‌کند:

- `Button text` — متنی که داخل Button نمایش داده می‌شود. Claim: `KB-004-C020`
- `Link` — با کلیک روی Plus sign می‌توان Link وارد کرد؛ بازدیدکننده با کلیک روی Button لینک را باز می‌کند. Claim: `KB-004-C021`
- `Open in a new tab` — اگر Button دارای Link باشد، Toggle می‌تواند لینک را در تب جدید باز کند. Claim: `KB-004-C022`
- `ID` — برای Tag کردن Elementهای منفرد در صفحه و لینک دادن به همان Element استفاده می‌شود. Claim: `KB-004-C023`

این صفحه درباره Protocolهای مجاز، Sanitization، رفتار AJAX/URL، خروجی HTML یا قواعد یکتایی ID توضیح کافی نمی‌دهد؛ این موارد در Evidence Gapها باقی مانده‌اند.

## تنظیمات Style tab

صفحه رسمی می‌گوید Elementها با Content و Style قابل سفارشی‌سازی هستند و در `Style tab` خانواده‌های زیر را به مقاله‌های مستقل ارجاع می‌دهد:

`Layout`, `Spacing`, `Size`, `Position`, `Typography`, `Background`, `Border`, `Effects`.  
Claim: `KB-004-C024`

خود صفحه جزئیات کامل این خانواده‌ها را توضیح نمی‌دهد؛ بنابراین جزئیات Layout/Spacing/Position/Effects یا Defaultهای آن‌ها از این سند نتیجه‌گیری نشده است.

## Element states و Hover

در مثال رسمی، صفحه توضیح می‌دهد `Hover` یک State است و Elementها می‌توانند بسته به State ظاهر متفاوتی داشته باشند. برای ویرایش Hover، در `Classes text field` روی Ellipsis کنار `local` کلیک می‌شود، `Hover` از Dropdown انتخاب می‌شود، واژه `hover` در Classes text box با رنگ صورتی ظاهر می‌شود، سپس Color picker باز می‌شود و Hex color به `#FFFFFF` و Opacity به `100%` تغییر می‌کند. نتیجه مثال این است که هنگام Mouse hover، Button سفید می‌شود.  
Claimها: `KB-004-C025`, `KB-004-C026`, `KB-004-C027`, `KB-004-C028`

این صفحه فقط Hover را نشان می‌دهد؛ مجموعه کامل Stateها، Cascade، Specificity، Keyboard focus و Focus-visible از این صفحه اثبات نمی‌شود.

## شواهد تصویری رسمی

در این مهاجرت، تصاویر رسمی زیر به‌صورت قابل مشاهده با ابزار وب بررسی شدند و برای Claimهای `observed` محدود استفاده شدند:

- `IMG-KB-004-001` — `Add-teh-element-to-the-canvas-scaled.webp`: پنل `Edit Button` با تب‌های `General` و `Style`، فیلد `Button text`، ردیف `Link` و دکمه روی Canvas را نشان می‌دهد.
- `IMG-KB-004-002` — `Enter-get-started-scaled.webp`: ورود مقدار `Get Started` در `Button text` را نشان می‌دهد.
- `IMG-KB-004-003` — `Click-the-plus-sign-2-241x300.png`: Plus sign کنار `Link` را نشان می‌دهد.
- `IMG-KB-004-004` — `Set-the-size-to-200-1-141x300.png`: در `Style > Size` مقدار Width برابر `200` و Height برابر `50` دیده می‌شود.
- `IMG-KB-004-005` — `Click-the-ellipses-1-151x300.png`: `CSS classes` و Chip `local` و Ellipsis کنار آن را نشان می‌دهد.
- `IMG-KB-004-006` — `Select-hover-from-the-dropdown-1-137x300.png`: Dropdown شامل `Normal`, `Hover`, `Focus`, `Active` را نشان می‌دهد؛ چون متن رسمی فقط Hover را توضیح می‌دهد، وجود سایر Stateها به‌عنوان Claim محصول ثبت نشده است.
- `IMG-KB-004-007` — `Open-the-color-picker-2-174x300.png`: Chipهای `local` و `hover` و Color picker را نشان می‌دهد.
- `IMG-KB-004-008` — `General-content-3.png`: بخش `General > Content` و فیلد `Button text` را نشان می‌دهد.
- `IMG-KB-004-009` — `Style-tab-2-504x1024.png`: فهرست Style tab شامل `Classes`, `Layout`, `Spacing`, `Size`, `Position`, `Typography`, `Background`, `Border`, `Effects` را نشان می‌دهد.

سایر تصاویر صفحه در وضعیت `discovered` باقی مانده‌اند مگر در فایل Image Evidence وضعیت دیگری ثبت شده باشد.

## مرزبندی شواهد

### documented

مواردی که متن صفحه رسمی صریحاً گفته است: دامنه Editor v4، تاریخ آخرین به‌روزرسانی، روش افزودن/حذف، هدف Button، موارد استفاده، مراحل مثال، کنترل‌های General، ارجاع‌های Style و توضیح Hover state.

### observed

مواردی که فقط از تصویر رسمی قابل مشاهده‌اند: ترکیب پنل `Edit Button`، وجود `General/Style`، نمایش Plus sign کنار Link، مقدارهای مثال در برخی کنترل‌ها، Chip `local`, Ellipsis، Dropdown Hover و ظاهر `hover` در Classes text box. Observationها فقط در محدوده تصویرهای inspected استفاده شده‌اند.

### derived

- چون صفحه Button را زیر `Editor V4` قرار داده و جدا از `Button Widget` V3 معرفی می‌کند، این سند اصطلاح `Button element` را برای V4 حفظ می‌کند. Derived from: `KB-004-C002`, `KB-004-C011`.
- چون صفحه برای Style options به مقاله‌های جداگانه لینک می‌دهد، این سند جزئیات آن‌ها را بدون بررسی مستقل آن صفحات ادعا نمی‌کند. Derived from: `KB-004-C024`.

### insufficient_evidence

این صفحه برای موارد زیر شواهد کافی ارائه نمی‌کند و Claim یا Gap جدا دارد:

- Default واقعی همه کنترل‌ها؛
- نسخه دقیق افزونه یا حداقل نسخه سازگار؛
- Free/Pro prerequisite؛
- Accessibility، ARIA role/name، Keyboard focus و Focus-visible؛
- خروجی HTML/DOM و Runtime behavior؛
- قواعد Sanitization، Protocolهای Link، URL/AJAX behavior؛
- Responsive overrideها و Breakpoint behavior؛
- Dynamic Tags، Variables، Global Classes و Cascade؛
- Submit/disabled/loading behavior؛
- Analytics یا Click tracking؛
- قواعد uniqueness و escaping برای `ID`.

## فایل‌های Evidence

- Source Record: `evidence/sources/SRC-KB-004-01.yaml`
- Claim Records: `evidence/claims/KB-004-button.yaml`
- Image Evidence: `evidence/images/KB-004-button.yaml`

## وضعیت نهایی مرحله

```yaml
stage_id: KB-004
review_status: machine_validated
provenance_status: claim_level
evidence_status: completed_with_gaps
peer_reviewed: false
blocking_gap: raw_html_content_sha256_not_available_in_this_run
```
