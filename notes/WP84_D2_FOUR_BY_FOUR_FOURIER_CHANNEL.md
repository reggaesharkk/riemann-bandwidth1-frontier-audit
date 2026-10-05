# WP84 — D2 rank-four state collapses to a one-dimensional 4x4 Fourier channel

Date: 2026-10-05

Status: **EXACT FINITE-DIMENSIONAL REDUCTION CLOSED; TWO-DIMENSIONAL SQUARED-CAUCHY SUM ELIMINATED**

No percentage theorem is claimed here.

The LRSC displacement reduction gave, for

    X=BR,
    C=[D,X],

the exact formula

    tr(X^2)
      = sum_i X_ii^2
        - sum_{i!=j} C_ij C_ji/(i-j)^2,

with

    rank C <= 4.

The remaining off-diagonal object still looked like a two-index sum.

It is actually a one-dimensional Fourier integral of matrices of size at
most 4 by 4.

## 1. Exact Fourier kernel

For 0<=t<=2*pi define

    S2(t)
      = pi^2/3 - pi t + t^2/2.

The classical Fourier identity is

    boxed:
    S2(t)
      = sum_{r in Z, r!=0} e^(i r t)/r^2.

Its average over one period is zero.

Therefore for every nonzero integer r,

    1/r^2
      = (1/(2*pi))
          int_0^(2*pi) S2(t) e^(-i r t) dt.

Also

    |S2(t)| <= pi^2/3.

## 2. Convert the entire off-diagonal sum

Let

    D=diag(0,1,...,d-1),
    U_t=exp(i t D).

For any complex d by d matrix C,

    tr(C U_t C U_t^*)
      = sum_{i,j}
          C_ij C_ji e^(-i(i-j)t).

Because S2 has zero constant Fourier coefficient, the diagonal i=j terms
drop after integration.

Hence exactly

    boxed:
    sum_{i!=j}
      C_ij C_ji/(i-j)^2

      = (1/(2*pi))
          int_0^(2*pi)
            S2(t)
            tr(C U_t C U_t^*) dt.

This is a finite-matrix identity.  No limiting argument enters.

## 3. Use rank at most four

Choose any displacement factorization

    C=G H^T,

with

    G,H in C^(d x r),
    r<=4.

Cyclicity of the trace gives

    tr(C U_t C U_t^*)
      = tr_r[
          (H^T U_t G)
          (H^T U_t^* G)
        ].

Define the r by r Fourier channel

    A(t)=H^T U_t G.

Then

    boxed:
    sum_{i!=j}
      C_ij C_ji/(i-j)^2

      = (1/(2*pi))
          int_0^(2*pi)
            S2(t)
            tr_r[A(t)A(-t)] dt.

Thus the nominal d-squared transition state has collapsed to:

- one scalar diagonal sequence X_ii;
- one periodic scalar integral;
- matrices A(t) of dimension at most 4.

The matrix size of the Fourier channel is independent of d.

## 4. D2 formula

The previous exact identity becomes

    boxed:
    tr(X^2)
      = sum_i X_ii^2
        - (1/(2*pi))
            int_0^(2*pi)
              S2(t)
              tr_r[A(t)A(-t)] dt.

Consequently

    D2(H;B,z)
      = (1/2) d/dz tau((BR)^2)

can be evaluated from one-dimensional generator Fourier statistics.

A generic bivariate transition measure is not needed, and neither is an
O(d^2) state.

## 5. Uniform domination

Since

    |S2(t)|<=pi^2/3,

we obtain immediately

    |offdiag(C)|
      <= (pi^2/3)
          * (1/(2*pi))
            int_0^(2*pi)
              |tr_r[A(t)A(-t)]| dt.

This is useful for a one-sided theorem such as the four-pole
delta=9 record gate: one can spend the explicit 0.011274... consumer budget
on a scalar integral bound instead of proving a full local law.

## 6. Why this is an LRSC-type reduction

The mechanism is exactly the one that made LRSC useful here:

    low displacement rank
      -> finite generator channels
      -> reconstruct the large matrix observable
         through a small channel algebra.

The Riemann object is not low ordinary rank.  The relevant rank is the
commutator/displacement rank, and the squared-Cauchy Green kernel can be
integrated out analytically.

## 7. New arithmetic target

For the four-pole F9 theorem, derive the current-block/subset averages of

    diagonal(BR)

and

    A_{S,p,z}(t)
      = H_{S,p,z}^T e^(itD) G_{S,p,z}

at only the four consumed poles.

The remaining state is now a family of at most 4 by 4 Fourier transforms on
one circle.

This is the point at which one should attempt:

- prime-base valuation cancellation;
- MRT/E2 long-shift bounds;
- Abel/summation-by-parts estimates in t;
- one-sided domination using the explicit record margin.

See:

    notes/WP84_D1_D2_DISPLACEMENT_REDUCTION.md
    notes/WP84_FOUR_POLE_INEQUALITY_KILL_GATE.md
