# Build-log status

`build_final_axioms.log` is the authoritative successful build of the exact final `A1294QuadraticLeaf.lean` source. It prints the axioms for the path, anchor, model bounds, exact tangent, tangent checker, and final box predicate.

`build_final.log` is a successful earlier build of the same mathematical proof before two additional `#print axioms` lines were added. `build_success_timed.log` records a direct compiler run from an earlier source iteration. `build_attempt_4.log` is a successful Lake build from an earlier proof iteration. These are retained as predecessor evidence; only `build_final_axioms.log` is tied to the final Lean source hash in `source_hash_inventory.json`.

`build_initial.log`, `build_attempt_2.log`, and `build_attempt_3.log` preserve failed proof iterations. They are not accepted proof evidence. The later successful source contains no proof escape and has a successful kernel build.
