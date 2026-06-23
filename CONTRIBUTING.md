# Contribution Guide

## اصل پایه

هیچ تغییر محتوایی یا کنترلی مستقیماً روی `main` انجام نشود.

## Workflow

```text
main
  └── kb/KB-XXX-short-name
        ├── content commit
        ├── canonical metadata + ledger commit
        ├── generated artifacts commit
        └── Pull Request
```

## اجرای محلی

```bash
python -m pip install -e ".[dev]"
python tools/kb.py generate
python tools/kb.py validate --strict
python tools/kb.py generate --check
python -m pytest
```

## افزودن Stage

1. رکورد Stage را در `manifests/stages.yaml` اضافه یا اصلاح کنید.
2. `source_id` پایدار بسازید.
3. برای هر منبع جدید Source Record ایجاد کنید.
4. تصاویر را در Image Evidence Ledger ثبت کنید.
5. سند Markdown دارای Front Matter معتبر تولید کنید.
6. Claimهای مهم را در فایل Claim مربوط ثبت کنید.
7. Event جدید را به انتهای `ledger/executions.jsonl` اضافه کنید.
8. `python tools/kb.py generate` را اجرا کنید.
9. PR باز کنید.

## Ledger

`ledger/executions.jsonl` append-only است.

ممنوع:

- ویرایش Event قبلی؛
- تغییر ترتیب خطوط؛
- JSON غیرCanonical؛
- Timestamp بدون Offset؛
- SHA ساختگی.

برای اصلاح رکورد قبلی، Event جدید با توضیح Correction اضافه شود.

## Generated Files

این فایل‌ها دستی ویرایش نمی‌شوند:

- `STATUS.md`
- `docs/_index.md`
- `manifests/coverage.yaml`
- `manifests/sources.yaml`

CI هر Drift را رد می‌کند.

## Source Locator

Locator باید تا حد ممکن پایدار و قابل بازبینی باشد:

```yaml
source_id: SRC-KB-016-01
locator: "heading=General tab; paragraph=4"
```

برای تصویر:

```yaml
source_id: SRC-KB-016-01
locator: "image=IMG-KB-016-003"
```

## Review

نویسنده Stage نباید Review نهایی همان Stage را انجام دهد. Review باید وجود Claim IDs، تطبیق Locatorها، مرزبندی Derived و ثبت Gapها را بررسی کند.
