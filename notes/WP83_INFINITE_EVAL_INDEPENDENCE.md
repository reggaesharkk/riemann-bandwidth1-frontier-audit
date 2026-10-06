# WP83 — exact independence of the infinite-grid zero evaluation vectors

Date: 2026-10-04
Status: **INFINITE-GRID EXACT CANCELLATION RULED OUT; FINITE-DIMENSION QUANTITATIVE ISOLATION REMAINS**

This note sharpens the generic matrix counterexample. The arbitrary hyperbolic cancellation example H1+H2=0 is algebraically valid, but it is not automatically realizable by the actual Gabor evaluation vectors.

## 1. Evaluation vectors are Fourier coefficient sequences

For a zero-coordinate z and the critical grid

    alpha_k=T+2*pi*k/L,

the infinite evaluation vector is

    u(z)_k = phihat(z-alpha_k).

By the paper Fourier convention,

    u(z)_k
      = integral_{-L/2}^{L/2}
          phi(t) exp(i(z-T)t) exp(-2*pi*i*k*t/L) dt.

Thus, up to the harmless Fourier-series normalization, u(z) is exactly the full sequence of Fourier coefficients on [-L/2,L/2] of

    f_z(t)=phi(t) exp(i(z-T)t).

## 2. Finite families of distinct evaluation points are linearly independent

Let z_1,...,z_M be distinct complex numbers in the zero strip and suppose

    sum_{j=1}^M c_j u(z_j)=0

as a full two-sided Fourier coefficient sequence.

Then every Fourier coefficient of

    F(t)=phi(t) * sum_j c_j exp(i(z_j-T)t)

vanishes.

Completeness of the Fourier basis on [-L/2,L/2] gives

    F(t)=0

almost everywhere.

The taper equals one on a nonempty open flat core for L>2w, so on that interval

    E(t):=sum_j c_j exp(i z_j t)=0.

E is an entire exponential polynomial. Vanishing on an interval implies E is identically zero.

Distinct exponentials are linearly independent, hence

    c_1=...=c_M=0.

Therefore

    boxed:
    {u(z_j)}_{j=1}^M
    is linearly independent in the infinite Gabor lattice

for every finite set of distinct zero coordinates.

## 3. Exact cancellation of a finite hyperbolic family is impossible on the infinite lattice

Let V have these evaluation vectors as columns and let H be the direct sum of the nonzero hyperbolic coefficient blocks attached to finitely many off-line pairs.

The independence result gives full column rank of V. Therefore

    Q=V H V* = 0

would imply

    H=V^dagger Q (V^dagger)*=0,

a contradiction.

So the exact arbitrary-matrix cancellation example cannot occur in the full infinite Gabor representation of finitely many distinct zeros.

## 4. Why this still does not prove Proposition R

The consumed matrix keeps only

    k=0,...,d-1,

with

    d=floor(LT/(2*pi)).

The active zero window contains about

    N(T,2T) = T*ell1/(2*pi)+O(log T),

while at lambda=1

    d = T*l/(2*pi)+O(1).

Since

    ell1=l+2*log 2-1,

the zero count exceeds d by an O(T) term. Thus the finite compression can contain more distinct zero evaluations than its dimension.

Accordingly, global full-column-rank isolation is not even dimensionally available for the entire finite-window zero family.

## 5. The quantitative obstruction is now precise

The infinite lattice gives exact uniqueness. The finite matrix throws away all frequencies outside one block of d consecutive Fourier coefficients.

Proposition R therefore needs a **finite-section stability theorem** of one of the following forms:

1. one maximal-depth pair/cluster remains at polynomial distance from the span of the other finite-section evaluation vectors;
2. a bounded number of shifted finite sections jointly recover a stable lower frame bound;
3. cancellation in one finite section forces amplification in another section, allowing a multi-window moment argument.

This is strictly sharper than the vague statement 'hyperbolic blocks may cancel'.

## 6. Immediate research direction

The most promising route is now a **multi-window finite-section argument**. The full Fourier coefficient map is injective; therefore persistent cancellation across enough translated blocks of consecutive coefficients is impossible. The task is to quantify how many blocks are needed, and whether the prime-side moment estimate is uniform for those translated Gabor windows.

That question can be attacked without assuming a lower bound on zero spacings.

## Evidence grade

The Fourier-coefficient representation follows directly from the definitions. Fourier completeness and linear independence of distinct exponentials are standard exact arguments. The quantitative finite-section step is open.
