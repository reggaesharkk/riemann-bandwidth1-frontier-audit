# Bounded multi-leaf generator and scaling feasibility

## Tested architecture

The experiment separates five stages and keeps the trust boundary visible:

1. **Source parsing:** `extract15_reconstruct.py` reads the V2 topology/kind/anchor streams and catalogs, performs a bounded DFS with the frozen weighted split rule, and emits exact terminal-15 JSON. It does not search or regenerate witnesses.
2. **Source/certificate replay:** `verify15_reconstruction.py` independently checks the V2 archive/manifest hashes, source path and anchor bytes, catalog hashes, deterministic catalog selection, segment interval coverage, 15 rows, and exact rational tangent. Normal, `-O`, and `-OO` all pass.
3. **Catalog and Lean-literal generation:** `generate_terminal15_catalog.py` creates the source-ordered selected catalog, compositional identity and lookup modules. `generate_terminal15_compositional.py` emits the exact 15 row definitions and all 369 segment occurrences from the recovered JSON and lookup map.
4. **Leaf acceptance:** Lean proves catalog identity, every required lookup, each row/segment check, the tangent check, `AuthenticCompact15.accepted_original`, and `AuthenticCompact15.leaf_sound`.
5. **Tree replay:** `generate_node51_replay.py` reads the frozen V2 byte stream, validates the recovered terminal data and the existing Node53 source/object, and constructs the node-51 token/payload streams from terminal 15 plus the authenticated node-53 subtree. Its output is byte-for-byte identical to the Lean source that compiled as `Node51Replay.olean`.

The multi-leaf stage reuses `Node53.replay53` with its exact existing `.olean`; it adds one terminal and proves the enclosing split and cursor transport. It does not regenerate or recompile the eight predecessor leaves.

The generator also rejects four altered inputs: a wrong split axis, a changed serialized anchor code, a nonmatching V2 archive hash, and a mutated Node53 object. These controls test the Python generator's fail-closed guards; they do not replace Lean acceptance or prove source authenticity.

## Measured bounded sample

The six sequential Lean stages compiled in 9:04.99 total wall time. Peak RSS across them was 5,559,236 KiB (about 5.30 GiB), below the per-process `-M6400` setting; no swap occurred. The full per-stage CPU, wall, RSS, page-fault, exit, source-size and `.olean`-size values are in `RESOURCE_BENCHMARK.json` and the individual build logs.

The six new object files total 14,823,728 bytes: the terminal-15 acceptance object is 12,449,128 bytes and the node-51 replay object is 607,232 bytes. The generated replay module is 8,883 source bytes. The V4 predecessor bundle contains 56 `.olean` files totaling 91,149,472 bytes; that is an inventory of the preserved bundle, not a minimized dependency-closure measurement. Node 51 directly imports the existing 601,856-byte `Node53Replay.olean`. Lean/Mathlib's external imported object closure is not bundled or included in those sums.

The exact-data verifier took 1.326–1.349 seconds across normal, `-O`, and `-OO`; the multi-leaf replay source generator took 0.634–0.665 seconds. These are Python-side checks and source assembly times. They are not end-to-end proof verification times. Lean did the acceptance/replay verification.

The observed costs show a viable small-chunk proof composition, not scalable full-tree throughput. A single authentic leaf still costs about 12.45 MB of `.olean` data and about four minutes in this environment; peak memory is dominated by the shared Lean/Mathlib process environment. No cache-controlled or large multi-chunk benchmark was run, so full-certificate feasibility remains OPEN.

## Source parser / catalog-selection bridge

The minimal eventual trusted bridge is either (a) a Lean parser for the frozen binary streams plus a Lean implementation/equivalence proof for the deterministic catalog selector, or (b) an independently verified translator that emits a Lean-checkable certificate whose source offsets and selected catalog references are themselves proved against the original bytes. A hash or VRK/IntentSeal receipt can bind the bytes and output but cannot establish that semantic mapping. This experiment uses exact external Python reconstruction and therefore leaves that bridge external.

## VRK / IntentSeal scope

The packet uses the existing VRK canonical JSON digest and evidence-root functions in `reference_dependencies/vrk/` to bind named evidence. It also runs the preserved IntentSeal/Reggae Shark Protocol candidate-manifest verifier against the packet's file manifest. This is integrity/provenance evidence only. No signed ledger, Ed25519 key, private credential, external freshness pin, or signature claim was used. The predecessor's source audit records a version-label mismatch between the protocol kernel header (1.3.2) and `pyproject.toml` (1.3.3.dev0); that historical mismatch remains visible in the V4 archive and is not resolved here.
