# WP70-2C — exact continuum-core geometry: \(C_{\rm core}=-1/48\)

Date: 2026-10-04  
Status: **EXACT RATIONAL GEOMETRY PASS; ANALYTIC BRIDGE STILL SEPARATE**

## New result

The continuum-core constant that the public 79.62 reproduction package evaluates
numerically at approximately

\[
-0.0208\text{ to }-0.0209
\]

has an unexpectedly simple exact leading-geometry value:

\[
\boxed{C_{\rm core}=-\frac1{48}}
=
-0.0208333333333333\ldots
\]

This was not obtained by fitting the public Richardson ladder.

It comes from rewriting each of the twelve oriented overlap-volume terms as a
four-dimensional rational polytope and integrating its first \((\nu-1)\)-moment
exactly.

## Scaled continuum formula

With \(\nu\in[1,2]\) and

\[
\nu-1\le\beta_1,\beta_2\le\frac{\nu}{2},
\]

the scaled overlap volume is

\[
v(p,q,r)
=
\max\!\left(
1-\bigl(\max(0,p,q,r)-\min(0,p,q,r)\bigr),0
\right).
\]

Let \(\bar Q(\nu,\beta_1,\beta_2)\) be the sum of the twelve
orientation/overlap terms produced by the fourth-moment geometry.

The leading continuum limit is

\[
C_{\rm core}
=
-2
\int_1^2
(\nu-1)
\int_{\nu-1}^{\nu/2}
\int_{\nu-1}^{\nu/2}
\bar Q(\nu,\beta_1,\beta_2)
\,d\beta_2\,d\beta_1\,d\nu.
\]

The factors of the large logarithmic scale cancel exactly:
the geometry contributes \(l^3\), the leading spectral mass contributes
\(-l^2(\nu-1)\), and the normalization contributes \(2/l^5\).

Thus the constant is a rational polytope moment; the fitted \(c^*\), finite-\(l\)
edge law, and the numerical Richardson extrapolation do not enter the leading
constant.

## Exact 4D polytope conversion

For one overlap term with affine coordinates \(L_0=0,L_1,L_2,L_3\), introduce
a fourth variable \(s\).  The condition

\[
0\le s\le1-\operatorname{span}(L_0,L_1,L_2,L_3)
\]

is equivalent to the finite rational halfspace system

\[
s+L_i-L_j\le1\qquad(0\le i,j\le3).
\]

Hence the integral of one overlap term against \((\nu-1)\) is simply

\[
\int_P(\nu-1)\,d\nu\,d\beta_1\,d\beta_2\,ds
\]

over a rational four-dimensional polytope \(P\).

The independent checker:

1. enumerates every candidate vertex from four active halfspaces;
2. solves the systems using exact \`Fraction\` Gaussian elimination;
3. checks every vertex against every halfspace exactly;
4. triangulates the convex boundary;
5. recomputes every simplex determinant and affine moment over \(\mathbb Q\);
6. sums the twelve exact contributions.

The twelve weighted moments are

\[
\left(
\frac1{480},0,\frac1{17280},
\frac1{480},\frac1{17280},0,
\frac1{480},\frac1{8640},\frac1{1152},
\frac1{480},\frac1{1152},\frac1{8640}
\right).
\]

They sum to

\[
\boxed{\frac1{96}}.
\]

Therefore

\[
\boxed{
C_{\rm core}
=
-2\cdot\frac1{96}
=
-\frac1{48}.
}
\]

The total unweighted four-dimensional overlap volume is independently

\[
\frac1{16}.
\]

## Consequence for the 70% one-sided route

Keeping the public conservative tail charge

\[
\varepsilon_{\rm tail}\le0.0111=\frac{111}{10000},
\]

the exact leading core would give

\[
\bar R
\le
-\frac1{48}+\frac{111}{10000}
=
\boxed{-\frac{73}{7500}}
=
-0.0097333333\ldots
\]

before any additional bridge/convergence errors.

This is comfortably below the exact 70% threshold

\[
-\frac1{180}
=
-0.005555\ldots
\]

by

\[
\frac{47}{11250}
=
0.004177777\ldots
\]

in \(R\)-units.

Feeding \(\bar R=-73/7500\) into the exact degree-two consumer gives

\[
\boxed{
\frac{N_0^s}{N}
\ge
\frac{1082}{1539}
=
0.7030539311241065\ldots
}
\]

and

\[
\boxed{
\frac{N_d}{N}
\ge
\frac{2621}{3078}
=
0.8515269655620533\ldots
}
\]

**conditional on the remaining analytic bridge being valid with no uncharged
error larger than the displayed margin.**

## Independent reproduction of the public numerical pipeline

Separate GitHub Actions run \`37182113806\` pinned the public source at
\`d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8\` and reran its own quadrature
pipeline from scratch.

It returned

- \(C_{\rm core}\approx-0.02126\);
- public heuristic budget \(B_{\rm total}\approx0.00131\);
- \(C_{\rm core}^{UB}\approx-0.01995\);
- \(\bar R\approx-0.00885\);
- diagnostic simple-zero coefficient \(\approx0.7024\).

This is consistent with the exact \(-1/48\) geometry, but that public
\(B_{\rm total}\) is not treated here as a rigorous enclosure because several
components are Richardson/grid sensitivity estimates.

## Remaining theorem gates

The exact continuum geometry removes the largest numerical-analysis ambiguity,
but does not by itself prove a new zeta theorem.

Still required:

1. prove that the scaled finite-\(T\) core converges to this exact rational
   polytope integral with an explicit one-sided error;
2. independently reconstruct the bridge/glue normalization from the core to
   the class \(R\);
3. certify the \(0.0111\) tail charge in the same convention;
4. close or independently replace the two archived steps in the \(m_3\to2\)
   argument;
5. then run the final exact moment consumer.

The key change is that the continuum target is no longer a numerical mystery:
its leading constant is exactly \(-1/48\).
