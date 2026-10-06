# WP84 — balanced nonclosed connected overlap amplitude is pointwise nonpositive

Date: 2026-10-06

Status: **EXACT 4D FINITE-ARRANGEMENT THEOREM — THE 26-TERM CONNECTED OVERLAP AMPLITUDE IS NONPOSITIVE ON EVERY BALANCED 2-vs-2 SIGN ORTHANT EVEN WITHOUT EXACT MULTIPLICATIVE CLOSURE**

No unconditional zero-density percentage is claimed here.

The previous pointwise theorem proved

    C4<=0

for exact closed four-step cycles

    v0+v1+v2+v3=0.

Finite Fourier compression introduces nonclosed near-resonant words, so it is
important to know whether the overlap combinatorics themselves can become
positive before the Dirichlet/carrier factor is inserted.

They cannot in the balanced 2-vs-2 sector.

## 1. Nonclosed overlap geometry

Let

    v=(v0,v1,v2,v3)

be four real normalized shifts, with no closure condition.

The common first walk has positions

    0,
    v0,
    v0+v1,
    v0+v1+v2,
    Y,

where

    Y=v0+v1+v2+v3.

Its overlap is

    O_A(v)
      =
      (
        1-spread(first walk)
      )_+.

For each of the 26 ordered-partition connected terms, the second overlap path
is the usual nested subset-sum chain, but now its final all-label endpoint

    Y

must be retained explicitly.

Define

    B4_nc(v)

as the signed 26-term sum of those second overlaps.

The finite-compression connected **amplitude** before the common
Dirichlet/carrier scalar is

    O_A(v) B4_nc(v).

## 2. Balanced sign sector

Assume exactly two of the v_j are nonnegative and the other two are
nonpositive.

This is precisely the sign pattern of the first hard balanced
two-positive/two-negative product sector.

The theorem is

    boxed:

    O_A(v)>0
      =>
    B4_nc(v)<=0.

Therefore

    boxed:

    O_A(v) B4_nc(v)<=0

pointwise for every balanced nonclosed four-step vector.

No condition

    Y=0

is required.

## 3. Exact arrangement certificate

Every overlap is piecewise affine.

All branch changes occur when two path positions coincide, and all cutoff
changes occur when their difference reaches +/-1.

In four variables the complete family contains

    boxed:
    45

distinct normalized hyperplanes, including:

- every max/min wall;
- every +/-1 cutoff wall;
- the common first-walk support walls;
- the coordinate sign walls;
- the cube walls |v_j|<=1.

Their four-fold independent intersections produce exactly

    boxed:
    327

rational vertices inside the ambient cube.

The six balanced sign orthants contain the following numbers of support
vertices:

    positive labels (0,1): 18
    positive labels (0,2): 31
    positive labels (0,3): 25
    positive labels (1,2): 25
    positive labels (1,3): 31
    positive labels (2,3): 18.

On every one of these vertices,

    boxed:
    B4_nc<=0.

The largest exact value is

    boxed:
    0.

Since B4_nc is affine on every arrangement cell, the vertex principle proves
the inequality throughout every balanced support cell.

The companion checker uses integer 4x4 determinants and Fraction arithmetic.
No floating arithmetic enters the acceptance decision.

## 4. Stronger structural interpretation

The earlier closed-cycle sign theorem was not merely a consequence of exact
multiplicative equality.

The overlap combinatorics already force the balanced connected amplitude to
be nonpositive before closure.

Thus finite-compression positivity cannot originate from the overlap
amplitude itself.

It can only enter through the common finite Fourier trace scalar

    K_T(Y)
      =
      (1/d)
      sum_k
        exp(i tau_k Y)

      =
      exp(iTY)
      D_d(Y/L),

which multiplies the connected amplitude.

For the real fourth moment, the relevant scalar is

    Re K_T(Y).

Hence a positive connected contribution requires

    boxed:

    Re K_T(Y)<0

on a sector where the connected amplitude is strictly negative.

This is a much smaller geometric target than an arbitrary near-resonant
four-prime error.

## 5. Central detuning interval is automatically safe

Because

    Re K_T(Y)
      =
      (1/d)
      sum_k cos(tau_k Y),

if

    |Y|
      <=
      pi/(2 tau_max),

then every cosine in the average is nonnegative.

Therefore

    boxed:

    |Y|<=pi/(2 tau_max)

implies that the balanced connected finite-compression contribution is
pointwise nonpositive.

For the standard consumed height range tau_max=2T+o(T), a convenient
asymptotic safe interval is

    boxed:

    |Y|
      <=
      pi/(4T)
      +o(1/T).

Thus only the outer detuning lobes, where Re K_T changes sign, can create
positive connected leakage.

## 6. What remains open

This theorem does **not** by itself close the R=400 fourth-moment gate.

The scalar Re K_T(Y) oscillates outside the central safe interval, so a
negative connected amplitude can be rotated into a positive real
contribution.

The remaining arithmetic theorem is now restricted to those negative
Dirichlet/carrier lobes.

This refinement is compatible with the q=1 principal-arc normalization
audit:

- overlap amplitude: sign-closed;
- central detuning lobe: sign-closed;
- transition product layer: mass-closed;
- discrete sampling: closed;
- remaining positive leakage: only outer near-resonant detuning lobes.

At R=400 the total allowance for all such positive non-pair leakage remains

    >0.0247937.

## 7. Evidence boundary

Closed:

- exact nonclosed balanced overlap-amplitude sign;
- exact 4D rational arrangement certificate;
- central finite-compression detuning interval is nonpositive.

Open:

- weighted arithmetic control of the outer negative-Re K_T lobes.

No unconditional record theorem is claimed.

See:

    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
    notes/WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md
    notes/WP84_E2_PRINCIPAL_ARC_NORMALIZATION_AUDIT.md
