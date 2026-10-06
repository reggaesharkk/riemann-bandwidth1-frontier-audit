# WP84 — rational canonical one-pole band fallback at a=1129/1000

Date: 2026-10-06

Status: **EXACT SUPPORT-FREE BOUNDED CONSUMER; DIRECT POINTWISE DOMINATION BY THE CHRISTOFFEL SQUARE; CERTIFIED O(1/R) BAND CONSTANT; DEGREE-SIX FIXED-BAND ARITHMETIC STILL OPEN**

No unconditional zero-proportion theorem is claimed here.

The functional-calculus band theorem makes it profitable to revisit the
canonical purely-imaginary one-point consumer before wrapping P^2 in the
six-pole F_delta family.

A rational pole just above the minimal Christoffel radius gives a substantially
smaller full-to-band constant and, crucially, is pointwise dominated by P^2
after band truncation.

## 1. Rational one-point consumer

Let

    a = 1129/1000,

and

    P(x)
      =
      1-(43428/13891)x
       +(37704/13891)x^2
       -(9660/13891)x^3.

Define

    boxed:

    p_a(x)
      =
      a^6 P(x)^2/(x^2+a^2)^3.

This is bounded, nonnegative, and has only the triple pole pair +/-ia.

## 2. Exact half-line support

Put x=-y, y>=0 and define

    N_a(y)
      =
      a^6 P(-y)^2-(y^2+a^2)^3.

After multiplying by the positive denominator

    24119985125000000000000000,

the ascending coefficients of N_a are exactly

    y^0: 0,
    y^1: 312325181258561005073689227,
    y^2: 641812916868032417834828544,
    y^3: 917209284937916964439954053,
    y^4: 492963023116959312324461412,
    y^5: 188568094885458749999730360,
    y^6: 36175979836774944268450.

Every nonconstant coefficient is strictly positive.

Therefore

    boxed:

    p_a(x)>=1
    for every x<=0.

Since p_a>=0 everywhere,

    boxed:

    1-p_a(x)
      <=
      1_{x>0}

globally.

Thus p_a is a valid bounded positive-index/simple-zero defect consumer.

## 3. Exact domination by the Christoffel square

For every real x,

    (x^2+a^2)^3>=a^6.

Hence

    boxed:

    p_a(x)<=P(x)^2

pointwise on the whole real line.

Consequently, for every Hermitian banded matrix H_R,

    boxed:

    tau p_a(H_R)
      <=
      tau P(H_R)^2.

This is stronger for the fixed-band fallback than the Jensen reduction for
F_delta: there is no concavity loss and no h_delta inflation.

The frozen Christoffel model value of the dominating square is

    w0=1415/13891
      ~=0.101864516593478.

## 4. Exact curvature certificate

The companion script differentiates p_a exactly.

Its second derivative has the form

    p_a''(x)=N(x)/D(x),

where

    D(x)
      =
      192959881
      (1000000 x^2+1274641)^5

up to an overall positive rational scale.

The exact Sturm gate checks that

    M D+N

and

    M D-N

have no real roots and are positive at x=0 for

    boxed:

    M=261637/10000
      =26.1637.

Therefore

    boxed:

    ||p_a''||_infinity
      <
      261637/10000.

The numerical maximum is near 26.16366, but that decimal is not used by the
certificate.

## 5. Functional band theorem

The general theorem gives

    |tau p_a(H)-tau p_a(H_R)|
      <=
      3 ||p_a''||_infinity/(pi^2 R)
      +o(R^-1).

Using pi>333/106 gives the completely rational bound

    boxed:

    |tau p_a(H)-tau p_a(H_R)|
      <
      C_a/R
      +o(R^-1),

with

    boxed:

    C_a
      =
      734938333/92407500
      ~=7.95323250818.

This is far smaller than the certified F79 curvature constant
about 21.58.

## 6. First >79 fixed-band targets

Because

    tau p_a(H_R)
      <= tau P(H_R)^2,

it is sufficient to prove

    boxed:

    limsup_T tau P(H_R)^2
      <
      0.105-C_a/R.

The model margin before band charge is exactly

    0.105-w0
      =
      8711/2778200
      ~=0.00313548340652.

The first integer R for which the certified band charge is below this entire
model margin is

    boxed:

    R=2537.

That radius leaves only a tiny arithmetic allowance and is not recommended
as the main working point.

Two more useful exact rungs are:

### R=3000

    boxed:

    tau P(H_3000)^2
      <
      28373424167/277222500000
      ~=0.102348922497272.

Allowance above w0:

    boxed:

    1865397603797/3850897747500000
      ~=0.000484405903794.

### R=5300

    boxed:

    tau P(H_5300)^2
      <
      956411989/9240750000
      ~=0.103499390092796.

Allowance above w0:

    boxed:

    209857689199/128363258250000
      ~=0.001634873499318.

The R=5300 allowance is already slightly larger than the exact cost

    ~=0.00156752584233

of replacing the model centered fourth moment 1/4 by the pair-only ceiling
4/15 while keeping the fifth and sixth centered moments at their model
values.

The exact first integer at which that comparison becomes favorable is

    boxed:

    R=5073.

This does **not** prove the fifth/sixth-order arithmetic.  It shows that the
full quantitative negative connected m4 correction is no longer mandatory
for a >79 fallback if the combined degree-five/six sector can be brought to
its model value with enough accuracy.

## 7. Why this is a better fixed-band interface

Compared with the F_delta fallback:

- one pole pair instead of three conjugate pairs;
- rational pole height;
- exact half-line support by positive coefficients;
- direct p_a<=P^2 domination after banding;
- no Jensen inflation;
- certified band constant about 7.95 instead of about 21.58;
- useful fixed radii around 3,000--5,300 instead of roughly 12,000.

The unbounded polynomial is still never applied to the full matrix.

The theorem-safe order remains:

    bounded p_a(H)
      -> functional O(1/R) comparison
      -> banded p_a(H_R)
      <= banded P(H_R)^2
      -> fixed-band degree-six arithmetic.

## 8. Evidence boundary

Closed:

- exact support-free consumer at a=1129/1000;
- exact pointwise domination p_a<=P^2;
- exact global curvature bound by Sturm;
- fully rational O(1/R) constant;
- explicit R=3000 and R=5300 >79 arithmetic thresholds.

Open:

- the fixed-band degree-six estimate for P(H_R)^2;
- final insertion of the already-audited zero-count transfer.

The primary one-point heat-curvature route remains active.  This is now the
preferred fixed-band fallback.

See:

    notes/WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md
    notes/WP84_FUNCTIONAL_BAND_DELTA79_SHARPENING.md
    notes/WP84_FIXED_BAND_CHRISTOFFEL_CENTERED_LEDGER.md
