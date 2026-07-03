# EDIS Rolling Queue

## Status

`implementation_status: dry_run_planner_with_external_executor`

The repository controller remains a deterministic planner and never overrides EDIS truth. Repository mutation is performed by the scheduled external executor through reviewed branches and pull requests.

## Sources of authority

- `manifests/stages.yaml`: canonical stage state.
- `manifests/work-items.yaml`: migration pipeline state.
- Evidence records and ledgers: factual traceability.
- `planning/ROLLING_QUEUE.json`: execution intent only.
- GitHub PRs and CI: change and enforcement boundaries.
- `planning/QUEUE_STATUS.md`: generated human-readable queue view.

## Hourly execution slice

One scheduled run may plan and complete a coherent execution slice instead of one tiny edit:

1. Select one highest-value primary task. This is the only task allowed to mutate shared stage, Work Item, ledger, queue, registry, or generated truth.
2. Select up to three additional preparation tasks when they are explicitly preparation-only, target a different stage (or no stage), and cannot affect release order.
3. Batch every safe same-scope edit for the primary task into one pull request.
4. Keep exact-head CI and the one-active-shared-mutation rule unchanged.
5. Stop the slice on a P0 reconciliation diagnostic, an external permission gate, or an unmet required review.

`tools/queue_controller.py` reports both the backward-compatible `selected_task` and the full `selected_tasks` execution slice. The default preparation capacity is three unless `max_planned_preparation_tasks` is explicitly set by a future compatible queue schema.

## Atomic stage finalization

Finalization is a two-phase trusted workflow:

- the content head is validated and converted to claim-level, machine-validated stage truth;
- the document trust fields, canonical gap registry, Stage, Work Item, generated artifacts, and ledger attestation are written back to the same migration branch;
- legacy provenance and snapshot gaps are resolved only when the corresponding claim records and captured source records validate;
- human review is never inferred, and the review gap remains open until a real review or fixture record exists.

This removes the need for separate PRs that only reconcile document, gap, Stage, Work Item, generated, or ledger state after each content change.

## Commands

```bash
python tools/queue_validate.py all
python tools/queue_reconcile.py --repo-state tests/fixtures/queue/repo-state-current.json
python tools/queue_controller.py --repo-state tests/fixtures/queue/repo-state-current.json
python validation/e2e/run_rolling_queue_check.py
```

## Write-mode boundary

The in-repository controller is still forbidden from direct GitHub mutation until optimistic-locking writes are introduced and approved. This does not block the external scheduled executor from using the plan through normal branch, PR, exact-head CI, and merge gates.
