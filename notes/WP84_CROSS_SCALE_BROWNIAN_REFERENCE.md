# WP84 — cross-scale Brownian reference and exact detuning factor

Date: 2026-10-06

Status: **EXACT STRUCTURAL REDUCTION — THE UNEQUAL-SCALE BALANCED CONNECTED KERNEL DIFFERS FROM A GLOBAL NEGATIVE-SEMIDEFINITE REFERENCE BY A KERNEL WITH AN EXPLICIT LINEAR DETUNING FACTOR**

No unconditional zero-density percentage is claimed here.

The equal-scale balanced kernel is negative semidefinite.  To avoid a lossy
cell-center freezing, introduce a positive-semidefinite reference directly
on the full scale-split state space.

## 1. Scale-split coordinates

For one positive factor pair write

    (x,s-x),

with

    1<=s<=2.

Define

    c_s=s-1,

    r_s(x)=min(x,s-x).

On the admissible factor domain,

    c_s<=r_s(x)<=s/2.

For two scale-split points

    i=(s,x),
    j=(t,y),

define

    A_ij
      =
      min(c_s,c_t),

and

    B_ij
      =
      [
        min(r_s(x),r_t(y))
        -
        max(c_s,c_t)
      ]_+.

Set

    boxed:

    G_ij=2 A_ij B_ij.

## 2. G is positive semidefinite

The kernel

    A_ij=min(c_i,c_j)

is the Brownian covariance kernel

    A_ij
      =
      int_0^1
        1_{u<=c_i}
        1_{u<=c_j}
      du.

Also

    B_ij

has the exact Gram representation

    B_ij
      =
      int_0^1
        1_{c_i<=v<=r_i}
        1_{c_j<=v<=r_j}
      dv.

Thus A and B are positive semidefinite.

By the Schur product theorem,

    boxed:

    G=2 A o B

is positive semidefinite on arbitrary collections of unequal scales.

## 3. Equal-scale match

If s=t, then

    A_ij=s-1,

and

    B_ij
      =
      min(r_s(x),r_s(y))
      -(s-1).

Therefore

    G((s,x),(s,y))

      =
      2(s-1)
      [
        min(r_s(x),r_s(y))
        -(s-1)
      ].

The exact orientation-normalized six-word connected kernel satisfies

    boxed:

    C_6((s,x),(s,y))
      =
      -G((s,x),(s,y)).

So -G is a global cross-scale negative-semidefinite extension of the exact
equal-scale connected kernel.

## 4. Elementary Lipschitz bound for the exact six-word kernel

Let

    C_6(s,t;x,y)

denote the exact sum over the six balanced sign patterns with fixed internal
same-sign label ordering.

Changing t while keeping s,x,y fixed changes only one of the four step
magnitudes by

    Delta=t-s.

For one connected word:

- every path position changes by at most |Delta|;
- every spread changes by at most 2|Delta|;
- every overlap changes by at most 2|Delta|;
- the 26-term connected bracket has absolute value at most 26;
- its change is at most 52|Delta|.

Hence one product

    O_A B4_nc

changes by at most

    104 |Delta|.

There are six balanced sign patterns, so

    boxed:

    |
      C_6(s,t;x,y)
      -
      C_6(s,s;x,y)
    |

      <=
      624 |s-t|.

If, after replacing t by s, one factor leaves [0,1], the corresponding
first-walk overlap is zero; the equal-scale Brownian formula extends by zero
because its interval B_ij is empty.  Thus the same comparison remains valid
at the factor-domain boundary.

## 5. Lipschitz bound for the cross-scale reference

For fixed s,x,y:

- min(c_s,c_t) changes by at most |s-t|;
- r_t(y)=min(y,t-y) changes by at most |s-t|;
- max(c_s,c_t) changes by at most |s-t|;
- the positive-part interval length B changes by at most 2|s-t|.

Since 0<=A,B<=1,

    boxed:

    |
      G((s,x),(t,y))
      -
      G((s,x),(s,y))
    |

      <=
      6 |s-t|.

## 6. Exact detuning residual

Define

    E(s,t;x,y)
      =
      C_6(s,t;x,y)
      +
      G((s,x),(t,y)).

Using Sections 3--5,

    boxed:

    |E(s,t;x,y)|
      <=
      630 |s-t|.

In arithmetic variables,

    s-t
      =
      log(m/n)/L.

Therefore

    boxed:

    |E_mn|
      <=
      630
      |log(m/n)|/L.

This is the missing explicit detuning factor.

