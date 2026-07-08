# Work Package External Execution Contract

status: `insufficient_evidence`

The repository contains a deterministic hourly planner. No in-repository evidence currently proves that an external mutation executor is installed, enabled, or consuming planner output. This document defines the required boundary; it does not claim that the external executor exists.

## Input

The executor may consume only a successful `Work Package Control Plane` run containing an observed repository state and deterministic plan.

Before mutation, it must re-read GitHub state and reject the plan when:

- the observed `main` SHA changed;
- the selected mutation PR head changed;
- a second mutation PR exists;
- required CI or review evidence is stale;
- the selected Work Package is no longer `active` or `ready`.

## Mutation boundary

The executor must:

1. use a branch named `automation/wp-<work-package-id>-<scope>`;
2. apply the `work-package` label to its PR;
3. preserve one primary Work Package objective;
4. never write directly to `main`;
5. never create status-only, bookkeeping-only, keepalive, reserve, or placeholder mutations;
6. preserve unknown, ambiguous, conflicting, and unavailable evidence states;
7. use the existing source-capture and repository validation boundaries.

## Reconciliation boundary

For an open mutation PR, the executor must:

1. re-read the exact head SHA;
2. inspect the required `KB Quality` run for that exact head;
3. inspect current review states;
4. apply only same-scope fixes;
5. use same-head rerun or workflow-dispatch recovery before creating a new commit solely for CI;
6. merge only with `expected_head_sha`;
7. verify current `main` after merge.

A planner result of `eligible_for_external_merge_reconciliation: true` is not a merge instruction. It shows only that the configured gates visible to the planner were satisfied at capture time. The executor remains responsible for a fresh exact-head check immediately before merge.

## Lifecycle reconciler gate

The Work Package planner must run only after the PR Lifecycle Reconciler has emitted a canonical `lifecycle-plan.json` for the same captured GitHub snapshot.

Required order:

1. capture current GitHub state;
2. run the PR Lifecycle Reconciler;
3. stop before planning when `planner_gate.new_work_allowed` is `false`;
4. run the Work Package planner only when lifecycle reconciliation allows new work;
5. select at most one substantial Work Package stage;
6. publish lifecycle and planner artifacts.

The planner must not start new Work Package work while an open mutation PR exists. Multiple open mutation PRs must be classified and reconciled first. Safe superseded draft PRs may be closed only by the PR Lifecycle Reconciler and only when the strict conditions in `docs/operations/pr-lifecycle-reconciler.md` pass.

## Major-work rule

A run satisfies the major-work rule only if it performs one of these actions:

- completes one Work Package stage through capture/finalization/validation;
- fixes a P0/P1 automation defect with tests;
- reconciles PR congestion that blocks Work Package progress;
- completes PR-Inspector read-only review artifacts for an active mutation PR;
- closes or cleans superseded PRs that unblock the planner;
- makes final exact-head gate visibility deterministic.

Bookkeeping-only changes must not be represented as completed Work Package work.

## Final exact-head gate

Finalization must dispatch KB Quality with `ref` and `expected_sha` inputs equal to the attested head SHA. The finalizer must record a visible final result containing:

- `run_id`;
- `head_sha`;
- `conclusion`;
- limitations, when the run cannot be uniquely observed.

Allowed labels are:

- `final-check-passed`;
- `final-check-failed`;
- `final-check-insufficient-evidence`.

Success must not be claimed when the dispatched run cannot be observed.
