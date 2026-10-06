# WP84 — conditioned two-pole defect compressed to an exact degree-3 one-Cayley majorant

Date: 2026-10-05

Status: **EXACT GLOBAL MAJORANT; THE CONDITIONED TWO-POLE FIRST STRIKE REDUCES AFTER BAND TRUNCATION TO U,U^2,U^3 AT z=i**

No unconditional zero-density percentage is claimed here.

The current theorem-conditioned two-simple-pole minorant is

    f_*(x)
      =
      1
      -
      g_*(x),

with

    g_*(x)
      =
      [x^2-(82/25)x+9/4]^2
      /
      [(x^2+1)(x^2+81/16)].

Its simple-pole representation is still the right tool for the O(1/R)
long-displacement comparison.

This note removes the second pole **after** that comparison by a one-sided
degree-3 Cayley majorant.

## 1. One Cayley unitary

For real x set

    u(x)
      =
      (x+i)/(x-i).

For Hermitian H,

    U
      =
      (H+iI)(H-iI)^(-1)

is unitary.

## 2. Exact degree-3 trigonometric polynomial

Define

    boxed:

    p_3(e^{i theta})
      =
      1.6895
      +0.2101 cos(theta)
      -2.2720 sin(theta)
      -0.6312 cos(2theta)
      -0.3306 sin(2theta)
      -0.1525 cos(3theta)
      +0.0439 sin(3theta).

Equivalently,

    p_3(U)

      =
      1.6895 I
      + 2 Re[
          c_1 U
          + c_2 U^2
          + c_3 U^3
        ],

with exact rational coefficients

    c_1
      =
      2101/20000
      +(284/250)i,

    c_2
      =
      -789/2500
      +(1653/10000)i,

    c_3
      =
      -61/800
      -(439/20000)i.

## 3. Exact global majorant certificate

Substituting

    u=(x+i)/(x-i)

and subtracting g_*(x) gives

    boxed:

    p_3(u(x))-g_*(x)

      =
      N(x)
      /
      [
        10000
        (x^2+1)^3
        (16x^2+81)
      ],

up to the common factor 2 in numerator/denominator reduction, where

    N(x)
      =
      18544 x^8
      +153120 x^7
      -141929 x^6
      -1672190 x^5
      +3748517 x^4
      -2772972 x^3
      +737557 x^2
      -34542 x
      +567.

The exact Sturm count is

    boxed:
    N has 0 real roots.

Also

    N(0)=567>0,

and the leading coefficient is positive.

Therefore

    boxed:
    p_3(u(x)) > g_*(x)

for every real x.

Hence

    boxed:
    1-p_3(u(x))
      <
      f_*(x)
      <=
      1_{x>0}.

So

    h_3(x)
      :=
      1-p_3(u(x))

is itself a valid global support-free bounded minorant.

## 4. Exact pinned-model expectation

Exact reduction modulo the pinned Christoffel cubic gives

    boxed:

    E_model[p_3(U)]

      =
      6816992961687106121191829211903
      /
      49768849157495700216914692570000

      =
      0.13697308812816694....

Therefore the induced model positive-index lower bound is

    boxed:

    q_{3,C}
      =
      0.8630269118718330...,

and the corresponding model simple-zero ledger is

    boxed:

    2q_{3,C}-1
      =
      0.7260538237436661....

Thus the degree-3 one-Cayley rung still sits at

    72.6053823744...%

at the model level.

This is not an unconditional zeta theorem.

## 5. Record margin

Against the conservative positive-index comparison threshold

    q_rec
      =
      0.8367500185439279...,

the remaining model margin is

    boxed:

    Delta_{3,C}
      =
      0.0262768933279051....

This is the budget available before charging the full-to-band comparison and
the final arithmetic/local-law error.

## 6. Hybrid proof architecture

Do not use p_3 to perform the long-displacement comparison.

Use the conditioned two-simple-pole consumer f_* for that step:

    tau f_*(H)
      >=
      tau f_*(H_R)
      -
      C_{2,*}/R
      +o(R^-1),

with

    C_{2,*}
      =
      2.2079400595....

Then apply the exact pointwise majorant on H_R:

    tau f_*(H_R)
      >=
      1-tau p_3(U_R).

Hence

    boxed:

    tau f_*(H)

      >=
      1
      -
      tau p_3(U_R)
      -
      C_{2,*}/R
      +o(1).

So the first-strike theorem is reduced to controlling only

    tau(U_R),
    tau(U_R^2),
    tau(U_R^3)

at the single spectral point z=i.

## 7. Explicit fixed-band budgeting

The pre-band model margin is

    Delta_{3,C}
      ~=
      0.02627689333.

For example:

    R=200:
      C_{2,*}/R
        ~=0.01103970030,

      leaving
        ~=0.01523719303

      for the finite-band arithmetic/local-law step.

    R=256:
      C_{2,*}/R
        ~=0.00862476586,

      leaving
        ~=0.01765212747.

    R=400:
      C_{2,*}/R
        ~=0.00551985015,

      leaving
        ~=0.02075704318.

Thus a fixed finite bandwidth leaves a substantial positive theorem budget.

No limit R->infinity is required if one fixed R can close the remaining
arithmetic inequality.

## 8. Why degree 3 matters

The prior Cayley-geometric reduction of the second pole used a finite
hierarchy reaching degree about 8 before the approximation error became
small.

The present one-sided certificate has:

- no second pole;
- no derivative;
- no geometric truncation;
- degree only 3;
- exact global validity.

At z=i,

    rank[D,U]<=2,

so

    rank[D,U^k]<=2k.

The highest consumed displacement rank is therefore only six.

This is currently the smallest bounded-unitary first-strike target on the
branch.

## 9. Remaining theorem gate

The exact remaining statement is now:

> for one fixed convenient R, prove
>
>     limsup_T tau p_3(U_{T,R})
>
> is below
>
>     0.163249981456072...
>       - C_{2,*}/R.

The model benchmark is

    0.13697308812816694....

The arithmetic theorem no longer needs:

- the second pole 9i/4;
- repeated poles;
- a global Gaussian/Loewner law;
- all Cayley powers through degree 8.

It needs one bounded degree-3 Cayley observable of one fixed-band sharp
matrix.

See:

    notes/WP84_TWO_SIMPLE_POLE_RECORD_RUNG.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
    notes/WP84_TWO_POLE_CAYLEY_FINITE_REDUCTION.md
