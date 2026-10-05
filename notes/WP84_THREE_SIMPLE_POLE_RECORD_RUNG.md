# WP84 — three-simple-pole minorant supersedes r2 as the best-conditioned first strike

Date: 2026-10-05

Status: **EXACT GLOBAL MINORANT + EXACT MODEL CERTIFICATE; THREE SIMPLE UPPER-HALF-PLANE POLES ONLY**

No unconditional zero-density percentage is claimed here.

The recent r2 architecture improved the theorem state dramatically, but it still consumes one repeated pole through m'(ia).

There is a cleaner bounded minorant using only three simple imaginary poles.

Define

    D(x)
      = (x^2+1)(x^2+9)(x^2+36),

    Q(x)
      = x^3 - 20x^2 + (81/2)x - 18,

and

    boxed:
    f_3(x)
      = 1 - Q(x)^2/D(x).

## 1. Global support-free minorant

For x>0,

    f_3(x)<=1

immediately because D(x)>0 and Q(x)^2>=0.

For x=-y<=0,

    Q(-y)
      = -[
          y^3 + 20y^2 + (81/2)y + 18
        ].

Also

    D(-y)
      =
      (y^2+1)(y^2+9)(y^2+36).

A direct expansion gives

    [y^3+20y^2+(81/2)y+18]^2
      - D(y)

      =
      40 y^5
      + 435 y^4
      + 1656 y^3
      + (7965/4) y^2
      + 1458 y,

which is nonnegative for y>=0.

Therefore

    Q(x)^2 >= D(x)
    for x<=0,

so

    boxed:
    f_3(x)<=0
    for x<=0.

Hence

    boxed:
    1_{x>0} >= f_3(x)

for every real x.

## 2. Only three simple poles

The exact partial-fraction formula is

    f_3(x)

      =
      -(632x-6225)/
        [1120(x^2+1)]

      + 27(56x+95)/
        [32(x^2+9)]

      - 9(26x+2025)/
        [35(x^2+36)].

Equivalently,

    boxed:
    f_3(H)
      =
      2 Re[
        c_1 (H-iI)^(-1)
        + c_3 (H-3iI)^(-1)
        + c_6 (H-6iI)^(-1)
      ],

with exact upper-half-plane residues

    c_1
      = -79/280 - (1245/448)i,

    c_3
      = 189/8 - (855/64)i,

    c_6
      = -117/35 + (1215/28)i.

There are no repeated poles and no z-derivatives.

The minimum pole height is exactly

    eta_min=1.

## 3. Exact pinned model value

Against the current exact four-node Christoffel model,

    boxed:

    q_3
      =
      120853387254098829282930524740
      /
      136197874685286537177311582089

      =
      0.8873368070783458....

The corresponding model simple-zero ledger is

    boxed:

    2q_3-1

      =
      105508899822911121388549467391
      /
      136197874685286537177311582089

      =
      0.7746736141566918....

So this rung has model simple-zero value

    77.4673614157...%.

This remains a model/consumer value only.

## 4. Record margin

Against the conservative positive-index record threshold

    q_rec
      =
      0.8367500185439279...,

the model consumer margin is

    boxed:

    Delta_3
      =
      0.0505867885344179....

This is larger than:

    r2,a=1 margin:
      0.0466326939503807...,

    r2,a=6/5 margin:
      0.03781247717645....

## 5. O(1/R) displacement-tail conditioning

The one-point resolvent-tail theorem gives

    |
      m_H(ia)-m_HR(ia)
    |

      <=
      6/(pi^2 a^3 R)
      +o(R^-1)

for each fixed pole ia.

Since f_3 uses only simple resolvents,

    |
      tau f_3(H)
      -
      tau f_3(H_R)
    |

      <=
      C_3/R
      +o(R^-1),

where

    C_3
      =
      12/pi^2
      [
        |c_1|/1^3
        + |c_3|/3^3
        + |c_6|/6^3
      ]

      =
      4.8634168148....

Therefore the raw band-conditioning ratio is

    boxed:

    Delta_3/C_3
      ~= 0.01040149.

For comparison, the current r2,a=6/5 O(1/R) ratio is only about 0.00382.

So under the present band-tail architecture, the three-simple-pole rung is
substantially better conditioned.

## 6. Why this is strategically cleaner than r2

The theorem consumes only

    m(i),
    m(3i),
    m(6i).

It does not require:

- m'(i);
- a Cauchy circle;
- repeated-pole derivative control;
- the r2 Cayley-square identity.

Every active Bernoulli/Gaussian/resolvent invariance theorem already applies
directly to fixed simple nonreal poles.

The large pole heights 3 and 6 are especially cheap analytically; only the
z=i point pays the worst resolvent constant.

## 7. The construction is not an LP artifact

The family behind this certificate is

    f(x)
      =
      1-Q(x)^2/
        prod_j (x^2+a_j^2),

with monic cubic

    Q(x)
      =
      x^3-Ax^2+Bx-c,

    c=a_1 a_2 a_3.

For x=-y<=0, the minorant condition follows whenever

    A>0,
    B>0,

    A^2+2B
      >=
      a_1^2+a_2^2+a_3^2,

    B^2+2Ac
      >=
      a_1^2a_2^2
      +a_1^2a_3^2
      +a_2^2a_3^2.

The choice

    (a_1,a_2,a_3)
      =
      (1,3,6),

    A=20,
    B=81/2

satisfies these inequalities with very large exact slack.

Thus the global minorant is certified algebraically.

## 8. New first-strike recommendation

The current ordering should now be:

1. three-simple-pole f_3 rung:
       model simple ledger 77.46736...%;
       poles i,3i,6i;
       no derivatives;
       largest current proof-conditioning ratio;

2. r2,a=1:
       model simple ledger 76.67654...%;
       one pole plus one derivative;

3. r2,a=6/5:
       model simple ledger 74.91250...%;
       better than a=1 for the r2-specific band constant;

4. six-pole Christoffel family:
       model simple target 79.62710...%.

Do not claim any of these as unconditional until the local arithmetic /
bounded-resolvent transport is completely closed.

The immediate analytic target should be the finite-local law for the three
simple Stieltjes values at

    z=i, 3i, 6i,

because this is now a cleaner record-crossing interface than the repeated-pole
r2 consumer.

See:

    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
    notes/WP84_R2_FINITE_BAND_LOCALITY.md
    notes/WP84_RESOLVENT_KILL_GATE_2026_10_05.md
