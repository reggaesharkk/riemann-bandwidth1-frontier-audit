# WP84 cubic first alias: one denominator-Type-II feasibility experiment

2026-10-08; input HEAD `9203b8e5d2c1466ad2c1e038ab945fdb86362602`.
**Verdict: NO-GO for transferring rectangular additive bilinear savings to
this source window by the tested denominator-Vaughan decomposition.** No
power saving on the actual window, o(1) bound for that window, or negative
signed constant is proved. A rigorous small-core phase linearization is
newly justified; its accuracy is not a magnitude saving. This verdict does
not falsify the arithmetic inequality or exclude other arithmetic methods.

## 1. Complete source expression for the tested window

Keep R=6000, X=T/(2pi), L=log X, N=floor(exp(L-sqrt L)), h=2pi/L,
d=floor(XL), a_phi->1, and the original prime sections and source masks.
Use the canonical I={0,...,d-1}, or its contiguous subintervals, for the
phase bound below. Arbitrary principal deletion still uses the inherited
COMPLETE-gate transfer; no masked deletion estimate is presumed.

For each original b=3 or b=5 closed displacement path ell, |ell_j|<=6000,
q_j=sum_(t<=j)ell_t, rho=n-max q+min q (or zero), i_min=a-min q, put

    F_j^eps(p)=f_(ell_j)^eps(log(p)/L)
                          exp(2pi i eps q_(j-1)log(p)/L),
    c_p=-log(p)/(a_phi L sqrt p),
    f_0^eps(s)=1-s,
    f_l^+(s)=(1-exp(2pi i l s))/(2pi i l), f_l^-=conj(f_l^+).

For any placement of two positive visible slots p,q and a negative slot r,

    delta=log(pq/(Xr)),
    K_ell(delta)=exp(iT L)/n
                 sum_(j=0)^(rho-1)exp(i(T+h(i_min+j))delta).       (1)

All prime variables remain <=N, with original ordered-slot restrictions.
Let chi contain the original masks, distinctness, dyadic prime/product
cells, U=pq asy X^(8/5), V=r asy X^(3/5),
r>sqrt X/L^3, and the EXACT chosen alias indicator on delta.
The b=3 contribution is

    S3=sum_(p,q,r distinct) c_p c_q c_r F_p^+(p)F_q^+(q)F_r^-(r)
                                      chi(p,q,r) K_ell(delta).    (2)

For b=5 choose the two hidden paired slots a,b and keep the physical FIVE
displacements, prefixes, rho and i_min. Its contribution has exactly (2)'s
three visible factors for those slots, multiplied by

    B_ab,T(p,q,r)=sum_(z prime<=N,z notin {p,q,r}) c_z^2
       [F_a^+(z)F_b^-(z)+F_a^-(z)F_b^+(z)],                      (3)

with its original hidden-slot masks retained. No covariance/PNT replacement
of (3) is performed on this frequency window. Its total absolute mass is
<=2 sum |c_z|^2<=2 eventually, sufficient for the bounds below. The paired
prime's frequency cancels; its prefix/filter phases do not disappear.

The tested shared sector is the real part of c3 times all (2)'s minus A
times all b=5 (2)--(3)'s, including the conjugate sign placements,
c3=21981971/46375000, A=11501/12500. The complete R=6000 path sums are
retained; neither three visible fifth-path increments nor their root ranges
are substituted by a cubic closed path. The carrier exp(iT L) remains in
every expression. Proper-power removal and complete good-section transfer
keep their existing bounded-gate hypotheses; no new masked power disposal
is claimed. Source definitions are pinned in the certificate.

## 2. The actual X^(1/10) loss and detuning shells

For r~V0, pq~X V0, on |delta|<=H/X with H/X<=1/4,
the integer u=pq interval has length <=3H r. An integer u has at most two
ordered distinct-prime representations. Since |c_p|<=2/sqrt p and |F|<=1,
the COMPLETE coefficient mass per fixed path/sign word is at most

    32 X^(-1/2) [1+3H V0].                                    (4)

