# WP84 resolvent kill gate -- 2026-10-05

Status: **RESET AFTER DUAL HOSTILE AUDIT — RADAU b3/b10 VALUES ARE SURROGATE RECONNAISSANCE, NOT CERTIFIED TARGET-LAW MARGINS**

## Surviving exact structure

1. The bounded beta family remains a valid pointwise positive-index minorant family.
2. The Laurent/Cauchy fixed-circle transfer constants are algebraically correct.
3. The exact one-block resolvent identity and the deterministic cubic remainder bound survive.
4. The prime-block cube mass gives a uniform fixed-circle o(1) cubic debt if the recorded O(L^-3) estimate is used.
5. The covariance-only scalar closure is false: it gives centered m4=7/30 instead of 1/4.
6. Non-cyclic partial translations reproduce the exact overlap rule
       (1-spread(partial walk))_+.
7. The Laplace resolvent-to-unitary-flow representation and Duhamel signs/remainders survive.
8. A finite F/G state does not close; repeated evolution generates a word hierarchy.

## Major correction: no active b3 numerical margin

The values

    q3 ~= 0.8964412949,
    q10 ~= 0.8981347675

come from evaluation on one specific Radau representing measure.

They are not lower bounds over all measures with the pinned moments m0..m6.

An exact positive rational seven-atom measure matching those moments has

    E[b3] ~= 0.890363090084 < 0.895.

See:

    src/wp84_b3_radau_surrogate_falsifier.py
    notes/WP84_EXTERNAL_AUDIT_RECONCILIATION_2026_10_05.md

Therefore the previously quoted b3 circle target 3.59e-5 is **not an active theorem error budget**. It is only the transfer tolerance relative to the Radau surrogate if that surrogate were independently proved to be the actual limiting law.

## Rejected audit objections

No resolvent 'outlier exclusion' or high-probability delocalization lemma is needed merely to sum the Lindeberg cubic remainder: every intermediate matrix is Hermitian and

    ||(H-zI)^(-1)|| <= 1/|Im z|

deterministically.

Also, the missing fourth-order 1/60 is not assigned a priori to the V-sum branch. The final closure must reproduce it, but it may arise from repeated word geometry across the full translation algebra.

## Current theorem gate

The clean surviving target is now a **positive-limit resolvent theorem**:

Prove that the empirical spectral measures nu_T have Stieltjes transforms converging locally uniformly in C_+ to a probability law nu_* whose first six model moments are the pinned values.

No support restriction is required.  The exact degree-6 square polynomial

    g(x)=P(x)^2,

with P the Christoffel cubic, satisfies g(x)>=1 for every x<=0 and

    int g dnu_* = 1415/13891.

Therefore

    nu_*((0,infinity)) >= 12476/13891.

Weak convergence and Portmanteau then give the asymptotic positive-index bound, and the exact zero-side counting ledger gives

    simple proportion >= 11061/13891
      = 0.7962709668... > 0.79.

Support positivity is NOT a theorem obligation: the moment-only half-line certificate works for arbitrary positive Borel measures on R.  The genuine obligation is to identify the limiting law and its pinned moments without reverting to raw finite-T higher-moment estimates.

## Active analytic technologies

Either of the following may prove the positive-limit theorem:

A. direct compressed-translation / finite Wiener-Hopf resolvent convergence;
B. bounded-time unitary-flow convergence followed by Laplace transform.

Any candidate must:

- derive the target law rather than insert the Radau quadrature;
- reproduce the known order-4, order-5 and order-6 overlap/connected anchors;
- preserve Proposition-R safety;
- include the actual arithmetic prime-block interface.

No unconditional >79 claim is promoted.
