# WP84 — minimal-radius semicircle of exact-frontier rank-six consumers

Date: 2026-10-06

Status: **EXACT ONE-PARAMETER FULL-FRONTIER FAMILY; UNIT LARGE-NOISE NORMALIZATION; RANK AT MOST SIX; LARGE-T ARITHMETIC ESTIMATE STILL OPEN**

No unconditional zero-proportion theorem is claimed here.

The previous exact-frontier constructions used either the canonical purely
imaginary pole or the rational shifted point z=(4/5)(1+i).  The model
frontier is actually carried by a continuous one-parameter family of single
triple-pole consumers.  The family keeps the pole radius at the smallest
possible value allowed by the negative-half-line support condition.

This gives a shifted point with the improved heat conditioning of the rational
shift while restoring the exact boundary normalization E_infinity=1.

## 1. Christoffel cubic and minimal radius

Write

    P(x)=1-Ax+Bx^2-Cx^3,

with

    A=43428/13891,
    B=37704/13891,
    C=9660/13891.

Define

    boxed:

    r_*^3=1/C=13891/9660.

Thus

    r_*~=1.128718027835367645.

For any

    0<=c<r_*,

put

    a_c=sqrt(r_*^2-c^2),

    z_c=c+i a_c.

Define

    boxed:

    p_c(x)
      =
      r_*^6 P(x)^2
      /
      [((x-c)^2+a_c^2)^3],

and h_c=1-p_c.

Because c^2+a_c^2=r_*^2,

    p_c(0)=1.

At every positive Christoffel node x_j, P(x_j)=0, hence

    p_c(x_j)=0.

Also

    lim_|x|->infinity p_c(x)
      =
      r_*^6 C^2
      =
      1.

So every member of the family has the clean boundary normalization

    boxed:

    E_infinity=1.

## 2. Uniform exact half-line support certificate

Put x=-y, y>=0.  Since

    (y+c)^2+a_c^2
      =
      y^2+2cy+r_*^2,

the support numerator is

    N_c(y)
      =
      r_*^6(1+Ay+By^2+Cy^3)^2
      -(y^2+2cy+r_*^2)^3.

Its constant and y^6 coefficients vanish exactly.  The remaining coefficients
are

    [y] N_c
      =
      2 r_*^4(A r_*^2-3c),

    [y^2] N_c
      =
      r_*^2[
        (A^2+2B)r_*^4
        -12c^2
        -3r_*^2
      ],

    [y^3] N_c
      =
      2[
        (AB+C)r_*^6
        -4c^3
        -6c r_*^2
      ],

    [y^4] N_c
      =
      (2AC+B^2)r_*^6
      -12c^2
      -3r_*^2,

    [y^5] N_c
      =
      2[
        BC r_*^6
        -3c
      ].

Every displayed coefficient is decreasing in c on [0,r_*].  It is therefore
enough to check c=r_*.

The following elementary rational bounds hold:

    1<r_*<6/5,

    r_*^2>5/4.

They follow by cubing and using r_*^3=13891/9660.

At c=r_* the five positivity checks reduce to the sufficient rational
inequalities

    A>3,

    (A^2+2B)(5/4)>15,

    AB/C>9,

    (2AC+B^2)(25/16)>15,

    B/C>18/5.

All five are strict exact rational inequalities.

Therefore

    boxed:

    N_c(y)>=0
    for every y>=0
    and every 0<=c<=r_*.

Hence

    boxed:

    p_c(x)>=1
    for every x<=0,

and globally

    boxed:

    h_c(x)<=1_{x>0}.

No numerical root isolation or optimization is used in this support proof.

## 3. Every member hits the same exact Christoffel frontier

The frozen four-node extremal measure has mass

    w0=1415/13891

at x=0 and the remaining mass at the three positive zeros of P.

For every c in the family,

    p_c(0)=1,

    p_c(x_j)=0.

