# A1294 node 61 bounded closure — 2026-11-05

The authoritative machine decisions are in DECISIONS.json; successful build exits, wall time, descendant peak RSS and faults are in resources.json and unabridged logs. The complete initialGapBox 60 predicate and full A1294 theorem remain OPEN. This audit does not change any WP84 conclusion.

## Authenticated inputs

The reference archive is A1294_NODE63_SOURCE_CONNECTED_FIVE_NODE_REPLAY_20261105.zip, SHA-256 9f7ffe3ad15c1cef23a56384896e6afd4641442e197df7629bd53602d52f5cd3. Its manifest and every listed source/object hash were verified. Pinned upstream fba91d214655aaa1fd0504bb893c8859c20c79f9, Mathlib 51e6992efd06126df61a496bebf8f49482a4e129, Lean 4.33.0-rc2 commit d8b18978322de05a8f3dba51ef03cf5461676c17 and Lake 5.0.0-src+d8b1897 were checked in the existing WSL project. environment.txt also records source and installed prior acceptance-object hashes. No dependency installation or Mathlib rebuild was performed.

The unchanged source-free V2 ZIP has SHA-256 3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5. Stream/catalog hashes and the archive's package manifest were checked by the bounded extraction. Original nodes 61–67 have topology [2,0,4,0,1,0,0]. Terminal cursors before those nodes are [20,20,21,21,22,22,23]; quadratic cursors are identical here because these prefix kinds are all quadratic. Anchor reads nevertheless use the count of quadratic kinds, not an assumption that every terminal consumes an anchor. The four kinds at terminals 20–23 are 1. Local exhaustion is (7,4); original terminal/quadratic end cursors are (24,24), anchor byte end 240.

Node 61's source box is:

| coordinate | lower | upper |
|---|---:|---:|
| 0 | 405/64 | 105/16 |
| 1 | 405/64 | 105/16 |
| 2 | 795/128 | 405/64 |
| 3 | 405/64 | 105/16 |
| 4 | 405/64 | 105/16 |

Its axis-1 midpoint is 825/128. The lower half is terminal 20 / node 62. The upper half is precisely Source63.parentBox. Source61 proves the original 41-step path, locate61/62 cursors, sourceBoxAt 61 = some (parentBox,20), topology, kinds and anchor decoding by importing the already proved rational checkpoints. source_geometry.json independently reconstructs every selected node from the original bytes using rational midpoint arithmetic.

## Authentic terminal 20

The anchor was recovered before choosing its representation. Terminal 20's original little-endian codes at byte offset 200 are [0,0,0,0,0], hence its actual anchor is the lower corner. No nonzero anchor was replaced. The frozen original deterministic model-selection code reconstructs 132 selected declarations and 304 segment occurrences across all fifteen rows. All these rows use segmented constant envelopes; no direct model or optimized replacement was introduced. The original certificate serializes anchor codes, not a separate list of selected model indices. The recovered indices and complete catalog records are retained as external source-reconstruction evidence.

AuthenticCompact20.accepted is proved by the existing generic compact checker soundness framework, with independent canonical rational checks, explicit successful catalog resolution, all segment-validity checks, complete interval/seam coverage, piece checks, all fifteen row checks and the exact rank tangent. It does not invoke an old concrete leaf acceptance theorem. As in the predecessor, the generic definitions and catalog facts are imported through CompositionalLeaf, so historical acceptance declarations remain in the transitive import closure without being acceptance premises for terminal 20.

The tangent lower bound is 43365651662553313027646381349923422449 / 3200000000000000000000000000000000000000. Its exact positive margin over A = 647/50000 is 1957651662553313027646381349923422449 / 3200000000000000000000000000000000000000. The verifier separately expands the recorded quadratic objective/gradient in exact Python fractions and checks this same tangent and margin. Lean acceptance does not assume that Python calculation.

