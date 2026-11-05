# WP19 → A1294–A1300 → WP84 recovery packet

This is a private, additive historical-recovery and erratum packet. It does not replace the existing A1294 forensic ZIP, alter research history, or promote the frozen WP84 claims.

## Reproduce the lightweight checks

From the extracted packet root, using Python 3.10+ and only the standard library:

```powershell
python verification/verify_a12994_erratum.py --output results/a12994_exact_replay.json
python -O verification/verify_a12994_erratum.py
python -OO verification/verify_a12994_erratum.py
python verification/check_wp19_archives.py
python verification/check_a1294_v2_package.py
python verification/verify_packet.py
```

The A1294 script re-evaluates the saved rational point against all 666 catalog models and all 15 contiguous partial sums. It is not a branch-and-bound search and does not rerun the 13,454,121-node certificate.

## Evidence layout

- `evidence/a1294_original_audit/` contains selected predecessor files byte-for-byte, including the erroneous checker/output, and the full predecessor ZIP as an untouched nested artifact.
- `evidence/a1294_source_free_v2/` contains the original local V2 replay ZIP and its result/manifest.
- `evidence/catalogs/` contains the exact catalogs needed by the independent Fraction checker.
- `evidence/wp19_archives/` contains nine recovered WP19 ZIPs. The large M14 split archive is not duplicated; `evidence/m14_metadata/M14_parts_sha256.json` records the hashes and verified internal member checksums.
- `evidence/wp84_october_sources/` contains selected October source notes and code extracted without changes. The older public-note versions are stored separately under `evidence/wp84_older_public_snapshot/`.
- `SOURCE_HASH_INVENTORY.json` records source commit, external archive hashes, member hashes, and limitations. `SHA256SUMS.txt` covers every packet file other than itself.

## Limits

The original GitHub Actions ZIP expired and was not recovered. The DOI reader could not access either Zenodo record. The D-drive checkout and WSL were inaccessible. These are not treated as proof of absence. No expensive historical search was restarted.
