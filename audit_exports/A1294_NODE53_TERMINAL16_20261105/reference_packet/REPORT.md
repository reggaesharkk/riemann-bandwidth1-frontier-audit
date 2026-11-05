# A1294 node 55 / terminal 17 source-connected proof audit

## Result

Terminal 17 is accepted by the Lean kernel using the original reconstructed witness, and the node-55 source-connected 13-node replay is kernel proved. The replay consumes exactly 13 topology tokens and 7 terminal payloads. The proof imports and reuses the predecessor's `Node57.replay57`; it does not rebuild terminal 18 or the node-57 subtree.

The proved propositions include:

- `AuthenticCompact17.accepted` and `AuthenticCompact17.leaf_sound`;
- `Node55.replay55 : replayAffineTree leafCheck topology payloads 7 0 0 parentBox = some (13, 7)`;
- `Node55.exact_exhaustion`;
- `Node55.source_check_accepted`;
- `Node55.source_connected_predicate : BoxPredicate (affineEnergyGoal A B) parentBox`.

The final `Node55Replay.lean` build exited 0. Printed dependencies for `left_check`, `replay55`, `exact_exhaustion`, `source_node55_box`, and `source_connected_predicate` are `[propext, Classical.choice, Quot.sound]`. No `sorry`, `sorryAx`, `admit`, `native_decide`, custom axiom, or external PASS value occurs in the successful modules.

## Frozen source and environment

The supplied predecessor archive was verified byte-for-byte: SHA-256 `1b2648fc7734f63a096623350e1290bae67fa6ad8b20241147d869e672674fcb` (93,781,352 bytes). Its embedded V2 source archive is SHA-256 `3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a` (5,672,384 bytes), with CRC and the internal package manifest checked by the Python reconstruction verifier.

The live pinned project was read-only checked: formal-math commit `fba91d214655aaa1fd0504bb893c8859c20c79f9`, Lean `4.33.0-rc2` commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, Lake `5.0.0-src+d8b1897`, Mathlib commit `51e6992efd06126df61a496bebf8f49482a4e129`, and `lake-manifest.json` SHA-256 `1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448`.

## Source reconstruction and exact arithmetic

The independent verifier checks the original topology bytes on nodes 55–67 as `[1,0,5,0,3,0,2,0,4,0,1,0,0]`: node 55 is a split on axis 0, node 56 is quadratic terminal 17, and node 57 is the right child. Terminal 17's anchor cursor is 17, its anchor byte offset is 170, and its five serialized codes are `(0,0,0,0,0)`.

The exact node-55 parent box is:

| coordinate | lower | upper |
|---|---:|---:|
| g0 | 195/32 | 105/16 |
| g1 | 405/64 | 105/16 |
| g2 | 195/32 | 405/64 |
| g3 | 405/64 | 105/16 |
| g4 | 195/32 | 105/16 |

The left child, terminal 17, has g0 upper endpoint `405/64` and the same other coordinate intervals. The exact lower-corner anchor is `(195/32, 405/64, 195/32, 405/64, 195/32)`. Lean proves the left/right midpoint-box identities against the parent and imported `Source57.parentBox`.

All fifteen rows are segmented constant-envelope rows, with 375 segment occurrences in total and 175 distinct catalog references (21 stable/macro and 154 refinement-v1; no v3 references). The generated catalog is split into blocks of 21, 77, and 77 references. `Catalog17Identity.original_eq_catalog` proves the selected original-reference list is equal to that block array; `Catalog17AllLookups` proves every one of the 175 local lookups and corresponding original lookups. Terminal17's exact rank-tangent lower bound is

`803196336133705194592676257298467787 / 50000000000000000000000000000000000000`.

Its exact margin above `A = 647/50000` is

`156196336133705194592676257298467787 / 50000000000000000000000000000000000000 > 0`.

The independent Python verifier replayed the deterministic catalog selection, checked every row's distance interval, all segment boundaries and source references, and recomputed the tangent with exact fractions. This is external source-conversion evidence; it is not a Lean proof that the Python selector's output equals the original byte-stream selection.

## Node-55 replay logic

The source suffix decodes to `[split 0, terminal, split 4, terminal, split 2, terminal, split 1, terminal, split 3, terminal, split 0, terminal, terminal]`. The seven quadratic payloads are the accepted terminal-17 payload followed by the six payloads already used by `Node57.replay57`. The split-chunk theorem combines the one-terminal left run `(2,1)` with the transported right run `(13,7)`; `checkAffineTree_exact_exhaustion` then equates those cursors to the stream lengths. Source path checkpoints prove `sourceBoxAt 55 = some (box38,17)`, and the source literal topology/payload adapters reduce to the checked replay. Upstream replay soundness yields the node-55 `BoxPredicate`.

## Trust boundary and theorem scope

Lean verifies the exact rational literals, catalog array identities/lookups, compact leaf acceptance, replay computation, cursor exhaustion, and source-connected predicate for the compiled source literals. The V2 archive and stream/catalog hashes bind the external inputs. However, the Lean kernel does not parse the original V2 archive bytes or formally prove the deterministic source catalog-selection algorithm corresponds to the generated Lean literals. These two byte/selection bridges remain external. The full `initialGapBox 60` predicate and full A1294 theorem remain OPEN. This packet changes no frozen WP84 result.

## Failed attempts retained

Earlier terminal-17 direct `decide` drafts failed at recursion depth or became stuck in rational decidability; these are preserved as evaluation/elaboration limitations, not mathematical rejection. The first node-55 draft also failed elaboration because the two right-subtree payloads were referenced under the wrong namespace, transport arguments were ordered incorrectly, and the source adapter rewrite was too broad. Its compiler log and reconstructed pre-fix draft are retained. The corrected source compiles cleanly.

