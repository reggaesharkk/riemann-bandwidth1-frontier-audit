# Cross-project method transfer audit — LRSC / VRK / Navier–Stokes -> Riemann

Date: 2026-10-04
Status: METHOD TRANSFER ONLY; no cross-domain theorem import

## Purpose

The other research programmes contain useful proof-engineering methods. Those
methods may be transferred to the Riemann programme, but mathematical
conclusions from another model are never treated as zeta inputs.

Method transfer is not theorem transfer.

## LRSC K10/K11 material inspected

The frozen LRSC structural-mechanism certificate records a locked finite
benchmark, rigorous interval coefficient enclosures, best-first
branch-and-bound with continuous weak-duality node bounds, certified exclusion
of all subsets of size at most 10, and an explicit passing K=11 witness.

The later reproducibility / VRK layer adds exact coverage counters,
independent reconstruction paths, hash-bound evidence, and fail-closed checks
for capped or unresolved branches.

The value K=11 itself is irrelevant to zeta and is not imported.

## Transfers adopted here

1. Coverage is a proof obligation. The new {5,2} certificate has exactly
   3 x 150 = 450 primitive exact rational work units. Missing or duplicate
   units are fatal.

2. Deterministic evidence digest. Canonically sorted primitive rows are hashed,
   so laptop, Colab, or any later public runner can be compared byte-for-byte
   at the evidence level.

3. Witness/exclusion separation. A large consumer coefficient is a witness on
   the consumer side. It does not establish that zeta supplies the assumed
   moments. The analytic transport remains a separate gate.

4. Outward intervals only where exact rationals stop. Connected polytope
   constants stay Fraction-exact whenever possible. Sign-critical numerical
   leftovers must be outward enclosed, not fitted.

5. Claim firewall. Exact C7, exact {5,2}, finite-height diagnostics, and exact
   Christoffel algebra retain separate evidence grades.

Implemented now:
- src/wp81_spec52_shard_plan.py
- src/wp81_spec52_verify.py

## Navier–Stokes method transfer

The useful transfer is the signed-decomposition audit style: preserve the main
term and bound only a certified remainder. This matches the current G9 rule

    w_k(n) = M_k(n) + e_k(n).

The Navier–Stokes results and constants themselves are not zeta inputs.

## Explicitly not transferred

No LRSC rank/compression value, K10/K11 numeric threshold, odd-ring identity,
Navier–Stokes finite-Galerkin constant, or physical interpretation is used as
a Riemann premise.

## Resulting proof-carrying pipeline

locked specification
 -> deterministic shards
 -> primitive exact evidence
 -> exact coverage verifier
 -> deterministic digest
 -> independent replay
 -> analytic transport
 -> theorem promotion only after every gate closes
