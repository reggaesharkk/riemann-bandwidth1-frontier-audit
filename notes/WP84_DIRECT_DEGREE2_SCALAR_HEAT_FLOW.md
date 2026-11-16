# WP84 — direct degree-two Cayley square as a one-point repeated-pole heat-flow functional

Date: 2026-10-06

Status: **EXACT FINITE-d FUNCTIONAL CALCULUS; THE CURRENT BEST ONE-POINT RANK-FOUR CONSUMER USES ONLY m(i) AND m'(i)**

No unconditional zero-density percentage is claimed here.

The current preferred direct support-free square is

    q(u)
      =
      [623 u^2 +(55-1058 i)u -(557+58 i)]/1000,

with

    U=(H+iI)(H-iI)^(-1),

    Q=q(U),

and

    h(H)=I-Q^*Q <= 1_{H>0}.

Its exact pinned-model defect energy is

    E_model
      =
      0.10803423463999824...,

against the conservative record energy ceiling

    E_rec
      =
      0.163249981456072...,

leaving the model energy margin

    0.0552157468160738....

This note rewrites the same positive energy in the scalar resolvent language.

## 1. Fourier coefficients of |q|^2

On |u|=1,

    p(u)=|q(u)|^2

has the exact Fourier expansion

    p(u)
      =
      c0
      + c1 u + conjugate(c1)u^(-1)
      + c2 u^2 + conjugate(c2)u^(-2),

with

    c0
      =
      1824131/1000000,

    c1
      =
      32497/500000
      +(125163/100000)i,

    c2
      =
      -347011/1000000
      +(18067/500000)i.

Therefore

    tau(Q^*Q)
      =
      c0
      +2 Re[
          c1 tau(U)
          +c2 tau(U^2)
        ].

## 2. Collapse to m(i) and m'(i)

At z=i let

    R=(H-iI)^(-1),

    m(i)=tau(R),

    m'(i)=tau(R^2).

Since

    U=I+2iR,

    U^2
      =
      I+4iR-4R^2.

Substitution gives exactly

    boxed:

    tau(Q^*Q)

      =
      1260097/1000000

      +2 Re[
          A m(i)
          +B m'(i)
        ],

where

    boxed:

    A
      =
      -661949/250000
      -(157257/125000)i,

    B
      =
      347011/250000
      -(18067/125000)i.

Thus the entire direct degree-two positive energy consumes only one
upper-half-plane point and one z derivative.

No second pole and no Cayley moment hierarchy remain.

## 3. Direct record inequality

A sufficient condition for the conservative comparison line is

    boxed:

    1260097/1000000

      +2 Re[
          A m_T(i)
          +B m_T'(i)
        ]

      <
      0.163249981456072...

in the large-T limit, after the already-closed background/taper/rank
transfers.

The model benchmark is

    0.10803423463999824...,

so this scalar repeated-pole formulation retains the full direct-square
margin

    0.0552157468160738....

This is much larger than the earlier scaled-r2 one-point margins.

## 4. Q itself is only quadratic in the resolvent

The operator factor has the exact form

    boxed:

    Q

      =
      (121/1000 -279i/250) I

      +(529/250 +1301i/500) R

      -(623/250) R^2.

This is useful if the proof prefers the positive energy Q^*Q rather than the
linear scalar trace formula.

The displacement rank remains

    rank[D,Q]<=4

because the Cayley representation is degree two.

## 5. Gaussian heat-flow representation

Use the already-closed Bernoulli-to-Gaussian invariance and the co-moving
additive Gaussian heat flow

    H_u
      =
      H_1 + sqrt(u) W,

with

    m_u(z)
      =
      E tau(H_u-zI)^(-1).

Define

    C_u(z)
      =
      partial_u m_u(z).

Then

    E_u
      :=
      E tau(
        q(U_u)^*q(U_u)
      )

satisfies exactly

    boxed:

    E_u

      =
      1260097/1000000

      +2 Re[
          A m_u(i)
          +B partial_z m_u(i)
        ],

and therefore

    boxed:

    E_u'

      =
      2 Re[
        A C_u(i)
        +B partial_z C_u(i)
      ].

So the direct rank-four theorem may be attacked with the same explicit
Gaussian covariance functional already developed for the r2 heat-flow route,
but with a much larger final error margin.

## 6. Infinite-noise boundary is explicit

For every fixed finite section, the existing Gaussian invertibility argument
gives

    U_u -> I

almost surely as u->infinity.

Hence

    q(U_u)
      ->
      q(1) I,

with

    q(1)
      =
      121/1000 -279i/250.

Therefore

    boxed:

    E_u
      ->
      |q(1)|^2
      =
      1260097/1000000
      =
      1.260097.

Thus at finite d,

    boxed:

    E_0

      =
      1260097/1000000

      -
      2 Re
      int_0^infinity
        [
          A C_u(i)
          +B partial_z C_u(i)
        ]
      du.

The record is crossed if the integrated curvature exceeds

    boxed:

    1260097/1000000
      -
      0.163249981456072...

      =
      1.096847018543928....

The model endpoint corresponds to an integral approximately

    1.1520627653600018....

So the available integrated-curvature margin is again

    0.0552157468160738....

## 7. Strategic significance

The direct degree-two square now has three equivalent theorem interfaces:

1. positive rank-four displacement energy:
       tau(Q^*Q);

2. one-point repeated-pole scalar:
       m(i), m'(i);

3. one-point Gaussian heat-flow curvature:
       C_u(i), partial_z C_u(i).

All three are exact.

This means we do not need to choose prematurely between displacement-rank
control and Gaussian integration by parts.

Whichever estimate closes first proves the same bounded consumer.

## 8. Evidence boundary

Closed here:

- exact Fourier coefficients;
- exact m(i),m'(i) reduction;
- exact quadratic resolvent formula for Q;
- exact finite-d heat-flow identity;
- exact finite-d large-u boundary.

Still open:

- a theorem-grade large-d one-sided bound strong enough to keep E_0 below
  the conservative ceiling.

No unconditional record theorem is claimed.

See:

    notes/WP84_DIRECT_DEGREE2_CAYLEY_SQUARE.md
    notes/WP84_BERNOULLI_GAUSSIAN_INVARIANCE.md
    notes/WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.md
