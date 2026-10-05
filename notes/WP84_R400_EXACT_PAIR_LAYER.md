# WP84 — exact fixed-band pair sector at R=400

Date: 2026-10-05

Status: **SOURCE-CLOSED SECOND-COVARIANCE CALCULATION; THE COMPLETE FIXED-BAND PAIR LAYER IS STRICTLY BELOW 4/15**

No unconditional zero-density percentage is claimed here.

The centered-fourth scalar gate only needs an upper bound on

    w_R=tau(P_R^4).

Its complete pair-pair sector depends only on the already-closed resonant
second covariance of the sharp prime field.

For the hard displacement band

    |i-j|<=R,

that pair contribution can be computed explicitly.

## 1. Resonant covariance input

Use the source-closed continuum covariances

    E alpha_i alpha_j
      = (1/4) delta_ij,

    E alpha_i beta_j
      =0,

    E beta_i beta_j
      =
      1/6                      if i=j,

      -1/[2 pi^2(i-j)^2]       if i!=j.

The banded centered prime operator is

    P_R
      =
      M_beta+[M_alpha,J_R],

where

    (J_R)_{ij}
      =
      1/[pi(j-i)]

for

    0<|i-j|<=R,

and zero otherwise.

The pair-pair fourth sector is exactly the Wick contraction of this second
covariance.  This statement concerns only the pair sector; it does not assume
the full field is Gaussian.

## 2. Adjacent/nested pairing

Let

    H2(R)=sum_{r=1}^R 1/r^2.

Define the finite odd harmonic polynomial

    h_R(theta)
      =
      sum_{0<|r|<=R}
        e^{ir theta}/r.

The Toeplitz matrix

    B_R=E[P_R^2]

has symbol

    b_R(theta)
      =
      1/6
      +
      1/(4 pi^2)
      [
        |h_R(theta)|^2
        +2 H2(R)
      ].

Therefore the adjacent pairing is

    boxed:

    t_adj(R)
      =
      (1/(2pi))
      int_0^(2pi)
        b_R(theta)^2 dtheta.

For an exact finite-sum form define

    E4(R)
      =
      (1/(2pi))
      int_0^(2pi)
        |h_R(theta)|^4 dtheta.

Then

    boxed:

    t_adj(R)

      =
      1/36
      +H2(R)/(3 pi^2)
      +
      [
        E4(R)+12 H2(R)^2
      ]
      /(16 pi^4).

All quantities except pi are rational finite sums.

## 3. Exact rational formula for E4(R)

Let

    H1(n)=sum_{j=1}^n 1/j.

The convolution coefficient

    s_r
      =
      sum_{
        0<|j|<=R,
        0<|r-j|<=R
      }
      1/[j(r-j)]

is

for 1<=r<=R,

    s_r
      =
      (2/r)
      [
        H1(r-1)
        +H1(R)
        -H1(r)
        -H1(R-r)
      ],

and for R<r<=2R,

    s_r
      =
      (2/r)
      [
        H1(R)
        -H1(r-R-1)
      ].

Since the zero convolution coefficient is

    -2 H2(R),

Parseval gives exactly

    boxed:

    E4(R)
      =
      4 H2(R)^2
      +
      2 sum_{r=1}^{2R} s_r^2.

Thus t_adj(R) is explicitly computable with rational arithmetic plus pi.

## 4. Crossing pairing

Put

    H4(R)=sum_{r=1}^R 1/r^4.

A direct covariance-tensor contraction gives

    boxed:

    t_opp(R)

      =
      1/36
      +
      H2(R)^2/(2 pi^4)
      -
      3 H4(R)/(4 pi^4).

The three pieces have a transparent provenance:

- diagonal beta-beta crossing;
- alpha-alpha shared-endpoint crossing;
- alpha-beta covariance correction through the nonlocal beta covariance.

As R->infinity this tends to

    1/30.

## 5. Complete fixed-band pair layer

The six A^2 B^2 words still split in the exact ratio 4:2, so

    boxed:

    Pair_R
      =
      2 t_adj(R)+t_opp(R).

Equivalently,

    Pair_R
      =
      1/12
      +
      [2 H2(R)/(3 pi^2)]

      +
      1/pi^4
      [
        E4(R)/8
        +2 H2(R)^2
        -3 H4(R)/4
      ].

This formula is exact in the infinite-volume fixed-R limit.

## 6. Exact R=400 certificate

The companion checker evaluates every harmonic sum with Fraction arithmetic.

It does not import a floating value of pi.

Instead it proves a rational enclosure for pi from Machin's formula

    pi
      =
      16 arctan(1/5)
      -4 arctan(1/239)

using alternating-series upper and lower bounds.

Because every coefficient of

    x=1/pi^2

in Pair_R is positive at R=400, the lower rational bound for pi gives a
rigorous upper bound for Pair_400.

The exact acceptance test is

    boxed:

    Pair_400
      <
      266329/1000000

      =
      0.266329.

Numerically,

    Pair_400
      =
      0.2663281218989228....

For comparison,

    4/15
      =
      0.2666666666666666....

So the hard fixed band actually lowers the complete pair layer by about

    0.00033854477.

## 7. Updated positive error budget at R=400

The centered-fourth theorem ceiling is

    W_400
      ~=0.2911227517.

Using the certified pair bound

    Pair_400<0.266329

leaves at least

    boxed:

    0.2911227517-0.266329
      >
      0.0247937

for every positive non-pair / finite-compression error.

Using the numerical exact pair value gives about

    0.0247946298.

This is slightly stronger than budgeting against the full 4/15 pair layer.

## 8. Evidence boundary

Closed here:

- the entire fixed-band pair sector;
- no almost-prime correlation theorem is used;
- no Gaussianity of the full state is assumed;
- only the already-closed second covariance is consumed.

Still open:

- the finite-compression connected/non-pair sector.

The new pointwise theorem

    C4<=0

shows its exact closed-cycle main cannot increase the fourth moment.

Thus the remaining arithmetic theorem only has to keep the positive
near-resonant leakage below the approximately 0.02479 R=400 budget.

See:

    notes/WP84_CENTERED_M4_SCALAR_GATE.md
    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
    notes/WP84_M4_LINDEBERG_WORD_ATTACK.md
