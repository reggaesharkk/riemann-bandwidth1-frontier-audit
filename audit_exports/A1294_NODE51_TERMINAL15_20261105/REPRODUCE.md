# Reproduction

## Integrity and source reconstruction

From this directory, verify the file inventory with the included IntentSeal/Reggae Shark Protocol verifier:

```powershell
python .\protocol\verify_candidate_manifest.py
```

Extract `reference_inputs/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip` into a writable scratch directory. Then run the exact source and selector replayer from this directory, substituting the extracted V2 package root and ZIP paths:

```powershell
python .\verify15_reconstruction.py <V2-package-root> .\reference_inputs\A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip .\terminal15_authentic_input.json
python -O .\verify15_reconstruction.py <V2-package-root> .\reference_inputs\A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip .\terminal15_authentic_input.json
python -OO .\verify15_reconstruction.py <V2-package-root> .\reference_inputs\A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip .\terminal15_authentic_input.json
```

For this packet, the outputs are recorded as `terminal15_reconstruction_final_{normal,O,OO}.log`. They pass. The external verifier checks exact rational arithmetic and source/catalog correspondence but is not a Lean theorem.

To reproduce tree source generation, first extract the V4 archive to a scratch directory. Pass its `Node53Replay.lean` and `Node53Replay.olean` with `generate_node51_replay.py`; the script reads the V2 topology bytes and checks the source-selected terminal record before generating. The three output runs are `multi_leaf_generator_v1_{normal,O,OO}.log`; each generated file is text-identical to `Node51Replay.lean`.

## Lean kernel builds

Use the pinned zeta23 project and environment in `ENVIRONMENT.txt`. Extract the V4 archive to a directory with its existing source and object tree. From the pinned zeta23 project, set `DEST` to this extracted packet directory, `V4` to the extracted V4 directory, and `VD` to the colon-separated parent directories of the V4 `.olean` files. Append the project environment from `lake env printenv LEAN_PATH`.

Run these sequentially in order. The existing source files and `.olean` outputs are included for inspection; the build logs record the actual exits and resource output.

```bash
lake env lean -M6400 --root "$DEST" "$DEST/Catalog15.lean" -o "$DEST/Catalog15.olean"
lake env lean -M6400 --root "$DEST" "$DEST/Catalog15Identity.lean" -o "$DEST/Catalog15Identity.olean"
lake env lean -M6400 --root "$DEST" "$DEST/Catalog15BoundaryBlocks.lean" -o "$DEST/Catalog15BoundaryBlocks.olean"
lake env lean -M6400 --root "$DEST" "$DEST/Catalog15AllLookups.lean" -o "$DEST/Catalog15AllLookups.olean"
lake env lean -M6400 --root "$DEST" "$DEST/Terminal15Compositional.lean" -o "$DEST/Terminal15Compositional.olean"
lake env lean -M6400 --root "$DEST" "$DEST/Node51Replay.lean" -o "$DEST/Node51Replay.olean"
```

`Node51Replay` imports terminal 15 and the existing node-53 replay. The included `reference_dependencies/Node53Replay.olean` is byte-identical to the V4 input object; its imports are resolved from the extracted V4 bundle. No terminal-16-or-earlier leaf is rebuilt by the node-51 module.

## Provenance tools

`create_node51_vrk_record.py` and `verify_node51_vrk_record.py` use the archived VRK canonical hashing and evidence-root functions in `reference_dependencies/vrk/`. The record is unsigned and does not establish theorem truth.

`protocol/verify_candidate_manifest.py` is the actual archived fail-closed file inventory verifier. It checks the local file manifest only; it is not the signed IntentSeal ledger/head verifier. No signing credentials or API services are required or used.

`MANIFEST_SHA256.txt` covers all packet files other than itself. It can be regenerated with `python .\write_manifest.py` and checked with the protocol verifier. The outer ZIP SHA-256 must be recorded independently after export.