For V0~X^(3/5), its leading exponent is H X^(1/10): there are O(H V0^2)
candidate (u,r) pairs of weight O(X^(-1/2)/V0). This is an upper bound,
not an assertion that primes realize the count. In shells
H/X<=|delta|<=2H/X, the geometric kernel is O(1/H), so the bulk
majorant remains O(X^(1/10)) per shell. Summing up to the unit-log window
introduces a logarithm, not a power saving.

The fixed-product dyadic prime cells have p~X^a,q~X^b,a+b=8/5.
Every listed cell is eventually allowed by the unchanged natural cutoff.

| a | b | r exponent | q interval after fixing p,r in fixed-H core | Existing bulk loss |
|---:|---:|---:|---:|---:|
| 13/20 | 19/20 | 3/5 | X^(-1/20) | X^(1/10) |
| 7/10 | 9/10 | 3/5 | X^(-1/10) | X^(1/10) |
| 3/4 | 17/20 | 3/5 | X^(-3/20) | X^(1/10) |
| 4/5 | 4/5 | 3/5 | X^(-1/5) | X^(1/10) |
| 17/20 | 3/4 | 3/5 | X^(-1/4) | X^(1/10) |
| 9/10 | 7/10 | 3/5 | X^(-3/10) | X^(1/10) |
| 19/20 | 13/20 | 3/5 | X^(-7/20) | X^(1/10) |

Intervals have these lengths up to fixed factors. A subunit interval can
contain an integer; it is not identically empty. It gives no long inner
sum for an ordinary univariate oscillation estimate.

## 3. Source-legal simplification that actually passes

Write w=(pq-Xr)/(Xr)=exp(delta)-1 and tau_j=T+h(i_min+j).
For |delta|<=H/X<=1/4, |w|<=2H/X<=1/2 and
|log(1+w)-w|<=w^2. On the stated canonical sections tau_j<=2T=4pi X.
Thus replacing only exp(i tau_j delta) by exp(i tau_j w) has pointwise
error <=16pi H^2/X. Combine with (4): the complete per-path error is

    <=512pi H^2 X^(-3/2)+1536pi H^3 V0 X^(-3/2).

For V0<=2X^(3/5) this is

    <=512pi H^2 X^(-3/2)+3072pi H^3 X^(-9/10).                  (5)

Multiply by 6(c3*12001^2+20*A*12001^4) for a conservative bound on the
entire shared cubic sector. All original weights, masks, hidden primes and
root sums stay unchanged. This is a direct summed estimate, not a wordwise
PNT error promotion. For fixed H the error is O_R(X^(-9/10)).

| H=X^h | Certified linearization error exponent from (5) | Saving on original magnitude |
|---:|---:|---:|
| h=0 | -9/10 | 0 |
| h=1/10 | -3/5 | 0 |
| h=1/5 | -3/10 | 0 |
| h=1/4 | -3/20 | 0 |
| h=3/10 | 0, insufficient for o(1) | 0 |

This replacement is accurate for h<3/10. It does not control larger
detuning shells or delete tails. The remaining additive form, with
theta_j=tau_j/(2pi X), is exactly the linearized root sum

    exp(iT L-i tau_j) * exp(2pi i theta_j pq/r).                  (6)

At physical root index i=0 (for example on the zero-displacement path),
theta=1. Every other canonical root has 1<theta<2 and is not an integer.
The cutoff conditions still couple pq and r.

## 4. One denominator Vaughan decomposition: identities versus estimates

Only the denominator prime weight is decomposed. Write
Lambda_prime=Lambda-E, where E is Lambda on proper prime powers and zero
elsewhere. For arbitrary integer cutoffs U0,V0>=1, Dirichlet convolution gives

    Lambda=mu_(<=U0)*log-mu_(<=U0)*1*Lambda_(<=V0)
                 +Lambda_(<=V0)+mu_(>U0)*1*Lambda_(>V0).          (7)

This exact identity is already established in the frozen source; here it
is specialized to r~X^(3/5), with U0=V0=floor(X^(1/10)).
The denominator short term is empty eventually. Type I has a<=U0 and a
logarithmic leaf, or a<=U0,c<=V0 and the remaining unrestricted leaf.
Type II writes r=ab, a>U0,b>V0, with coefficient
mu(a) beta_V0(b), beta_V0(b)=sum_(c|b,c>V0)Lambda(c)<=log b.
The proper-power compensation E is retained EXACTLY on this window.

