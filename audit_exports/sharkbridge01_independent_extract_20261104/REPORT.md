# SHARKBRIDGE-01 — decision

Research owner: Prince. Private experiment, 2026-11-04. Recommendation: do not pursue this prototype as a cheaper A1294 verifier. Preserve the exact typed-table correspondence result, use conventional compression for archival transport, and require a new independent acceptance architecture before scaling.

| Required verdict | Decision |
|---|---|
| SHARKLANG_CERTIFICATE_CODEC | EXPERIMENTAL |
| SHARK_PROTOCOL_PROVENANCE | USEFUL, limited to deterministic canonical hash binding |
| LRSC_EXACT_COMPRESSION | NOT_USEFUL in this benchmark |
| LOSSLESS_ROUNDTRIP | PASS for the precisely defined checker-input stream and tested ordinary-compression streams |
| TWO_LEAF_KERNEL_EQUIVALENCE | PROVED for typed decoded tables; byte parsing remains external |
| SOURCE_SIZE_IMPROVEMENT | NOT_ESTABLISHED |
| OBJECT_SIZE_IMPROVEMENT | NOT_ESTABLISHED |
| PEAK_RAM_IMPROVEMENT | NOT_ESTABLISHED |
| FULL_TREE_FEASIBILITY | OPEN |

## Isolation and authentic input

Local branch codex/sharkbridge-01 in the separate worktree audit_exports/sharkbridge01_worktree, base eb36159ee7e57053fcae3de025fe4dac539435ab. Only the untracked SHARKBRIDGE01 experiment directory is written. Historical project sources, packets, releases, licenses and successful proof objects are untouched. No commit, push, merge, publication, production deployment, provider API, credential or private key is involved.

Frozen parent packet SHA-256: 643dfc7b60959608c1c6550457f21a487eeaaade5d9d410090f486693a3f2bd9. The contained source-free V2 ZIP is independently hash-checked as 3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5. The exact two-leaf ledger remains 9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072. No full-tree replay was run.

Technology provenance, release-version discrepancies and exact implementation boundaries are in TECHNOLOGY_AUDIT.md and technology_sources.json. The actual SharkLang strict JSON parser and Protocol canonical JSON/hash helper definitions are reused unchanged through an audited AST allowlist, avoiding all module CLI, networking and signer initialization. The released VM is not altered and does not implement the new dialect. Protocol source here is a v1.3.3-labelled workspace's 1.3.3.dev0 candidate, not a newly authenticated final release. LRSC source and finite certificate statements are kept distinct from numerical checks and draft supplements. Original notices remain; no new license is assigned to copied sources.

## Exact codec and formal result

FORMAT.md defines a bounded, versioned table encoding with canonical exact rationals, interned segments, checked catalog references, all five-coordinate boxes/anchors, fifteen models per leaf and the exact split. This benchmark has 126 unique rationals, 110 unique segment records, 100 catalog declarations, 400 segment occurrences and 30 model rows. The decoder verifies structural limits and exact midpoint boxes. Eleven targeted malformed-input tests pass in normal/-O/-OO Python. These are finite regression tests, not a universal security proof.

The canonical mathematical input stream is 24,247 bytes; interned wire payload is 7,456 bytes. Both decode and re-encode reconstruct that stream byte-for-byte. This does not mean the compact format reconstructs historical JSON whitespace, owner-provenance metadata or the complete V2 binary tree: those original bytes are retained and hash-bound separately. The canonical stream includes exact selected rational values and catalog identities; complete source model definitions remain pinned dependencies.

WireParent.lean contains actual typed rational/segment tables and a bounded Option decoder, not a compressed Lean file that expands back into source. Lean proves decoded_left and decoded_right for all fifteen rows; box/anchor reconstruction equalities; decoded_children; accepted_left/right; leaf_left/right; and the complete parent theorem. The final proposition is the same parent node 65 box and inequality A <= sextupleEnergy(g)+B*sextupleSpan(g), A=647/50000, B=1094977/5000000000. The parent box is [405/64,105/16] x [825/128,105/16] x [795/128,405/64] x [825/128,105/16] x [405/64,105/16], split at 825/128 in coordinate zero.

The final parent depends on the two transported compact acceptances and upstream midpoint coverage. All printed axioms are propext, Classical.choice and Quot.sound. Both fresh baseline and new bridge compile with exit 0. There is no sorry, admit, custom axiom, native_decide or runtime PASS premise in the mathematical acceptance.

