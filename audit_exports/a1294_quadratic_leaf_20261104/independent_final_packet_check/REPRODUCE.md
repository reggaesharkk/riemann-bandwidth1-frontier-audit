# Reproduction instructions

## Exact Python extraction and comparisons

The packet includes the frozen V2 ZIP and the bounded extractor. Extract the V2 ZIP into a temporary folder, then run the extractor in all three modes:

```powershell
python extract_first_quadratic_ledger.py <V2-package-root> > ledger-normal.json
python -O extract_first_quadratic_ledger.py <V2-package-root> > ledger-O.json
python -OO extract_first_quadratic_ledger.py <V2-package-root> > ledger-OO.json
```

The three JSON values must agree exactly. The extractor validates the archive's input and stream hashes, decodes only the prefix through the first terminal, checks each weighted split, and reconstructs the fifteen rational model intervals. It does not run the full-tree certificate replay.

Run the 666-model JSON/Lean field comparison in each mode as well:

```powershell
python compare_catalogs.py <V2-package-root> <pinned-zeta23-root>
python -O compare_catalogs.py <V2-package-root> <pinned-zeta23-root>
python -OO compare_catalogs.py <V2-package-root> <pinned-zeta23-root>
```

Each catalog must have zero model-field mismatches. The comparison reports owner metadata separately; that metadata is not represented by the upstream `MacroPiece` structure.

`python verify_quadratic_leaf_evidence.py <packet-root>` checks the packaged hashes, ZIP CRCs, all three Python-mode outputs, exact rational claims, absence of Lean shortcuts, and the recorded final build/axiom transcript. These checks reproduce the evidence package; only the Lean build kernel-checks the theorem.

## Pinned Lean build

Use an isolated checkout of `anthropics/formal-math` at `fba91d214655aaa1fd0504bb893c8859c20c79f9`, with the included `zeta23/lean-toolchain`, `lakefile.toml`, and `lake-manifest.json`. The manifest pins Mathlib at `51e6992efd06126df61a496bebf8f49482a4e129`. Lean is `leanprover/lean4:v4.33.0-rc2`.

Copy `lean/A1294QuadraticLeaf.lean` to `zeta23/Zeta23/ThmD/Sextuple/A1294QuadraticLeaf.lean`, then run from the `zeta23` directory:

```bash
lean --version
lake --version
git rev-parse HEAD
lake build Zeta23.ThmD.Sextuple.A1294QuadraticLeaf
```

The expected final output is preserved in `logs/build_final_axioms.log`. It compiles the selected module and its dependencies, prints `#print axioms` for the path, anchor, model, tangent, and final box-predicate theorems, and reports a successful 8,706-job build. The local successful run used WSL2; no source-tracked upstream files were changed.

## Expected status

* `authentic_quadratic_leaf_box_predicate`: kernel-checked.
* Source bytes to explicit Lean path: externally hash-checked, not kernel-checked.
* Full original serialization: not parsed by Lean.
* Full A1294 theorem: not proved.
