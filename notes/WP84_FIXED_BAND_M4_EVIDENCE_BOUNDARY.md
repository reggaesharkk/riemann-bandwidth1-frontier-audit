# WP84 — fixed-band fourth-moment evidence boundary

Date: 2026-10-05

Status: **CORRECTION — FIXED MATRIX BANDWIDTH DOES NOT BY ITSELF MAKE THE RAW FOURTH MOMENT ROUTINE**

No unconditional zero-density percentage is claimed here.

The quartic reduction is algebraically valid, but its interpretation needs a strict boundary.

For the sharp fixed-band matrix

    H_R=M_beta+[M_alpha,J_R],

the diagonal field beta is unchanged by truncating matrix displacement.  Therefore the full retained prime Dirichlet polynomial is still present on the diagonal.

If P_R denotes the centered fixed-band prime matrix, then for a real-symmetric matrix

    tau(P_R^4)=d^(-1)||P_R^2||_F^2.

Since

    (P_R^2)_ii=beta_i^2+sum_{j!=i}(P_R)_ij^2 >= beta_i^2,

we have the deterministic lower bound

    boxed:
    tau(P_R^4) >= d^(-1) sum_i beta_i^4.

Thus fixed off-diagonal bandwidth does not control amplitude tails of the prime field.  The balanced 2-vs-2 near-product-collision problem can survive entirely through the diagonal beta contribution.

Consequently the statement

    tau(P_R^4) < W_R

remains a genuine arithmetic theorem target.  The new pointwise sign C4<=0 and the exact R=400 pair layer make this target much narrower, but they do not prove it automatically.

Large alpha/beta sites may be removed by small rank for a bounded resolvent consumer.  They may not be silently removed and then sent to infinity inside an unbounded quartic polynomial without an additional uniform-integrability theorem.

Therefore the safe route ordering is:

1. matched rational rank-four route — bounded throughout;
2. degree-3 / integer Cayley route — bounded throughout;
3. quartic fixed-band route — conditional fallback requiring a genuine one-sided fourth-moment theorem.

For Route 3, the current sharp scalar target at R=400 is

    tau(P_R^4) < 0.2911227517...,

and the exact pair calculation gives

    Pair_400 < 0.266329.

Together with C4<=0 on exact closed cycles, this leaves roughly 0.02479 for positive nonclosed / finite-compression leakage.  Bounding that leakage is the actual remaining arithmetic problem.

The Evans almost-prime theorem remains relevant in the long-shift regime, but its almost-all-h L2 corollary cannot simply be inserted into the WP84 trace sum: a naive Cauchy--Schwarz step can lose the full shift length H.  The correct source interface should work at the weighted circle-method / local minor-arc level.

See:

    notes/WP84_CENTERED_M4_SCALAR_GATE.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
    notes/WP84_ONE_CAYLEY_RATIONAL_RANK4.md
