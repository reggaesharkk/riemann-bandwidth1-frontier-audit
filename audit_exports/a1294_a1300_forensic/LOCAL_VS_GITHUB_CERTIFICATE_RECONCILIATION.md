# Local / GitHub certificate reconciliation

## A1294 Actions record

Read-only GitHub connector inspection reported workflow run `37133363690` on commit `3b748a75ad619ee130c4fabd22792102ccbe986c`, workflow `.github/workflows/a1294-seam-full-certificate.yml`, event `push`, run attempt 2. Run conclusion was `success`; the `generate` and `verify` jobs both succeeded, including the independent verifier and hash-freeze steps. The run is associated with the A1294 PR work, whose PR head was `de11ac12…`.

The historical artifact record identifies artifact `11286675906`, name `a1294-seam-aware-full-certificate`, size 6,737,519 bytes, and SHA-256 `11c1ab1820039284f60e492fe609f6a497175284acdd0c3c53d6ab62b8b1cd19`. The preserved local inventory was collected on 2026-10-08 and then marked the artifact unexpired, with expiration `2026-11-02T22:30:42Z`. On the November 3 audit date, the GitHub artifact listing was empty and the recorded direct download request returned HTTP 404. Therefore the original Actions ZIP was **not** recovered or independently rehashed in this audit.

## Recovered local V2 package

The local V2 source-free package ZIP is a distinct artifact:

```text
Name:   A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip
Bytes:  5,672,384
SHA256: 3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5
```

Its package manifest covers 14 packaged members. This audit independently checked each packaged file length and SHA-256, the ZIP CRC, and the three binary certificate-stream hashes. It also checked the included saved result: `A=647/50000`, `B=1094977/5000000000`, status `PASS`, 13,454,121 nodes, 6,727,061 leaves (6,725,258 quadratic; 1,803 tail), maximum pending stack 55. Saved runtime is 18,897.781 seconds on CPython 3.12.10 / Windows 11 ARM64.

The result record reports exact smallest margins:

- quadratic: `33853157328150681621271330867899241/8192000000000000000000000000000000000000000000`
- tail: `49931/250000000`

The audit rechecked all manifest-covered package bytes and the fixed-B point witness, but did not repeat the five-hour traversal. The source-free V2 package is evidence of a historical independent replay; it is not a recovered copy of the expired GitHub artifact.

The archive's own `certificate/SHA256SUMS.txt` also names canonical-repository paths for `feedback.txt`, `generator.log`, and `verifier.log`; those three files are not ZIP members. The V2 `PACKAGE_MANIFEST.json` instead hashes all 14 actual package members and was verified here. Thus the three absent canonical log/feedback entries are documented provenance gaps, not silently treated as bundled files.

## Earlier package and PR context

- V1 package SHA-256: `14db7449078ff7f60962c1dca8a5bc5ca2b414be2ee66d173870e6f05ffdd124`. Its launcher failed on Windows because a trailing backslash escaped the quote in `--package-root %~dp0`; preserve this as a failure, not as a pass.
- PR #1 concerns the A1290 replay, not an A1294–A1300 result. Its recorded independent run passed 3,550,925 nodes / 1,775,463 leaves over 602 catalog entries and 31,664 seams; the Lean rebuild was not run.
- PR #2 remains open at head `de11ac12a161f93bba311b1ab251d2567f2772b3` (base `d7a371fcd1605d71e2bede7542fb2061a10acdb7`), target `A=0.01294`, `B=1094977/5000000000`; its body lists source-free external replay, Lean integration, same-lineage priority search, and release/rights/DOI checks as remaining gates.
- PR #3 remains an open draft at `630af9b066cd84af9a2a92ded6f1a569367eb916`, a distinct q8/eta retune importing separate q8 certificates; it does not certify any A1294–A1300 row here.
- Upstream PR #17 is in `anthropics/formal-math` and pins source head `fba91d214655aaa1fd0504bb893c8859c20c79f9`; it is not the same candidate certificate or repository state.

Repository copies observed read-only:

| Location | HEAD | Ref/status |
|---|---|---|
| Downloads clone | `908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5` | `research/frontier-7962-hostile-audit-v0.1`, no short-status entries observed |
| second worktree `dd2a` | `e61f116ac3eb4b07bf1df3e91960d84a6f730034` | detached HEAD; unrelated untracked SHARKLANG/output/release files observed and left untouched |
| current audit worktree | `eb36159ee7e57053fcae3de025fe4dac539435ab` | existing `codex/cross-project-math-frontier-20261103`; pre-existing untracked materials preserved; this packet is additive under `audit_exports/` |

