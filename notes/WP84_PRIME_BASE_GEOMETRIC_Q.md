# WP84 — exact prime-base Dirichlet block and prime-only variance reduction

Date: 2026-10-05

Status: **CURRENT PRIME-BASE Q_p CLOSED AS A FINITE GEOMETRIC SERIES; PROPER POWERS ARE o(1) IN THE CURRENT D2/VARIANCE SLOT**

No percentage theorem is claimed here.

Prime-base grouping is the correct Lindeberg decomposition because it removes
all exact current-base resonances.  The grouped current block is also much
more explicit than a generic sum of prime powers.

## 1. Exact scalar Q_p

In sharp hat normalization the positive prime-power coefficient is

    - Lambda(n)/(a L sqrt(n)),

with the carrier included in exp(i tau log n).

For one prime base p put

    M_p = floor(L/log p),

so p^m<=X=e^L iff 1<=m<=M_p.

Define

    z_p(tau)
      = p^(-1/2) exp(i tau log p).

Then the entire grouped scalar Dirichlet polynomial is exactly

    boxed:
    Q_p(tau)
      = -(log p)/(a L)
          sum_{m=1}^{M_p} z_p(tau)^m

      = -(log p)/(a L)
          z_p(tau)
          [1-z_p(tau)^(M_p)]/[1-z_p(tau)].

Because

    |z_p|=p^(-1/2)<=2^(-1/2),

the denominator is uniformly bounded away from zero.

Thus the current scalar fields

    alpha_p = Im Q_p,

    beta_p
      = 2 Re Q_p - 2(Im Q_p)'/L

are explicit finite-geometric functions of one phase exp(i tau log p).

## 2. Exact derivative

Writing z=z_p(tau),

    d/dtau z^m
      = i m log(p) z^m.

Therefore

    Q_p'(tau)
      = -i (log p)^2/(a L)
          sum_{m=1}^{M_p} m z^m.

The finite arithmetico-geometric sum is

    sum_{m=1}^M m z^m
      = z[1-(M+1)z^M+M z^(M+1)]/(1-z)^2.

So beta_p requires no numerical differentiation and no separate
prime-power loop.

## 3. Uniform grouped-block scale

The exact geometric series immediately gives

    |Q_p(tau)|
      <= (log p)/(a L)
          * 1/(sqrt(p)-1).

This is the scalar counterpart of the grouped operator bound

    ||G_p||
      <= (4 log p/L)/(sqrt(p)-1).

## 4. Split ordinary prime from proper powers

Write

    G_p = B_p + H_p,

where B_p is the p^1 block and

    H_p = sum_{m>=2,p^m<=X} B_{p^m}.

The existing one-block norm gives

    ||B_p||
      <= 4 log p/(L sqrt p),

and the geometric tail gives

    boxed:
    ||H_p||
      <= (4 log p/L)
          * [1/p]/[1-p^(-1/2)].

## 5. Proper powers disappear from the current variance slot

For any matrix A,

    G_p A G_p - B_p A B_p
      = B_p A H_p
        + H_p A B_p
        + H_p A H_p.

Hence

    ||G_p A G_p - B_p A B_p||
      <= ||A||
          [2||B_p||||H_p||+||H_p||^2].

Summing over p,

    sum_p ||B_p||||H_p||
      <= C/L^2
          sum_p (log p)^2/p^(3/2),

and

    sum_p ||H_p||^2
      <= C/L^2
          sum_p (log p)^2/p^2.

Both prime series converge absolutely.

Therefore

    boxed:
    sum_p
      ||G_p A G_p-B_p A B_p||
      = O(||A||/L^2)
      = o(1)

uniformly for bounded A.

At every fixed nonreal pole, ||R||<=1/eta.  Thus the accumulated
second-order Lindeberg term satisfies

    sum_p [
      tau(R G_p R G_p R)
      - tau(R B_p R B_p R)
    ]
      = O_eta(L^-2)

when the intermediate state R is held fixed and p remains excluded.

So the **current block in D2 may be replaced by the ordinary-prime block**
with o(1) total error.

## 6. Important asymmetry with D1

The same absolute argument does not delete H_p from the current first-order
slot, because

    sum_p ||H_p||

is not o(1) under the crude norm bound.

Therefore:

- D2 current slot: ordinary primes only, up to o(1);
- D1 current slot: retain the exact grouped geometric Q_p unless a separate
  oscillatory theorem removes the proper-power drift.

This distinction is fail-closed and should be preserved.

## 7. Consequence for the rank-three formulas

For D2 one may now set, up to o(1),

    alpha_p(tau)
      = -(log p)/(a L sqrt p)
          sin(tau log p),

with the corresponding exact beta_p from the single p block.

Thus the current response

    w_p=R alpha_p

is a resolvent response to one sinusoidal Fourier vector, and the rank-three
channel is averaged against the square-prime measure

    (log p)^2/p.

That is exactly the measure already controlled by the
Chebyshev--Mertens input.

The hard noncommutative memory remains in R; the current arithmetic is no
longer a prime-power combinatorial object.

See:

    notes/WP84_BR_RANK3_SCALAR_D1.md
    notes/WP84_BERNOULLI_PERMUTATION_BRIDGE.md
    notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md
