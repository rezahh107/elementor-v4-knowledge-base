# EDIS Rolling Queue

## Status

`implementation_status: legacy_compatibility_only`

The rolling queue is retained for historical validation. It is not the active scheduler input.

Active planning contracts:

- `planning/WORK_PACKAGE_CATALOG.json`
- `planning/WORK_PACKAGE_QUEUE.json`
- `config/work-package-planner.json`
- `.github/workflows/work-package-control-plane.yml`

Use `python tools/work_package_validate.py all` to validate current planning contracts. Legacy queue commands remain available only for their existing compatibility tests.

The in-repository planner is read-only. The external execution boundary is documented in `docs/operations/work-package-execution-contract.md`.
