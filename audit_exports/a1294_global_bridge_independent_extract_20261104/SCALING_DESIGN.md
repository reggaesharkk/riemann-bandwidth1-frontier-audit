# Full-certificate plan: not a completed proof

The frozen external manifest records 13454121 topology nodes, 6727061 terminals, 6725258 quadratic terminals, 1803 tails and maximum depth 80. Raw streams total 87433762 bytes: topology 13454121, kinds 6727061 and anchors 67252580. Anchors occupy ten bytes per QUADRATIC terminal, not per terminal. These counts and the five-hour exact replay are external evidence, not a kernel proof of the root.

## Required checked state

A full decoder needs separate topology t, terminal u and quadratic q cursors, with anchor byte cursor 10*q. Splits consume one topology code and push ordered children; terminal tags consume one kind; only quadratic tags consume five little-endian anchor codes. Every read must return some and validate the code/range. A tail must not consume anchors. A payload adapter must reject any row list whose length is not fifteen, any anchor whose length is not five, invalid catalog/segment references and incomplete segment coverage.

At a checkpoint, retain the exact pending traversal stack or a formally related source path and box, not merely a numeric node label or an external hash. A chunk claim must bind source stream identity, all start/end cursors, root box, chosen fuel, and replay result. Two independently valid boxes do not establish cursor continuity or prove that no branch is missing.

## Chunk contract and composition

Use upstream replayAffineTree and its soundness, rather than generating millions of unrelated theorem declarations. A chunk certificate should prove replayAffineTree leafCheck topology payloads fuel t u box = some (t',u'), together with the source-byte decoder relation for q and the exact anchor consumption. Preserve the original complete topology and selected data. The checker streams are immutable and identical across chunks.

A split-assembly lemma can combine a checked left replay beginning at t+1,u and a right replay beginning at the returned cursors, provided topology.get? t is exactly the split token. The parent result is obtained by the actual defining replay equation, while replayAffineTree_sound or checkAffineTree_sound transports the universal leaf soundness. Passing only BoxPredicate facts is not enough to certify serialized stream consumption.

The global final call must begin at all-zero cursors on initialGapBox 60, and finish at topology length 13454121, terminal length 6727061 and quadratic/anchor lengths 6725258/67252580. Root checkAffineTree acceptance already requires exact topology/payload exhaustion, but an adapter proof must additionally pay for every byte/kind/anchor consumption. Partial chunk success is not full exhaustion. Invalid topology codes, truncated streams, extra tokens and extra payloads must be rejected.

Fuel is depth fuel in the upstream implementation, not total node count. The manifest's depth bound suggests 81 units at the root, but that depth bound must itself be checked, not imported as an external assertion. One option is to assign chunks the remaining global depth fuel directly. Another needs a proved successful-replay fuel-monotonicity lemma before mixing chunk fuel values. Neither a new complete depth proof nor a full arbitrary-chunk assembly theorem is supplied by this design.

## Reusable leaf facts

Quadratic soundness should use accepted exact canonical/model data, interval coverage, catalog piece soundness and rankTangentCheck_energy_sound. Tail soundness is affineTailCheck_sound. affineLeafCheck_sound and checkAffineCertificate_sound combine these universally. Shared catalog checks and source scalar-envelope records can be reused as theorem facts, but lookup indices and every applicable interval/floor must still be proved valid. Untrusted proposed data are acceptable only when the kernel checks them; external PASS flags, native evaluation and owner-selection assumptions are not substitutes.

The original V2 streams do not serialize every expanded segment/floor record. A complete bridge must specify whether it formally implements the pinned source selection algorithm or accepts expanded witness data with independently checked mathematical soundness. The latter can establish a root inequality but does not by itself prove byte-identical source selection. All three catalog versions and source-admission semantics must remain pinned; a two-leaf success involving stable/v1 pieces does not authenticate all global v3 uses.

## Resource decision

The preceding experiments show roughly 5.5 GiB RSS dominated by common Mathlib/catalog imports; fresh standalone acceptance increased total object and compilation costs. Do not expand those failed architectures. Millions of hand-generated per-leaf modules are not a demonstrated feasible ARM64 plan. The raw input size alone is not the principal limitation: kernel reductions, proof-object duplication, import footprint and serialization/cursor proofs remain unresolved.

Select a next chunk only after a source-connected complete subtree passes, using actual unique model/segment counts, measured replay time, proof bytes and peak RSS with safety margin. The smallest enclosing subtree in the existing topology is node 63 (three quadratic leaves), but its node count alone does not justify compiling it. No expansion is authorized by this note. The maximum available WSL memory and observed import cost leave little evidence for full-certificate scaling; implementability of a full replay remains OPEN.

The exact first global mathematical obligation remains BoxPredicate (affineEnergyGoal (647/50000) (1094977/5000000000)) (initialGapBox 60). Once that proof is supplied, the compiled conditional globalization interface closes the final theorem. This document does not supply that root proof or turn an external replay into a Lean proof.
