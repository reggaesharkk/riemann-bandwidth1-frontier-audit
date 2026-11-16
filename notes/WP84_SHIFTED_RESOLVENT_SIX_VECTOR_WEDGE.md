# WP84 — shifted frontier energy as a six-vector Hankel wedge

Date: 2026-10-06

Status: **EXACT FINITE-MATRIX FACTORIZATION; COUPLED POSITIVE SIX-CHANNEL ENERGY; NO LARGE-T THEOREM CLAIMED**

This note makes the rank-six displacement structure of the shifted exact-frontier consumer explicit in resolvent coordinates. It is an algebraic reduction only. It does not establish a permutation-averaged or large-\(T\) estimate for the arithmetic matrices.

## 1. Setup

Let
[
z=\frac45(1+i),\qquad r^2=|z|^2=\frac{32}{25},\qquad
P(x)=1-Ax+Bx^2-Cx^3,
]
where
[
A=\frac{43428}{13891},\quad B=\frac{37704}{13891},\quad C=\frac{9660}{13891}.
]
For a real symmetric sharp Loewner matrix (H), set
[
R=(H-zI)^{-1},\qquad Q_s=r^3P(H)R^3.
]
Then (Q_s^*Q_s=p_s(H)), as in the shifted-consumer certificate.

Write (p_0=1,p_1=-A,p_2=B,p_3=-C). Since (H=zI+R^{-1}), exact polynomial division gives
[
P(H)R^3=b_0I+b_1R+b_2R^2+b_3R^3,
]
where
[
b_0=p_3,quad
b_1=3zp_3+p_2,quad
b_2=3z^2p_3+2zp_2+p_1,quad
b_3=P(z).
]
The (b_0I) term commutes with (D), so it contributes nothing to the displacement.

## 2. Six-vector factorization

For the sharp displacement law
[
[D,H]=\frac1\pi(\mathbf1\alpha^T-\alpha\mathbf1^T),
]
the resolvent identity is
[
[D,R^k]=-R^k[D,H]R-\cdots-R[D,H]R^k.
]
Equivalently, with (u_j=R^j\mathbf1) and (v_j=R^j\alpha),
[
[D,R^k]=-\frac1\pi\sum_{j=1}^k
(u_jv_{k+1-j}^T-v_ju_{k+1-j}^T).
]

Put
[
U=[u_1 u_2 u_3],\qquad V=[v_1 v_2 v_3],
]
and define the exact (3\times3) Hankel-triangular coefficient matrix
[
M=\begin{pmatrix}
b_1&b_2&b_3\\
b_2&b_3&0\\
b_3&0&0
\end{pmatrix}.
]
Summing the (k=1,2,3) formulas yields the identity
[
\boxed{
[D,Q_s]=-\frac{r^3}{\pi}
\left(UMV^T-VMU^T\right).
}
]
This is a coupled wedge/Gram representation, not six independent rank-two errors. In block form its middle skew matrix acts on only the six columns of ([U V]); hence
[
\operatorname{rank}[D,Q_s]\le6.
]
It also identifies the precise six resolvent vectors that any later probabilistic or arithmetic limit must control.

## 3. Exact positive-energy representation

For (i\ne j), ([D,Q_s]_{ij}=(i-j)(Q_s)_{ij}). Therefore
[
\boxed{
\tau(Q_s^*Q_s)
=\frac1d\sum_i|(Q_s)_{ii}|^2
+\frac{r^6}{\pi^2d}\sum_{i\ne j}
\frac{|(UMV^T-VMU^T)_{ij}|^2}{(i-j)^2}.
}
]
The second term is a positive (K_2)-weighted squared norm of one Hankel-weighted wedge. Keeping it grouped preserves all cross-cancellation among the six columns. Applying separate triangle inequalities to the six wedges would discard exactly that structure.

A useful implementation form is
[
\mathcal L(K)=\sum_{i\ne j}\frac{|K_{ij}|^2}{(i-j)^2},
\qquad K=UMV^T-VMU^T,
]
so the full energy is the diagonal term plus (r^6\mathcal L(K)/(\pi^2d)). This is a deterministic finite-dimensional state, not yet a bound uniform in the zeta height.

## 4. Regression and evidence boundary

The companion script
`src/wp84_shifted_resolvent_wedge_gate.py` constructs a finite real symmetric matrix with the exact rank-two sharp displacement form, evaluates (Q_s) directly, and independently evaluates the six-vector factorization. It also checks the diagonal-plus-displacement positive-energy identity.

The deterministic floating-point replay passes with maximum commutator residual below (5\times10^{-15}) and energy-identity residual below (3\times10^{-16}) in the recorded run. This is an implementation regression only; the identities above follow algebraically and do not rely on that numerical tolerance.

Closed here:
- exact conversion of (P(H)R^3) to a cubic in (R);
- exact Hankel coefficient matrix (M);
- exact six-vector wedge factorization;
- exact positive (K_2)-energy identity.

Still open:
- a theorem-grade large-(T) bound for the diagonal term and the coupled (K_2)-weighted wedge statistic;
- transfer of its limit to the actual sharp prime state and all background/taper/counting corrections.

No (>79\%) or (79.62709668\%\) unconditional zero theorem is claimed.
