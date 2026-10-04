
# WP71 — published MRT import audit and G9 boundary

Date: 2026-10-04
Status: G2 variance/structured-shift input DERIVED FROM THE PUBLISHED THEOREM;
G9 weighted welding reduction STILL OPEN

## Source checked independently

K. Matomäki, M. Radziwill, T. Tao,
"Correlations of the von Mangoldt and higher divisor functions I.
Long shift ranges", Proc. London Math. Soc. 118 (2019), 284-350,
DOI 10.1112/plms.12181.

The published Theorem 1.3(i) applies for

    X^(8/33+eps) <= H <= X^(1-eps)

and a center h0 <= X^(1-eps).  For arbitrary logarithmic saving it gives the
Hardy-Littlewood prime-pair asymptotic for all but a logarithmically sparse
exceptional set of shifts in |h-h0|<=H.

Important correction to the shorthand used in the public candidate:
Theorem 1.3(i) is stated as an almost-all pointwise theorem, not literally as
an L2 variance formula.  The L2 formula needed here is nevertheless an easy
corollary, written out below.

## 1. L2 variance corollary

Define

    dev(h) = sum_{X<n<=2X} Lambda(n)Lambda(n+h) - S(h) X.

Invoke Theorem 1.3(i) with an exponent B that may be chosen arbitrarily large.

Good shifts:
there are O(H) of them and

    |dev(h)| << X (log X)^(-B),

so their squared contribution is

    << H X^2 (log X)^(-2B).

Exceptional shifts:
their number is

    << H (log X)^(-B).

For |h|<=X^(1-eps), the elementary envelope Lambda(n)<=log(3X), together with
the standard polylogarithmic envelope for the singular series, gives more than
enough for

    |dev(h)| << X (log X)^2.

Hence the exceptional squared contribution is

    << H X^2 (log X)^(-B+4).

Because B is arbitrary, for every requested A we choose B>A+4 and obtain

    sum_{|h-h0|<=H} |dev(h)|^2
      <<_{A,eps} H X^2 (log X)^(-A).

Thus the variance input used by Stage A is a derived corollary of the
published theorem, not an additional conjecture.

## 2. Structured shifts lose no modulus-count factor

For a modulus family Q and K_q<=H/q,

    sum_{q in Q} sum_{k<=K_q} |dev(qk)|^2
      = sum_{h<=H} nu(h) |dev(h)|^2,

where

    nu(h) <= tau(h).

Set V=(log X)^C.

On tau(h)<=V, use the L2 corollary with an arbitrarily stronger logarithmic
saving.

On tau(h)>V, use the elementary pointwise envelope above and

    sum_{h<=H, tau(h)>V} tau(h)
      <= V^(-1) sum_{h<=H} tau(h)^2
      << H (log H)^3 / V.

Taking C and the source saving large enough gives, for every A,

    sum_{q in Q} sum_{k<=K_q} |dev(qk)|^2
      <<_A H X^2 (log X)^(-A),

uniformly in the chosen structured modulus family.

This independently closes the logical content of Stage-A G2.

## 3. What Proposition 5.4 actually is

The published Proposition 5.4 is a mean-value estimate for Dirichlet series
with q<=log^B X and H=X^(8/33+eps), under its stated lambda/q ranges.  Appendix
A proves a related Proposition 5.5 using combinatorial decompositions and
Dirichlet-polynomial mean values.

Neither statement, as written in the published paper, directly names or
bounds the Stage-A welding weight

    w_k(n) = sum_{m in I(n)} Lambda(m)Lambda(m-rk).

Therefore the public candidate's sentence saying that the glue "closes" by
main-term factorization, Abel summation, and Proposition 5.4 / Appendix A is
not yet a self-contained proof of G9.

We must provide the reduction explicitly.

## 4. G9 is now split into four fail-closed doors

### G9-A — exact welding identity

Rewrite the middle-band off-diagonal term in the exact public normalization as

    sum_{k,n} G_k(n) w_k(n) Lambda(n)Lambda(n-qk),

with all ranges, endpoint conventions, q,r gcd factors, and the slow geometry
G_k(n) stated explicitly.

No asymptotic estimate is allowed in this door.

### G9-B — signed major-arc main

Decompose

    w_k(n) = M_k(n) + e_k(n).

The M_k contribution must be carried with sign intact.  Prove its local-density
factorization and perform Abel summation against G_k(n).  This door must end in
the same singular-series/continuum object already used for C_core=-1/48.

No absolute value or family-level Cauchy-Schwarz may touch M_k.

### G9-C — minor-arc / remainder reduction

Express the e_k contribution as the exact Dirichlet-polynomial family to which
the published MRT mean-value machinery is applied.

For every invocation record explicitly:

- X;
- H;
- q, q0, q1;
- lambda;
- smoothing function / interval;
- verification of X^(8/33+eps)<=H<=X^(1-eps);
- verification q<=log^B X;
- verification of the lambda bounds in Proposition 5.4.

A citation alone does not close this door.

### G9-D — R-unit normalization

After the MRT bound is obtained, convert it back to

    1/(pi*l*X*ell1^4)

units and prove the total remainder is o(1), uniformly over the polylogarithmic
modulus family.

Only Cauchy-Schwarz in the shift variable is permitted.

## 5. Cross-project method applied

The LRSC K10/K11 programme used separate "doors": a witness did not close an
exclusion door, and every terminal branch needed its own certificate.

We use that discipline here:

- G9-B is the signed-main door;
- G9-C is the analytic remainder door;
- neither is allowed to borrow the other's conclusion;
- G11 remains blocked until both are closed.

This is method transfer only. No LRSC numerical result is used.

## Current conclusion

G2: CLOSED from published MRT Theorem 1.3(i) plus an explicit L2 and divisor
multiplicity argument.

G9: NOT CLOSED.  The exact missing object is no longer vague: it is the
explicit reduction of the welding remainder to the hypotheses of published
MRT Proposition 5.4 / Appendix A, followed by conversion to R-units.
