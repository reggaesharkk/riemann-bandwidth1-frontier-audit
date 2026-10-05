# WP84 — canonical two-vector frame for the sine-square leakage

Date: 2026-10-06

Status: **EXACT FINITE-d REDUCTION; THE OFF-DIAGONAL ENERGY IS CONTROLLED BY ONE 2x2 WARD GRAM DETERMINANT AND ONE LEVERAGE-SCORE IPR**

No unconditional zero-density percentage is claimed here.

For the preferred sine-square parameters

    a=63/50,
    t=17/16,

let

    R=(H-iaI)^(-1),

    u=R 1,
    v=R alpha.

The exact displacement generator is

    [D,Q]
      =
      (2ta/pi)
      Re(
        u v^T-v u^T
      ).

The pair (u,v) is not unique.  Any determinant-one change of basis in the
two-dimensional source space leaves the wedge unchanged.  This freedom can
be used to put the two-vector state into a canonical form.

## 1. Source-frame invariance

Write

    W=[u,v]

as a d by 2 matrix.

For any 2 by 2 complex matrix M with

    det M=1,

put

    W'=W M

with columns u',v'.

Then

    boxed:

    u' v'^T-v' u'^T
      =
      u v^T-v u^T.

Therefore the exact off-diagonal energy is invariant under SL(2,C) changes
of the source frame.

This includes:

- shears v -> v-c u;
- reciprocal rescalings u -> lambda u, v -> lambda^(-1)v;
- the canonical isotropization below.

## 2. Canonical isotropic frame

Let

    G=W^*W

be the 2 by 2 Hermitian Gram matrix.

If det G=0 then u and v are linearly dependent and the wedge energy is
identically zero.

Assume det G>0.

Define

    boxed:

    M
      =
      (det G)^(1/4)
      G^(-1/2).

Then

    det M=1,

and

    boxed:

    (W M)^*(W M)
      =
      sqrt(det G) I_2.

Thus the transformed columns are orthogonal and have the same squared norm

    sqrt(det G).

## 3. Leverage scores

Let W_c=WM be the canonical frame.

Define

    boxed:

    ell_i
      =
      ||(W_c)_{i,:}||_2^2
      /
      sqrt(det G).

Then the normalized matrix

    Phi
      =
      W_c/(det G)^(1/4)

has orthonormal columns, so ell_i are exactly its rank-two leverage scores.

Hence

    boxed:

    0<=ell_i<=1,

    sum_i ell_i=2.

Define the leverage inverse-participation statistic

    boxed:

    kappa
      =
      d sum_i ell_i^2.

Its deterministic range is

    4<=kappa<=2d.

The lower endpoint corresponds to a perfectly flat rank-two frame.

## 4. Canonical wedge majorant

For rows w_i,w_j of the canonical frame,

    |det(w_i,w_j)|^2
      <=
      ||w_i||_2^2
      ||w_j||_2^2.

Since

    ||w_i||_2^2
      =
      sqrt(det G) ell_i,

the exact sine-square off-diagonal energy satisfies

    E_off

      <=
      4t^2a^2/
      (pi^2 d)
      det G
      sum_{i!=j}
        ell_i ell_j/(i-j)^2.

The K2 operator norm bound

    ||K2||op<=pi^2/3

then gives

    boxed:

    E_off
      <=
      4t^2a^2/3
      *
      gamma
      *
      kappa,

where

    boxed:

    gamma
      =
      det G/d^2,

    kappa
      =
      d sum_i ell_i^2.

At

    a=63/50,
    t=17/16,

    boxed:

    4t^2a^2/3
      =
      382347/160000
      =
      2.38966875.

So

    boxed:

    E_off
      <=
      2.38966875
      gamma kappa.

This bound is invariant under the arbitrary choice of the two source
generators.

## 5. Ward form of gamma

Let

    Y=Im R.

For Hermitian H,

    R^*R=Y/a.

Let

    X=[1,alpha].

Then

    G
      =
      X^T R^*R X
      =
      (1/a)
      X^T Y X.

Therefore

    boxed:

    gamma
      =
      1/(a^2 d^2)
      det
      [
        <1,Y1>          <1,Y alpha>
        <alpha,Y1>      <alpha,Y alpha>
      ].

So gamma is only a 2 by 2 positive Ward determinant.

The direct route has now separated into:

1. diagonal resolvent energy;
2. one scalar 2 by 2 Ward determinant gamma;
3. one rank-two leverage IPR kappa.

## 6. Static sufficient inequality

At a fixed band R, let

    E_target(R)
      =
      E_rec
      -
      C_sine/R,

with

    C_sine
      ~=4.43651377028.

A sufficient theorem is

    boxed:

    E_diag
      +
      2.38966875 gamma kappa

      <
      E_target(R),

where

    E_diag
      =
      d^(-1)
      sum_i
        [
          1-2ta Re R_ii
        ]^2.

For example,

    R=256:

      E_target
        ~=0.1459198495.

Thus a sufficient fixed-band gate is

    boxed:

    E_diag
      +
      2.38966875 gamma kappa

      <
      0.1459198495.

## 7. Interpretation of the remaining debt

The row-energy problem is not an arbitrary l4 estimate.

It is precisely the concentration of the leverage scores of a two-dimensional
resolvent source space.

The theorem can close by any estimate that controls the product

    gamma kappa

together with E_diag.

Possible routes include:

- direct control of the exact K2-weighted leverage form, avoiding the
  operator-norm bound;
- a leverage-score delocalization estimate for the canonical frame;
- a local-law estimate for the two Ward quadratic forms entering gamma.

The exact wedge formula remains primary.  The gamma-kappa inequality is a
fail-closed sufficient gate.

## 8. Evidence boundary

Closed:

- SL(2,C) invariance of the source wedge;
- canonical equal-norm orthogonal frame;
- exact leverage normalization;
- invariant gamma-kappa majorant;
- 2 by 2 Ward determinant formula.

Open:

- a theorem-grade upper bound on the actual product gamma*kappa strong enough
  to close the fixed-band energy inequality.

No unconditional record theorem is claimed.

See:

    notes/WP84_SINE_TWO_VECTOR_WEDGE.md
    notes/WP84_MPRIME_TRANSPOSE_VERIFICATION.md
