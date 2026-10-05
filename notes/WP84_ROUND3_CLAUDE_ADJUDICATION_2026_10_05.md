# WP84 — fresh-Claude round-3 adjudication

Date: 2026-10-05

Status: **GOOGLE'S HANKEL/M7 OBJECTION REJECTED; ASYMPTOTIC PORTMANTEAU ROUTE CONFIRMED; HOPF TRANSFER LIMITED TO PROOF ARCHITECTURE; NEXT GATE IS THE FULL OPERATOR-VALUED SECOND-ORDER GENERATOR**

A fresh Claude account audited Google's round-3 response from a self-contained
state packet.  The useful conclusions are recorded here with two corrections
to Claude's own wording.

## 1. Exact Hankel/Christoffel facts

For the pinned moments m0..m6, let

    H=(m_{i+j})_{0<=i,j<=3}.

Exact arithmetic gives

    det H = 283/108864 > 0

and

    K(0,0)=e0^T H^{-1}e0 = 13891/1415.

Therefore the Christoffel function at zero is the reciprocal

    lambda(0)=1/K(0,0)=1415/13891.

The exact degree-3 minimizer normalized by P(0)=1 is

    P(x)
      = 1
        - (43428/13891)x
        + (37704/13891)x^2
        - (9660/13891)x^3.

For **every** positive Borel measure on R with the pinned moments,

    integral P(x)^2 dnu = 1415/13891

exactly.

This is stronger/more precise than the fresh-Claude sentence
"integral g dnu >= reciprocal": because P is the exact Christoffel minimizer
determined by H and all moments through degree six are pinned, the displayed
integral is an equality for every representing measure.

## 2. One-line half-line sign certificate

Write

    P(x)-1=x Q(x),

where

    Q(x)
      = -(43428 - 37704 x + 9660 x^2)/13891.

For x<=0 the polynomial in parentheses is strictly positive, hence Q(x)<0.
Therefore x Q(x)>=0 and

    P(x)>=1,
    P(x)^2>=1

on the whole nonpositive half-line.

Thus

    nu((-infinity,0])
      <= 1415/13891,

and

    nu((0,infinity))
      >= 12476/13891.

This is a genuine example of the reusable proof pattern from the user's Hopf
work: exact elimination to a rational expression followed by a same-sign
coefficient certificate.  It is not a transfer of Hopf bifurcation theory.

Companion exact checker:

    src/wp84_round3_hankel_christoffel_audit.py

## 3. Google's shifted-Hankel/m7 falsifier is malformed

Google displayed

    det (m_{i+j+1})_{0<=i,j<=2}

while saying a future m7 was needed.

That determinant uses only m1..m5 and is already exactly

    23/1296 > 0.

No m7 enters it.

More fundamentally, positivity of shifted Hankel matrices is a Stieltjes
support condition connected with support on [0,infinity).  WP84's half-line
certificate requires no such support condition.  A nonpositive shifted minor
would not imply "negative weights" for a positive measure on R; it would only
obstruct an all-nonnegative-support representation.

The relevant Hamburger moment matrix H above is positive definite.

## 4. Qualitative weak convergence is enough for the stated theorem

The target is asymptotic, not an effective finite-height theorem.

If

    nu_T => nu_*

and theta_T->0, then for every epsilon>0,

    liminf nu_T((theta_T,infinity))
      >= nu_*((epsilon,infinity)).

Sending epsilon down to zero gives

    liminf nu_T((theta_T,infinity))
      >= nu_*((0,infinity)).

Therefore no explicit convergence rate is mathematically required for the
asymptotic liminf statement.  A rate would only be needed for an effective T0
or a numerical finite-height certification.

Google's objection on this point is rejected.

## 5. Contour issue clarified

For rho<1 the disk |z-i|<=rho lies entirely in the upper half-plane.  The
Stieltjes transform of a Hermitian spectral measure is analytic there because
all poles lie on the real axis.

Therefore a Cauchy argument inside that disk is not illegal because of hidden
eigenvalue poles.

