# WP70-2D — analytic scaling of the exact core and the 70% error budget

Date: 2026-10-04  
Status: **DERIVED ASYMPTOTIC REDUCTION**

## Exact geometry already established

The independent rational-polytope audit gives

\[
A:=
\int_1^2(\nu-1)\iint\bar Q\,d\beta_1d\beta_2d\nu
=
\frac1{96},
\]

and

\[
B:=
\int_1^2\iint\bar Q\,d\beta_1d\beta_2d\nu
=
\frac1{16}.
\]

Hence the leading continuum core is

\[
C_{\rm core}=-2A=-\frac1{48}.
\]

## Why the fitted \(c^*\) is not leading-order data

The public continuum law has

\[
g_{\rm law}(\nu;l)
=
-l^2(\nu-1)-l\widetilde c,
\qquad
\widetilde c=c^*-\log(2\pi),
\]

while the scaled overlap geometry contributes \(l^3\) and the normalization is

\[
\frac{2}{l\,\ell_1^4},
\qquad
\ell_1=l+2\log2-1.
\]

Therefore the exact continuous-law expression is

\[
C_{\rm law}(l)
=
-2A\left(\frac{l}{\ell_1}\right)^4
-
2\widetilde c\,B\frac{l^3}{\ell_1^4}.
\]

The second term is \(O(1/l)\), so

\[
\boxed{
\lim_{l\to\infty}C_{\rm law}(l)
=
-\frac1{48}.
}
\]

Thus the unidentified mean-oscillation component inside \(c^*\) affects the
finite-\(l\) approach but **not the asymptotic constant**.

This is important: once the public analytic universality collapse and slope-one
statement are justified, the leading continuum constant no longer requires
Richardson extrapolation or a fitted \(c^*\).

## Exact error budget for 70%

The one-sided fourth-moment route requires

\[
R<-\frac1{180}.
\]

If the analytic assembly gives

\[
R\le -\frac1{48}+\varepsilon_{\rm total},
\]

then 70% follows whenever

\[
\varepsilon_{\rm total}
<
-\frac1{180}+\frac1{48}
=
\boxed{\frac{11}{720}}
=
0.0152777777\ldots
\]

This is the complete positive-error budget after the exact core.

### Using the public 0.0115 tail charge

If

\[
\varepsilon_{\rm tail}\le0.0115,
\]

then the remaining allowed bridge/convergence error is

\[
\boxed{
\frac{11}{720}-0.0115
=
\frac{17}{4500}
=
0.0037777777\ldots
}
\]

### Using the public 0.0111 tail charge

If

\[
\varepsilon_{\rm tail}\le0.0111,
\]

the remaining room is

\[
\boxed{
\frac{47}{11250}
=
0.0041777777\ldots
}
\]

So we do not need a tiny numerical-analysis error.  The exact core creates
several \(10^{-3}\) of room in \(R\)-units.

## Conditional coefficients

With no further positive error beyond the public tail charge:

- tail \(0.0115\) gives a simple-zero coefficient above 70%;
- tail \(0.0111\) gives exactly
  \[
  \frac{1082}{1539}
  =
  0.7030539311241065\ldots
  \]

The latter is the 70.30539% conditional value recorded in WP70-2C.

## What this closes and what it does not

Closed:

1. exact rational continuum geometry;
2. exact asymptotic scaling of the public law once slope \(=1\);
3. proof that \(c^*\) is lower order;
4. exact total error budget required for \(>70\%\).

Still load-bearing:

1. the analytic universality-collapse argument from the original prime-power
   ensemble to the scaled universal \((1,1)\) law;
2. a same-convention rigorous tail bound;
3. the bridge/glue normalization from the continuum object into class \(R\);
4. the two archived steps in the \(m_3\to2\) theorem.

This turns the next phase into a finite list of analytic lemmas rather than a
numerical quadrature problem.
