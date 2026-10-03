# Literature frontier

Audit cutoff: 2026-10-03. We searched arXiv, the official formalization and its open pull request, GitHub issues, and the authors' public pages surfaced by these searches. No peer-reviewed journal version of the 2026 AF/Lamzouri/Wang results was identified by the cutoff. “Preprint” below means arXiv, not peer-reviewed publication.

## Target-specific record

| Evidence class | Source/date | Simple and on-line proportion | Assumptions and status | Checked by this project |
|---|---|---:|---|---|
| PEER_REVIEWED | No newer peer-reviewed paper identified by 2026-10-03 | No peer-reviewed value established here | Search result is not proof that no publication exists; cutoff and search scope recorded | No |
| PREPRINT | Alpöge–Furman, arXiv:2608.13637v2, 2026-08-13 / revised 2026-08-19, Theorem A and §5.4 | 2/3 baseline; exact MT value C0 = 3/2 − (1/√2)cot(1/√2) = 0.672500703679411645… | Unconditional proof stated; Lean companion advertised. This is the source theorem. | Formula independently evaluated here; analytic theorem not rebuilt |
| PREPRINT | Lamzouri, arXiv:2609.02882v2, 2026-09-02, Theorem 1 | Same >67.25% endpoint and ≥83.62% distinct zeros | New Hilbert-space inequality replaces the finite matrix framework; also gives ≥88.76% simple or on the line (union) and ≥83.62% average of simple/on-line proportions. No improvement in the target simple-and-on-line endpoint. | No proof replay |
| PREPRINT | Wang, arXiv:2609.24167v1, 2026-09-21, abstract and theorem | C0 + δ0, with δ0 = 6.66624…×10^-8; approx. 0.67250077034 | Refines Lamzouri's method. Still a tiny increment in the same first/second-moment style; no evidence found that it changes the bandwidth-one input class. | Not replayed |
| PREPRINT | Wang, arXiv:2609.07918, 2026-09-07 | No new global target coefficient stated | Short-interval simple critical zeros and distinct-zero bounds; different estimand from global proportion. | Not replayed |
| FORMALIZED_FINITE_IMPLICATION | Public open PR #17, branch head fba91d214655aaa1fd0504bb893c8859c20c79f9; A1290/10000 | Exact frozen coefficient 6728005676/10^10 = 0.6728005676 | The PR's exact rational Lean certificate gives a finite affine inequality; source branch audit reports successful Lean builds and standard-axiom audits. PR remains open. Our project did not rebuild Lean or run Comparator/NanoDa. | Source inspected; not independently Lean-replayed |
| NUMERICAL_CERTIFICATE / UNVERIFIED | Same PR branch AUDIT, A=1293/100000 | Feedback formula evaluates to approximately 0.672803938934799542 | Branch states an independent external replay of a 10,003,455-token tree, but says streams not committed. Treat as reported evidence until files are available and independently replayed. | No |
| FORMALIZED_FINITE_IMPLICATION with external hypothesis | AF §7.2 and PairCeiling source; N=256 law | p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000 = 0.68182868746… | Conditional theorem about every configuration-wise bandwidth-one certificate, with explicit stability error. It assumes EnclOK for externally produced form-factor enclosures. It is not an achieved unconditional lower bound. | Rational p0 evaluated here; EnclOK not checked |

## Status of the Montgomery–Taylor value

The paper's window-optimization statement is restricted to the one-window family, equivalently coefficients of the form 2−R(ψ), and cites CCLM17 Corollary 14 for optimality within that family. The exact AF constant is C0 above. The arXiv paper states the rounded value 0.67250. The source mathematics also gives distinct-zero coefficient C1=(C0+1)/2=0.836250351839705822….

This is a preprint-era source record, not a claim that the result has appeared in a peer-reviewed journal.

## Status of the wider bandwidth-one ceiling

The AF paper defines a broad certificate as a configuration function p that depends only on the first two trace moments of bandwidth-one test functions and the on-line/off-line partition, and obeys p≤N0^s/N configuration by configuration. Its §7.2 ceiling uses an explicit 256-periodic marked-configuration law and states p0≤0.6818287 plus a derivative-regularity error. For band-limited windows with r(±1)=0, the displayed edge term vanishes; the remaining error is 2.55×10^-6 times |r′(1)|+∫|r″|.

The numeric law enclosures are an external input EnclOK. The formal theorem checks downstream consequences conditional on EnclOK. The issue about reproducing that input notes that the source repository does not contain the exact rational law file or the interval-enclosure producer. Therefore the ceiling is not a fully self-contained numerical certificate in the current public repository snapshot, and is not a constructive density result.

## Constructive interval between MT and the ceiling?

Yes, public formalized-source candidate A1290 gives 0.6728005676, and the same public branch reports A1293/100000 giving about 0.67280394. Both lie above C0 and below the conditional ~0.68183 ceiling. A1290's Lean source and generated proof modules are present in the PR branch; A1293 streams are reported absent. We have not independently checked either chain. This means the initial goal “find c>C0” is stale as a novelty target. The immediate research gate is independent replay of the strongest available certificate chain, not a fresh search against 0.67250.

## Did later work alter the certificate class or inputs?

- Lamzouri changes proof architecture: a Hilbert-space inequality in place of the finite matrix compression; the target endpoint remains C0.
- Wang refines Lamzouri's method and reports a delta of about 6.7e-8. The public abstract does not establish a broader Fourier support or higher unconditional trace-moment input.
- The sextuple branch adds a constructive finite affine penalty on five nonnegative gap variables and an exact finite rational certificate. The source describes its analytic feedback to the zero-count ledger. It is a later constructive certificate candidate within the unconditional analysis, not a change to the AF paper's definition of the entire bandwidth-one class.
- No retrieved source establishes access to unconditional tr(G^k), k≥3, at bandwidth one. AF §7.2 explains that the prime-side diagonal method gives higher moments only in a shorter support regime; at X≈T it allows only k=1 beyond the second moment evaluation.

## Key sources

- AF paper and theorem statements: https://arxiv.org/abs/2608.13637
- Official HTML §7.2 and Appendix A: https://arxiv.org/html/2608.13637v2
- Lamzouri: https://arxiv.org/abs/2609.02882
- Wang: https://arxiv.org/abs/2609.24167
- Wang short intervals: https://arxiv.org/abs/2609.07918
- Lean source PR #17: https://github.com/anthropics/formal-math/pull/17
- EnclOK reproduction issue #14: https://github.com/anthropics/formal-math/issues/14
- Certificate-file request issue #8: https://github.com/anthropics/formal-math/issues/8
