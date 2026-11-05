# A1294–A1300 forensic audit packet

This is a private, offline recovery and independent-check packet. It preserves the copied October 3 local evidence and distinguishes completed certificates from diagnostic search frontiers. No research source, historical commit, GitHub branch, or Drive file was modified.

## Reproduction

Requirements: CPython 3.12 or later; standard library only. No `mpmath`, SymPy, network access, credentials, or project checker import is needed for the independent exact witness and integrity checks.

From the extracted packet root, run:

```powershell
python verification/verify_manifest.py
python verification/verify_packet.py
python verification/verify_exact_witness.py --output verification/exact_witness_result.json
```

To rebuild the packet checksum file and a ZIP from an unchanged staging tree:

```powershell
python verification/build_manifest.py
python verification/zip_audit_packet.py --output ..\A1294_A1300_COMPLETE_LOCAL_GITHUB_FORENSIC_AUDIT_20261103.zip
python verification/verify_final_zip.py ..\A1294_A1300_COMPLETE_LOCAL_GITHUB_FORENSIC_AUDIT_20261103.zip
```

The same checks were run in normal Python, `python -O`, and `python -OO`; exact witness outputs were byte-identical. `verify_packet.py` checks the V2 package manifest, ZIP CRC, certificate stream hashes, and saved full replay record. It does **not** repeat the historical 18,897.781-second, 13,454,121-node traversal. That traversal's saved PASS record is evidence, not a fresh replay. The V1 launcher is preserved as historical failure evidence and must not be treated as a successful replay.

The `.bat` launchers are included only as source evidence. Do not execute them for this audit: launcher scripts may clear/recreate extraction directories. No new million-node search was started. The V2 package's internal `certificate/SHA256SUMS.txt` refers to three canonical-repository files (`feedback.txt`, `generator.log`, `verifier.log`) that are absent from its ZIP; all actual ZIP members are covered by its package manifest.

## Decision snapshot

- A1294 fixed-catalog certificate: historical independent source-free replay PASS; original GitHub artifact ZIP is not recovered.
- A1295 and A1296: local diagnostics ended with open frontiers; the exact witness does not refute these targets.
- A1297, A1298, A1299, A12994, A1300: exact pointwise counterexamples to the fixed-B catalog inequality, using the unchanged catalog and `B=1094977/5000000000`.
- The witness value is a valid upper bound on any target `A` for which that same global inequality could hold. It does not establish that the value is the optimal/global ceiling.
- No inference is made about the separate q8 route, strict greater-than-79% theorem, or RH.

See the five audit reports and `SOURCE_AND_EXECUTION_HASH_INVENTORY.json`. `SHA256SUMS.txt` covers every packet file except itself (a self-hash would be recursive); the final ZIP SHA-256 is reported outside the ZIP.
