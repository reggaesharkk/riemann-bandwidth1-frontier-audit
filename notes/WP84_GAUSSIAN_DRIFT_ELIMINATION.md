# WP84 — exact elimination of the deterministic drift on the Gaussian bridge

Date: 2026-10-05

Status: **EXACT GAUSSIAN IDENTITY — AFTER BACKGROUND SCALARIZATION THE FULL PRIME DRIFT DISAPPEARS FROM THE EVOLUTION EQUATION; ONLY THE MIXED COVARIANCE FUNCTIONAL REMAINS**

No percentage theorem is claimed here.

The Gaussian quadrature bridge was introduced because its artificial noise
has **mixed-sign-only** covariance.  Its derivative formula still contained
the deterministic full-prime drift

    E tau(R_t P_full R_t).

That drift can be eliminated exactly.

## 1. Setup

Let

    H_t
      = s0 I
        + t P
        + sqrt(v(t)) W,

    v(t)=t(1-t),

where:

- P is the full deterministic retained sharp prime operator;
- W is the artificial circular/quadrature Gaussian operator;
- its covariance map is

      V(X)=E[W X W],

  which contains only the mixed-sign prime-square channel.

Put

    R_t(z)=(H_t-zI)^(-1),

    F(t,z)=E tau(R_t(z)),

and define

    C(t,z)
      = E tau(
          R_t V(R_t) R_t
        ).

## 2. Bridge derivative

Differentiating the resolvent gives

    F_t
      =
      - D
      + v'(t) C,

where

    D
      = E tau(R_t P R_t).

For v=t(1-t),

    v'=1-2t.

## 3. Gaussian integration by parts for the W term

Write

    W=sum_j g_j E_j

in its independent real Gaussian Hermitian directions.

Then

    partial_{g_j} R
      = -sqrt(v) R E_j R.

For

    f_j(g)=tau(R E_j R),

    partial_{g_j} f_j
      = -2 sqrt(v)
          tau(R E_j R E_j R).

Therefore Gaussian integration by parts gives

    E tau(R W R)
      =
      -2 sqrt(v) C.

This identity is exact at finite d.

## 4. Use H-s0 I to solve for the drift

Since

    H-s0 I
      = tP + sqrt(v)W,

we have

    E tau(
      R(H-s0 I)R
    )

      =
      tD - 2vC.

But

    H-s0 I
      =(H-zI)+(z-s0)I,

so

    R(H-s0 I)R
      = R +(z-s0)R^2.

Hence

    boxed:
    tD - 2vC
      =
      F +(z-s0)F_z.

Thus

    D
      =
      [F +(z-s0)F_z +2vC]/t.

## 5. Exact drift-free bridge equation

Substitute Section 4 into Section 2:

    F_t
      =
      -[F +(z-s0)F_z]/t
      +[v' -2v/t] C.

For

    v=t(1-t),

    v' -2v/t
      =(1-2t)-2(1-t)
      =-1.

Therefore

    boxed:
    F_t(t,z)
      + [F(t,z)+(z-s0)F_z(t,z)]/t
      + C(t,z)
      =0.

Equivalently,

    boxed:
    C(t,z)
      =
      -F_t
      -[F+(z-s0)F_z]/t.

The deterministic prime drift P has disappeared completely from the
evolution equation.

It remains encoded in the mean of H_t and hence inside F and C, but there is
no separate twisted-prime drift theorem left to prove.

## 6. Actual background S instead of s0 I

For

    H_t=S+tP+sqrt(v)W,

the same proof gives

    tD-2vC
      =
      F
      +E tau(
        R(zI-S)R
      ).

The source-closed background scalarization is

    S=s0 I+E_S,

with normalized trace-norm / operator contribution o(1) for every fixed
nonreal resolvent consumer.

Thus uniformly on the four F9 pole circles,

    E tau(
      R(zI-S)R
    )

      =(z-s0)F_z+o(1).

Hence the drift-free equation survives with o(1) error for the actual
background.

## 7. Why this changes the active frontier

The Gaussian route previously appeared to trade one hard object for another:

    remove same-sign variance
      but inherit full deterministic drift.

That trade is no longer present.

After the exact identity above, the bridge theorem needs only the
mixed-sign covariance functional

    C(t,z)
      =E tau(
        R_t V_mix(R_t) R_t
      ),

plus the already-controlled background error.

There is:

- no explicit first-order prime sum;
- no p^(+/- iT) drift estimate;
- no p^(+/-2iT) same-sign variance estimate;
- no fixed-cardinality subset combinatorics;
- no cubic Taylor remainder.

All deterministic arithmetic enters through the mean Loewner field inside
R_t; the only exposed nonlinear generator is the carrier-free square-prime
mixed covariance.

## 8. Remaining theorem target

The active analytic problem is now sharply:

> control the mixed covariance scalar
>
>     C(t,z)
>
> for 0<t<1 and the four fixed F9 pole circles, using the rank-two
> displacement law, the explicit circular Gaussian covariance, and the
> source-closed square-prime measure.

This is strictly smaller than the prior drift-plus-variance problem.

See:

    notes/WP84_GAUSSIAN_QUADRATURE_BRIDGE.md
    notes/WP84_CIRCULAR_GAUSSIAN_Q_FIELD.md
    notes/WP84_PRIME_FRAME_GAUSSIAN_CONCENTRATION.md
