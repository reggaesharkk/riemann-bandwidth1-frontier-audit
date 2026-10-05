# WP84 — aggregate D1 and prime-only D2 reduction

Date: 2026-10-05

Status: **EXACT D1 CURRENT-AVERAGE COLLAPSE; PROPER PRIME POWERS REMOVED FROM D2 AT O(L^-2) UNIFORMLY OFF THE REAL AXIS**

No percentage theorem is claimed here.

Prime-base grouping writes the retained prime operator as

    sum_{p<=X} G_p,

where

    G_p = B_p^(1) + E_p,

    B_p^(1) := B_{p},

    E_p := sum_{a>=2, p^a<=X} B_{p^a}.

The grouped Lindeberg step has two surviving terms:

    D1 ~ tau(R G_p R),

    D2 ~ tau(R G_p R G_p R).

The two terms behave differently with respect to proper powers.

The first is linear in the current block and should be aggregated exactly.
The second is quadratic, but all proper-power corrections are absolutely
summable and vanish uniformly.

## 1. Exact conditional aggregation of D1

Fix a subset S of already inserted prime bases and let

    R_S(z)
      = (H_S-zI)^(-1).

Conditioned on S, the next prime base is uniform in the complement.

Define

    M1(S)
      = 1/(M-|S|)
        sum_{p notin S} G_p.

Then exactly

    E_{p | S} tau(R_S G_p R_S)
      = tau(R_S M1(S) R_S).

Equivalently, at the primitive level,

    E_{p | S} tau(G_p R_S)
      = tau(M1(S) R_S).

Thus D1 never needs one current-prime state per p.

## 2. M1 is encoded by one remaining Dirichlet polynomial

For each prime-base group write its scalar polynomial

    Q_p(tau)
      = sum_{a>=1, p^a<=X}
          c_{p^a} exp(i tau a log p).

Put

    Q_rem,S(tau)
      = 1/(M-|S|)
        sum_{p notin S} Q_p(tau).

Then the exact Loewner representation gives

    M1(S)
      = M_{beta_bar}
        + [M_{alpha_bar},J],

where

    alpha_bar
      = Im Q_rem,S,

    beta_bar
      = 2 Re Q_rem,S
        - 2 (Im Q_rem,S)'/L.

So the entire conditional D1 current average is encoded by **one scalar
remaining polynomial**.

## 3. Exact scalar D1 primitive after averaging

Let the subset state be encoded by

    a = Im Q_S,

and put

    u=R_S 1,
    v=R_S a,
    r_i=(R_S)_{ii}.

For

    L_alpha
      = M_alpha K2 - K2 M_alpha,

the rank-three note proved

    tr(BR)
      = sum_i beta_i r_i
        + (2/pi^2) u^T L_alpha v.

By linearity in alpha and beta, conditioned on S,

    boxed:
    E_{p | S} tr(G_p R_S)

      = sum_i beta_bar_i r_i
        + (2/pi^2)
          u^T L_{alpha_bar} v.

Therefore

    boxed:
    E_{p | S} D1(H_S;G_p,z)

      = d/dz [
          d^(-1)
          {
            sum_i beta_bar_i r_i
            + (2/pi^2) u^T L_{alpha_bar} v
          }
        ].

This is exact at finite d.

There is no current-prime summation left in D1.

## 4. Proper powers are uniformly negligible in D2

Use the established grouped-block norm bound

    ||B_{p^a}||op
      <= 4 log p/(L p^(a/2)).

Then

    ||B_p^(1)||op
      <= 4 log p/(L sqrt p),

and

    ||E_p||op
      <= (4 log p/L)
          sum_{a>=2} p^(-a/2)

      = (4 log p/L)
          /[p(1-p^(-1/2))].

For every fixed nonreal spectral parameter with

    eta=|Im z|>0,

we have

    ||R_S(z)||op <= eta^(-1).

The difference between the grouped quadratic primitive and its prime-only
version obeys

    |tau(
       R G_p R G_p R
       - R B_p^(1) R B_p^(1) R
     )|

      <= eta^(-3)
          [
            2 ||B_p^(1)|| ||E_p||
            + ||E_p||^2
          ].

Summing over p gives

    sum_p ||B_p^(1)|| ||E_p||
      <= C/L^2
          sum_p
            (log p)^2 /
            [p^(3/2)(1-p^(-1/2))],

and

    sum_p ||E_p||^2
      <= C/L^2
          sum_p
            (log p)^2 /
            [p^2(1-p^(-1/2))^2].

Both prime series converge absolutely.

Hence, uniformly over every fixed pole set bounded away from the real axis,

    boxed:
    sum_p
      |
        D2(H_S;G_p,z)
        - D2(H_S;B_p^(1),z)
      |
      = O_eta(L^-2)
      = o(1).

The same estimate survives permutation averaging because it is deterministic
and uniform in S.

## 5. Consequence: D2 only needs ordinary primes

For the theorem-side second-order term, prime-base groups may be replaced by
their first-power blocks:

    G_p  ->  B_p.

All same-base cross-power covariance disappears into an o(1) error.

Thus the active D2 current field has the exact simple form

    Q_p(tau)
      = c_p exp(i tau log p),

so

    alpha_p(tau)
      = c_p sin(tau log p),

    beta_p(tau)
      = 2 c_p
          (1-log p/L)
          cos(tau log p).

This is a major simplification.

The second-order current covariance is now built only from products of one
sine/cosine frequency per prime.

## 6. Exact difference/sum frequency split at the scalar-field level

For y_p=log p,

    alpha_p(tau_i) alpha_p(tau_j)

      = c_p^2/2 [
          cos((tau_i-tau_j)y_p)
          - cos((tau_i+tau_j)y_p)
        ],

and analogous product-to-sum identities hold for

    alpha_p beta_p,
    beta_p beta_p.

Therefore every D2 scalar covariance kernel splits exactly into:

1. **difference-frequency terms**
       depending on tau_i-tau_j,
       with the height carrier T cancelled;

2. **sum-frequency terms**
       depending on tau_i+tau_j,
       carrying frequency approximately 2T.

This is the scalar Loewner version of the previously derived
mixed-sign / same-sign variance split.

## 7. Current theorem state

After this reduction:

D1:
    one subset resolvent state
    + one aggregate remaining scalar polynomial Q_rem,S.

D2:
    ordinary primes only
    + explicit sine/cosine current fields
    + rank-three / one-dimensional Fourier reconstruction.

No proper-prime-power covariance theorem remains in D2.

The next analytic attack should therefore treat separately:

    D2-difference:
      square-prime Mertens / continuum overlap channel;

    D2-sum:
      carrier-2T compressed trace channel;

while D1 uses the aggregate remaining polynomial and the prime-base
near-resonance firewall.

See:

    notes/WP84_BR_RANK3_SCALAR_D1.md
    notes/WP84_VARIANCE_CHANNEL_SPLIT.md
    notes/WP84_FOUR_POLE_INEQUALITY_KILL_GATE.md
