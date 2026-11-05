# A1294 global interface and bounded source bridge — partial result

Research owner: Prince. Private additive audit, 2026-11-04. **The global-reduction interface is kernel proved. The source-connected subtree acceptance is NOT proved in this audit. Stop at the recorded source-normalization/environment blocker.**

## Decisions

| Gate | Decision |
|---|---|
| A1294_GLOBALIZATION_FROM_ROOT_KERNEL_PROVED | YES |
| A1294_ROOT_PREDICATE_STATUS | OPEN |
| SOURCE_NODE65_CORRESPONDENCE | OPEN; byte/cursor declarations emitted clean reports inside a FAILED module, but no clean source-bridge module was accepted |
| GENERIC_COMBINED_LEAF_SOUNDNESS | Existing upstream/compact components proved; new serialized payload adapter UNVERIFIED |
| BOUNDED_SOURCE_CONNECTED_TREE_ACCEPTED | NO |
| CHUNK_COMPOSITION_SOUNDNESS | OPEN; generic upstream replay soundness exists, new chunk/source assembly is draft only |
| FULL_V2_REPLAY_FEASIBILITY | OPEN, not demonstrated on current ARM64/WSL resources |
| EXTERNAL_TRUST_BOUNDARY | File hashing, byte-to-literal conversion, catalog field/source-selection correspondence remain external |
| FULL_A1294_THEOREM_STATUS | NOT_YET_PROVED |

This does not meet the requested complete success criterion of both globalization and one source-connected subtree. It preserves a genuine new conditional theorem and the exact first local obstacle, rather than presenting draft code as proof.

## Proved global theorem

GlobalInterface.lean successfully proves:

`A1294_global_of_root_predicate`

given `root : BoxPredicate (affineEnergyGoal (647/50000) (1094977/5000000000)) (initialGapBox 60)`, for every real five-vector g with all coordinates nonnegative,

647/50000 <= sextupleEnergy(g) + (1094977/5000000000)*sextupleSpan(g).

The exact rational tail margin is also proved: 60*(1094977/5000000000)-647/50000 = 49931/250000000 > 0. Both printed axiom reports contain only propext, Classical.choice and Quot.sound. There is no root axiom or asserted root predicate: the root proof is an explicit theorem argument. No original acceptance or parent theorem is used by this interface.

The inspected upstream A1290.Certificate.sextuple_affine uses affineTree_global_at with limit 59. This audit uses the same theorem at limit 60 with the A1294 constants. The pinned ParametricAdapter source was available, but its compiled object was absent; the initial pre-elaboration failure is preserved in global_missing_object.log. GenericGlobalization.lean therefore compiles the VERBATIM affineTree_global_at theorem/proof excerpt from the pinned ParametricAdapter, importing AffineTree instead of unrelated scalar-certificate machinery. The original source and excerpt hashes are recorded. This is a source-preserving reuse, not an invented axiom or a claim that the entire ParametricAdapter/A1290 project was newly built.

## Source bridge attempt and exact stopping point

generate_source.py authenticates the frozen V2 ZIP and copies its first 68 topology bytes, first 24 kinds and first 240 anchor bytes. It builds a rejecting bounded DFS interpreter of topology, terminal cursors and paths. The declarations node65, node66 and node67 reported [propext] during the failed build: before those nodes the interpreted paths/cursors match parent 65 at terminal cursor 22, left child 66 at 22 and right child 67 at 23. These clean local reports are evidence of where reduction worked, but the containing module FAILED, so no complete source bridge is counted as accepted.

The anchor convention matters globally: the manifest has 6725258 quadratic leaves but 6727061 total terminals. The anchor stream contains ten bytes per quadratic leaf only. All first 24 kinds are 1, so bounded indices 22 and 23 coincide with their quadratic indices. The new bounded reader computes the quadratic index from preceding kinds, and only quadratic payloads read anchors. This is not a global three-cursor decoder proof.

The previous monolithic 44-step rational unfolding was not repeated. SourceNode65_failed_v1.lean instead contains 43 explicit rational box checkpoints, each intended to normalize one midpoint update, followed by their composition. The FIRST failed declaration is checkpoint0:

`box0.lowerHalf (⟨2, by decide⟩ : Fin 5) = box1`

