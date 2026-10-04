# WP70-1C — explicit polynomial witness for >70%

Date: 2026-10-04  
Status: **DERIVED SUFFICIENT CONDITION — ANALYTIC MOMENT BOUNDS STILL OPEN**

## Why this is useful

WP70-1B derived the optimal two-parameter Christoffel region for uncertain
third and fourth moments.  For an analytic proof, however, it is useful to
have an even simpler fixed witness that never has to invert an uncertain
moment matrix.

Use the degree-two polynomial

\[
\boxed{
P(x)=1-\frac74x+\frac23x^2.
}
\]

This is the exact Christoffel minimizer at the sine-kernel moments

\[
\mu_0=1,\quad
\mu_1=1,\quad
\mu_2=\frac43,\quad
\mu_3=2,\quad
\mu_4=\frac{13}{4}.
\]

A direct exact calculation gives

\[
\mathbb E P(X)^2=\frac5{36}.
\]

Because the spectral measure is supported on \([0,\infty)\) and \(P(0)=1\),
the mass at zero is at most \(\mathbb E P(X)^2\).  Therefore the positive-rank
fraction is at least \(1-\mathbb E P(X)^2\), and the simple-zero transfer gives

\[
\frac{N_0^s}{N}
\ge
1-2\mathbb E P(X)^2.
\]

At the exact target moments this recovers

\[
1-\frac{10}{36}
=
\frac{13}{18}.
\]

## One-sided moment errors

Suppose only that

\[
\mu_3\ge2-\delta_3,
\qquad
\mu_4\le\frac{13}{4}+\delta_4.
\]

Expanding \(P^2\) shows that the coefficient of \(\mu_3\) is \(-7/3\) and
the coefficient of \(\mu_4\) is \(4/9\).  Hence

\[
\mathbb E P(X)^2
\le
\frac5{36}
+
\frac73\delta_3
+
\frac49\delta_4.
\]

Thus a completely explicit sufficient condition for \(>70\%\) is

\[
\boxed{
210\delta_3+40\delta_4<1.
}
\]

This condition is slightly stronger than the fully reoptimized Christoffel
region in WP70-1B, but it is much easier to insert into an analytic trace proof.

## Clean kill-shot theorem target

A particularly simple target is

\[
\boxed{
\mu_3\ge1.996,\qquad
\mu_4\le3.25.
}
\]

Here

\[
\delta_3=\frac1{250},\qquad \delta_4=0,
\]

so

\[
210\delta_3=\frac{21}{25}<1.
\]

The fixed polynomial then proves the exact lower bound

\[
\boxed{
\frac{N_0^s}{N}
\ge
\frac{1583}{2250}
=
0.703555\ldots
}
\]

or

\[
\boxed{70.3555\ldots\%}.
\]

Therefore we do **not** need to prove the exact sine-process third moment to
reach 70%.

We can lose four thousandths in the third moment and still cross the line,
provided the fourth moment has the correct one-sided upper bound.

## Why this is a better analytic objective

The prime-side theorem can now be designed around inequalities rather than
full asymptotics:

\[
\liminf \mu_3(T)\ge1.996,
\qquad
\limsup \mu_4(T)\le3.25.
\]

That leaves room to discard difficult positive pieces, use one-sided majorants,
or prove only enough cancellation to control the bad-sign terms.

The arithmetic problem is now much more concrete:

> Can the long-shift \((\Lambda*\Lambda)\) average in the fourth trace be
> bounded from above strongly enough to keep \(\mu_4\le3.25+o(1)\), while a
> separate lower estimate keeps \(\mu_3\ge1.996-o(1)\)?

If yes, the fixed polynomial certificate already delivers \(>70\%\).

## Independent checker

Run:

\`python src/wp70_explicit_polynomial_witness.py\`

Expected final line:

\`RESULT: EXPLICIT_POLYNOMIAL_70_PERCENT_WITNESS_PASS\`

## Claim boundary

This is an exact algebraic reduction.

It is not yet an unconditional zeta theorem because the required one-sided
third/fourth trace estimates have not been proved.
