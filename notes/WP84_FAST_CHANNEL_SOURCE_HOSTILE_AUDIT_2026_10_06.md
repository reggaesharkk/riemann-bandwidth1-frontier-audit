# WP84 — hostile source check for the carrier-2T prime sum (2026-10-06)

Status: **CITED POINTWISE INPUT VERIFIED AND PARAMETER FIT CHECKED; STATE-FLOW THEOREM REMAINS OPEN**

This note records an independent check of the external estimate used in
`notes/WP84_D2_FAST_CHANNEL_VK_CLOSURE.md`. It closes a source/normalization
question only; it does not prove the active six-pole inequality.

## 1. Source verified

Sarvagya Jain, “Existence of Smooth Numbers in Short Intervals,”
*Quarterly Journal of Mathematics* 77 (2026), no. 2, 397–422,
Lemma 2.6, DOI: https://doi.org/10.1093/qmath/haag010.

The published lemma states, for a dyadic prime block (p\sim P), parameter
(X\ge 1), (P\ge \exp((\log X)^{2/3}(\log\log X)^{4/3})), and
(|t|\le X),
[
\left|\sum_{p\sim P}p^{-1-it}\right|
\ll P^{-\sigma_0}+\frac{(\log X)^3}{1+|t|},
\qquad
\sigma_0=\frac{A_{VK}}{(\log X)^{2/3}(\log\log X)^{1/3}},
]
for a fixed positive (A_{VK}). The same bound for negative (t) follows
by complex conjugation.

## 2. Parameter match in the WP84 fast channel

Set (L=\log T), (X_0\asymp 5T), and discard primes below
[
P_0=\exp\bigl(KL^{2/3}(\log L)^{4/3}\bigr).
]
For fixed (K>1) and sufficiently large (T), every remaining dyadic
block satisfies the lemma's lower cutoff. Moreover,
[
\sigma_0\log P_0=(A_{VK}K+o(1))\log L.
]
Choosing fixed (K) with (A_{VK}K>10) gives
(P^{-\sigma_0}\ll L^{-10}) on every retained block.

The fast covariance frequencies obey (2T\le |t|\le 5T\le X_0), so the
lemma applies uniformly and its second term is (O(L^3/T)). There are
(O(L)) dyadic blocks. After the fixed polynomial weights in
(s=\log p/L) are restored by partial summation, the retained fast
covariance is (o(1)); the crude total of the pointwise main terms is
(O(L^{-9}+L^4/T)). The omitted small-prime square mass is
[
L^{-2}\sum_{p\le P_0}\frac{(\log p)^2}{p}
=O\bigl(L^{-2/3}(\log L)^{8/3}\bigr)=o(1).
]

These checks match the hypotheses and scales stated in the fast-channel
note. They support only the same-sign/carrier-(2T) current-prime
covariance estimate; they do not control the resonant channel or the
Bernoulli-state average.

## 3. Evidence boundary

The article and the quoted lemma are verified against the publisher's
published text. The estimate is an external analytic-number-theory input
used for a prime Dirichlet polynomial; it is not a Riemann-zero theorem.

The live open input remains the one-sided six-pole bound for the integrated
actual Bernoulli resolvent state described in
`notes/WP84_CURRENT_MISSING_INPUT_AUDIT_2026_10_06.md`. No unconditional
zero-proportion claim follows from this source check.
