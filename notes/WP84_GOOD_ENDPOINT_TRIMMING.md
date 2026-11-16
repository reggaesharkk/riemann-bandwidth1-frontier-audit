# WP84 — good-endpoint trimming closes the detuning endpoint family

Date: 2026-10-06

Status: **THEOREM-SIDE REDUCTION; THE RANK-TWO ENDPOINT DEBT CAN BE AVERAGED OVER AN o(d) FREQUENCY-ROW QUARANTINE AND BOUNDED BY THE CLASSICAL DIRICHLET-POLYNOMIAL MEAN-VALUE THEOREM**

No unconditional zero-density percentage is claimed here.

The connected detuning remainder has already been reduced to a finite family of
rank-two endpoint terms.  The obstacle was that the two hard Fourier endpoints
are fixed frequencies, while the strongest generic Dirichlet-polynomial tools
are mean-square statements.

For the bounded first-strike consumer we may delete o(d) Fourier rows before
using the quartic fixed-band fallback.  This converts the fixed endpoints into
endpoints chosen from short candidate windows.  A mean-square argument then
selects good endpoints.

## 1. Rank-small row quarantine is allowed before the quartic step

Let H_d be the full sharp Hermitian matrix and let H_I be a contiguous
principal submatrix obtained by deleting r rows in total from the two
frequency-band ends.

Embed H_I back into d dimensions by adjoining zeros.  The difference from
H_d has rank at most 2r.  Therefore the empirical spectral distribution
functions differ by O(r/d).

For every fixed bounded rational consumer of bounded variation, in particular
the matched bounded consumer used before the quartic majorant,

    |tau_d f(H_d) - tau_|I| f(H_I)| = O(r/d).

Choose

    epsilon_L = L^(-1/2),

    r = floor(epsilon_L d).

Then

    r/d = O(L^(-1/2)) = o(1).

This rank deletion is performed while the theorem object is still bounded.
Only afterwards do we apply the fixed-band resolvent comparison and quartic
majorant to the selected principal section.

## 2. Candidate endpoint windows

The lower endpoint may be chosen among the first r retained Fourier-grid
positions and the upper endpoint among the last r positions.

The grid spacing is

    Delta_tau = 2 pi/L.

Hence each candidate window has physical frequency length

    U
      asymp
      r/L
      asymp
      epsilon_L T.

The selected principal section still has dimension

    d' = d(1+O(epsilon_L)),

and both its lower carrier height and its total frequency span are
T(1+O(epsilon_L)).  All fixed-R continuum covariance formulas therefore
change by only o(1).

## 3. Integrated endpoint feature families

After the exact sharp detuning formula, the rank-two endpoint commutator, and
the finite threshold-feature decomposition, every remaining endpoint object
has the form

    S_theta(tau)
      =
      sum_{m<=N}
        a_m(theta)
        exp(i tau log m),

where

    N <= T^2,

theta ranges over one or two compact feature parameters, and the feature
weights satisfy |feature|<=1.

The balanced product second-mass theorem gives

    int
      sum_m |a_m(theta)|^2
    dtheta
      <= C

uniformly in T.

Proper prime-power pieces are o(1) in this norm.

The universal Fourier multiplier introduced by the divided-difference ratio
has absolutely summable coefficients, so it changes only the fixed constant C.

## 4. Discrete mean-square estimate on a candidate window

The Montgomery--Vaughan mean-value theorem gives, uniformly for any interval
J of length U,

    int_J |S_theta(t)|^2 dt
      <=
      C (U+N)
      sum_m |a_m(theta)|^2.

For the actual Fourier grid, with spacing h=2 pi/L, use the elementary local
Sobolev sampling inequality on disjoint h-cells (enlarging J by O(h) at the
two ends):

    sum_{tau_k in J} |S_theta(tau_k)|^2
      <=
      C [
        h^(-1) int_{J+} |S_theta(t)|^2 dt
        + h int_{J+} |S_theta'(t)|^2 dt
      ].

Here

    S_theta'(t)
      =
      i sum_{m<=N}
          (log m) a_m(theta) exp(i t log m).

Apply Montgomery--Vaughan separately to S_theta and S_theta'.  Since

    N<=T^2,
    log N=O(L)

