# GitHub, Drive, local archive and DOI reconciliation

Snapshot date: 3 November 2026. Read-only inspection only.

## A1294 GitHub source and certificate record

The A1294 source files at their recorded commits match the Git blob SHA-1 values returned by the connected GitHub source inspection. Independent local SHA-256 hashes are:

| Role | Commit | Path | Bytes | Git blob SHA-1 | SHA-256 |
|---|---|---|---:|---|---|
| Generator | `79d19eaca41874c6994e514cebe86b848366ecd7` | `src/a1294_certificate_generator.py` | 7,136 | `11ebe5707b2ef118cbad5b5307d45359f7787173` | `ca3309ada7ea69f95c032830e06dff1b4e4747cdb0b9b87c15f373fc88adfa7d` |
| Independent verifier | `a52128bae18adeb38fd20c8067c57ba70216271d` | `src/a1294_certificate_verifier.py` | 9,975 | `cec96888c0dbdcaf85708b1df81b1039be35c670` | `50ea847b19f518533039480f9681b8840b6bb96e5b3d573b2f386df8ce401ca9` |
| Actions workflow | `3b748a75ad619ee130c4fabd22792102ccbe986c` | `.github/workflows/a1294-seam-full-certificate.yml` | 2,989 | `d726cb17b6627cef4775e1cd03df3b5990939647` | `19631d6ba229c6829baa00c5f3879c5cd30b125467a8199f841c12e7da757a2e` |
| Frozen result JSON | `420d65cec710dcdaa2aad6e63d035667dcc189e2` | `results/optimization/a1294_full_certificate_final_freeze.json` | 2,553 | `ff421196cfd0db69b4e65ea1d3398c2ac6f83310` | `0b75610625cf0fdbb4e1de65f00f94d525545e65643a72941a5174d84e74ddee` |

Connected GitHub metadata reports private PR #1 open and unmerged, PR #2 open and unmerged at the A1294 head, PR #3 open/draft for a separate q=8 retune, and external PR #17 open. PR #2 reports run `37133363690` as successful and gives the original Actions artifact ID/hash. Its artifact expired on 2 November and was not recovered or rehashed. The saved local V2 replay is a distinct artifact. Therefore this packet verifies the current stored local V2 package and the historical source commit bytes; it does not independently reconstruct the expired Actions ZIP.

## Google Drive V2 source-free package

The connected “Mr Shark” Drive collection contains folder `1XoKubUTXaxIzwha-kbmJUXkQBIL1TOd2` (`A1294_SOURCE_FREE_REPLAY_PACKAGE_V2`) with data, certificate, replay script, package manifest, result and log files. The three fetched catalog files match the corresponding local catalog bytes exactly:

| Drive file | Drive ID | Bytes | SHA-256 |
|---|---|---:|---|
| `macro-data-exact.json` | `1mGh7V4a-ENeQhKdxGRIpueSyigMe0QwP` | 17,396 | `961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b` |
| `refinement-catalog-v1-exact.json` | `1GruYyoHoz5hlWqPfOFbRnTuaqGRPHrPd` | 67,741 | `3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9` |
| `refinement-catalog-v3.json` | `1IfNPJuftnpFe3oo6-lZ__1Ipa2eaTQcn` | 132,964 | `7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d` |

Drive `A1294_SOURCE_FREE_REPLAY_RESULT.json` SHA-256 is `7de6a70671dee42307847e3b321389f1bdfcae66f8bc73b99b0227a6c8e54db0`; its 1,442 bytes exactly match the local extracted V2 result. Drive `PACKAGE_MANIFEST.json` SHA-256 is `4b125bfb8c94a382afa3b0e7dede37e7c411278d406597b51dd314e0ce566fe4`; its 2,131 bytes exactly match the local manifest. The manifest records the three catalog hashes above and a 14-member package. Drive lists the certificate arrays; the local V2 package contains the same manifest-covered arrays, whose member digests were checked by the predecessor audit. This does not identify those arrays as the GitHub Actions artifact.

The second connected Drive collection did not return the V2 folder or WP19/M14 archives in targeted title queries. It did return portfolio/technical-specification documents that mention the DOI string; it did not provide a DOI record payload.

## WP84 archive version reconciliation

The October full source, incremental archive and private prepublication archive contain byte-identical copies of the selected R400 filtered-kernel source and notes. The older public `riemann-bandwidth1-verification-0.1.0.zip` has the same SHA-256 for `src/wp84_r400_filtered_connected_kernel.py` as the October full source (`1a8b339f944bd5bcc776da5ce2608a980a1b0161b64174f8ce30bed17cf52486`), but its note SHA is `5df4b27870bf774998faffb29a2c1b1f9fdcd274dbcd4001e82a14de837eab86`; the October note SHA is `35fabf8e14cca2b5da08f1d6a20814de5e5148f4dd0f9127a681d1662629ccc7`. Both notes are included under distinct provenance paths.

## WP19 v0.25b checksum detail

All five N14–N18 signed JSON payloads and `WP19_v0_25b_SUMMARY.json` match the digests listed in `SHA256SUMS.txt` when the stale `final/` prefix is treated as an archive-root path. The archived checksum manifest itself is named `SHA256SUMS.txt`, not `final/SHA256SUMS.txt`, and its listed digest does not match the archived manifest bytes. The old verifier flags the missing prefixed names. This is a packaging/self-digest issue; it does not invalidate the six verified payload JSON hashes or expand the finite theorem scope.

## DOI status

Target identifiers are `10.5281/zenodo.23244818` and concept DOI `10.5281/zenodo.23244817`. Direct DOI resolver and Zenodo record URLs were inaccessible through the available web reader on this pass. Targeted Drive queries found mentions in synthesis documents but no actual Zenodo record/file payload. Status: **DOI RECORD INACCESSIBLE/UNVERIFIED**, not “absent,” deleted or invalid. No credentials or authenticated web session were accessed.