Therefore

    boxed:

    E_model[p_c]
      =
      1415/13891,

and the induced model simple-zero coefficient is always

    boxed:

    1-2w0
      =
      11061/13891
      =
      79.6270966813...%.

Thus moving the pole along the minimal-radius semicircle costs **zero**
Christoffel-model margin.

## 4. One positive rank-six energy for every c

For real-symmetric Hermitian H define

    boxed:

    Q_c
      =
      r_*^3
      P(H)
      (H-z_c I)^(-3).

Then

    Q_c^*Q_c=p_c(H).

Let

    U_c
      =
      (H-conjugate(z_c)I)
      (H-z_c I)^(-1).

Since P has degree three, Q_c is a degree-three polynomial q_c(U_c).
The sharp Loewner state has

    rank[D,U_c]<=2,

so

    boxed:

    rank[D,Q_c]<=6.

Moreover

    q_c(1)
      =
      -r_*^3 C
      =
      -1.

This is the operator reason every minimal-radius member has
E_infinity=1.

## 5. A cleaner shifted point

Take the simple horizontal shift

    boxed:

    c0=4/5,

and keep the radius minimal:

    boxed:

    a0
      =
      sqrt(
        r_*^2-16/25
      )
      ~=0.796243923908096.

So

    z0=4/5+i a0.

This differs slightly from the earlier rational point
z=(4/5)(1+i): the horizontal coordinate is unchanged, but the imaginary
coordinate is moved inward just enough to satisfy

    |z0|=r_*.

The earlier rational point had E_infinity~=1.0141849.  The new point has

    boxed:

    E_infinity=1

exactly.

The same one-point expansion

    tau p_c(H)
      =
      1
      +2 Re[
          A_c m(z_c)
          +B_c m'(z_c)
          +C_c m''(z_c)
        ]

holds.  At c0=4/5 the numerical coefficient diagnostics are

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

Hence

    |A_0|+|B_0|+|C_0|
      ~=2.81445697475,

compared with

    ~=2.85878

for the earlier rational shifted point.

The simple eta-weighted proxy

    |A|/eta
      +|B|/eta^2
      +2|C|/eta^3

is

    boxed:

    ~=4.36691919

at the minimal-radius c0 point, versus about 4.40132 for the earlier
rational shifted point and about 11.49346 for the canonical purely imaginary
point.

These proxy values are conditioning diagnostics only.  They are not theorem
bounds.

## 6. Strategic consequence

The exact-frontier one-point attack should no longer be viewed as choosing
between only

    z=i r_*

and

    z=(4/5)(1+i).

There is an exact admissible semicircle

    boxed:

    z_c=c+i sqrt(r_*^2-c^2),
    0<=c<r_*,

on which all of the following remain fixed:

- exact half-line support;
- exact model defect 1415/13891;
- exact model coefficient 79.6270966813...%;
- E_infinity=1;
- one triple pole;
- degree-three Cayley factor;
- displacement rank at most six.

Only the analytic conditioning changes with c.

The point c=4/5 is a convenient exact/algebraic default and is strictly
better conditioned by the current exposed heat proxies than both previous
exact-frontier representatives.

The remaining theorem is unchanged in nature:

    limsup_T tau p_c(H_T)<0.105

for the first >79 result, and

    limsup_T tau p_c(H_T)<=1415/13891

for the full frontier.

No member of the semicircle supplies that large-T inequality automatically.

## Evidence boundary

Closed here:

- exact one-parameter support certificate;
- exact unit boundary normalization on the whole family;
- exact Christoffel saturation;
- exact rank-six positive-energy architecture;
- improved one-point conditioning at c=4/5.

Open:

- theorem-grade large-T control of the actual zeta-side consumer;
- rigorous optimization of c against the complete grouped heat-curvature
  estimate rather than a proxy.

See:

    notes/WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.md
    notes/WP84_SHIFTED_EXACT_FRONTIER_RANK6.md
    notes/WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md
