# A1294 Lean kernel pilot packet

This packet records a narrow formalization pilot against `anthropics/formal-math` commit
`fba91d214655aaa1fd0504bb893c8859c20c79f9` and its pinned `zeta23` project. The original
research checkout, V2 ZIP, historical result, and upstream source commit were not changed.

## Verified results

- Lean 4.33.0-rc2 runs on the host Windows installation and in WSL2. The WSL Lake project
  uses the pinned Mathlib revision `51e6992efd06126df61a496bebf8f49482a4e129`.
- `lake build Zeta23.ThmD.Sextuple.AffineTree` passed. The final A1294 pilot module also
  passed under that source and toolchain.
- Lean proves the exact tail margin
  `60 * (1094977 / 5000000000) - (647 / 50000) = 49931 / 250000000 > 0`, the corresponding
  span-at-least-60 energy bound, and coverage of the complement of `[0,60]^5` for
  nonnegative gaps.
- Lean also checks the exact 25-split path to source tail leaf 6,676,785, its rational box,
  the one-node tail checker, and the resulting box predicate. This is a complete one-leaf
  subtree. It contains no quadratic terminal.
- `#print axioms` reports only `propext`, `Classical.choice`, and `Quot.sound`; there is no
  `sorryAx`, custom axiom, `admit`, or `native_decide` in the successful proof.
- The V2 ZIP hash, ZIP CRC, package preflight, stream hashes, and exact field comparison of
  all 666 catalog entries are recorded in `evidence/` and `logs/`.

## Scope limits

This does **not** kernel-check the 13,454,121-node A1294 tree, its 6,725,258 quadratic
terminals, the catalog owner-selection relation, or the global A1294 theorem. The prior
source-free Python full replay is included as evidence and was not rerun here. The catalog
comparison is an independent Python field comparison, not a Lean theorem connecting the
JSON owner metadata to the refinement selection. The source-stream-to-leaf location is
authenticated by SHA-256 plus the included deterministic structural extractor; that
prefix scan is not itself a Lean proof of all preceding certificate terminals.

The exact pinned upstream `AffineTree` build passed. A broader attempt to build the existing
A1290 certificate target expanded to 55,731 Lake jobs and was interrupted; its log is
preserved and is not reported as a proof failure or a pass. The complete Mathlib source and
compiled cache are not bundled, so this is an offline evidence packet, not a hermetic Lean
build image. The exact dependency lock and source revisions are included.

## Decisions

| Item | Decision |
|---|---|
| `HOST_LEAN_433` | VERIFIED |
| `PINNED_MATHLIB` | READY |
| `UPSTREAM_SEXTUPLE_BUILD` | PASS (`AffineTree` module) |
| `A1294_TAIL_KERNEL_PROVED` | YES |
| `A1294_SUBTREE_KERNEL_PROVED` | YES (one source tail leaf) |
| `CATALOG_CONNECTION` | CONDITIONAL |
| `FULL_PORT_RESOURCE_FEASIBILITY` | UNCERTAIN |
| `FULL_A1294_THEOREM` | NOT_YET_PROVED |

The next mathematical/formalization blocker is an exact source-matched quadratic terminal
pilot, including the selected catalog pieces and the JSON owner relation. Only after that
pilot succeeds should a chunked encoding of the full topology and all terminal streams be
designed and benchmarked.

See `REPRODUCE.md`, `PROVENANCE.md`, `PROOF_STATUS.md`, and `SHA256SUMS.txt`.
