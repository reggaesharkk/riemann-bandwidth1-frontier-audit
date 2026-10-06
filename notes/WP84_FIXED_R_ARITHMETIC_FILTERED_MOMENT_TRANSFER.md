# WP84 — fixed-R arithmetic filtered moment transfer

Date: 2026-10-07. Parent: 8ff09bcb3e295338b655dea8cb8661b5e521ae35.

Status: **CLOSED finite correlation expansion, exact closure reduction and
short-cutoff arithmetic theorem; FALSIFIED preservation of the frozen fifth
moment under that short-cutoff reduction; OPEN original-scale B->C.**
The geometric/reprojection results are frozen and not changed here.

## 1. Scale audit: three lengths must not be conflated

Use Z(T)=N(T,2T) for the ZERO count, N for the largest retained prime power,
and X for the original support cutoff. The source test family has exactly

    ell=log(T/(2pi)), L=ell, X=exp(L)=T/(2pi),
    h=2pi/L, d=floor(TL/(2pi)), tau_k=T+hk.

These definitions are in Section 2.2 of
[Alpöge–Furman, arXiv:2608.13637v2](https://arxiv.org/html/2608.13637v2#S2.SS2).
Source Remark 6.1 also discusses L=lambda*ell as a DIFFERENT bandwidth
construction. By the Riemann–von Mangoldt formula, d/Z(T)->L/log T; at the
headline scale this tends to 1. No exact equality d=Z(T) is needed here.

The branch's adaptive endpoint surrogate takes

    N=floor(X exp(-W)), W->infinity, W/L->0,

with working choice W=sqrt(L). The notes sometimes write the weaker bound
N<=T exp(-sqrt(L)+o(1)), absorbing 2pi. There is no executable prescription
for a largest prime itself: sums use the integers n<=N with Lambda(n)!=0.
No uniform logarithmic allowance is provided for N far below this range.
The permitted o(L) quarantine has log N/L->1 and log N/log T->1; hence

    N^k/T=T^(k-1-o(1)) -> infinity for every fixed k>1.

Changing W within o(L) cannot impose N^3/T->0.

The relevant assumption inventory is below. These are hypotheses used by
this branch, not a claim that every historical note has been independently
re-proved. Unrelated numerical parameters also called L are excluded.

| Gate | Actual length/normalization requirement | Short-scale consequence |
| --- | --- | --- |
| Explicit-formula support | supp(phi) subset [-L/2,L/2], prime shifts log n<=L, X=e^L | L may define a different family, but a sharp prime cutoff below e^L is not the same full Weil matrix |
| Taper/ramp | w=o(L), a_phi=||phi||_2^2/L->1; width one is sufficient | Still possible if L->infinity |
| PNT square measure | a_phi^-2 L^-2 sum_p (log p)^2/p delta_(log p/L) -> s ds when log N/L->1 | Holds for any L->infinity with N=e^(L-o(L)); fails to keep full [0,1] mass if L is held fixed relative to log T while N is power-shortened |
| Linear/proper-power mass | sum |c_n|^2=O(1), proper powers O(L^-2), c_n=-Lambda(n)/(a_phi L sqrt n) | Still holds for any L->infinity; not a raw high-moment disposal by itself |
| Background scalar | s0=ell1(T)/(a_phi L), ell1(T)=log T+O(1) | s0->1/theta at L~theta log T, not 1; diverges if L=o(log T) |
| Dimension / zero count | d=floor(TL/(2pi)), Z(T)~T log T/(2pi) | d/Z->theta, or zero if L=o(log T) |
| Physical endpoint quarantine | W=o(L), rank fraction O(W/L); quadrature error dominates crude sqrt(X) norm | Power shortening at unchanged L needs W/L bounded away from zero and is not the proved o-rank operation |
| Good principal section | q=floor(d/sqrt(L)), d'/d->1, N/(qh)->0, qh~T/sqrt(L) | Shorter N makes the linear sampling condition easier |
| Fixed R reprojection | R fixed, finite local score, d'->infinity | Preserved for a different short-scale PRIME operator |
| Functional band comparison | finite normalized alpha square mass; q_alpha->1/4 at full prime measure | Finite bound survives; the frozen 1/4 and variance budget change at an unrenormalized shortened cutoff |
| Carrier-2T current covariance | X0~T, log P0~(log T)^(2/3)(log log T)^(4/3), log P0=o(L) | Works for fixed theta>0; not automatically for arbitrary L=o(log T) |
| Lower centered gates | center at 1, full prime-pair variance near 1/3, aggregate third moment removal | Center at 1 is lost when L/log T does not tend to 1; the original aggregate third gate is not a new high-product theorem |
| Bounded zero transfer | full matrix, d/Z->1 for the frozen consumer coefficient; o(d) rank deletion | Positive-index lower bound becomes 2(d/Z)(n_+/d)-1; the frozen >79 coefficient is not preserved |

The matrix/zero-ratio and scalar-background conclusions follow directly from
the displayed formulas. They do not depend on a conjectural higher-moment
transfer. The source's tail-Weyl estimates improve when X is shorter, but
this does not recover the lost dimension or the different centering.

### Two distinct shortening experiments

**Keep L~log T, set N=T^theta with theta<1/3.** Then the prime-square measure
becomes s*1_[0,theta](s) ds, not s ds on [0,1]. Its total mass is theta^2/2.
In the existing sharp pair normalization the variance is

    2 int_0^theta s(1-s) ds = theta^2-(2/3)theta^3,

instead of 1/3. At theta=1/3 it is 7/81. The deleted square mass has a
nonzero limit. Neither PNT renormalization nor the o(L) endpoint theorem
preserves the frozen continuum law in this experiment.

**Set L~theta log T, N=e^(L-o(L)).** The one-prime s ds measure is preserved,
and theta<1/3 makes short-product estimates available. However s0->1/theta
and d/Z->theta. Even a positive definite matrix only supplies n_+/Z<=theta,
so the retained positive-index implication cannot yield >79 (it requires
theta>0.895 even with zero consumer defect). Renormalizing the whole matrix
to center one multiplies its prime coefficients by theta, changing their
moments. L=o(log T), L->infinity, has the same problem more strongly.

Therefore a stronger cutoff is admissible for a DIFFERENT arithmetic family,
but not as a free change preserving this frozen theorem and its moments.

## 2. CLOSED: finite Dirichlet-correlation expansion of the actual B

Use the selected section I=[k_-,k_+], length d', and the infinite band
operator S_T,R from the previous note. B_b=d'^-1 tr(P_I S_T,R^b P_I).
For fixed R enumerate r_1,...,r_b in [-R,R] with sum r_j=0, and let
q_j=sum_(a<=j) r_a. These are finitely many lattice paths independent of T.

For s=log n/L in [0,1], the Fourier coefficients of the two partial shifts are

    j_0^+(s)=j_0^-(s)=1-s,
    j_r^+(s)=(exp(-2pi i r s)-1)/(2pi i r),
    j_r^-(s)=(1-exp(2pi i r s))/(2pi i r), r!=0.

Define explicit linear polynomials

    F_(r,q,+)(t)=sum_(n<=N) c_n j_r^+(log n/L) exp(i h q log n) n^(it),
    F_(r,q,-)(t)=sum_(n<=N) c_n j_r^-(log n/L) exp(-i h q log n) n^(-it).

Then EXACTLY

    B_b= sum_(closed paths r) sum_(epsilon in {+,-}^b)
           d'^-1 sum_(k in I) product_(j=1)^b F_(r_j,q_j,epsilon_j)(T+hk).

This is a finite sum of correlations at fixed R. Its coefficients are explicit
fixed-R FUNCTIONS of log n/L, not constants independent of n. That distinction
matters for PNT testing, but they are uniformly bounded with bounded variation.

Collapse the positive factors to a_r(u) and the negative factors to a_s(v),
where r+s=b. Absorb their fixed-lag phases and j-functions into the coefficients.
Write the negative-side polynomial as conjugate(sum_v a_s(v) v^(it)). Then
each correlation is

    H_(r,s)=sum_(u<=N^r,v<=N^s) a_r(u) conjugate(a_s(v)) K_I(log(u/v)),
    K_I(lambda)=exp(i(T+h k_-)lambda) D_d'(lambda/L),
    D_m(z)=m^-1 sum_(k=0)^(m-1) exp(2pi i k z).

Empty sides have a_0(1)=1. This identity retains the actual selected-section
carrier and all aliases. No continuum kernel or sign is inserted in it.

| Degree / population | Factor lengths | Maximum pooled length | Weighted Hilbert scale |
| --- | --- | --- | --- |
| 5: 0-vs-5, 5-vs-0 | 1, N^5 | N^5 | N^(5/2)/T |
| 5: 1-vs-4, 4-vs-1 | N, N^4 | N^4 | N^(5/2)/T |
| 5: 2-vs-3, 3-vs-2 | N^2, N^3 | N^3 | N^(5/2)/T |
| 6: 0-vs-6, 6-vs-0 | 1, N^6 | N^6 | N^3/T |
| 6: 1-vs-5, 5-vs-1 | N, N^5 | N^5 | N^3/T |
| 6: 2-vs-4, 4-vs-2 | N^2, N^4 | N^4 | N^3/T |
| 6: 3-vs-3 | N^3, N^3 | N^3 | N^3/T |

Repeated factors/proper powers do not increase these support lengths. Exact
closures reduce to at most three independent prime bases; nearby lower-
multiplicity sectors still live inside the indicated long correlation.
The sign counts are binom(b,r); none is omitted. Aliases shift one frequency
family by mL and hence are not ordinary integer-product equalities.

## 3. CLOSED: coefficient norms including proper powers

For any fixed j<=6 and bounded slow coefficient factors, collapsed j-fold
coefficients obey

    sum_u |a_j(u)|^2=O_j(1),
    sum_u u |a_j(u)|^2 <= N^j O_j(1).

Proof: expand the square, an exact equality between two j-fold products.
Group occurrences by prime base. For one base p let v be the number of
occurrences and E their total exponent. Balance gives E even. Its absolute
weight is bounded by const_v (log p)^v/(L^v p^(E/2)). The only leading group
is v=E=2, an ordinary opposite-side pair, whose sum is O(1). Every other
balanced group has E>=4. Summing over all exponent compositions introduces
only a fixed-degree polynomial in E. The sum over p and E then converges
absolutely, leaving O(L^-v). There are finitely many base-group patterns.

This proof extends the ordinary two-product lemma to the degrees needed here
and INCLUDES proper powers. It does not bound the long off-diagonal energy by
these norms alone. A crude pointwise bound useful at aliases is

    |a_j(u)| <= C_j(1+L)^j/sqrt(u), u<=N^j.

Indeed each individual |Lambda(n)/(a_phi L)| is bounded, and a product with
at most j distinct prime bases has at most C_j(1+log u)^j ordered prime-power
representations. Both bounds are uniform over the finite set of lag features
at fixed R and over the starting carrier phase.

## 4. Mean values in the correct normalization

On a continuous interval J of length U~T, the bilinear Montgomery--Vaughan
Hilbert estimate, applied to the integer log frequencies, gives

    |U^-1 int_J P_r(t) conjugate(P_s(t)) dt
       -sum_u a_r(u) conjugate(a_s(u))|
      <= C/U [sum_u u|a_r(u)|^2]^1/2
                 [sum_v v|a_s(v)|^2]^1/2
      = O_b(N^(b/2)/T).

Local spacing is >=c/u; the bilinear endpoint phases do not change the norms.
This is stronger than using the minimum global separation and pooled length
N^max(r,s). The applicable inequality is the weighted bilinear form in
Montgomery–Vaughan, [Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
or source Lemma 2.2. The observation N^4 in a 2-vs-4 sector does not require
N^4/T->0: the two weighted norms give N^3/T.

BUT the actual average is a Fourier-grid sum. A continuous mean value does
not identify it: frequencies may agree modulo L. This requires the separate
alias analysis in Section 5.

For the zero-alias cell |lambda|<=L/2, u!=v, the exact geometric sum gives

    |K_I(lambda)|<=C/(T|lambda|),

uniformly over the selected section, since h d'~T. If |log(u/v)|<=1, then
1/|log(u/v)|<=C sqrt(uv)/|u-v|. The positive kernel 1/|u-v| on integers
up to N^b has l2 norm O(1+log(N^b)) by its row sums. Apply it to
sqrt(u)|a_r(u)| and sqrt(v)|a_s(v)|. For |lambda|>1, use |K|<=C/T and
the l1 norms bounded by sqrt(support)*l2 norm. Consequently the CENTRAL
nonexact discrete contribution is

    O_b((1+L) N^(b/2)/T).

This is an absolute grouped estimate, not wordwise prime l1 summation.
At the current N=T^(1-o(1)) it does NOT tend to zero for b=5 or b=6.
At a fixed theta<1/3 it does. A failure of this upper bound is not a
counterexample to the original-scale correlation asymptotic.

The same discrete/alias estimates at degrees one and two DO tend to zero
at the working original cutoff: their worst product scales are sqrt(N)/T
and N/T, and the sqrt(L) quarantine absorbs every fixed logarithmic factor.
They justify the fixed-lag linear mean and pair covariance/PNT substitutions
used in the band comparison. At degree three our generic bound does not
close at that long cutoff; previously claimed aggregate third-moment gates
still require their own valid signed estimate. In the short-cutoff theorem
all degrees through six, including centered third PRIME moment, are covered.

## 5. Periodic aliases: exact condition, bound, and remaining debt

The exact sampled resonance condition is

    h log(u/v) in 2pi Z,
    log(u/v)=m L, equivalently u/v=X^m.

An exact alias has D_d'(m)=1 and carrier exp(i T mL); its Fourier-section
phase exp(2pi i k_- m)=1. For approximate aliases

    |log(u/v)-mL| <= O(1/T)

the geometric sum can still be order one. Only finitely many integers
|m|<=b can occur at degree b. If X is irrational there may be no exact
nonzero aliases, but this does not control approximate ones uniformly in T.

Here is a grouped bound valid even when X is tuned to an exact arithmetic
alias. For m>0 write A=X^m; exchange u,v for m<0. In the near-alias zone
|log(u/(Av))|<=1, u is comparable with Av. The kernel is bounded by

    min(1,C Av/(T |u-Av|)).

For each fixed integer v, at most a fixed number of nearest integers u
contribute the first bound 1. The remaining distances give a harmonic sum:

    sum_(u~Av) min(1,C Av/(T |u-Av|))
       <= C[1+(Av/T)(1+log(N^b))].

Interpret a zero denominator by the bound 1. Multiplying the pointwise
coefficient bounds from Section 3 by 1/sqrt(uv)~A^-1/2/v and summing v up to
V<=min(N^s,e N^r/A) gives

    Alias_(r,s,m)
      = O_b((1+L)^(b+1)[X^(-|m|/2)+N^(b/2)/T]).

Use A^1/2 V<=sqrt(e)N^(b/2). If a side is empty, v=1 and the same bound
holds. Away from every |lambda-mL|<=1, the kernel is O(1/T), and support/l2
Cauchy–Schwarz gives O_b(N^(b/2)/T).

Therefore exact nonzero aliases alone are CLOSED o(1) at the current scale,
bounded by O_b((1+L)^(b+1)X^-1/2); their carriers need not cancel. Near aliases
remain OPEN there, since the second bound grows. Under

    (1+L)^7 N^3/T ->0, X=e^L->infinity,

ALL alias and central nonexact terms for b<=6 are CLOSED o(1). Fixed
L=theta log T, theta<1/3, or L=o(log T) with L->infinity and N<=e^L,
satisfies this sufficient condition. Bare N^3/T->0 is sufficient for the
continuous Hilbert estimate, but the crude discrete alias proof here asks
for the displayed logarithmic saving. No arbitrary near-frequency gap is
assumed.

## 6. CLOSED exact closures and PNT transfer AFTER reduction

For ordinary primes u=v means equal multisets on the two sign sides.
At degree five there is no equality: the two sides have different counts.
At degree six, only 3-vs-3 is possible. Its leading exact equalities have
three distinct prime bases, each used once positively and once negatively.
There are 15 perfect matchings of the six positions and 2^3 orientations.
Repeated bases such as p,p,q or p,p,p have vanishing normalized mass because
sum_p |c_p|^4=O(L^-4). Exact closures containing proper powers are lower
order by the same prime-base argument in Section 3. This includes the
exceptional 2-vs-3 and 2-vs-4 equations made possible by powers.

After this exact reduction, the sixth pair contribution converges by PNT/BV
to the explicitly filtered Wick functional

    Pair6_R=sum_(15 matchings pi) sum_(2^3 orientations epsilon)
                 int_[0,1]^3 Omega_6,R(v_(pi,epsilon,s))
                              product_(a=1)^3 s_a ds_a.

Each matched position receives opposite shifts +/-s_a. The carrier and section
phases cancel EXACTLY. All finite-R tests are bounded/BV in each coordinate.
The O(L^-2) one-prime discrepancy, log N/L->1, a_phi->1, product testing,
and vanishing coincident-prime mass justify this transfer. No oscillatory
kernel is left at this stage. The corresponding fifth exact part is zero.
For the retained endpoint surrogate, the omitted interval contributes
O_R(1-log N/L), in addition to the full-measure O_R(L^-2) discrepancy and
O_R(|a_phi-1|). Thus the working W=sqrt(L) yields an O_R(L^-1/2) endpoint
charge, not an O(L^-2) total transfer error. All these charges tend to zero.
This proves the PNT transfer of the EXACT sectors at the ORIGINAL scale too;
it does not remove nonexact terms there.

The labels {4,2} and {6} in the frozen continuum cumulant ledger are not
additional ordinary-prime exact-equality multiplicity types. The only leading
ordinary exact class at degree six is the three-pair class. A finite-R
identification of its Wick functional with any particular cumulant/model
sector must respect the full model normalization; its name alone is not a
proof. Exact ordinary equations do NOT generate a degree-five 1/36 or
separate leading connected four/six prime-base groups.

## 7. CLOSED short-cutoff theorem / FALSIFIED unchanged fifth target

Assume L->infinity, X=e^L, a_phi->1, log N/L->1, d' h~T, and
(1+L)^7 N^3/T->0. For every fixed R, the finite expansion, norm bounds,
alias bounds, exact closures, and PNT transfer above prove

    B_5,T,R=o(1),
    B_6,T,R=Pair6_R+o(1).

The estimates are uniform over admissible contiguous selected sections
because only d' h~T is used and endpoint carrier phases have modulus one.
Proper powers are included in this theorem and disposed of AFTER the
nonexact terms have been controlled.

Thus short-cutoff arithmetic DOES close, but to a pure pair/Wick law, NOT
to the frozen fifth model 1/36. The assertion that shortening preserves the
same full normalized C5_R is FALSIFIED: the fifth limit is zero for every
fixed R in this regime, whereas the frozen C5_R tends to 1/36 as R increases.
One-prime measure invariance is not full-moment invariance.

At the original scale, write the exact decomposition

    B5 = NearNonexact5 + o(1),
    B6 = Pair6_R + NearNonexact6 + o(1),

where NearNonexact includes the finite lag-feature correlations after exact
equalities and exact aliases have been removed. Far terms are INCLUDED unless
separately estimated; no claim that they are already o(1) at the long scale
is made. The name indicates the known unsuppressed windows, not a proved
support localization. The frozen nonzero fifth constant must come from this
nonexact arithmetic if the proposed B5->C5_R is true. Its value/density has
not been derived from prime-square PNT. The supercritical model integral
1/36 is a target for this transfer, not an arithmetic equality sector.

## 8. Single remaining theorem interface

OPEN: for the actual N=floor((T/(2pi)) exp(-o(log T))) with the working
sqrt(L) quarantine, prove the normalized signed product-correlation law,
uniformly over the selected section and the finite set of R-lag features,

    Nonexact5_R(T) -> C5_R,
    Nonexact6_R(T) -> C6_R-Pair6_R.

The left sides are exactly the H_(r,s) sums of Section 2 with u=v removed
and negligible exact nonzero aliases removed. They include the 2-vs-3,
2-vs-4 and 3-vs-3 near-product windows, near aliases u~X^m v, and all
proper-power/repeated-base residuals. A joint signed estimate of these two
finite-feature quantities is the narrowest remaining arithmetic theorem;
stronger positivity or full asymptotics for each separate sector is not
necessary. Existing current-prime carrier-2T estimates apply to bounded
resolvents, not this unbounded product state, and do not supply this law.

B5/B6->the frozen C5_R/C6_R remains OPEN. No scale-preserving bypass by
N^3/T->0 is available from the audited construction. No geometric statement,
C5 sign theorem, C6 witness, or prior commit is changed; no push is performed.

## 9. Verification scope

The companion script independently checks source-scale consequences,
product-length/sign counts, exact multiplicative closure patterns, the
finite Fourier-path expansion against a direct ambient matrix power, and
the collapsed diagonal correlation identity including proper powers.
These finite checks are diagnostics. Sections 3–7 contain the asymptotic
proofs and their hypotheses; the script certifies no long-scale arithmetic
limit or zero-proportion theorem.
