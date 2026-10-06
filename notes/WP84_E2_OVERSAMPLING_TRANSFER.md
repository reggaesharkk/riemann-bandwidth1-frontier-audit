# WP84 — oversampled local Fourier transfer for the balanced E2 sector

Date: 2026-10-06

Status: **DETERMINISTIC SAMPLING LEMMA CLOSED — THE DISCRETE GABOR AVERAGE ON A PRODUCT CELL IS A LOCAL FREQUENCY INTEGRAL PLUS o(1)**

No unconditional zero-density percentage is claimed here.

The balanced product kernel on one product cell is

    (1/d)
    sum_k
      |
        F(alpha_k)
      |^2,

where

    F(alpha)
      =
      sum_{m in I}
        c(m)e(m alpha),

and

    alpha_k
      =
      tau_k/(2pi M_0)

      =
      alpha_0
      +
      k/(L M_0).

Thus the frequency grid spacing is

    delta
      =
      1/(L M_0).

The relevant alpha-window has length comparable to

    1/H,

with

    H=M_0/T.

The grid is therefore strongly oversampled relative to the Fourier degree of
F.  This note makes the discrete-to-continuous transfer quantitative without
a lossy pointwise derivative bound.

## 1. Smooth local cutoff

Let J be the consumed alpha-window.

Choose a smooth cutoff psi such that

    0<=psi<=1,

    psi=1 on J,

    supp psi subset J^+,

where J^+ enlarges J by O(1/H), and for every fixed integer A>=1,

    ||psi^(A)||_1
      <=
      C_A H^(A-1).

Such a cutoff is obtained by rescaling one fixed compactly supported bump.

Because psi>=1 on J,

    delta
    sum_{alpha_k in J}
      |F(alpha_k)|^2

      <=
      delta
      sum_{k in Z}
        psi(alpha_k)|F(alpha_k)|^2.

Only the actual consumed finite block contributes because psi is supported
inside the alpha-span after an arbitrarily small endpoint trimming.

## 2. Poisson summation

Put

    g(alpha)=|F(alpha)|^2.

Since I is contained in one product block of width O(M_0),

    g(alpha)
      =
      sum_{|r|<=M_0}
        b_r e(r alpha).

Apply Poisson summation to

    f(alpha)=psi(alpha)g(alpha)

on the lattice alpha_0+delta Z:

    boxed:

    delta
    sum_k
      f(alpha_0+k delta)

      =
      sum_{ell in Z}
        e(ell alpha_0/delta)
        fhat(ell/delta).

The zero alias is exactly

    fhat(0)
      =
      int
        psi(alpha)|F(alpha)|^2
      d alpha.

## 3. Nonzero aliases

Since

    1/delta=L M_0,

and |r|<=M_0, for L>=2 and ell!=0,

    |ell/delta-r|
      >=
      c |ell| L M_0

for an absolute c>0.

Integration by parts A times gives

    |psihat(xi)|
      <=
      C_A
      H^(A-1)
      |xi|^(-A).

Also

    fhat(xi)
      =
      sum_r
        b_r psihat(xi-r).

For g=|F|^2,

    sum_r |b_r|
      <=
      N_I
      sum_{m in I}|c(m)|^2,

where N_I<=C M_0 is the number of available integer frequencies.

Therefore

    sum_{ell!=0}
      |fhat(ell/delta)|

      <=
      C_A
      [
        M_0 H^(A-1)
        /(L M_0)^A
      ]
      sum_m|c(m)|^2.

Since

    H=M_0/T,

this becomes

    boxed:

    sum_{ell!=0}
      |fhat(ell/delta)|

      <=
      C_A
      /
      [L^A T^(A-1)]
      *
      sum_m|c(m)|^2.

Already A=2 gives

    O(
      1/(L^2 T)
    )
    sum_m|c(m)|^2.

## 4. Discrete-to-local-integral theorem

Combining the previous sections,

    boxed:

    delta
    sum_{alpha_k in J}
      |F(alpha_k)|^2

      <=
      int_{J^+}
        |F(alpha)|^2
      d alpha

      +
      O_A(
        1/[L^A T^(A-1)]
      )
      sum_m|c(m)|^2.

Now

    d delta
      =
      d/(L M_0)

is comparable to T/M_0=1/H.

Therefore

    boxed:

    (1/d)
    sum_{alpha_k in J}
      |F(alpha_k)|^2

      <=
      C H
      int_{J^+}
        |F(alpha)|^2
      d alpha

      +
      O_A(
        H/[L^A T^(A-1)]
      )
      sum_m|c(m)|^2.

Since H<=T in the consumed product range M_0<=T^2, choosing A=2 gives

    boxed:

    sampling error
      =
      O(L^(-2))
      sum_m|c(m)|^2.

Thus any product cell with normalized diagonal energy O(1) has o(1)
sampling loss.

## 5. Why the coefficient norm is available

In the exact balanced product identity, the diagonal m=n contribution is

    sum_m|c(m)|^2.

This is part of the already-calibrated pair sector.

Hence after the project normalization, the total product-coefficient square
mass over all cells is O(1).

Consequently the sum of the sampling errors over any bounded-overlap cell
partition is

    boxed:
    o(1).

No additional almost-prime theorem is needed for this step.

## 6. Consequence for the E2 interface

The discrete Gabor average may now be replaced by a local frequency integral
before the circle-method split:

    discrete balanced trace cell

      <=

    C H
    int_{J^+}
      |F(alpha)|^2 d alpha

      +o(1).

Therefore the local minor-arc estimate on intervals of width 1/H is at the
correct analytic level for the WP84 trace.

The previously open discrete-sample-to-local-integral step is closed.

## 7. Remaining transfer debt

Still open:

1. transfer the exact WP84 factor-sliced smooth coefficient to the E2 weight;
2. preserve the major-arc signed main term under that transfer;
3. sum the factor slices with uniform constants.

The shrinking transition layer is handled separately.

No unconditional record theorem is claimed.

See:

    notes/WP84_E2_LOCAL_WINDOW_TRANSFER.md
    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
