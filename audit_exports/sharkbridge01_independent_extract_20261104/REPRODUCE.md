# Private reproduction

Do not execute released CLIs, provider integrations or signer initialization. No keys, API access or network are needed for the included tests.

1. Verify SHA256SUMS.txt and evidence.sha256. Run `python verify_experiment.py`, then with `-O` and `-OO`.
2. Run codec.py and structural_test.py in a disposable copy; both only read copied sources/data and write experiment outputs. codec.py executes an AST allowlist of four audited pure parser/hash helpers, not whole original modules. The complete copied helper files are retained for provenance and notices.
3. Run generate_wire_lean.py and compare the resulting WireParent.lean SHA-256 against evidence.json. Python conversion and byte authentication remain external to the kernel.
4. Use pinned upstream zeta23 fba91d214655aaa1fd0504bb893c8859c20c79f9 and Mathlib 51e6992efd06126df61a496bebf8f49482a4e129 with Lean 4.33.0-rc2. Existing matching dependencies are needed; this packet does not vendor the full toolchain or 6-GB Mathlib cache.
5. Create a read-only dependency link overlay using `python3 link_dependencies.py /path/to/zeta23/.lake/build/lib/lean/Zeta23 /path/to/experiment/baseline/lib/Zeta23`. Never link the three certificate output files: the script excludes them explicitly. LEAN_PATH chooses the first matching Zeta23 package root, so that root must have the common dependencies. The captured first setup failure demonstrates this requirement.
6. From the pinned project, run `lake env bash /path/to/experiment/build_baseline.sh` (600-second outer timeout was used). Then run `lake env bash /path/to/experiment/build_wire.sh`. Both scripts are serial and capped; do not run concurrent heavy builds. Inspect exits, printed axioms and printed parent proof. Imported-object caches are trusted as ordinary existing Lean builds; no separate full-library -t0 replay is included.
7. Import-only: under the same LEAN_PATH and `lake env`, compile ImportOnly.lean with `lean -M 6800 --root /path/to/experiment ImportOnly.lean -o ImportOnly.olean`. Time/RSS measurements depend on cache state. Do not infer pure kernel replay speed or subtract peak RSS values.

The three baseline Lean sources and newly compiled objects are included. Read-only upstream dependency links are excluded from the ZIP and represented by an inventory; recreate them locally. The frozen previous packet also retains original source/lockfile provenance. Tests do not claim independent authentication of published releases, mathematical correctness from a signature, full source-stream kernel decoding or a full A1294 theorem.