The source functions of r become functions of ab. They can be handled
algebraically: (ab)^it=a^it b^it, the nonzero-displacement f is a difference
of two multiplicative factors, and f_0=1-log(a)/L-log(b)/L. These expansions
are finite and preserve the source filter. The alias indicator is still
1_E(log(pq/(Xab))), and the original exclusions and product windows remain.
They are not independent rectangular weights.

| Type-II a exponent | b exponent | b interval after fixing p,q,a, fixed H |
|---:|---:|---:|
| 1/5 | 2/5 | X^(-3/5) |
| 1/4 | 7/20 | X^(-13/20) |
| 3/10 | 3/10 | X^(-7/10) |
| 7/20 | 1/4 | X^(-3/4) |
| 2/5 | 1/5 | X^(-4/5) |

These are genuine algebraic Type-II leaves; the inner constrained intervals
are not long rectangles. Keeping a prime indicator 1_P(ab) on each Type-II
leaf would instead kill that leaf identically. The valid decomposition uses
(7)-E on integers and reconstructs the prime weight by cancellation. Dropping
E already fails at r=49. No separately masked E=o(1) theorem is invented.
The independent formal-log convolution test checks (7)-E through 192.
No Heath-Brown expansion is needed or launched for this experiment.

## 5. Attempted bilinear saving: first invalid transfer and exact zero mode

Here is the specific unconditional rectangular estimate tested. If v is a
positive integer, c is an integer coprime to v, and A_p,B_q are SEPARABLE
arrays on integer intervals of lengths P,Q, then

    |sum_(p,q) A_p B_q exp(2pi i c pq/v)|
      <=sqrt(v ceil(P/v) ceil(Q/v)) ||A||2 ||B||2.               (8)

Constant 1 is exact for this bound. Proof: collect residues modulo v;
each residue sum's squared norm is at most ceil(P/v) or ceil(Q/v) times
the original squared norm. The discrete Fourier matrix has norm sqrt v
because c permutes the residues. Cauchy finishes the proof. Prime-supported
and source filter arrays are permitted, provided the weight remains separable.

At P,Q~X^(4/5),v~X^(3/5), (8) gives a relative X^(-3/10) saving on the
UNRESTRICTED rectangle. With normalized prime weights' individual squared
masses bounded, the bound is O(X^(1/2)) per v. Multiplying by v^(-1/2)
and summing V~X^(3/5) denominators permits O(X^(4/5)), up to logarithms:
still much worse than the strip's existing X^(1/10) bound. Subtracting 3/10
from 1/10 to claim X^(-1/5) is invalid; they have different starting counts.
Vaughan leaf norms only add logarithmic/divisor costs, not a certified gain.

Even this rectangular theorem's hypotheses fail for the actual expression:
for most roots theta_j in (6) is not a coprime integer numerator, and for
ALL roots the near-product mask is not a separable rectangle. At physical
root i=0, where the phase hypothesis does pass, mask completion
exhibits the missing component explicitly.

Take the allowed integer-X subcase and the positive half-core

    0<pq-Xv<=floor(v/1000).

This is inside |delta|<=1/(1000X). Its exact mask is the intersection of
Xv<=pq<(X+1)v and the periodic residue mask
M_v(n)=1_(n mod v in J), J={1,...,floor(v/1000)}. Define

    hat M_v(a)=v^(-1) sum_(j in J) exp(-2pi i a j/v).
    exp(2pi i n/v) M_v(n)
      =sum_(a mod v) hat M_v(a) exp(2pi i (a+1)n/v).             (9)

The a=v-1 term has ZERO frequency. Its coefficient is
v^(-1) sum_(j in J) exp(2pi i j/v), with positive real part
>= (4999/5000)*|J|/v for J nonempty. Thus a uniform coprime/minor-arc
saving cannot be applied to every completed mode. The quotient/product
mask also remains coupled; it is not silently removed by (9).
For v=1009 the zero-mode coefficient is exactly exp(2pi i/1009)/1009,
nonzero. This is an exact identity, not a surrogate moment calculation.

