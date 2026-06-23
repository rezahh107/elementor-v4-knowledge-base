# Queue Manager Contract v2

## وضعیت فعلی

`queue.enabled: false`

صف در دوره Hardening متوقف است.

## Preflight

مدیر صف قبل از Scheduling باید:

1. `manifests/stages.yaml` را بخواند.
2. تأیید کند Queue فعال است.
3. `python tools/kb.py validate --strict` را با نتیجه موفق اجرا کند.
4. تأیید کند Generated Artifacts تازه‌اند.
5. تعداد PRهای پژوهشی باز را بشمارد.
6. فقط اولین Stage `not_scheduled` را طبق `queue_priority` انتخاب کند.

## Concurrency

تا وقتی Merge Queue مستقل پیاده نشده:

```yaml
max_active_research_tasks: 1
```

## اجرای Stage

- Branch مستقل `kb/KB-XXX-slug`
- Source Record و Fingerprint
- Image Evidence Ledger
- Claim IDs و Locators
- سند فارسی
- Content Commit
- Canonical Manifest + append-only Ledger
- Generated Artifacts
- Validation و Test
- Pull Request

مدیر صف حق Push مستقیم به `main` یا اعلام Review ندارد.

## Failure

در شکست دریافت منبع، Commit یا CI:

- Stage به‌طور خودکار completed نمی‌شود.
- Event `failed` یا `blocked` به Ledger اضافه می‌شود.
- Evidence Gap لازم ثبت می‌شود.
- صف Fail-closed باقی می‌ماند.
