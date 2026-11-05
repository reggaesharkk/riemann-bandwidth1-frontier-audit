# Reproduction

This proof packet contains the exact frozen predecessor ZIP and the original V2 source ZIP. The pinned Lean/Lake environment and upstream dependency checkout are not vendored; use the verified A1294 project environment recorded in `reference/predecessor/.../environment_pinned.log`.

1. Verify the two source archives against `SOURCE_HASH_INVENTORY.json` and `SHA256SUMS.txt`.
2. Extract `reference/A1294_CATALOG18_IDENTITY_TERMINAL18_NODE57_20261105.zip` to `reference/predecessor/A1294_CATALOG18_IDENTITY_20261105/`. The packet contains the V2 archive at the expected nested input path; verify it is byte-identical after extraction.
3. Extract the V2 archive to `reference/v2_source/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/` if that tree is absent. The included verifier uses this path.
4. Run `python verify_terminal17_reconstruction.py`. It checks archive CRC/manifest, stream/catalog hashes, bounded topology and geometry, catalog selection, all fifteen rows and exact tangent arithmetic.
5. In the pinned WSL project, set `PACKET` to this packet root, `PREV` to its extracted predecessor directory, and `LEAN_PATH` to `PACKET`, `PREV`, every directory containing predecessor `.olean` files, and the pinned `lake env printenv LEAN_PATH`.
6. Compile in order, strictly sequentially: `GenericArrayIdentity.lean`, `Catalog17.lean`, `Catalog17Identity.lean`, `Catalog17BoundaryBlocks.lean`, `Catalog17AllLookups.lean`, `Terminal17Compositional.lean`, then `Node55Replay.lean`. Use the exact pinned compiler, `lean -M6400 --root "$PACKET" MODULE.lean -o "$PACKET/MODULE.olean"`, wrapped in `/usr/bin/time -v` and an external timeout. The successful terminal-17 and node-55 command/resource logs are included. Do not invoke the full V2 replay.
7. Inspect each final module's `#print axioms` output. Expected axiom list for the stated final propositions is `[propext, Classical.choice, Quot.sound]`.

`Node55Replay_failed_v1.lean` is a reconstructed pre-fix draft matching the first compiler errors, paired with the unchanged initial `Node55Replay.build.log`; it is marked reconstructed in the report, not represented as a byte-authenticated original. The successful corrected module is `Node55Replay.lean` with `Node55Replay_retry.build.log` and `Node55Replay.olean`.

