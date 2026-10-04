# WP71 — prime-power measure collapse toward the exact \(-1/48\) core

Date: 2026-10-04  
Status: **STANDARD-INPUT ANALYTIC REDUCTION; BRIDGE/ARITHMETIC KERNEL INTERFACE STILL TO CLOSE**

## Purpose

The exact polytope computation proves the value of the *limiting geometric
integral*.  The remaining question is why the finite prime-power ledger
converges to that integral.

This note isolates the part that follows from standard prime-number-theorem
technology and separates it from the genuinely project-specific bridge.

## 1. The logarithmic prime-power measure

Let \(l\to\infty\) and define

\[
\mu_l
:=
\frac1l
\sum_{n\le e^l}
\frac{\Lambda(n)}{n}\,
\delta_{\log n/l}.
\]

The standard Mertens/PNT estimate

\[
A(x):=\sum_{n\le x}\frac{\Lambda(n)}n
=
\log x + O(1)
\]

gives, uniformly for \(0\le u\le1\),

\[
\mu_l([0,u])
=
\frac{A(e^{lu})}{l}
=
u+O(l^{-1}).
\]

For the tiny range \(e^{lu}<2\), both sides are \(O(l^{-1})\), so the same
uniform discrepancy statement holds up to \(u=0\).

Therefore

\[
\boxed{
D_l:=
\sup_{0\le u\le1}
|\mu_l([0,u])-u|
=
O(l^{-1}).
}
\]

For every bounded-variation test function \(f\),

\[
\int f\,d\mu_l
=
\int_0^1f(u)\,du
+
O\!\left(D_l\,\|f\|_{\rm BV}\right).
\]

This is just Stieltjes integration by parts.

## 2. Two prime-power coordinates

The fourth-moment core contains

\[
\frac{\Lambda(b_1)\Lambda(b_2)}{b_1b_2}.
\]

Hence its normalized arithmetic measure is the product
\(\mu_l\otimes\mu_l\).  Rectangle discrepancy is \(O(l^{-1})\):

\[
(\mu_l\otimes\mu_l)([0,u]\times[0,v])
=
uv+O(l^{-1}),
\]

uniformly on the unit square.

The moving region

\[
\nu-1\le\beta_1,\beta_2\le\frac{\nu}{2},
\qquad 1\le\nu\le2,
\]

is a polytope with finitely many planar boundary pieces.  The overlap
function

\[
\bar Q(\nu,\beta_1,\beta_2)
\]

is a finite sum of positive parts of maxima/minima of affine functions.
Consequently it is bounded, piecewise affine and of bounded variation on
this compact polytope.

Thus the product prime-power sum converges to the Lebesgue integral of
\(\bar Q\), and likewise after multiplication by the bounded factor
\((\nu-1)\).

This is exactly the regularity class for which the discrepancy estimate
above transfers the arithmetic sums to the rational-polytope integral.

## 3. Exceptional small-prime / coincident-prime mass vanishes

A fixed prime \(p\) contributes

\[
\sum_{k\ge1}\frac{\log p}{p^k}
=
\frac{\log p}{p-1}
\]

to the unnormalised measure.  After division by \(l\), every fixed finite
set of primes therefore has total mass \(O(l^{-1})\).

The diagonal prime-power pair has even smaller normalized mass:

\[
\frac1{l^2}
\sum_{p^k\le e^l}
\left(\frac{\log p}{p^k}\right)^2
=
O(l^{-2}),
\]

because the infinite square-sum converges.

Hence fixed exceptional local classes, equal-prime pairs, and any finite
collection of small-prime corrections cannot contribute a new leading
constant.  Their effect belongs to the lower-order transfer error.

## 4. The continuum geometry

After the logarithmic scaling

\[
\beta_i=\frac{\log b_i}{l},
\]

the twelve overlap terms become exactly the piecewise-linear geometry
certified in WP70-2C.  Its weighted moment is

\[
\int_1^2(\nu-1)
\int_{\nu-1}^{\nu/2}\int_{\nu-1}^{\nu/2}
\bar Q(\nu,\beta_1,\beta_2)
\,d\beta_2\,d\beta_1\,d\nu
=
\frac1{96}.
\]

Therefore once the project-specific spectral mass has the leading law

\[
-l^2(\nu-1)
\]

with a lower-order \(O(l)\) correction, the normalized core converges to

\[
-2\cdot\frac1{96}
=
\boxed{-\frac1{48}}.
\]

The already derived \(c^*\)-term is \(O(l^{-1})\) after normalization and
does not alter this limit.

## 5. What this removes from the open list

The following parts do **not** require a fitted continuum ansatz:

- replacement of weighted prime-power logarithms by Lebesgue variables;
- disappearance of fixed small-prime classes at leading order;
- disappearance of the diagonal prime-power pair at leading order;
- evaluation of the limiting overlap geometry;
- removal of \(c^*\) from the leading constant.

The remaining load-bearing interface is narrower:

1. derive the leading spectral-mass law with the correct sign and factor in
   the same \(R\)-normalization;
2. show the public bridge/glue reduction reaches this prime-power measure
   without an uncharged leading term;
3. show the covered/middle/low-zone and collar errors are \(o(1)\);
4. close the singular-series tail with \(P=(\log X)^B\).

If these hold, the natural one-sided rung is the exact

\[
\boxed{
\frac{N_0^s}{N}\ge\frac{269}{378}=71.16402116\ldots\%
}
\]

from WP70-2G.

## Evidence boundary

This note uses the standard Mertens/PNT estimate as an external classical
input.  It does not, by itself, prove that the public fourth-moment ledger
has exactly the required spectral-mass/bridge normalization.  That interface
is the next hostile-audit target.