Here box0 is [0,60]^5 and box1 has coordinate 2 bounded by [0,30], all others [0,60]. At SourceNode65_failed_v1.lean:59:37, the tactic norm_num with the supplied finite-index simp rules reaches maximum recursion depth (6000). It is a normalization failure, not a mathematical counterexample or a false byte interpretation. The failed dependent source_path_box/node65_box reports contain sorryAx and are explicitly excluded from success.

The failed source/log are preserved unchanged. The prepared SourceNode65.lean removes the extra Fin.ext_iff simp rule. CheckpointSmoke.lean isolates only checkpoint0. Neither revised file was Lean tested: its WSL invocation never created checkpoint_smoke.log, and a separate read-only WSL responsiveness invocation also produced no output. After bounded waiting, only this audit's blocked WSL client helpers were identified by exact command lines and canceled; their records are in pending_helpers_cancelled.json. Both client sessions then exited 1. This is cancellation of unresponsive launch helpers, NOT a Lean rejection. WSL was not restarted, no service was stopped, and other research processes were not touched.

The exact next local obligation is to obtain a clean kernel equality for the isolated one-step checkpoint, then compose all checkpoints and accept a clean source module. The smoke test was deliberately not followed by the full 43-checkpoint build unless it passed. No new claim is made about the revised proof.

## Combined checker and chunks: prepared, not certified

CombinedTree.lean is an UNCOMPILED draft, not a successful theorem module. It proposes rejecting length-checked row/anchor decoders, compact fifteen-model soundness, upstream affineLeafCheck_sound and checkAffineTree_sound, an actual source-driven Boolean replay on the three local topology tokens and two payloads, exact exhaustion and malformed/truncated/extra-input controls. It uses the already verified child Boolean certificates as leaf facts, not the old parent theorem. None of its new wrapper/replay/chunk declarations may be cited as kernel proved until the source module and then this module compile cleanly. All compatibility/proof obligations in this draft remain open, including any ordinary elaboration errors not yet observed.

The upstream universal tail/combined/replay theorems and previous compact fifteen-model soundness are preserved proven ingredients. They do not automatically prove this new serialized adapter or the root. SCALING_DESIGN.md states the necessary cursor, stack, payload and exhaustion invariants and the unproved chunk/fuel interfaces. It is a design, not a completed proof. No next subtree is selected for execution because the required source-connected bounded test did not pass. Node 63 is only a previously known enclosing candidate; no proof or resource extrapolation justifies expanding it here.

## Actual resources

Pinned Lean 4.33.0-rc2, compiler d8b18978322de05a8f3dba51ef03cf5461676c17; upstream fba91d214655aaa1fd0504bb893c8859c20c79f9; Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. Serial processes used -M 6800 with explicit timeouts. Compilation times include elaboration/import/kernel work; no separate kernel-only timing is claimed.

| Build | Exit | Wall seconds | Peak RSS KiB | Major faults |
|---|---:|---:|---:|---:|
| First generic globalization | 124 timeout | 181.21 | 5448196 | 86417 |
| Verbatim generic globalization retry | 0 | 247.59 | 5469188 | 160828 |
| Conditional global interface | 0 | 108.65 | 5780468 | 54094 |
| Source bridge v1, FAILED | 1 | 133.54 | 5705140 | 50898 |
| Revised checkpoint smoke | client canceled | unavailable | unavailable | unavailable |

The two successful objects are GenericGlobalization.olean (68960 bytes) and GlobalInterface.olean (44720 bytes). The first timeout had no Lean rejection; its high system time motivated one bounded retry. No unsafe-memory conclusion is inferred from timeouts or service delay.

## First global obligation and freeze

The first missing GLOBAL mathematical proof remains precisely the complete `[0,60]^5` root predicate above. The successful external 13454121-node replay is not that Lean proof. This audit closes only the final logical reduction once that predicate is supplied. Source authenticity remains external to hashes and typed-literal soundness, and the coordinate/source replay bridge remains formally incomplete.

All original archives, successful standalone/compact proofs, negative SharkBridge experiments, licenses, five-hour replay evidence and historical WP84 conclusions are preserved. No full tree, additional leaf, large search, API call, push, merge, publication or destructive file operation occurred.
