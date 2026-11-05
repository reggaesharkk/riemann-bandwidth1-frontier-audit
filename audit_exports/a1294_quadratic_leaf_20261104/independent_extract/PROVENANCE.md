# Provenance and source hashes

## Pinned revisions

* Upstream `anthropics/formal-math`: `fba91d214655aaa1fd0504bb893c8859c20c79f9`.
* Mathlib: `51e6992efd06126df61a496bebf8f49482a4e129`.
* Lean: `leanprover/lean4:v4.33.0-rc2`, compiler commit `d8b18978322de05a8f3dba51ef03cf5461676c17`.
* Current local Riemann worktree commit is recorded in `source_hash_inventory.json`.

## Frozen certificate inputs

* V2 package ZIP: SHA-256 `3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5`.
* Stable catalog JSON: `961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b`.
* Refinement-v1 JSON: `3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9`.
* Refinement-v2 JSON: `7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d`.
* Topology stream: `9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76`.
* Terminal-kind stream: `859e25cdff7379072c7a3928347b66dfbe762ff83c98035b0e3b591e9b533f06`.
* Anchor stream: `32e1264ab3c8350a31b9b8e1d260a16ef3ec82a71046378441f4f429dc4254f5`.
* Prior successful pilot ZIP (preserved byte-for-byte): `2e1284945636ce6de55b21ab686ae0835d4400e40b830c3226a304907311e949`.

The exact final Lean source, source-free package, upstream source files, evidence outputs, and prior packet have individual hashes in `source_hash_inventory.json` and `SHA256SUMS.txt`. The evidence ZIP contains the complete V2 ZIP and the prior successful pilot ZIP unchanged.

## What the hashes establish

The certificate package manifest hashes the input catalogs and serialized streams. The bounded extractor rechecks those values before producing the leaf path and model ledger. The catalog comparator checks the 666 model fields against pinned Lean declarations. Hash agreement and these finite comparisons authenticate the external source mapping; they do not turn the Python parser or owner-selection routine into a Lean theorem.