The elementary Fourier orthogonality in (8)--(9) is proved here; no external
theorem is imported beyond its hypotheses. The classical Vaughan identity
is independently proved/tested as convolution, consistent with the existing
source and [Petrow's primary notes, Section 3.1](https://www.homepages.ucl.ac.uk/~ucahpet/Vino3Primes.pdf).
An additive-prime theorem for sum Lambda(n)e(alpha n) would also require its
linear phase and approximation hypotheses: (6) is reciprocal in the
decomposed denominator, and retains the thin-strip mask. No such theorem
constant is asserted for this source form. A dispersion application would
require new estimates for the exact off-diagonal masked correlations;
performing Cauchy does not supply them.

## 6. Falsifier for the generic envelope-to-o(1) inference

This is INTEGER SURROGATE data, not source primes, source filters or zeta
moments. It tests the claimed transfer from coefficient envelopes and
rectangle norms to a thin-window o(1) bound. Let X=M^5, U=M^8, V=M^3,
M>=13, and take arrays u^(-1/2),v^(-1/2) on [U,2U),[V,2V). Each squared
norm is <=1. Keep the ACTUAL canonical root kernel (1) with R=6000's
zero-displacement path. Sum only u=Xv+j,1<=j<=floor(v/1000).
These lie in the requested product ranges and strictly exclude exact aliases.

Since delta<=1/(1000X), every canonical root phase tau_j delta is <1/50.
After rotating by the still-present COMMON carrier, the kernel's real part
is >=4999/5000. There are at least V^2/2000 such integer pairs; each
weight is >=1/(2sqrt X V). Hence

    |S_toy| >= (4999/20000000) X^(1/10).                       (10)

This is a rigorous growing lower bound for a surrogate satisfying the pointwise
envelope and bounded squared masses. The common carrier was not discarded:
the rotation is used only to lower-bound the absolute value. Source prime
factorization and filters are absent, so (10) is NOT a lower bound on WP84.
It falsifies a generic norm/rectangle argument, not the prime inequality.

## 7. Exponents, log factors, budget and stopping verdict

Strongest certified power saving on the actual window's MAGNITUDE: 0.
Certified fixed-core LINEARIZATION error exponent: 9/10, a different quantity.
Actual constant signed saving: 0. Neither the sign of the shared covariance
coefficient nor the carrier implies a negative contribution.

A new normalized per-block estimate X^(1/10-eta) L^B would beat the power
loss if eta>1/10, for any fixed B. The denominator-Type-II expansion has
O(L) compatible p/q dyadic pairs, O(L) compatible a/b pairs, and O(L)
detuning shells: a uniform block estimate incurs at most L^(B+3) in that
branch. At eta=1/10 this would require B<-3, not merely a power tie.
Closing the full Vaughan identity also requires its Type-I and compensation
branches, including their dyadic counts. No such block estimate is proved.

The frozen same-section conditional margin remains
8558084052085891/91584868530424500000=0.00009344430132847649... .
The complete third/fifth/sixth residual still needs an upper bound
Jcap-B Pair6_6000-kappa-eta, with
Jcap=51835308978310574561/457924342652122500000. Its necessary negative
saving exceeds 0.002057354918974498... plus payments kappa and a strict gap.
No part of this quantitative deficit is earned by (5), (8) or (9).
Even a future o(1) removal of this one window would not itself earn a
negative constant or close the other cubic/ fifth/sixth windows and tails.

The narrowest new input for extending THIS method is a signed/absolute
dilated prime-product strip estimate for (2)--(3), controlling the zero/major
frequency component exposed by (9), uniformly in original weights and
roots, and strong enough to beat X^(1/10) and all aggregate log costs.
The frozen joint signed saving and prime-to-Weil, band-interface and
zero-side analytic obligations remain separate. No Gaussian or GUE values
are substituted. Stop here: NO-GO for the tested rectangular transfer;
the required prime correlation theorem remains unresolved.

## Independent reproduction

Run `python src/wp84_cubic_first_alias_typeii.py`, then the separate
`python src/wp84_cubic_first_alias_typeii_replay.py`. The latter imports no
producer, checks formal logarithmic convolution through 192, all exact
exponent/constant tables, zero-mode index and the coherent surrogate bound,
and rejects ten hostile promotions. These tests supplement the analytic
proofs; finite input enumeration is not an asymptotic prime theorem.
