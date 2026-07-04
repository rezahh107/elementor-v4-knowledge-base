# Automation Throughput Runbook

A controller task advances one stage to merge or to one verified external blocker. It is not a status poll.

Run stage mutation only through an explicit exact-head transaction. Capture current source truth, retain transport bytes as workflow artifacts, publish repository source records only for normalized-content changes, bind claims, reconcile gaps and Work Items, generate artifacts, attest the ledger, validate the final local head, verify the remote head is unchanged, and push once.

After that push, KB Quality is read-only and must pass on the exact head for Python 3.11 and 3.13. Merge with `expected_head_sha`, then validate `main`.

Draft/Ready toggles, reopen events, comments, timestamps, empty commits, unchanged blocker records, and pending-state commits are not valid triggers or durable work.

Only one active PR may mutate shared truth. While it waits, prepare later stages without changing manifests, ledgers, queue runtime, or global generated indexes.
