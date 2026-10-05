# WP84 — exact Shapley/Bernoulli representation of the permutation path

Date: 2026-10-05

Status: **PERMUTATION COMBINATORICS REPLACED EXACTLY BY A CONTINUOUS BERNOULLI SUBSET FLOW**

No percentage theorem is claimed here.

The random permutation in the Lindeberg argument is only a proof device.
There is an exact equivalent representation that is cleaner for arithmetic:
the Shapley/Bernoulli interpolation on the Boolean cube.

This removes the stage-by-stage hypergeometric bookkeeping.

## 1. General finite set identity

Let

    [M]={1,...,M}

and let F(S) be any complex-valued set function.

For p in [M], let S_t^{(-p)} be a random subset of [M]\{p} in which every
q!=p is included independently with probability t.

Then exactly

    boxed:
    F([M])-F(empty)

      =
      sum_{p=1}^M
      int_0^1
        E[
          F(S_t^{(-p)} union {p})
          - F(S_t^{(-p)})
        ] dt.

Proof: for a fixed S not containing p with |S|=k, its Bernoulli weight is

    t^k (1-t)^(M-k-1).

Integrating gives

    int_0^1
      t^k(1-t)^(M-k-1) dt

      = k!(M-k-1)!/M!,

which is exactly the probability that S is the set preceding p in a uniform
random permutation.

So this is the permutation average written continuously.

## 2. Apply to the resolvent trace

Put

    H_S = H_0 + sum_{q in S} G_q,

    F_z(S)=tau_d((H_S-zI)^(-1)).

Then

    boxed:
    m_full(z)-m_0(z)

      =
      sum_p
      int_0^1
        E_t[
          m_{S_t^{(-p)}+p}(z)
          - m_{S_t^{(-p)}}(z)
        ] dt.

No approximation has entered.

## 3. Second-order one-block expansion

For

    R=(H_{S_t^{(-p)}}-zI)^(-1),

the exact resolvent expansion gives

    m_{S+p}-m_S

      =
      - tau(R G_p R)
      + tau(R G_p R G_p R)
      + E_{p,S}(z),

with

    |E_{p,S}(z)|
      <= eta^(-4) ||G_p||^3,

    eta=|Im z|.

Summing p and integrating t,

    boxed:
    m_full-m_0

      =
      int_0^1
      E_t [
        - sum_p D1_{p,t}^{(-p)}
        + sum_p D2_{p,t}^{(-p)}
      ] dt
      + O_eta(sum_p ||G_p||^3).

Since

    sum_p ||G_p||^3=O(L^-3),

the total remainder is o(1).

## 4. Strategic advantage

At each fixed t:

- the inclusion variables for all q!=p are independent Bernoulli(t);
- the current p is absent by construction;
- there is no random subset size denominator;
- the whole path is indexed by one deterministic continuum parameter
  t in [0,1].

This is much cleaner than carrying all k=0,...,M-1 hypergeometric stages.

## 5. Centered form of the Bernoulli state

Write independent indicators

    xi_q(t) in {0,1},
    E xi_q=t.

Then the full Bernoulli state is

    H_t
      = H_0
        + t P
        + sum_q (xi_q-t) G_q,

where

    P=sum_q G_q.

Thus the state splits exactly into:

1. deterministic mean path H_0+tP;
2. centered independent infinitesimal fluctuations.

The fluctuation square mass is O(1) and the cubic mass is o(1).

This is the natural setup for a matrix Dyson/cumulant calculation if one can
control the deterministic carrier-bearing mean path.

## 6. Relation to the D2 leave-one-out note

The separate D2 coupling note shows that the omission of the current p from
the state can be removed at o(1) total cost in the second-order sector.

In the Bernoulli language this means D2 may be studied using one common
Bernoulli state H_t and the deterministic variance map

    V(A)=sum_p G_p A G_p,

up to o(1).

The first-order sector does not admit that replacement for free and remains
the harder drift problem.

## 7. Symmetric endpoint form

For one block define

    R_0=(H_S-zI)^(-1),
    R_1=(H_S+G_p-zI)^(-1).

The exact path identity is

    m_1-m_0
      = - int_0^1
          tau(
            R_theta G_p R_theta
          ) dtheta,

where

    R_theta=(H_S+theta G_p-zI)^(-1).

The trapezoidal expansion gives

    m_1-m_0
      =
      -1/2 [
        tau(R_0 G_p R_0)
        + tau(R_1 G_p R_1)
      ]
      + O_eta(||G_p||^3).

This is equivalent to the D1-D2 expansion through second order.

It shows conceptually that D2 is the correction required when the drift is
sampled only at the pre-insertion endpoint.

## 8. New theorem formulation

The four-pole F9 comparison can now be attacked as a continuous t-flow:

    four fixed z_j
      x t in [0,1]
      x Bernoulli subset state
      x small displacement/Fourier channels.

The discrete permutation combinatorics are no longer part of the theorem
debt.

See:

    notes/WP84_D2_LEAVE_ONE_OUT_DECOUPLING.md
    notes/WP84_D1_AGGREGATE_D2_PRIME_ONLY.md
    notes/WP84_BR_RANK3_SCALAR_D1.md
