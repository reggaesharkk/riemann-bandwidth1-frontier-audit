# WP84 — consolidated theorem-state corrections

Date: 2026-10-05

Status: **AUTHORITATIVE CORRECTION LEDGER; NO UNCONDITIONAL >79% CLAIM**

This note consolidates the hostile-audit corrections that materially changed
the WP84 route.  It intentionally records only mathematical claims, not the
provenance of external reviews.

## 1. Radau beta values are surrogate evaluations

The displayed beta-consumer values such as

    q3 ~= 0.8964412949

are evaluations on one specific Radau representing measure.  They are not
lower bounds over all positive measures with the pinned moments through m6.

An exact positive rational seven-atom measure matching

    1, 1, 4/3, 2, 13/4, 101/18, 12809/1260

has

    E[b3] ~= 0.890363090084 < 0.895.

Therefore the former b3 fixed-circle tolerance is not an active theorem
budget.

## 2. Exact half-line certificate needs no support assumption

Let

    P(x)
      = 1
        - (43428/13891)x
        + (37704/13891)x^2
        - (9660/13891)x^3.

For the pinned moments,

    integral P(x)^2 dnu = 1415/13891.

Writing

    P(x)-1
      = -x(43428-37704x+9660x^2)/13891

shows immediately that P(x)>=1 for x<=0.  Hence

    nu((-infinity,0]) <= 1415/13891

and

    nu((0,infinity)) >= 12476/13891

for every positive Borel probability measure on R with the pinned moments.
No support restriction nu subset [0,infinity) is required.

The exact zero-side ledger converts this to

    11061/13891 = 0.7962709668...

provided the limiting arithmetic spectral law has the pinned moments.

## 3. Exact Hankel facts

For the 4x4 Hamburger Hankel matrix H=(m_{i+j})_{0<=i,j<=3},

    det H = 283/108864 > 0,
    e0^T H^{-1} e0 = 13891/1415.

The Christoffel function at zero is the reciprocal

    1415/13891.

The shifted 3x3 determinant

    det(m_{i+j+1})_{0<=i,j<=2}
      = 23/1296 > 0

uses only m1..m5.  No m7 enters that calculation.

Shifted-Hankel positivity is a Stieltjes support condition and is not required
for the Hamburger half-line certificate above.

## 4. Nonreal resolvent stability is deterministic

For every Hermitian H and every nonreal z,

    ||(H-zI)^(-1)||op <= 1/|Im z|.

No eigenvalue-repulsion or delocalization hypothesis is needed for this bound.

If Hermitian A,B differ by rank at most r in dimension d, then

    sup_x |F_A(x)-F_B(x)| <= r/d

and

    |m_A(z)-m_B(z)| <= pi*r/(d*Im z).

Thus an o(d)-rank deep-zero sector is invisible to the weak/Stieltjes limit,
even if its outlier eigenvalues are arbitrarily large.

## 5. Qualitative weak convergence suffices asymptotically

If nu_T converges weakly to nu_* and theta_T->0, then

    liminf_T nu_T((theta_T,infinity))
      >= nu_*((0,infinity)).

An explicit rate is required for an effective finite T0, but not for the
asymptotic liminf theorem.

## 6. Exact translation state

Non-cyclic translation words obey

    tr(S_{r1}...S_{rb})
      = 0                       if sum rj != 0,

and, for closed words,

    tr(S_{r1}...S_{rb})
      = max(0,N-(max p_j-min p_j)),

where p_j are the partial sums.

This exact spread law is the correct finite-section state geometry.
A scalar covariance closure loses information at order four.

## 7. Current closure boundary

The covariance-only multiplication model gives centered

    m4 = 7/30,

whereas the pinned target is

    1/4.

The exact deficit is

    1/60.

The finite F/G unitary variables do not close under repeated Duhamel
evolution; longer translation words are generated.

The next theorem gate is therefore the full operator-valued order-four
generator audit, followed by the arithmetic-to-model Stieltjes convergence
theorem.

## 8. Cross-research methodological lesson

A separate exact finite-dimensional bifurcation project established a hard
sign theorem by the pattern

    exact spectral identity
      -> exact elimination
      -> sign reduction
      -> same-sign rational coefficient certificate.

No bifurcation theorem is imported into WP84.  The reusable asset is only
this proof architecture.  The polynomial half-line certificate above is
already an instance of the same style.
