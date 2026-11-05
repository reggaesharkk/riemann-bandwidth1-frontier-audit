# Bounded reproduction

Run `python verify_packet.py`, `python -O verify_packet.py`, and `python -OO verify_packet.py` in an extracted copy. These verify provenance, manifest, exact bounded Python arithmetic and recorded outcomes; they do not substitute for Lean.

Use only the existing matching project: upstream fba91d214655aaa1fd0504bb893c8859c20c79f9, Mathlib 51e6992efd06126df61a496bebf8f49482a4e129, Lean 4.33.0-rc2 commit d8b18978322de05a8f3dba51ef03cf5461676c17. environment.txt and the two lockfiles bind the actual environment. The imported historical CompositionalLeaf/Right and generic dependencies are retained in reference/compact_parent.zip. The global bridge reference retains the frozen V2 and upstream AffineTree source. This packet is not a vendored Mathlib/toolchain distribution. Supplied objects were built on WSL aarch64; rebuild from source on another platform.

In the existing pinned zeta23 project, set D to a disposable extracted packet's absolute Linux path. Set `LEAN_PATH="$D${LEAN_PATH:+:$LEAN_PATH}"`. Compile, strictly sequentially:

1. CheckpointTargeted.lean
2. SourceNode65.lean
3. CombinedHelpers.lean
4. ReplayOnly.lean
5. CombinedTree.lean
6. NegativeControls.lean

For each module NAME, use `lake env /usr/bin/time -v timeout 90 lean -M6800 --root "$D" "$D/NAME.lean" -o "$D/NAME.olean"` with output redirected to a new log. On slower/cold systems a timeout is not a mathematical rejection. Stop on error, unsafe memory, nonzero exit or sorryAx. Do not compile *_failed*, *_timeout*, CombinedFixed, CombinedExplicit, CombinedGeneric, CombinedInstrumented or GenericReplay as if they were the final proof. They are retained diagnostics. Do not replace historical files or re-run the full V2 replay.

Successful theorem and axiom outputs are in checkpoint_targeted.log, source.log, helpers.log, replay_only.log, combined.log and negative.log. SourceNode65's final theorem depends on every path checkpoint. CombinedTree's final mathematical predicate explicitly depends on source_check_accepted and both compact leaves through replay/tree soundness. Root-globalization remains conditional on an unproved complete root predicate.
