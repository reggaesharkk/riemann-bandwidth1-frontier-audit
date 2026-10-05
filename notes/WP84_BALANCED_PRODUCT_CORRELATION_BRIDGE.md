# WP84 — balanced product-correlation bridge for the bounded resolvent route

Date: 2026-10-05

Status: **EXACT 2-vs-2 KERNEL REDUCTION CLOSED; PUBLISHED AVERAGE E2-CORRELATION INPUT IDENTIFIED FOR THE LONG-SHIFT RANGE; WEIGHTED ADAPTATION / SHORT-SHIFT PATCH OPEN**

This note combines three previously separate pieces:

1. the exact finite-compression Dirichlet trace kernel;
2. the old WP70 observation that fourth-order off-diagonals are weighted
   correlations of `Lambda*Lambda`;
3. a published unconditional average-correlation theorem for almost primes.

The result is a much narrower arithmetic interface for the first balanced
near-resonance sector of WP84.

## 1. Exact product collapse

Let `u_n` denote any scalar coefficient attached to a retained prime-power
shift.  In a balanced two-positive/two-negative sector define the product
convolution

    c(m) = sum_{ab=m} u_a u_b.

Then on the Gabor/Fourier grid

    tau_k = T + 2*pi*k/L

we have exactly

    sum_{a,b} u_a u_b exp(i tau_k log(ab))
      = sum_m c(m) exp(i tau_k log m).

Therefore the balanced quadratic form collapses from four prime-power
indices to two product indices:

    (1/d) sum_k |sum_m c(m) exp(i tau_k log m)|^2

      = sum_{m,n}
          c(m) conjugate(c(n))
          exp(i T log(m/n))
          D_d(log(m/n)/L),

where

    D_d(s)=(1/d) sum_{k=0}^{d-1} exp(i 2*pi*k s).

This is an exact identity at finite d.

The overlap/spread factors do not destroy the reduction: after the usual
cell decomposition they become bounded piecewise-polynomial weights in the
factor variables, so each cell gives the same product-kernel identity with a
weighted convolution coefficient.

## 2. Multiplicative near resonance becomes an additive shift

Restrict m,n to one dyadic product block

    M < m,n <= 2M.

Write

    h=n-m.

If

    |log(n/m)| <= C/T,

then

    |h| <= C' M/T

for an absolute C' depending only on C.

Conversely, for |h|<=M/2,

    |log(1+h/m)| <= 2|h|/M.

Thus the finite-compression window is, scale by scale, exactly an additive
shift window of length

    boxed:
    H_M ~ M/T.

The balanced off-diagonal is therefore a smooth weighted average of

    boxed:
    sum_m c(m) c(m+h).

For prime support,

    c(m)

is the two-almost-prime / generalized-Mangoldt convolution.  For distinct
primes p q,

    (Lambda*Lambda)(pq)
      = 2 log p log q.

So the hard 2-vs-2 sector is not an unspecified four-prime theorem.  It is a
long-shift correlation problem for weighted E2 numbers.

## 3. Exact connection to the old WP70 dispersion lead

The earlier WP70 reduction had already isolated

    sum_m (Lambda*Lambda)(m)(Lambda*Lambda)(m+h),

with shift range

    H = X^2/T

when the prime cutoff is X.

The present derivation identifies the same object directly from the bounded
resolvent / displacement route.

At bandwidth X=T^lambda,

    product scale M ~ X^2,
    H_M ~ X^2/T = T^(2 lambda-1).

Thus the WP70 dispersion object and the WP84 first balanced-resonance object
are the same arithmetic family, reached from two independent derivations.

This is a strong consistency check.

## 4. Existing unconditional theorem in the long-shift range

Natalie Evans, *Correlations of almost primes* (Math. Proc. Cambridge Philos.
Soc. 174 (2023), 301-344), proves an average Hardy--Littlewood asymptotic for
products of two primes.

The theorem is especially close to our coefficient because the proof first
uses the weighted function

    varpi_2(n)=log p_2

for n=p_1 p_2 with one factor p_1 in a prescribed multiplicative slice.

For

    log^(19+eps) M <= H <= M log^(-A) M,

Theorem 3.2 gives, for almost all |h|<=H,

    sum_{M<n<=2M} varpi_2(n)varpi_2(n+h)

      = singular_series(h) * main_term
        + O(M/log^eta M).

