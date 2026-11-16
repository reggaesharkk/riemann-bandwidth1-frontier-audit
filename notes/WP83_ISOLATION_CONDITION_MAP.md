# WP83 — isolation condition map for Proposition R

Date: 2026-10-04
Status: **PAIR-LEVEL CONDITIONING REDUCED TO A NEW COMPLEX-POISSON GATE; NO UNCONDITIONAL GLOBAL ISOLATION FROM GABOR SPACING ALONE**

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

for the relevant evaluation family is a sufficient globalization lemma.

## 2. Localized version

Let V_J be one selected pair or cluster and V_rest all remaining evaluation columns. Let P_perp be orthogonal projection onto the complement of span(V_rest). Then

    P_perp Q P_perp
      = (P_perp V_J) H_J (P_perp V_J)*.

If

    sigma_min(P_perp V_J)^2 >= a_J > 0,

then

    ||Q||_op >= ||P_perp Q P_perp||_op
             >= a_J ||H_J||_op.

This is the exact finite-dimensional isolation obligation.

## 3. Source audit: the public formalization does NOT prove complex Poisson

The public Lean file `zeta23/Zeta23/Poisson.lean` explicitly says that it proves the Poisson--Gabor identity only for **real** arguments and that the complex continuation mentioned in the paper's pair-block remark is not used by the proof.

Therefore the earlier draft of this note was too aggressive when it treated

    sum_k phihat(z-alpha_k) phihat(z'-alpha_k)
      = L * widehat(phi^2)(z-z')

for complex z,z' as already source-closed.

It is not source-closed.

## 4. Independent complex-continuation target

The continuation is nevertheless a concrete theorem we can try to prove.

For the actual C^2 compactly supported taper, the strip estimate

    |phihat(r-i y)| <= exp(L|y|/2) * C / |r-i y|^2

is available for |y|<=1/2.

Hence on every compact subset of the zero strip, the series

    F(z,z') = sum_k phihat(z-alpha_k) phihat(z'-alpha_k)

is normally convergent because each factor is O(k^-2), so the product is O(k^-4).

Thus F is holomorphic separately in z and z'. The right side

    L * widehat(phi^2)(z-z')

is entire.

The real-real identity is already proved. Fix real z'. Identity in the variable z extends from the real line to the strip by the one-variable identity theorem. Then fix the now-complex z and extend in z' from the real line in the same way.

This would prove the complex identity throughout the relevant strip.

This argument still needs a polished write-out checking the uniform compact-strip decay and the exact Fourier convention. Until that is frozen, pair-level complex Gram formulas remain **derived-but-not-yet-closed**.

## 5. Consequence if the complex continuation is closed

Let

    z = gamma - i*delta,
    zbar = gamma + i*delta,

and u be the infinite-grid evaluation vector at z.

Because phi is real,

    v(zbar)=conj(v(z)).

Define

    A = L * widehat(phi^2)(2 i delta),
    B = L * widehat(phi^2)(0).

Then the complex Poisson identity would give

    ||u||^2 = A,
    sum_k u_k^2 = B.

Writing u=x+i y with real x,y gives

    x dot y = 0,
    ||x||^2 = (A+B)/2,
    ||y||^2 = (A-B)/2.

The single off-line pair contribution

    2m (x x^T - y y^T)

would therefore have exact nonzero eigenvalues

    m(A+B),
    -m(A-B).

For delta!=0 and a nontrivial even window,

    A>B,

because widehat(phi^2)(2 i delta) is the integral of phi(u)^2 cosh(2 delta u), strictly larger than its value at zero.

So a **single infinite-grid off-line pair is internally nondegenerate** once the complex-continuation gate is proved.

## 6. Finite compression is another separate gate

The actual compressed Weil matrix uses only k=0,...,d-1, not the full infinite lattice.

Therefore the infinite-grid spectrum above is not yet the spectrum of the consumed finite pair block.

To transfer it, we need a tail estimate showing that for a target zero placed well inside the active frequency window, the omitted k<0 and k>=d evaluation energy is negligible relative to A-B.

Because the moment statement is supposed to hold for every large dyadic height, a target zero at ordinate gamma can in principle be placed in the interior of a suitable dyadic window rather than at an endpoint. But the resulting finite-grid capture estimate must be written explicitly.

## 7. Why Gabor spacing still does not globalize

Even after the complex-Poisson and finite-capture gates close, they only control one pair.

The spacing

    alpha_{k+1}-alpha_k=2*pi/L

is spacing of the **test frequencies**. It is not a spacing theorem for the zero ordinates.

A lower bound for sigma_min(V) over many zero evaluation vectors requires quantitative control of the full Gram matrix for the actual zero set. Such a bound can collapse under near-collisions.

Neither C26 nor the declared prime-side inputs gives a uniform polynomial lower bound on distinct zero spacing.

Therefore critical-density Gabor sampling by itself does not supply the missing Proposition-R globalization lemma.

## 8. Three sufficient globalization mechanisms

### R1 — global Riesz lower bound

Prove

    V*V >= a I

on the complete relevant off-line family with a at worst polylogarithmically small.

Status: OPEN; also impossible by dimension counting whenever the selected column family has more columns than the Gabor dimension.

### R2 — isolated pair/cluster after projection

Find one maximal-depth pair/cluster J with

    sigma_min(P_perp V_J) >= (log T)^(-C).

Status: OPEN. This is the cleanest exact form of the reviewer isolation obligation.

### R3 — depth-gap dominance

Split

    Q=Q_max+R.

If the maximal-depth block/cluster is exponentially larger than the rest, Weyl's inequality prevents cancellation.

Status: NOT AVAILABLE UNCONDITIONALLY; no suitable depth-gap theorem for zeta zeros is among the declared inputs.

## 9. Cluster variant

Near-colliding zeros must be treated as one cluster. A cluster theorem would need a lower bound for the smallest nonzero singular value of its projected evaluation matrix.

Distinct zeros cannot simply be relabelled as multiplicities. No unconditional polynomial spacing lower bound is available from the present input list.

## 10. Current verdict

The targeted search does **not** show that the specific Gabor grid bypasses Proposition R.

What it does show is a sharper sequence of gates:

    real Poisson identity [SOURCE-CLOSED]
      -> complex continuation [DERIVABLE; WRITE-OUT OPEN]
      -> exact isolated-pair spectrum [CONDITIONAL ON PREVIOUS]
      -> finite-grid capture [OPEN]
      -> pair/cluster isolation against background [OPEN]
      -> Proposition-R moment-to-zero-free implication.

The final isolation step remains the genuine barrier.


## 11. Two-window cluster-energy refinement

The raw two-window inequality in coefficient l2 norm is false without zero spacing: for any finite family of analytic observation windows U(z), the two columns U(z), U(z+eps) have a difference of size O(eps), so their smallest Gram eigenvalue is O(eps^2).

The correct near-collision coordinates are confluent jets. For a cluster of size s<=4, the full-lattice centered-jet Gram dominates

    c_s * L * exp(delta L - 2 delta(w+1)),

with exact rational Hilbert floors

    c_1=1,
    c_2=1/16,
    c_3=5/25392,
    c_4=49/1395654656.

Thus internal cluster energy is quantitatively nonzero in confluent coordinates even when raw zero nodes coalesce. The remaining barrier is not cluster self-conditioning but **background isolation**: show that one/two finite windows retain a polynomially large component of this cluster energy after projecting away all other clusters.

See `WP83_TWO_WINDOW_CLUSTER_ENERGY.md`.
