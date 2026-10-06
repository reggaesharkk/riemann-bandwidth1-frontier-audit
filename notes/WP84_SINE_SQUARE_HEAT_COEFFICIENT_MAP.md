# WP84 — sine-square heat-curvature coefficient map

Date: 2026-10-06

Status: **EXACT COEFFICIENT MAP FOR THE CURRENT RANK-FOUR SINE-SQUARE HEAT FLOW; T13 IS THE LARGEST EXPLICIT FOURIER-LEAKAGE COEFFICIENT**

No unconditional zero-density percentage is claimed here.

Use the current preferred rational band-conditioned sine-square parameters

    a=63/50,
    t=17/16.

The heat curvature is

    E_u'
      =
      Re E[
        A1 Xi_z
        +A2 Xi_zz
      ]
      +o(1),

with

    boxed:

    A1
      =
      a(-2t-it^2)
      =
      -1071/400
      -(18207/12800)i,

    A2
      =
      a^2 t^2
      =
      1147041/640000.

The exact resonant stencil is

    Xi_z
      =
      <r1,r2>/(3d)
      -T12/pi^2
      +<h1,h2>/d
      -[<r2,q1>+<r1,q2>]/(2d),

and

    Xi_zz
      =
      [<r2,r2>+2<r1,r3>]/(3d)
      -[T22+2T13]/pi^2
      +[<h2,h2>+2<h1,h3>]/d
      -[<r3,q1>+<r2,q2>+<r1,q3>]/d.

## 1. Exact map of every exposed scalar

The A1 block contributes:

    <r1,r2>:
      A1/3

    T12:
      -A1/pi^2

    <h1,h2>:
      A1

    <r2,q1>:
      -A1/2

    <r1,q2>:
      -A1/2.

The A2 block contributes:

    <r2,r2>:
      A2/3

    <r1,r3>:
      2A2/3

    T22:
      -A2/pi^2

    T13:
      -2A2/pi^2

    <h2,h2>:
      A2

    <h1,h3>:
      2A2

    <r3,q1>:
      -A2

    <r2,q2>:
      -A2

    <r1,q3>:
      -A2.

No other scalar statistic occurs in the exact one-point curvature.

## 2. Raw coefficient sizes

Numerically,

    |A1|
      ~=3.031879,

    A2
      ~=1.79225156.

Therefore the raw coefficient magnitudes are approximately:

    <r1,r2>       1.010626
    T12            0.307194
    <h1,h2>        3.031879
    each A1 rq     1.515939

    <r2,r2>        0.597417
    <r1,r3>        1.194834
    T22            0.181593
    T13            0.363186
    <h2,h2>        1.792252
    <h1,h3>        3.584503
    each A2 rq     1.792252.

Thus:

- among the three squared-Cauchy Fourier leakages, the largest explicit
  coefficient is

      boxed:
      T13

  with coefficient magnitude

      2A2/pi^2
        ~=0.363186;

- among the diagonal/Hilbert terms, the largest raw coefficient is

      boxed:
      <h1,h3>

  with coefficient

      2A2
        ~=3.584503.

This identifies the first two places to optimize before spending effort on
the smaller channels.

## 3. T22 and T13 are not independent

The Fourier terms satisfy the exact z-derivative identity

    boxed:

    partial_z T12
      =
      T22
      +2T13.

Therefore the entire Fourier contribution to the heat curvature is

    boxed:

    -1/pi^2
    Re E[
      A1 T12
      +A2 partial_z T12
    ].

So there are only two independent Fourier-channel objects:

    T12,
    partial_z T12,

not three unrelated arithmetic debts.

The T22/T13 split is useful only for low-rank channel bookkeeping.

## 4. Channel widths

Using

    rank[D,R^k]<=2k,

the exact Fourier pieces may be evaluated through:

    T12:
      2 x 4,

    T22:
      4 x 4,

    T13:
      2 x 6.

But the derivative combination

    T22+2T13

should be retained as one differentiated T12 object whenever possible, to
preserve cancellation.

## 5. Strategic consequence

Do not bound T22 and T13 independently unless forced.

The preferred order is:

1. keep
       A1 T12 + A2 partial_z T12
   intact;

2. use the 2x4 T12 factorization with the corrected S4 Fourier kernel and
   differentiate the resulting small channel analytically in z;

3. only split into 4x4 and 2x6 terms for a fail-closed norm estimate.

This avoids paying triangle-inequality loss exactly at the largest
Fourier-leakage coefficient.

## 6. Evidence boundary

Closed here:

- exact rational heat coefficients;
- exact coefficient map;
- exact derivative relation partial_z T12=T22+2T13;
- exact identification of the largest raw Fourier and diagonal coefficients.

Still open:

- a one-sided integrated bound on the combined small-channel trajectory.

No unconditional record theorem is claimed.

See:

    notes/WP84_DIRECT_DEGREE2_HEAT_CURVATURE_STENCIL.md
    notes/WP84_DIRECT_MPRIME_TAIL_O1_OVER_R.md
    notes/WP84_SINE_SQUARE_RANK4_ROUTE.md


## 7. Fourier-kernel correction

When T_ab is represented through **both** displacement commutators
[D,R^a] and [D,R^b], the correct scalar Fourier kernel is

    S4(t)
      =
      sum_{r!=0} e^(irt)/r^4,

not S2.

The reason is

    [D,R^a]_ij[D,R^b]_ij
      =
      (i-j)^2(R^a)_ij(R^b)_ij,

while T_ab already contains an additional 1/(i-j)^2.

Thus the commutator representation needs 1/(i-j)^4.

The channel sizes and the exact derivative identity

    partial_z T12=T22+2T13

remain unchanged.
