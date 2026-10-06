# WP84 — normalization audit for the q=1 E2 principal-arc bridge

Date: 2026-10-06

Status: **FAIL-CLOSED SOURCE AUDIT — THE PUBLISHED GLOBAL POSITIVE L2 MAJOR-ARC REMAINDER BOUND DOES NOT BY ITSELF CLOSE THE WP84 NORMALIZATION; THE DANGEROUS TERM IS AN OFF-DIAGONAL SHIFTED-PRIME CONTRIBUTION**

No unconditional zero-density percentage is claimed here.

The balanced degree-four reduction, the short-cell multiplicative-to-additive
linearization, the oversampling lemma, and the transition-layer mass bound
are already closed.

The main long-shift window lies inside the q=1 principal major arc.

This note checks whether the published E2 major-arc remainder estimate can
be inserted as a black-box positive L2 bound in the exact WP84
normalization.

It cannot.

## 1. WP84 factor-slice scale

For an ordinary prime p, the sharp positive coefficient has the form

    u_p
      =
      - log p/
        (a_phi L sqrt p),

where a_phi is the taper-mass normalization.

In the balanced product coefficient

    c(m)
      =
      sum_{ab=m}
        u_a u_b,

restrict one prime factor to a multiplicative slice

    P<p_1<=P^(1+delta)

and one short product cell

    m~M.

For distinct primes m=p_1 p_2, the sliced coefficient has the form

    boxed:

    c_I(m)
      =
      w_I(m)
      varpi_2(m),

where

    varpi_2(m)=log p_2

is the E2 weight used in the source theorem and, uniformly on a sufficiently
fine slice/cell,

    boxed:

    |w_I(m)|
      comparable to
      log P/
      (a_phi^2 L^2 sqrt M).

The possible orientation factor is absolute and irrelevant to the
normalization test.

Smooth variation of log p_1 and m^(-1/2) can be handled by partial
summation after this scale check.

## 2. Oversampling factor

The deterministic sampling theorem gives, on a local frequency window J of
length comparable to 1/H,

    (1/d)
    sum_{alpha_k in J}
      |F_I(alpha_k)|^2

      <=
      C H
      int_{J^+}
        |F_I(alpha)|^2 d alpha

      +o(1),

where

    H=M/T.

Thus any positive L2 estimate imported from the E2 source is multiplied by
H in the WP84 discrete normalization.

## 3. What the published global major-arc bound gives

Let b(alpha) denote the centered E2 major-arc remainder.

The source proves a global major-arc estimate of the form

    B^2(M)
      =
      int_major
        |b(alpha)|^2 d alpha

      <<
      M/log^eta M

for some fixed eta>0.

Since J lies inside the q=1 principal arc,

    int_J |b(alpha)|^2 d alpha
      <=
      B^2(M).

After inserting the WP84 factor weight,

    |F_{I,centered}|^2
      has scale

      (log P)^2/
      (a_phi^4 L^4 M)

      times
      |b|^2.

Therefore the direct positive black-box insertion gives only

    boxed:

    WP84 centered cell
      <<
      H
      (log P)^2/
      [
        a_phi^4
        L^4
        log^eta M
      ].

## 4. This is not o(1) on fixed supercritical cells

For a fixed supercritical product exponent

    M=T^s,
    s>1,

we have

    H=M/T
      =
      T^(s-1).

Meanwhile L is logarithmic in T and the E2 factor parameter P is at most
subexponential on the logarithmic scale used by the source theorem.

Hence every fixed power of log M is dominated by H.

In particular

    H
    (log P)^2/
    [
      L^4
      log^eta M
    ]

does not tend to zero merely from the published fixed-log-saving estimate.

Thus:

    boxed:

    the global positive major-arc L2 estimate is not a theorem-grade WP84
    closure by itself.

This is a statement about the strength of the available bound, not a claim
that the actual centered WP84 contribution is large.

## 5. Exact local strength that would suffice

The positive oversampling route would close one factor slice if one could
prove

    boxed:

    int_J
      |b_I(alpha)|^2 d alpha

      =
      o(
        a_phi^4
        L^4
        M
        /
        [
          H
          (log P)^2
        ]
      )

uniformly over the consumed long-shift cells and slices.

Relative to the published global scale M/log^eta M, this requires an
additional effective H^(-1) gain up to logarithmic factors.

There are only two credible ways to obtain that gain:

1. prove a genuinely local principal-arc remainder estimate at the required
   scale;

2. do not take an absolute positive L2 bound before assembling the signed
   connected WP84 combination.

## 6. Source of the dangerous +1 term

The source's Dirichlet-polynomial estimate has the schematic factor

    boxed:

    q P T_src log M/M
      +
      1.

The origin of the two terms can be read directly from the mean-value
decomposition.

The mean-value lemma separates:

    diagonal coefficient square mass

and

    shifted off-diagonal correlations
      n -> n+h,
      h<=M/T_src.

In the proof of the E2 estimate:

- the diagonal prime-count term produces the term proportional to

      q P T_src log M/M;

- the shifted-prime correlation term produces the dimensionless

      +1.

Therefore the dangerous +1 is **not** simply the diagonal pair mass.

It is generated by a short shifted-prime off-diagonal estimate.

Consequently it may not be removed by declaring that the WP84 pair layer has
already been subtracted.

Any such cancellation must be proved at the exact connected-kernel level.

## 7. Consequence for the pair-layer strategy

The exact R=400 pair sector remains

    Pair_400
      <
      0.266329,

and the total positive non-pair allowance remains

    >0.0247937.

But the E2 source audit now shows that the next arithmetic theorem cannot be

    "apply B^2(M)<<M/log^eta M and sum cells."

That loses H.

The correct theorem target is narrower:

    boxed:

    prove a pair-subtracted / connected q=1 principal-arc estimate before
    discarding the signs of the connected order-four combination.

Equivalently, isolate the exact WP84 counterpart of the shifted-prime
off-diagonal +1 term and show that its connected contribution is either

    o(1)

or is already contained in the certified pair/closed-cycle ledger.

## 8. Updated arithmetic frontier

Closed:

- balanced product collapse;
- H=M/T shift geometry;
- short-cell phase linearization;
- discrete-to-local oversampling;
- shrinking transition-layer mass;
- q=1 principal-major-arc location;
- exact R=400 pair layer;
- pointwise nonpositivity of the exact closed connected kernel.

Now ruled out:

- black-box use of the global positive E2 major-arc L2 bound as the final
  WP84 estimate.

Open:

- a signed connected principal-arc estimate at the exact WP84
  normalization;
- or a stronger local centered-remainder theorem with the required
  effective H^(-1) gain.

No unconditional record theorem is claimed.

Source interface:

Natalie Evans, "Correlations of almost primes",
Math. Proc. Cambridge Philos. Soc. 174 (2023), especially Sections 6 and 8.

See:

    notes/WP84_E2_PRINCIPAL_ARC_GEOMETRY.md
    notes/WP84_E2_OVERSAMPLING_TRANSFER.md
    notes/WP84_E2_TRANSITION_LAYER_MASS.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
