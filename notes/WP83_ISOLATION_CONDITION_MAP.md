# WP83 — isolation condition map for Proposition R

Date: 2026-10-04
Status: **PAIR-LEVEL CONDITIONING DERIVED; NO UNCONDITIONAL GLOBAL ISOLATION FROM GABOR SPACING ALONE**

Goal: identify exact spectral hypotheses under which the signature-(1,1) off-line blocks cannot cancel in the full compressed Weil matrix.

## 1. Abstract cancellation lemma

Let V be the matrix whose columns are the evaluation vectors attached to a chosen collection of off-line zero partners, and let H be the block-diagonal hyperbolic coefficient matrix. The resulting contribution is

    Q = V H V*.

If V has full column rank, then with V^dagger its Moore--Penrose left inverse,

    H = V^dagger Q (V^dagger)*.

Hence

    ||Q||_op >= sigma_min(V)^2 ||H||_op.

Therefore a quantitative lower Riesz bound

    sigma_min(V)^2 >= a > 0

for the relevant evaluation family is a sufficient globalization lemma. Under such a bound, exact cancellation of a nonzero hyperbolic block family is impossible.

## 2. Localized version

Let V_J be one selected pair or cluster and V_rest all remaining evaluation columns. Let P_perp be orthogonal projection onto the complement of span(V_rest). Then

    P_perp Q P_perp
      = (P_perp V_J) H_J (P_perp V_J)*.

If

    sigma_min(P_perp V_J)^2 >= a_J > 0,

then

    ||Q||_op >= ||P_perp Q P_perp||_op
             >= a_J ||H_J||_op.

This is the precise finite-dimensional form of an isolation lemma: one must exhibit a pair/cluster whose evaluation vectors retain a quantitative component outside the span of all competing pairs.

## 3. What critical-density Gabor spacing actually gives

C26's Poisson--Gabor identity controls the Gram kernel of evaluation vectors. For complex evaluation points z,z',

    sum_k phihat(z-alpha_k) phihat(z'-alpha_k)
      = L * widehat(phi^2)(z-z').

For an off-line pair with depth delta, z=gamma-i*delta and zbar=gamma+i*delta. Because phi is real/even, the two-column Gram matrix has the symmetric form

    G_pair = [[A,B],[B,A]],

with

    A = L * widehat(phi^2)(2 i delta),
    B = L * widehat(phi^2)(0).

Thus its two squared singular values are

    A+B,  A-B.

For delta>0 and a nontrivial window, A>B, so a **single isolated pair is internally nondegenerate**. For the flat-window heuristic, A grows like sinh(delta L)/delta while B is only of order L; this recovers the exponential/off-line amplification behind Proposition R.

## 4. Why this does not yet globalize

The Gabor spacing alpha_{k+1}-alpha_k=2*pi/L is spacing of the **test frequencies**. It is not a spacing theorem for the zero ordinates gamma.

A lower bound for sigma_min(V) over many zero evaluation vectors requires quantitative control of the Gram matrix

    widehat(phi^2)(z_i-z_j)

for distinct zeros. Such a bound can fail or become arbitrarily small when evaluation points cluster. Neither C26 nor the declared prime-side inputs supply a uniform separation theorem for distinct zeta zeros.

Therefore critical-density Gabor sampling by itself does not provide the missing Proposition-R globalization lemma.

## 5. Three sufficient mechanisms and their status

### R1 — global Riesz lower bound

Prove V*V >= a I on the complete off-line family with a at worst polylogarithmically small.

Status: OPEN; impossible from dimension counting if the selected column family has more columns than the Gabor dimension.

### R2 — isolated pair/cluster after projection

Find one maximal-depth pair/cluster J with

    sigma_min(P_perp V_J) >= (log T)^(-C).

Status: OPEN. This is the cleanest direct form of the reviewer isolation obligation.

### R3 — depth-gap dominance

Split Q=Q_max+R. If one depth delta_max exceeds all competing depths by a fixed/logarithmic gap and

    ||Q_max|| >> ||R||,

then Weyl's inequality prevents cancellation.

Status: NOT AVAILABLE UNCONDITIONALLY; no suitable depth-gap theorem for zeta zeros is among the declared inputs.

## 6. Cluster variant

If several zeros share nearly the same ordinate/depth, they must be treated as one cluster. A cluster-level globalization theorem would need a lower bound for the smallest nonzero singular value of its evaluation matrix after projecting away the background.

Near-collisions cannot simply be called multiplicities: distinct zeros may be arbitrarily close, and no unconditional polynomial spacing lower bound is available from the current input list.

## 7. Consequence for Proposition R

The pair-level exponential amplification is structurally real, but the missing step is now exact:

    local off-line amplification
       + quantitative evaluation-vector isolation
       => full-matrix operator lower bound
       => finite even moment bound forces a power-law zero-free strip.

The second arrow is the only unresolved part of our reconstruction.

## 8. Current verdict

The specific Gabor dimension/frequency spacing does **not** presently bypass Proposition R. It gives an exact Gram kernel and strong conditioning for one isolated pair, but no theorem-grade lower frame bound against an arbitrary background of clustered zero evaluations.

The next productive search is for an argument using extremal depth plus the exact Poisson--Gabor kernel to prove R2 at cluster level without assuming zero spacing. If that cannot be done, the successor retraction remains a genuine external barrier rather than a bookkeeping issue.
