# Hardening Migration v1

## وضعیت

این Migration ساختار قبلی را حذف نمی‌کند. هجده سند موجود به‌عنوان `document_level_legacy` ثبت شده‌اند.

## تغییرات

- `manifests/stages.yaml` به SSOT تبدیل شد.
- چهار فایل وضعیت به Generated Artifact تبدیل شدند.
- Ledger append-only اضافه شد.
- Schema و Validator اضافه شد.
- Evidence Gapهای Provenance، Snapshot و Review برای اسناد Legacy ثبت شد.
- صف پژوهش تا عبور Gateها متوقف شد.
- Workflow آینده Branch + PR + CI است.

## محدودیت باقی‌مانده

Claim-level migration هجده سند قدیمی نیازمند بازبینی مجدد منابع است. این عملیات به‌طور خودکار جعل نشده است و به‌عنوان Gap باز باقی می‌ماند.
