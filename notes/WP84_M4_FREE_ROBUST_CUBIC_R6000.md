# WP84 — m4-free robust cubic >79 fallback at fixed band R=6000

Date: 2026-10-06

Status: **EXACT CONSUMER/ALGEBRA REDUCTION — THE >79 FIXED-BAND TARGET NO LONGER REQUIRES ANY QUANTITATIVE FOURTH-MOMENT CONNECTED CORRECTION; IT REDUCES TO ONE-SIDED CENTERED m5 AND m6 BOUNDS**

No unconditional zero-proportion theorem is claimed here.

The previous Christoffel-square fallback used the exact model cubic and
therefore retained a positive centered-fourth-moment coefficient.  This note
re-optimizes the cubic under theorem-side one-sided information.

The key result is an exact cubic square whose centered x^4 coefficient is
zero.  Consequently the hard quantitative fourth-order connected correction
drops out of the >79 fallback entirely.

## 1. Robust centered cubic

Let X=H_R-I and define

    q(X)
      =
      a0+a1 X+a2 X^2+a3 X^3,

with

    a0 = -19101/185500,
    a1 =  961/3710,
    a2 =  31/50,
    a3 = -371/500.

The constraint

    a2^2+2 a1 a3=0

holds exactly.

Hence in q(X)^2 the coefficient of X^4 is exactly zero.

In the original spectral variable x=1+X this polynomial is

    boxed:

    P_dag(x)
      =
      1
      -(594893/185500)x
      +(1423/500)x^2
      -(371/500)x^3.

All three nonconstant coefficients of P_dag(-y) are positive for y>=0, so

    P_dag(x)>=1
    for x<=0.

## 2. Exact centered square ledger

The square has centered coefficients

    q(X)^2
      =
      c0+c1 X+c2 X^2+c3 X^3
      +0*X^4+c5 X^5+c6 X^6,

where

    c0 = 364848201/34410250000,
    c1 = -18356061/344102500,
    c2 = -26060119/430128125,
    c3 = 21981971/46375000,
    c5 = -11501/12500,
    c6 = 137641/250000.

Thus the theorem directions are favorable:

- c2<0: a lower bound on centered m2 is enough;
- c4=0: centered m4 is absent completely;
- c5<0: a lower bound on centered m5 is enough;
- c6>0: an upper bound on centered m6 is enough.

The centered m1 and m3 terms are o(1) under the already-established
fixed-band lower-moment/sign-balance gates.

## 3. Robust high-order target

Assume only

    mu2^c(H_R)
      >=
      1/3 - 2/(pi^2 R)+o(1),

    mu3^c(H_R)=o(1),

    boxed:
    mu5^c(H_R)
      >=
      1/36-o(1),

and

    boxed:
    mu6^c(H_R)
      <=
      34/135+o(1).

No quantitative hypothesis on mu4^c is used.

The sixth-moment ceiling has a direct sector interpretation.  The frozen
model decomposition is

    mu6^c
      =
      131/420
      -23/420
      -1/126

      =
      157/630,

corresponding to

    {2,2,2},
    {4,2},
    {6}.

The relaxed ceiling

    34/135

is exactly

    131/420
      -23/420
      -(2/3)(1/126).

Therefore it requires the pair and {4,2} sectors at their frozen values but
only two thirds of the favorable fully connected {6} correction.

Under these one-sided bounds,

    boxed:

    limsup tau P_dag(H_R)^2
      <=
      E_rob
      +
      |c2| * 2/(pi^2 R),

where

    boxed:

    E_rob
      =
      240421959557/2322691875000
      ~=0.103510053203678.

This number already includes the relaxed mu6=34/135 ceiling.

## 4. Bounded rational one-pole consumer

Take the rational pole height

    boxed:

    a=221/200.

Define

    boxed:

    p_dag(x)
      =
      a^6 P_dag(x)^2/(x^2+a^2)^3.

For x=-y<=0, the exact numerator

    a^6 P_dag(-y)^2-(y^2+a^2)^3

has zero constant coefficient and strictly positive coefficients in every
power y^1,...,y^6.  Hence

    p_dag(x)>=1
    for x<=0.

Also p_dag>=0 globally.

Since

    (x^2+a^2)^3>=a^6,

we have the exact pointwise domination

    boxed:

    p_dag(x)<=P_dag(x)^2

for all real x.

Thus the unbounded cubic square is consumed only after fixed-band truncation.

## 5. Exact curvature certificate and band charge

The companion exact Sturm gate proves

    boxed:

    ||p_dag''||_infinity
      <
      137721/5000
      =
      27.5442.

The universal functional band theorem therefore gives

    |tau p_dag(H)-tau p_dag(H_R)|
      <=
      3 ||p_dag''||_infinity/(pi^2 R)
      +o(R^-1).

Using pi>333/106 yields the fully rational constant

    boxed:

    C_dag
      =
      128952763/15401250
      ~=8.37287642237.

## 6. Freeze R=6000

At

    boxed:

    R=6000,

the full-to-band charge is

    C_dag/R
      =
      128952763/92407500000
      ~=0.00139547940372805.

The fixed-band variance-deficit charge caused by c2<0 is at most

    boxed:

    |c2| * 2/[ (333/106)^2 R ]

      =
      26060119/12734908593750
      ~=0.00000204635304667909.

Therefore the complete theorem-side defect budget is

    E_rob
      + band charge
      + variance-deficit charge

      <
      0.105

by the exact rational margin

    boxed:

    52897896569489/572357731837500000

      ~=0.0000924210395475315.

The first integer R for which this exact rational budget is positive is 5628;
R=6000 is retained as the cleaner working band.

## 7. New arithmetic kill gate

A strict >79 simple-zero theorem now follows if the actual fixed-band sharp
prime state at R=6000 satisfies

    boxed:

    mu5^c(H_6000)
      >=
      1/36-o(1),

and

    boxed:

    mu6^c(H_6000)
      <=
      34/135+o(1),

together with the already-developed lower-moment facts

    mu1^c=o(1),
    mu2^c>=1/3-2/(pi^2 R)+o(1),
    mu3^c=o(1).

There is **no mu4^c hypothesis** in this kill gate.

This is a qualitative change from the previous fixed-band fallback.

## 8. Why the fully connected sixth sector still matters

If the entire {6}=-1/126 correction is discarded while the other centered
moments stay at their model values, the optimal unrestricted degree-three
Christoffel square has defect

    1615/15331
      ~=0.1053421173,

which is already above 0.105.

Thus some sixth connected information is genuinely necessary within the
degree-three square architecture.

However, the exact optimization shows that at zero band cost only slightly
more than 10.7% of that correction is information-theoretically necessary
after re-optimizing the cubic.  The present c4-free rational certificate uses
a more conservative and cleaner theorem target: recover two thirds of {6}.

## 9. Evidence boundary

Closed:

- exact rational cubic with c4=0;
- exact support-free one-pole bounded consumer;
- exact pointwise p_dag<=P_dag^2;
- exact Sturm curvature bound;
- exact R=6000 defect budget;
- exact removal of the quantitative fourth-moment connected sector from the
  >79 fallback.

Open:

- prove the fixed-band one-sided fifth-moment bound;
- prove the fixed-band sixth-moment ceiling 34/135;
- then insert the already-audited zero-count transfer.

This is now the preferred fixed-band arithmetic target.  The minimal-radius
one-point heat-curvature route remains the primary all-resolvent attack.

Public model constants used for orientation:
C5=1/36, {4,2}=-23/420, {6}=-1/126.  Their finite symbolic values do not by
themselves prove the required zeta-side fixed-band transport.
