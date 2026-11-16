# WP84 — exact Bernoulliization of the permutation-Lindeberg path

Date: 2026-10-05

Status: **EXACT COMBINATORIAL REDUCTION CLOSED; FIXED-CARDINALITY SUBSET AVERAGE REPLACED BY ONE SCALAR t AND INDEPENDENT PRIME MASKS**

No percentage theorem is claimed here.

The permutation symmetrization introduced earlier is exact but awkward:
at step s+1 the previous set is a uniformly random s-element subset and the
current prime-base group is a uniformly random element of its complement.

There is an exact continuous representation of the same average using
independent Bernoulli masks.

## 1. Permutation weight

Let there be M prime-base groups.

For any function F(S,j) defined whenever j is not in S, the permutation sum is

    A_perm
      = E_pi sum_{s=0}^{M-1}
          F(S_s(pi), pi(s+1)),

where S_s(pi) is the set of the first s elements.

Fix one pair (S,j) with |S|=s and j not in S.

The probability that a random permutation has exactly S first, in any order,
followed by j is

    s! (M-s-1)! / M!
      = 1/[M * C(M-1,s)].

Therefore

    A_perm
      = sum_j sum_{S subset [M]\{j}}
          F(S,j)
          s!(M-s-1)!/M!.

## 2. Beta integral

The beta identity gives

    int_0^1 t^s (1-t)^(M-1-s) dt
      = s!(M-s-1)!/M!.

Now, for fixed j and fixed t, let S_t^(j) include each q!=j
independently with probability t.

Then

    P(S_t^(j)=S)
      = t^s(1-t)^(M-1-s).

Substituting the beta integral yields the exact identity

    boxed:
    A_perm
      = sum_{j=1}^M
          int_0^1
            E_t[
              F(S_t^(j),j)
            ] dt.

There is no approximation and no large-M limit here.

## 3. Exact Bernoulli bridge for the resolvent

Let the current group be G_p and define

    H_{t,-p}
      = S0 + sum_{q!=p} xi_q(t) G_q,

where the xi_q(t) are independent Bernoulli(t).

Then the two surviving permutation-Lindeberg terms may be written exactly as

    A1(z)
      = sum_p int_0^1
          E[
            tau(
              R_{t,-p} G_p R_{t,-p}
            )
          ] dt,

    A2(z)
      = sum_p int_0^1
          E[
            tau(
              R_{t,-p} G_p
              R_{t,-p} G_p
              R_{t,-p}
            )
          ] dt,

up to the same signs used in the one-block resolvent expansion.

Here

    R_{t,-p}
      =(H_{t,-p}-zI)^(-1).

The current prime base p remains excluded from the state.  Therefore the
prime-base valuation firewall is preserved exactly.

## 4. Scalar Dirichlet-polynomial state

Because subset states add linearly at the Q-level,

    Q_{t,-p}(tau)
      = sum_{q!=p}
          xi_q(t) Q_q(tau).

Thus the random state is one scalar analytic function built from
**independent prime-base masks**.

The exact Loewner formula becomes

    H_{t,-p}
      = background
        + M_{2 Re Q_{t,-p}
             -2(Im Q_{t,-p})'/L}
        + [M_{Im Q_{t,-p}},J].

The large matrix randomness is therefore entirely induced by an independent
random scalar Dirichlet polynomial.

## 5. Exact first and second mask moments

For each fixed tau,

    E Q_{t,-p}(tau)
      = t Q_{-p}(tau),

where

    Q_{-p}=sum_{q!=p}Q_q.

For two spectral points tau,sigma,

    Cov(
      Q_{t,-p}(tau),
      conjugate(Q_{t,-p}(sigma))
    )

is exactly

    boxed:
    t(1-t)
      sum_{q!=p}
        Q_q(tau) conjugate(Q_q(sigma)).

The nonconjugated covariance is likewise

    t(1-t)
      sum_{q!=p}
        Q_q(tau) Q_q(sigma).

Higher centered mask cumulants are single prime-base sums.
For example,

    cum_3
      = t(1-t)(1-2t)
        sum_{q!=p}
          Q_q(tau1)Q_q(tau2)Q_q(tau3).

Thus no combinatorial subset correlation has to be computed separately.

## 6. Relation to the infinitesimal block ledger

The grouped blocks satisfy

    max_p ||G_p|| = O(1/L),

    sum_p ||G_p||^3 = O(L^-3).

Therefore every theorem step that compares smooth fixed-pole functionals
under two coefficient laws with matching first two moments has a natural
dimension-free third-order error budget.

This observation does **not** by itself prove that the Bernoulli state may be
replaced by a Gaussian state in every quantity consumed by the full theorem;
the current-p summation and required uniformities must be checked explicitly.

It does show that such an invariance-principle attack is now structurally
well matched to the exact prime-base decomposition.

## 7. Why this is useful

The active averaging variables have changed from

    random permutation
      + random fixed-cardinality subset
      + random current complement element

to

    one deterministic scalar t in [0,1]
      + independent Bernoulli masks on q!=p
      + deterministic current p.

This preserves the exact current-base exclusion while unlocking:

- independent-variable concentration/invariance tools;
- direct cumulant formulas for Q_{t,-p};
- Chebyshev--Mertens evaluation of the covariance sum;
- prime-base valuation cancellation for the current block;
- the rank-three BR / scalar-D1 formulas.

## 8. Immediate next gate

Insert the rank-three formulas with

    a=Im Q_{t,-p},
    alpha=Im Q_p,

into A1 and A2.

Then classify each surviving scalar Fourier term according to whether its
prime-base average is:

1. exact valuation-zero and therefore killed;
2. square-prime covariance and therefore Chebyshev--Mertens;
3. a finite-compression near resonance;
4. a proper-prime-power remainder.

The Bernoulli bridge should be used before any new large computation, because
it may eliminate the remaining subset combinatorics analytically.

See:

    notes/WP84_BR_RANK3_SCALAR_D1.md
    notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md
    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
