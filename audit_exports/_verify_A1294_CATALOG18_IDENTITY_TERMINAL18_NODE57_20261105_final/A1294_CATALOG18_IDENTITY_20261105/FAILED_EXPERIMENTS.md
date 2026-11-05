# Preserved failed experiments and their interpretation

All entries below are retained under the original names; none was silently repaired or relabeled as a mathematical counterexample.

1. **Broad catalog unfolding exceeded the available elaboration budget.** Earlier terminal-18 drafts used `simp [catalog]` across the 171 references and stalled/timed out. See `failed_drafts/terminal18/` and `catalog_all_lookups_failed_v1.log`, `catalog_all_lookups_failed_v2.log`. This was an elaboration/resource issue, not a false lookup or rejected leaf.
2. **Cross-architecture `.olean` import.** A Windows/native `GenericArrayIdentity.olean` was rejected by pinned WSL Lean with `incompatible header` when imported into a Linux Lean process. See `catalog_identity_cross_arch_failed.log` and its draft. The generic theorem was then embedded/rebuilt in the matching pinned environment; the cross-architecture object is retained but not used.
3. **First catalog identity import path.** An initial build could not resolve `Catalog18Lookup`; module search configuration was corrected. The catalog identity proof itself subsequently compiled.
4. **First generated lookup script.** Boundary proofs at indices 57 and 114 were already solved by imported block-boundary theorems, so generated scripts reached “No goals to be solved.” The final script reuses these lemmas and proves all indices. This is an elaboration-script correction, not a mathematical failure.
5. **Initial node-57 module search path.** The first `Source57`/replay attempt could not find the imported node-65/source dependencies. After adding the predecessor object directories to the search path, the final Source57, helper, replay, and final statement modules compiled.
6. **Python launcher mismatch in this session.** `py -3` reported “No installed Python found”; the host Python 3.12.10 executable worked. This was an environment launcher issue. The test scripts passed with normal Python, `-O`, and `-OO`.
7. **A test-assert audit correction.** During this checkpoint, the verifier's two line-count checks were changed from Python `assert` to explicit `require` exceptions so they remain active under `-O`/`-OO`. This changed only the new audit verifier, not research inputs or proof source. All three modes were rerun successfully.

None of these failures is evidence of mathematical rejection. The successful proof source does not rely on them.
