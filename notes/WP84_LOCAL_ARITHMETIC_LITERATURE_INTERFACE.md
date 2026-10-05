# WP84 — modern short-interval correlation literature interface for the finite-local fallback

Date: 2026-10-05

Status: **LITERATURE ROUTING NOTE; IDENTIFIES SOURCE-CLOSED SUPERCRITICAL RANGES BUT DOES NOT CLAIM THE EXACT WP84 WEIGHTS ARE ALREADY COVERED**

No unconditional zero-density percentage is claimed here.

The new r2 reductions make a finite-degree / finite-local arithmetic fallback
legitimate after fixed displacement and rank quarantine.

Before inventing a new correlation theorem, the relevant 2022--2026
short-interval literature should be used at the exact point where its
hypotheses match.

This note records the useful interfaces and the remaining mismatches.

## 1. Product scale and additive shift scale

A balanced multiplicative word with positive product scale

    M

enters the finite-compression window through

    |n-m|
      = |h|
      ~ M/T.

Write

    M=T^s,
    s>1.

Then

    H:=M/T
      = T^(s-1)
      = M^theta,

with

    boxed:
    theta=(s-1)/s.

Thus every fixed supercritical product exponent s>1 corresponds to a
positive-power additive shift range.

As s->1+, theta->0.

## 2. Evans: E2 / semiprime correlation

Natalie Evans, "Correlations of almost primes"
(Math. Proc. Cambridge Philos. Soc. 174 (2023), 301--344),
proves an averaged Hardy--Littlewood asymptotic for products of two primes in
shift ranges beginning at a polylogarithmic scale, under a factor-size
restriction.

This is the closest published input to the first balanced 2-vs-2 WP84
coefficient.

For every fixed s>1,

    H=M^theta

eventually dominates every fixed power of log M.

Therefore fixed supercritical semiprime cells are in the long-shift regime
of that theorem after the already-identified factor-slice / smooth-weight
adaptation.

The shrinking s=1+o(1) transition layer remains separate.

## 3. 2026 higher-uniformity theorem

Matomaki--Radziwill--Shao--Tao--Teravainen,
"Higher uniformity of arithmetic functions in short intervals II.
Almost all intervals", Invent. Math. 244 (2026), studies Lambda, mu and
d_k in almost all short intervals.

Two ranges are especially relevant.

### Lambda

Their Hardy--Littlewood theorem with one averaging variable treats fixed
prime correlations for

    H >= X^(1/3+epsilon).

Under the WP84 product/shift conversion this corresponds to

    theta>1/3,

hence

    boxed:
    s>3/2

for a direct identification of X with the product scale M.

So sufficiently deep supercritical prime-tuple cells have a modern
source-closed average-correlation mechanism.

### Divisor functions

Their divisor-correlation theorem with one averaging variable works for

    H >= X^epsilon

for every fixed epsilon>0.

Thus at the level of divisor functions, **every fixed s>1** lies in the
published positive-power shift regime.

This is potentially valuable for fixed-degree WP84 product coefficients,
which are divisor-bounded / convolutional after suitable identities.

## 4. Important mismatch: WP84 coefficients are not automatically d_k

A degree-2m balanced WP84 word produces weighted almost-prime coefficients
built from prime / von-Mangoldt factors, roughly of the form

    Lambda^{*m}

with square-root and smooth factor weights.

These are not literally the divisor function d_m.

Therefore Theorem 1.6 of the 2026 paper may not simply be cited as the final
WP84 correlation theorem.

A theorem-grade transfer would need one of:

1. an exact convolution identity reducing the needed weighted coefficient to
   a finite combination of d_k-type correlations and smooth derivatives;

2. a Heath--Brown decomposition whose resulting type-I/type-II pieces fit
   the published higher-uniformity estimates;

3. a dedicated almost-prime correlation result such as Evans in the m=2
   sector.

This note does not claim that step is already done.

## 5. Why the literature still changes the fallback calculation

After the r2 finite-local reduction, any fixed polynomial degree n creates
only finitely many balanced product sectors.

They can be stratified by product exponent s.

The literature now suggests the following proof architecture:

    exact diagonal / subcritical sector:
      unique factorization + k lambda < 2 gate;

    fixed supercritical E2 sector:
      Evans;

    deeper fixed supercritical prime-tuple sectors:
      2026 higher-uniformity / Hardy--Littlewood machinery;

    divisor-bounded convolution sectors:
      2026 d_k one-average theorem after an explicit coefficient bridge;

    shrinking s=1+o(1) layers:
      separate transition estimate using the already-derived
      connected-kernel turn-on and bounded consumer margin.

This is far narrower than proving arbitrary fixed-shift Hardy--Littlewood
conjectures from scratch.

## 6. Practical conclusion

Do not launch a giant finite-degree calculation yet.

First determine the smallest approximation degree actually required by the
conditioned r2 consumer.

Then classify each resulting arithmetic word into the source-closed ranges
above.

Only the sectors that survive this literature matching should become new
theorem targets.

Public sources:

- Natalie Evans, "Correlations of almost primes", MPCPS 174 (2023).
- K. Matomaki, M. Radziwill, X. Shao, T. Tao, J. Teravainen,
  "Higher uniformity of arithmetic functions in short intervals II.
  Almost all intervals", Invent. Math. 244 (2026).

See:

    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
    notes/WP84_R2_BETA_RANK_QUARANTINE.md
    notes/WP84_R2_SCALE_CONDITIONING.md
