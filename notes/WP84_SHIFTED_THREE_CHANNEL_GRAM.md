# WP84 — three-channel Gram compression of the shifted wedge energy

Date: 2026-10-06

Status: **EXACT POSITIVE THREE-CHANNEL GRAM IDENTITY; LARGE-T GRAM BOUND OPEN**

This is a further compression of the shifted six-vector formula. It groups by resolvent power before estimating anything.

Let (R=(H-zI)^{-1}), (u_j=R^j\mathbf1), (v_j=R^j\alpha), and define the three skew-symmetric channel matrices
[
W_k=\sum_{j=1}^k
\left(u_jv_{k+1-j}^T-v_ju_{k+1-j}^T\right),
\qquad k=1,2,3.
]
The exact rank-two source law gives
[
[D,R^k]=-\frac1\pi W_k.
]
With (b=(b_1,b_2,b_3)^T) from the shifted Hankel coefficient audit,
[
[D,Q_s]=-\frac{r^3}{\pi}\sum_{k=1}^3 b_kW_k.
]

For off-diagonal matrices define the weighted inner product
[
\langle A,B\rangle_{K_2}
=\sum_{i\ne j}\frac{\overline{A_{ij}}B_{ij}}{(i-j)^2}.
]
Its weights are strictly positive, so the (3\times3) channel Gram matrix
[
G_{k\ell}=\langle W_k,W_\ell\rangle_{K_2}
]
is Hermitian positive semidefinite. Consequently the exact energy identity is
[
\boxed{
\tau(Q_s^*Q_s)
=\frac1d\sum_i|(Q_s)_{ii}|^2
+\frac{r^6}{\pi^2d}\,b^*Gb.
}
]
This is the same energy as the six-vector Hankel wedge, expressed as a quadratic form in a fixed three-channel Gram matrix. Every cross-channel phase term remains inside (b^*Gb); no triangle inequality has been used.

The representation makes the next theorem target precise: control the large-(T), heat-time/permutation average of the diagonal energy and the scalar contraction (b^*G_Tb/d). Positivity of (G_T) alone is insufficient. In particular, an eigenvalue bound for (G_T) is useful only if it is sharp enough for the fixed coefficient vector (b), and the entries of (G_T) still depend on the actual resolvent field.

The companion gate checks:
1. the exact rational-complex coefficients of (b) and the invariants of (M);
2. the direct commutator against the six-vector factorization;
3. the equality between the direct (K_2)-weighted commutator energy and (b^*Gb);
4. the diagonal-plus-off-diagonal positive-energy identity.

Those floating finite-matrix checks test implementation on one deterministic sample; the algebraic identities are exact.

Evidence boundary:
- Closed: positive-semidefinite three-channel Gram representation and exact scalar contraction.
- Open: any useful large-(T) upper bound on (b^*G_Tb/d), plus the diagonal term and the established heat-flow/background/taper/counting transfers.

No unconditional (>79\%\) or (79.62709668\%\) zero theorem is claimed.
