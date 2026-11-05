# Riemann audit export synchronization — 2026-11-06

This record adds the source and textual evidence material under `audit_exports/` to the public repository. The synchronization began at local commit `eb36159ee7e57053fcae3de025fe4dac539435ab` on `codex/cross-project-math-frontier-20261103`.

## Included in Git

The sync set contains 5,044 source/evidence files (293,255,235 bytes): Lean and Python sources, audit reports, logs, JSON records, scripts, and small text evidence. `AUDIT_EXPORTS_SYNC_MANIFEST_20261106.json` records the path, byte length, SHA-256, and disposition of every file found in the local audit-export tree. The included files were scanned for common GitHub, AWS, Slack, and private-key credential patterns; no matches were found.

The manifest generator is `audit_exports_sync_manifest.ps1`. It is read-only with respect to the audited files and writes the inventory and Git pathspec in the repository root.

The root `.gitattributes` marks `audit_exports/**` as byte-preserving (`-text`) so a clone does not rewrite line endings and invalidate the recorded source hashes.

## Archive and generated-artifact inventory

The local tree contains 217 ZIP paths totaling 5,342,255,030 bytes. They represent 56 distinct archive byte streams totaling 2,462,048,823 bytes after SHA-256 deduplication. The individual files are below GitHub's 2 GiB release-asset ceiling; the candidate list is in `AUDIT_EXPORTS_RELEASE_ASSET_CANDIDATES_20261106.json`. These binaries are not Git blobs in this source-sync commit. Generated Lean objects and raw build artifacts are likewise inventoried but not added to ordinary Git. The nested `sharkbridge01_worktree` and `__pycache__` copies are excluded as scratch/build copies.

This commit does not claim that those release candidates have been uploaded. The source/evidence branch and existing Git refs are synchronized separately from those large archive payloads. The manifest makes the remaining local-only payloads and hashes explicit.

## Reproduce the inventory

From the repository root in Windows PowerShell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\audit_exports_sync_manifest.ps1
```

The script hashes every non-scratch file in `audit_exports/`; scratch copies are explicitly marked `NOT_HASHED_SCRATCH`. It does not modify, remove, or execute any research source.

## Scope and theorem status

This is a repository synchronization record only. It does not change any A1294 or WP84 proof decision and does not claim the full A1294 root predicate or any WP84 theorem is proved.
