# WP84 — full deterministic drift is already a scalar Loewner channel

Date: 2026-10-05

Status: **COMMON-STATE D1 DRIFT ALGEBRA CLOSED; NO FULL d-by-d PRIME MATRIX MULTIPLICATION IS NEEDED**

No percentage theorem is claimed here.

After the common-state Bernoulli reduction, the only first-order term is

    tau(R_t P R_t),

where

    P=sum_p G_p

is the full deterministic retained sharp prime operator.

This may look like the last generic matrix object.

It is not.

The exact scalar Loewner representation and the scalar D1 identity apply to
P itself, so the full drift is already determined by one fixed scalar prime
Dirichlet polynomial plus the same three state vectors used elsewhere.

## 1. Full scalar prime field

Let

    Q_*(tau)
      =
      sum_{n in retained range}
        c_n exp(i tau log n).

Write

    alpha_*
      = Im Q_*(tau_k),

    beta_*
      =
      2 Re Q_*(tau_k)
      - 2 (Im Q_*)'(tau_k)/L.

Then exactly

    boxed:
    P
      =
      M_{beta_*}
      + [M_{alpha_*},J].

No additional matrix data are needed.

## 2. Bernoulli state field

At time t, one realization of the Bernoulli state is encoded by

    Q_t(tau)
      =
      sum_n xi_n(t)c_n exp(i tau log n)

with prime-base grouping understood.

Put

    a_t=Im Q_t(tau_k),

    R_t=(H_t-zI)^(-1),

and define

    r_t=diag R_t,

    u_t=R_t 1,

    v_t=R_t a_t.

These are the same state variables appearing in the rank-three D1/D2
reduction.

## 3. Exact drift primitive

For any current Loewner block B with scalar fields alpha,beta, the already
proved identity is

    tr(BR)
      =
      sum_i beta_i R_ii
      + (2/pi^2)
        u^T L_alpha v,

where

    L_alpha
      =
      M_alpha K2-K2 M_alpha.

Set B=P.

Then exactly

    boxed:

    tau(P R_t)

      =
      d^(-1)
      [
        sum_i beta_{*,i} r_{t,i}

        + (2/pi^2)
          u_t^T
          L_{alpha_*}
          v_t
      ].

The full prime operator enters only through the **fixed vectors**

    alpha_*,
    beta_*.

## 4. Exact common-state D1 coefficient

Because

    dR/dz=R^2,

    d/dz tau(P R)
      =
      tau(P R^2)
      =
      tau(R P R).

Therefore

    boxed:

    tau(R_t P R_t)

      =
      d/dz
      {
        d^(-1)
        [
          beta_*^T r_t
          + (2/pi^2)
            u_t^T L_{alpha_*} v_t
        ]
      }.

So the deterministic drift in the Bernoulli generator is a scalar
one-dimensional Loewner/K2 statistic.

It is not a remaining generic matrix multiplication problem.

## 5. Flow after inserting the D2 closure

The common-state resolvent equation becomes

    d/dt E tau(R_t)

      =
      - d/dz
        E[
          d^(-1)
          {
            beta_*^T r_t
            + (2/pi^2)
              u_t^T L_{alpha_*} v_t
          }
        ]

      + (1-2t)
        E D2_res_state(R_t)

      + o(1).

Every term is now expressed through:

    fixed arithmetic data:
      alpha_*, beta_*;

    state data:
      diag R_t,
      R_t 1,
      R_t a_t,
      diag(JR_t),
      diag(JR_tJ);

    one-dimensional bounded operators:
      J, K2, L_{alpha_*}.

No d by d product with P needs to be formed.

## 6. Two-parameter characteristic interpretation

Introduce

    m(t,theta,z)
      =
      E tau[
        (
          H_t + theta P - zI
        )^(-1)
      ].

Then

    partial_theta m
      =
      - E tau(
          R_{t,theta} P R_{t,theta}
        ).

Hence the drift is exactly a theta-characteristic derivative:

    boxed:
    partial_t m
      =
      partial_theta m
      + (1-2t)
        E D2_res_state(R_{t,theta})
      + o(1).

This reformulation does not solve the state evolution by itself, but it
removes P as a mysterious forcing term.

The unresolved object is now the evolution of the finite Loewner-generator
state under a known characteristic plus a known second-order resonant
functional.

## 7. Frontier

The algebraic matrix reduction is now essentially exhausted.

What remains is a genuine limiting-state theorem:

> control the Bernoulli averages of the scalar/resolvent generator variables
> uniformly at the four F9 poles strongly enough to keep the final bounded
> consumer below 0.1632499815.

That is narrower than a generic prime-side resolvent law and narrower than a
raw moment theorem.

See:

    notes/WP84_BERNOULLI_COMMON_STATE_GENERATOR.md
    notes/WP84_BR_RANK3_SCALAR_D1.md
    notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md
