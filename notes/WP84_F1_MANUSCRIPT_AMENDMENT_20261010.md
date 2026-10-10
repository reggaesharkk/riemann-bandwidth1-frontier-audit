# WP84 manuscript amendment plan — 2026-10-10

The earlier referee-facing PDF and LaTeX manuscript were generated outside this repository and are not tracked here. This note supplies replacement wording for a future authorized manuscript edit; it does not claim that either external manuscript was changed.

## Proposed theorem: adaptive finite-section boundary correction

> **Theorem (existential adaptive boundary correction).** Let the source prime-power field, natural cutoff, normalization, and contiguous starting interval satisfy the hypotheses in `WP84_ADAPTIVE_BOUNDARY_LOCAL_LARGE_SIEVE.md`. Then for each sufficiently large (T) there is a contiguous trimmed interval (I_T\) obtained by deleting at most (2M=o(d)) endpoint rows, with (E(I_T)=\|P_{I_T}V(I-P_{I_T})\|_{HS}^2=O(\log d)). On this selected interval, the complete normalized finite-section compression-versus-compressed-cube correction satisfies
> \[
> d'^{-1}\left|\operatorname{Tr}(P_{I_T}H^3P_{I_T})-\operatorname{Tr}((P_{I_T}HP_{I_T})^3)\right|=o(1).
> \]
> The assertion is existential in the trimmed interval; it is not uniform over all admissible sections.

## Proposed theorem/remark: direct first-strike one-prime endpoint selection

> **Theorem (one-prime endpoint score on the adaptive pair window).** Fix (R). Under the source normalization and natural prime-power cutoff in `WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md`, define (Q,\alpha,\beta) from all (p^v\le N) with coefficients (-\Lambda(p^v)/(a_\phi L\sqrt{p^v})), and set (S_R(k)=\sum_{|t|\le12R}(|\alpha_{k+t}|^2+|\beta_{k+t}|^2)). On each of the two endpoint windows used by Decision B, the equal-weight mean of (S_R) is (O_R(1)). Consequently each endpoint window contains a score-good set of density at least (1/2). Their Cartesian product has pair density at least (1/4) under Decision B's same uniform pair weights. Restricting Decision B's nonnegative boundary-energy average to this product yields a common interval with (E(I)=O(\log d)). On that interval, the local row bound (K_R=O_R(1)) gives the fixed-(R), (b=5,6) weighted reprojection payment (4bRK_R^b/d'=o(1)).

> **Remark (scope).** This is a source-specific result for the direct one-prime first-strike endpoint consumer. The bounded score follows from the one-prime prime-power field, its (O(1)) coefficient square mass, frequency separation (\delta\ge1/((N+1)L)), and (N/U_T\to0) on Decision B's window. It does not identify the score with a two-prime (pq) detuning feature, and does not establish a bounded mean for that separate product-frequency feature.

## Proposed conditional statement: fourth-order product-feature endpoint

> **Conditional endpoint lemma (fourth-order product features).** Suppose an exact source-generated fixed-(R) endpoint feature map is provided, including all product frequencies, prime-power terms, path/root weights, gates, carrier phases, and its consumer identity. Suppose also that its lower- and upper-endpoint score means are (O_R(1)) on the specified equally weighted pair window. Then Markov gives endpoint-good sets of positive density; if the consumer conditions separate by endpoint, their Cartesian product has positive pair density. Any nonnegative crossing-energy mean bound on the same weighted pair window restricts to that set with the reciprocal weighted-density loss. Under these hypotheses, the corresponding common-section selection follows.

> The source hypotheses in this conditional statement have not been established for the Decision D pair-frequency feature. Its possible support reaches (pq\le N^2) (and the documented broad pair pool permits (X^2)); the one-prime (N)-length estimate cannot be substituted without a source theorem. F1B's two-factor payment is generic and remains conditional on its explicit support, maximal-estimate, coefficient, and consumer-matching assumptions.

> Under the narrower F1B hypotheses (D\le N^2), bounded collapsed coefficient mass, and prefix/interval maximal truncation, its separate rank-two normalized payment is (O_R(L^3/X+L^3e^{-3\sqrt L/2})=o(1)), even though the generic product-score majorant itself grows. This alternative pays only that normalized endpoint term; it does not supply Decision D's asserted (O_R(1)) score premise or prove the source gates, feature generator, or consumer identity. It is inapplicable to the broader (X^2) pool without a new estimate.

## Required limiting-scope sentence

> Neither the adaptive boundary theorem nor the first-strike endpoint/reprojection theorem transfers the raw cubic trace from the original full interval to the trimmed interval. Raw cubic deletion requires a separate source-specific uniform-integrability or deleted-block estimate. The signed fifth/sixth arithmetic gate, same-section moment identification, prime-to-Weil transfer, and zero-side block/tail transfer are also open. Therefore strict (>79\%\) remains unproved.

## Editorial provenance

The first theorem is Decision B's adaptive boundary result. The one-prime endpoint theorem is F1C, supported by the fixed-band weighted reprojection note. The fourth-order product-feature statement is only conditional, reflecting Decision D's corrected scope, F1's frequency-support audit, and F1B's generic conditional payment. No earlier referee PDF or LaTeX source is present as a tracked repository file, so this amendment is proposed text only.
