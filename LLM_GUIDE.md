# راهنمای اجباری مدل‌های زبانی

## ترتیب مطالعه

1. `QUALITY_POLICY.md`
2. `manifests/stages.yaml`
3. `manifests/evidence-gaps.yaml`
4. `manifests/sources.yaml`
5. `STATUS.md`
6. سند موضوعی
7. Claim Record و Source Record مربوط
8. `registries/evidence-states.yaml`

## منبع حقیقت

`manifests/stages.yaml` تنها SSOT وضعیت مراحل است. `STATUS.md`، `docs/_index.md`، `manifests/coverage.yaml` و `manifests/sources.yaml` فایل‌های تولیدشده‌اند.

## قاعده استناد

برای ادعای authoritative باید این زنجیره موجود باشد:

```text
claim_id
→ evidence_state
→ source_id
→ source_locator
→ source_record/content_fingerprint
→ review_status
```

اگر این زنجیره کامل نیست، ادعا را با وضعیت واقعی آن بیان کنید:

- `documented` یا `observed` فقط در محدوده Evidence موجود؛
- `derived` همراه `derived_from`؛
- `insufficient_evidence` همراه Missing Evidence؛
- سند `document_level_legacy` را authoritative معرفی نکنید.

## فرمت توصیه‌شده پاسخ

```text
[ادعا]
- claim_id: KB-XXX-CNNN
- document: docs/...
- evidence_state: documented
- source_id: SRC-KB-XXX-01
- locator: ...
- review_status: peer_reviewed
```

در اسناد Legacy که Claim ID ندارند:

```text
status: document_level_legacy
citation_scope: document_only
authoritative: false
```

## ممنوعیت‌ها

- حدس‌زدن نسخه، Default، Pro prerequisite، Accessibility یا Runtime behavior؛
- تبدیل خاموش V3 و V4؛
- تبدیل `derived` به `documented`؛
- استفاده از تصویر `not_inspected` به‌عنوان Observation؛
- استفاده از `STATUS.md` به‌عنوان منبع رفتار Elementor؛
- اعلام Commit، CI یا Review بدون نتیجه واقعی ابزار؛
- نادیده‌گرفتن Evidence Gap باز.

## تازه‌بودن

`last_updated` تاریخ گزارش‌شده مقاله است، نه تاریخ عرضه قابلیت. برای ادعای Current behavior باید Freshness و Source Snapshot بررسی شود.

## اولویت تعارض

1. Contract و Registry نسخه‌دار
2. Source Record رسمی جدیدتر
3. Fixture واقعی کنترل‌شده
4. سند Synthesis
5. یادداشت Legacy

تعارض باید گزارش شود، نه اینکه خاموش Merge شود.