in the active scaling, the derivative term obeys

    h (U+N)
      sum_m (log m)^2 |a_m(theta)|^2
      <=
      C L (U+N)
      sum_m |a_m(theta)|^2,

while the zeroth-order term has the same C L(U+N) scale.  Therefore, after
integrating the finite feature parameters and using their uniform second-mass
bound,

    sum_{k in window}
      int |S_theta(tau_k)|^2 dtheta

      <=
      C L (U+N).

This supplies the discrete step directly; no unproved pointwise sampling
claim is being inserted.

Since

    r asymp U L,

the average endpoint score is at most

    C (1+N/U).

With N<=T^2 and U asymp epsilon_L T,

    boxed:

    average endpoint score
      <=
      C T/epsilon_L.

Therefore there exists a lower endpoint k_- and independently an upper
endpoint k_+ such that every finite summed/integrated feature score required
by the commutator reduction is bounded by

    O(T/epsilon_L).

Include the adjacent Fourier index in the score so that the two rank-one
vectors in each endpoint commutator term are covered simultaneously.

## 5. Final endpoint budget

Each rank-two commutator term carries the normalization

    1/d'.

For a feature integral, Cauchy--Schwarz in the feature parameter gives

    endpoint contribution

      <=
      C/d'
      *
      sqrt(T/epsilon_L)
      *
      sqrt(T/epsilon_L).

Hence

    endpoint contribution

      <=
      C
      T/(epsilon_L d').

Since

    d' asymp T L,

    boxed:

    endpoint contribution
      =
      O(
        1/(epsilon_L L)
      ).

With epsilon_L=L^(-1/2),

    boxed:

    endpoint contribution
      =
      O(L^(-1/2))
      =
      o(1).

The finite number of threshold families and the absolutely summable
Fourier-multiplier family preserve this rate.

## 6. Consequence for the balanced connected sector

The exact decomposition is

    connected kernel
      =
      negative-semidefinite Brownian reference
      +
      detuning remainder.

The first term is nonpositive.

The second term has now been reduced to endpoint families whose total
positive contribution is o(1) after the good-endpoint row quarantine.

Therefore, on the selected principal section,

    boxed:

    positive balanced connected leakage
      =
      o(1).

The principal-section deletion itself costs only o(1) at the bounded consumer
level.

Thus the connected fourth-order finite-compression sector no longer requires a
new shifted-prime or semiprime correlation theorem.

## 7. Fixed-band fourth-moment implication

At R=400 the exact pair layer satisfies

    Pair_400 < 0.266329.

The connected sector contributes at most o(1) positively, so

    limsup w_400
      <=
      0.266329,

for the selected principal section, provided the already-closed unbalanced and
proper-power sectors are inserted in the same normalization.

This is strictly below the centered-fourth record ceiling

    W_400
      =
      0.2911227517....

The remaining promotion check is bookkeeping:

1. replay the complete fixed-band order-four ledger on the selected principal
   section;
2. verify every non-balanced remainder is already in an o(1) gate;
3. assemble the matched bounded-consumer rank charge, full-to-band charge,
   quartic majorant, and centered-fourth ceiling in one same-convention note.

## 8. External input

The only new analytic input is the classical Montgomery--Vaughan mean-value
theorem for Dirichlet polynomials,

    integral |sum_{n<=N} a_n n^(-it)|^2 dt
      <=
      (U+C N)
      sum |a_n|^2

on an interval of length U, with an absolute constant C.

No prime-specific cancellation is consumed.

## Evidence boundary

Closed in this note:

- rank-small frequency-end deletion at the bounded-consumer level;
- good-endpoint existence from generic Dirichlet-polynomial mean square;
- O(L^-1/2) endpoint budget for the finite feature family.

Still to assemble before a theorem claim:

- the complete same-normalization fixed-band fourth-order ledger after the
  principal-section selection;
- the final bounded-consumer inequality and percentage conversion.

No unconditional record theorem is claimed here.

See:

    notes/WP84_CROSS_SCALE_SHARP_DETUNING.md
    notes/WP84_DETUNING_COMMUTATOR_ENDPOINT.md
    notes/WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION.md
    notes/WP84_BALANCED_PRODUCT_SECOND_MASS.md
    notes/WP84_CENTERED_M4_SCALAR_GATE.md
