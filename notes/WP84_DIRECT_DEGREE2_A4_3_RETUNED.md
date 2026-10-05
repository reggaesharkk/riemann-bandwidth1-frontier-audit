# WP84 — retuned direct degree-two Cayley square at a=4/3

Date: 2026-10-06

Status: **EXACT GLOBAL HALF-LINE CERTIFICATE; SAME ONE-POINT RANK-FOUR ARCHITECTURE WITH SUBSTANTIALLY BETTER SCALE-CONDITIONED MODEL ENERGY**

No unconditional zero-density percentage is claimed here.

The first scale-conditioning pass reused the a=1 degree-two polynomial q at
a=4/3.  That improved the pole-gap constants but left model energy

    0.12289284898....

The degree-two square can be retuned at the new scale.

Define

    a=4/3,

    U_a
      =
      (H+iaI)(H-iaI)^(-1),

and

    boxed:

    q_{4/3}(u)
      =
      1/1000 [
        773 u^2
        +(376-1361 i)u
        -(664+397 i)
      ].

Put

    Q=q_{4/3}(U_a),

    h(H)=I-Q^*Q.

## 1. Exact half-line certificate

For real x,

    |q_{4/3}(U_a(x))|^2-1

      =
      N(x)
      /
      [
        1000000
        (9x^2+16)^2
      ],

where

    boxed:

    N(x)
      =
      188388909 x^4
      -1174517712 x^3
      +1517576544 x^2
      -1145293056 x
      +149760.

The denominator is strictly positive.

Exact Sturm count gives

    boxed:
    N has zero real roots on (-infinity,0].

Also

    N(0)=149760>0.

Therefore

    |q_{4/3}(U_a(x))|^2>=1

for every x<=0.

For x>0 the defect square is automatically nonnegative.

Hence globally

    boxed:

    1-|q_{4/3}(U_a(x))|^2
      <=
      1_{x>0}.

This is an exact support-free bounded minorant.

## 2. Exact pinned-model energy

Exact reduction against the pinned Christoffel cubic gives

    boxed:

    E_model

      =
      2425080141045661660562746421
      /
      21513987578630813262384200000

      =
      0.11272109050831747....

Therefore the model positive-index lower bound is

    boxed:
    0.8872789094916825...,

and the corresponding model simple-zero ledger is

    boxed:

    77.45578189833651...%.

This is a model benchmark only.

## 3. Conservative record margin

Against

    E_rec
      =
      0.163249981456072...,

the direct defect-energy margin is

    boxed:

    Delta_{4/3,new}
      =
      0.0505288909477545....

The theorem-conditioning metric is

    boxed:

    a^2 Delta
      =
      (16/9) Delta
      =
      0.0898291394626747....

For comparison, the previous a=1 direct square had

    a^2 Delta
      =
      0.0552157468160738....

So the retuned a=4/3 square improves the explicit margin-versus-a^-2
fixed-pole metric by approximately

    boxed:
    62.7%.

This supersedes the earlier reused-q a=4/3 conditioning note as the preferred
direct-square scale.

## 4. Rank-four structure survives

Because q_{4/3} has degree two,

    [D,Q]

      =
      [D,U_a]
        (
          q_1 I+q_2 U_a
        )

      +q_2
        U_a [D,U_a].

Since

    rank[D,U_a]<=2

for the sharp Loewner state,

    boxed:
    rank[D,Q]<=4.

Thus the structural theorem state is unchanged:

    one spectral point z=4i/3,
    degree two,
    one positive energy,
    displacement rank at most four.

## 5. Exact scalar repeated-pole representation

The polynomial itself has the resolvent form

    boxed:

    Q

      =
      (
        97/200
        -879 i/500
      ) I

      +
      (
        1361/375
        +1922 i/375
      )
      R(4i/3)

      -
      6184/1125
      R(4i/3)^2.

The energy Fourier coefficients give

    boxed:

    tau(Q^*Q)

      =
      3325789/1000000

      +2 Re[
          A_* m(4i/3)
          +B_* m'(4i/3)
        ],

where

    boxed:

    A_*
      =
      -2718791/375000
      -445243 i/375000,

    B_*
      =
      513272/140625
      -306881 i/140625.

So the improved square keeps exactly the same one-point / first-derivative
analytic interface.

## 6. Gaussian heat-flow form

For the additive Gaussian bridge

    H_u=H_1+sqrt(u)W,

put

    m_u(z)
      =
      E tau(H_u-zI)^(-1),

    C_u(z)
      =
      partial_u m_u(z).

Then

    boxed:

    E_u'

      =
      2 Re[
        A_* C_u(4i/3)
        +B_* partial_z C_u(4i/3)
      ].

The finite-d infinite-noise boundary is

    boxed:

    E_infinity
      =
      |q_{4/3}(1)|^2
      =
      3325789/1000000
      =
      3.325789.

Thus

    E_0
      =
      3.325789

      -
      2 Re
      int_0^infinity
        [
          A_* C_u(4i/3)
          +B_* partial_z C_u(4i/3)
        ]
      du.

The record crossing requires the integrated curvature to exceed

    boxed:

    3.325789
      -
      0.163249981456072...

      =
      3.162539018543928....

The model endpoint corresponds to a larger integrated value by exactly the
energy margin

    0.0505288909477545....

## 7. Current route hierarchy

Primary direct-square route:

    a=4/3,
    retuned degree-two q,
    model simple ledger 77.45578...%,
    one point,
    one derivative,
    rank four,
    scale-conditioned margin metric 0.0898291....

Raw-margin comparison:

    a=1 old q,
    model simple ledger 78.39315...%,
    margin metric 0.0552157....

The a=1 route still has the slightly larger raw model ledger, but the retuned
a=4/3 route is now substantially better under the explicit a^-2 fixed-pole
conditioning metric.

## 8. Evidence boundary

Closed here:

- exact rational degree-two q at a=4/3;
- exact half-line Sturm certificate;
- exact pinned-model energy;
- exact scalar resolvent coefficients;
- exact rank-four persistence;
- exact finite-d heat-flow identity.

Still open:

- the large-T one-sided energy transport / heat-curvature integral bound.

No unconditional record theorem is claimed.

See:

    notes/WP84_DIRECT_DEGREE2_CAYLEY_SQUARE.md
    notes/WP84_DIRECT_DEGREE2_HEAT_CURVATURE_STENCIL.md
    notes/WP84_DIRECT_DEGREE2_SCALE_CONDITIONING.md
