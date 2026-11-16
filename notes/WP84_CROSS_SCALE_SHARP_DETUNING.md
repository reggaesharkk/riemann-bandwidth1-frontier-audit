# WP84 — exact cross-scale alternating formula and sharp detuning residual

Date: 2026-10-06

Status: **EXACT CHAMBER REDUCTION — THE SIX-WORD CONNECTED RESIDUAL IS NONPOSITIVE AND ITS MAGNITUDE IS AT MOST ONE TORUS DETUNING**

No unconditional zero-density percentage is claimed here.

The previous cross-scale reference used the coarse bound

    |E_ij|
      <=
      630 dist(s_i-s_j,Z).

The exact alternating-word geometry is much sharper.

## 1. Fundamental chamber

By swapping the two factors inside each same-sign pair and then swapping the
positive and negative pair, it is enough to work with

    1<=s<=t<=2,

and write

    c=s-1,
    d=t-1,
    delta=d-c,

    x=c+a,
    y=d+b,

with

    0<=a<=(1-c)/2,

    0<=b<=(1-d)/2.

Thus the two positive factors are

    c+a,
    1-a,

and the two negative magnitudes are

    d+b,
    1-b.

The four nonalternating sign patterns vanish identically on common-overlap
support.  Only

    + - + -

and

    - + - +

survive.

## 2. First alternating word

For

    v=(c+a, -(d+b), 1-a, -(1-b)),

the first-walk positions are

    0,
    c+a,
    a-b-delta,
    1-delta-b,
    -delta.

Direct max/min reduction gives

    boxed:

    O_1
      =
      [
        min(
          a,
          b,
          1-d-a
        )
      ]_+.

On O_1>0, the exact 26-term connected bracket is

    boxed:

    B_1
      =
      -min(c+a,d).

Therefore

    boxed:

    A_1
      =
      -min(c+a,d)
      [
        min(a,b,1-d-a)
      ]_+.

## 3. Second alternating word

For

    v=(-(d+b), c+a, -(1-b), 1-a),

the first-walk positions are

    0,
    -(d+b),
    a-b-delta,
    a-delta-1,
    -delta.

Hence

    boxed:

    O_2
      =
      min(
        b,
        (a-delta)_+
      ).

On O_2>0, the exact connected bracket is simply

    boxed:

    B_2=-c.

Thus

    boxed:

    A_2
      =
      -c
      min(
        b,
        (a-delta)_+
      ).

The companion arrangement checker verifies the two bracket formulas against
the complete 26-term connected ledger after refining by the chamber and min
walls.

## 4. Exact six-word formula

The complete six-sign-pattern kernel is

    boxed:

    C_6
      =
      A_1+A_2.

The global Brownian reference from the previous note becomes, on this chamber,

    G
      =
      2c
      min(
        b,
        (a-delta)_+
      ).

Therefore the residual

    E=C_6+G

is exactly

    boxed:

    E
      =
      -min(c+a,d)
       [
         min(a,b,1-d-a)
       ]_+

      +
      c
      min(
        b,
        (a-delta)_+
      ).

## 5. Exact sign

If a<=delta, the second term vanishes, so E<=0.

Assume a>delta.  Then

    min(c+a,d)=d.

Put

    m=min(b,a-delta).

Because

    a<=(1-c)/2,

we have

    1-d-a
      >=
      a-delta.

Therefore

    [
      min(a,b,1-d-a)
    ]_+
      >=
      m.

Since d>=c,

    d[
      min(a,b,1-d-a)
    ]
      >=
      c m.

Hence in all cases

    boxed:

    E<=0.

So even the cross-scale correction keeps the same pointwise sign as the
connected kernel.  Its possible positive contribution arises only after
multiplication by a negative real Fourier lobe.

## 6. Sharp detuning magnitude

For delta<=1/2 we prove

    boxed:
    -E<=delta.

If a<=delta, then

    -E
      <=
      (c+a)a
      <=
      a
      <=
      delta.

Now suppose a>delta.

If b<=a-delta, both minima equal b and

    -E
      =
      delta b
      <=
      delta.

If b>a-delta, put m=a-delta.

There are three possible active minima in

    B=min(a,b,1-d-a).

### B=a

Then

    -E
      =
      delta(c+a)
      <=
      delta.

### B=b

Using b<=a and b<=(1-d)/2,

    -E
      =
      d b-c(a-delta)

      <=
      delta(c+b)

      <=
      delta.

### B=1-d-a

Here B<=a implies a>=(1-d)/2.  Since the expression decreases with a,

    -E
      =
      d(1-d-a)-c(a-delta)

      <=
      delta
      [
        (1-d)/2+c
      ]

      <=
      delta.

Thus -E<=delta whenever delta<=1/2.

For delta>=1/2, simply use

    -E
      <=
      min(c+a,d)
      [
        min(a,b,1-d-a)
      ]_+

      <=
      b

      <=
      (1-d)/2

      <=
      (1-delta)/2.

Therefore globally

    boxed:

    -dist(s-t,Z)
      <=
      E(s,t;x,y)
      <=
      0.

In particular,

    boxed:

    |E|
      <=
      dist(s-t,Z).

This improves the previous constant 630 to the sharp scale 1.

## 7. Consequences

The divided-difference kernel

    H_ij
      =
      E_ij/(z_i-z_j)

now obeys

    boxed:

    |H_ij|
      <=
      1/4,

because

    |z_i-z_j|
      >=
      4 dist(s_i-s_j,Z).

And the pointwise Dirichlet cancellation improves to

    boxed:

    |E_ij K_ij|
      <=
      1/(2d).

The remaining problem is still operator/arithmetic rather than entrywise:
one must preserve the finite-feature structure of H instead of applying an
l1 bound.

## 8. New structural target

The exact formulas show that H is generated only by:

- minima of one-state affine depths;
- positive parts of affine depth differences;
- two alternating sign words.

Thus the Schur-feature problem is finite and much smaller than the original
26-term connected ledger.

The next gate is to convert these min/positive-part factors into interval
indicator features and apply the rank-two endpoint commutator before any
absolute product sum.

## 9. Evidence boundary

Closed:

- exact two-alternating-word formulas on the fundamental chamber;
- exact six-word residual formula;
- pointwise sign E<=0;
- sharp global detuning bound |E|<=dist(s-t,Z);
- improved divided-difference and Dirichlet constants.

Open:

- finite-feature/Schur control of the divided-difference kernel H;
- endpoint arithmetic after that factorization.

No unconditional record theorem is claimed.

See:

    notes/WP84_PHI4_ALTERNATING_ENVELOPE.md
    notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md
    notes/WP84_CROSS_SCALE_BROWNIAN_REFERENCE.md
    notes/WP84_DETUNING_COMMUTATOR_ENDPOINT.md