Whether a proposed L1 contour formula has the correct numerical constant is a
separate algebraic question.  In the current shortest route it is no longer
central because the beta consumers have been demoted.

## 6. Hopf transfer: limited but real at the proof-architecture level

There is no literal Hopf-bifurcation theorem to import into WP84.

A spectral-flow homotopy

    H(s)=H_model+s(H_arith-H_model)

does not currently shorten the problem:

- the crossing derivative <v,H'(s)v> has no fixed sign;
- zero crossings can be highly degenerate;
- there is no finite-dimensional parameter elimination analogous to the
  3-variable ODE;
- the relevant translation-word state dimension grows rather than collapsing
  to a finite center manifold.

A Fredholm/Birman--Schwinger recasting would need uniform compactness or
trace-class control that has not been established.

So the Hopf theorem's **method** is transferable:

    exact boundary / identity
      -> eliminate nuisance variables
      -> reduce to sign
      -> exact positive-coefficient certificate,

but the ODE theorem itself is not.

The half-line P(x)^2 certificate is already a successful instance of that
method.

## 7. Fresh Claude's "cubic-budget dichotomy" needs one correction

The exact Lindeberg identity gives

    total cubic remainder
      <= eta^{-4} sum_j ||B_j||^3
      = o(1).

Hence the limiting resolvent, if the first/second conditional operators
converge, is governed by those operators.

However, if a proposed closure returns centered m4=7/30 rather than 1/4,
that does **not** falsify the exact Lindeberg expansion.  It falsifies the
proposed closure or the proposed target law.

The correct finite consistency gate is:

> derive the fourth-order coefficient from the **full operator-valued**
> conditional drift/variance generator, without scalarizing the state.

Required output:

    centered m4 = 1/4.

The known scalar multiplication/covariance reduction returns only

    7/30

and is already rejected.

If the full operator-valued generator still returns 7/30, then the hoped-for
six-moment limit law is not the limit of that generator.

## 8. The next theorem gate

Before attempting m5/m6 at finite height, prove the following order-4
consistency statement.

**Operator-generator m4 gate.**

Take the exact permutation-averaged first/second-order resolvent dynamics of
the retained prime blocks, retain the full truncated-translation state, and
derive the order-four centered coefficient of its candidate limiting law.

It must reproduce

    1/4
      = 2*(7/60) + (1/30 - 1/60).

Equivalently the generator must retain the crossing/connected correction

    1/60

missing from the scalar covariance closure.

Possible outcomes:

1. **PASS:** full operator-valued generator gives 1/4.
   Continue to m5/m6 and full resolvent convergence.

2. **FAIL:** exact full generator gives 7/30 or another value.
   The current target law is wrong for this route.

3. **ARITHMETIC DEPENDENCE:** the coefficient cannot be evaluated without a
   new prime-correlation input.
   Then that input is the exact theorem debt.

This gate is theorem-relevant and finite.  Google's proposed finite-height raw
m5/m6 sampler is only diagnostic and should not replace it.

## 9. A useful analytic simplification

To identify a unique limiting Stieltjes transform it is not necessary to prove
convergence uniformly on an entire contour at the start.

Because normalized Stieltjes transforms form a normal family on C_+, it is
enough to prove convergence at a sequence of fixed nonreal points with an
accumulation point inside C_+, for example

    z_n=i(1+1/n), n>=1.

Every subsequential analytic limit then agrees on a set with an interior
accumulation point, so the identity theorem gives uniqueness; normal-family
compactness upgrades this to local-uniform convergence.

This can reduce the arithmetic comparison target from a continuum of z-values
to countably many fixed resolvent points.

## 10. Evidence boundary

No unconditional >79 theorem is claimed.

Current exact status:

- degree-6 half-line consumer: closed;
- low-rank weak/Stieltjes stability: closed;
- single-block cubic remainder: closed;
- scalar covariance closure: falsified;
- finite F/G closure: falsified;
- full operator-valued generator m4 consistency: OPEN;
- arithmetic-to-model Stieltjes convergence: OPEN.