Crucially, the bridge proves correspondence and transports the existing authentic acceptance proofs. It retains their entire source/object dependency closure. It is not a demonstrated smaller independent acceptance engine. rowOrDefault is used only after concrete theorems show every decode is some of the authentic row; its fallback is not a rejection-policy theorem. Python parsing, byte-to-typed-literal conversion, catalog-name/index authentication and cryptographic file binding remain external. Neither signatures nor hashes establish the mathematical inequality.

## Complete-parent costs

Pinned Lean 4.33.0-rc2, compiler d8b18978322de05a8f3dba51ef03cf5461676c17; upstream fba91d214655aaa1fd0504bb893c8859c20c79f9; Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. Compilation is serial, with per-process allocation cap -M 6800 and bounded timeouts. Original dependency objects are read through a link overlay that explicitly excludes every output being rebuilt. The initial missing-module-root setup failure is preserved, followed by the successful corrected setup. No mathematical source correction was needed.

| Metric | Complete baseline closure | Baseline plus typed bridge closure |
|---|---:|---:|
| Lean source bytes | 273228 | 289025 |
| Compiled object bytes | 20794984 | 23323144 |
| Measured serial compilation seconds | 257.14 | 324.46 |
| Peak RSS KiB | 5490748 | 5722316 |
| Major faults | 445789 | 531629 |
| Framed source stream, zlib-9 bytes | 26781 | 30178 |
| Framed object stream, zlib-9 bytes | 6487664 | 7166236 |

The experimental complete total is measured baseline plus measured bridge increment (67.32 seconds), not a separately randomized cold-cache run. Cache/paging effects are not controlled, so no statistical speed/RAM conclusion is claimed. Comparing the new module alone against the complete baseline would be invalid. Kernel-only replay time was not isolated: these are Lean elaboration-and-kernel-checking wall times. A trust-level-zero recheck of all imported Mathlib modules was not attempted. No lower total verification cost has been demonstrated.

Import-only compilation with the same compiler/cap took 101.05 seconds and peaked at 5500256 KiB, illustrating the dominant environment/import baseline. Peak values cannot be subtracted to obtain a reliable certificate-only allocation cost. Conversion source dependencies add 447536 bytes (codec, generator and the two full original helper source files); Python runtime/standard library are additional common tools. Proof data is present in both payload and generated typed literals, so they cannot be counted as one replacement for the old proof inputs.

The read-only Zeta23 dependency overlay inventories 1455 files, 639124805 bytes, excluding the three certificate outputs. Installed cache upper bounds are 6006957427 bytes for Mathlib's lib/lean and 659473397 bytes for the old project's lib/lean. These are upper bounds, not the exact minimal import closure; a complete minimal dependency census was not established, and no dependency savings is claimed. Toolchain/Mathlib caches are not bundled or called self-contained in this packet.

## Ordinary compression and LRSC falsification

Every zlib comparison checks byte equality after decompression. zstd is absent in both native Python and the checked WSL command/module environment; nothing was downloaded.

| Same mathematical content | Bytes after zlib-9 |
|---|---:|
| Ordinary canonical semantic JSON | 1782 |
| New interned payload | 1974 |

Although interning shrinks uncompressed data, ordinary compression already exploits the repetition more effectively here. For the row substream, ordinary exact row interning finds 14 unique rows among 30 occurrences: 295 zlib bytes. Exact reflection/template residuals reconstruct every integer index, but use 399 zlib bytes. Reject this LRSC-inspired grouping for this application. The numerical K11 projection is never used as mathematical input; rank-deficient projection cannot losslessly encode arbitrary data without full residuals. No LRSC novelty or theorem transfer is claimed.

## Provenance and next action

evidence.json binds frozen input/packet/V2 hashes, format version, compressed and decoded payload hashes, pinned compiler revisions, proof source/object/log hashes and explicit result scope. Its canonical SHA-256 uses the inspected Protocol helper. There is no signature, external timestamp or independent rollback anchor. An attacker replacing both files defeats a locally recomputable hash; the manifest is reproducibility evidence, not authenticated external history.

Keep the successful typed correspondence theorem as a small independent engineering result. Do not expand the tree or add a branded compression layer. Further A1294 work would need a reusable standalone checker that accepts the interned data without retaining both original acceptance modules; it must beat the conventional baseline including all proof, decoder and dependency costs before another integration benchmark is justified. Full A1294 and all frozen WP84 theorem conclusions remain unchanged.
