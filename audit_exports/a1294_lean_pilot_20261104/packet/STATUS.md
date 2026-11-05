# A1294 Lean kernel pilot — blocked at environment gate

This is a blocker/evidence packet, not a completed Lean pilot. The task's stop rule was applied because the pinned Lean environment could not be reproduced locally.

## Verified artifacts

- The included `source/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip` has SHA-256 `3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a`, matching the supplied digest.
- The ZIP test completed successfully and a separate extraction succeeded. The package's quick `preflight.py` printed `PREFLIGHT PASS`; that script checks schema/node count and file presence only. It is not the exact full replay.
- The included prior result record is the previously recorded full Python replay result, SHA-256 `7de6a70671dee42307847e3b321389f1bdfcae66f8bc73b99b0227a6c8e54db0`. It reports PASS over 13,454,121 nodes and 6,727,061 leaves. This turn did not rerun that multi-hour replay.

## Environment blocker

- Required upstream toolchain: `leanprover/lean4:v4.33.0-rc2`.
- Installed toolchains: `leanprover/lean4:v4.35.0` and `leanprover/lean4:v4.36.0-rc1`; current Lake is `5.0.0-src+eb6cafb`.
- WSL returned `Wsl/E_ACCESSDENIED`.
- An approved `elan toolchain install leanprover/lean4:v4.33.0-rc2` attempt entered the download step but made no progress. A public upstream checkout attempt then failed because this shell could not resolve `github.com`. The incomplete clone was removed after verifying it was confined to this new pilot directory.
- The pinned Mathlib revision is recorded in `UPSTREAM_PINNED_METADATA.txt`, but it is not present as a local Lake dependency. No Lean source was compiled, no `#print axioms` output exists, and no RAM/proof-size benchmark was taken.

## Decisions

| Item | Status | Evidence boundary |
|---|---|---|
| `PINNED_LEAN_ENVIRONMENT` | `BLOCKED` | Required Lean binary and matching local Mathlib tree unavailable; WSL denied; GitHub DNS unavailable in shell. |
| `A1294_DATA_AUTHENTICITY` | `INCOMPLETE` | Supplied ZIP digest and ZIP structure verified; this pilot stopped before input-to-upstream catalog comparison. |
| `A1294_SAMPLE_SUBTREE` | `OPEN` | No subtree was translated or kernel checked. |
| `CATALOG_CONNECTION` | `CONDITIONAL` | Existing audit records exact catalog correspondence, but this packet adds no new Lean-checked connection. |
| `A1294_TAIL` | `OPEN` | The rational identity is recorded in the prior certificate, but no Lean proof was compiled here. |
| `FULL_PORT_RESOURCE_FEASIBILITY` | `UNCERTAIN` | No Lean pilot measurements; prior Python runtime is not a Lean scaling estimate. |
| `FULL_A1294_THEOREM` | `NOT_YET_PROVED` | Neither the root certificate nor the tail was joined in the Lean kernel. |
| `NEXT_COMPUTATION_JUSTIFIED` | `NO` for full port | Resume only with the pinned toolchain and Mathlib available, then complete a small subtree pilot first. No new search is justified. |

This packet does not change any A1294 or WP84 theorem status.
