# WP80 — exact moment-cone floor for the k=8 rung

Date: 2026-10-04  
Status: **EXACT CONSUMER-SIDE ALGEBRA; analytic moment transport remains separate**

## Result

Assume a nonnegative measure \(\nu\) on \([0,\infty)\) with

\[
m_0=1,\quad
m_1=1,\quad
m_2=\frac43,\quad
m_3=2,\quad
m_4=\frac{13}{4},\quad
m_5=\frac{101}{18},\quad
m_6=\frac{12809}{1260}.
\]

Then

\[
\boxed{
m_7\ge \frac{25866469}{1352400}
=19.126345016267\ldots
}
\]

This strictly improves the public decimal floor \(m_7\ge19.123\) used in
the reconnaissance k=8 outlook.

The proof is a one-line positivity statement once the exact witness is known:

\[
r(x)=x^3-\frac{3142}{805}x^2+\frac{517}{115}x-\frac{13891}{9660},
\]

and, because \(x\ge0\) on the support,

\[
0\le \int x\,r(x)^2\,d\nu(x)
=
m_7-\frac{25866469}{1352400}.
\]

No grid, optimizer, floating-point LP or support truncation is consumed.

## Derivation

Use the shifted Stieltjes moment matrix

\[
H_1=
\begin{pmatrix}
m_1&m_2&m_3&m_4\\
m_2&m_3&m_4&m_5\\
m_3&m_4&m_5&m_6\\
m_4&m_5&m_6&m_7
\end{pmatrix}\succeq0.
\]

Its fixed upper-left block is

\[
A=
\begin{pmatrix}
1&4/3&2\\
4/3&2&13/4\\
2&13/4&101/18
\end{pmatrix},
\qquad
v=
\begin{pmatrix}
13/4\\101/18\\12809/1260
\end{pmatrix}.
\]

The leading principal minors of \(A\) are exactly

\[
1,\qquad \frac29,\qquad \frac{23}{1296},
\]

so \(A\) is positive definite.  The Schur complement gives

\[
m_7\ge v^T A^{-1}v.
\]

Exact elimination yields

\[
A^{-1}v=
\begin{pmatrix}
13891/9660\\
-517/115\\
3142/805
\end{pmatrix}
\]

and therefore

\[
v^T A^{-1}v
=
\frac{25866469}{1352400}.
\]

The polynomial witness above is exactly the Schur-complement residual.

## Why this matters for the post-79 programme

The public k=8 reconnaissance used

\[
m_7\in[19.123,19.136].
\]

Without changing any model-side connected constant, positivity alone narrows
the admissible interval to

\[
\boxed{
m_7\in
\left[
\frac{25866469}{1352400},
,19.136
\right]
}
\]

whenever the exact \(m_1,\ldots,m_6\) premises are available.

This is useful because a degree-eight zero-mass certificate naturally has a
negative \(m_7\) coefficient and a positive \(m_8\) coefficient: raising
the rigorous lower floor on \(m_7\) improves the worst-case mass-at-zero
bound before any new k=8 arithmetic is proved.

## Evidence boundary

This note does **not** claim that \(m_5\) or \(m_6\) have already been
transported analytically for zeta at theorem grade.  It says:

> conditional on those exact moment premises, the stronger \(m_7\) floor is
> an exact consequence of positivity of a Stieltjes moment matrix.

The machine companion is
`src/wp80_m7_moment_cone_exact.py`, implemented only with
`fractions.Fraction`.
