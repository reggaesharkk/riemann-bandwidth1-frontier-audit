# WP84 — external-audit reconciliation and exact b3 surrogate falsifier

Date: 2026-10-05

Status: **MAJOR CORRECTION — THE RADAU b3 VALUE IS NOT A MOMENT-IMPLIED LOWER BOUND; FIXED-CIRCLE ERROR TARGETS ARE NOT YET THEOREM BUDGETS**

Two independent hostile audits were received after the 2026-10-05 WP84 packet.  This note records what survives, what fails, and what the next theorem target actually is.

## 1. Claude's central objection is correct

The displayed values

    q3 = 0.8964412949...
    q10 = 0.8981347675...

were obtained by evaluating b_m on the specific four-node extremal quadrature
(atom at zero plus three positive roots of the Christoffel cubic).

That quadrature matches the pinned moments m0..m6, but **evaluation of a
non-polynomial rational function on one representing measure is not a lower
bound over all representing measures**.

The repository had labelled these numbers 'model reconnaissance', but later
used q3-0.895 as though it were an available theorem margin.  That inference
is invalid.

## 2. Exact rational counterexample for b3

The companion script

    src/wp84_b3_radau_surrogate_falsifier.py

constructs seven positive rational atoms on [0,4] and solves exactly for
positive rational weights matching

    m0=1,
    m1=1,
    m2=4/3,
    m3=2,
    m4=13/4,
    m5=101/18,
    m6=12809/1260.

For that exact representing measure,

    E[b3] = 0.89036309008427...

which is strictly below

    0.895.

Therefore

    boxed:
    moments through m6 do NOT force E[b3] > 0.895.

This is an exact falsifier, not a grid LP or floating-point witness.

## 3. What the conditioning calculation still means

The Laurent/Cauchy calculation itself remains valid as a **transfer
constant**:

    | int b_m d(nu-nu_*) |
      <= C_m(rho) sup_{|z-i|=rho}|s_nu(z)-s_*(z)|,

with the conjugate circle included.

Thus C3(0.9) ~= 40.14 and the old 3.59e-5 figure are algebraically correct
*conditional on already having a certified target law nu_* with
int b3 dnu_* = 0.896441...*.

What fails is the identification of the Radau quadrature with that target
law.

Accordingly:

- b3 is no longer an unconditional theorem target;
- b10 is no longer an unconditional theorem target;
- neither numerical circle tolerance is an active theorem budget until the
  limiting spectral law is identified and its consumer value is certified.

## 4. Google's resolvent-outlier objection is rejected

For every Hermitian intermediate matrix H_k and every nonreal z,

    ||(H_k-zI)^(-1)||op <= 1/|Im z|

deterministically.

No high-probability delocalization or 'outlier exclusion' lemma is required.
On |z-i|=rho<1 the bound is uniformly

    <= 1/(1-rho)

for every permutation and every intermediate matrix.

Therefore the exact summation

    |E_{>=3}(z)|
      <= |Im z|^(-4) sum_j ||B_j||op^3

survives the hostile audit, provided the cube-mass estimate itself is correct.

## 5. Google's attribution of the missing 1/60 to V-sum is not established

The 1/60 deficit proves that a scalar/covariance-only closure is incomplete.
It does **not** identify the entire missing contribution with the same-sign
variance branch V-sum.

Crossing/connected geometry can be generated through repeated evolution in
the full truncated-translation algebra, including interactions of mixed
branches.

Therefore:

    'V-sum must equal the 1/60 correction'

is not consumed.

The fail-closed requirement is only that the final closure reproduce the
known order-4, order-5 and order-6 anchors.

## 6. Claude's Duhamel/Lindeberg audit survives

The following pieces remain sound:

- resolvent one-block identity and cubic remainder;
- deterministic summation of cubic remainders;
- Laplace resolvent representation;
- Duhamel signs and time-ordering;
- normalized-trace cubic remainder t^3 ||B||^3 / 6;
- exact non-cyclic partial-shift overlap identity.

## 7. Finite F/G closure is demoted

The two observables

    F_A(t;s)
    G_A(t,u;s1,s2)

do not form a finite closed hierarchy.

Repeated Duhamel differentiation generates longer translation words.
The exact partial-shift rule shows why this matters: adjacent and crossing
four-letter words can have different normalized traces even when all
two-letter overlap data agree at the covariance level.

Hence the unitary-flow route remains a valid representation, but not a
two-variable closure theorem.

## 8. New shortest theorem interface

The cleanest surviving target is now qualitative, not a preassigned b3
numerical tolerance.

A sufficient theorem has the form:

**Positive-limit resolvent theorem.**

Let nu_T be the empirical spectral measures of the normalized compressed
matrices. Prove local-uniform convergence of their Stieltjes transforms

    s_T(z) -> s_*(z)

on a nonempty open subset of C_+ (equivalently on one contour plus a normal
family argument), where s_* is the Stieltjes transform of a probability
measure nu_* satisfying:

1. nu_* is supported on [0,infinity);
2. its first six moments are the pinned model moments
   1, 1, 4/3, 2, 13/4, 101/18, 12809/1260.

Then the degree-3 Christoffel atom bound gives

    nu_*({0}) <= 1415/13891,

hence

    nu_*((0,infinity)) >= 12476/13891,

and weak convergence plus Portmanteau yields the positive-index lower bound

    liminf nu_T((0,infinity))
      >= 12476/13891.

After the exact zero-side counting conversion this gives

    simple proportion >= 11061/13891
      = 0.7962709668... > 0.79.

This theorem does **not** require that the finite-T measures be supported on
[0,infinity).  The support condition is only on the limiting law and is a
substantive theorem obligation.

## 9. Critical warning about the positive-support hypothesis

The actual compressed Weil matrices can be indefinite.  Therefore support of
nu_* on [0,infinity) must not be assumed from the finite matrices or from the
six moments.

It must come from the identified limiting operator/model itself.

This is the exact point at which the proposed 'simpler Christoffel transfer'
can otherwise become circular.

## 10. Current kill gate

The theorem-side question is no longer

    can we achieve epsilon < 3.59e-5 around the Radau b3 surrogate?

It is

    can we identify the actual limiting spectral law of the
    compressed-translation prime-side operator, prove it is nonnegative,
    and establish qualitative Stieltjes convergence to it?

The fixed-circle and unitary-flow calculations remain candidate technologies
for proving that convergence.  Their target law must be derived, not inserted
from the Radau quadrature.

No >79 theorem is claimed.
