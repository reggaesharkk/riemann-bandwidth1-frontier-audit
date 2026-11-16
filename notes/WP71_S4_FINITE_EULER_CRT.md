# WP71 — finite Euler/CRT assembly of the S4 local coupling

Date: 2026-10-04
Status: **FINITE-PRIME ASSEMBLY AND BOTH GLOBAL MARGINALS CLOSED EXACTLY**

Let P be any finite set of primes and define the truncated four-point singular-series factor

    S4_P(k,j) = product_{p in P} K4_p(k,j),

where K4_p is the exact local coupling from `WP71_S4_LOCAL_COUPLING.md`.

Because every K4_p depends only on the corresponding p-primary residues, the Chinese remainder theorem makes the finite Euler product completely independent across primes.

## j-marginal

Take j over one complete modulus

    M_j = product_{p in P} p^(min(v_p(b1),v_p(b2))+1).

Then CRT and the exact local j-marginal give

    E_{j mod M_j} S4_P(k,j)
      = product_{p in P} tau_p(rk) tau_p(qk).

So the finite four-point comb reduces **exactly** to the finite product of the two twin singular-series factors after j-averaging.

## k-marginal

Take k modulo

    M_k = product_{p in P} p.

Put

    g_P = product_{p in P} p^min(v_p(b1),v_p(b2)).

Then

    E_{k mod M_k} S4_P(k,j)
      = (1/g_P) * product_{p in P} kappa_p(b1,b2;j)^2.

Once P contains every prime dividing gcd(b1,b2), g_P is the full gcd contribution from those special primes.

## Interpretation

This proves the finite arithmetic comb has no additional inter-prime constraint beyond CRT. The nontrivial coupling is **within each prime**, through the j-k coincidence loci already identified. Across different primes the model factors exactly.

This also explains why two apparently different main terms appear in the archive:

- the j-frame sees the squared lock singular series;
- the k/spectral frame sees the product of two twin singular series.

They are exact CRT marginals of the same finite Euler object.

Companion checker: `src/wp71_s4_finite_euler_crt.py`.

## What remains

The arithmetic finite-Euler assembly is now clean. The next nontrivial step is analytic rather than local:

1. identify the finite Euler comb with the major-major spectral comb at the same truncation P*;
2. control the omitted Euler tail;
3. close the mixed/minor spectral size budget.


## Full tau-frame CRT identity

The same-lock marginal is only tau=0 of a stronger exact finite identity.

For finite weighted position sequences define

    A(j)=sum_{b1*n-b2*m=j} a_m b_n

and

    rho(tau)=sum_j A(j) A(j-tau).

Expanding and writing

    u=m'-m,
    w=n'-n

gives

    b2*u - b1*w = tau.

The m and n sums then factor, so exactly

    boxed:
    rho(tau)
      = sum_{b2*u-b1*w=tau} C_m(u) C_n(w),

where C_m,C_n are the two autocorrelations.

Now set

    t=b2*u.

Then

    t == 0 mod b2,
    t == tau mod b1,

and conversely every integer t on that CRT progression gives

    u=t/b2,
    w=(t-tau)/b1.

Thus the support of the public spectral comb is an exact finite Fubini/CRT identity. It is not inferred from finite-height tracking.

### Exact diagonal branches

The two excluded off-diagonal values are structural:

- t=0 iff b1 divides tau. This gives C_m(0) times the n-side pair correlation at shift -tau/b1.
- t=tau iff b2 divides tau. This gives C_n(0) times the m-side pair correlation at shift tau/b2.

These are precisely the two diagonal branches added separately by the public spectral model. They must remain exact; the twin singular series is not used at shift zero.

### Orientation symmetry

Swapping the two outer legs and the two sequences sends tau -> -tau. Therefore

    rho_(b1,b2)(tau) = rho_(b2,b1)(-tau)

in the swapped-window convention. This is the full-profile asymmetry anomaly gate.

## S5 consequence

The finite algebraic CRT support and diagonal decomposition are now closed. Together with the p-local coupling and finite Euler CRT assembly, the exact core of S5 is no longer open.

The remaining S5 debt is analytic:

1. identify the off-diagonal pair-correlation mains with the truncated Euler factors in the identical window/smoothing convention;
2. prove the omitted Euler/singular-series tail;
3. combine this with the independently proved mixed/minor spectral bound.

Finite-height face_dispersion is retained only as a falsifier.
