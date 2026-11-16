# WP84 — shifted exact-frontier rank-six consumer with improved one-point conditioning

Date: 2026-10-06

Status: **EXACT SUPPORT-FREE BOUNDED CONSUMER HITTING THE FULL 79.62709668... CHRISTOFFEL MODEL FRONTIER; SHIFTED ONE-POINT POLE z=(4/5)(1+i); POSITIVE ENERGY; DISPLACEMENT RANK AT MOST SIX**

No unconditional zero-density percentage is claimed here.

The canonical exact-frontier consumer used the purely imaginary pole
`z=i a_*`, with `a_*^3=13891/9660`.  That choice has the attractive
normalization `p(x)->1` at infinity.

For the actual one-point heat-flow theorem, however, there is no requirement
that the pole have zero real part or that the large-noise boundary equal one.
The frozen Christoffel model is saturated whenever the defect equals one at
the zero atom and vanishes at the three positive Christoffel nodes.

This observation yields a better-conditioned exact-frontier point.

## 1. Exact shifted consumer

Let

    c=a=4/5,

    z=c+i a=(4/5)(1+i),

    r^2=c^2+a^2=32/25.

Define

    boxed:

    p_s(x)
      =
      r^6 P(x)^2
      /
      [
        ((x-c)^2+a^2)^3
      ],

and

    boxed:

    h_s(x)=1-p_s(x).

The denominator is strictly positive on the real line.

At x=0,

    ((-c)^2+a^2)^3
      =
      r^6,

so

    boxed:

    p_s(0)=1,
    h_s(0)=0.

At every positive Christoffel node x_j, P(x_j)=0, hence

    boxed:

    p_s(x_j)=0,
    h_s(x_j)=1.

Therefore this consumer hits the same frozen four-node model exactly.

## 2. Exact negative-half-line support certificate

Put x=-y, y>=0.  Then

    N_s(y)
      =
      r^6 P(-y)^2
      -
      [
        (y+c)^2+a^2
      ]^3.

The constant coefficient cancels exactly.  The remaining coefficients are

    y:
      1139171328/217046875,

    y^2:
      51666437692416/3014998140625,

    y^3:
      66705610299392/3014998140625,

    y^4:
      39343236454368/3014998140625,

    y^5:
      1879514557608/602999628125,

    y^6:
      1710697607/120599925625.

Every coefficient is strictly positive.

Therefore

    boxed:

    N_s(y)>=0
    for every y>=0,

with equality only at y=0.

Hence

    p_s(x)>=1
    for every x<=0.

For x>0, p_s(x)>=0 trivially.  Thus globally

    boxed:

    h_s(x)
      <=
      1_{x>0}.

This is a finite exact coefficient-sign certificate.

## 3. Exact full-frontier model value

Because h_s is zero at the zero atom and one at all three positive
Christoffel nodes,

    boxed:

    E_model[p_s]
      =
      w0
      =
      1415/13891,

and

    boxed:

    2 E_model[h_s]-1
      =
      11061/13891
      =
      79.6270966813...%.

Thus the shifted point loses no model frontier at all.

The >79 defect cushion is the same exact quantity as for the canonical
frontier consumer:

    boxed:

    0.105-w0
      =
      8711/2778200
      =
      0.00313548340652221....

## 4. Positive one-point factor

Define

    boxed:

    Q_s
      =
      r^3
      P(H)
      (H-zI)^(-3),

with

    r^3=128 sqrt(2)/125.

Then

    boxed:

    Q_s^*Q_s
      =
      p_s(H).

Therefore

    tau h_s(H)
      =
      1-tau(Q_s^*Q_s).

The theorem is again one positive-energy inequality.

## 5. Exact shifted Cayley polynomial

Let

    U_s
      =
      (H-conjugate(z) I)
      (H-z I)^(-1)

      =
      (H-cI+i a I)
      (H-cI-i a I)^(-1).

Then

    Q_s=q_s(U_s),

where the exact degree-three polynomial is

    boxed:

    q_s(u)
      =
      sqrt(2)/1389100
      [
        (-90672+273989 i)

        +(-403920+107313 i)u

        +(-403920-107313 i)u^2

        +(-90672-273989 i)u^3
      ].

