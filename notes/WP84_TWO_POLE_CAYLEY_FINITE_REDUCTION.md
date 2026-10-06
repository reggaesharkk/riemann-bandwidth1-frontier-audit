# WP84 — Cayley reduction of the two-pole first strike to one unitary point

Date: 2026-10-05

Status: **EXACT FUNCTIONAL CALCULUS; SECOND SIMPLE POLE REDUCED TO A GEOMETRIC SERIES IN THE z=i CAYLEY UNITARY WITH EXPLICIT UNIFORM TAIL**

No unconditional zero-density percentage is claimed here.

The conditioned two-simple-pole first strike consumes only

    m(i),
    m(9i/4).

The second point can be eliminated in favor of a rapidly convergent bounded
polynomial in the Cayley unitary at z=i.

## 1. Cayley unitary

For a Hermitian H define

    boxed:
    U
      =
      (H+iI)(H-iI)^(-1).

Then U is unitary and

    U=I+2iR(i),

so

    boxed:
    R(i)
      =
      (U-I)/(2i).

Thus the first consumed Stieltjes value is already a degree-one unitary
moment.

## 2. Exact second-pole identity

For any b>1,

    H
      =
      i(U+I)(U-I)^(-1).

Therefore

    H-ibI

      =
      i(1+b)
      [
        I-q_b U
      ]
      (U-I)^(-1),

where

    q_b
      =
      (b-1)/(b+1).

Hence exactly

    boxed:

    R(ib)

      =
      (U-I)
      /
      [
        i(1+b)
      ]
      *
      (I-q_b U)^(-1).

Since U is unitary and 0<q_b<1,

    (I-q_bU)^(-1)
      =
      sum_{n>=0}
        q_b^n U^n

in operator norm.

## 3. Specialize to b=9/4

For the conditioned first-strike pole,

    b=9/4,

so

    boxed:
    q_b=5/13.

Thus

    R(9i/4)

      =
      4/(13i)
      (U-I)
      sum_{n>=0}
        (5/13)^n U^n.

Define the degree-N truncation

    R_b^[N]

      =
      4/(13i)
      (U-I)
      sum_{n=0}^{N-1}
        (5/13)^n U^n.

Because

    ||U-I||<=2

and

    sum_{n>=N} q^n
      =
      q^N/(1-q),

we obtain the exact uniform operator bound

    boxed:

    ||R(9i/4)-R_b^[N]||
      <=
      (5/13)^N.

No spectral clipping and no moment assumption enter this estimate.

## 4. Conditioned two-pole consumer

Use the theorem-conditioned member

    f_{2,*}(H)

      =
      2 Re[
        c_1 R(i)
        +
        c_b R(9i/4)
      ],

with

    c_1
      =
      328/325
      -(91959/81250)i,

    c_b
      =
      738/325
      +(827631/325000)i.

Its exact second residue magnitude is

    boxed:

    |c_b|
      =
      1108881/325000.

Therefore replacing R(9i/4) by R_b^[N] costs at most

    boxed:

    epsilon_N
      =
      2
      (1108881/325000)
      (5/13)^N

in normalized trace, uniformly for every Hermitian H.

Examples:

    N=7:
      epsilon_N
        ~= 0.0084960712,

    N=8:
      epsilon_N
        ~= 0.0032677197,

    N=9:
      epsilon_N
        ~= 0.0012568153,

    N=10:
      epsilon_N
        ~= 0.0004833905.

The positive-index model record margin is

    Delta_{2,*}
      ~= 0.0289320962.

Thus already N=8 spends only about 11.3% of the total record margin.

## 5. Finite bounded-unitary theorem target

After truncation,

    f_{2,*}(H)

is approximated by a fixed polynomial

    P_N(U)

of degree at most N.

Hence

    boxed:

    tau f_{2,*}(H)

      =
      sum_{k=0}^N
        d_k tau(U^k)

      + O(epsilon_N),

with exact coefficients d_k obtained from the geometric series.

Every U^k is unitary, so

    |tau(U^k)|<=1.

This is a **bounded finite-degree** reduction.

It is not a raw moment statement about H and is therefore
Proposition-R safe.

## 6. Why this matters analytically

The first record theorem may now be attacked at a single spectral point

    z=i

using only finitely many powers of one unitary matrix.

No m'(i) is needed.

No second resolvent pole is needed after the geometric truncation.

No unbounded H^k moment is introduced.

Moreover

    [D,U]
      =
      2i[D,R(i)]

has rank at most two.

Therefore

    [D,U^k]
      =
      sum_{j=0}^{k-1}
        U^j[D,U]U^{k-1-j}

has rank at most

    boxed:
    2k.

For N=8 or N=10 the entire truncated consumer lives in a finite
low-displacement-rank unitary hierarchy.

## 7. Next theorem gate

The preferred bounded theorem target is now:

> control
>
>     tau(U^k),
>     1<=k<=8
>
> for the actual sharp retained zeta matrix strongly enough that the total
> transport error plus
>
>     epsilon_8 ~= 0.00326772
>
> stays below
>
>     Delta_{2,*} ~= 0.02893210.

If an 8th-order bounded-unitary transport is awkward, N=10 reduces the
analytic approximation debt below 5e-4 while remaining finite.

This is substantially narrower than proving a global resolvent law.

See:

    notes/WP84_TWO_SIMPLE_POLE_RECORD_RUNG.md
    notes/WP84_R2_CAYLEY_DEFECT_GATE.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
