# A1294 node 51 / terminal 15 proof report

## Decision

Terminal 15's authentic quadratic acceptance and leaf soundness are kernel proved. The node-51 source-connected replay is also kernel proved over the compiled source literals. The exact 17-token subtree consumes 9 payloads and terminates at cursor pair `(17,9)`. Node 53's eight-terminal replay is imported from the V4 predecessor object and transported by the generic cursor-offset theorem.

The full `initialGapBox 60` predicate and the global A1294 theorem remain **OPEN**. No claim is made about the full certificate or WP84.

## Frozen evidence and environment

- Input proof packet: `A1294_NODE53_TERMINAL16_PROOF_PACKET_V4_20261105.zip`, 325,810,186 bytes, SHA-256 `a0b58ec6b7241f88b0bb3b223c7944fbdc0d7922fcd8f049f040d61b642d3b13`.
- Embedded source package: `A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip`, 5,672,384 bytes, SHA-256 `3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5`.
- Local audit worktree HEAD at start: `eb36159ee7e57053fcae3de025fe4dac539435ab`.
- Formal Math commit: `fba91d214655aaa1fd0504bb893c8859c20c79f9`.
- Mathlib commit: `51e6992efd06126df61a496bebf8f49482a4e129`.
- Lean 4.33.0-rc2 commit `d8b18978322de05a8f3dba51ef03cf5461676c17`; Lake `5.0.0-src+d8b1897`; pinned `lake-manifest.json` SHA-256 `1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448`.

The environment identity was checked read-only before compilation. All Lean builds were sequential, used `-M6400`, did not rebuild Mathlib, and exited 0. Exact commands, stdout, resource data, theorem statements, and `#print axioms` results are in the per-module build logs.

## Terminal 15 source reconstruction

The bounded source parser and independent exact-rational verifier reproduce topology nodes 51–67 as:

```text
[2,0,4,0,1,0,5,0,3,0,2,0,4,0,1,0,0]
```

Node 51 is token 2 / axis 1. Node 52 is its left child, terminal ordinal 15, quadratic kind; node 53 is the right child. Parent box is `A1294Source.box36`:

```text
g0 [195/32,105/16]   g1 [195/32,105/16]   g2 [195/32,405/64]
g3 [195/32,105/16]   g4 [195/32,105/16]
```

Terminal 15's lower-half box is:

```text
g0 [195/32,105/16]   g1 [195/32,405/64]   g2 [195/32,405/64]
g3 [195/32,105/16]   g4 [195/32,105/16]
```

Its anchor stream offset is 150 bytes. The serialized codes are `(0,0,0,0,0)` (denominator 16384), giving the exact lower-corner anchor `(195/32,195/32,195/32,195/32,195/32)`. The source selector yields 15 segmented-constant rows, 369 segment occurrences, and 167 distinct catalog references: 23 stable entries and 144 refinement-v1 entries. Exact source-selection records and all interval endpoints are retained in `terminal15_authentic_input.json`.

The exact rational tangent lower value is

```text
80248403072798677216495474300033874301 / 5000000000000000000000000000000000000000
```

Subtracting `A=647/50000` gives the strictly positive exact margin

```text
15548403072798677216495474300033874301 / 5000000000000000000000000000000000000000.
```

The Python reconstruction verifier independently replays the bounded weighted-split prefix, source hashes, anchor decoding, catalog selection, interval coverage, all row data, and tangent arithmetic. Normal, `-O`, and `-OO` runs passed. The Python check is evidence about the input conversion; it is not the proof of the inequality.

## Kernel-checked claims

`Catalog15Identity.original_eq_catalog` proves the generated block representation equals the original 167-entry source-order array. `Catalog15AllLookups` proves all 167 required lookups and original-array lookups. `AuthenticCompact15.accepted_original` proves the exact compact checker returns `true` on the original array. `AuthenticCompact15.leaf_sound` derives the upstream quadratic box inequality.

`Node51Replay.left_box` proves the exact lower-half geometry; `Node51Replay.right_box` reuses the source checkpoint to node 53. `Node51Replay.replay51` proves the replay; `exact_exhaustion` proves its result equals both stream lengths, `(17,9)`. `source_node51_box` checks the source path against the compiled source literal, and `source_connected_predicate` proves `BoxPredicate (affineEnergyGoal A B) A1294Source.box36` from the accepted source-shaped replay.

All reported theorem dependencies are the standard Lean/Mathlib axioms `[propext, Classical.choice, Quot.sound]`. There are no custom axioms, `sorry`, `admit`, `sorryAx`, `native_decide`, or external PASS assumptions in the successful modules. A warning about an unused simp argument is recorded in the terminal-15 Lean log; it did not fail elaboration.

## Trust boundaries and remaining root premise

The kernel checks exact Lean literals, catalog identity/lookups, compact leaf checks, midpoint geometry, replay, exhaustion, and the resulting node-51 box predicate. The source-byte-to-Lean-literal conversion and the deterministic algorithm selecting catalog rows/segments are checked by independent Python over the hashed V2 files, not proved in Lean. The V2 source archive's origin is not authenticated by its local hash alone. VRK binds evidence identities; the existing IntentSeal manifest verifier checks file-manifest integrity. Neither mechanism proves a mathematical claim or authenticates the archive publisher.

The next ancestor would need the independently accepted sibling subtree and exact source split above node 49. This packet does not prove that sibling, the node-49 predicate, the complete root predicate, or any global theorem.
