# WP84 — alternating-order envelope for the balanced nonclosed connected amplitude

Date: 2026-10-06

Status: **EXACT FINITE-ARRANGEMENT THEOREM; FOUR BALANCED SIGN ORDERINGS VANISH IDENTICALLY ON SUPPORT, AND THE TWO ALTERNATING ORDERINGS HAVE A SHARP ONE-PAIR SUPERCRITICAL ENVELOPE**

No unconditional zero-density percentage is claimed here.

The previous theorem established, for every balanced two-positive/two-negative
nonclosed four-step word,

    O_A(v) B4_nc(v) <= 0.

This note sharpens that statement substantially.

Write

    C_nc(v)=O_A(v) B4_nc(v),

where O_A is the common first-walk overlap.

## 1. Four of the six balanced sign orderings vanish identically

Let P be the set of positive labels.

On the support O_A(v)>0, exact arrangement verification gives

    boxed:

    B4_nc(v)=0

for

    P in {
      {0,1},
      {0,3},
      {1,2},
      {2,3}
    }.

Thus only the two alternating sign orders survive:

    + - + -
    - + - +.

This removes four sixths of the balanced ordering geometry before any
arithmetic estimate is used.

## 2. Sharp envelope for + - + -

Write

    v=(p,-r,q,-s),

with

    0<=p,q,r,s<=1.

On O_A(v)>0,

    boxed:

    0 >= B4_nc(p,-r,q,-s)
      >= -(r+s-1)_+.

Equivalently,

    boxed:

    0 <= -C_nc(v)
      <= O_A(v) (r+s-1)_+.

The envelope depends only on the supercritical excess of the negative pair.

## 3. Sharp envelope for - + - +

Write

    v=(-r,p,-s,q).

On O_A(v)>0,

    boxed:

    0 >= B4_nc(-r,p,-s,q)
      >= -(p+q-1)_+.

Hence

    boxed:

    0 <= -C_nc(v)
      <= O_A(v) (p+q-1)_+.

Now the envelope depends only on the supercritical excess of the positive
pair.

## 4. Exact finite-arrangement certificate

The same complete nonclosed arrangement used by the sign theorem contains

    45

rational hyperplanes and

    327

rational ambient vertices.

The extra envelope kink planes

    v_1+v_3=+1,
    v_1+v_3=-1

already belong to that arrangement.

Therefore, on every arrangement cell:

- B4_nc is affine;
- each envelope is affine;
- the difference between B4_nc and the claimed lower envelope is affine.

It is enough to check the support vertices.

The exact results are:

    positive labels {0,1}: 18 vertices, B4_nc identically 0
    positive labels {0,2}: 31 vertices, B4_nc+( -v1-v3-1 )_+ >=0
    positive labels {0,3}: 25 vertices, B4_nc identically 0
    positive labels {1,2}: 25 vertices, B4_nc identically 0
    positive labels {1,3}: 31 vertices, B4_nc+(  v1+v3-1 )_+ >=0
    positive labels {2,3}: 18 vertices, B4_nc identically 0.

All acceptance decisions use Fraction arithmetic.

## 5. Exact continuum envelope integral: 1/144 per alternating order

The envelope itself has a simple exact integral.

For the +-+- ordering,

    I
      =
      integral_[0,1]^4
        O_A(p,-r,q,-s)
        (r+s-1)_+
        dp dq dr ds.

Use the overlap representation

    O_A(v)
      =
      integral_0^1
        1{
          x,
          x+p,
          x+p-r,
          x+p-r+q,
          x+p-r+q-s
          all lie in [0,1]
        }
      dx.

Change variables to the five walk positions

    x0=x,
    x1=x+p,
    x2=x+p-r,
    x3=x+p-r+q,
    x4=x+p-r+q-s.

The Jacobian is one.

The step constraints become

    x0<=x1,
    x2<=x1,
    x2<=x3,
    x4<=x3,

with every xj in [0,1], while

    r+s-1
      =
      x1+x3-x2-x4-1.

Integrating first in x0 gives a factor x1.
Integrating x4 over [0,x3] gives

    (1/2)
    (x1+x3-x2-1)_+^2.

Because

    x1+x3-1
      <=
      min(x1,x3),

the x2 integral is exactly

    (1/3)
    (x1+x3-1)_+^3.

Therefore

    I
      =
      (1/6)
      integral_{x1+x3>1}
        x1
        (x1+x3-1)^3
        dx1 dx3

      =
      (1/24)
      integral_0^1 x1^5 dx1

      =
      boxed:
      1/144.

By reversal symmetry, the -+-+ envelope has the same integral.

Thus the total Lebesgue continuum envelope over all six balanced sign
orderings is at most

    boxed:

    2/144
      =
      1/72
      =
      0.013888888888....

This is an exact geometric number.

## 6. Relation to the R=400 leakage budget

The current positive non-pair allowance at R=400 is

    >0.0247937.

The geometric continuum envelope

    1/72
      ~=0.0138889

is below that allowance by

    >0.0109048.

This does NOT by itself close the arithmetic theorem.

The nonclosed prime coefficient sector is not automatically the four-fold
Lebesgue prime measure: the balanced product coefficient is linear in the
prime amplitudes and requires its own arithmetic/normalization transfer.

The exact consequence is narrower:

    any theorem-grade transfer that bounds the positive nonclosed arithmetic
    contribution by this geometric envelope, up to o(1), closes the complete
    R=400 connected leakage gate.

That is now a concrete scalar target.

## 7. High-frequency consequence

The finite trace satisfies

    |Re K_T(Y)|<=1.

Hence only the arithmetic coefficient measure can amplify the geometric
envelope.

There is no longer any need to budget six balanced orderings or an arbitrary
26-term amplitude in the high-frequency tail.

The remaining outer-detuning analysis may be restricted to:

1. the two alternating orderings;
2. one pair-excess factor, (s_pair-1)_+;
3. the exact signed finite-trace multiplier.

This is the appropriate form for a dual-weighted / annular estimate: keep
the finite-trace sign and estimate only the coefficient-side residual.

## 8. Evidence boundary

Closed:

- four balanced sign orders vanish identically on support;
- exact alternating-order pointwise envelopes;
- exact 1/144 continuum envelope integral per alternating order;
- exact total geometric envelope 1/72.

Open:

- theorem-grade transfer from the actual balanced prime-product coefficient
  measure to the geometric envelope without a hidden H amplification.

No unconditional record theorem is claimed.

See:

    notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md
    notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md
    notes/WP84_E2_PRINCIPAL_ARC_NORMALIZATION_AUDIT.md
