# WP83 — finite-grid capture of one deep off-line pair

Date: 2026-10-04
Status: **PAIR-LEVEL FINITE COMPRESSION CLOSED FOR FIXED DEPTH; GLOBAL CANCELLATION STILL OPEN**

This note transfers the infinite-lattice isolated-pair spectrum of `WP83_COMPLEX_POISSON_PAIR_SPECTRUM.md` to the actual finite Gabor compression.

## 1. Put the target ordinate in the interior

For a target zero ordinate gamma, choose the dyadic parameter

    T = 2*gamma/3.

Then

    gamma = 3T/2,

so the target lies a distance T/2 from both endpoints T and 2T.

The claimed moment asymptotics are statements for all sufficiently large T, so a Proposition-R contradiction is allowed to choose this height parameter around the target zero.

More generally it is enough to assume

    gamma in [5T/4,7T/4].

Then the distance to both grid edges is at least R=T/4 up to one grid spacing.

## 2. Omitted lattice energy

The full grid is

    alpha_k=T+k*h,
    h=2*pi/L.

The consumed matrix keeps k=0,...,d-1, with d=floor(T/h).

For the off-line coordinate

    z=gamma-i*delta,

the public all-complex taper bound gives

    |phihat(z-alpha_k)|
      <= exp(|delta|L/2) * C1 / |z-alpha_k|^2.

For every omitted index, the real distance from gamma is at least R+n*h for some n>=0. Hence

    sum_omitted |phihat(z-alpha_k)|^2
      <= 2 exp(|delta|L) C1^2
         * sum_{n>=0} (R+n*h)^(-4).

Using the monotone integral bound

    sum_{n>=0}(R+n*h)^(-4)
      <= R^(-4) + 1/(3*h*R^3),

we obtain

    boxed:
    E_tail
      <= 2 exp(|delta|L) C1^2
         * (R^(-4)+1/(3*h*R^3)).

For R=T/4 and h=2*pi/L,

    E_tail
      = O(exp(|delta|L) * C1^2 * L/T^3).

## 3. Lower bound for the off-line pair energy

From the complex Poisson continuation,

    A-B
      = L * integral phi(u)^2 (cosh(2 delta u)-1) du.

The taper equals one on

    |u| <= L/2-w.

Use the interval

    I_core=[L/2-2w, L/2-w],

which has length w and lies in the flat core once L>=4w.

For delta>0,

    A-B
      >= L*w*(cosh(delta*(L-4w))-1).

For every fixed delta>=delta0>0 and fixed w, this is

    >>_{delta0,w} L * exp(delta L).

Since X=exp(L),

    A-B >> L*X^delta.

The same scale controls A+B from below.

## 4. Tail is negligible relative to the pair eigenvalues

Combining the two estimates gives, uniformly for delta>=delta0>0,

    E_tail/(A-B)
      = O_{delta0,w,profile}(C1^2/T^3).

up to harmless logarithmic factors from h^{-1}. In particular this ratio tends to zero with a power of T.

Therefore the finite evaluation vectors retain asymptotically all of the two-dimensional Gram geometry of the infinite pair.

By finite-rank perturbation/Weyl continuity, the two nonzero eigenvalues of the finite pair block satisfy

    lambda_plus(fin)
      = m(A+B)*(1+o(1)),

    lambda_minus(fin)
      = -m(A-B)*(1+o(1)),

for a target zero of fixed depth delta>=delta0 placed in the interior window.

Thus

    boxed:
    ||Q_pair,fin||_op >= c(delta0,w) * X^delta

for all sufficiently large T.

## 5. Power-law barrier regime is exactly the regime covered

To deduce a fixed zero-free strip from a fourth-moment bound, Proposition R only needs to rule out zeros with

    delta >= 1/(4*lambda)+epsilon,

which is a fixed positive depth. Therefore the fixed-delta0 finite-capture theorem is sufficient for the power-law implication; no uniform estimate as delta->0 is required for that first barrier.

## 6. What remains

This removes **finite truncation of the Gabor grid** as the missing Proposition-R step.

The only serious gap left in our reconstruction is still aggregation:

    one finite deep pair has eigenvalues of size X^delta,

but the full matrix is the sum of that block with all on-line and all other off-line contributions.

We still need a theorem showing that these other contributions cannot cancel every X^delta direction of a maximal-depth pair/cluster.

That is the globalization/isolation lemma.

## 7. Evidence grade

The decay estimate and the finite-grid definitions are source-closed in the public formalization. The complex Poisson continuation and the perturbative pair-spectrum transfer are our analytic write-outs and are not yet Lean-formalized.