The constant 630 is intentionally crude.  Only its finiteness matters.

## 7. Consequence for the finite trace

The connected finite-compression kernel decomposes as

    C_6 o K

      =
      -G o K
      +
      E o K.

Both G and K are positive semidefinite, so

    boxed:

    -G o K

is negative semidefinite globally, with no scale partition.

All possible positive leakage is confined to

    boxed:

    E o K,

and E carries the explicit normalized detuning factor

    |log(m/n)|/L.

This is the correct high-frequency commutator object.

## 8. What remains

The remaining theorem is now an operator estimate:

    boxed:

    c^*(E o K)c=o(1)

for the balanced product coefficient vector c.

The coefficient mass is already O(1), and the product-block trace Gram
matrix satisfies

    ||K||_op
      <=
      1+16pi M/T.

A cell-center freezing of width L^(-1/2) is not sufficient by itself, because
the large-sieve factor can grow like M/T.

The active estimate must use the actual detuning factor in E before applying
the product-block operator bound.

This supersedes any argument that replaces |s-t| by the width of an
arbitrary scale cell.

## 9. Evidence boundary

Closed:

- global unequal-scale PSD reference G;
- exact equal-scale match;
- explicit deterministic residual bound
      |E|<=630|s-t|;
- reduction of all positive connected leakage to the detuning-weighted
  kernel E o K.

Open:

- prove the quadratic-form bound
      c^*(E o K)c=o(1)
  uniformly over the consumed product range.

See:

    notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md
    notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md
    notes/WP84_BALANCED_PRODUCT_SECOND_MASS.md
    notes/WP84_PRODUCT_BLOCK_LARGE_SIEVE.md


## 10. Torus-distance strengthening and Dirichlet cancellation

The linear detuning bound in Section 6 can be upgraded to the natural
mod-one distance.

Put

    delta=|s-t| in [0,1],

    rho=min(delta,1-delta).

For delta<=1/2, Section 6 already gives

    |E|<=630 rho.

For delta>=1/2, use the endpoint geometry directly.

Every first-walk overlap contains both the initial point 0 and the final
endpoint s-t.  Therefore

    O_A
      <=
      1-delta
      =
      rho.

Since |B4_nc|<=26, the six-word connected sum obeys

    |C_6|
      <=
      6*26*rho
      =
      156 rho.

For the cross-scale reference,

    min(c_s,c_t)
      <=
      1-|s-t|
      =
      rho,

so

    0<=G<=2 rho.

Hence globally

    boxed:

    |E(s,t;x,y)|
      <=
      630
      dist(s-t,Z).

Now use the exact Dirichlet kernel

    D_d(u)
      =
      sin(pi d u)
      /
      [
        d sin(pi u)
      ]

up to a unit phase.

For

    rho=dist(u,Z)<=1/2,

    |sin(pi u)|
      >=
      2 rho.

Thus

    |D_d(u)|
      <=
      min(
        1,
        1/(2d rho)
      ).

Combining with the residual bound gives the pointwise high-frequency
cancellation

    boxed:

    |E_ij K_ij|
      <=
      315/d.

This is a genuine detuning-versus-Dirichlet cancellation: the zero of the
cross-scale residual at exact scale matching and at the mod-one alias walls
cancels the singular denominator of the finite trace.

Important:

    the entrywise 315/d bound alone does not close the quadratic form,
    because an l1 estimate for the full product coefficient is too costly.

The remaining step must preserve either:

- product-block l2 structure through a Schur/large-sieve estimate; or
- the exact finite-branch separability of E before taking absolute values.

Still, the dangerous high-frequency denominator is now removed exactly.


## 11. Superseding sharp residual theorem

The coarse constants 630 and 315/d above are no longer authoritative.

The exact alternating-word chamber reduction now gives

    boxed:

    -dist(s-t,Z)
      <=
      E(s,t;x,y)
      <=
      0.

Hence

    boxed:

    |E|
      <=
      dist(s-t,Z).

Consequently the divided difference

    H_ij
      =
      E_ij/(z_i-z_j)

satisfies

    boxed:

    |H_ij|
      <=
      1/4,

and the finite-trace product obeys

    boxed:

    |E_ij K_ij|
      <=
      1/(2d).

The proof is not a numerical optimization.  It comes from the exact two
alternating-word formulas on the fundamental chamber and elementary case
analysis.

See:

    notes/WP84_CROSS_SCALE_SHARP_DETUNING.md
    src/wp84_cross_scale_sharp_detuning.py
