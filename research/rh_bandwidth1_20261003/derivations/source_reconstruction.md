# Source reconstruction: Alpöge–Furman Theorem A

Source: arXiv:2608.13637v2, §§1–6 and §7.2. This is a source reconstruction and arithmetic replay, not an independent proof of every analytic estimate.

## A. Weil Hermitian form

For compactly supported test functions, define W(f,g) as the zero sum
Σρ mρ f̂(γρ) conjugate(ĝ(overline(γρ))), with γρ=(ρ−1/2)/i. Positivity for all test functions is equivalent to RH; the proof avoids assuming that positivity.

## B. Gabor test family

Choose an even window ψ supported on [-1/2,1/2] and a smooth cutoff χ. Put L=log(T/(2π)), X=e^L=T/(2π), and
φ(u)=χ(L/2+u)χ(L/2−u)√ψ(u/L).
This function is supported in [-L/2,L/2]. Modulate it at αk=T+2πk/L for 0≤k<d, with d=floor(LT/(2π))=N(T,2T)+O(L). The product supports are contained in [-L,L]=[-log X,log X]. The Poisson–Gabor identity gives the frame normalization used below.

## C. Finite compression

For each zero ρ form vρ=(φ̂(γρ−αk))k. Let a=||φ||²/L and normalize by aL²:
G̃=(aL²)^−1 ΣRe γρ∈I′ mρ vρvρᵀ.
Using the Weil explicit formula, the entries are also the prime-side integrals over νX. This is a real symmetric finite matrix after pairing conjugate off-line zeros.

## D–E. On-line block and off-line inertia

P=(aL²)^−1 Σρ on the critical line mρ vρvρᵀ is positive semidefinite. Set Q=G̃−P. An on-line zero contributes a positive rank-one form. Each off-line pair {ρ,1−conjugate(ρ)} contributes a real block of signature (1,1), so its positive index contributes at most one. The truncation tail has negligible trace norm.

## F. Trace data

If s1 is the number of simple on-line zeros, s2 the number of multiple on-line points, and p the number of off-line pairs:
- tr(P)≤N0;
- n₊(Q)≤p;
- N≥s1+2s2+2p;
- tr(G̃)=(1+o(1))N.

The corresponding bound for the simple-on-line sub-block P1 also uses tr(P1)+2n₊(Q′)≤N for Q′=G̃−P1.

## G. Hilbert–Schmidt second moment

The unconditional prime-side calculation gives
||G̃||HS²=(R(ψ)+o(1))N.
For the indicator window R=4/3. For the Montgomery–Taylor window ψMT(s)=cos(√2s) on [-1/2,1/2],
RMT=1/2+(1/√2)cot(1/√2).
The formula requires X≤T. The paper lists Weil's formula, zero counting, Stirling, Chebyshev–Mertens prime sums, and Montgomery–Vaughan for log frequencies. It does not assume RH or a zero-free region.

## H. Rank–trace/inertia inequality

For P1≥0 and Hermitian Q′ with n₊(Q′)≤b:
rank(P1)≥2tr(P1)+4tr(Q′)−4b−||P1+Q′||HS².
Use P1 as the simple-on-line part and Q′=G̃−P1 to obtain
N0s+o(N) ≥ rank(P1) ≥ 4tr(G̃)−2N−||G̃||HS²
=(2−R(ψ)−o(1))N.

## I–J. Window functional and optimization

The one-window objective is 2−R(ψ). The paper cites Montgomery–Taylor optimality within this one-window family and gives
C0=2−RMT=3/2−(1/√2)cot(1/√2)
=0.672500703679411645734379790803295188593403….
The exact-rational interval evaluator in src/replay_alpoge_furman.py independently encloses this expression.

## K. Simple-zero deduction

The rank of P1 is bounded above by the number of simple zeros on the line. The inequality above therefore gives the simple-on-line coefficient 2−R(ψ), with the asymptotic o(N) error.

## L. Distinct-zero deduction

Rearranging the same zero-side counts gives
3s1+4(s2+p)≥(4−R(ψ))N.
Subtracting N≥s1+2s2+2p yields
2(s1+s2+p)≥(3−R(ψ))N.
Therefore the distinct-zero coefficient is (3−R(ψ))/2. At MT this is C1=(C0+1)/2=0.836250351839705822867189895401647594296701….

## M. Bandwidth-one ceiling

The broader certificate class uses arbitrary configuration-wise lower bounds p depending only on first and second trace moments from Fourier support [-1,1] tests and the on/off-line partition. A 256-periodic marked law with external EnclOK enclosures gives p0≈0.68182868746 plus a derivative-regularity error. The independent status is documented in CERTIFICATE_SPEC.md. It is conditional on external interval data, not an unconditional attained lower bound.
