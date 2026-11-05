# A1294 two-quadratic parent: proof audit

## Decision

| Obligation | Result |
|---|---|
| `TWO_QUADRATIC_LEAVES_SOURCE_AUTHENTICATED` | YES by a bounded exact replay of the frozen V2 archive (Python source bridge; not a Lean decode of raw bytes) |
| `BOTH_CHILDREN_KERNEL_PROVED` | YES for the two literal boxes reconstructed in the included ledger |
| `FIFTEEN_MODEL_VALIDITY` | YES for the fifteen literals on each child, by direct checked-domain and soundness proofs |
| `PARENT_COVERAGE_KERNEL_PROVED` | YES for the literal parent and its two exact midpoint halves |
| `PIECEWISE_ENVELOPE_CHECKER_REUSABLE` | YES as a generic Lean soundness lemma plus generated exact row-check proofs; source-stream decoder is not formalized |
| `CATALOG_OWNER_SEMANTICS` | Not used to prove envelope validity; mapping serialized catalog indices to Lean literals remains external |
| `SOURCE_SERIALIZATION_BRIDGE` | EXTERNALLY VERIFIED; NOT KERNEL-PROVED |
| `SMALL_SUBTREE_KERNEL_PROVED` | YES, complete two-terminal subtree (nodes 65–67) |
| `CHUNKED_BUILD_FEASIBILITY` | TWO-LEAF CHUNK COMPILES; larger chunks and full assembly remain open |
| `FULL_A1294_THEOREM_STATUS` | NOT YET PROVED |

No A1294 global theorem follows from this packet. No WP84, zero-density, greater-than-79%, or RH status changes.

## Exact frozen source and candidate

The V2 source archive is SHA-256 `3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5` (5,672,384 bytes). Its authenticated streams are:

- `topology-u8.bin`: `9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76`
- `terminal-kinds-u8.bin`: `859e25cdff7379072c7a3928347b66dfbe762ff83c98035b0e3b591e9b533f06`
- `anchors-u16le.bin`: `32e1264ab3c8350a31b9b8e1d260a16ef3ec82a71046378441f4f429dc4254f5`
- catalog `macro-data-exact.json`: `961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b`
- catalog `refinement-catalog-v1-exact.json`: `3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9`
- catalog `refinement-catalog-v3.json`: `7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d`

The bounded decoder verifies the archive manifest and CRC, then reconstructs topology node 65 (token 1, axis 0), children 66 and 67, and terminal stream indices 22 and 23 (kind byte 1, quadratic). The parent path has length 43; the children append the axis-0 lower/upper step and have length 44. The two children are the complete immediate binary split of this parent. This is a prefix replay through node 67, not full-certificate replay.

Each leaf has 15 selected rank models: two direct pieces and thirteen segmented-constant terms. The positive-floor terms contribute 400 rational segment rows total, 22 positive floors. Each anchor stream has five zero codes with denominator 16384, so its exact point is the lower corner. Exact parameters are `A=647/50000`, `B=1094977/5000000000`.

Parent box, in coordinate order:

`[405/64,105/16] × [825/128,105/16] × [795/128,405/64] × [825/128,105/16] × [405/64,105/16]`.

Left child box:

`[405/64,825/128] × [825/128,105/16] × [795/128,405/64] × [825/128,105/16] × [405/64,105/16]`.

Right child box:

`[825/128,105/16] × [825/128,105/16] × [795/128,405/64] × [825/128,105/16] × [405/64,105/16]`.

The exact tangent margins `rankTangentLower - A` are positive:

- left: `7760205129699356804065918948443215217/7812500000000000000000000000000000000000`;
- right: `156215021254826261948480423241409791537/2000000000000000000000000000000000000000000`.

The raw selected paths and all 15 model selections are preserved in `source/siblings_normal.json`; `source/siblings_O.json` and `source/siblings_OO.json` are identical independent replay outputs.

## Kernel proof

`source/A1294TwoQuadraticParent.lean` compiles under Lean `4.33.0-rc2` with the pinned upstream source at `fba91d214655aaa1fd0504bb893c8859c20c79f9` and Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`.

The generic checker is `sourcePiecewiseCheck` with soundness theorem `sourcePiecewiseCheck_sound` (in the generated module at line 177; prototype at line 176). It verifies nonempty interval lists, exact contiguous endpoint coverage, segment ordering, segment containment in the chosen model's validity box, and a rational floor below the segment minimum. Segment rows are checked individually with `norm_num`; the full 400-row module then assembles those checked rows. The proof invokes upstream `MacroPiece.check_sound` for every selected piece. Zero-floor rank terms are discharged by nonnegativity; direct pieces are handled by their checked source interval and the same upstream soundness theorem.

This proof does **not** invoke a catalog owner-selection theorem. Instead, for every model literal supplied by the authenticated extractor, Lean proves its checked domain contains the relevant source-distance interval and proves the model lower bound directly. Thus envelope validity does not depend on owner-selection semantics. The separate external bridge from serialized catalog indices to those literals remains outside Lean.

The child box predicates are `source_left_box_predicate` and `source_right_box_predicate` (lines 2722 and 2995). Each is derived from its exact rational tangent checker and the pointwise validity of all fifteen model terms, using upstream `rankTangentCheck_energy_sound` (AffineTree line 517). `source_children_match_parent_split` (line 2423) proves both literal child boxes equal the lower and upper midpoint halves of the literal parent box. `source_parent_box_predicate` (line 3004) applies upstream `boxPredicate_of_midpoint_children` (AffineTree line 763), so the parent conclusion covers every point in the parent box, including the shared midpoint boundary.

The command's `#print axioms` output for the box match, both child predicates, and parent predicate is respectively based on `[propext, Classical.choice, Quot.sound]`. It contains no `sorryAx`, no custom axiom, and the module contains no `sorry`, `admit`, or `native_decide`.

## Serialization boundary and limitations

The Lean kernel checks the exact rational literals and theorem statements in the module. It does not parse the V2 ZIP or prove that the external JSON extractor maps raw topology/catalog/anchor stream bytes to those literals. That link is independently replayed in normal Python, `-O`, and `-OO`, with equal output SHA-256 `9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072`, plus exact `Fraction` checks. Accordingly, the source authenticity decision is supported by the archive hash, manifests, bounded decoder, and replay tests, but is not a complete kernel proof of serialization.

The earlier optional attempt to fold all 43 ancestors inside Lean exceeded simplifier recursion/heartbeat limits; those failures are retained in logs. It is not needed for the kernel parent theorem: the parent/child literal relation is proved directly, while path-to-literal correspondence remains in the external source replay. Earlier v1–v6 parent builds are retained with their failures; v7 is the successful proof build.

## Resource result

The successful parent module source is 245,907 bytes; its compiled `.olean` is 14,407,976 bytes (SHA-256 `5c6fc561151c1da472d205cd787cb1ac6ef50b23c45b1b7adbc76ab9d6d1a2fa`). The v7 build took 63.86 seconds elapsed and peaked at 5,460,740 KiB RSS. A separate nine-segment row-check smoke build took 90.68 seconds and peaked at 5,672,564 KiB RSS. These are meaningful two-leaf/small-row measurements, but they show high fixed memory overhead. They do not establish that larger chunks or the 13,454,121-node tree can be assembled. No full-tree compilation was attempted.

## Reproducibility

See `README.md` for commands and exact prerequisites. `logs/parent_compile.log` through `parent_compile_v6.log` retain prior failures; `logs/parent_compile_v7.log` is the successful kernel build and axiom output. The packet also preserves the earlier pilot and quadratic-leaf packets unchanged.
