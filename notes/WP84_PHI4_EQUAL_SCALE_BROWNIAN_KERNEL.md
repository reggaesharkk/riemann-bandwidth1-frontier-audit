# WP84 — equal-product-scale connected kernel is a Brownian covariance kernel with negative sign

Date: 2026-10-06

Status: **EXACT CLOSED-SCALE KERNEL IDENTITY; THE SYMMETRIZED BALANCED CONNECTED AMPLITUDE IS NEGATIVE SEMIDEFINITE ON EVERY FIXED PRODUCT SCALE**

No unconditional zero-density percentage is claimed here.

The balanced fourth-order sector may be parameterized by two positive
factor pairs

    (x, s-x),
    (y, s-y),

with

    1 <= s <= 2,
    s-1 <= x,y <= 1.

The common product scale is s.  Thus the corresponding balanced four-step
word is exactly closed at the product level.

Let C_s(x,y) denote the full connected overlap amplitude, averaged over the
eight alternating sign orderings of the two positive and two negative
factors.

Define

    d_s(u)
      =
      min(
        u-s+1,
        1-u
      ).

On the stated domain, d_s(u)>=0.

The exact identity is

    boxed:

    C_s(x,y)
      =
      -(s-1)
      min(
        d_s(x),
        d_s(y)
      ).

This is substantially stronger than pointwise nonpositivity.

## 1. Fundamental chamber reduction

The eight-order average is invariant under:

    x -> s-x,
    y -> s-y,
    x <-> y.

Therefore it is enough to work on

    s-1 <= x <= y <= s/2.

On this chamber,

    d_s(x)=x-s+1,

and

    d_s(x)<=d_s(y).

Hence the target identity reduces to

    C_s(x,y)
      =
      -(s-1)(x-s+1).

For each of the eight alternating orderings, direct collection of the
26 ordered-partition connected overlap terms gives exactly

    (s-1)(s-1-x),

which is the same expression.

No limiting argument is used.

## 2. Negative-semidefinite representation

Use the elementary identity

    min(a,b)
      =
      int_0^infinity
        1_{r<a}
        1_{r<b}
      dr

for a,b>=0.

Therefore

    -C_s(x,y)

      =
      (s-1)
      int_0^infinity
        1_{r<d_s(x)}
        1_{r<d_s(y)}
      dr.

For every finitely supported real or complex coefficient family z_j,

    sum_{j,k}
      conjugate(z_j)
      [-C_s(x_j,x_k)]
      z_k

      =
      (s-1)
      int_0^infinity
        |
          sum_j
            z_j
            1_{r<d_s(x_j)}
        |^2
      dr

      >=0.

Thus

    boxed:

    C_s
      is negative semidefinite

on every fixed product scale s.

The kernel -C_s is exactly a Brownian covariance kernel after the depth map

    x -> d_s(x).

## 3. Principal q=1 diagonal consequence

At equal product scale,

    log(ab/cd)=0,

so the finite-compression trace scalar is

    K_T(0)=1.

Hence the q=1 diagonal/principal contribution of the balanced connected
sector is not merely pointwise nonpositive: its complete quadratic form in
the factor-split variable is nonpositive.

No absolute-value estimate or almost-prime correlation theorem is required
for this exact equal-scale piece.

This closes the sign question for the diagonal product-scale principal
kernel.

## 4. Relation to near resonance

For finite compression the remaining arithmetic terms have nearby but
unequal product scales

    s_+ - s_-
      =
      log(ab/cd)/L.

The equal-scale theorem supplies the canonical reference operator for a
perturbative treatment of those terms.

The remaining task is therefore not to bound an arbitrary connected
four-prime kernel.  It is to control the departure from the negative
Brownian kernel under the small scale detuning

    |s_+-s_-|
      =
      O(1/(T L))

in the genuinely near-resonant region, together with the outer Dirichlet
lobes already isolated by the shift-range analysis.

This is the exact analogue of a boundary/commutator perturbation problem:
the zero-detuning operator has a one-sided sign, and only the detuning
variation can create positive leakage.

## 5. Evidence boundary

Closed:

- exact fixed-scale formula for the eight-order balanced connected kernel;
- exact negative-semidefinite Gram representation;
- q=1 equal-product-scale principal quadratic form is nonpositive.

Open:

- a uniform perturbation bound for unequal product scales strong enough to
  preserve the R=400 positive-error budget;
- centered arithmetic remainder on the outer detuning lobes.

No unconditional record theorem is claimed.

See:

    notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md
    notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md
    notes/WP84_E2_PRINCIPAL_ARC_NORMALIZATION_AUDIT.md
