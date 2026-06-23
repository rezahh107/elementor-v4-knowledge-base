## Stage / scope

- Stage IDs:
- Change type: content / evidence / schema / tooling / generated artifacts

## Evidence

- Source Records added or updated:
- Claim Records added or updated:
- Image Evidence inspected:
- Evidence Gaps opened/resolved:

## Validation

- [ ] `python tools/kb.py validate --strict`
- [ ] `python tools/kb.py generate --check`
- [ ] `python -m pytest`
- [ ] Generated files were not manually edited.
- [ ] Ledger changes are append-only.
- [ ] No status, SHA, review, or evidence result was guessed.

## Review

- [ ] Claim locators were checked against the source.
- [ ] `derived` claims include `derived_from`.
- [ ] `observed` claims only use inspected visual evidence.
- [ ] Authoritative status requirements are satisfied or explicit gaps remain open.
