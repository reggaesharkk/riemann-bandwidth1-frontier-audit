# WP83 — complex Poisson continuation and isolated-pair spectrum

Date: 2026-10-04
Status: **COMPLEX CONTINUATION CLOSED IN WRITE-OUT; INFINITE-GRID ISOLATED-PAIR SPECTRUM CLOSED; FINITE COMPRESSION/GLOBAL ISOLATION OPEN**

The public Lean package proves the Poisson--Gabor identity only for real arguments, but it also proves the exact all-complex decay estimate needed to extend it.

## 1. Inputs already source-closed

For the C^3 compactly supported taper phi, the public formalization proves for every complex z

    |phihat(z)| * |z|^2
      <= exp(|Im z| L/2) * C1,

with C1=||phi''||_1.

It also proves for all real x,y

    sum_{k in Z} phihat(x-alpha_k) phihat(y-alpha_k)
      = L * Phi(x-y),

where Phi=widehat(phi^2).

## 2. Normal convergence on compact subsets of C^2

Fix a compact K subset C^2. Then |Im z| and |Im z'| are bounded on K.

For |k| large,

    |z-alpha_k| >= c_K(1+|k|),
    |z'-alpha_k| >= c_K(1+|k|),

because alpha_k=T+2*pi*k/L is affine in k.

The all-complex decay therefore gives, uniformly on K,

    |phihat(z-alpha_k) phihat(z'-alpha_k)|
      <= C_K (1+|k|)^(-4).

The Weierstrass M-test gives normal convergence of

    F(z,z')
      := sum_k phihat(z-alpha_k) phihat(z'-alpha_k).

Hence F is jointly holomorphic (equivalently, separately holomorphic with local uniform convergence).

The function

    G(z,z'):=L*Phi(z-z')

is entire because phi^2 has compact support.

## 3. Sequential identity-theorem continuation

Fix a real y. The function

    z -> F(z,y)-G(z,y)

is entire and vanishes for every real z by the already-proved real Poisson identity. Since the real line has accumulation points in C, the one-variable identity theorem gives

    F(z,y)=G(z,y)

for every complex z and every real y.

Now fix any complex z. The function

    z' -> F(z,z')-G(z,z')

is entire and vanishes for every real z' by the previous paragraph. A second application of the identity theorem gives

    boxed:
    sum_k phihat(z-alpha_k) phihat(z'-alpha_k)
      = L*Phi(z-z')

for all complex z,z'.

No several-complex-variables uniqueness theorem is required.

## 4. Exact isolated off-line pair Gram data

Take an off-line zero coordinate

    z=gamma-i*delta,
    zbar=gamma+i*delta,

with delta!=0, and let

    u_k=phihat(z-alpha_k).

Since phi is real,

    phihat(zbar-alpha_k)=conj(u_k).

Put

    A=L*Phi(2 i delta),
    B=L*Phi(0).

Using the complex Poisson identity:

    sum_k |u_k|^2 = A,
    sum_k u_k^2   = B.

Write

    u=x+i y

with real vectors x,y. Since B is real,

    x dot y=0.

Also

    ||x||^2+||y||^2=A,
    ||x||^2-||y||^2=B.

Therefore

    ||x||^2=(A+B)/2,
    ||y||^2=(A-B)/2.

The paired zero contribution is exactly

    Q_pair=2m (x x^T - y y^T).

Because x is orthogonal to y, its only nonzero eigenvalues are

    boxed:
    lambda_plus =  m(A+B),
    lambda_minus = -m(A-B).

## 5. Strict nondegeneracy off the line

Because phi is even and real,

    Phi(2 i delta)
      = integral phi(u)^2 cosh(2 delta u) du.

Thus

    A-B
      = L * integral phi(u)^2 (cosh(2 delta u)-1) du.

For delta!=0 and a nonzero window with support away from the single point u=0, this is strictly positive.

Hence every isolated infinite-grid off-line pair has exact signature (1,1), rank two, and a quantitatively nonzero negative direction.

## 6. Exponential scale

The taper equals 1 on the flat core

    |u| <= L/2-w.

For delta>0, any fixed positive-length subinterval near the right end of that core gives

    A >= c * exp(delta*(L-O(w)))

with c depending only on the chosen subinterval width.

When w=o(L), the pair eigenvalue scale is therefore

    exp(delta L+o(L)) = X^(delta+o(1))

under L=lambda log X.

This is the precise local amplification needed in Proposition R.

## 7. What remains

This closes only the **infinite-lattice isolated-pair** calculation.

The consumed matrix uses the finite grid k=0,...,d-1. Two further gates remain:

1. finite-grid capture: place the target zero inside a suitable height window and show the omitted lattice tails are negligible relative to A-B;
2. globalization: prove that the target pair or a maximal-depth cluster retains a quantitative component outside the span of all competing zero evaluations.

Only the second gate prevents cancellation between distinct off-line pairs.

## 8. Source-status correction

The complex identity is not currently theorem-checked in the public Lean package. Its real restriction and the all-complex decay estimate are theorem-checked there; the continuation above is our independent analytic write-out.

Until independently formalized or externally checked, grade this gate as **proved write-out / not machine-formalized**.
