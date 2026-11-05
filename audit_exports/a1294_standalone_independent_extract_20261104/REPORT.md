# Independent compact terminal-22 acceptance

Research owner: Prince. Private additive experiment, 2026-11-04.

**Result: the independent acceptance theorem is kernel proved. This implementation does not improve total object size, compilation cost or peak memory; stop this architecture rather than adding more layers.** SharkBridge-01 remains an unchanged successful correspondence experiment with negative compression results.

| Required decision | Result |
|---|---|
| STANDALONE_COMPACT_ACCEPTANCE_PROVED | YES |
| ORIGINAL_ACCEPTANCE_IMPORTS_ELIMINATED | YES, confirmed by actual transitive module census |
| SOURCE_CORRESPONDENCE_STATUS | Typed index/compact/model decoding proved; original-byte and pinned-catalog correspondence remain external; optional path-to-box proof OPEN |
| TOTAL_OBJECT_SIZE_IMPROVEMENT | NO; measured increase |
| TOTAL_COMPILATION_COST_IMPROVEMENT | NO demonstrated improvement; measured increase |
| PEAK_MEMORY_IMPROVEMENT | NOT_DEMONSTRATED |
| NEXT_EXACT_BLOCKER | No acceptance-proof blocker. Performance break-even is unmet. The separate source-path normalization goal remains unresolved. |

## Minimal mathematical interface and dependency elimination

StandaloneCore.lean preserves the established generic mathematical prefix from A1294FifteenBridge.lean unchanged. It reuses source-piece envelope soundness, ModelRow/modelCheck_sound and upstream rankTangentCheck_energy_sound. Catalog definitions come from the exact upstream AffineTree, Macro.AffineAdapter and A1275.RefinementData imports. Source model ownership is not assumed in place of a proof: each selected segment's interval and mathematical piece check is verified.

The old default-valued decodedRow definition and its checker/soundness interface are omitted. The new explicitLeafCheck uses compactRowCheck, explicit mathematical models and rankTangentCheck. Its generic soundness theorem requires a proof that every interpCompactRow returns some of the supplied mathematical model. The interned wire decoder separately returns Option and requires success at every rational, segment and catalog lookup. No getD, get!, unchecked default or runtime PASS premise is used.

StandaloneTerminal22.lean imports only StandaloneCore. It checks 119 canonical rational records through their source row occurrences; 107 unique segments; 100 selected catalog declarations; all 208 original segment occurrences; and fifteen exact model rows. Each unique segment is checked at the maximum of the unchanged source floors using it. This maximum is one of the source floors, not an optimized replacement. A new small generic monotonicity lemma transfers the check to every other source occurrence. Each row's exact interval coverage and the original catalog piece checks are proved. Both direct macroPiece11 rows and the zero-floor rows are checked afresh.

The main fresh results are wire_success (interned indices decode to the compact rows), model_success (compact rows decode to the mathematical models), all_rows, tangent_checked, accepted and leaf_sound. None invokes any old concrete acceptance theorem. The final elaborated proof is exactly explicitLeafCheck_sound model_success accepted, as printed in leaf_build.log. Every printed axiom report is [propext, Classical.choice, Quot.sound]; no sorryAx, custom axiom, admit, native_decide or externally asserted Boolean appears in successful proof modules.

The actual mathematical statement is: for all g : Fin 5 -> real in

[405/64,825/128] x [825/128,105/16] x [795/128,405/64] x [825/128,105/16] x [405/64,105/16],

647/50000 <= sextupleEnergy(g) + (1094977/5000000000)*sextupleSpan(g).

The original lower-corner anchor and exact tangent lower bound 108853955129699356804065918948443215217/7812500000000000000000000000000000000000 are unchanged. This is terminal 22/node 66 only, not the parent or global A1294 theorem.

## Source correspondence and preserved failure

authentic_input.json is still SHA-256 9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072. verify_source.py independently reconstructs the exact source segment/floor stream from the generated interned definitions, and passes in normal/-O/-OO modes. data_certificate.json records the exact interned values. The kernel proves typed decoding success; it does not parse JSON, verify a SHA-256 digest, decode the V2 topology bytes or prove JSON-catalog field correspondence with pinned upstream declarations. These boundaries remain external. The unchanged original V2 archive is retained under frozen/ and hash recorded separately.

