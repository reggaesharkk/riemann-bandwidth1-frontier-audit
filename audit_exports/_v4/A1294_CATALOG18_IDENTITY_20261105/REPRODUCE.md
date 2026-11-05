# Reproduction

## Inputs and environment

The archive contains the frozen V2 input, predecessor checkpoint archives, exact generated source, compiled Lean objects, pinned version/hashes, logs, and the existing node 59/61/63/65 dependency source/object chain under `reference/deps/n59`, `reference/deps/n61`, `reference/deps/n63`, and `reference/deps/n65`. These are byte-preserving copies with shortened directory names to stay within Windows extraction path limits. The full upstream Lean/Mathlib checkout is not vendored. Use the pinned external checkout identified in `environment_pinned.log` and do not rebuild Mathlib unless required by the pinned environment.

Pinned values:

- Upstream formal-math commit: `fba91d214655aaa1fd0504bb893c8859c20c79f9`.
- Mathlib commit: `51e6992efd06126df61a496bebf8f49482a4e129`.
- `leanprover/lean4:v4.33.0-rc2`, Lean commit `d8b18978322de05a8f3dba51ef03cf5461676c17`.
- Lake `5.0.0-src+d8b1897`.
- Pinned `lake-manifest.json` SHA-256: `1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448`.

## Recheck evidence

From this directory, regenerate the inventory and unsigned local provenance record, execute the checks in all Python modes, write the SHA-256 manifest, and validate the extracted tree with:

```powershell
python generate_source_hash_inventory.py
$env:PYTHONPATH = 'reference'
python create_vrk_claim_record.py
python replay_local_tests.py
python write_sha256_manifest.py
python make_checkpoint_zip.py [optional-output-zip-path]
python verify_extracted_packet.py <fresh-extraction-directory>
```

The standalone evidence commands are:

```powershell
python verify_catalog_source.py
python -O verify_catalog_source.py
python -OO verify_catalog_source.py
python verify_terminal18_provenance.py
python -O verify_terminal18_provenance.py
python -OO verify_terminal18_provenance.py
python verify_vrk_claim_record.py
python test_provenance_mutations.py
```

The Python scripts use explicit exceptions, not `assert`, for acceptance conditions. They authenticate the bundled ZIP hash/CRC, compare the 171 ordered source references across the old inline catalog, named 57-entry blocks, original array, and summary records; check the 350 segment / 15 row evidence counts; verify exact source-normalized equivalence; and replay the exact rational anchor/tangent data and source geometry. These Python checks are external evidence and do not replace the Lean proofs.

## Lean source builds

The recorded exact commands and resource data are in each `*.log`. From the pinned WSL project, the proved modules were compiled sequentially with `lean -M6800 --root <audit-root> <file>.lean -o <file>.olean` and an external `LEAN_PATH` containing the pinned project build plus the predecessor node proof directories. Use the same order:

1. `generic_linux/GenericArrayIdentity.lean` (Init-only standalone check).
2. `Catalog18Identity.lean`.
3. `Catalog18AllLookups.lean`.
4. `Terminal18Compositional.lean`.
5. `Terminal18CatalogConnection.lean`.
6. `Terminal18HistoricalAcceptance.lean`.
7. `Source57.lean`, `Node57Helpers.lean`, `Node57Replay.lean`, and `Node57Final.lean`.

The corresponding successful `.olean` files and actual logs are included. Do not copy the Windows/native `GenericArrayIdentity.olean` into the Linux module search path; the compatible pinned Linux object is under `generic_linux/`. Verify each module's `#print axioms` lines in its log. The proofs depend only on standard Lean axioms such as `propext`, `Classical.choice`, and `Quot.sound`.

The bounded `/mnt/c`/ext4 comparison commands and four exact logs are under `resource_bench/`. The small ext4 stage used source and dependency objects copied byte-for-byte from this packet; do not overwrite the recorded stage. `resource_bench/RESOURCE_COMPARISON.md` records the memory limit, timeouts, initial memory state, and why the samples do not establish a speed or RAM optimization.

The final extraction/manifest procedure and resulting ZIP hash are described in `PACKET_VERIFICATION.md`.
