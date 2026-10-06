# WP84 — exact dual certificate: degree two cannot beat the record in the conditioned one-Cayley majorant route

Date: 2026-10-05

Status: **EXACT OBSTRUCTION — DEGREE-2 TRIGONOMETRIC MAJORANTS OF THE CONDITIONED TWO-POLE DEFECT CANNOT CROSS THE CONSERVATIVE RECORD EVEN AT THE PINNED MODEL LEVEL**

No unconditional zero-density percentage is claimed here.

The degree-3 Cayley majorant is now the preferred post-band theorem target.

Before spending effort trying to reduce its displacement rank from six to
four by searching for a degree-2 majorant, we should know whether degree two
can possibly retain enough record margin.

It cannot.

This note gives an exact finite dual certificate.

## 1. Conditioned defect

Use

    g_*(x)
      =
      [x^2-(82/25)x+9/4]^2
      /
      [(x^2+1)(x^2+81/16)].

Let

    u(x)
      =
      (x+i)/(x-i)
      =
      exp(i theta(x)).

A general real degree-2 trigonometric polynomial is

    p_2(theta)
      =
      a_0
      +a_1 cos(theta)
      +b_1 sin(theta)
      +a_2 cos(2theta)
      +b_2 sin(2theta).

Suppose

    boxed:
    p_2(theta(x)) >= g_*(x)

for every real x.

We will prove that its pinned-model expectation is already too large.

## 2. Exact pinned-model moments of the five basis functions

The exact model expectations are

    E[1]
      = 1,

    E[cos theta]
      =
      -164937945/1707336793,

    E[sin theta]
      =
      1372449200/1707336793,

    E[cos 2theta]
      =
      -1307813823907483055
       /2914998924731524849,

    E[sin 2theta]
      =
      107171791159706464
       /2914998924731524849.

Call this five-vector m.

## 3. Five exact rational support points

Take the real points

    x_1 = 63/50,
    x_2 = 5/4,
    x_3 = 51/200,
    x_4 = 1/4,
    x_5 = -17/5.

For each x_j define the basis vector

    phi(x_j)
      =
      (
        1,
        cos theta(x_j),
        sin theta(x_j),
        cos 2theta(x_j),
        sin 2theta(x_j)
      ).

Because

    cos theta(x)
      =
      (x^2-1)/(x^2+1),

    sin theta(x)
      =
      2x/(x^2+1),

all these vectors are rational.

There is an exact positive solution of

    boxed:
    m
      =
      sum_{j=1}^5
        lambda_j phi(x_j),

with

    lambda_1
      =
      387171110253290672241298027
      /
      919222173922473455238327800,

    lambda_2
      =
      1834489883571625240911761
      /
      6905329292800810288696704,

    lambda_3
      =
      4657455326768729568018424151
      /
      22728650051982882090692101600,

    lambda_4
      =
      258108011731484438197093
      /
      2751012745221828187094656,

    lambda_5
      =
      242761394878395404388960772
      /
      16853399278237477620234625515.

Every lambda_j is strictly positive and

    sum_j lambda_j=1.

So these five atoms form an exact positive quadrature for the degree-2
Cayley basis under the pinned model.

## 4. Dual lower bound for every degree-2 majorant

For any degree-2 p_2 majorizing g_* pointwise,

    E_model[p_2]

      =
      sum_j
        lambda_j p_2(theta(x_j))

      >=
      sum_j
        lambda_j g_*(x_j).

The right side is the exact rational number

    boxed:

    L_2
      =
      202255841048454875843203393363533529
      /
      1212298386228020210032390410776980000

      =
      0.1668366825742955....

Thus

    boxed:
    E_model[p_2] >= 0.1668366825742955....

for **every** global degree-2 Cayley majorant of the conditioned defect.

## 5. This is already above the record ceiling

The conservative positive-index record ceiling is

    0.163249981456072....

Even the slightly larger rational number

    0.16325
      =
      653/4000

lies below L_2.

Exactly,

    boxed:

    L_2 - 653/4000

      =
      543516187091322069426957350523943
      /
      151537298278502526254048801347122500

      >0.

Therefore no degree-2 trigonometric majorant can produce a record crossing
in this conditioned one-Cayley route, even before paying any band or
arithmetic error.

## 6. Consequence for displacement rank

A degree-n Cayley polynomial has

    rank[D,q(U)] <= 2n

after Fejer--Riesz compression from rank[D,U]<=2.

Degree two would have offered a rank-four positive-energy state.

The exact dual obstruction above proves that this simplification is
incompatible with crossing the conservative record for the current
conditioned defect.

Thus the degree-3 / rank-six target is not merely an artifact of an
unoptimized search.

Within this global one-sided trigonometric-majorant architecture,

    boxed:
    degree three is the first degree with enough model margin.

So the rank-six positive displacement energy from

    WP84_DEGREE3_POSITIVE_RANK6_ENERGY.md

is the correct minimal first-strike state to attack.

## 7. Strategic conclusion

Do not spend further time searching for a degree-2 Cayley majorant of
g_*.

The next theorem effort should go directly into the rank-six positive energy

    tau(Q_R^*Q_R)

for one fixed band R.

The exact degree-2 obstruction saves a potentially large optimization detour.

See:

    notes/WP84_CONDITIONED_DEGREE3_CAYLEY_MAJORANT.md
    notes/WP84_DEGREE3_POSITIVE_RANK6_ENERGY.md
