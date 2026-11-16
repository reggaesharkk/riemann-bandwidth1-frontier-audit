# WP84 — direct O(1/R) repeated-pole tail bound without Cauchy loss

Date: 2026-10-06

Status: **EXACT FINITE-d RESOLVENT DIFFERENTIATION; THE m'(z) FULL-TO-BAND CONSTANT IMPROVES BY MORE THAN A FACTOR THREE OVER THE PREVIOUS CAUCHY-CIRCLE BOUND**

No unconditional zero-density percentage is claimed here.

The one-point bounded consumers use both

    m(z)=tau(H-zI)^(-1)

and

    m'(z)=tau(H-zI)^(-2).

The first O(1/R) displacement-tail note controlled m'(z) by Cauchy's
derivative estimate applied to the m(z) comparison.  That is valid but loses
a large constant.

This note differentiates the second resolvent identity directly.

## 1. Setup

Let

    H=H_R+Delta,

where H_R keeps displacements |i-j|<=R and Delta is the long-displacement
Loewner tail.

Write

    G=(H-zI)^(-1),

    S=(H_R-zI)^(-1),

and assume

    |Im z|>=eta>0.

Then

    ||G||,||S||<=eta^(-1).

Let

    q_alpha=||alpha||_2^2/d.

The already-closed tail estimates are

    tau(Delta^2)
      <=
      8 q_alpha/(pi^2 R),

and

    ||[D,H_R]||_F^2/d
      <=
      8 R q_alpha/pi^2.

## 2. Second resolvent identity

Iterating once,

    G-S
      =
      -S Delta S
      +S Delta S Delta G.

Taking normalized trace,

    m_H-m_R

      =
      -tau(Delta S^2)

      +tau(S Delta S Delta G).

This is the starting point of the previous O(1/R) theorem.

## 3. Differentiate directly

Because

    partial_z S=S^2,

    partial_z G=G^2,

we obtain exactly

    boxed:

    m_H'(z)-m_R'(z)

      =
      -2 tau(Delta S^3)

      +tau(S^2 Delta S Delta G)

      +tau(S Delta S^2 Delta G)

      +tau(S Delta S Delta G^2).

The first term is linear in Delta but gets the extra displacement
denominator.  The last three are quadratic in Delta.

## 4. Linear term

For i!=j,

    Delta_ij
      =
      (alpha_i-alpha_j)/[pi(j-i)],

and

    (S^3)_ji
      =
      [D,S^3]_ji/(j-i).

Therefore

    |tau(Delta S^3)|

      <=
      1/(pi d)
      [
        sum_tail
          |alpha_i-alpha_j|^2/(i-j)^2
      ]^(1/2)

      [
        sum_tail
          |[D,S^3]_ji|^2/(i-j)^2
      ]^(1/2).

On the tail,

    1/|i-j|<=1/R.

Also

    [D,S]
      =
      -S[D,H_R]S,

and

    [D,S^3]
      =
      [D,S]S^2
      +S[D,S]S
      +S^2[D,S].

Hence

    ||[D,S^3]||_F
      <=
      3 eta^(-4)
      ||[D,H_R]||_F.

Combining the two normalized Frobenius estimates gives

    boxed:

    |tau(Delta S^3)|
      <=
      24 q_alpha/
      (pi^2 eta^4 R).

Thus the differentiated linear term contributes at most

    boxed:

    48 q_alpha/
    (pi^2 eta^4 R).

## 5. Quadratic terms

Each differentiated quadratic term contains two Delta factors and four
resolvent factors in total.

For example, by Hilbert--Schmidt Cauchy--Schwarz,

    |tau(S^2 Delta S Delta G)|
      <=
      eta^(-4) tau(Delta^2).

The same bound holds for

    tau(S Delta S^2 Delta G)

and

    tau(S Delta S Delta G^2).

Therefore the three quadratic terms contribute at most

    3 eta^(-4) tau(Delta^2)

      <=
      24 q_alpha/
      (pi^2 eta^4 R).

## 6. Sharp direct derivative comparison

