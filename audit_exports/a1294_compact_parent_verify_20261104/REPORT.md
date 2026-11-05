# Authentic compact two-leaf parent

Research owner: Prince. Private additive result, 2026-11-04.

## Decisions

- RIGHT_COMPACT_LEAF_ACCEPTED: YES, kernel proved.
- COMPACT_PARENT_COVERAGE_PROVED: YES, kernel proved.
- COMPACT_TWO_LEAF_PARENT_KERNEL_PROVED: YES.
- SOURCE_CORRESPONDENCE_STATUS: external authenticated V2 replay and literal comparison; full binary decoding and catalog correspondence are not kernel authenticated.
- LIKE_FOR_LIKE_RESOURCE_COMPARISON: not established; no compression or memory advantage claimed.
- FULL_A1294_THEOREM_STATUS: NOT_YET_PROVED.

## Result and proof dependencies

The bounded frozen-source replay through node 67 reproduced SHA-256 9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072 in normal Python, -O and -OO. It checks the frozen ZIP hash, CRC, package manifest, input catalogs and topology/kind/anchor stream hashes. No full-tree replay or search was run.

Terminal 23/node 67 uses its original lower-corner anchor, 192 segments, 92 selected declarations, all fifteen original model rows, exact source floors and endpoints. Its exact tangent lower value is 26036215021254826261948480423241409791537/2000000000000000000000000000000000000000000; its margin above A is 156215021254826261948480423241409791537/2000000000000000000000000000000000000000000. CompositionalRight.lean proves canonicality, decoding, each segment validity, interval coverage, all fifteen row checks, tangent acceptance, AuthenticCompactRight.accepted and AuthenticCompactRight.leaf_sound. It reuses the generic compact soundness framework imported through the unchanged successful left module.

A1294CompactParent.lean proves both exact child-box identities for the axis-0 midpoint split of parent node 65. It applies boxPredicate_of_midpoint_children to AuthenticCompactLeaf.leaf_sound and AuthenticCompactRight.leaf_sound. The printed elaborated proof in parent_build.log explicitly contains both references. It does not import or invoke the historical parent theorem.

The final theorem is: for every g : Fin 5 -> real satisfying the coordinate box below,

647/50000 <= sextupleEnergy(g) + (1094977/5000000000) * sextupleSpan(g).

| Coordinate | Lower | Upper |
|---|---:|---:|
| 0 | 405/64 | 105/16 |
| 1 | 825/128 | 105/16 |
| 2 | 795/128 | 405/64 |
| 3 | 825/128 | 105/16 |
| 4 | 405/64 | 105/16 |

The split midpoint in coordinate 0 is 825/128. Both closed children cover the midpoint; no gap is omitted. verify_inputs.py checks exact equality of the historical parent declaration and theorem statement, exact rational midpoint boxes and every right segment proof statement against the frozen ledger. The old source is bundled under historical/ for comparison only.

The right-leaf and parent builds both exited 0. Printed axioms for the right acceptance/soundness, midpoint identities, both leaf acceptances and parent conclusion are only propext, Classical.choice and Quot.sound. No sorryAx, sorry, admit, custom axiom, native_decide or external PASS premise is used. Warnings in the logs are unused simplifier/tactic warnings, not failed goals.

## Resources and hashes

| Module | Source bytes | Object bytes | Wall seconds | Peak RSS KiB | Major faults |
|---|---:|---:|---:|---:|---:|
| Preserved left compact leaf | 148181 | 11078224 | 136.49 | 5490764 | 164918 |
| New right compact leaf | 122176 | 9270368 | 112.61 | 5492820 | 171234 |
| New compact parent assembly | 2871 | 446368 | 49.02 | 5870988 | 94618 |

The left measurement is its preserved earlier successful run. The new parent imports precompiled leaves; 49.02 seconds is assembly cost, not a complete clean build. The historical monolithic proof and this modular chain were not rebuilt under controlled identical cache conditions. Do not compare assembly alone with the historical complete parent. The table is not a like-for-like compression benchmark. Full closure source totals 273228 bytes and closure objects total 20794960 bytes, excluding upstream dependencies; these are file sums, not independent memory costs.

Right source SHA-256: 4baa4a617f3d2cec4602a476a30c8d2e59dbaa831b3a49227507eb15b34f7905.
Right object SHA-256: 2d17b9c061e22c4d9a14a59ead52c4f0f33068692a2e2a08e37657570fed62dd.
Parent source SHA-256: 31de815525cb22f1cd656bae923a34ffc57f99832add6e352293372324d3fe5b.
Parent object SHA-256: 0acec8e1b47ad691d30275ce0d3935e4356239c7c0dc48134adf9be7c988bcb5.
The manifest records all bundled file hashes, including the unchanged left source/object/log and old parent source.

Pinned Lean 4.33.0-rc2 (aarch64 compiler d8b18978322de05a8f3dba51ef03cf5461676c17), Lake 5.0.0-src+d8b1897, upstream fba91d214655aaa1fd0504bb893c8859c20c79f9, Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. The earlier environment evidence is included in left_preserved/environment.txt. Matching upstream lockfiles and source excerpts are bundled; the entire toolchain and Mathlib cache are not vendored.

## Trust boundary and next bounded milestone

Lean proves the literal boxes, compact checks, model soundness and parent predicate. Cryptographic provenance, conversion from V2 binary topology/anchor streams to literals, and index-to-upstream-catalog equality remain independently checked external obligations. This task does not turn that external bridge into a Lean binary decoder. The original left packet, all 208 left segments and frozen certificate remain unchanged.

A bounded topology inspection identifies the smallest strictly enclosing complete subtree: node 63 through 67, five nodes, with children node 64 and node 65 and quadratic terminals 21, 22 and 23. It needs one additional compact quadratic proof plus one split assembly. No mathematics for terminal 21 was compiled here. Based only on these observed runs, allow roughly 2–5 additional minutes for one comparable leaf plus assembly and at least 6 GiB available RSS capacity, with a safety margin; complexity and paging may exceed this estimate. This is a planning estimate, not a scaling theorem or permission to start that build. Larger-tree feasibility remains unestablished.

All existing research and historical packets were preserved. No full-tree replay, WSL restart, push, merge or publication occurred. WP84's frozen conclusions remain unchanged.
