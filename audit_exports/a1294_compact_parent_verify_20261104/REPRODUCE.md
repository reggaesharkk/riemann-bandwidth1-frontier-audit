# Reproduce without a full-tree search

1. Verify SHA256SUMS.txt against every packaged file. The archive CRC and independent extraction checks were also performed when creating this packet.
2. In a disposable directory, extract frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip. Run the bundled extract_siblings.py with the extracted A1294_SOURCE_FREE_REPLAY_PACKAGE_V2 directory and the frozen ZIP as its two arguments. Its output must match authentic_input.json byte-for-byte. This is a bounded prefix reconstruction through node 67, not a full certificate replay.
3. Run `python verify_inputs.py`, `python -O verify_inputs.py`, and `python -OO verify_inputs.py` from this packet directory. No Lean result is inferred from these external checks.
4. Use the exact pinned upstream zeta23 project and Mathlib revisions in REPORT.md. Copy left_preserved/CompositionalLeaf.lean, CompositionalRight.lean and A1294CompactParent.lean into Zeta23/ThmD/Sextuple/ in an isolated copy. Do not change historical research files.
5. Compile left first using `lake env lean Zeta23/ThmD/Sextuple/CompositionalLeaf.lean -o .lake/build/lib/lean/Zeta23/ThmD/Sextuple/CompositionalLeaf.olean`, then the right module with the corresponding right .olean destination, then the parent. These three modules import pinned upstream dependencies; the complete Mathlib/toolchain cache is not bundled. Do not use `native_decide` or replace failures with axioms.
6. Inspect build exits, `#print axioms` and the printed parent proof. The parent must depend on both compact leaf_sound theorems; it must not depend on historical/source_parent_box_predicate. Only propext, Classical.choice and Quot.sound appear in the recorded reports.

Optional literal regeneration, in a copy: `python -X utf8 prepare_right.py`, then `python generate_parent.py`. Exact generated source hashes must match source_hashes.json. These scripts create source literals and proofs from the bundled ledger; the external source-to-literal trust boundary is not eliminated by executing them.

Original left source/object/logs are copied unchanged. The historical parent is for statement comparison, not an imported proof dependency. No claim of full A1294 or of full binary-stream kernel authentication follows from this packet.
