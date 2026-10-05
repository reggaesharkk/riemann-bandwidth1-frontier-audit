# WP84 — sine-square mean/variance kill gate

Date: 2026-10-06

Status: **EXACT GLOBAL MEAN LOWER BOUND FROM THE SOURCE-CLOSED FIRST TWO MOMENTS; THE FULL-SHARP SINE-SQUARE THEOREM REDUCES TO ONE BOUNDED TRACE-VARIANCE INEQUALITY**

No unconditional zero-density percentage is claimed here.

Use the current preferred sine-square parameters

    a=63/50,
    t=17/16,

and define

    S_a(H)
      =
      2aH/(H^2+a^2),

    Q
      =
      I-tS_a(H).

Then

    tau(Q^2)

      =
      [1-t tau(S_a)]^2

      +
      t^2 Var_tau(S_a),

where

    Var_tau(S_a)
      =
      tau(S_a^2)
      -
      tau(S_a)^2.

This identity is exact at finite d.

The point of this note is that the mean term can be controlled globally from
the already-closed first two sharp moments.  The only new theorem debt is
then the bounded trace variance of S_a.

## 1. Exact quadratic lower minorant for S_a

For

    a=63/50,

put

    s_a(x)
      =
      2ax/(x^2+a^2).

Define the quadratic polynomial

    boxed:

    L_2(x)
      =
      -7/10000
      +(15473/10000)x
      -(1197/2000)x^2.

Then

    boxed:

    s_a(x)-L_2(x)

      =
      N(x)
      /
      [
        10000(2500x^2+3969)
      ],

where

    N(x)
      =
      14962500 x^4
      -38682500 x^3
      +23771965 x^2
      +1587663 x
      +27783.

The denominator is strictly positive.

The exact Sturm count is

    boxed:
    N has zero real roots.

Also

    N(0)=27783>0,

and the leading coefficient is positive.

Therefore

    boxed:
    L_2(x)<=s_a(x)

for every real x.

## 2. Source-closed mean lower bound

For the sharp normalized state,

    tau(H)=1+o(1),

    tau(H^2)=4/3+o(1).

Therefore the global polynomial minorant gives

    tau(S_a)

      >=
      -7/10000
      +15473/10000
      -(1197/2000)(4/3)
      +o(1).

The exact constant is

    boxed:

    tau(S_a)
      >=
      3743/5000
      +o(1)

      =
      0.7486+o(1).

No fourth moment and no resolvent local law are used in this step.

## 3. Exact mean/variance decomposition

Let

    mu_S=tau(S_a),

    sigma_S^2
      =
      tau(S_a^2)-mu_S^2.

Then exactly

    boxed:

    tau(Q^2)

      =
      (1-t mu_S)^2
      +t^2 sigma_S^2.

Because

    -1<=S_a<=1,

we have

    mu_S<=1.

At

    t=17/16,

the point 1/t is

    16/17
      ~=0.941176.

On the interval

    3743/5000
      <= mu_S <=1,

the maximum of

    (1-t mu_S)^2

occurs at the lower endpoint.

Therefore

    boxed:

    (1-t mu_S)^2

      <=
      (
        1
        -(17/16)(3743/5000)
      )^2

      =
      267944161/6400000000

      =
      0.04186627515625.

[The exact checker below is authoritative for the rational arithmetic.]

## 4. One scalar variance target

Let the conservative defect ceiling be

    E_rec
      =
      0.163249981456072....

A sufficient condition for the full-sharp record crossing is now

    boxed:

    Var_tau(S_a)

      <
      [
        E_rec
        -
        (
          1
          -(17/16)(3743/5000)
        )^2
      ]
      /
      (17/16)^2.

Numerically this is

    boxed:

    Var_tau(S_a)
      <
      0.1075232831....

Thus the first two raw moments already pay for the entire mean part of the
sine-square energy.

The remaining theorem is one bounded variance estimate.

## 5. Pinned-model comparison

At the pinned model,

    E_model[S_a]
      =
      0.7941745610835772...,

    E_model[S_a^2]
      =
      0.7175878318152314....

Hence

    boxed:

    Var_model(S_a)
      =
      0.0868745983429390....

The variance theorem therefore has a model cushion of roughly

    boxed:

    0.0206486.

This is a different error budget from the original defect-energy margin:
the source-closed first two moments have already removed the mean uncertainty.

## 6. Positive Poisson-kernel form

Let

    R=(H-iaI)^(-1),

    X=Re R,

    Y=Im R.

For Hermitian H,

    Y>=0,

and

    R^*R=Y/a.

Since X and Y are commuting functions of H,

    boxed:

    X^2
      =
      Y/a-Y^2.

Also

    S_a
      =
      2aX.

Therefore

    boxed:

    tau(S_a^2)
      =
      4a tau(Y)
      -4a^2 tau(Y^2).

The remaining variance can equivalently be written as

    boxed:

    Var_tau(S_a)

      =
      4a Im m(ia)
      -4a^2 tau[(Im R)^2]
      -4a^2 [Re m(ia)]^2.

This formulation keeps the only quadratic correction

    tau[(Im R)^2]

manifestly positive.

## 7. Current theorem hierarchy

The full-sharp sine-square route may now be attacked in either equivalent
form.

### Mean/variance form

Prove

    Var_tau(S_a)<0.1075232831....

The mean is already bounded below by 0.7486 from mu1 and mu2.

### Exact positive-energy form

Prove

    tau(Q^2)<0.163249981456072....

using the two-vector wedge / scalar K2 representation.

The mean/variance form is the smaller scalar target.  The wedge form retains
more matrix structure and may provide the stronger theorem estimate.

## 8. Evidence boundary

Closed:

- exact global quadratic minorant for S_a;
- exact source-moment mean lower bound;
- exact finite-d mean/variance decomposition;
- exact positive Poisson-kernel identity.

Open:

- the one-sided bounded variance estimate

      Var_tau(S_a)<0.1075232831....

No unconditional record theorem is claimed.

See:

    notes/WP84_SINE_TWO_VECTOR_WEDGE.md
    notes/WP84_SINE_SCALAR_K2_WEDGE.md
    notes/WP84_MPRIME_TRANSPOSE_VERIFICATION.md
