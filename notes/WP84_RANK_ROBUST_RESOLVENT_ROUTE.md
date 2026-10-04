# WP84 — rank-robust spectral route around the Proposition-R obstruction

Date: 2026-10-04
Status: **NEW THEOREM ARCHITECTURE; rank/zero-density reduction closed in shape, prime-side regularized spectral law open**

The Proposition-R obstruction attacks raw higher even moments because a vanishing fraction of deep off-line zeros can create polynomially large eigenvalues and dominate every high Schatten moment.  But the zero-counting objective is an **inertia/proportion** statistic, which is stable under low-rank perturbations.

This suggests replacing raw higher moments by a bounded, rank-robust spectral observable.

## 1. Deep off-line zeros form a negligible-rank perturbation

Let

    H = G_tilde / ell1

be the normalized compressed Weil matrix, and fix a depth threshold

    eta_T = W(T)/log T

with W(T)->infinity slowly.

Split the zero-side active-window matrix as

    H = H_near + B_deep + E_tail,

where B_deep contains zero pairs with

    |beta-1/2| > eta_T.

A classical zero-density estimate has the form

    N(1/2 + W/log T, 3T)
      << exp(-c W) T log T

for some absolute c>0 (indeed stronger constants are known). By functional-equation symmetry the same bound holds on the left side.

Each off-line pair contributes rank at most two. Therefore

    rank(B_deep)
      << exp(-c W) T log T.

Since

    d = T L/(2*pi) + O(1) asymp T log T,

we obtain

    boxed:
    rank(B_deep)/d << exp(-c W) -> 0.

Thus deep off-line zeros are asymptotically invisible to every rank-stable spectral proportion.

## 2. Exact rank inequality for inertia and empirical spectra

For Hermitian A and B with

    rank(A-B) <= r,

Cauchy interlacing gives, for every threshold x,

    | #{lambda_i(A)<=x} - #{lambda_i(B)<=x} | <= r.

In particular

    boxed:
    | n_+(A) - n_+(B) | <= r.

So removing B_deep changes the positive-index proportion by o(1).

More generally, the empirical spectral distribution functions obey

    sup_x |F_A(x)-F_B(x)| <= r/d.

Consequently every bounded monotone spectral observable is stable at the same scale.

## 3. Resolvent stability

For z=E+i y with y>0, integration by parts against the rank inequality gives

    |m_A(z)-m_B(z)|
      <= (r/d) integral_R dx / ((x-E)^2+y^2)
      = pi*r/(d*y),

where

    m_A(z)=(1/d) tr (A-zI)^(-1).

Hence for fixed y>0, deleting all deep off-line zeros changes the normalized resolvent by o(1).

This is the exact robustness property raw moments lack.

## 4. The remaining near-line zeros do not have power-law amplification

For

    |beta-1/2| <= W/log T,

and bandwidth X=T^(lambda+o(1)), the off-line exponential factor is at most

    X^|beta-1/2| <= exp(lambda W+o(W)).

Choose, for example,

    W=(log log T)^(1/2).

Then

    exp(lambda W)=(log T)^o(1),

while the discarded rank fraction is

    exp(-c sqrt(log log T))=o(1).

So after the negligible-rank deletion, all off-line amplification is only sub-polynomial in log T rather than a power of T.

This is precisely the regime in which arbitrary log-power savings from Siegel--Walfisz/MRT-type inputs could in principle absorb the zero-side growth.

## 5. A sign-preserving bounded consumer

Raw x^(2m) is the wrong observable: it magnifies a few outliers and triggers Proposition R.

A natural replacement is a bounded sign proxy, for example

    s_y(x) = 1/2 + (1/pi) arctan(x/y),

or equivalently a Cauchy/Poisson integral of the resolvent.

It satisfies

    0 < s_y(x) < 1,

    s_y(x) -> 1_{x>0}

away from an O(y) neighborhood of zero.

Because s_y is bounded and monotone, a rank-r perturbation changes

    (1/d) tr s_y(H)

by at most r/d.

Thus deep off-line zeros cannot spoil this statistic.

## 6. Why this route evades Proposition R

A bounded spectral statistic cannot detect the polynomial magnitude of a fixed number of deep outliers.  Therefore a theorem controlling it does **not** automatically imply a power-law zero-free region.

This is the correct semantic match to the target statement: a proportion theorem is allowed to ignore o(N) exceptional zeros.

Proposition R is therefore a barrier to the **raw higher-even-moment architecture**, not automatically to every spectral route beyond 2/3.

## 7. New prime-side kill gate

The unresolved step is now sharply different from G9:

    prove a prime-side limit/control for the normalized resolvent
    m_H(E+i y)

or for an equivalent bounded sign proxy, without expanding it into a finite raw higher-even-moment tower.

Possible routes to audit:

1. a Gabor/Toeplitz operator limit for bounded continuous functional calculus;
2. a direct resolvent identity on the prime-side compressed operator;
3. a low-rank-stable spectral-distribution theorem (Szego-type rather than moment-type);
4. a rational approximation whose poles stay a fixed distance off the real axis and whose trace can be controlled directly.

Any route that first proves finite raw fourth/eighth moments of H has fallen back into the Proposition-R barrier and is rejected.

## 8. Relation to the exact model track

The C7, {5,2}, Christoffel and exact connected/polytope calculations remain useful as a model fingerprint: they predict the limiting bulk spectral law and can validate any proposed resolvent equation.

But they are no longer the theorem-side transport mechanism by themselves.

## 9. Claim boundary

This note does **not** prove a new >79% theorem. It establishes a viable architecture that is logically compatible with classical zero-density information and is not ruled out by Proposition R.

The next target is to derive or falsify the bounded functional-calculus / resolvent limit for the actual compressed Weil matrix.
