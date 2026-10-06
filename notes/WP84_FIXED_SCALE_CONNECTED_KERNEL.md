# WP84 — fixed-product-scale connected kernel is a negative Brownian covariance

Date: 2026-10-06

Status: **EXACT FIXED-SCALE FACTORIZATION — AFTER SUMMING THE SIX BALANCED SIGN INTERLEAVINGS, THE CONNECTED OVERLAP KERNEL IS NEGATIVE SEMIDEFINITE ON EACH EXACT PRODUCT-SCALE SLICE**

No unconditional zero-density percentage is claimed here.

The remaining positive fourth-order finite-compression debt was localized to
outer detuning lobes because the individual balanced connected amplitude is
nonpositive while the finite trace scalar can change sign.

There is a stronger structure after the complete six-word balanced
interleaving sum is assembled.

## 1. Pair coordinates

Fix a normalized product scale

    1<=s<=2.

Write one positive factor pair as

    x,
    s-x,

and another as

    y,
    s-y,

with every individual factor in [0,1].

Define

    r_x=min(x,s-x),
    r_y=min(y,s-y),

and

    c=s-1.

Because both factors are at most one,

    r_x>=c,
    r_y>=c.

Let C_s(x,y) be the sum of the six balanced sign interleavings of the exact
nonclosed connected overlap amplitude

    O_A(v) B4_nc(v),

with positive steps x,s-x and negative steps -y,-(s-y).

## 2. Exact six-interleaving identity

The companion symbolic certificate proves

    boxed:

    C_s(x,y)

      =
      -2(s-1)
      [
        min(r_x,r_y)
        -(s-1)
      ].

The proof uses only exact rational/symbolic arithmetic.

By the symmetries

    x <-> s-x,
    y <-> s-y,
    x <-> y,

it reduces to

    1<=s<=2,
    s-1<=x<=y<=s/2.

On that reduced polytope every max/min/cutoff branch hyperplane has a fixed
weak sign.  The symbolic branch sum then collapses identically to

    -2(s-1)[x-(s-1)].

No floating acceptance decision enters the checker.

## 3. Negative-semidefinite factorization

The min-kernel has the exact Gram representation

    min(r_x,r_y)-c

      =
      int_c^(s/2)
        1_{u<=r_x}
        1_{u<=r_y}
      du.

Therefore

    boxed:

    -C_s(x,y)

      =
      2c
      int_c^(s/2)
        1_{u<=r_x}
        1_{u<=r_y}
      du

is positive semidefinite.

Equivalently,

    boxed:

    C_s

is a negative-semidefinite kernel on every exact product-scale slice.

This is substantially stronger than pointwise nonpositivity.

## 4. Interaction with the finite Fourier trace

For any product indices m_i, the finite-compression trace matrix

    K_ij
      =
      d^(-1)
      sum_k
        exp(
          i tau_k log(m_i/m_j)
        )

is Hermitian positive semidefinite: it is a Gram matrix of the vectors

    d^(-1/2)
    (
      exp(i tau_k log m_i)
    )_k.

Hence, on an exact common product-scale slice,

    -C_s

and

    K

are both positive semidefinite.

By the Schur product theorem,

    boxed:

    (-C_s) o K

is positive semidefinite.

Thus for arbitrary complex coefficient vector z,

    boxed:

    sum_{i,j}
      conjugate(z_i)
      C_s(i,j)
      K_ij
      z_j

      <=0.

This signs the complete finite-compression connected contribution on an
exact scale slice, including every outer Dirichlet lobe.

No shifted-prime correlation estimate is needed for this fixed-scale sign.

## 5. Remaining mismatch: product scale is only approximately fixed

In the actual nonclosed trace,

    s_i-s_j
      =
      log(m_i/m_j)/L.

Near resonance gives

    |s_i-s_j|
      =
      O(1/(TL)).

So the exact equal-scale theorem is already at the correct asymptotic
resolution.

A theorem-grade passage can use a product-scale partition of width

    delta_L ->0,

with

    1/(TL)
      =
      o(delta_L).

Inside each cell, freeze the connected kernel to the cell scale and use the
negative-semidefinite Schur-product theorem.

Cross-cell near-resonant pairs can only occur in a boundary strip of width

    O(1/(TL))

around the cell boundaries.

The normalized prime-product measure has one-dimensional discrepancy
O(1/L), so with

    delta_L=L^(-1/2),

the total boundary-strip mass is bounded schematically by

    O(
      1/(TL delta_L)
      +1/(L delta_L)
    )

      =
      O(L^(-1/2)).

The within-cell freezing error is O(delta_L) because every overlap factor is
piecewise affine with a fixed finite ledger.

Therefore the expected total scale-freezing error is

    boxed:

    O(L^(-1/2))

provided the existing prime-measure normalization is applied to the exact
balanced coefficient measure.

This last normalization step must be written explicitly before promoting the
full nonclosed sector to theorem-closed.

## 6. Structural consequence

The arithmetic frontier changes again.

The outer negative Dirichlet lobes are not intrinsically dangerous once the
six balanced connected words are assembled at a common product scale.

The finite trace itself is a positive-semidefinite Gram kernel, and the
six-word connected amplitude is a negative-semidefinite Brownian min-kernel.

Their Schur product therefore has the correct sign globally.

The remaining task is no longer an outer-lobe correlation theorem.  It is a
scale-freezing/boundary-strip estimate.

This is the same mathematical pattern as a boundary-annulus reduction:
the bulk same-scale interaction is sign-closed, and only the thin interface
between neighboring scale cells has to be estimated.

## 7. Evidence boundary

Closed:

- exact six-interleaving fixed-scale identity;
- exact negative-semidefinite Brownian factorization;
- exact positive-semidefinite finite-trace Gram structure;
- exact same-scale Schur-product sign.

Still open:

- write the product-scale partition against the exact WP84 coefficient
  normalization and prove the boundary-strip plus freezing error is o(1).

No unconditional record theorem is claimed.

See:

    notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md
    notes/WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md
    notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md
