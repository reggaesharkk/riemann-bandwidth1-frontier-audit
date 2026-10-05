# WP84 — two-simple-pole first-strike minorant

Date: 2026-10-05

Status: **EXACT GLOBAL MINORANT + EXACT MODEL CERTIFICATE; ONLY TWO SIMPLE UPPER-HALF-PLANE STIELTJES VALUES**

No unconditional zero-density percentage is claimed here.

The three-simple-pole rung is already cleaner than the repeated-pole r2 consumer.

A still smaller record-beating consumer exists with only two simple imaginary poles.

Define

    D(x)
      = (x^2+1)(x^2+81/16),

    Q(x)
      = x^2 -(17/5)x + 9/4,

and

    boxed:
    f_2(x)
      = 1 - Q(x)^2/D(x).

## 1. Global support-free minorant

For x>0,

    f_2(x)<=1

because D(x)>0.

For x=-y<=0,

    Q(-y)
      = y^2 +(17/5)y +9/4.

A direct exact expansion gives

    [y^2 +(17/5)y +9/4]^2
      -(y^2+1)(y^2+81/16)

      =
      y(
        2720 y^2
        +3999 y
        +6120
      )/400

      >=0.

Therefore

    Q(x)^2>=D(x)
    for x<=0,

so

    f_2(x)<=0
    for x<=0.

Hence

    boxed:
    1_{x>0} >= f_2(x)

for every real x.

## 2. Only two simple poles

The exact partial-fraction decomposition is

    f_2(x)

      =
      (3400x+3999)/
        [1625(x^2+1)]

      + 9(13600x-35991)/
        [1625(16x^2+81)].

Equivalently,

    boxed:

    f_2(H)
      =
      2 Re[
        c_1 (H-iI)^(-1)
        + c_{9/4}(H-(9/4)i I)^(-1)
      ],

with exact upper-half-plane residues

    c_1
      = 68/65
        -(3999/3250)i,

    c_{9/4}
      = 153/65
        +(35991/13000)i.

No z derivative is consumed.

The minimum pole height is

    eta_min=1.

## 3. Exact pinned model value

Against the pinned four-node Christoffel model,

    boxed:

    q_2
      =
      298046731976058910350368
      /
      343933139638869493768225

      =
      0.8665833489875636....

The corresponding model simple-zero ledger is

    boxed:

    2q_2-1

      =
      252160324313248326932511
      /
      343933139638869493768225

      =
      0.7331666979751273....

So the model rung is

    73.3166697975...%.

This remains a model/consumer value only.

## 4. Record margin

Against the conservative positive-index threshold

    q_rec
      =
      0.8367500185439279...,

the model consumer margin is

    boxed:

    Delta_2
      =
      0.0298333304436357....

That is smaller than the three-pole raw margin, but the theorem consumes one
fewer pole and has significantly smaller resolvent-tail conditioning cost.

## 5. O(1/R) displacement-tail conditioning

For a simple pole ia, the sharpened displacement theorem gives

    |
      m_H(ia)-m_HR(ia)
    |

      <=
      6/(pi^2 a^3 R)
      +o(R^-1).

Therefore

    |
      tau f_2(H)
      -
      tau f_2(H_R)
    |

      <=
      C_2/R
      +o(R^-1),

where

    C_2
      =
      12/pi^2
      [
        |c_1|
        + |c_{9/4}|/(9/4)^3
      ]

      =
      2.3515890423....

Thus

    boxed:

    Delta_2/C_2
      ~= 0.01268646.

This is better than:

    three-simple-pole (1,3,6):
      ~0.01040;

    r2,a=6/5:
      ~0.00382.

So under the current explicit O(1/R) theorem constants, this two-pole rung is
the best-conditioned first record crossing among the current exact consumers.

## 6. Minimality within the present simple-pole hierarchy

A single simple-pole support-free member

    r_{1,a}(x)
      = 2ax/(x^2+a^2)

does not reach the audited record in the pinned model at the tested optimum
near a=1.

The present f_2 rung shows that **two simple poles suffice**.

So the first theorem target can now be phrased using only

    m(i),
    m(9i/4).

There is no derivative and no third spectral point.

## 7. General two-pole family

For pole heights a,b>0 define

    D(x)
      = (x^2+a^2)(x^2+b^2),

    Q(x)
      = x^2-Ax+ab.

Then

    f(x)
      = 1-Q(x)^2/D(x)

is automatically <=1 on x>0.

For x=-y<=0,

    Q(-y)^2-D(-y)

      =
      2A y^3
      +
      [A^2-(a-b)^2]y^2
      +
      2Aab y.

Thus the global negative-half-line condition is simply

    boxed:
    A >= |a-b|.

The exact choice

    a=1,
    b=9/4,
    A=17/5

has ample slack.

This makes the certificate transparent rather than numerical.

## 8. New recommendation

The first-strike hierarchy should now be:

1. **two-simple-pole f_2**:
       model simple ledger 73.31667...%;
       poles i and 9i/4;
       no derivatives;
       best current explicit margin/tail-conditioning ratio;

2. three-simple-pole f_3:
       model simple ledger 77.46736...%;
       poles i,3i,6i;
       larger raw margin;

3. r2,a=1 or a=6/5:
       one point but one repeated-pole derivative;

4. six-pole Christoffel family:
       model simple target 79.62710...%.

The immediate analytic target should therefore be the finite-local /
bounded-resolvent transport for the two simple Stieltjes values

    z=i,
    z=9i/4.

No unconditional record theorem is claimed until that transport is closed.

See:

    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
    notes/WP84_THREE_SIMPLE_POLE_RECORD_RUNG.md
    notes/WP84_RESOLVENT_KILL_GATE_2026_10_05.md
