# Offline integrity and bounded Lean reproduction

Run `python verify_packet.py`, `python -O verify_packet.py`, and `python -OO verify_packet.py` after independent extraction. These check the manifest, original archive/streams/catalog records, preserved prior objects, exact source geometry and an independent rational tangent expansion. They check recorded Lean results, not a replacement proof system.

Use the existing pinned project and Mathlib cache. Do not rebuild Mathlib or install another compiler. The compiler and libraries are not vendored here. The object files are WSL aarch64 builds; another architecture must rebuild from source. The retained reference/node65.zip contains the complete previous proof packet, lockfiles, source and objects, with nested original source dependencies. Extract it to a separate PREV directory and set NEW to this packet's extracted directory. Existing installed CompositionalLeaf/Right and generic dependencies must match environment.txt. See the predecessor reproduction notes if restoring those private modules in an isolated project.

Set `LEAN_PATH="$NEW:$PREV${LEAN_PATH:+:$LEAN_PATH}"` in the pinned zeta23 project. Compile sequentially, writing fresh logs and objects only in a disposable extraction:

1. Terminal21.lean (240-second bound)
2. Source63.lean
3. ReplayTransport.lean
4. Node63Helpers.lean
5. Node63Replay.lean
6. Node63Controls.lean

For NAME use `lake env /usr/bin/time -v timeout 90 lean -M6800 --root "$NEW" "$NEW/NAME.lean" -o "$NEW/NAME.olean"`, substituting 240 for Terminal21. A cold machine may time out; this is not a false check. Stop on nonzero exit, sorryAx or unsafe memory. No build of a larger subtree or the full V2 certificate is needed or authorized by these instructions.

The initial generated AuthenticCompact21.lean is a literal-generation intermediate and was not used as a monolithic acceptance build. Terminal21.lean is the compositional acceptance proof. The retained *_failed* source/log is an unsuccessful draft. No failed draft's axiom output counts as a verified result. The final modules and objects have hashes in source_hashes.json and SHA256SUMS.txt.

extract21.py is a bounded source reconstruction aid using the frozen original replay module. It verifies archive/package/stream/catalog hashes and inspects only topology through node 67. It does not launch the full replay or a search. Its arguments are an extracted original V2 root and the unchanged V2 ZIP; compare its mathematical leaf output with authentic_input_recheck.json. Original-byte parsing and pinned catalog correspondence remain external, as detailed in REPORT.md.
