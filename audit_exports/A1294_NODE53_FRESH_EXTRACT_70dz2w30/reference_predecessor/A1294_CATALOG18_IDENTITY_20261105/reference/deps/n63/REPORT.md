# A1294 node 63 bounded closure — 2026-11-05

Terminal 21, the five-node upstream replay and the source-connected node-63 predicate are Lean kernel proved. Every final build exited 0, with only propext, Classical.choice and Quot.sound in the printed axiom reports. The full A1294 theorem remains NOT_YET_PROVED. WP84 frozen conclusions are unchanged.

## Source and theorem

The predecessor ZIP has SHA-256 7205153baa297ab573ab65b212db41469144f494eaa2eea064b9650182b35a54. Its manifest, existing source/objects and exact reference archive hashes were checked. Existing installed CompositionalLeaf/Right sources and objects match the recorded hashes (environment.txt). Upstream is fba91d214655aaa1fd0504bb893c8859c20c79f9, Mathlib 51e6992efd06126df61a496bebf8f49482a4e129, Lean 4.33.0-rc2 commit d8b18978322de05a8f3dba51ef03cf5461676c17, Lake 5.0.0-src+d8b1897. Local research worktree HEAD remains eb36159ee7e57053fcae3de025fe4dac539435ab; tracked source changes were absent.

Original topology at nodes 63–67 is [4,0,1,0,0]. The root splits on axis 3; node 64 is quadratic terminal 21; node 65 is the prior axis-0 subtree with quadratic terminals 22 and 23 at nodes 66 and 67. Terminal and quadratic cursors before nodes 63–67 are respectively [21,21,22,22,23]. All three kinds are 1. End cursors are 24 and 24; anchors end at byte 240. Anchor indexing uses the count of quadratic kinds before the terminal, not a general assumption that every terminal consumes anchors.

Node 63's closed rational box is:

| coordinate | lower | upper |
|---|---:|---:|
| 0 | 405/64 | 105/16 |
| 1 | 825/128 | 105/16 |
| 2 | 795/128 | 405/64 |
| 3 | 405/64 | 105/16 |
| 4 | 405/64 | 105/16 |

The axis-3 midpoint is 825/128. The lower half is exactly terminal 21's source box; the upper half is the previously proved node-65 box. Source63 proves the 42-step source path using the imported checkpoints, sourceBoxAt 63 = some (parentBox,21), quadratic cursors, kinds, anchors and topology. Exact five-node geometry and paths are in source_geometry.json.

For terminal 21, all five original anchor codes are zero, so the anchor is the exact lower corner. The deterministic frozen source replay reconstructs 118 selected catalog declarations, 254 segment occurrences and fifteen rows, with direct piece macroPiece11 only on row 1. These model choices are reconstructed by the original source algorithm; catalog selections are not separately stored as fifteen indices in the binary topology. No new optimization or branch-and-bound search was performed. Selected original catalog items and endpoints are retained in authentic_input.json and independently rechecked. Lean checks rational canonicality, reference resolution, every segment, complete contiguous endpoint coverage, each piece's check, all fifteen row checks, ordered box, anchor membership, nonnegative quadratic weights and the exact tangent.

The exact tangent lower bound is 27278434335998064713136849756959829048453 / 2000000000000000000000000000000000000000000. Its margin above 647/50000 is 1398434335998064713136849756959829048453 / 2000000000000000000000000000000000000000000 > 0. The Python verifier also expands the quadratic objective and gradient independently from the recorded row coefficients and recovers the same rational tangent; Lean acceptance does not assume that Python result.

`AuthenticCompact21.accepted` and `leaf_sound` are new independent acceptance proofs, not calls to either old concrete acceptance theorem. The module imports CompositionalLeaf for the existing generic checker and catalog framework, so historical acceptance declarations remain in its transitive import closure, but they are not invoked to prove terminal 21. No claim of a minimal acceptance import closure or reduced compiler cost is made.

