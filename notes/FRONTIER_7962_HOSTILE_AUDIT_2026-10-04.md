# Frontier 79.62 hostile audit — exact consumption optimization

Date: 2026-10-04  
Status: **EXACT CONSUMPTION IMPROVEMENT CONDITIONAL ON IMPORTED MOMENTS**

## Public candidate located

A Zenodo preprint and GitHub reproduction package by Hongyi Yang and Shihua
Yang publicly claim

\[
\frac{N_0^s}{N}\ge0.7962,
\]

with exact model moments

\[
m_0=1,\quad
m_1=1,\quad
m_2=\frac43,\quad
m_3=2,\quad
m_4=\frac{13}{4},\quad
m_5=\frac{101}{18},\quad
m_6=\frac{12809}{1260}.
\]

The authors grade the work **certified-candidate**, not established record:
the rational/certificate layers are machine-checked, but the analytic
higher-moment chain is unformalized and external review is pending.

This public candidate numerically supersedes our 70% target, so it is now the
highest-priority hostile-audit object.

## Independent exact consumption replay

The public certificate uses a squared cubic with three rounded rational roots.
Instead of importing that polynomial, solve the degree-three Christoffel
minimization directly over the exact moment matrix.

For

\[
P(x)=1+ax+bx^2+cx^3,
\]

minimize \(\mathbb E[P(X)^2]\) under \(P(0)=1\).  The exact normal equations
give

\[
\boxed{
a=-\frac{43428}{13891},\qquad
b=\frac{37704}{13891},\qquad
c=-\frac{9660}{13891}.
}
\]

Since \(a<0,b>0,c<0\), every nonconstant term is nonnegative when \(x\le0\).
Hence

\[
P(x)\ge1\quad(x\le0),
\]

so \(P(x)^2\ge1\) on the entire nonpositive half-line.  This is an admissible
inertia/counting dual certificate, not merely an atom-at-zero certificate.

Exact substitution gives

\[
\boxed{
w_0=\mathbb E[P(X)^2]=\frac{1415}{13891}.
}
\]

Therefore the simple-zero transfer gives

\[
\boxed{
\frac{N_0^s}{N}
\ge
1-2w_0
=
\frac{11061}{13891}
=
0.7962709668130444172\ldots
}
\]

and the distinct-zero transfer gives

\[
\boxed{
\frac{N_d}{N}
\ge
1-w_0
=
\frac{12476}{13891}
=
0.8981354834065222086\ldots
}
\]

conditional on the same imported moment premises.

The public rational-root certificate itself gives approximately

\[
0.7962709657383785\ldots
\]

so the exact coefficient-form Christoffel certificate improves even their
unrounded exact certificate by about \(1.07\times10^{-9}\) in proportion.

This gain is tiny numerically but important structurally: the consumption
layer is now solved exactly without root rounding.

## Claim boundary

This does **not** validate the 79.62% theorem claim.

It proves only:

> If the six imported normalized moment statements are valid in the required
> asymptotic sense, then the exact polynomial above yields the stronger
> coefficient \(11061/13891\).

The active hostile audit is therefore entirely upstream of the consumption
layer.

## Weakest link found so far

The public package's own grading identifies the analytic higher-moment chain
as unformalized.

The most consequential new statement is its truncated fourth-moment
"“Lemma D”":

\[
m_4\to13/4.
\]

The unrestricted shifted-correlation problem is acknowledged there as open.
The paper claims that an \(\ell_1\)-cell truncation plus a Parseval/spectral
reorganization reduces the consumed logarithmic-modulus range to
Siegel--Walfisz major arcs and Vaughan minor arcs.

If this theorem survives independent audit, 70% is already surpassed:
the exact fourth-moment rung alone gives \(13/18=72.22\ldots\%\).

If it fails, the 79.62% and 72.22% headlines both lose their analytic bridge.

## Hostile-audit order

1. **Truncation discharge.** Re-derive the claimed
   \(P^{-(k-2)+\varepsilon}\) cell-tail bound from the original cycle weights;
   do not trust the normalization prose.
2. **Minor/mixed spectral budget.** Check whether a pointwise Vaughan saving
   on one factor is quantitatively sufficient after squaring the spectral
   density and summing all bins.
3. **Major-major normalization.** Reconstruct the exact Parseval constants and
   the singular-series comb at the joint modulus.
4. **Consumer interface.** Verify that the variance theorem actually implies
   the exact normalized fourth trace consumed by the zero-side polynomial.
5. Only after the fourth moment survives, audit the fifth/sixth extension.

## Current frontier classification

- \(0.6735000520898147\): our independently exact scalar retune, conditional
  on a public q=8 finite certificate.
- \(13/18=0.72222\ldots\): public candidate rung, conditional on the new
  fourth-moment analytic theorem.
- \(11061/13891=0.7962709668\ldots\): exact optimized consumption of the
  public six-moment candidate, conditional on all imported moments.

No 79.62% theorem claim is frozen until the analytic chain survives hostile
re-derivation.