More useful for us than the pointwise-exception formulation is the L2
estimate proved immediately before the theorem: the squared correlation
error summed over |h|<=H is

    O(H M^2 / log^eta M).

That is exactly the norm needed for a bounded smooth h-kernel: Cauchy--Schwarz
turns the L2 average into an aggregate error without requiring a theorem for
every fixed h.

## 5. Why the Evans weight is structurally compatible with Lambda*Lambda

On a factor slice

    P < p_1 <= P^(1+delta)

and a product block M<n<=2M,

our distinct-prime coefficient is

    2 log p_1 log p_2 / sqrt(n).

Inside a sufficiently fine multiplicative partition:

- 1/sqrt(n) is a smooth product-scale weight;
- log p_1 is a slowly varying factor-slice weight;
- log p_2 is exactly the Evans varpi_2 weight.

Therefore a theorem-grade adaptation should proceed by:

1. dyadic/smooth partition in product scale n;
2. multiplicative partition of one prime factor;
3. partial summation to insert 1/sqrt(n) and log p_1;
4. use the L2-in-h Evans estimate before summing the bounded Dirichlet kernel;
5. sum the factor slices;
6. handle diagonal p=q and proper-prime-power pieces separately.

This is substantially narrower than proving a new pointwise
Hardy--Littlewood conjecture for Lambda*Lambda.

## 6. Long-shift cells potentially become source-closed

On product scale M the theorem applies once

    H_M=M/T >= log^(19+eps) M.

Equivalently,

    M >= T log^(19+eps) M.

For those cells, the first balanced near-resonance obstruction has a
published unconditional average-correlation mechanism whose norm matches the
statistic we actually consume.

The remaining analytic work is an adaptation/provenance proof, not the
invention of a new correlation conjecture.

## 7. The short-shift patch is now explicit

The unresolved product scales satisfy

    M/T < log^(19+eps) M.

These are precisely the cells too short for the cited E2 theorem.

We should not guess that their contribution is negligible.

Instead the companion exact computation

    src/wp84_phi4_product_scale_split.py

splits the known connected calibration

    Phi4=-1/60

at the normalized product-scale wall

    s=log M/L=1.

That calculation tells us how much of the connected model correction is
carried by the long-product side versus the classical-length side.

If the long side carries the entire connected correction, the Evans route is
a direct candidate closure.  If not, the residual short side becomes a
separate, numerically quantified theorem target.

## 8. Proposition-R firewall

This bridge is being used only inside a bounded fixed-pole resolvent
functional.

We are **not** asserting a finite-T fourth raw trace-moment bound.

That distinction is essential: Proposition R blocks the old unconditional
raw higher-even-moment route, while bounded resolvent statistics are stable
under o(d)-rank power-law outliers.

## 9. New kill gate

The next theorem-grade statement is now concrete:

> Prove the Evans/dispersion L2 correlation estimate with the exact
> Lambda*Lambda, taper-cell and finite-population weights appearing in the
> bounded D1/D2 generator, then insert it into the six-pole F_delta
> functional.

At order four the target must still reproduce

    pair layer = 4/15,
    connected core = -1/60.

No unconditional >79% theorem is claimed yet.


## 10. Evidence boundary: this is not yet the full fixed-pole theorem

The Evans/dispersion interface controls the first balanced degree-four
near-product-collision calibration sector.

It must **not** be promoted to a proof of the full four-pole or six-pole
resolvent comparison merely because the order-four model gate closes.

A fixed nonreal resolvent contains translation words of all degrees through
the evolving intermediate state.  The active theorem still needs one of:

1. a direct bounded-resolvent estimate that sums those higher-degree sectors;
2. a closed finite generator law for the rank-four displacement statistics;
3. a truncation/approximation theorem with an error budget uniform enough to
   reduce the full bounded consumer to finitely many calibrated sectors.

Accordingly, the published almost-prime correlation theorem is a real
source-closed input for one previously unnamed arithmetic obstruction, but it
is **not** by itself the WP84 kill shot.

The new four-pole delta=6 rung in

    notes/WP84_FOUR_POLE_RECORD_BEATING_RUNG.md

is the preferred place to test whether the remaining bounded generator can
be closed with enough margin before escalating to the six-pole 79.627% rung.
