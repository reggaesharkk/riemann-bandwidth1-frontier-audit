# A1294 authentic quadratic terminal: proof audit

## Decision

The first source-serialized quadratic terminal is kernel-proved on its exact rational box. Its five anchor coordinates, fifteen effective partial lower models, exact rank tangent, and resulting A1294 box predicate are checked in the pinned Lean environment. The correspondence between the serialized stream prefix and the explicitly encoded Lean path is hash-checked by the Python extractor; Lean does not parse or authenticate the complete serialized tree.

## Exact statement

Let `g : Fin 5 → ℝ` satisfy the leaf box `sourceLeafBox` in `A1294QuadraticLeaf.lean`: coordinates 0, 1, 3, and 4 lie in `[0, 15/2]`, and coordinate 2 lies in `[0, 15/4]`. With

* `A = 647/50000`,
* `B = 1094977/5000000000`,

the kernel-checked theorem `authentic_quadratic_leaf_box_predicate` proves

`A ≤ sextupleEnergy(g) + B * sextupleSpan(g)`.

The source-selected tangent lower value is exactly `14630385677/1000000000000`; subtracting `A` gives the strictly positive rational margin `1690385677/1000000000000`.

## Serialized leaf and path

The bounded extractor reads the frozen V2 streams after checking their manifest hashes. It finds the first terminal at zero-based topology node 16, terminal index 0, kind byte 1 (quadratic), with topology tokens

`[3,2,4,1,5,3,2,4,1,5,3,2,4,1,5,3,0]`.

The sixteen split axes are zero-based `[2,1,3,0,4,2,1,3,0,4,2,1,3,0,4,2]`; each split takes the left child. The five anchor codes are `[0,0,0,0,0]` at denominator 16384, read from byte offset 0. These give the exact box and anchor stated above. The exact prefix is retained in `quadratic_leaf_prefix.json`; the full model/segment ledger is `quadratic_leaf_source_ledger.json`.

The Lean theorem `source_path_reconstructs_box` proves that the sixteen explicitly written left splits from the upstream root box yield the stated rational box. Its input path is the path already extracted from the stream; the theorem does not prove that node 16 in the binary topology has those bytes. That serialization-to-path link remains an external, reproducible, SHA-256-checked extraction step.

## Fifteen lower models

The exact extractor reconstructs all fifteen source partials and records 969 rational segment selections. Each record contains the distance interval, catalog index, declaration name, owner index, exact source JSON item, segment infimum, and whether it attains that partial's minimum. Normal, `-O`, and `-OO` executions produce identical ledger objects.

The effective lower constants on the fifteen partials are zero except for zero-based pair 9, whose exact constant is `14630385677/1000000000000`. For each zero term, Lean proves the required inequality globally from `0 ≤ 2 * mtKernel x ^ 2`; this direct argument is valid on every recorded interval and does not rely on catalog ownership or refinement selection.

For pair 9, the source distance is exactly coordinate 2, with interval `[0,15/4]`. On `[0,2]`, upstream `MacroPiece0` has checked model value `1/4`; on `[2,15/4]`, upstream `MacroPiece1` has checked model value equal to the positive lower constant. The seam at 2 is included in both checked intervals, and the exact rational comparison `14630385677/10^12 ≤ 1/4` closes the left piece. `selected_pair9_model_valid` therefore proves the effective lower model over the entire source interval using upstream `MacroPiece.check_sound` certificates.

`selected_models_pairwise_valid` proves all fifteen effective models satisfy their required kernel inequality on the leaf box. Together with the exact `rankTangentCheck`, upstream `rankTangentCheck_energy_sound` yields the stated box predicate.

The upstream `checkedLowerPieceLeafCheck` / `checkedLowerPieceLeafCheck_sound` route and the corresponding `checkedLowerPieceAffineTree_sound` theorem were inspected but are not used for this single leaf. Their checked lower-piece representation is not the convenient way to encode this segmented positive floor as one full-interval piece: the source certificate supplies the positive floor on `[2,15/4]` and a weaker floor on `[0,2]`. The proof instead stays in the same upstream `AffineTree` framework and applies its rank-tangent soundness theorem after proving the exact piecewise model inequality over the whole distance interval. No result is imported from a geometric surrogate or from an unchecked owner claim.

## Catalog and owner semantics

The JSON-to-Lean comparison found exact field equality, with zero mismatches, for 56 stable, 216 refinement-v1, and 394 refinement-v2 source declarations. The JSON catalogs additionally carry owner indices for all 610 refinement entries; the Lean `MacroPiece` declarations do not encode those owner fields, and the comparison is not a Lean theorem about the selection algorithm.

For this leaf's final mathematical bound, the owner relation is bypassed safely: the proof directly establishes the selected effective lower model on each full partial interval, with a source-certified piecewise proof for the only positive constant and a global proof for each zero constant. Thus `CATALOG_OWNER_SEMANTICS` remains not formalized, but it is not an assumption of the kernel-checked leaf theorem. The 969-entry ledger preserves the external selector/owner evidence for independent inspection.

## Kernel and resource result

The final module builds at upstream commit `fba91d214655aaa1fd0504bb893c8859c20c79f9`, Lean `4.33.0-rc2` (compiler commit `d8b18978322de05a8f3dba51ef03cf5461676c17`), Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`. `lake build Zeta23.ThmD.Sextuple.A1294QuadraticLeaf` completed successfully (8,706 jobs). The exact final-source build log reports 1m23.15s wall time and 5,539,572 KB maximum resident set size. `#print axioms` reports `[propext, Classical.choice, Quot.sound]` for each printed theorem, with no `sorryAx` or custom axiom.

The one-leaf proof is practical in the pinned environment. This does not establish a resource estimate for the 13,454,121-node certificate. No mixed parent subtree or full certificate port was attempted.

## Scope limits

This proves one finite terminal predicate only. It does not prove completeness of the full topology, the global root-box certificate, an improved zero-density result, a percentage theorem, or RH. The full A1294 theorem remains unproved.
