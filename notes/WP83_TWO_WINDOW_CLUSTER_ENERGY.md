# WP83 — two-window cluster-energy target and exact confluent floor

Date: 2026-10-04
Status: **NAIVE RAW-COLUMN TWO-WINDOW FLOOR FALSIFIED; CONFLUENT CLUSTER FLOOR DERIVED FOR CLUSTERS OF SIZE <=4; BACKGROUND ISOLATION STILL OPEN**

The successor retraction mentions a later 'two-window cluster-energy floor theorem'. No public document containing that theorem was located, so this note reconstructs the strongest statement justified by the present Gabor structure.

## 1. Exact joint two-window matrix

For two finite Gabor observations A and B of the same zero cluster C={z_1,...,z_s}, let

    V_A = [u_A(z_1) ... u_A(z_s)],
    V_B = [u_B(z_1) ... u_B(z_s)].

The stacked observation operator is

    V_AB = [ V_A ; V_B ],

and its cluster Gram is exactly

    boxed:
    G_AB = V_AB* V_AB
         = V_A*V_A + V_B*V_B.

Thus the best possible raw-coefficient energy floor is lambda_min(G_AB).

At lambda=1 the row count 2d exceeds N(T,2T) for large T, so two windows remove the **dimension-count obstruction**. They do not by themselves give conditioning.

## 2. Falsifier: no separation-free raw-column floor from any fixed finite number of analytic windows

Let U(z) denote the stacked evaluation vector for any fixed finite collection of windows. U is analytic in z.

For two distinct points z and z+eps choose coefficients (1,-1). Then

    U(z+eps)-U(z) = eps U'(z) + O(eps^2).

Hence

    ||U(z+eps)-U(z)||^2 = O(|eps|^2),

while the coefficient norm stays equal to 2.

Therefore

    boxed:
    lambda_min([U(z),U(z+eps)]*[U(z),U(z+eps)])
      = O(|eps|^2) -> 0.

So infinite-lattice injectivity does **not** imply the raw bound

    ||sum c_j U(z_j)||^2 >= T^(-o(1)) sum |c_j|^2

without a zero-spacing hypothesis.

This directly corrects the tempting but invalid version of the two-window argument.

## 3. Correct near-collision coordinates: confluent jets

When nodes collide, replace the raw node basis by the confluent jet basis at a cluster center z0:

    J_r(z0) = (1/r!) d^r/dz^r u(z)|_{z=z0},
    r=0,...,s-1.

Under the paper Fourier convention, J_r is the Fourier-coefficient sequence of

    phi(t) * (i t)^r/r! * exp(i(z0-T)t).

More generally, after a triangular change of basis we may use centered monomials

    phi(t) * (t-a)^r * exp(i(z0-T)t),

which is better conditioned near an interior subinterval.

Distinct confluent exponentials are linearly independent on the full lattice. This extends `WP83_INFINITE_EVAL_INDEPENDENCE.md` from distinct nodes to colliding clusters with multiplicity.

## 4. Exact unit-interval floor

Choose the unit interval at the right end of the flat core

    I0=[a,a+1],
    a=L/2-w-1,

which lies where phi=1 once L>=4(w+1).

For an off-line depth delta>0, the full-lattice Gram of the centered jet functions dominates

    L * exp(2 delta a) * H_s,

where

    (H_s)_{r,t} = integral_0^1 x^(r+t) dx
                = 1/(r+t+1)

is the s x s Hilbert matrix.

Therefore

    lambda_min(G_jet)
      >= L exp(2 delta a) lambda_min(H_s).

To obtain a fully rational certificate, use

    lambda_min(H_s)
      >= det(H_s) / tr(H_s)^(s-1).

For s<=4 the exact certified floors are

| cluster size s | rational c_s with lambda_min(H_s)>=c_s |
|---:|---:|
| 1 | 1 |
| 2 | 1/16 |
| 3 | 5/25392 |
| 4 | 49/1395654656 |

Thus for every confluent cluster of size at most four,

    boxed:
    lambda_min(G_jet)
      >= c_s * L * exp(delta L - 2 delta(w+1)).

For fixed w and fixed depth delta>=delta0>0, this is

    >= C(delta0,w,s) * L * X^delta.

The constant c_4=49/1395654656 is small but exact and strictly positive.

Companion exact checker: `src/wp83_cluster_hilbert_floor.py`.

## 5. Finite-section transfer

The derivative/centered-jet windows are still C^2 and compactly supported. For fixed s<=4, their Fourier tails inherit the same |frequency|^-2 decay with constants growing only by fixed powers of L.

Placing the cluster in the interior as in `WP83_FINITE_PAIR_CAPTURE.md` therefore gives

    G_jet,finite = G_jet,infinite + error,

with

    ||error|| / lambda_min(G_jet,infinite) -> 0

at a power of T times fixed powers of log T.

So the finite compressed section retains the confluent cluster floor for every fixed-depth cluster of size <=4.

This transfer is an analytic write-out and still needs a fully explicit constant ledger or formal check.

## 6. What two windows can legitimately do

Two windows are useful for coverage and background isolation:

- their stacked row count removes the one-window dimension obstruction;
- overlapping height placements can ensure every target cluster is interior in at least one observation;
- the combined Gram is the sum G_A+G_B, so energy missed by one section may be captured by the other.

But two windows **cannot** cure raw near-collision conditioning. The cluster must first be represented in confluent/divided-difference coordinates.

## 7. Remaining Proposition-R gate

We now have a quantitative floor for the internal energy of a size<=4 cluster in the correct confluent coordinates.

What is still missing is a theorem comparing that cluster energy against the span/contribution of all other clusters:

    sigma_min(P_perp V_cluster,finite)
      >= X^(delta/2) / polylog(T)

or an equivalent energy-counting inequality.

That is the genuine two-window **background-isolation** problem.

## 8. Strategic consequence

The retraction's phrase 'unconditional <=4-cluster form' is now mathematically suggestive: size four is exactly small enough for a finite confluent moment matrix whose floor can be certified explicitly with the 4x4 Hilbert minor above.

This does not prove that the authors' unreleased theorem used this mechanism, and the repo must not claim that attribution. It gives us an independent, source-compatible route to test.
