# Work Package Control Plane

The repository planning unit is a Knowledge Work Package, not an isolated task.

## Authority order

1. current `main` contracts and schemas;
2. verified source records;
3. validated fixtures and checks;
4. normalized knowledge entries;
5. execution intent.

Operational files never upgrade factual truth.

## Implemented scheduler

`.github/workflows/work-package-control-plane.yml` runs at minute 17 of every hour and can also be dispatched manually.

Each run:

1. checks out the exact scheduler revision;
2. installs the pinned project dependencies;
3. validates Catalog, Queue, planner policy, and executable negative fixtures;
4. captures the current default-branch SHA, open PRs, labels, exact-head workflow runs, and latest review state;
5. produces a deterministic execution plan;
6. publishes the observed state and plan as a retained workflow artifact.

The workflow has read-only permissions and does not mutate repository truth.

## Execution policy

- One active Work Package mutation at a time.
- Only explicitly classified mutation PRs block new mutation work.
- Existing mutation PRs are reconciled before a new Work Package starts.
- Same-objective changes are completed together when safely reviewable.
- Status-only, bookkeeping-only, placeholder, reserve, keepalive, and isolated-guard-only objectives are invalid.
- Exact-head CI and blocking review states remain external merge gates.

Mutation PR classification is explicit:

- label: `work-package`; or
- a configured automation or migration branch prefix in `config/work-package-planner.json`.

An unrelated human or dependency PR does not block Work Package selection.

## Runtime truth

Volatile GitHub state is captured from the GitHub API. The current `main` SHA is not stored as static control truth.

`config/work-package-planner.json` records active policy and boundaries. `planning/CONTROL_STATE.json` is retained as superseded historical state. The workflow artifact records the actually observed SHA, PRs, checks, and reviews for one run.

## Replenishment

Catalog refresh is state driven:

- ready depth below threshold;
- material verified source drift;
- architecture or schema changes;
- real capability gaps.

It is not triggered by completed task count, elapsed time, CI polling, merge events, or queue maintenance.

## External execution boundary

The in-repository workflow is a deterministic planner, not an evidence-authoring agent. The required external mutation contract is documented in `docs/operations/work-package-execution-contract.md`.

External executor availability is currently `unverified_external_dependency`. Do not describe the system as fully autonomous until a real executor run and its GitHub mutations are observed and validated.

## Legacy migration

`planning/ROLLING_QUEUE.json` is retained as historical execution intent. It is not the active scheduler input. The active planning contracts are:

- `planning/WORK_PACKAGE_CATALOG.json`;
- `planning/WORK_PACKAGE_QUEUE.json`;
- `config/work-package-planner.json`.