Combining Sections 4--5,

    boxed:

    |m_H'(z)-m_R'(z)|

      <=
      72 q_alpha/
      (pi^2 eta^4 R).

For the retained sharp prime field,

    q_alpha
      =
      1/4+o(1),

so

    boxed:

    |m_H'(z)-m_R'(z)|

      <=
      18/
      (pi^2 eta^4 R)

      +o(R^-1).

The m(z) comparison remains

    boxed:

    |m_H(z)-m_R(z)|

      <=
      6/
      (pi^2 eta^3 R)

      +o(R^-1).

## 7. Improvement over the old Cauchy-circle bound

The previous derivative estimate used a Cauchy circle of radius rho eta and
gave, at the optimized elementary choice rho=1/4,

    6 * 256/27
    /
    (pi^2 eta^4 R).

The coefficient before 1/(pi^2 eta^4 R) was therefore

    1536/27
      =
      56.8888....

The direct differentiation coefficient is only

    18.

So the repeated-pole constant improves by the factor

    boxed:

    (1536/27)/18
      =
      256/81
      ~=3.16049.

This is theorem-level constant improvement, not a numerical fit.

## 8. Consequence for the sine-square energy

For

    P_{a,t}(H)
      =
      [
        I
        -t 2aH/(H^2+a^2)
      ]^2,

the exact scalar form is

    tau P_{a,t}(H)

      =
      1
      +2 Re[
          A m(ia)
          +B m'(ia)
        ],

with

    A
      =
      a(-2t-it^2),

    B
      =
      a^2 t^2.

Using the direct m and m' tail estimates at eta=a gives

    boxed:

    |
      tau P_{a,t}(H)
      -
      tau P_{a,t}(H_R)
    |

      <=
      C_sine(a,t)/R
      +o(R^-1),

where

    boxed:

    C_sine(a,t)

      =
      1/(pi^2 a^2)
      [
        12 t sqrt(4+t^2)
        +36 t^2
      ].

This supersedes the earlier sine-square constant

    12/(pi^2 a^2)
    [
      t sqrt(4+t^2)
      +(256/27)t^2
    ].

## 9. Updated rational conditioning point

Under the improved constant, a continuous model-only reconnaissance of

    Delta(a,t)/C_sine(a,t)

peaks near

    a~=1.26441,
    t~=1.06235.

A very simple rational point is

    boxed:

    a=63/50,
    t=17/16.

Its exact pinned-model defect energy is

    boxed:

    E_model
      =
      16936977322225889866362306131535233
      /
      138296662375342896486666218354808008

      =
      0.12246844595756208....

Thus its model simple-zero ledger is

    boxed:

    75.50631080848759...%.

The conservative defect margin is

    boxed:

    Delta
      =
      0.0407815354985099....

The improved full-to-band constant is

    boxed:

    C_sine
      ~=4.43651377028.

Therefore

    boxed:

    Delta/C_sine
      ~=0.00919224815.

Compared with the previous t=37/35 sine-square route using the old Cauchy
derivative bound, the explicit margin-to-band-cost ratio improves by more
than a factor two.

Useful residual margins after the theorem-grade band charge are:

    R=128:
      ~0.00612127;

    R=192:
      ~0.01767469;

    R=256:
      ~0.02345140;

    R=400:
      ~0.02969025.

So even a fixed band near R=128 is no longer excluded by the explicit
long-displacement constant.

## 10. Evidence boundary

Closed here:

- exact differentiated second resolvent identity;
- exact O(1/R) m' comparison;
- exact 256/81 improvement over the previous Cauchy-circle coefficient;
- exact sine-square band constant;
- exact rational model certificate at a=63/50,t=17/16.

Still open:

- the actual large-T bounded-energy transport on the retained/fixed-band
  state.

No unconditional record theorem is claimed.

See:

    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
    notes/WP84_SINE_SQUARE_RANK4_ROUTE.md
    notes/WP84_DIRECT_DEGREE2_HEAT_CURVATURE_STENCIL.md
