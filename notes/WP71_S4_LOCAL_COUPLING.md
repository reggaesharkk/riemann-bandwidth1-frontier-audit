# WP71 — exact p-local coupling for S4(k,j)

Date: 2026-10-04
Status: **POINTWISE LOCAL COUPLING AND BOTH MARGINALS CLOSED EXACTLY**

This audit asks whether the centered four-point main `S4(k,j)V(k,j)` has extra arithmetic couplings between the lock j and the shift k.

The answer is: **yes pointwise, and exactly in a controlled way**. Those cross-constraints disappear only after the correct marginal average. Therefore a naive pointwise replacement by a product of two twin singular series would be wrong.

## Local definition

Fix a prime p. Put

    g=gcd(b1,b2), r=b1/g, q=b2/g,
    e1=v_p(b1), e2=v_p(b2), e=min(e1,e2).

For the locked quadruple

    b1*n-b2*m=j,
    m'=m-rk, n'=n-qk,

define K4_p(k,j) by counting solutions modulo p^s with all four variables p-units and normalizing by

    p^s*(1-1/p)^4,

the same unconditioned convention used by the public two-point kappa_p table.

## Equal p-valuations

When e1=e2=e and p^e divides j, strip the common p^e and the p-free common factor. Modulo p the four forbidden residues of the free variable are, after a unit normalization,

    {0, -r*k, d, d-r*k},

where d is a unit multiple of j/p^e.

If D is the number of distinct residues in that set, then

    K4_p(k,j) = p^e * (1-D/p)/(1-1/p)^4.

If p^e does not divide j, the factor is zero.

For p not dividing b1*b2, the possible extra coincidences occur on

    p|k,
    p|j,
    p|(j-lcm(b1,b2)k),
    p|(j+lcm(b1,b2)k).

So the true pointwise four-point local factor contains genuine j-k cross constraints.

## Unequal p-valuations

If e1>e2, then after stripping p^e the lock fixes m modulo p, r is p-divisible and q is a unit. A nonzero factor requires v_p(j)=e, and the remaining free n-variable contributes the ordinary twin local factor for n and n-qk.

The case e2>e1 is symmetric.

## Exact j-marginal

For every p,b1,b2,k, averaging K4_p over one complete local j-period gives

    E_j K4_p(k,j) = tau_p(rk) tau_p(qk).

This is the exact local origin of the k-side product of twin singular series.

## Exact k-marginal

For fixed j, averaging over k modulo p gives

    E_k K4_p(k,j)
      = kappa_p(e1,e2;v_p(j))^2 / p^e.

Equivalently, after averaging over j,

    E_j[kappa_p(j)^2]
      = p^e E_k[tau_p(rk)tau_p(qk)],

which is exactly the local identity already used in the G9-B Euler-factor calibration.

Thus the squared lock model in the j-frame and the twin-product model in the k-frame are the two marginals of one exact local coupling.

## Consequence for G9-C

The correct pointwise main is an Euler product of K4_p(k,j)-type local factors. It must not be replaced pointwise by `S(rk)S(qk)`. That product is obtained only after j-averaging.

This resolves the main local-arithmetic concern in the j-first pivot: the cross-modulus constraints are real, explicit, and already encoded by the four-point local coupling rather than representing an unknown extra obstruction.

Companion exact checker:

`src/wp71_s4_local_coupling_exact.py`

It uses only `fractions.Fraction`, compares the formula with direct modular counts on representative prime-power cells, and verifies both marginal identities with zero tolerance.

## Evidence boundary

This closes the p-local arithmetic structure of S4(k,j). It does not prove the global four-point variance theorem.

The next open layers are:

1. assemble the truncated Euler/CRT comb from these local couplings;
2. match that comb to the doubly-major spectral main in identical conventions;
3. independently prove the mixed/minor spectral L2 budget;
4. carry the centered error through the Stage-A R-unit normalization.
