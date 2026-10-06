# WP84 — detuning commutator converts the residual Fourier kernel to a rank-two endpoint carrier

Date: 2026-10-06

Status: **EXACT FINITE-DIMENSIONAL IDENTITY — THE SCALE-DETUING FACTOR CAN BE MOVED ONTO THE FINITE-TRACE GRAM MATRIX AS A RANK-TWO ENDPOINT COMMUTATOR**

No unconditional zero-density percentage is claimed here.

The active connected-sector remainder is

    c^*(E o K)c,

where

    K_ij
      =
      exp(i T L(s_i-s_j))
      D_d(s_i-s_j),

and

    |E_ij|
      <=
      630 dist(s_i-s_j,Z).

This note records the exact commutator identity behind the high-frequency
regularization.

## 1. Phase variable

Put

    z_i=exp(2 pi i s_i),

    v_i=exp(i T L s_i),

and let

    Z=diag(z_i),
    V=diag(v_i).

The normalized Dirichlet Gram matrix is

    D_ij
      =
      d^(-1)
      sum_{k=0}^{d-1}
        (z_i conjugate(z_j))^k.

Then

    K=V D V^*.

## 2. Exact endpoint identity

For every i,j,

    (z_i-z_j)D_ij

      =
      d^(-1)
      [
        z_i^d z_j^(1-d)
        -
        z_j
      ].

Therefore

    boxed:

    [Z,K]
      =
      d^(-1)
      [
        a b^*
        -
        v w^*
      ],

where

    a_i=v_i z_i^d,

    b_i=v_i z_i^(d-1),

    w_i=v_i conjugate(z_i).

Hence

    boxed:

    rank[Z,K]<=2

exactly.

The apparent singularity of the Dirichlet kernel has disappeared.  Only the
two Fourier endpoints remain.

## 3. Exact factorization of the detuning residual

For i!=j define

    H_ij
      =
      E_ij/(z_i-z_j),

and put H_ii=0.

Then exactly

    boxed:

    E o K

      =
      H o [Z,K].

No approximation is used.

The torus-distance bound gives a uniform entrywise estimate for H.  Since

    |z_i-z_j|
      =
      2|sin(pi(s_i-s_j))|

and, for rho=dist(s_i-s_j,Z)<=1/2,

    |sin(pi rho)|
      >=
      2 rho,

we obtain

    boxed:

    |H_ij|
      <=
      630/4
      =
      157.5.

Thus the complete positive connected debt has been moved from a dense
Dirichlet Gram matrix to a Schur action on a rank-two endpoint carrier.

## 4. Why entrywise boundedness is not yet closure

A uniformly bounded matrix is not automatically a uniformly bounded Schur
multiplier.

Therefore the estimate

    |H_ij|<=157.5

must not be converted into a dimension-free operator bound without further
structure.

The remaining theorem target is sharper than before:

    boxed:

    prove that the divided-difference kernel H has a dimension-free Schur
    multiplier / finite-feature bound on the exact balanced coefficient
    space.

If

    ||M_H||_Schur=O(1),

then the connected remainder reduces to the two endpoint quadratic forms
coming from the rank-two matrix [Z,K].

Those endpoint forms are explicit semiprime Dirichlet-polynomial quantities
at the lower and upper Fourier boundaries.

## 5. Relation to the existing arithmetic tools

This identity isolates the precise places where existing arithmetic input may
be used:

- the upper endpoint lies at carrier height comparable with T or 2T and can
  be tested against the existing high-frequency prime-polynomial machinery;

- the lower endpoint is the only potentially nonoscillatory boundary term;

- the connected ordered-partition cancellation must be checked before
  estimating that lower endpoint, because an absolute-value bound there
  would reintroduce the large l1 mass.

Thus the next gate is no longer a generic high-frequency estimate.  It is:

    connected overlap divided difference
      -> finite Schur feature decomposition
      -> two endpoint Dirichlet forms.

## 6. Evidence boundary

Closed:

- exact rank-two commutator identity for the finite trace;
- exact factorization E o K = H o [Z,K];
- uniform entrywise bound on H.

Open:

- dimension-free Schur/feature control of H;
- endpoint arithmetic after that feature decomposition.

No unconditional record theorem is claimed.

See:

    notes/WP84_CROSS_SCALE_BROWNIAN_REFERENCE.md
    notes/WP84_PRODUCT_BLOCK_LARGE_SIEVE.md
    notes/WP84_BALANCED_PRODUCT_SECOND_MASS.md
