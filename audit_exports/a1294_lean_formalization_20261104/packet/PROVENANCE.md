# Provenance and source mapping

## Frozen references

- Local research worktree base for this task: `7f3394c5655238b1e9736f91233d0bcc4c49fd43`.
- Pinned upstream source: `anthropics/formal-math@fba91d214655aaa1fd0504bb893c8859c20c79f9`.
- Pinned project: upstream `zeta23`, with `lean-toolchain` and `lake-manifest.json` copied
  into `source/upstream/zeta23/`.
- Pinned Mathlib revision: `51e6992efd06126df61a496bebf8f49482a4e129`.
- Compiler commit: `d8b18978322de05a8f3dba51ef03cf5461676c17`, Lean 4.33.0-rc2.

## A1294 input

The supplied V2 ZIP SHA-256 is
`3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5`; its ZIP CRC test
passed with 15 entries. The three certificate stream hashes are listed in
`evidence/source_tail_leaf.json` and `PROOF_STATUS.md`. The source-free replay result is
included separately with SHA-256
`7de6a70671dee42307847e3b321389f1bdfcae66f8bc73b99b0227a6c8e54db0`.

## Catalog comparison

`scripts/compare_catalogs.py` parses each exact rational model from the V2 JSON and the
pinned Lean declaration files. It found 56/56 stable, 216/216 v1, and 394/394 v2 exact
field matches with zero mismatches. This is a Python comparison, not a kernel theorem.
The V1/V2 JSON contains `stable_piece_index` owner metadata; the compared Lean `MacroPiece`
records do not carry that field. Its selection relationship remains an unproved dependency
for the full quadratic certificate.

## Lean dependency graph

The pilot imports `AffineTree.lean`, which imports `PieceCert.lean` and `Energy.lean`.
`PieceCert.lean` imports `KernelInterval.lean`; that imports `Kernel.lean` and
`TrigInterval.lean`; `TrigInterval.lean` imports `Interval.lean`. These exact source files,
catalog definition files, project lockfiles, and license notice are included. Mathlib source
and cache are pinned but not bundled.

## Working-copy status

The upstream clone's tracked tree remained at the pinned commit and clean. The only local
addition in that isolated clone was `Zeta23/ThmD/Sextuple/A1294Pilot.lean`. The research
worktree's tracked historical files were not changed; packet and logs are additive audit
artifacts.
