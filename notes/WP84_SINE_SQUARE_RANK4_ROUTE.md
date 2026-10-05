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
