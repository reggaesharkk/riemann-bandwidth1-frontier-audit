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


## 10. Exact Ingham log-budget trade

The deep-rank reduction can be made quantitatively cleaner using Ingham's
classical zero-density estimate

    N(sigma,T)
      << T^[3(1-sigma)/(2-sigma)] (log T)^5.

Set

    sigma = 1/2 + W/log T.

Writing x=W/log T, the exponent satisfies

    3(1/2-x)/(3/2-x)
      = 1 - 2x/(3/2-x).

Hence, uniformly for x=o(1),

    T^[3(1-sigma)/(2-sigma)]
      = T * exp(-(4/3+o(1))W).

Therefore

    rank(B_deep)/d
      << exp(-(4/3+o(1))W) (log T)^4,

up to the harmless dyadic-height enlargement and reflection factor.

Now choose

    W = K log log T

with a fixed constant K>0. Then

    rank(B_deep)/d
      << (log T)^[4-(4/3)K+o(1)],

while every retained near-line off-line weight satisfies

    X^|beta-1/2|
      <= exp(lambda W+o(W))
      = (log T)^[lambda K+o(1)].

Thus for any prescribed rank-error exponent A we can choose K so that

    rank(B_deep)/d << (log T)^(-A),

and the cost of retaining the near-line part is only another **fixed power of
log T**.

This is stronger and cleaner than taking W=sqrt(log log T): both the discarded
rank and the retained amplification can now be entered in one ordinary
log-power ledger.

The trade is exact at the exponent level:

    deep-rank saving exponent  ~ (4/3)K-4,
    near-line amplification    ~ lambda K.

Any proposed bounded-functional-calculus prime-side estimate must beat the
second quantity while the rank-stability argument consumes the first.

## 11. Consequence for the theorem architecture

This does not compute the bounded spectral observable. It does show that
classical zero density is already sufficient to move every power-of-T
off-line obstruction into an arbitrarily small rank fraction while leaving
only polylogarithmic amplification in the retained bulk.

Accordingly, a successful resolvent/sign-proxy estimate with arbitrary
logarithmic saving would evade Proposition R without any EC-star close-pair
input.


## 12. Exact simple-zero consumer

The bounded-spectral route now has an exact zero-side consumer.

If nplus is the positive index of the active normalized block, then the source-closed inequalities

    nplus <= s1+s2+p,
    s1+2s2+2p <= N(I')

give immediately

    boxed:
    s1 >= 2*nplus - N(I').

Thus one does **not** need to recover simple zeros indirectly from distinct-zero proportions.

For the bounded minorant

    f_{theta,y}(x)=(2/pi) arctan((x-theta)/y),

we have pointwise

    1_{x>theta} >= f_{theta,y}(x),

so

    nplusAbove_theta(H) >= tr f_{theta,y}(H).

Combining with the existing tail-Weyl transfer gives a direct sufficient target:

    (1/N) tr f_{theta_tail,y}(Ghat) > 0.895+eta

for some eta>0 implies a simple-zero proportion strictly above 79 percent.

Likewise a bound above 0.9+eta gives a simple-zero proportion above 80 percent.

See `WP84_BOUNDED_RESOLVENT_CONSUMER.md`.

This is the precise nonlinear prime-side kill gate.
