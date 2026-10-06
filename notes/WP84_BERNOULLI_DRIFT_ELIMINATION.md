# WP84 — Bernoulli state self-consistency eliminates the first-order drift

Date: 2026-10-05

Status: **EXACT STATE IDENTITY + SECOND-ORDER BERNOULLI INTEGRATION REDUCE THE COMMON-STATE FLOW TO m, z-derivatives, AND THE ALREADY-EXPLICIT D2 STATE FUNCTIONAL**

No percentage theorem is claimed here.

The current common-state equation is

    partial_t m_t(z)
      =
      - A_t(z)
      + (1-2t) B_t(z)
      + o(1),

where

    A_t(z)
      = E tau(R_t P R_t),

    B_t(z)
      = E sum_p tau(
          R_t G_p R_t G_p R_t
        ),

and the cubic remainder is o(1) uniformly at every fixed nonreal z.

The apparent remaining obstacle is A_t.

It can be eliminated.

## 1. Bernoulli state notation

Assume first that the non-prime background is exactly scalar,

    H_0=s_0 I.

Let

    H_t
      = H_0 + sum_p xi_p G_p,

with independent

    xi_p ~ Bernoulli(t),

and

    R_t=(H_t-zI)^(-1).

Put

    X_t=H_t-H_0=sum_p xi_p G_p.

Define

    C_t(z)
      = E tau(
          R_t X_t R_t
        ).

Since X_t=H_t-s_0 I commutes with H_t and hence with R_t,

    boxed:
    C_t(z)
      =
      m_t(z)
      + (z-s_0) partial_z m_t(z).

This identity is exact.

## 2. One-coordinate Bernoulli identity

Fix p and condition on every xi_q with q!=p.

Let

    R^-=(H^(-p)-zI)^(-1),

    R^+=(H^(-p)+G_p-zI)^(-1).

Put

    F^- = tau(R^- G_p R^-),
    F^+ = tau(R^+ G_p R^+),

and

    B^- = tau(R^- G_p R^- G_p R^-).

The resolvent expansion gives

    F^+
      =
      F^-
      - 2 B^-
      + O_eta(||G_p||^3).

The common-state averages satisfy

    A_p
      =
      (1-t)F^- + tF^+,

while the p contribution to C_t is

    C_p
      =
      E[
        xi_p tau(R_t G_p R_t)
      ]
      =
      tF^+.

Therefore

    C_p - t A_p
      =
      t(1-t)(F^+-F^-)

      =
      -2t(1-t)B^-
      + O_eta(||G_p||^3).

Replacing B^- by the common-state average

    B_p
      =
      (1-t)
        tau(R^- G_p R^- G_p R^-)
      + t
        tau(R^+ G_p R^+ G_p R^+)

costs another O_eta(||G_p||^3).

Hence

    boxed:
    C_p
      =
      t A_p
      - 2t(1-t) B_p
      + O_eta(||G_p||^3).

## 3. Sum over prime-base groups

Using

    sum_p ||G_p||^3=o(1),

we obtain uniformly for t in [0,1],

    boxed:
    C_t
      =
      t A_t
      - 2t(1-t) B_t
      + o(1).

This is the missing self-consistency relation between the first-order drift
and the second-order state term.

## 4. Eliminate A_t from the common-state generator

Multiply

    partial_t m
      =
      -A_t +(1-2t)B_t+o(1)

by t and substitute Section 3:

    t partial_t m
      =
      -C_t
      - t B_t
      + o(1).

Using the exact state identity from Section 1 gives

    boxed:

    t partial_t m_t(z)
      + m_t(z)
      + (z-s_0) partial_z m_t(z)
      + t B_t(z)

      =
      o(1).

The first-order prime drift has disappeared completely.

This is stronger than merely scalarizing A_t.

## 5. Background scalarization error

The actual background satisfies

    H_0
      = s_0(T) I + E_0,

with

    ||E_0||_1/d=o(1)

from WP84_BACKGROUND_SCALARIZATION.md.

For every fixed pole distance eta>0,

    tau(
      R_t E_0 R_t
    )

is o(1) uniformly because

    |tau(R_t E_0 R_t)|
      <= eta^(-2) ||E_0||_1/d.

Therefore the boxed equation survives unchanged with o(1) error for the
actual background.

## 6. B_t is already explicit

The D2 arithmetic closure gives

    B_t(z)
      =
      E Xi_res(R_t(z))
      + o(1),

where Xi_res is the explicit resonant state functional

    Xi_res(R)
      =
      1/(6a_phi^2 d)
        sum_i r_i^2

      - 1/(2a_phi^2 pi^2 d)
        sum_{i!=j}
          R_ij^2/(i-j)^2

      + 1/(2a_phi^2 d)
        [
          sum_i h_i^2
          - sum_i r_i q_i
        ],

with

    r=diag R,
    h=diag(JR),
    q=diag(JRJ).

The fast/carrier-2T D2 channel is already o(1).

Thus the common-state evolution is now

    boxed:

    t partial_t m_t
      + m_t
      + (z-s_0) partial_z m_t

      =
      - t E Xi_res(R_t)
      + o(1).

There is no separate D1 theorem left.

## 7. Functional form

Let f be any fixed rational function with poles a fixed distance from R.

The same argument gives

    boxed:

    t d/dt E tau f(H_t)

      =
      E tau[
        (H_t-s_0 I) f'(H_t)
      ]

      - (t/2)
        E sum_p
          D^2[tau f(H_t)]
            [G_p,G_p]

      + o(1).

For the four-pole F9 consumer this is one scalar bounded-functional identity.

The second term is exactly the already-closed D2 current covariance applied
to the actual state.

## 8. Why this matters

The previous frontier had two state quantities:

    first-order drift A_t,
    second-order correction B_t.

The first one is not independent.

The Bernoulli state itself forces

    t A_t
      =
      m_t +(z-s_0)m_z
      + 2t(1-t)B_t
      + o(1).

So the theorem frontier is now:

> control one explicit second-order Loewner/resolvent state functional
> strongly enough to integrate the scalar transport equation at the four F9
> poles.

No independent deterministic-prime drift estimate remains.

## 9. Characteristic warning

The transport operator

    t partial_t
      + (z-s_0) partial_z

has characteristics

    z-s_0 proportional to t.

Following a characteristic all the way to t=0 moves the spectral parameter
toward the real axis, so one must **not** simply integrate to t=0 using only
fixed-strip resolvent bounds.

A theorem-grade use of the identity should instead:

- work on t>=t0>0 and control the small-t layer separately; or
- use the bounded rational functional form directly; or
- choose a contour/consumer estimate that never collapses the imaginary part.

This note closes an algebraic state variable, not the remaining analytic
small-t problem.

See:

    notes/WP84_BERNOULLI_COMMON_STATE_GENERATOR.md
    notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md
    notes/WP84_BACKGROUND_SCALARIZATION.md
