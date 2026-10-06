# WP84 — scale-freezing bridge for the balanced connected sector

Date: 2026-10-06

Status: **THEOREM INTERFACE — THE EXACT FIXED-SCALE NEGATIVE KERNEL REDUCES THE NONCLOSED FOURTH-ORDER DEBT TO A THIN SCALE-BOUNDARY / COMMUTATOR ERROR**

No unconditional zero-density percentage is claimed here.

The exact fixed-product-scale theorem gives a negative-semidefinite connected
kernel

    C_s<=0

after the six balanced sign interleavings are assembled.

The finite Fourier trace kernel

    K_ij
      =
      d^(-1)
      sum_k exp(i tau_k log(m_i/m_j))

is positive semidefinite.

Hence, at exactly equal product scale, the Schur product has the correct sign
for every coefficient vector.

The actual finite-compression relation is only slightly off equal scale:

    s_i-s_j
      =
      log(m_i/m_j)/L.

For the only non-negligible near-resonant pairs,

    |log(m_i/m_j)|
      =
      O(1/T),

so

    boxed:

    |s_i-s_j|
      =
      O(1/(TL)).

This note records the theorem interface needed to turn the exact equal-scale
sign into an asymptotic full-sector sign.

## 1. Partition the product-scale axis

Partition

    1<=s<=2

into cells of width

    delta_L=L^(-1/2).

The near-resonant scale mismatch satisfies

    1/(TL)
      =
      o(delta_L).

Therefore a near-resonant pair can lie in nonadjacent cells only if the
Dirichlet trace is already negligible.

Pairs crossing an adjacent-cell boundary must have at least one product scale
inside an O(1/(TL)) strip around that boundary.

## 2. Boundary-strip mass

The normalized prime measure has one-dimensional discrepancy

    D_L=O(1/L).

The two-factor product-scale measure is its convolution.

For one strip of width eps,

    product-mass(strip)
      =
      O(eps+1/L).

There are O(1/delta_L) cell boundaries.

With

    eps=O(1/(TL)),

the total boundary-strip mass is

    O(
      1/(TL delta_L)
      +
      1/(L delta_L)
    )

      =
      O(L^(-1/2)).

Thus the only near-resonant pairs that can cross scale cells form an
asymptotically negligible boundary annulus.

## 3. Bulk same-cell reduction

Inside one cell, freeze the common product scale at its center s_0.

The exact connected amplitude is piecewise polynomial of bounded degree with
a finite branch ledger.

Away from its finitely many branch walls, changing the two product scales by

    O(delta_L)

changes the kernel by a finite sum of diagonal commutator / anticommutator
terms whose coefficients are O(delta_L).

The finite-trace Gram matrix has the standard large-sieve operator scale

    ||K||_op
      <=
      C(1+M/T)

on a product block m~M.

Write

    H=M/T.

On the near-resonant support,

    |s_i-s_j|
      =
      O(1/(TL)).

Therefore the commutator-scale perturbation is bounded schematically by

    O(
      (1+H)/(TL)
    ).

Since the retained balanced product scale has

    M<=T^2+o(T^2),

we have

    H<=T+o(T),

and hence

    boxed:

    (1+H)/(TL)
      =
      O(1/L).

So the large-sieve amplification is cancelled by the much smaller normalized
scale mismatch.

This is the key high-frequency cancellation.

## 4. Branch-wall annuli

The only place where the piecewise-polynomial branch formula can change is a
finite family of linear walls in the factor variables.

A scale partition may be refined by these walls.

Near-resonant pairs that cross a branch wall are again confined to an
O(1/(TL)) neighborhood of that wall.

The same discrepancy / boundary-annulus estimate gives o(1) total normalized
mass after summing finitely many wall families.

## 5. Resulting theorem target

The complete balanced connected sector decomposes as

    bulk same-scale cells
      +
    scale-boundary annuli
      +
    branch-wall annuli
      +
    Dirichlet-negligible far detuning.

The bulk contribution is nonpositive by

    fixed-scale negative-semidefinite kernel
      +
    finite-trace positive-semidefinite Gram kernel
      +
    Schur product theorem.

The annular terms are the only positive errors.

The target is therefore

    boxed:

    positive connected leakage
      =
      O(L^(-1/2))
      +
      O(L^(-1))
      +
      o(1)

      =
      o(1).

If the exact WP84 coefficient normalization satisfies the standard bounded
second-mass ledger already used in the pair sector, this closes the balanced
connected fourth-order error without importing a new shifted-prime
correlation theorem.

## 6. Why this route is preferable

The earlier principal-arc route treated the shifted correlations first and
their signs later.  That generated an artificial H-loss.

The present route reverses the order:

1. assemble the exact six connected words;
2. exploit the negative-semidefinite equal-scale kernel;
3. keep the finite trace as a positive-semidefinite Gram matrix;
4. estimate only the thin scale/interface mismatch.

This is the same mathematical architecture as a boundary-annulus argument:
the bulk is controlled structurally and only the interface needs an
estimate.

## 7. Remaining explicit checks

Before this can be promoted to theorem-closed, verify:

1. the six-interleaving kernel is exactly the balanced connected ledger used
   by the fixed-band fourth moment, with no missing orientation factor;

2. the normalized coefficient vector has the bounded second mass required
   by the large-sieve quadratic-form estimate;

3. the product-scale and branch-wall strip discrepancy is inserted with the
   exact taper/prime-power normalization;

4. the fixed-block large-sieve constant is uniform over the consumed smooth
   product cells.

No unconditional record theorem is claimed.

See:

    notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md
    src/wp84_fixed_scale_connected_kernel.py
    notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md
    notes/WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md
