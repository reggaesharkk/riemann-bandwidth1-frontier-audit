# WP72 — MRT almost-all theorem to the structured \(L^2\) variance consumed by Lemma D

Date: 2026-10-04  
Status: **ANALYTIC REDUCTION CLOSED MODULO STANDARD UPPER-SIEVE/DIVISOR BOUNDS**

## Why this note exists

The public higher-moment paper cites Matomäki--Radziwiłł--Tao (MRT),
Theorem 1.3(i), in the stronger-looking variance form

\[
\sum_{|h-h_0|\le H}
|\operatorname{dev}(h)|^2
\ll_{A,\varepsilon}
H X^2(\log X)^{-A}.
\]

MRT's theorem is normally stated as an **almost-all shifts** asymptotic, not
literally in this displayed \(L^2\) form.  This note checks that the form
consumed by the zeta ledger follows by parameter retuning and standard
envelopes.

## 1. MRT input

For every fixed \(A_0>0\), \(\varepsilon>0\), and

\[
X^{8/33+\varepsilon}\le H\le X^{1-\varepsilon},
\qquad
0\le h_0\le X^{1-\varepsilon},
\]

MRT gives the Hardy--Littlewood asymptotic for all but

\[
O_{A_0,\varepsilon}(H(\log X)^{-A_0})
\]

shifts in \(|h-h_0|\le H\), with an arbitrarily large logarithmic saving in
the good-shift error.

Write

\[
E(h)
=
\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)
-
\mathfrak S(h)X.
\]

On good shifts, after requesting enough logarithmic saving,

\[
|E(h)|\ll X(\log X)^{-A_1}.
\]

On all shifts the standard upper-bound sieve gives a crude envelope of the
shape

\[
|E(h)|\ll X\,\mathfrak S(h)
\]

(up to a harmless absolute/logarithmic factor, which can be absorbed below).

For the twin singular series,

\[
\mathfrak S(h)\ll \log\log(3|h|)
\]

is more than sufficient.

## 2. Almost-all \(\Rightarrow L^2\)

Split the shift interval into good and exceptional sets.

Good contribution:

\[
\sum_{\rm good}|E(h)|^2
\ll
H X^2(\log X)^{-2A_1}.
\]

Exceptional contribution:

\[
\sum_{\rm exc}|E(h)|^2
\ll
H(\log X)^{-A_0}
X^2(\log\log X)^2.
\]

Because MRT allows \(A_0,A_1\) to be chosen arbitrarily large, for every
prescribed \(A\) we choose, for example,

\[
2A_1\ge A+2,
\qquad
A_0\ge A+3.
\]

Then

\[
\boxed{
\sum_{|h-h_0|\le H}|E(h)|^2
\ll_{A,\varepsilon}
H X^2(\log X)^{-A}.
}
\]

Thus the public “variance form” is a legitimate corollary of the published
almost-all theorem; it does not require a stronger external hypothesis.

Dyadic subdivision handles windows comparable to \([X,4X]\), and smooth
weights follow by the usual partial-summation/partition argument.

## 3. Structured multiples do not lose the arbitrary log saving

The ledger does not sum each shift once.  It encounters structured families

\[
h=qk,\qquad q\in\mathcal Q,\quad k\le K_q\le H/q.
\]

Let

\[
\nu(h)
=
\#\{(q,k):q\in\mathcal Q,\ k\le K_q,\ qk=h\}.
\]

Then

\[
\nu(h)\le\tau(h)
\]

and

\[
\sum_{q\in\mathcal Q}\sum_{k\le K_q}|E(qk)|^2
=
\sum_{h\le H}\nu(h)|E(h)|^2.
\]

Choose \(V=(\log X)^C\).

### Generic divisor multiplicity

On \(\tau(h)\le V\),

\[
\sum \nu(h)|E(h)|^2
\le
V\sum|E(h)|^2.
\]

Request the MRT-derived \(L^2\) estimate with exponent \(A+C+2\); this
contributes

\[
\ll H X^2(\log X)^{-A-2}.
\]

### Rare divisor multiplicity

On \(\tau(h)>V\), use

\[
\nu(h)\le\tau(h),
\qquad
|E(h)|^2\ll X^2(\log\log X)^2.
\]

Since

\[
\tau(h)\mathbf 1_{\tau(h)>V}
\le
\frac{\tau(h)^2}{V}
\]

and the classical second moment satisfies

\[
\sum_{h\le H}\tau(h)^2\ll H(\log H)^3,
\]

we obtain

\[
\sum_{\tau(h)>V}\nu(h)|E(h)|^2
\ll
H X^2
(\log\log X)^2
(\log X)^{3-C}.
\]

Take \(C>A+5\).  This is

\[
\ll_A H X^2(\log X)^{-A}.
\]

Therefore

\[
\boxed{
\sum_{q\in\mathcal Q}\sum_{k\le K_q}
|E(qk)|^2
\ll_A
H X^2(\log X)^{-A}.
}
\]

No factor of the structured moduli survives.

## 4. Consequence for the hostile audit

This closes one important interface in the public Lemma-D architecture:

**published MRT almost-all control is strong enough to feed the structured
shift families after retuning the arbitrary log saving.**

So this is no longer on the critical unresolved list.

The current load-bearing Lemma-D gaps are instead:

1. the exact bridge/glue normalization from the cell variance to the
   spectral \(L^2\) object;
2. complete quantitative write-out of the mixed/minor spectral-bin budget;
3. the comb-to-singular-series normalization at all required local classes;
4. the high-cell-parameter truncation normalization.

Those are internal interfaces, not missing strength from MRT.

## Scope boundary

This note does not import the conclusion of the public higher-moment paper.
It uses only MRT's published almost-all result plus standard upper-sieve,
singular-series and divisor-moment bounds to derive the exact type of
structured \(L^2\) estimate required by the ledger.
