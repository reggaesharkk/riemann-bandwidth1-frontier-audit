# Local Git / two Google Drives / DOI reconciliation runbook — 2026-11-05

**Intent:** Safely complete the synchronization *after* the GitHub documentation branches are reviewed. This runbook is NOT evidence that files have already been uploaded or copied into either Google Drive or the user's laptop repositories.

## Current remote GitHub state

- Private repository: `reggaesharkk/riemann-bandwidth1-frontier-audit`; branch `audit/a1294-proof-timeline-20261105`; draft PR #6. Existing PRs #1–#5 remain untouched. Initial `main` HEAD at reconciliation: `7cd74b347369e933f8da634001611f625e6a797f`.
- Public repository: `reggaesharkk/riemann-bandwidth1-verification`; branch `docs/20261105-private-audit-status`; draft PR #1. Initial `main` HEAD: `4cec55eb89ddcdfac8f1b06ecec28b06632973d8`.
- These PRs are draft and **not merged**. No Git tag, GitHub release, DOI or license is changed.
- The historical public `v0.1.0` source tag and DOI are intentionally immutable.

## Local Codex worktree safety

Before doing anything:
1. Inspect `git status --short`, `git branch -avv`, `git remote -v`, `git log --all --date=iso-strict --decorate --oneline`, and `git worktree list` from **each** local repository; save outputs as dated audit attachments.
2. Confirm which worktree contains the 2026-11-05 proof packets. Do not assume its current branch matches the GitHub draft branch, nor that `git checkout` or `git pull` is safe with uncommitted changes.
3. Confirm every packet's size, SHA-256, manifest and source-prefix version. The latest expected local input is `audit_exports/A1294_NODE51_TERMINAL15_SOURCE_CONNECTED_REPLAY_20261105.zip`, reported size `337171866` and SHA-256 `2461505d5cf86aeceb0dce12ad50fcddae1958cad9e12f316b5d49234fc3ac83`. A mismatch is a STOP, not a reason to rebuild or overwrite.
4. Preserve original commits, worktrees, draft PRs and failed run logs. Keep source-only additions and documentation as additive Git commits; never force-push, rebase historical evidence, alter tags or auto-merge.

## Artifact placement

- The 337 MB nested evidence ZIP should **not** be sent through ordinary GitHub contents API or committed into the curated public repository. Prefer private Drive archiving and hash-linked Git manifests. Evaluate Git LFS/release asset policy and permissions separately if private GitHub binary storage is required.
- If adding source/proof files to the private Git branch, check upstream licenses and byte-to-literal provenance, commit immutable relative paths, and reference each original packet SHA. Do not accidentally publish `.olean`, original V2 binary streams, private working papers or proprietary/unlicensed source.
- Keep `main` and all v0.1.0 publication metadata unchanged until a separate review/merge decision.

## Google Drive #1 — primary

- This Drive has multiple archived A1294 families, including the folder named `A1294_SOURCE_FREE_REPLAY_V2` (`1F3_JCRisQ1nLmndWBWA0MDFtswGCVsSW`) and nested package folder `A1294_SOURCE_FREE_REPLAY_PACKAGE_V2` (`129BxyQoF4ouSZksBFjVZWGzJVG48dEEg`).
- Two folders are named `29` (`15i1BvfxmtvfbCBaXhge0F0LK93ualy5B` and `1PGgpkNhg38w-vkYdu3K_BXfoWVcHgbnr`), so identify the intended parent by full folder ID/contents, not name alone.
- Before upload, inspect duplicates by filename **and** SHA-256; add a versioned file without overwriting any historical original. Record resulting file ID, URL, sharing state and a downloaded-byte hash.

## Google Drive #2 — separate connected account

- The secondary Drive search located research/portfolio documents but did not establish that the latest A1294 packet has been uploaded.
- Treat the secondary account as a distinct archive. Confirm intended destination folder, private sharing and available storage before uploading the same checked bytes. Capture its own file ID/URL and downloaded SHA-256. A link or file title alone does not establish byte identity.

## DOI and archival release

- Existing fixed DOI: https://doi.org/10.5281/zenodo.23244818; concept DOI: https://doi.org/10.5281/zenodo.23244817.
- DOIs and their original v0.1.0 archived contents are **not** updated by changing GitHub documentation. A new deposit/version is a separate publication decision after rights, science and provenance review; do not use an open-status draft as a Zenodo release.
- When citing, distinguish: fixed v0.1.0 DOI versus latest private November proof packet, which currently has **no independently verified new DOI**.

## Completion gate

Declare `LOCAL_AND_BOTH_DRIVES_SYNCED` only after: (a) verified original ZIP bytes and saved Git history; (b) independently checked exact copies in each intended Drive; (c) matching Git source/manifests; (d) privacy and permission inspection; (e) no tag/release/license/DOI change; and (f) per-repository draft PR review. Until then: `REMOTE_GITHUB_DOCS_STAGED; LOCAL_AND_CLOUD_BYTE_SYNC_PENDING`.