The bounded 44-midpoint-step path attempt is preserved in SourcePath.lean and source_path_build.log. A single bounded retry with kernel decide is preserved in SourcePath_v2.lean and source_path_v2_build.log. Both failed. The first unresolved retry goal is SourcePath_v2.lean:60:153, the lower coordinate-zero equality after expanding descend root steps. Lean reports that the Decidable instance for nested Fin equalities and rational numerators did not reduce to isTrue or isFalse. This is an evaluation/normalization blockage, not Boolean false or a source counterexample. The retry exited 1 after 122.57 seconds, peak RSS 5493172 KiB. Any sorryAx report in this failed module is not counted as proof. Neither failed module is imported by the successful acceptance theorem. No further path variants were attempted.

## Complete import census and dominant environment costs

Lean's actual environment header reports 10502 imported modules for the new theorem, versus 10501 for the original. The only module-set difference is StandaloneCore + StandaloneTerminal22 replacing Zeta23.ThmD.Sextuple.CompositionalLeaf. The new set has no old leaf, right leaf, parent, SharkBridge or historical acceptance module. Full module/source/path/size/hash records are in *_closure_complete.json; the raw censuses are preserved separately. The single initially unresolved Lake.Util.Casing source was located at the pinned compiler's src/lean/lake path, and is resolved in the additive complete inventories.

There are 10500 common modules, with 123596428 source bytes and 2731782456 primary .olean bytes. Upstream Sextuple.Interval imports all Mathlib. RefinementData alone is 440533672 .olean bytes and EnvelopeData is 97270320 bytes. Both architectures retain these common imports. The core/import RSS near 5.5 million KiB and the earlier import-only measurement support identifying the common environment as dominant; no isolated per-module RSS attribution was measured. This task does not rewrite the established upstream mathematical libraries or claim a new import-pruning theorem.

The complete new module census has 2744958000 primary .olean bytes and 8044897320 bytes of listed module artifacts including available companion/IR files. The baseline raw census has 2742860680 primary .olean bytes and 8042800000 listed artifact bytes. Its previously cached root object is 8 bytes smaller than this fresh baseline object; measurements.json explicitly adjusts the baseline primary-object closure to 2742860688 for the fresh artifact. Both root sources have the same original SHA-256. Source hashes resolve for every census module. This is a complete loaded-module census, not a minimal reachable-proof-constant graph, and excludes OS/runtime shared libraries and compiler binaries.

## Equivalent-condition measurements

Pinned Lean 4.33.0-rc2, compiler d8b18978322de05a8f3dba51ef03cf5461676c17; upstream fba91d214655aaa1fd0504bb893c8859c20c79f9; Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. Both implementations use the same installed dependencies, serial Lean processes, -M 6800 and bounded timeouts. The original theorem is compiled only as a separate performance baseline, never as an input to the new proof.

| Measure | Original self-contained leaf | Fresh standalone core + leaf |
|---|---:|---:|
| Local Lean source bytes | 148181 | 140348 |
| Local .olean bytes | 11078232 | 13175544 |
| Lean compile-process wall seconds | 118.47 | 201.13 |
| Peak RSS KiB | 5498500 | 5502300 |
| Summed major faults | 154915 | 296430 |

The new core takes 119.32 seconds, 5502300 KiB, 161860 major faults and emits 1230920 object bytes. The new leaf takes 81.81 seconds, 5377096 KiB, 134570 faults and emits 11944624 object bytes. Its warm-core time alone must not be compared with a complete old build. The new outer Lake/shell wrapper takes 206.57 seconds; the table uses summed Lean process times to compare equivalent units. The core and leaf both exit 0, as does the fresh old baseline.

Source sharing saves 7833 local source bytes, but total objects grow by 2097312 bytes. Peak-memory differences are too small and cache-dependent to support an improvement claim. Cache/paging states were not randomized or reset; this is one bounded comparison, not a statistical performance theorem. No pure kernel-only replay timing was isolated: compilation includes elaboration and kernel checking. Imported modules were used as ordinary pinned Lean objects; a full -t0 recheck of Mathlib was not attempted. Audit and failed path-module build costs are separately logged and not hidden in the acceptance timings.

## Stop decision

The architectural independence milestone is complete: an authentic leaf can be checked without historical acceptance imports. The requested lower-cost architecture is not demonstrated. Stop here, preserve the proof and measurements, and do not add another decoder layer, terminal 23, node 63 or full-tree build. Complete byte-source authentication and the optional typed path normalization remain separate obligations. Full A1294, all frozen WP84 conclusions and SharkBridge's negative compression results remain unchanged. No API calls, push, merge, publication, license change or destructive operation occurred.
