# WP70-2F — exact universal \(\gamma\)-series tail

Date: 2026-10-04  
Status: **RIGOROUS UNIVERSAL-CLASS TAIL BOUND**

## Motivation

The public absolute tail helper \`tail_bound.py env\` fired badly.  The revised
\(\gamma\)-resummed helper passes numerically, but truncates the displayed
\(\gamma_d\) tail at \(d=4000\).

Before using it in a proof we need an **infinite** tail bound.

The universal \((1,1)\) class is much simpler than the raw finite-height
tensor sieve.

## Exact coefficient law

The public paper's Proposition \(c_0\) gives

\[
\gamma_{2m}
=
C_2
\prod_{p\mid m}\frac1{p(p-2)}
\]

for odd squarefree \(m\), with all other coefficients zero, where

\[
C_2
=
\prod_{p>2}\left(1-\frac1{(p-1)^2}\right).
\]

All coefficients are nonnegative.

Moreover,

\[
1+\frac1{p(p-2)}
=
\frac{(p-1)^2}{p(p-2)}
=
\left(1-\frac1{(p-1)^2}\right)^{-1},
\]

so the Euler products cancel exactly and

\[
\boxed{\sum_{d\ge1}\gamma_d=1}.
\]

Hence the tail after \(D\) is not estimated by a generic divisor bound.  It is

\[
1-
C_2
\sum_{\substack{m\le D/2\\m\ {\rm odd\ squarefree}}}
\prod_{p\mid m}\frac1{p(p-2)}.
\]

## Rigorous enclosure of \(C_2\)

The checker multiplies every local factor for primes up to

\[
P=10^6
\]

with downward directed Decimal rounding.

For the omitted product,

\[
\prod_{p>P}(1-x_p)
\ge1-\sum_{p>P}x_p,
\qquad
x_p=\frac1{(p-1)^2}.
\]

Without using any theorem on prime distribution,

\[
\sum_{p>P}x_p
\le
\sum_{n>P}\frac1{(n-1)^2}
\le
\frac1P+\frac1{P^2}.
\]

This produces a rigorous lower enclosure for \(C_2\).

The finite coefficient sum through \(D/2\) is computed exactly with
\`Fraction\`.

## Result

The GitHub checker certifies

\[
\boxed{
\sum_{d>4000}\gamma_d < 0.000252
}
\]

for the universal class.

The same script also records the larger \(D=40\) and \(D=400\) tails.

This closes the otherwise omitted \(d>4000\) part of the revised public
\(\gamma\)-resummation **at the universal-class level**.

## Why this matters

The raw F-E3c absolute envelope threw away essentially all signed structure and
returned numbers near one.

The \(\gamma\)-resummed representation keeps the signed finite part and places
only the genuinely omitted coefficient mass inside an absolute-value bound.
This is the same proof architecture used elsewhere in our research: preserve
the signed certified contribution and intervalize only the remainder.

That is orders of magnitude sharper.

## Claim boundary

This does **not yet** prove the paper's global
\(\varepsilon_{\rm tail}\le0.0111\).

Still required:

1. prove the universality-collapse passage from the prime-power ensemble to the
   universal \((1,1)\) \(\gamma\)-law in the same normalization;
2. carry the coefficient-tail bound through the exact zone geometry;
3. include finite-\(T\) / normalization corrections with directed sign.

But the infinite arithmetic tail itself is now rigorously small rather than an
uncontrolled \(d>4000\) omission.
