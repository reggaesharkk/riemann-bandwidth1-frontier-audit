# A1294 terminal 16 and source-connected node 53

## Decision

Terminal 16 is kernel accepted, and the complete source-connected node-53 subtree is kernel proved. The proof consumes the authentic 15-token subtree and eight quadratic payloads, reusing the already compiled node-55 replay object. This does not prove the initial/root predicate.

The successful claims are:

- `AuthenticCompact16.accepted_original` and `AuthenticCompact16.leaf_sound`;
- `Node53.replay53 : replayAffineTree leafCheck topology payloads 8 0 0 parentBox = some (15,8)`;
- `Node53.exact_exhaustion`, with lengths `(15,8)`;
- `Node53.source_node53_box : sourceBoxAt 53 = some (A1294Source.box37,16)`;
- `Node53.source_check_accepted`;
- `Node53.source_connected_predicate : BoxPredicate (affineEnergyGoal A B) parentBox`.

`Node53Replay.lean` compiled with Lean exit 0 in 2:22.72. Its maximum RSS was 5,287,912 KiB, with 174,378 major faults and no swap. Its `.olean` is 601,856 bytes. The terminal-16 acceptance module compiled with exit 0 in 4:00.65; peak RSS was 5,256,076 KiB, with 177,049 major faults and no swap. Its source is 310,586 bytes and its `.olean` is 12,473,880 bytes. All reported theorem dependencies are `[propext, Classical.choice, Quot.sound]`.

## Frozen source reconstruction

The supplied node-55 packet SHA-256 is `ba18a4a2993cf3941ffa1c13c11db812852b4a3ea3b485bd850f0b481264ab14` (111,239,721 bytes). The embedded frozen V2 package SHA-256 is `3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a` (5,672,384 bytes). Their archive CRCs and embedded manifests were checked by the independent verifier.

The bounded source parser and exact-rational verifier establish:

- raw topology bytes at nodes 53–67: `[4,0,1,0,5,0,3,0,2,0,4,0,1,0,0]`;
- node 53 is split token 4 (zero-based axis 3), node 54 is quadratic terminal 16, and node 55 is the right subtree;
- node-53 parent box is `box37`; node-54 box is its lower axis-3 half, and node-55 box is its upper axis-3 half (`box38`);
- terminal 16 is quadratic, its anchor ordinal is 16, and its anchor stream byte offset is 160;
- anchor codes are `(0,0,0,0,0)`, giving `(195/32,405/64,195/32,195/32,195/32)`;
- all 15 rows are segmented constant-envelope rows, with 357 segment occurrences and 166 distinct catalog references (22 stable and 144 refinement-v1 references; no v3 references);
- exact tangent lower value is `80505038307173677216495474300033874301 / 5000000000000000000000000000000000000000`;
- exact margin over `A=647/50000` is `15805038307173677216495474300033874301 / 5000000000000000000000000000000000000000`, which is positive.

The generated catalog uses the source-preserving 22+72+72 block representation. `Catalog16Identity.original_eq_catalog` and all 166 corresponding original-array lookups were kernel proved. `Catalog16AllLookups` also proves the needed local lookups. Segment decoding, all fifteen row checks, tangent check, acceptance, and leaf soundness are kernel checked.

## Node-53 replay

The Lean topology is the decoded form of those 15 source bytes:

`[split 3, terminal, split 0, terminal, split 4, terminal, split 2, terminal, split 1, terminal, split 3, terminal, split 0, terminal, terminal]`.

The payload stream contains terminal 16 followed by the seven payloads from `Node55`. The local left run consumes `(2,1)`. `ReplayTransport.transport` reuses `Node55.replay55` at offsets `(2,1)`, producing `(15,8)`. `split_chunk_replay` proves the node-53 replay, and the upstream exact-exhaustion theorem identifies that result with the stream lengths. Source path checkpoints through checkpoint 36 give `sourceBoxAt 53 = some (box37,16)`. The byte suffix, mapped topology, terminal-kind/anchor record, payload cursor, and source-connected predicate are separately recorded in the Lean module.

The proof checks the local source-connected 15-node subtree on the compiled source literals. It is not a formal parser for the original ZIP bytes.

## Trust boundary

**Kernel checked:** rational values and comparisons in the generated terminal-16 module; catalog block identity and lookup equalities; row/segment/tangent Boolean acceptance; leaf soundness; node-53 split geometry; 15-node replay; exact `(15,8)` cursor exhaustion; and the source-connected `BoxPredicate` over the compiled literal source streams.

**Externally checked:** ZIP and stream/catalog hashes; conversion of original byte streams into the Lean literal arrays; and execution of the deterministic catalog-selection algorithm that maps source records to the generated declarations and segment/row data. Hashes bind these artifacts but do not prove the conversion or selection algorithm in Lean. The user-provided source archive is not cryptographically signed here.

The packet carries a provenance claim/evidence record and content hashes. It does not claim that an IntentSeal or VRK verifier has kernel-checked the mathematical theorem, nor that a receipt proves mathematical truth.

## Chunk feasibility

This is a bounded, complete 15-node/eight-terminal chunk. Terminal 16's 357 source segment occurrences were generated automatically from the preserved witness and passed through the reusable compact checker; the other seven terminal payloads are reused through the existing node-55 proof object. The new replay module is 8,723 source bytes and 601,856 object bytes. The imported terminal-16 acceptance object is 12,473,880 bytes; the reused node-55 object is 597,864 bytes.

This demonstrates that one generated segmented leaf and a source-connected replay chunk can compose without rewriting the predecessor leaves. It does not demonstrate small total dependency cost: Lean/Mathlib import overhead dominated measured peak RSS (about 5.0 GiB in each run), and each successful leaf acceptance object remains about 12 MB. Full-certificate throughput, object growth, compilation feasibility, and peak memory remain OPEN. No full-certificate experiment was run.

The next authentic enclosing subtree is node 51: raw split token 2 (axis 1), left terminal node 52 / terminal ordinal 15, and right child node 53. Its source box is `box36`, and its local stream is `[2,0]` followed by the node-53 15-token stream, for 17 topology tokens and nine terminal payloads. Node 51 is identified from the frozen source prefix only; terminal 15 acceptance and the node-51 replay were not attempted.

## Overall scope

The full `initialGapBox 60` predicate and full A1294 theorem remain OPEN. This result does not change any frozen WP84 theorem status.
