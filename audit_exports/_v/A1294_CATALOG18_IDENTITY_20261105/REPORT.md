# A1294 catalog identity and terminal 18 checkpoint

## Result

The original-array correspondence obstruction is closed in Lean for the 171 declaration references in the frozen terminal-18 catalog. The exact generic list-to-array split theorem is proved under `Init`, the generated blocked catalog is proved equal to the original catalog, and the historical inline terminal-18 catalog is proved equal to that same array. All 171 lookups are proved on both the blocked and original arrays. Terminal 18's Boolean acceptance and the generic leaf soundness theorem are kernel checked, including transport back to the historical inline catalog. The bounded source-connected node-57 replay is also kernel checked with exact cursor exhaustion `(11,6)`.

This does not kernel-decode the original V2 byte streams or prove the external deterministic catalog-selection conversion. The Lean results apply to the exact literals and source structures in the compiled modules; Python/source evidence maps those literals to the frozen V2 package. The complete A1294 root predicate is OPEN.

## Decisions

See `DECISIONS.json`. In summary: `GENERIC_ARRAY_IDENTITY=KERNEL_PROVED`; `ORIGINAL_ARRAY_CORRESPONDENCE=KERNEL_PROVED`; `HISTORICAL_CATALOG_CONNECTION=KERNEL_PROVED`; `ALL_171_LOOKUPS=KERNEL_PROVED`; `TERMINAL18_ACCEPTANCE=KERNEL_PROVED`; `NODE57_REPLAY_AND_PREDICATE=KERNEL_PROVED`; `SOURCE_BYTE_AND_SELECTION_BRIDGE=EXTERNALLY_CHECKED`; `FULL_ROOT_PREDICATE=OPEN`.

## Exact Lean result

`Catalog18Identity.original_eq_catalog : Catalog18.original = Catalog18.catalog`.

The theorem is derived from the parametric `List.append_toArray` identity, with blocks preserving all 171 ordered references and lengths 57+57+57. The proof does not unfold `MacroPiece`, `refinementPiece*`, or `macroPiece*` computational definitions. `Terminal18CatalogConnection.historicalTerminal18_eq_original` connects the original three-inline-array expression in the preserved terminal-18 source to `Catalog18.original`; a second theorem connects it to `Catalog18.catalog`.

`Terminal18HistoricalAcceptance.accepted_on_historical_catalog` proves the exact `compactQuadraticLeafCheck` on the historical catalog evaluates to `true`, and `leaf_sound_on_historical_catalog` derives the upstream soundness result. The accepted proof retains the source witness. The exact rational tangent is

`805762688477455194592676257298467787 / 50000000000000000000000000000000000000`

and its exact margin over `A = 647/50000` is

`158762688477455194592676257298467787 / 50000000000000000000000000000000000000`.

Both are positive; the comparisons were checked in Lean and independently with rational arithmetic. Terminal 18 contains 15 model rows and 350 segment decoder occurrences in the original source. The current compact proof module proves all 15 row checks and the acceptance/tangent checks; source-normalization verification confirms the historical witness, segment declarations, model data, box, anchor, and tangent are unchanged outside the catalog-storage and catalog-lookup proof bridge.

`Node57.replay57` proves the bounded replay equation with result `some (11,6)`. `Node57Final.cursor_counts` proves the stream lengths are 11 topology entries and 6 payloads; `Node57.source_connected_predicate` proves `BoxPredicate (affineEnergyGoal A B) Source57.parentBox` through the existing upstream replay soundness route. The proof reuses the verified node-59 subtree objects.

## Generic identity

`CatalogArrayIdentity.toArray_append3` proves for arbitrary `α` and arbitrary lists `xs`, `ys`, `zs`:

`((xs ++ ys) ++ zs).toArray = (xs.toArray ++ ys.toArray) ++ zs.toArray`.

The `2+2+2` and `3+3+3` examples are proved from this generic theorem. The original 57+57+57 array identity is an application to concrete declaration-reference lists. Only proof irrelevance/classical infrastructure from Lean's standard theory appears in printed axiom dependencies; no custom axioms, `sorryAx`, `native_decide`, or unproved acceptance premises occur in successful modules.

## Build and resources

Pinned source/compiler checks and successful build measurements are in `environment_pinned.log` and the individual `*.log` files. The minimal `Init` theorem compiled in 1.90 s at 518,752 KiB peak RSS (1,389 major faults). The heavy project imports dominate: the original catalog identity build was 68.71 s / 5,489,960 KiB / 158,285 major faults; all 171 lookups 72.05 s / 5,497,184 KiB / 169,579 faults; terminal-18 compact acceptance 82.65 s / 5,493,768 KiB / 160,981 faults; historical catalog acceptance transport 66.59 s / 5,473,276 KiB / 154,369 faults; node-57 final replay/statements 69.30 s / 5,495,436 KiB / 166,997 faults. These are recorded one-at-a-time runs; they are not evidence of low memory use. `-M6800` bounded the Lean process and no swap was recorded.

A Windows/native `.olean` could not be imported in the pinned Linux environment (`incompatible header`). That cross-architecture import failure is preserved as a tool-format failure, not a mathematical failure; the pinned WSL `.olean` was built from the same source and used for project proofs.

For Windows packet extraction, the copied predecessor dependency directories were shortened to `reference/deps/n59`, `n61`, `n63`, and `n65` after a 298-character path exceeded the host extraction limit. The copies' file bytes are unchanged; the extraction attempts and resolution are preserved in `failed_drafts/packaging/extraction_attempts.log`.

## Source, catalog, and provenance boundary

The frozen V2 ZIP SHA-256 is `3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5`. Its CRC and the topology/kind/anchor/catalog-stream hashes are verified by the included source recheck. The extraction and deterministic selection procedure are replayed in Python. The Lean kernel checks the supplied literals and the structural equality of the two Lean arrays; it does not parse/authenticate the V2 ZIP bytes or prove the Python selection algorithm equivalent to the literal generator. These remain external correspondence obligations.

The VRK-style claim/evidence record uses the copied implementation's canonical JSON digest and evidence-root functions solely to bind local identities. It is unsigned and is not a mathematical proof or cryptographic trust anchor. The copied protocol verifier is provenance tooling, not an extension of Lean's kernel.

IntentSeal lineage identities are separated in `lineage_identification.json`: final published lineage hash `05ba923c…e5d4c0`; historical inventory hash `14f920b5…5dd56db`. Neither historical ZIP was altered.

## Remaining obligations

1. Formally parse the original V2 topology, anchor, catalog, and payload bytes in Lean (or prove a trusted external parser's output corresponds to the bytes).
2. Prove the deterministic catalog-selection procedure's output corresponds to the exact selected model/segment literals.
3. Prove the complete root `BoxPredicate` for the initial `GapBox 60` from a complete authenticated certificate. This checkpoint proves only the bounded node-57 source-connected subtree.
4. Do not infer a full A1294 theorem, any WP84 theorem, a zero-density improvement, or RH from these finite subtree results.
