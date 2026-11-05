# Reproduction

## Python source/witness replay

Use Python 3.12.10. From this directory run sequentially:

```powershell
python verify_terminal16_reconstruction.py
python -O verify_terminal16_reconstruction.py
python -OO verify_terminal16_reconstruction.py
```

The recorded outputs are `replay_normal.log`, `replay_O.log`, and `replay_OO.log`. All exited 0. The checker uses explicit `require` failures rather than `assert`, so optimized modes do not remove its checks.

## Lean acceptance and node replay

Use the exact Formal Math / Mathlib commits and Lean/Lake versions in `ENVIRONMENT.txt`. Install or select the pinned `zeta23` project, without rebuilding Mathlib if the pinned objects are available. Set `LEAN_PATH` to include this packet directory, `reference_packet`, `reference_predecessor`, and every directory containing an included `.olean`, followed by the pinned project's `lake env printenv LEAN_PATH`.

From the pinned `zeta23` project, the successful commands were:

```bash
lake env lean -M6400 --root "$DEST" "$DEST/Terminal16Compositional.lean" -o "$DEST/Terminal16Compositional.olean"
lake env lean -M6400 --root "$DEST" "$DEST/Node53Replay.lean" -o "$DEST/Node53Replay.olean"
```

The complete timed commands, exits, theorem statements, and axiom reports are preserved in the two `.build.log` files. `Node53Replay` imports the already compiled `Node55Replay.olean`; it does not rebuild the predecessor subtree's leaves. The archive does not bundle Lean, Mathlib, or their full external package closure.

## Packet integrity

Run:

```powershell
python verify_evidence_packet.py
```

The verifier checks the outer evidence manifest and exact predecessor/V2 ZIP hashes. The manifest does not authenticate the ZIP publisher; it detects byte changes relative to this packet.

From a writable workspace directory, use Python's `zipfile` implementation for independent fresh extraction, CRC/path checks, and normal/`-O`/`-OO` replay from the extracted copy:

```powershell
python independent_extract_check.py A1294_NODE53_TERMINAL16_PROOF_PACKET_20261105.zip
```

The checker leaves the fresh extraction as a sibling directory so it does not depend on the restricted Windows temporary directory. An initial attempt using the sandbox temporary directory failed with `PermissionError` before creating the extraction; its log is retained as `failed_sandbox_temp_extraction.log`. That failure was environmental and says nothing about archive integrity.
