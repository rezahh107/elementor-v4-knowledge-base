# Elementor Evidence Knowledge Base

پایگاه دانش شواهد‌محور برای Elementor Editor V4، Loop، Design System و Style System.

این مخزن صرفاً مجموعه‌ای از جزوه‌ها نیست. داده‌های وضعیت، منابع، شکاف‌های شواهد و تاریخچه اجرا به‌صورت ماشین‌خوان نگهداری و با CI اعتبارسنجی می‌شوند.

## سطح اعتماد

هر سند یکی از این وضعیت‌ها را دارد:

- `unreviewed` یا `document_level_legacy`: پژوهش‌نامه است و authoritative نیست.
- `machine_validated`: ساختار و ارجاعات ماشینی معتبرند، اما Review مستقل نشده است.
- `peer_reviewed`: ادعاهای ثبت‌شده Review مستقل دارند.
- `verified_by_fixture`: رفتار با Fixture واقعی یا آزمون کنترل‌شده تأیید شده است.

هیچ مدل زبانی نباید یک سند را فقط به‌دلیل `storage_status: committed` حقیقت کامل محصول تلقی کند.

## شروع سریع

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python tools/kb.py validate --strict
python tools/kb.py generate --check
python -m pytest
```

## منبع حقیقت

`manifests/stages.yaml` تنها منبع حقیقت وضعیت مراحل و صف است.

فایل‌های زیر تولیدشده‌اند و نباید دستی ویرایش شوند:

- `STATUS.md`
- `docs/_index.md`
- `manifests/coverage.yaml`
- `manifests/sources.yaml`

برای بازتولید آن‌ها:

```bash
python tools/kb.py generate
```

## افزودن یا به‌روزرسانی محتوا

1. Branch مستقل بسازید.
2. Source Record و Image Evidence را ثبت کنید.
3. Claimهای مهم را با Claim ID و Source Locator بنویسید.
4. سند و `manifests/stages.yaml` را به‌روزرسانی کنید.
5. Event جدید را به `ledger/executions.jsonl` اضافه کنید؛ رکوردهای قبلی را تغییر ندهید.
6. Generated artifacts را بازسازی کنید.
7. Validator و Testها را اجرا کنید.
8. Pull Request بسازید و فقط پس از عبور CI و Review Merge کنید.

جزئیات در `CONTRIBUTING.md` و `QUALITY_POLICY.md` آمده است.

## سیاست منابع

ترتیب اعتبار:

1. مستندات رسمی Elementor
2. مستندات رسمی توسعه‌دهندگان Elementor
3. کد و Changelog رسمی Elementor
4. Fixture واقعی کنترل‌شده
5. Fixture مصنوعی با برچسب صریح
6. منبع ثالث با برچسب صریح

## صف پژوهش

صف در دوره Hardening متوقف است. ازسرگیری فقط پس از عبور این Gateها مجاز است:

```text
python tools/kb.py validate --strict
python tools/kb.py generate --check
python -m pytest
```

و Merge شدن تغییرات Hardening از طریق Pull Request.