The coefficients satisfy

    q_k=conjugate(q_{3-k}),

so the same self-inversive/skew-displacement symmetry is present.

Since

    rank[D,U_s]<=2,

the cubic commutator identity gives

    boxed:

    rank[D,Q_s]<=6.

Thus the exact full-frontier state remains a six-column displacement problem.

## 6. Large-noise boundary

Unlike the canonical point, this shifted consumer does not tend to unit
defect at infinity.

Exactly,

    boxed:

    E_infinity
      =
      lim_{|x|->infinity} p_s(x)

      =
      r^6 C^2

      =
      122310623232/120599925625

      =
      1.01418489769487368....

This is harmless: the co-moving heat-flow identity becomes

    E_0
      =
      E_infinity
      -
      int_0^infinity E_u' du.

The >79 target is

    int_0^infinity E_u' du
      >
      E_infinity-0.105,

and the full-frontier target is

    int_0^infinity E_u' du
      >=
      E_infinity-w0-o(1).

The model cushion between those two thresholds remains exactly
`0.105-w0`.

## 7. Exact one-point heat coefficients

At the single spectral point

    z=(4/5)(1+i),

write

    m(z)=d^(-1)tr(H-zI)^(-1).

Then

    boxed:

    tau(Q_s^*Q_s)

      =
      E_infinity

      +2 Re[
          A_s m(z)
          +B_s m'(z)
          +C_s m''(z)
        ],

with exact coefficients

    A_s
      =
      -183845781504/120599925625
      +i 112029847146/602999628125,

    B_s
      =
      297763801992/602999628125
      -i 623773801728/602999628125,

    C_s
      =
      1589960358912/15074990703125
      +i 2139153937184/15074990703125.

Numerically,

    A_s ~= -1.52442698908 +0.18578758911 i,

    B_s ~=  0.49380428794 -1.03445138709 i,

    C_s ~=  0.10547007227 +0.14190084620 i.

The raw exposed coefficient norm is

    boxed:

    |A_s|+|B_s|+|C_s|
      ~=2.85878.

For the canonical exact-frontier point `z=i a_*`, the corresponding norm is
about `13.0089`.

A simple resolvent-scale weighted proxy

    |A|/eta
      +|B|/eta^2
      +2|C|/eta^3

is approximately

    shifted point:
      4.40132,

    canonical point:
      11.49346.

These are conditioning diagnostics, not theorem bounds.  They show that the
smaller imaginary part eta=4/5 is more than compensated in this first exposed
one-point stencil by much smaller coefficients.

## 8. Strategic consequence

There are now two exact-frontier rank-six consumers:

1. canonical:
       z=i a_*,
       eta~=1.12872,
       E_infinity=1;

2. shifted conditioned:
       z=(4/5)(1+i),
       eta=0.8,
       E_infinity~=1.01418,
       substantially smaller one-point heat coefficients.

Both have:

- exact half-line support;
- exact model value 79.6270966813...%;
- one positive energy;
- one fixed nonreal point;
- degree-three Cayley form;
- displacement rank at most six.

The shifted point should therefore be carried as the preferred conditioning
candidate for the six-channel heat-flow attack, while the canonical point is
retained as the cleaner normalization cross-check.

No large-T theorem is claimed until the actual positive-energy/heat-curvature
inequality is proved.

## Evidence boundary

Closed here:

- exact rational support numerator and coefficient positivity;
- exact Christoffel-model saturation;
- exact full-frontier model coefficient;
- exact shifted one-point factor;
- exact degree-three Cayley polynomial;
- exact rank-six displacement ceiling;
- exact large-noise boundary;
- exact m,m',m'' coefficient map.

Open:

- theorem-grade large-T control at z=(4/5)(1+i);
- comparison of the complete differentiated T12 channel against the canonical
  point using rigorous, not proxy, bounds.

See:

    notes/WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.md
    notes/WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md
    notes/WP84_CONDITIONED_RANK6_79_CONSUMER.md