The first whole-row decoding draft and the subsequent per-segment reflexivity draft failed with maximum recursion depth while unfolding the 132-entry catalog. They are preserved with complete logs and sorryAx-dependent failed reports, which are not counted as success. The final proof introduces 132 separately simp-proved catalog lookup facts and 304 per-segment decoding equalities; row decoders compose those facts. No recursion-limit increase or witness change was used. finish_decoders.py reconstructs this exact conversion from the retained first draft and checks byte equality with the final source. The final accepted theorem and axiom reports are the only terminal-20 proof result. No false mathematical row check or counterexample was established by either elaboration failure.

## Source-connected seven-node replay

Node61.topology/payloads contain the seven source tokens and four authentic quadratic payloads in source order. Node61.reused_node63_run applies the imported generic ReplayTransport.transport theorem to the existing Node63.replay63 object, explicitly setting fuel 3, original cursors (0,0), offsets (2,1) and output (7,4). The generic transport theorem required no new soundness extension. No old large leaf payload module was re-elaborated. Node61.right_predicate separately reuses Node63.source_connected_predicate through exact upper-half equality.

Node61.replay61 joins terminal 20's accepted run with the transported node-63 run under the upstream axis-1 split equation, with fuel 4. Node61.accepted_tree proves checkAffineTree = true and exact_exhaustion proves both local streams are exhausted. Node61.source_check_accepted binds that Boolean replay to the prefix source box, token decoder, kind reads and quadratic-only anchor indexing. Node61.source_connected_predicate follows from this accepted source replay and upstream tree soundness, not merely a restatement of a previously proved parent predicate.

Its mathematical content is: for every g : Fin 5 → ℝ in the displayed closed node-61 box,

647/50000 ≤ sextupleEnergy(g) + (1094977/5000000000) * sextupleSpan(g).

FinalStatements.lean prints the exact theorem signatures and axiom dependencies. No invented acceptance premise, custom axiom, native_decide, admit or sorry is used in successful modules. resources.json explicitly separates the two failed terminal drafts from successful builds. All builds are sequential and bounded, with /usr/bin/time directly wrapping Lean; recorded RSS/faults include compiler descendants. No full-tree throughput inference is justified by these cold/warm mixed measurements.

## Controls and external boundaries

Node61Controls tests upstream Boolean rejection for an extra topology token, truncated topology and a missing final payload, using generic symbolic leaf checks then authentic instantiation. It also checks invalid token decoding and invalid kind scanning. Misordered source topology is proved unequal to the authenticated source prefix; this is not a universal rejection theorem for permutations of otherwise valid mathematical witnesses. Tested controls are not universal malformed-input validation. Elaboration failures, timeouts, Boolean false and provenance gaps are distinct statuses in the evidence.

Original-byte-to-Lean-literal conversion, pinned JSON-to-catalog-declaration identity and deterministic source model-selection correspondence remain external authentication boundaries. Hashes and the Python verifier bind/check recorded bytes but are not formal binary-parser or catalog-identity theorems. Lean proves literal-level source arithmetic, chosen model validity and replay soundness. This distinction is unchanged by another successful enclosing subtree.

The smallest outstanding global premise is still `BoxPredicate (affineEnergyGoal (647/50000) (1094977/5000000000)) (initialGapBox 60)`. Remaining root coverage, complete stream assembly and all other terminals have not been discharged. The preserved global reduction is conditional on that missing premise. All historical archives/proofs are unchanged; no push, merge, publication, WSL restart or full certificate replay occurred.

## Next enclosure and architecture

Topology-only inspection identifies node 59 through 67 as the immediate next enclosure: [3,0,2,0,4,0,1,0,0], axis-2 split, left child node 60 / quadratic terminal 19, right child node 61. It has nine nodes and five payloads. No terminal-19 acceptance or next-subtree build was attempted. See next_enclosure.json and BULK_VERIFICATION.md.

The existing generic checker, cursor transport and exact assembly provide a credible design route for automated chunked verification without manually authoring millions of proofs. A practical full-certificate acceptance engine and resource strategy are not yet demonstrated. The present generator's many arithmetic facts, substantial common import footprint, and decoder-depth failures preclude claiming full-scale feasibility from this result. Complete root coverage and full A1294 remain OPEN.