`ReplayTransport.transport` is a generic kernel-proved cursor-offset theorem. `Node63.reused_node65_run` applies it explicitly to imported `A1294Combined.replay65`, moving the old replay from local cursors (0,0) to (2,1), with result (5,3). The old payloads and their acceptance proofs are imported, not re-elaborated. `Node63.replay63` then joins terminal 21 and that imported run using the upstream split replay equation. `accepted_tree` proves the exact upstream checkAffineTree Boolean; `source_check_accepted` connects it to the source prefix, kinds, anchor reads and selected witnesses. `source_connected_predicate` follows from this accepted source replay and upstream soundness, rather than merely restating a midpoint parent theorem.

The proved mathematical statement is: for every g : Fin 5 → ℝ in the displayed closed box,

647/50000 ≤ sextupleEnergy(g) + (1094977/5000000000) * sextupleSpan(g).

The corresponding Lean theorem is `Node63.source_connected_predicate : BoxPredicate (affineEnergyGoal A B) Source63.parentBox`, with A and B the exact rationals above. `Node63.exact_exhaustion` proves replay equals some (topology.length,payloads.length), concretely (5,3). Source and raw statement/axiom outputs are preserved.

## Controls, failures and resources

Node63Controls proves upstream rejection of an extra topology token, topology missing the last terminal, and a missing right payload. It also proves invalid token decoding and invalid kind scanning. A deliberately reordered topology is proved unequal to the frozen source prefix. This last test is source-order disagreement, not a theorem that the semantic checker rejects every permutation of otherwise valid witnesses. No universal malformed-input rejection is claimed.

The first replay draft failed at elaboration of the imported transport application with maximum recursion depth and downstream sorryAx reports. It is retained as Node63Replay_failed_v1.lean and replay63_failed_v1.log and is NOT a successful proof. Supplying explicit fuel, cursors, output cursors and box resolved the problem; no recursion-limit increase or acceptance assumption was used. There was no substantive mathematical rejection, timeout or unsafe-memory termination in this audit. The final successful module and axiom reports supersede only this new draft's proof status; all historical artifacts remain unchanged.

All builds were sequential. /usr/bin/time directly wrapped the bounded Lean compiler, so logs include compiler-descendant wall time, maximum resident set and major/minor faults rather than merely Lake startup costs. See resources.json for exact numbers. Terminal 21: 103.26 s, peak 5,562,884 KiB; source path: 26.34 s, 5,800,436 KiB; transport: 30.76 s, 5,822,564 KiB; helpers: 48.60 s, 5,415,540 KiB; five-node replay/source composition: 76.63 s, 5,484,328 KiB; controls: 31.58 s, 5,461,132 KiB. These cold/warm mixed runs with substantial page faults establish no scaling law or compression improvement.

The inherited extractor initially copied a hard-coded metadata count `weighted_split_checks_through_parent: 66`. The corrected recheck records the actual 44 nonterminal weighted splits in the bounded 68-token prefix. Both outputs are retained; their terminal-21 mathematical payloads are identical. The adapted legacy JSON labels `children.left/right` are sampled terminals 21/23, not a claim that terminal 23 is node 63's immediate right child. source_geometry.json is the unambiguous five-node hierarchy; the immediate right child is node 65. Neither metadata issue is used as a Lean premise.

## Remaining trust boundary and root obligation

Lean proves arithmetic and cursor semantics for the supplied literal source prefix, validity of the chosen interval/model data and exact replay soundness. Conversion from original ZIP bytes to those literals, pinned catalog JSON-to-declaration identity, and correspondence of deterministic source model selection remain external provenance obligations. Hashes bind bytes but do not formalize a binary parser or prove a catalog identity theorem. The offline verifier authenticates the original streams, catalog records, exact geometry and tangent without executing a full-tree replay.

The precise missing global premise is `BoxPredicate (affineEnergyGoal (647/50000) (1094977/5000000000)) (initialGapBox 60)`. Only this bounded subtree has been added to the successful proofs; the remaining root coverage, complete stream serialization/assembly and all other terminal obligations are not discharged. The preserved global-reduction theorem remains conditional. No WP84, zero-density or RH conclusion changes. No full certificate run, WSL restart, Mathlib rebuild, push, merge or publication occurred.
