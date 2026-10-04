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
