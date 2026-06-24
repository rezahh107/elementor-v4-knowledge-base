# EDIS Rolling Queue

## Status

`implementation_status: dry_run`

This control plane chooses execution work. It does not create or override EDIS truth.

## Sources of authority

- `manifests/stages.yaml`: canonical stage state.
- `manifests/work-items.yaml`: migration pipeline state.
- Evidence records and ledgers: factual traceability.
- `planning/ROLLING_QUEUE.json`: execution intent only.
- GitHub PRs and CI: change and enforcement boundaries.
- `planning/QUEUE_STATUS.md`: generated human-readable queue view.

## PR A.2 boundary

The controller is deliberately dry-run only. It validates the queue, reads local
STATUS and Work Item state, consumes an explicit GitHub state snapshot, reports
drift, and selects exactly one eligible bounded task. It performs no GitHub
mutation, no evidence mutation, no merge, and no automation scheduling.

## Commands

```bash
python tools/queue_validate.py all
python tools/queue_reconcile.py --repo-state tests/fixtures/queue/repo-state-current.json
python tools/queue_controller.py --repo-state tests/fixtures/queue/repo-state-current.json
python validation/e2e/run_rolling_queue_check.py
```

## Promotion gates

Write mode is forbidden until:

1. Queue schema, task hashes, transitions, leases, and JSONL pass.
2. The current drift fixture produces deterministic diagnostics.
3. CI passes on Python 3.11 and 3.13.
4. A separate approved PR introduces optimistic-locking writes.
5. The old prompt-driven supervisor remains disabled.
