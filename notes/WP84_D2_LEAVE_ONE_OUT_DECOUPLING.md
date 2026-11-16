# WP84 — D2 leave-one-out decoupling from the permutation state

Date: 2026-10-05

Status: **SECOND-ORDER CURRENT BLOCK DECOUPLES FROM THE SUBSET STATE WITH o(1) TOTAL ERROR; FULL D2 PATH USES ONE DETERMINISTIC VARIANCE MAP**

No percentage theorem is claimed here.

The permutation-Lindeberg representation has, at stage k,

    S = k already-inserted prime-base groups,

    p = next current prime base, p notin S,

and the second-order scalar

    F(S,p;z)
      = tau(
          R_S G_p
          R_S G_p
          R_S
        ).

The current p and the state S are not independent because p is excluded from
S.

For D2 this dependence is asymptotically removable.  The reason is exactly
the infinitesimal-block cube-mass estimate.

## 1. Exact sampling representation

Let M be the number of retained prime bases.

The joint law at stage k is equivalently:

1. choose p uniformly from {1,...,M};
2. choose S uniformly among k-subsets of the other M-1 indices.

Now construct S0, a uniform k-subset of all M indices, as follows.

With probability

    1-k/M,

set

    S0=S.

With probability

    k/M,

choose q uniformly from S and set

    S0=(S\{q}) union {p}.

A direct counting check shows that S0 is uniform over all k-subsets of
{1,...,M}.

Moreover p and S0 have the product law:

    p uniform,
    S0 uniform k-subset,

when S0 is generated independently instead.

The coupling above compares the actual exclusion law with that product law.

## 2. One swap changes the state by one infinitesimal difference

When S0 differs from S,

    H_{S0}-H_S = G_p-G_q.

For nonreal z with

    eta=|Im z|,

the resolvent identity gives

    ||R_{S0}-R_S||op
      <= eta^(-2)
          (||G_p||+||G_q||).

The cubic D2 functional is Lipschitz in the resolvent:

    |F(S,p;z)-F(S0,p;z)|

      <= C_eta
          ||G_p||^2
          (||G_p||+||G_q||),

with, for example,

    C_eta=3 eta^(-4)

up to an inessential larger fixed constant from replacing intermediate
resolvents by the uniform eta^(-1) bound.

Only the scaling matters below.

## 3. Averaged one-stage coupling error

Write

    b_p=||G_p||op.

Under the coupling,

    E b_p^3
      = M^(-1) sum_p b_p^3,

while the mixed term obeys

    E b_p^2 b_q
      <=
      [M^(-1) sum_p b_p^2]
      [ (M-1)^(-1) sum_q b_q ]

up to the harmless distinct-index correction.

The established prime-base bounds give

    sum_p b_p^2 = O(1),

    sum_p b_p^3 = O(L^-3),

and elementary Chebyshev/partial summation gives

    sum_p b_p = O(sqrt(X)/L).

Also

    M=pi(X)
      asymp X/L

at the coarse scale needed here.

Hence one stage costs

    O_eta(
      L^-3/M
      + 1/(M sqrt(X))
    ).

## 4. The entire M-stage D2 path decouples

There are M stages.

Summing the previous bound over k gives

    boxed:
    total D2 exclusion-coupling error

      = O_eta(
          L^-3
          + X^(-1/2)
        )
      = o(1).

This estimate is uniform in the stage fraction k/M and in every fixed
nonreal pole set.

Therefore the condition

    p notin S

may be removed from the D2 theorem at o(1) total cost.

This is a second-order leave-one-out theorem.

## 5. Deterministic full variance map

After decoupling, take

    p uniform in {1,...,M}

independently of a uniform k-subset S0.

Then

    E_p F(S0,p;z)

      = 1/M
        sum_p
          tau(
            R_{S0} G_p
            R_{S0} G_p
            R_{S0}
          )

      = 1/M
        tau(
          R_{S0}
          V(R_{S0})
          R_{S0}
        ),

where the deterministic full variance map is

    boxed:
    V(A)
      = sum_p G_p A G_p.

Consequently the complete second-order contribution is

    boxed:
    A2(z)
      =
      1/M
      sum_{k=0}^{M-1}
        E_{S_k}
          tau(
            R_{S_k}
            V(R_{S_k})
            R_{S_k}
          )
      + o(1),

with S_k now simply a uniform k-subset.

The current prime variable has disappeared.

## 6. Combine with proper-power removal

The companion reduction proved

    V(A)
      =
      sum_p B_p A B_p
      + o(1)

inside the bounded D2 trace, where B_p is the ordinary-prime first-power
block.

Thus the deterministic variance map needed by the whole path is, to o(1),

    boxed:
    V_prime(A)
      = sum_{p<=X} B_p A B_p.

This map has the exact difference/sum-frequency split:

    V_prime
      = V_res + V_fast.

So D2 is no longer a subset-dependent arithmetic covariance.

The only subset dependence left in D2 is through the bounded resolvent
R_{S_k} on which one deterministic map acts.

## 7. Why D1 does not admit the same free decoupling

The analogous leave-one-out replacement in the first-order term carries only
one factor b_p.

Its state-swap error is therefore quadratic,

    O_eta(
      b_p(b_p+b_q)
    ),

whose M-stage sum is not forced to vanish by the cube-mass ledger.

So this note is deliberately **D2-only**.

D1 remains the aggregate remaining-polynomial problem from

    WP84_D1_AGGREGATE_D2_PRIME_ONLY.md.

## 8. New D2 frontier

The second-order theorem has now reduced to:

1. one deterministic ordinary-prime variance map V_prime;
2. its resonant/difference-frequency part V_res;
3. its carrier-2T part V_fast;
4. the random-subset resolvent distribution, with no current-prime exclusion
   correlation.

The next target is to compute V_res explicitly on arbitrary matrices using
the scalar alpha/beta covariance kernels and then isolate V_fast as the sole
non-Mertens variance obstruction.

See:

    notes/WP84_D1_AGGREGATE_D2_PRIME_ONLY.md
    notes/WP84_VARIANCE_CHANNEL_SPLIT.md
    notes/WP84_FOUR_POLE_INEQUALITY_KILL_GATE.md
