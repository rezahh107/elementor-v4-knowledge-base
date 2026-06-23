# Evidence Records

این پوشه برای شواهد قابل بازتولید است.

## ساختار پیشنهادی

```text
evidence/
├── sources/   # Source Recordهای مستقل
├── images/    # Image Evidence Recordها
├── claims/    # Claim Recordهای اتمیک
└── fixtures/  # Fixtureهای واقعی یا مصنوعی با برچسب صریح
```

فایل‌های Schema در `schemas/` قرار دارند.

اسناد Legacy فعلی Source Snapshot و Claim Record کامل ندارند. این کمبود در `manifests/evidence-gaps.yaml` ثبت شده و تا رفع آن authoritative نیستند.
