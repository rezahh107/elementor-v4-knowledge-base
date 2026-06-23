---
id: elementor.help.explore-v4-features
title: Explore the V4 features
source_url: https://elementor.com/help/explore-the-v4-features/
source_type: official_help
version_scope: rolling_documentation
last_updated: 2025-06-11
researched_at: 2026-06-23T10:47:13+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-003
---

# آشنایی با قابلیت‌های Editor V4

## دامنه و وضعیت منبع

- منبع: مقاله رسمی Elementor با عنوان `Explore the V4 features`
- آخرین به‌روزرسانی اعلام‌شده: `June 11, 2025`
- این سند فقط ادعاهای صریح همان مقاله و مشاهدات تصاویر رسمی آن را پوشش می‌دهد.

## documented

### فعال‌سازی و تشخیص Elementهای V4

پس از Opt-in به V4، Elementهای V4 در پنل همراه Widgetهای Elementor Editor 3.x ظاهر می‌شوند.

Elementهای V4 با دو نشانه معرفی شده‌اند:

1. `Atomic icon` در کنار Element؛
2. قرارگرفتن در گروه `V4 Elements`.

این مقاله وجود هم‌زمان Elementهای V4 و Widgetهای 3.x را در پنل صریحاً بیان می‌کند، اما درباره قواعد ذخیره یا سازگاری اسناد Hybrid توضیح فنی نمی‌دهد.

### پنل تنظیمات Element

بعد از افزودن Element V4 به Canvas، تنظیمات آن در پنل ظاهر می‌شود.

مقاله نام دو حوزه را مطرح می‌کند:

- `General tab` — تب عمومی؛
- `Style tab` — تب استایل.

متن مقاله در یک جمله از تقسیم گزینه‌ها به `General and Content` یاد می‌کند، اما بلافاصله ساختار را به General و Style توضیح می‌دهد. این ناسازگاری متنی باید بدون اصلاح خاموش حفظ شود.

### General tab

`General tab` شامل گزینه‌های مخصوص همان Element است.

نمونه مستند:

- General در Paragraph شامل متن Element و Link تعبیه‌شده در متن است.

این نمونه نباید به همه Elementها تعمیم داده شود.

### Style tab

`Style tab` شامل گزینه‌های مشترک میان Elementها و مؤثر بر ظاهر و حس بصری است.

مقاله وجود `Classes text box` را در Style tab بیان می‌کند.

### Classes text box

- نام همه Classهای اعمال‌شده بر Element را نمایش می‌دهد.
- همه Elementها دارای `local class` هستند.
- local class به همان Element مشخص مربوط است.

این مقاله ترتیب اولویت Classها، ساختار ذخیره‌سازی، Cascade property-level یا رفتار Runtime را توضیح نمی‌دهد.

### Class Manager

`Class Manager` برای این عملیات معرفی شده است:

- rearrange — جابه‌جایی ترتیب؛
- delete — حذف؛
- rename — تغییر نام.

دسترسی به آن از طریق `Class Manager icon` انجام می‌شود.

## observed

تصاویر رسمی مقاله موارد زیر را نمایش می‌دهند:

- Atomic icon در پنل؛
- گروه V4 Elements؛
- پنل General یک Element؛
- بخش‌های Style؛
- Classes text box؛
- Class Manager.

جزئیات دقیق تمام Labelها و مقادیر تصاویر از متن مقاله قابل استخراج کامل نیست و تا مشاهده مستقیم با وضوح کافی، `insufficient_evidence` باقی می‌ماند.

## derived

- V4 یک لایه Element/Style مبتنی بر Class را کنار محیط قدیمی 3.x ارائه می‌کند.
- Style tab برای دانش مشترک میان Elementها مناسب است و باید در پایگاه دانش به اسناد مستقل Style system متصل شود.
- وجود local class به معنای اثبات اولویت آن نسبت به Global Classes نیست؛ این نتیجه باید از منبع مستقل Class precedence گرفته شود.

## insufficient_evidence

این مقاله شواهد کافی درباره موارد زیر ندارد:

- نسخه دقیق Elementor که این UI را پیاده می‌کند؛
- وضعیت Stable/Beta یا شرایط Opt-in؛
- Free/Pro prerequisite؛
- Schema ذخیره Elementها، Classها و local class؛
- ترتیب Cascade و Conflict resolution؛
- Responsive behavior؛
- Dynamic Tags، Variables و Interactions؛
- Accessibility و keyboard navigation؛
- Runtime DOM و CSS output؛
- مهاجرت خودکار V3 به V4.

## تعارض ثبت‌شده

```yaml
status: documented_conflict
claim_a: "options are divided into General and Content"
claim_b: "General contains element-specific options and Style contains common options"
action: preserve_both_without_silent_repair
required_evidence: updated_official_page_or_controlled_runtime_fixture
```
