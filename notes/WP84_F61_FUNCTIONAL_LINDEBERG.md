# WP84 — direct functional Lindeberg calculus for the bounded consumer

Date: 2026-10-05

Status: **SIX-POLE SUM COLLAPSED TO ONE TRACE GRADIENT/HESSIAN FUNCTIONAL; ARITHMETIC TRANSITION-MEASURE CLOSURE OPEN**

The active consumer is

    f(x)=F_61(x)=62 P(x)^2/(P(x)^2+61).

It is useful to keep its six-pole representation for robust resolvent bounds,
but the first and second Lindeberg terms can be rewritten intrinsically in
terms of f.  This removes unnecessary pole-by-pole bookkeeping from the
operator calculation.

## 1. One-block expansion

Write

    f(x)=62 + sum_j c_j/(x-z_j),

and for Hermitian A put

    R_j=(A-z_j I)^(-1).

For a Hermitian increment B,

    tau[f(A+B)-f(A)]
      = - sum_j c_j tau(R_j B R_j)
        + sum_j c_j tau(R_j B R_j B R_j)
        + E_f(A,B).

Because every pole satisfies |Im z_j|>1,

    |E_f(A,B)|
      <= C_3 ||B||^3,

where the fixed consumer constant is

    C_3
      = sum_j |c_j| / |Im z_j|^4
      < infinity.

Thus the accumulated remainder is

    O(C_3 sum_n ||B_n||^3)
      = O(L^-3).

No contour derivative and no raw moment enters.

## 2. First-order trace collapses exactly

Trace cyclicity gives

    - sum_j c_j tau(R_j B R_j)
      = - sum_j c_j tau(B R_j^2).

But

    f'(x)
      = - sum_j c_j/(x-z_j)^2.

Hence

    boxed:
    D_1(A;B)
      = tau(f'(A) B).

This is the exact first-order functional Lindeberg term.

For the permutation process, the conditional first-order contribution is

    tau(f'(A_S) M_1(S)),

where M_1(S) is the average remaining prime block.

This is the correct drift object.  Proving it small may not assume that
f'(A_S) is a multiplication operator.

## 3. Second-order trace is a divided-difference quadratic form

Diagonalize

    A u_p=lambda_p u_p.

For one pole,

    tau(R B R B R)
      = d^(-1) sum_{p,q}
          |B_{pq}|^2
          (lambda_p-z)^(-2)(lambda_q-z)^(-1).

Symmetrizing p and q gives the exact real functional kernel

    K_f(x,y)
      = 1/2 * (f'(x)-f'(y))/(x-y),

with diagonal value

    K_f(x,x)=f''(x)/2.

Therefore

    boxed:
    D_2(A;B)
      = d^(-1) sum_{p,q}
          |B_{pq}|^2 K_f(lambda_p,lambda_q).

Equivalently D_2 is one half of the trace Hessian

    D_2(A;B)
      = (1/2) D^2[tau f(A)][B,B].

This is exact for arbitrary Hermitian A and B; no commutation is assumed.

## 4. Positive transition-measure formulation

For fixed A and a family of remaining blocks define the positive bivariate
measure

    Gamma_A
      = d^(-1) average_B
          sum_{p,q}
            |B_{pq}|^2
            delta_(lambda_p,lambda_q).

Then the conditional second-order term is simply

    boxed:
    integral K_f(x,y) dGamma_A(x,y).

So the active bounded theorem no longer needs an operator-valued variance map
as an abstract object if one can identify the corresponding **spectral
transition measure** Gamma_A.

This is a genuine reduction:

- Gamma_A is positive;
- its total mass is
      d^(-1) average_B tr(B^2);
- the noncommutative information survives in where that mass sits in
  (x,y), rather than being collapsed to one scalar covariance.

## 5. Why scalar covariance failed

Replacing Gamma_A by a product/diagonal surrogate that remembers only its
total mass erases the distinction between adjacent and alternating translation
words.

At order four that loses

    t_opp=1/30

and produces the rejected centered value 7/30.

Therefore the theorem must identify enough of Gamma_A to preserve the
crossing class and the connected state dependence.

## 6. Uniform deterministic bounds

By the mean-value theorem,

    |K_f(x,y)|
      <= (1/2) sup_R |f''|.

For F_61 the real-line derivatives are bounded because f is a fixed rational
function with no real poles.

This gives a crude square-mass domination

    |D_2(A;B)|
      <= (1/2) ||f''||_infinity * tau(B^2).

Likewise

    |D_1(A;B)|
      <= ||f'||_infinity * tau(|B|)

when a trace-norm estimate is available.

These bounds are not sharp enough by themselves to prove the target, but they
give theorem-grade domination for truncation and approximation arguments.

## 7. New theorem interface

For the permutation-averaged path, the six-pole inequality can be written as

    tau f(H)-tau f(S)
      = E_pi sum_k [
          tau(f'(A_{k-1}) B_{pi(k)})
          + integral K_f dGamma_{A_{k-1},B_{pi(k)}}
        ]
        + o(1).

After conditioning on the inserted subset this becomes

    drift:
        tau(f'(A_S) M_1(S)),

    Hessian/variance:
        integral K_f dGamma_S.

This is narrower and more invariant than six separate A1/A2 equations.

## 8. Immediate attack target

Prove a continuum/translation-algebra limit for the two bounded quantities

    tau(f'(A_S) M_1(S))

and

    integral K_f dGamma_S

uniformly in the subset fraction, with the full word geometry retained.

The order-four crossing/connected gate remains the fail-closed calibration of
that transition-measure law.

No unconditional >79 theorem is claimed.
