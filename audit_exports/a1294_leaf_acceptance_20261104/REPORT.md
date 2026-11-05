# Terminal-22 acceptance isolation

Decision: EVALUATION_BLOCKED_AT_EXACT_SUBCHECK.

The first compiler-local blocking expression in compositional_build.log is:

interpCompactRow catalog row6 = some (ModelRow.floor 0 segments6)

At CompositionalLeaf.lean:946, rfl did not establish definitional equality. Row 10 has the same zero-floor normalization failure. The decoder retains interpRat ⟨0,1⟩ while the expected literal is rational zero. These expressions require a proved rational normalization step; no Boolean-false witness was produced. The two direct rows (1 and 13) separately stopped at the expanded macroPiece11.check = true goal. The proposed proof applies the existing pinned macroPiece11_check theorem before unfolding that declaration.

The corrected source CompositionalLeaf.lean explicitly normalizes the two zero floors and changes only proof steps for direct-piece checks. It has NOT been compiler verified: its build invocation returned Wsl/Service/ERROR_TIMEOUT before Lean output. A read-only responsiveness check also failed with Wsl/Service/CreateInstance/ERROR_TIMEOUT. No WSL restart, process termination or environment installation was performed. This environmental failure is not a mathematical rejection or evidence of memory exhaustion.

Clean kernel results obtained in this revision are first_floor_canonical, first_catalog_ref and first_segment_decode in Checkpoints.lean. The canonicality proof has no axioms; the lookup/decoder proofs report propext, Classical.choice and Quot.sound. Checkpoints.olean and the successful build log are included.

The attempted compositional build contains fifteen separate canonicality checks and decoder equalities, thirteen exact interval-coverage and piecewise-envelope checks, 208 separate sourceSegmentCheck proofs, fifteen compactRowCheck proofs, exact distance-interval correspondence, rational tangent arithmetic, tangent acceptance, and final assembly. Its compiler reported four local errors: decode_6, decode_10, row_checked_1 and row_checked_13. Other declarations produced no errors, but the module failed and its final accepted/leaf_sound reports contain sorryAx. Accordingly this module is NOT counted as a successful leaf proof. Dependent row6/row10 and final assembly are not certified results. subcheck_ledger.json lists 288 exact checkpoint expressions with explicit statuses; no entry infers false from failure to reduce. The corrected-build results remain unknown.

All 208 original source segments remain present, including zero-floor rows 6 and 10. All selected catalog declarations, compact endpoint/floor records, box and anchor remain the unchanged authentic declaration prefix from the prior leaf input. The frozen ledger SHA-256 is 9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072. verify_preservation.py checks prefix identity, this hash, and the 208 source/208 segment-proof count in normal Python, -O and -OO. Those external checks pass. They do not prove original-byte decoding inside Lean. Catalog-index-to-literal correspondence, original topology/anchor decoding and cryptographic file provenance remain external; no new ownership assumption is introduced into the generic model soundness theorem.

Resources, measured with the same pinned compiler/imports and sequential /usr/bin/time -v timeout 240 commands:

| Build | Result | Wall seconds | Peak RSS KiB | Major page faults |
|---|---|---:|---:|---:|
| Prior import-only baseline | PASS | 84.02 | 5323240 | 116885 |
| Three isolated checkpoints | PASS | 110.70 | 5490504 | 162116 |
| Compositional leaf v1 | FAILED, four local proof errors | 121.83 | 5493672 | 165120 |
| Corrected leaf v2 | WSL service timeout | unavailable | unavailable | unavailable |

There is no successful complete-leaf object or acceptance-build benchmark. The checkpoint object is 2047424 bytes. Cache and paging states were not controlled; no incremental-memory or compression claim is made. The prior generic theorem and historic two-leaf proof remain valid and unchanged. Full A1294 remains NOT_YET_PROVED. No full-tree, extra-leaf or Downloads work was performed.

Pinned Lean 4.33.0-rc2; upstream fba91d214655aaa1fd0504bb893c8859c20c79f9; Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. Upstream local sources and lockfiles are bundled; Mathlib itself is not vendored. The generator currently uses the previous local authentic source as its declaration-prefix reference; AuthenticDeclarationPrefix.lean is also bundled to support offline inspection. Build and failed-source versions are preserved. The next action is to rerun the corrected compositional source in the same pinned environment once WSL responds, then inspect any remaining exact subcheck error without changing certificate data.
