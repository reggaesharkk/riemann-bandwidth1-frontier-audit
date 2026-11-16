# WP84 — common-state Bernoulli generator equation

Date: 2026-10-05

Status: **D1 LEAVE-ONE-OUT STATE ELIMINATED WHEN COMBINED WITH D2; SECOND-ORDER FLOW WRITTEN WITH ONE COMMON BERNOULLI RESOLVENT**

No percentage theorem is claimed here.

The Shapley/Bernoulli representation uses, for each current prime-base block
G_p, a state in which p is forced absent.

That leave-one-out state was harmless for D2 but remained awkward for D1.

The key observation is that D1 and D2 should not be decoupled at this point.
When they are recombined, replacing the leave-one-out resolvent by the
ordinary Bernoulli resolvent produces exactly the Bernoulli skew factor

    1-2t.

Thus the complete second-order flow uses one common state R_t.

## 1. Bernoulli ensemble

Let

    xi_p(t) in {0,1}

be independent with

    P(xi_p=1)=t.

Put

    H_t
      = H_0 + sum_p xi_p G_p,

    R_t(z)
      = (H_t-zI)^(-1).

For a fixed p let

    H_t^(-p)
      = H_0 + sum_{q!=p} xi_q G_q,

    R^-=(H_t^(-p)-zI)^(-1),

and

    R^+=(H_t^(-p)+G_p-zI)^(-1).

Conditioned on all q!=p,

    R_t
      =
      R^- with probability 1-t,
      R^+ with probability t.

## 2. One-block expansion

Write

    D1^-
      = tau(R^- G_p R^-),

    D2^-
      = tau(R^- G_p R^- G_p R^-).

The resolvent expansion gives

    R^+
      =
      R^-
      - R^- G_p R^-
      + R^- G_p R^- G_p R^-
      + O_eta(||G_p||^3).

Insert this into the common-state drift

    tau(R_t G_p R_t).

Conditioned on the leave-one-out state,

    E_{xi_p}
      tau(R_t G_p R_t)

      =
      D1^-
      - 2t D2^-
      + O_eta(||G_p||^3).

Similarly,

    E_{xi_p}
      tau(R_t G_p R_t G_p R_t)

      =
      D2^-
      + O_eta(||G_p||^3).

Therefore

    boxed:
    -D1^- + D2^-

      =
      - E_{xi_p}
          tau(R_t G_p R_t)

      + (1-2t)
        E_{xi_p}
          tau(
            R_t G_p R_t G_p R_t
          )

      + O_eta(||G_p||^3).

## 3. Sum over p

The exact Bernoulli/Shapley derivative is

    d/dt E tau(R_t)
      =
      sum_p
      E[
        tau(R^+)-tau(R^-)
      ].

Using Section 2 and

    sum_p ||G_p||^3=o(1),

we get uniformly at every fixed nonreal z

    boxed:

    d/dt E tau(R_t)

      =
      - E tau(
          R_t P R_t
        )

      + (1-2t)
        E tau(
          R_t V(R_t) R_t
        )

      + o(1),

where

    P=sum_p G_p

is the full deterministic prime operator and

    V(A)=sum_p G_p A G_p

is the deterministic variance map.

The entire leave-one-out dependence has disappeared.

## 4. Prime-only D2 insertion

The proper-power reduction and the two D2 closure notes give

    V(R)
      =
      V_res(R)
      + o(1)

inside the normalized D2 trace, because:

- proper powers are o(1);
- the carrier-2T fast channel is o(1);
- the resonant prime-square channel has a uniform continuum limit.

Therefore

    boxed:

    d/dt E tau(R_t)

      =
      - E tau(
          R_t P R_t
        )

      + (1-2t)
        E D2_res_state(R_t)

      + o(1),

where D2_res_state is the explicit deterministic resonant state functional
already derived.

This is the current smallest resolvent evolution equation.

## 5. Functional version

Let f be any fixed rational function whose poles stay a fixed distance from
the real axis, including the four-pole F9 consumer.

The same one-block Taylor calculation gives

    boxed:

    d/dt E tau f(H_t)

      =
      E D[tau f(H_t)][P]

      + (1-2t)/2
        E sum_p
          D^2[tau f(H_t)]
            [G_p,G_p]

      + o(1).

For a resolvent f_z(x)=(x-z)^(-1), this reduces exactly to Section 3.

Thus the bounded four-pole consumer can be propagated directly without
separate pole-by-pole leave-one-out states.

## 6. Interpretation of the factor 1-2t

The coefficient is the third central signature of a Bernoulli bridge.

At t=0 the second-order correction enters with positive sign.

At t=1 it enters with negative sign.

At t=1/2 it vanishes in this common-state representation.

This does **not** mean the accumulated variance effect vanishes: the state
R_t itself depends on t, so the integral of

    (1-2t) D2_res_state(R_t)

need not be zero.

This is precisely where connected/noncommutative memory can survive.

## 7. New theorem frontier

The current-prime arithmetic in D2 is no longer open.

The remaining bounded F9 theorem has two coupled state quantities:

    deterministic drift:
      E tau(R_t P R_t),

    explicit resonant state correction:
      E D2_res_state(R_t).

Both use the **same** Bernoulli state R_t.

The next reduction should exploit the exact scalar Loewner form of P and the
rank-two displacement structure of R_t to turn the drift term into the same
small-channel state variables used by D2.

See:

    notes/WP84_SHAPLEY_BERNOULLI_FLOW.md
    notes/WP84_D2_FAST_CHANNEL_VK_CLOSURE.md
    notes/WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md
    notes/WP84_BR_RANK3_SCALAR_D1.md
