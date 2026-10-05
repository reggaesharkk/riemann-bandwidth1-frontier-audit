# WP84 — direct degree-two Cayley square

Date: 2026-10-05

Status: **EXACT GLOBAL HALF-LINE MINORANT; ONE CAYLEY POINT; DEGREE TWO; DISPLACEMENT RANK AT MOST FOUR**

Let

    U=(H+iI)(H-iI)^(-1)

and define

    q(u)
      =
      1/1000 [
        623 u^2
        +(55-1058 i)u
        -(557+58 i)
      ].

Put

    p(u)=|q(u)|^2

on the unit circle and

    h(x)
      =
      1-p((x+i)/(x-i)).

## Exact half-line certificate

For real x,

    p((x+i)/(x-i))-1
      =
      N(x)
      /
      [
        1000000 (x^2+1)^2
      ],

where

    N(x)
      =
      260097 x^4
      -5295592 x^3
      +5812394 x^2
      -4717448 x
      +121.

An exact Sturm count gives zero real roots of N on the interval

    (-infinity,0].

Since N(0)=121>0,

    p>=1

for x<=0.

For x>0,

    p>=0

automatically because it is a modulus square.

Hence

    boxed:
    h(x)<=1_{x>0}

for every real x.

## Exact pinned-model value

Exact reduction against the pinned Christoffel model gives

    E_model[p(U)]
      =
      314919677809788131206697
      /
      2914998924731524849000000

      =
      0.10803423463999824....

Therefore the associated model positive-index value is

    0.8919657653600017...,

and the associated model simple-zero ledger is

    boxed:
    78.3931530720...%.

This is a model benchmark, not an unconditional zero statement.

Relative to the conservative positive-index energy ceiling

    0.163249981456072...,

the model energy margin is approximately

    boxed:
    0.0552157468160738.

## Positive rank-four state

Put

    Q=q(U).

Then exactly

    h(H)=I-Q^*Q.

Thus the consumed scalar is the positive normalized energy

    tau(Q^*Q).

Let

    C=[D,U].

For the sharp Loewner state,

    rank C<=2.

Since q has degree two,

    [D,Q]
      =
      C(q1 I+q2 U)
      +q2 U C.

Therefore

    boxed:
    rank[D,Q]<=4.

For i!=j,

    Q_ij
      =
      [D,Q]_ij/(i-j),

so

    boxed:

    tau(Q^*Q)
      =
      d^(-1) sum_i |Q_ii|^2

      +
      d^(-1) sum_{i!=j}
        |[D,Q]_ij|^2/(i-j)^2.

Both pieces are nonnegative.  The off-diagonal term has the standard
one-dimensional squared-Cauchy Fourier representation with an internal
channel of size at most 4 x 4.

## Scope of the previous degree-two obstruction

The existing degree-two dual obstruction imposed the stronger condition

    p_2 >= g_*

for the conditioned two-pole defect g_*.

The direct square above does not use that wrapper.  It satisfies only the
actual half-line conditions

    p>=1 on x<=0,
    p>=0 everywhere.

So there is no contradiction: degree three is minimal in the conditioned
two-pole majorant family, while a direct degree-two support-free square
exists.

This is currently the smallest bounded one-point model consumer on the
branch: one Cayley point z=i, no derivative, degree two, rational
coefficients, and displacement rank at most four.
