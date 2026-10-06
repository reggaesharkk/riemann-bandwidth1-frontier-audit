# WP84 — grouped one-point heat stencil on the minimal-radius frontier

Date: 2026-10-06

Status: **EXACT ONE-POINT COEFFICIENT FORMULAS AND GROUPED CURVATURE TARGET; LARGE-T ONE-SIDED ESTIMATE OPEN**

No unconditional zero-proportion theorem is claimed here.

Use the minimal-radius family

    r_*^3=1/C=13891/9660,

    z=c+i a,

    c^2+a^2=r_*^2,

    Q=r_*^3 P(H)(H-zI)^(-3),

    p_c(H)=Q^*Q.

Because r_*^3 C=1, the scalar defect tends to one at infinity.

## 1. Exact partial-fraction coefficients from one pole

For real x,

    p_c(x)
      =
      r_*^6 P(x)^2
      /
      [(x-z)^3(x-conjugate(z))^3].

Write

    p_c(x)
      =
      1
      +2 Re[
          A_c/(x-z)
          +B_c/(x-z)^2
          +D_c/(x-z)^3
        ].

Put

    Delta=z-conjugate(z)=2 i a.

Then the upper-pole Laurent coefficients are exactly

    boxed:

    D_c
      =
      r_*^6 P(z)^2/Delta^3,

    B_c
      =
      r_*^6[
        2P(z)P'(z)/Delta^3
        -3P(z)^2/Delta^4
      ],

    A_c
      =
      r_*^6[
        (P'(z)^2+P(z)P''(z))/Delta^3
        -6P(z)P'(z)/Delta^4
        +6P(z)^2/Delta^5
      ].

Since

    m''(z)
      =
      2 int (x-z)^(-3) dnu(x),

the coefficient multiplying m'' is

    boxed:

    C_c=D_c/2.

Therefore, for every Hermitian H,

    boxed:

    tau p_c(H)
      =
      1
      +2 Re[
          A_c m_H(z)
          +B_c m_H'(z)
          +C_c m_H''(z)
        ].

This derives the one-point coefficients directly from P and the pole.  No
Cayley-Fourier coefficient expansion is needed.

As a quick exact consistency check, comparison of the 1/x term at infinity
gives

    boxed:

    Re A_c
      =
      3c-B/C.

For c=4/5 this is exactly

    Re A_c
      =
      -242/161
      =
      -1.5031055900621118....

## 2. Minimal-radius c=4/5 point

Use

    c0=4/5,

    a0=sqrt(r_*^2-16/25)
      ~=0.796243923908096.

Then

    A_0
      ~=
      -1.503105590062112
      +0.177236537154552 i,

    B_0
      ~=
       0.490463373514631
      -1.014959437692106 i,

    C_0
      ~=
       0.102814015087646
      +0.139986335625773 i.

The rigorous Cauchy-envelope coefficient is

    K_Cauchy
      =
      |A_0|/a0
      +|B_0|/a0^2
      +2|C_0|/a0^3

      ~=4.36691919.

Indeed

    |m(z)|<=1/a,
    |m'(z)|<=1/a^2,
    |m''(z)|<=2/a^3

for every Hermitian state.  The displayed K_Cauchy is therefore a genuine
uniform resolvent-conditioning constant, although by itself it is much too
crude to prove the desired consumer bound.

## 3. Grouped Gaussian curvature

For the co-moving Gaussian Loewner bridge, the already-established resonant
primitive gives

    partial_u m_u(z)
      =
      (1/2) E Xi_z(R_u(z))
      +o(1).

Differentiating in z and inserting the exact one-point representation yields

    boxed:

    E_u'
      =
      Re E[
        A_c Xi_z
        +B_c Xi_zz
        +C_c Xi_zzz
      ]
      +o(1).

At c=c0 this is the active minimal-radius stencil.

The complete Fourier leakage must remain grouped as

    boxed:

    -(1/pi^2)
    Re E[
      A_0 T12
      +B_0 partial_z T12
      +C_0 partial_z^2 T12
    ].

Do not replace the three terms by separate absolute values before exploiting
their common displacement/Fourier channel.

The remaining diagonal/J terms are the corresponding grouped combination of
the exact Xi_z, Xi_zz, Xi_zzz formulas already recorded in
WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md.

## 4. Integrated theorem targets regain the clean canonical boundary

Because E_infinity=1 exactly on the minimal-radius family,

    E_0
      =
      1
      -
      int_0^infinity E_u' du

at finite dimension.

Hence the first >79 target is again simply

    boxed:

    int_0^infinity E_u' du
      >
      0.895.

The frozen model endpoint gives

    1-w0
      =
      12476/13891
      =
      0.8981354834065222...,

so the exact curvature cushion remains

    boxed:

    8711/2778200
      =
      0.00313548340652221....

For the full frontier it is enough to prove

    boxed:

    int_0^infinity E_u' du
      >=
      12476/13891
      -o(1).

Thus the minimal-radius shift keeps the improved one-point conditioning while
removing the previous shifted point's E_infinity>1 normalization.

## 5. Evidence boundary

Closed:

- exact one-pole Laurent coefficients;
- exact one-point m,m',m'' representation;
- exact grouped Xi_z/Xi_zz/Xi_zzz heat stencil;
- exact grouped differentiated-T12 channel;
- exact E_infinity=1 integrated thresholds.

Open:

- a one-sided large-T estimate of the grouped stencil;
- a theorem-grade finite-u state bound strong enough to use the
  0.00313548 cushion;
- final background/taper/zero-count transfer after that estimate.

See:

    notes/WP84_MINIMAL_RADIUS_EXACT_FRONTIER_FAMILY.md
    notes/WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md
    notes/WP84_SHIFTED_K2_GRAM_CANCELLATION.md
