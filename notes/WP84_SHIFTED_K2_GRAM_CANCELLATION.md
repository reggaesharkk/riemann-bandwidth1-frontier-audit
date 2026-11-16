# WP84 — K2 cancellation reduces the wedge Gram to resolvent Hilbert–Schmidt data

Date: 2026-10-06

Status: **EXACT FINITE-d CANCELLATION AND STIELTJES REPRESENTATION; HEAT-CURVATURE BOUND OPEN**

This note audits whether the shifted wedge requires a new joint local law for the six vectors (U,V). It does not.

## 1. The displacement denominator cancels

For (R=(H-zI)^{-1}), let (W_k=-\pi[D,R^k]), so
[
(W_k)_{ij}=-\pi(i-j)(R^k)_{ij},\qquad i\ne j.
]
The (K_2)-weighted Gram introduced in
`WP84_SHIFTED_THREE_CHANNEL_GRAM.md` is
[
G_{k\ell}=\sum_{i\ne j}\frac{\overline{(W_k)_{ij}}(W_\ell)_{ij}}{(i-j)^2}
=\pi^2\sum_{i\ne j}\overline{(R^k)_{ij}}(R^\ell)_{ij}.
]
Thus the apparent long-range kernel disappears exactly after using the resolvent displacement identity. No approximation or limit is involved.

Define the normalized off-diagonal Gram (widehat G=G/(\pi^2d)). Then
[
\boxed{
\widehat G_{k\ell}
=\tau((R^k)^*R^\ell)
-\frac1d\sum_i\overline{(R^k)_{ii}}(R^\ell)_{ii}.
}
]
The first term is scalar resolvent data. The second is the diagonal resolvent-product statistic. Both are still state-dependent.

## 2. The full-trace term is a mixed Stieltjes derivative

Write (R_z=(H-zI)^{-1}), and regard (z,ar z) as independent variables when differentiating. Since (H) is Hermitian,
[
S(z,\bar z)=\tau(R_zR_{\bar z})
=\frac{m(z)-m(\bar z)}{z-\bar z},
\qquad m(z)=\tau(R_z).
]
For (k,\ell\ge1),
[
\boxed{
\tau((R_z^k)^*R_z^\ell)
=\frac{\partial_{\bar z}^{\,k-1}\partial_z^{\,\ell-1}S(z,\bar z)}
{(k-1)!(\ell-1)!}.
}
]
Therefore all nine full-trace components of the (3\times3) Gram are determined by the one-point Stieltjes transform and its mixed derivatives. A separate six-vector joint distribution is not needed for those components.

The diagonal subtraction remains a distinct local statistic. The exact-frontier heat-flow formulation already rewrites the **total** consumer energy as a fixed linear combination of (m(z),m'(z),m''(z)); its unresolved theorem gate is the one-sided integrated heat-curvature estimate and its large-(u) truncation. This cancellation therefore redirects the attack toward that existing scalar interface rather than proving an unnecessary (U,V) cross-moment local law.

## 3. Relation to the positive three-channel contraction

The off-diagonal consumer energy is
[
\frac{r^6}{\pi^2d}b^*Gb
=r^6\,b^*\widehat G b
=\frac{r^6}{d}\sum_{i\ne j}
\left|\sum_{k=1}^3 b_k(R^k)_{ij}\right|^2.
]
This is exactly the off-diagonal Hilbert–Schmidt energy of the nonconstant part of (Q_s/r^3). The diagonal term completes the full positive trace. This is a reorganization of the same observable, not an additional upper bound.

## 4. Regression/evidence boundary

The updated `wp84_shifted_resolvent_wedge_gate.py` checks, on a deterministic finite sharp-Loewner example:
- the exact coefficient and Hankel factorization gates;
- equality of the three-channel (b^*Gb) contraction with the direct weighted wedge;
- the (K_2)-cancellation identity against the off-diagonal resolvent-power Gram;
- the positive-energy identity.

These are finite algebra regressions. They do not establish convergence of the diagonal statistics, a large-(T) local law, or the required integrated heat-curvature inequality.

## Conclusion

A separate theorem controlling every cross-moment of (U,V) is not the smallest target. The remaining analytic gate is the already identified scalar one-point heat-flow inequality, including its uniform tail/truncation and the background, taper, and zero-count transfers. No (>79\%) unconditional theorem is claimed.
