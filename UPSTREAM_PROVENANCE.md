# Upstream provenance

Accessed: 2026-10-03. No upstream file is vendored or modified in this repository.

| Source | Pinned version / commit | Role | Artifact class | License / status |
|---|---|---|---|---|
| Alpöge–Furman, “More than two thirds of the zeta zeros are simple and on the critical line” | arXiv:2608.13637v2; submitted 2026-08-13, revised 2026-08-19; https://arxiv.org/abs/2608.13637 | Primary theorem, proof, constants, and bandwidth-one certificate definition | Preprint; official arXiv HTML is the mathematical source | arXiv perpetual non-exclusive license; journal publication not identified in this audit |
| Anthropic zeta23 formalization, now under formal-math | https://github.com/anthropics/formal-math/tree/2bafb8c88f177284a2123b5fefa2ff84e2365eb6/zeta23 | Baseline Lean project and published formal statements | Machine-checked upstream source; not rebuilt here | Apache-2.0 |
| Formal-math current main snapshot | https://github.com/anthropics/formal-math/commit/fbdc36bbf17d20af3fd0447c6d1a8a02773c9844 | Confirms current repository layout and project availability | Current source snapshot, accessed 2026-10-03 | Apache-2.0 |
| Lean | `leanprover/lean4:v4.33.0-rc2` from upstream `zeta23/lean-toolchain` at commit 2bafb8c88f177284a2123b5fefa2ff84e2365eb6 | Reproduction toolchain | Exact version pin | Lean project toolchain license |
| Mathlib | `leanprover-community/mathlib4@51e6992efd06126df61a496bebf8f49482a4e129` from upstream lake-manifest at commit 2bafb8c88f177284a2123b5fefa2ff84e2365eb6 | Imported formal library | Exact commit pin | Apache-2.0 |
| Formal-math PR #17 | https://github.com/anthropics/formal-math/pull/17; base SHA 2bafb8c88f177284a2123b5fefa2ff84e2365eb6; head SHA fba91d214655aaa1fd0504bb893c8859c20c79f9 | Public sextuple certificate candidate; A1290 source and A1293 audit report | Open PR; A1290 source-contained in branch; A1293 replay streams absent per branch audit | Fork source license Apache-2.0; no upstream merge as of access |
| Biao Wang, “Proportions of the non-trivial zeros of the Riemann zeta function” | arXiv:2609.24167v1, submitted 2026-09-21; https://arxiv.org/abs/2609.24167 | Later tiny improvement to Montgomery–Taylor coefficient | Preprint | arXiv version only |
| Youness Lamzouri, “A new proof that more than 2/3…” | arXiv:2609.02882v2; https://arxiv.org/abs/2609.02882 | Hilbert-space proof of the same baseline endpoint plus other proportions | Preprint | arXiv version only |
| Biao Wang, “Simple critical zeros and distinct zeros … in short intervals” | arXiv:2609.07918; https://arxiv.org/abs/2609.07918 | Short-interval bounds; does not replace global proportion record in this project | Preprint | arXiv version only |

## Specific branch evidence

At PR #17 head `fba91d214655aaa1fd0504bb893c8859c20c79f9`:
- `zeta23/Zeta23/ThmD/Sextuple/A1290/Unconditional.lean`: blob `a7f873340ab63e325e396478edac1edbebc8111a`.
- `zeta23/Zeta23/ThmD/Sextuple/A1290/LineDecimal.lean`: blob `c8cdcbbee41fa769260205e866255353a7531f01`.
- `zeta23/Zeta23/ThmD/Sextuple/A1290/Certificate.lean`: blob `f59342c5050cf2172025c8082d15fb055b5df410`.
- `zeta23/Zeta23/ThmD/Sextuple/Feedback.lean`: blob `31c8fc2f4bbc3ce0526ef225c4ed7d7be317c23b`.
- `zeta23/README.md`: blob `abb70fecff7dd27b49601397cb2cc0095ac4c582`.
- `zeta23/AUDIT.md`: blob `b8252393d5933dddea02f695b2935bc373811360`.

The branch audit reports A1290 as a Lean-kernel-checked exact rational certificate with coefficient 0.6728005676. The same audit reports A=1293/100000 as externally replayed, with its streams not committed. The project has not independently checked those reports.

## Access and role

The paper is the source of the theorem and analytical definitions. The formal-math commit provides the exact Lean/mathlib baseline. PR #17 is tracked only as a later public candidate, not used as source code in our replay. The replay script below computes the constants from mathematical formulas and a cited exact rational law value, not from hidden data or copied code.
