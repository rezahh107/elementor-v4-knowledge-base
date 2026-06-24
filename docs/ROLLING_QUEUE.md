# EDIS Rolling Queue

## وضعیت

```yaml
implementation_status: dry_run
truth_authority: none
```

این Control Plane فقط اقدام اجرایی بعدی را انتخاب می‌کند و هیچ Fact یا Evidence state را ایجاد، اصلاح یا ارتقا نمی‌دهد.

## منابع حقیقت

- `manifests/stages.yaml`: وضعیت Canonical مراحل.
- `manifests/work-items.yaml`: وضعیت Pipeline مهاجرت.
- Evidence records و Ledgerها: زنجیره شواهد.
- `planning/ROLLING_QUEUE.json`: قصد اجرایی، نه حقیقت EDIS.
- GitHub PR و CI: مرز تغییر و Enforcement.
- `planning/QUEUE_STATUS.md`: نمای انسانی و غیرهنجاری.

## مرز PR A.2

Controller در این نسخه فقط Dry Run است. Queue را Validate می‌کند، Work Itemهای محلی و Snapshot صریح GitHub را می‌خواند، Drift را گزارش می‌دهد و دقیقاً یک Task واجد شرایط را انتخاب می‌کند.

این نسخه هیچ GitHub mutation، تغییر Evidence، Merge، Lease واقعی یا Automation scheduling انجام نمی‌دهد.

## فرمان‌ها

```bash
python tools/queue_validate.py
python tools/queue_reconcile.py --repo-state tests/fixtures/queue/repo-state-current.json
python tools/queue_controller.py --repo-state tests/fixtures/queue/repo-state-current.json
python -m pytest tests/test_rolling_queue.py
```

## Gate ارتقا به Write Mode

1. Queue Schema، Spec Hashها، State Machine و Event Ledger در Python 3.11 و 3.13 پاس شوند.
2. Fixture فعلی به‌طور قطعی `RQ_DUPLICATE_PR`، `RQ_WORK_ITEM_DRIFT` و `RQ_CI_MISSING_JOBS` تولید کند.
3. علت `action_required` با Job واقعی اثبات و اصلاح شود.
4. PR جداگانه Optimistic Locking و Lease persistence را اضافه کند.
5. ناظر قدیمی تا زمان تأیید Write Mode غیرفعال بماند.
