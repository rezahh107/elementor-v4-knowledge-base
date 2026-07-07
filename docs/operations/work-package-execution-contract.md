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
