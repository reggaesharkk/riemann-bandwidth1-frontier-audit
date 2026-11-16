# WP84 — order-four V-sum resonance is proper-prime-power suppressed

Date: 2026-10-05

Status: **ORDER-4 SAME-SIGN PRIME SECTOR REDUCED TO ABSOLUTELY SUMMABLE PROPER-POWER RESONANCES**

The exact noncommuting witness shows that V-sum cannot be discarded for an
arbitrary intermediate matrix.

The actual permutation path has additional structure: the current block is
not among the previously inserted blocks, and sharp translation traces obey
an exact displacement-closure rule.

At order four this changes the conclusion substantially.

## 1. Trace closure becomes multiplicative resonance

For a sharp prime-power block n, each complex branch shifts physical position
by

    +/- log n / L.

A product of non-cyclic partial shifts has zero trace unless the total signed
displacement is zero.

Exponentiating the closure condition gives an exact multiplicative relation
among the participating prime powers.

Unique factorization then enforces exponent balance separately at every prime.

## 2. Current prime block, same-sign insertion

Take the current block to be a prime p.

The V-sum branch inserts it twice with the same sign, contributing p-exponent

    +2

or -2.

At theta^4 there are exactly two previous block occurrences.

Because the current block p is excluded from the previous subset, any previous
block with prime base p has exponent at least 2:

    p^b, p^c,
    b,c>=2.

For the +,+ current branch the closure equation is

    2 + eps1 b + eps2 c = 0,
    eps1,eps2 in {+1,-1}.

The complete solution pattern is

    boxed:
    |b-c|=2.

Therefore

    b+c>=6.

So every order-four same-sign resonance for a current prime necessarily uses
two **proper prime powers** of the same prime base.

No ordinary distinct-prime pair can contribute.

Companion checker:

    src/wp84_order4_vsum_prime_resonance.py

## 3. Absolute size

The block norm scale is

    ||B_{p^a}||
      << log p / (L p^(a/2)).

The two current prime insertions contribute

    << (log p)^2/(L^2 p).

A resonant previous pair contributes, because b+c>=6,

    << (log p)^2/(L^2 p^3).

Hence the complete resonant order-four weight is

    << (log p)^4/(L^4 p^4).

Summing over primes converges absolutely:

    sum_p (log p)^4/p^4 < infinity.

Thus the current-prime V-sum sector at order four is

    O(L^-4).

## 4. Current proper-prime-power blocks

If the current block itself is p^a with a>=2, its total square-mass sector is

    sum_{p,a>=2}
      (log p)^2/(L^2 p^a)
      = O(L^-2).

So current proper powers are already negligible in the variance ledger.

Combining both cases gives:

    boxed:
    order-four V-sum = o(1)

in the sharp retained-range word expansion.

This uses only unique factorization and absolute convergence of proper-power
weights; no prime-pair theorem is involved.

## 5. Consequence for the 1/4 calibration

The crossing pair repair

    t_opp=1/30

cannot be assigned to the order-four V-sum sector.

At order four it must be carried by the mixed-sign D2 geometry and/or the
first-order evolving state.

Likewise the connected

    Phi4=-1/60

must come from the non-pair state dependence of those surviving sectors.

This narrows the provenance calculation considerably.

## 6. Evidence boundary

This note closes only the fixed degree-four same-sign sector.

At unrestricted resolvent degree, a current prime can resonate with longer
previous words containing proper powers plus internally cancelling pairs.
A full bounded-resolvent V-sum theorem still requires summing those longer
resonance families or another functional-calculus argument.

No unconditional >79 theorem is claimed.
