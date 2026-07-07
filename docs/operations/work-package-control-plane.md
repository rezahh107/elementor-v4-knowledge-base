# Work Package Control Plane

The repository planning unit is a Knowledge Work Package, not an isolated task.

## Authority order

1. current main contracts and schemas
2. verified source records
3. validated fixtures and checks
4. normalized knowledge entries
5. execution intent

Operational files never upgrade factual truth.

## Execution policy

- One active Work Package mutation at a time.
- Existing mutation PRs are reconciled before new mutation work.
- Same-objective changes are completed together when safely reviewable.
- Status-only, bookkeeping-only, placeholder and reserve work are invalid objectives.

## Replenishment

Catalog refresh is state driven:

- ready depth below threshold;
- material verified source drift;
- architecture/schema changes;
- real capability gaps.

It is not triggered by completed task count, elapsed time, CI polling, or queue maintenance.

## Legacy migration

`planning/ROLLING_QUEUE.json` is retained as historical execution intent. The capability catalog and control state are the active planning contracts.
