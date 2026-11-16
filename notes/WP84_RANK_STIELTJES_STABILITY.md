# WP84 — rank-stability of the Stieltjes/weak-limit route

Date: 2026-10-05

Status: **EXACT LOW-RANK STABILITY CLOSED; DEEP-ZERO o(d)-RANK DELETION CANNOT CHANGE THE LIMITING SPECTRAL LAW**

This note supplies the deterministic bridge needed by the round-2 limiting-law route.

## 1. Rank inequality for empirical spectral distributions

Let A,B be d x d Hermitian matrices and suppose

    rank(A-B) <= r.

By the standard Hermitian rank/interlacing inequality, their empirical distribution functions F_A,F_B satisfy

    sup_x |F_A(x)-F_B(x)| <= r/d.

No norm bound on A-B is required.

## 2. Stieltjes-transform consequence

For z=E+i eta with eta>0, put

    m_A(z)=d^{-1} tr (A-zI)^(-1)
          = integral (x-z)^(-1) dmu_A(x).

Integration by parts against F_A-F_B gives

    m_A(z)-m_B(z)
      = - integral (F_A(x)-F_B(x)) d[(x-z)^(-1)].

Hence

    |m_A(z)-m_B(z)|
      <= (r/d) integral_R dx / |x-z|^2
      = pi r/(d eta).

Therefore

    boxed:
    |m_A(z)-m_B(z)|
      <= pi * rank(A-B)/(d Im z).

Uniformly on any compact K subset C_+ with Im z>=eta0>0,

    sup_{z in K}|m_A(z)-m_B(z)|
      <= pi r/(d eta0).

Thus an o(d)-rank perturbation is invisible to the limiting Stieltjes transform on every fixed nonreal compact set, even if its eigenvalues are arbitrarily large.

## 3. Weak-limit consequence

The same rank inequality shows that if r/d->0, then A and B have the same weak subsequential spectral limits.

This is exactly the mode needed for the deep-zero deletion:

- power-law-amplified deep zeros may create enormous eigenvalues;
- if their contribution is confined to o(d) rank, they disappear from the empirical weak limit;
- they may still destroy raw higher moments.

That last point is why this route remains logically distinct from the raw fourth/sixth-moment route and can stay Proposition-R safe.

## 4. Moving threshold

Suppose the retained/full empirical laws converge weakly to nu_* and the zero-side threshold theta_T tends to zero.

For every fixed epsilon>0 and all sufficiently large T,

    (epsilon,infinity) subset (theta_T,infinity).

Hence

    liminf mu_T((theta_T,infinity))
      >= liminf mu_T((epsilon,infinity))
      >= nu_*((epsilon,infinity))

by Portmanteau because (epsilon,infinity) is open.

Let epsilon decrease to zero. Continuity from below gives

    boxed:
    liminf mu_T((theta_T,infinity))
      >= nu_*((0,infinity)).

No effective convergence rate is required for the asymptotic theorem.

## 5. Combined interface with the degree-6 certificate

If the limiting law nu_* has the pinned moments through order six, then the moment-only positive-index certificate gives

    nu_*((0,infinity)) >= 12476/13891.

Therefore any full matrix differing from the retained/model matrix by o(d) rank inherits the same asymptotic positive-index lower bound after the vanishing threshold is inserted.

The exact zero-side counting inequality then yields the model headline

    11061/13891 = 0.7962709668...

provided the arithmetic-to-model Stieltjes convergence is proved.

## 6. Remaining theorem debt

Low-rank stability is no longer an open part of WP84.

The unique major debt is now:

    retained arithmetic compressed-translation matrix
       -> limiting Stieltjes law nu_*
       -> identify the pinned first six moments of nu_*.

The moment identities must be properties of the limiting model law, not finite-T raw-moment estimates for the full arithmetic matrix.
