# WP84 — round-2 adjudication: moment-only positive-index certificate

Date: 2026-10-05

Status: **CLAUDE ROUND-2 CORRECTION VERIFIED EXACTLY — SUPPORT POSITIVITY IS NOT NEEDED; GOOGLE'S OUTLIER OBJECTION REMAINS FALSE; THE ACTIVE BLOCK IS STILL THE SPECTRAL-CLOSURE THEOREM**

## 1. Exact polynomial certificate

Define

    P(x)
      = 1
        - (43428/13891) x
        + (37704/13891) x^2
        - (9660/13891) x^3,

and

    g(x)=P(x)^2.

For the pinned moment vector

    (m0,...,m6)
      = (1,1,4/3,2,13/4,101/18,12809/1260),

exact rational arithmetic gives

    integral g dnu = 1415/13891.

The cubic P has three distinct positive roots:

- discriminant(P)>0, so all roots are real and distinct;
- P(-u) has strictly positive coefficients for u>=0, so P has no nonpositive root.

Since P(0)=1, writing the roots as xi_i>0 gives

    P(x)=product_i (1-x/xi_i).

Therefore for every x<=0 each factor is >=1, so

    g(x)>=1.

Thus for **every positive Borel measure on the whole real line** with the
pinned moments,

    nu((-infty,0])
      <= integral g dnu
      = 1415/13891,

hence

    boxed:
    nu((0,infty))
      >= 12476/13891
      = 0.8981354834....

No support assumption nu subset [0,infinity) is needed.

The exact counting conversion gives

    2*(12476/13891)-1
      = 11061/13891
      = 0.7962709668....

Companion checker:

    src/wp84_moment_only_positive_index_certificate.py

## 2. Relation to the public certificate

This is the one-sided Chebyshev--Markov / Christoffel mechanism already
present in the public higher-moment candidate: a nonnegative degree-6 square
polynomial majorizes the nonpositive half-line and converts the first six
moments into a positive-index count.

The round-2 audit did not discover a new zero-side principle; it correctly
recovered the right certificate and corrected our mistaken support
requirement.

## 3. Important distinction: limit moments versus raw finite-T moments

Applying the degree-6 certificate directly to the finite arithmetic spectral
measure requires control of finite-T moments through order six. That is
precisely the raw higher-moment route and is exposed to the Proposition-R
barrier.

The rank-robust resolvent route remains potentially different:

1. quarantine deep off-line contributions into o(d) rank;
2. prove weak/Stieltjes convergence of the empirical spectral measures to a
   limiting law nu_* using bounded resolvent/unitary observables;
3. identify the first six moments of **the limiting model law** from the
   compressed-translation model itself;
4. apply the polynomial certificate to nu_*;
5. transfer positive-index mass back by weak convergence / rank stability.

Rare power-law outliers may disappear in weak spectral measure while still
destroying raw moments. Therefore this route does not automatically prove or
consume a finite raw sixth-moment bound.

## 4. Moving threshold transfer

The zero-side count uses an eigenvalue threshold theta_T -> 0 rather than
strictly x>0.

If nu_T => nu_* weakly and theta_T->0, then for every fixed epsilon>0 and all
large T,

    nu_T((theta_T,infinity))
      >= nu_T((epsilon,infinity)).

Portmanteau gives

    liminf_T nu_T((epsilon,infinity))
      >= nu_*((epsilon,infinity)).

Let epsilon decrease to zero. By continuity from below,

    boxed:
    liminf_T nu_T((theta_T,infinity))
      >= nu_*((0,infinity)).

Thus qualitative weak convergence is enough for the asymptotic counting
theorem; an effective finite-height rate is not required unless one wants an
effective T0.

This rejects Google's claim that the limit route is invalid merely because it
lacks a quantitative rate.

## 5. Google's resolvent-path objection is still false

Every permutation-Lindeberg intermediate matrix is Hermitian. Hence for
nonreal z,

    ||(H_k-zI)^(-1)||op <= 1/|Im z|

deterministically.

No high-probability eigenvalue-repulsion or delocalization lemma is required
to control the cubic one-block remainders on a fixed nonreal contour.

The only conditional input in that step is the recorded prime-block cube-mass
bound itself.

## 6. Google's 1/60 self-correction is accepted

Google correctly retracts its previous claim that the entire missing 1/60
must live in V_sum.

The final closure must reproduce the 1/60 fourth-order correction, but the
correction can arise through noncommutative crossing geometry in the
carrier-cancelling difference branch and/or repeated full-algebra evolution.

No branch is assigned the entire constant a priori.

## 7. F/G finite closure remains false

The two proposed dynamic observables F and G are not a finite closed state.
Repeated Duhamel evolution generates arbitrary translation words.

The exact partial-shift trace identity provides the natural state descriptor:

    closed word -> (1-spread(partial walk))_+.

Thus the remaining theorem is an operator/word-law closure, not a two-scalar
flow equation.

## 8. What the theorem target is now

The shortest clean target is:

**Rank-robust limiting-law theorem.**

After deleting the deep-zero o(d)-rank sector, prove local-uniform convergence
of the normalized Stieltjes transforms to a probability law nu_* such that
the compressed-translation model gives

    m_k(nu_*) =
      1,1,4/3,2,13/4,101/18,12809/1260
      for k=0,...,6.

No support restriction is required.

Then the exact polynomial certificate gives

    nu_*((0,infinity)) >= 12476/13891,

and the moving-threshold Portmanteau argument plus the exact counting
inequality yields

    liminf simple-zero proportion
      >= 11061/13891
      > 0.79.

## 9. Current blocker

The route is **not proved**.

The blocker is now exactly the spectral-closure statement:

    arithmetic compressed-translation operator
      -> rank-robust Stieltjes/weak limit
      -> model law with the pinned six moments.

The Radau b3/b10 surrogate values and their Cauchy tolerances are no longer
part of the shortest theorem route.

## 10. Verdict after both round-2 audits

- zero-side degree-6 certificate: CLOSED EXACTLY;
- Radau b3 theorem margin: FALSIFIED;
- deterministic nonreal resolvent bound: CLOSED;
- cubic one-block summation: survives conditional on cube-mass input;
- scalar covariance closure: FALSIFIED;
- finite F/G closure: FALSIFIED;
- full translation-word geometry: exact algebra identified;
- arithmetic-to-model limiting-law closure: OPEN.

Therefore:

    ROUTE SURVIVES, BUT IS CURRENTLY BLOCKED AT ONE MAJOR ANALYTIC CLOSURE.
