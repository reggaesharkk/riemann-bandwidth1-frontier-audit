# Private bounded reproduction

Run verify_packet.py in normal Python, -O and -OO after independent extraction. Also run `python -X utf8 finish_decoders.py`. These check manifests, frozen source bytes/catalog records, exact geometry/tangent and recorded clean builds; Python is not a substitute for kernel replay.

Use the existing pinned WSL project and Mathlib cache named in environment.txt. Compiler/Mathlib binaries are not vendored here. Objects are WSL aarch64; other platforms must rebuild from source. Extract reference/node63.zip into PREV63 and its reference/node65.zip into PREV65. Set NEW to a disposable extraction of this packet and set `LEAN_PATH="$NEW:$PREV63:$PREV65${LEAN_PATH:+:$LEAN_PATH}"` in the pinned zeta23 project. Installed generic/CompositionalLeaf/Right sources and objects must match the preserved environment hashes; nested predecessor packets retain their sources and reproduction instructions.

Compile sequentially:

1. Terminal20.lean (240-second bound)
2. Source61.lean (90-second bound)
3. Node61Helpers.lean
4. Node61Replay.lean
5. Node61Controls.lean
6. FinalStatements.lean

For each NAME use `lake env /usr/bin/time -v timeout 90 lean -M6800 --root "$NEW" "$NEW/NAME.lean" -o "$NEW/NAME.olean"` with fresh logs, substituting 240 for Terminal20. Stop on unsafe memory, nonzero exit or sorryAx. A timeout is not mathematical rejection. Do not rebuild Mathlib, compile a larger subtree, overwrite original archives or run the full V2 replay.

The files *_failed_v1/v2 and their logs are unsuccessful preserved drafts. AuthenticCompact20.lean is a literal-generation intermediate; its monolithic acceptance was not used. generate_literals.py/generate_proofs.py create the initial compositional draft, while finish_decoders.py verifies the exact final decoding conversion from Terminal20_failed_v1.lean without rewriting any file. The successful source for acceptance is Terminal20.lean.

extract20.py takes the original extracted V2 root and unchanged V2 ZIP as arguments. It authenticates archive/package/stream/catalog hashes and reconstructs only the prefix through node 67 plus the selected leaves. It does not invoke the full replay or optimize witnesses. The inherited JSON `children.left/right` labels designate sampled terminals 20/23, not both immediate children of node 61. source_geometry.json supplies the unambiguous hierarchy, whose immediate right child is node 63. No such label is a Lean assumption.

All exact hashes and object sizes are in source_hashes.json and SHA256SUMS.txt. DECISIONS.json distinguishes local proof success, external authentication and the still-open complete-root premise. BULK_VERIFICATION.md is a design assessment, not a proven performance claim.
