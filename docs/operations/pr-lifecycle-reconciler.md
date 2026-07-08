# PR Lifecycle Reconciler

## Status

- `schema_version`: 1
- `implementation_status`: implemented
- `evidence_boundary`: lifecycle metadata only
- `mutation_authority`: PR Lifecycle Reconciler only

The PR Lifecycle Reconciler is a separate automation layer. It does not execute Work Packages, capture source evidence, finalize evidence, approve PRs, merge PRs, or modify repository evidence files.

## Pipeline position

Each automated run must follow this order:

1. Capture current GitHub state.
2. Classify open PRs.
3. Fetch review submissions and review threads.
4. Apply deterministic review disposition rules.
5. Detect superseded PRs.
6. Safely close superseded draft PRs only when strict policy conditions pass.
7. Re-read GitHub state after lifecycle reconciliation before Work Package planning.
8. Run the Work Package planner only when `planner_gate.new_work_allowed` is `true`.

The standalone workflow is `.github/workflows/pr-lifecycle-reconcile.yml`. The Work Package control plane runs the same reconciler before planning.

## Inputs

- `config/pr-lifecycle-policy.json`
- Current GitHub snapshot from `tools/github_state_snapshot.py`
- Optional PR-Inspector read-only gate output

`tools/github_state_snapshot.py` captures open PRs, exact head SHAs, labels, latest review submissions, GraphQL review threads with resolved state, and exact-head workflow runs.

## Canonical output

The reconciler emits canonical JSON with sorted keys and finite-number validation:

```json
{
  "schema_version": 1,
  "observed_at": "2026-07-08T00:00:00Z",
  "repository": "owner/repo",
  "actions": [],
  "planner_gate": {
    "new_work_allowed": false,
    "reason": "open mutation PRs must be reconciled first"
  }
}
```

## Classifications

Allowed PR classifications are:

- `active_mutation`
- `draft_in_progress`
- `superseded_must_close`
- `blocked_by_review`
- `blocked_by_ci`
- `blocked_by_missing_final_gate`
- `repair_required`
- `ready_for_human_review`
- `ready_to_merge`
- `must_not_merge`
- `insufficient_evidence`

## Review dispositions

Allowed review dispositions are:

- `accepted_fixed`
- `accepted_superseded`
- `accepted_deferred`
- `rejected_with_contract`
- `rejected_with_evidence`
- `insufficient_evidence`
- `unresolved_blocker`

A PR cannot become ready for human review or merge while any review thread has `unresolved_blocker` or lacks a disposition.

Explicit dispositions may be provided in a review comment with:

```text
pr-lifecycle-disposition: rejected_with_contract
```

The marker is deterministic and must use one of the allowed disposition values.

## Superseded PR closure policy

The reconciler may close a superseded PR only when all conditions are true:

1. PR is open.
2. PR is not merged.
3. PR is draft or has the `superseded` label.
4. Replacement PR exists.
5. Replacement PR covers the same stage.
6. No unique completed ledger event would be lost, evidenced by `unique_completed_ledger_event: false` in the snapshot or the `no-unique-ledger-event` label.
7. Every review thread has an explicit disposition.
8. A lifecycle comment is posted before closing.
9. The close action appears in `lifecycle-plan.json` as an allowed mutation.

If any condition is missing, the reconciler emits `insufficient_evidence` and applies only comment/label mutations.

## PR-Inspector integration

PR-Inspector is integrated as a read-only gate. The workflows clone `rezahh107/PR-Inspector`, validate `protocol-manifest.yaml`, and require:

- `operation_mode: read_only_review`
- forbidden default actions for target-repository mutation, commenting, approving, and merging
- a repository validation command

The lifecycle reconciler may consume PR-Inspector artifacts, but PR-Inspector must not close PRs, resolve threads, approve, merge, create source records, or execute Work Packages.

## Mutation rules

Allowed lifecycle mutations are:

- `comment`
- `resolve_thread`
- `close_pr`
- `label`

The reconciler never performs source/evidence mutations and never merges PRs.

## Validation commands

```bash
python -m compileall tools tests
python -m pytest
python tools/work_package_validate.py all
python tools/work_package_controller.py --repo-state tests/fixtures/pr_lifecycle/superseded_draft.json
python tools/pr_lifecycle_reconcile.py --repo-state tests/fixtures/pr_lifecycle/superseded_draft.json
```

For PR-Inspector, run its manifest-declared repository validation command after cloning the read-only repository.
