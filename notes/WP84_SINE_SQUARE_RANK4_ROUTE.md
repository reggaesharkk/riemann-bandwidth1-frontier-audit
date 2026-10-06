# WP84 — sine-square rank-four route

Date: 2026-10-06

Status: **EXACT GLOBAL SUPPORT-FREE FAMILY; ONE UPPER-HALF-PLANE POINT; ONE DERIVATIVE; DISPLACEMENT RANK AT MOST FOUR**

No unconditional zero-density percentage is claimed here.

For a>0 and t>0 define

    U_a=(H+iaI)(H-iaI)^(-1),
    S_a=(U_a-U_a^*)/(2i),
    Q_{a,t}=I-t S_a,
    P_{a,t}=Q_{a,t}^2.

For a real scalar x,

    S_a(x)=2ax/(x^2+a^2).

If x<=0 then S_a(x)<=0, hence Q_{a,t}(x)>=1 and P_{a,t}(x)>=1. For x>0, P_{a,t}(x)>=0. Therefore

    1-P_{a,t}(x) <= 1_{x>0}

globally. The support certificate is immediate and needs no Sturm calculation.

On the unit circle, P=(1-t sin theta)^2, so this is a degree-two trigonometric energy. At z=ia,

    tau P_{a,t}(H)
      =1+2 Re[ a(-2t-i t^2)m(ia)+a^2 t^2 m'(ia) ].

Also

    S_a=a[(H-iaI)^(-1)+(H+iaI)^(-1)],

so rank[D,S_a]<=4 and therefore rank[D,Q_{a,t}]<=4.

A simple rational pair close to the best conditioning found in reconnaissance is

    a=63/50,
    t=37/35.

Exact reduction against the pinned Christoffel model gives

    E_model
      =2123356554130375347858538674965521
       /17287082796917862060833277294351001
      =0.12282908452945869... .

Hence the model positive-index lower bound is 0.8771709154705413... and the model simple-zero ledger is

    75.43418309410826...%.

Against the conservative defect-energy ceiling 0.163249981456072..., the model margin is

    0.0404208969266133... .

For this family the explicit O(1/R) full-to-band constant is

    C_tail(a,t)
      =12/(pi^2 a^2)
       [ t sqrt(4+t^2)+(256/27)t^2 ].

At a=63/50,t=37/35,

    C_tail ~=9.9464075751,

so the margin-to-band-cost ratio is about 0.004063869. This improves the current reused-q a=4/3 ratio (about 0.003650775) by roughly 11.3%.

Useful residual margins after the band charge are approximately:

    R=256: 0.00156774
    R=320: 0.00933837
    R=400: 0.01555488
    R=512: 0.02099432

For the additive Gaussian bridge H_u=H_1+sqrt(u)W,

    d/du E tau P_{a,t}(H_u)
      =2 Re[ a(-2t-i t^2) C_u(ia)+a^2 t^2 partial_z C_u(ia) ].

Using C_u=(1/2)E Xi_z+o(1) and partial_z C_u=(1/2)E Xi_zz+o(1),

    E_u'
      =Re E[ a(-2t-i t^2) Xi_z+a^2 t^2 Xi_zz ]+o(1).

This is currently the simplest coefficient pattern for the rank-four one-point route.

Evidence boundary: exact support-free family, exact scalar form, exact rank bound, exact rational model value and explicit conditioning constant are closed. The large-T one-sided bounded-energy transport remains open.

See WP84_DIRECT_DEGREE2_HEAT_CURVATURE_STENCIL.md and WP84_DIRECT_DEGREE2_SCALE_CONDITIONING.md.


## 12. Exact four-column displacement generator

Let

    C_H=[D,H]=G_2 H_2^*

be any rank-two factorization of the sharp Loewner commutator.

Write

    R_+=(H-iaI)^(-1),
    R_-=(H+iaI)^(-1).

Since

    S_a=a(R_+ + R_-),

we have

    [D,R_+]
      =
      -R_+ C_H R_+,

    [D,R_-]
      =
      -R_- C_H R_-.

Therefore

    boxed:

    [D,Q_{a,t}]

      =
      t a
      [
        R_+ C_H R_+
        +R_- C_H R_-
      ].

Hence an explicit four-column factorization is

    boxed:

    [D,Q_{a,t}]
      =
      G_4 H_4^*,

with

    G_4
      =
      [
        t a R_+ G_2,
        t a R_- G_2
      ],

and block rows

    H_4^*
      =
      [
        H_2^* R_+;
        H_2^* R_-
      ].

This realizes the rank-four bound without any generic rank inequality.

## 13. Positive diagonal plus 4x4 Fourier energy

Because Q_{a,t} is Hermitian,

    tau(Q_{a,t}^2)

      =
      d^(-1)
      sum_i
        |Q_{ii}|^2

      +
      d^(-1)
      sum_{i!=j}
        |Q_{ij}|^2.

For i!=j,

    Q_{ij}
      =
      [D,Q]_{ij}/(i-j).

Also

    Q_{ii}
      =
      1
      -t a[
          (R_+)_{ii}
          +(R_-)_{ii}
        ]

      =
      1
      -2 t a
        Re (R_+)_{ii}.

Thus exactly

    boxed:

    tau(Q_{a,t}^2)

      =
      d^(-1)
      sum_i
        [
          1
          -2ta Re(R_+)_{ii}
        ]^2

      +
      d^(-1)
      sum_{i!=j}
        |[D,Q]_{ij}|^2/(i-j)^2.

Both terms are nonnegative.

Using the standard squared-Cauchy Fourier kernel S2(t), the second term is a
one-dimensional integral of a matrix channel of size at most 4x4.

Therefore the sine-square theorem also has a completely positive
displacement interface:

    one diagonal resolvent energy
      +
    one 4x4 Fourier energy.

This is the direct non-heat-flow route to test before expanding any
resolvent into prime words.


## 14. Superseding band-conditioning update

The original conditioning estimate in this note used the Cauchy-circle bound
for m'(ia).  That has now been superseded by direct differentiation of the
second resolvent identity.

The theorem-grade derivative comparison is

    |m_H'(z)-m_HR'(z)|
      <=
      18/(pi^2 eta^4 R)
      +o(R^-1)

in the sharp q_alpha=1/4 normalization.

Therefore the sine-square full-to-band constant improves to

    boxed:

    C_sine(a,t)

      =
      [
        12 t sqrt(4+t^2)
        +36 t^2
      ]
      /
      (pi^2 a^2).

This replaces the earlier

    12/(pi^2 a^2)
    [
      t sqrt(4+t^2)
      +(256/27)t^2
    ].

The continuous model-only conditioning optimum moves slightly to

    a~=1.26441,
    t~=1.06235.

A simple exact rational pair now preferred for the band-conditioned route is

    boxed:

    a=63/50,
    t=17/16.

At this pair the exact pinned-model defect energy is

    16936977322225889866362306131535233
    /
    138296662375342896486666218354808008

      =
      0.12246844595756208...,

giving model simple-zero ledger

    boxed:
    75.50631080848759...%.

The conservative defect margin is

    0.0407815354985099...,

while

    C_sine
      ~=4.43651377028.

Hence

    boxed:
    Delta/C_sine
      ~=0.00919224815.

This more than doubles the earlier explicit margin-to-band-cost ratio.

Residual margins after the full-to-band theorem charge are approximately:

    R=128: 0.00612127
    R=192: 0.01767469
    R=256: 0.02345140
    R=400: 0.02969025

So the prior t=37/35 point remains a valid exact certificate, but
a=63/50,t=17/16 is now the preferred fixed-band-conditioned sine-square
configuration.

See:

    notes/WP84_DIRECT_MPRIME_TAIL_O1_OVER_R.md
    src/wp84_direct_mprime_tail_o1_over_r_gate.py


## 15. Scope of the rank-four statement

The exact rank-four factorization

    [D,Q]
      =
      ta(
        R_+[D,H]R_+
        +R_-[D,H]R_-
      )

uses the full sharp identity

    rank[D,H]<=2.

A hard displacement truncation H_R does not preserve that rank-two
commutator. Therefore:

- rank[D,Q(H)]<=4 is a full-sharp statement;
- after replacing H by H_R, the O(1/R) scalar comparison remains valid, but
  the rank-four generator must not be reused for Q(H_R).

Keep the two routes distinct:

1. full sharp direct energy:
       exploit the exact rank-four/two-vector wedge;

2. fixed-band fallback:
       pay C_sine/R and use finite-band locality or moment bounds.

This scope separation is load-bearing.
