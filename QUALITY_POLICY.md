# Quality Policy

## هدف

این سند شرایطی را تعریف می‌کند که تحت آن یک مطلب می‌تواند توسط انسان یا مدل زبانی مورد استناد قرار گیرد.

## چهار لایه داده

1. **Source Record**: مشخصات منبع، URL درخواستی و Canonical، زمان دریافت، وضعیت HTTP و SHA-256 محتوای Canonical.
2. **Evidence Record**: متن، تصویر یا Fixture قابل ردیابی.
3. **Claim Record**: ادعای اتمیک با `claim_id`، وضعیت شواهد و Locator.
4. **Synthesis Document**: توضیح فارسی که فقط Claimهای ثبت‌شده را ترکیب می‌کند.

## وضعیت‌های شواهد

- `documented`: متن منبع صریحاً ادعا را بیان کرده است.
- `observed`: ادعا مستقیماً در تصویر رسمی یا Capture کنترل‌شده دیده شده است.
- `validated`: Fixture واقعی یا آزمون کنترل‌شده آن را تأیید کرده است.
- `derived`: نتیجه محدود و قابل ردیابی از Claimهای دیگر است.
- `proposed`: پیشنهاد است.
- `unverified`: هنوز تأیید نشده است.
- `insufficient_evidence`: شواهد کافی وجود ندارد.

`derived` بدون `derived_from` و `observed` بدون Image Evidence با `inspection_status: inspected` نامعتبر است.

## شرایط authoritative

یک Stage فقط زمانی authoritative است که:

- `review_status` برابر `peer_reviewed` یا `verified_by_fixture` باشد؛
- `provenance_status` برابر `claim_level` باشد؛
- همه Source Snapshotهای لازم `captured` باشند؛
- هیچ Evidence Gap باز که `authoritative_status` را Block کند وجود نداشته باشد؛
- Schema، Consistency و Generated Artifact Gateها عبور کرده باشند.

## اسناد Legacy

اسناد مهاجرت‌یافته با:

```yaml
review_status: unreviewed
provenance_status: document_level_legacy
```

حفظ می‌شوند. این اسناد حذف نمی‌شوند، اما تا Migration و Review مستقل authoritative نیستند.

## سیاست تصویر

سه وضعیت مستقل ثبت می‌شوند:

- `discovered`
- `retrieved`
- `inspected`

وجود URL تصویر یا شمارش تصویر، مشاهده محسوب نمی‌شود. تصویر `cache_miss` یا `not_inspected` نمی‌تواند Claim از نوع `observed` را پشتیبانی کند.

## سیاست Snapshot

برای منابع جدید باید Source Record شامل این موارد وجود داشته باشد:

- `requested_url`
- `canonical_url`
- `retrieved_at`
- `http_status`
- `page_title`
- `reported_last_updated`
- `content_sha256`
- `image_evidence_ids`

ذخیره متن کامل صفحات دارای حق نشر الزامی نیست؛ Fingerprint، Locator و Quote کوتاه کافی است.

## تغییر وضعیت

هیچ Automation یا مدل زبانی اجازه ندارد:

- `unreviewed` را بدون Review واقعی به `peer_reviewed` تبدیل کند؛
- `document_level_legacy` را بدون Claim Migration به `claim_level` تبدیل کند؛
- Evidence Gap را بدون Evidence Record معتبر ببندد؛
- SHA، Timestamp یا نتیجه CI را حدس بزند.

## Fail-closed Queue

مدیر صف فقط وقتی فعال می‌شود که:

```yaml
repository_consistency: clean
blocking_diagnostics: 0
queue.enabled: true
```

در هر مغایرت، صف متوقف می‌ماند.
