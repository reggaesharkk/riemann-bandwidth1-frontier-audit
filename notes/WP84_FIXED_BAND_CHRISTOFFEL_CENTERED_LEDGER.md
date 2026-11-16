# WP84 — centered ledger for the fixed-band Christoffel square

Date: 2026-10-06

Status: **EXACT DEGREE-SIX CENTERED REDUCTION; IDENTIFIES THE TRUE NEW ARITHMETIC DEBT**

No unconditional zero-proportion theorem is claimed here.

This note expands the fixed-band fallback observable

    g(H_R)=P(H_R)^2

around the scalar background H_R=I+X_R.  It shows precisely which centered
moments are actually needed and, just as importantly, why the existing
degree-four upper bound by itself is not enough to reach the full
Christoffel value.

## 1. Exact centered cubic

With

    P(x)
      =
      1-(43428/13891)x
       +(37704/13891)x^2
       -(9660/13891)x^3,

put x=1+y.  Then

    boxed:

    P(1+y)
      =
      (-1493+3000y+8724y^2-9660y^3)/13891.

Therefore

    g(1+y)=P(1+y)^2

has exact centered coefficients

    boxed:

    g(1+y)
      =
      1/192959881 *
      [
        2229049
        -8958000 y
        -17049864 y^2
        +81188760 y^3
        +18148176 y^4
        -168547680 y^5
        +93315600 y^6
      ].

For

    mu_k^c(R)=tau(X_R^k),

the exact fixed-band square is therefore

    boxed:

    tau g(H_R)
      =
      1/192959881 *
      [
        2229049
        -8958000 mu_1^c
        -17049864 mu_2^c
        +81188760 mu_3^c
        +18148176 mu_4^c
        -168547680 mu_5^c
        +93315600 mu_6^c
      ].

This is the single combined observable required by the fallback route.

## 2. Frozen model centered moments

From the pinned raw moments

    m0=1,
    m1=1,
    m2=4/3,
    m3=2,
    m4=13/4,
    m5=101/18,
    m6=12809/1260,

the centered moments are exactly

    boxed:

    mu_1^c=0,
    mu_2^c=1/3,
    mu_3^c=0,
    mu_4^c=1/4,
    mu_5^c=1/36,
    mu_6^c=157/630.

Substitution gives

    boxed:

    tau g
      =
      1415/13891
      =
      w0.

The degree-by-degree contributions are approximately

    k=0:  +0.0115518780
    k=2:  -0.0294532105
    k=4:  +0.0235128876
    k=5:  -0.0242634893
    k=6:  +0.1205164508.

Thus the sixth-order term is dominant, while the fifth-order term supplies a
substantial favorable subtraction.

## 3. The existing degree-four nonpositivity is not enough

The current R=400-style theorem only uses

    mu_4^c
      <=
      Pair_R+o(1),

and in the large fixed-R limit the pair layer tends to

    4/15.

If one inserts 4/15 instead of the model value 1/4, while keeping every other
centered moment at its model value, the square trace increases by exactly

    boxed:

    (18148176/192959881)
    *
    (4/15-1/4)

      =
      3024696/1929598810

      ~=0.00156752584233.

That is already about half of the entire ideal first->79 model cushion

    0.105-w0
      ~=0.00313548340652.

Therefore a degree-six fixed-band proof cannot simply reuse the current
"connected sector <=0" estimate and ignore its quantitative negative mass.

It must recover a nontrivial portion of the connected fourth-order correction,
or compensate through a sharper favorable fifth/sixth-order combination.

## 4. The genuinely new high-order debt is one signed combination

Assume the already-established lower-order fixed-band controls are inserted:

    mu_1^c=o(1),

    mu_2^c
      =
      1/3+small error,

    mu_3^c=o(1).

Then the only new high-order quantity appears through

    boxed:

    93315600 mu_6^c
      -168547680 mu_5^c
      +18148176 mu_4^c.

Equivalently, after dividing by 192959881,

    boxed:

    0.4836010445... mu_6^c
      -0.8734856133... mu_5^c
      +0.09405155054... mu_4^c.

So the fallback does **not** require separate convergence theorems for
m4,m5,m6.  It requires a one-sided estimate for this single signed
combination.

The model value of the m5/m6 part is

    boxed:

    -168547680/192959881 * (1/36)
    +93315600/192959881 * (157/630)

      ~=0.096252961516.

If one only pays the pair-layer upper bound mu_4^c<=4/15, then to return to
w0 the required m5/m6 combination would have to improve over its model value
by about

    0.00156752584233.

This is a precise quantitative target for any degree-five/six connected-word
cancellation.

## 5. A useful completion of square

The top three powers satisfy the exact identity

    c6 y^6+c5 y^5+c4 y^4

      =
      c6 y^4 (y-727/805)^2
      -
      (57960000/192959881)y^4,

where

    c6=93315600/192959881.

Thus the high-order portion contains one manifest positive square plus a
negative quartic correction.

This does not by itself bound the trace, because y=X_R is an operator and the
scalar powers commute only because they are powers of the same Hermitian
matrix, but here that is sufficient: the identity lifts exactly by functional
calculus.

Hence

    boxed:

    c6 mu_6^c+c5 mu_5^c+c4 mu_4^c

      =
      c6 tau[
        X_R^4 (X_R-727/805 I)^2
      ]
      -
      (57960000/192959881) mu_4^c.

This representation may be more useful than estimating mu5 and mu6
separately.  The first term is nonnegative and contains the entire new
degree-five/six dependence.

For an upper bound one still needs a theorem controlling that positive square,
but the target is now one positive fixed-band observable rather than two raw
moments.

## 6. Revised fixed-band fallback target

Combining with

    notes/WP84_FIXED_BAND_CHRISTOFFEL_SQUARE_FALLBACK.md,

the >79 fallback may be attacked by proving a one-sided fixed-band bound for

    boxed:

    tau[
      X_R^4 (X_R-727/805 I)^2
    ]

together with the already-developed controls on mu2, mu3 and the quantitative
connected part of mu4.

This is the smallest degree-six positive object exposed by the exact
Christoffel square after centering.

## Evidence boundary

Closed:

- exact centered polynomial;
- exact model centered moments;
- exact 0.0015675 cost of replacing the connected m4 target by the pair-only
  4/15 bound;
- exact signed m4/m5/m6 combination;
- exact square completion at 727/805.

Open:

- theorem-grade fixed-band upper bound for the positive degree-six square;
- quantitative recovery of enough negative connected m4 mass;
- common normalization with the full-to-band bounded consumer.

No >79 theorem is claimed.

See:

    notes/WP84_FIXED_BAND_CHRISTOFFEL_SQUARE_FALLBACK.md
    notes/WP84_R400_COMPLETE_WORD_LEDGER_REPLAY.md
    notes/WP84_FIXED_BAND_LOWER_MOMENT_COLLAPSE.md
