# A1294 two-quadratic parent proof packet

This packet records a kernel-checked complete two-terminal parent subtree from frozen source-free V2 data. The proof is source-authenticated by bounded external replay, while the raw serialization-to-Lean-literal bridge is explicitly not kernel formalized. See `PROOF_AUDIT.md` for exact scope, decisions, limitations, and resources.

## Pinned build

- Upstream `anthropics/formal-math`: `fba91d214655aaa1fd0504bb893c8859c20c79f9`
- Mathlib: `51e6992efd06126df61a496bebf8f49482a4e129`
- `lean-toolchain`: `leanprover/lean4:v4.33.0-rc2`
- Lean commit: `d8b18978322de05a8f3dba51ef03cf5461676c17`

The packet includes the pinned `zeta23` project source subset and lock files under `upstream/zeta23`, the V2 source ZIP plus an extracted copy under `v2_input`, the exact extracted ledger, the Lean module, its generators, prior packets, successful/failed logs, and the compiled parent `.olean`.

## Replay the Python source bridge

From this directory, set `V2ROOT` to `v2_input/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2` and `V2ZIP` to `v2_input/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip`:

```powershell
$V2ROOT = (Resolve-Path .\v2_input\A1294_SOURCE_FREE_REPLAY_PACKAGE_V2).Path
$V2ZIP = (Resolve-Path .\v2_input\A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip).Path
$env:A1294_REPLAY_LOG_DIR = (Resolve-Path .\logs\replay2).Path
python .\source\extract_siblings.py $V2ROOT $V2ZIP > .\logs\replay2\extract_normal.json
python -O .\source\extract_siblings.py $V2ROOT $V2ZIP > .\logs\replay2\extract_O.json
python -OO .\source\extract_siblings.py $V2ROOT $V2ZIP > .\logs\replay2\extract_OO.json
python .\source\verify_pair_ledger.py
python -O .\source\verify_pair_ledger.py
python -OO .\source\verify_pair_ledger.py
```

The outputs should be byte-identical. Exact checks use Python `fractions.Fraction`; no optimization search is run.

## Recompile the Lean theorem

Use the pinned upstream/Mathlib checkout and copy `source/A1294TwoQuadraticParent.lean` to `zeta23/Zeta23/ThmD/Sextuple/`. Then run:

```bash
lake env lean Zeta23/ThmD/Sextuple/A1294TwoQuadraticParent.lean -o /tmp/A1294TwoQuadraticParent.olean
```

The source file ends with `#print axioms` for the parent/child split and each predicate. Confirm the proof declarations have no `sorryAx`. The included `.olean` was produced by this command in the pinned environment; its hash is in `SHA256SUMS.txt`.

The source bundle does not vendor Mathlib itself. A local checkout/cache at the pinned manifest revision is required to recompile.

## Manifest

`SHA256SUMS.txt` contains hashes for every packet file except itself. The manifest file's own SHA-256 is recorded in `MANIFEST_SHA256.txt`. The ZIP's SHA-256 and byte length are recorded outside this extracted packet alongside the archive.
