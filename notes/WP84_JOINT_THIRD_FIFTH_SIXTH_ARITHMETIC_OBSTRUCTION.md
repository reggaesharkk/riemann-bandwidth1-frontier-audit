# WP84: source-exact joint cubic contraction and alias/product reductions

2026-10-08. Input HEAD `8db0eb54019a7b69d18f4ba937b26e98d0c9a1d2`;
branch `codex/c5-c6-attack-20261006`. Additive local artifacts only.

**New result:** summed low-product sectors and all exact nonzero aliases of
the ordinary-prime D3 and Q3 populations are o(1), uniformly in the actual
contiguous section. The third and fifth single-pair populations do share
exact frequencies. Their full path contraction is identified below; treating
it as a scalar variance contraction is false. No positive constant signed
saving is proved. Strict >79 remains OPEN.

## 1. Source and budget, unchanged

Source formulas: [source-matched reduction](WP84_STRICT79_SOURCE_MATCHED_ARITHMETIC_REDUCTION.md),
Sections 2--3; [signed ledger](WP84_STRICT79_SIGNED_ARITHMETIC_THEOREM_OR_OBSTRUCTION.md),
Sections 2--5; [third-aware same-section theorem](WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md),
Sections 1--7; [foundation audit](WP84_INDEPENDENT_REFEREE_RESPONSE_FOUNDATIONS_AND_GUE.md).
The JSON certificate pins their blobs and SHA-256 hashes at the input HEAD.

Keep X=T/(2pi), L=log X, N=floor(exp(L-sqrt L)), h=2pi/L,
d=floor(TL/(2pi)), fixed R=6000, and I=[a,a+n-1], n/d->1.
For every prime power m=p^v<=N use c_m=-Lambda(m)/(a_phi L sqrt m),
a_phi->1, s_m=log(m)/L. No prime pool, slot window, or filter is shortened.
For b=3,5,6, closed paths have |ell_j|<=6000, sum ell_j=0,
q_0=0, q_j=sum_(t<=j)ell_t, rho=max(0,n-max q+min q), i_min=a-min q.
Exactly,

    M_b^pow = sum_(eps,ell,m) W K(lambda),
    W=prod_j c_(m_j) f_(ell_j)^eps_j(s_(m_j))
          exp(2pi i sum_j eps_j q_(j-1)s_(m_j)),
    lambda=sum_j eps_j log(m_j),
    K(lambda)=exp(i(T+h*i_min)lambda)/n
                 sum_(j=0)^(rho-1) exp(i h j lambda),
    f_0^eps(s)=1-s,
    f_l^+(s)=(1-exp(2pi i l s))/(2pi i l), f_l^-=conj(f_l^+).

All sums retain the original ordered paths, factors and roots. At
lambda=m_alias L+delta, K retains exp(iT*m_alias L); it is not periodic
in lambda. Exact aliases need not have zero carrier phase.

For a good section formed by arbitrary principal row deletion, the
contiguous geometric kernel is NOT a formula for its frequency-masked
sum. Use these population estimates on the canonical full section, then
the previously proved bounded-gate Schatten transfer for the COMPLETE
joint gate: third/fifth compression losses are o(1) and sixth compression
is one-sided contractive when o(d) rows are deleted. This is conditional
on a bounded complete gate and the actual admissible section theorem;
no historical selector or masked deletion estimate is invented.

The frozen q is -19101/185500+(961/3710)x+(31/50)x^2-(371/500)x^3.
Every coefficient of q^2, in increasing degree, is

    (364848201/34410250000, -18356061/344102500,
     -26060119/430128125, 21981971/46375000,
     0, -11501/12500, 137641/250000).

Write c3=21981971/46375000, A=11501/12500, B=137641/250000.
For actual same-section centered moments, the sufficient gate is

    limsup(c3*mu3-A*mu5+B*mu6) <= Jcap-kappa-eta, eta>0,       (1)
    Jcap=51835308978310574561/457924342652122500000.

Here kappa>=0 is any additional source/zero-side payment, not certified zero.
The ordinary-prime first/second theorem gives mu1=o(1) and
mu2=1/6+pi^-2 sum_(r=1)^6000 r^-2+o(1), uniformly on the same I.
Its legitimate variance payment is 208480952/203775517378125;
band payment remains 128952763/92407500000. The resulting conditional
reference margin, independently recomputed from q^2, is

    Mref=8558084052085891/91584868530424500000
        =0.00009344430132847649... .                          (2)

Equivalently, with SIGNED reference differences, not zeta moment assumptions,

    limsup[c3*mu3+A*(1/36-mu5)+B*(mu6-34/135)]
                    <= Mref-kappa-eta.                      (3)

The prior Pair6_6000 lower certificate is retained. It makes the negative
joint residual saving necessarily exceed

    gnew=15909857470864664470267332031322977/
         7733161315109907280429056000000000000
        =0.002057354918974498...,

before kappa and eta. This lower bound is not a sufficient substitute for
the actual Pair6_6000 appearing in the residual gate.

## 2. Actual third sectors and aliases

Previously closed ordinary collisions leave D3: three distinct primes with
exponents +/-1. Unique factorization forbids lambda=0. Mixed signs have
lambda=+/-log(U/V), U=pq, V=r, three distinct primes. Same signs have
lambda=+/-log U, U=pqr. Mixed signs can meet +/-L; same signs can meet
both +/-L and +/-2L. The natural cutoff quarantines +/-3L by 3sqrt L.
Transition and far tails are always included. These statements concern
ordinary primes, not the still-present proper-power sum.

Q3 is the fifth-order population with one balanced prime pair and three
distinct visible primes. Its visible frequency is exactly the same cubic
frequency. The hidden prime retains its two slot filters and prefix phases.
It is summed over the full source cutoff, excluding the visible primes.
For large T, |c_p|<=2/sqrt p, |f|<=1, and
2 sum_(p<=N)|c_p|^2<=2. Thus the hidden pair has bounded total absolute
mass even before any PNT replacement. The following estimates apply to
both D3 and Q3 with their original fifth-order roots.

## 3. New unconditional SUMMED low-product theorem

**Theorem (ordinary source).** Uniformly in I as above, remove from either
D3 or Q3 (a) mixed-sign terms with U<=N, and (b) same-sign terms with
U<=N^2. Their complete sums are respectively

    O_R(N*(1+log(3N))/T)=o(1),
    O_R(N/T+L/sqrt X)=o(1).                                 (4)

These are partitions of the existing product sum, not changes to the prime
cutoff. Their bounds cover all original slot masks and carrier phases.

Proof. The geometric series gives, for distance delta to L*Z,
|K|<=min(1,C/(T*|delta|)), uniformly in starting phase and fixed path.
Every semiprime U has at most 2 ordered distinct-prime representations;
every three-prime U at most 6. The absolute coefficient of a visible cubic
tuple is at most 8/sqrt(UV) in the mixed case, or 8/sqrt U in the same-sign
case. Counting representations BEFORE summation, rather than estimating
one word and asserting a sum, is essential.

Mixed case: U,V<=N excludes a first alias by at least sqrt L. In the central
unit window, U~V and
1/|log(U/V)|<=C sqrt(UV)/|U-V|. Distinctness excludes U=V. Summing the
integer harmonic majorant over U,V<=N, with representation counts 2 and 1,
gives C N(1+log(3N))/T. Outside this window K=O(1/T), and
sum_(U<=N,V<=N)1/sqrt(UV)<=4N, giving O(N/T).

Same-sign case: log U>=log 8 and log U<=2log N<=2L-2sqrt L.
Outside |log(U/X)|<=1, every alias distance is bounded below by a positive
constant, so K=O(1/T). The TOTAL coefficient mass is bounded by
48 sum_(U<=N^2)U^-1/2<=96N. Within that first-alias window, U~X and

    |K|<=min(1,C X/(T*|U-X|)).

There are at most two nearest integers, costing O(X^-1/2), including an
exact alias. All remaining integers contribute a harmonic sum
O(log X/sqrt X). This proves (4). Arbitrary source masks can only decrease
these absolute majorants. For Q3, first sum the bounded hidden pair mass;
the same representation counting then applies. Finally sum over the FINITE
paths, sign placements and pair placements. Their constants depend on
6000 but not T. No growing-word summation or continuous mean value is used.
Since N/T=O(exp(-sqrt L)), both rates vanish.

## 4. New unconditional exact-alias theorem

**Theorem.** All exact nonzero aliases of D3 and Q3 are o(1).

Proof. For same signs, an exact alias requires U=X or U=X^2 to be an
integer. For each such value there are at most 6 ordered representations.
Each cubic coefficient is <=8/sqrt U, hence O(X^-1/2).
For mixed signs, an exact first alias requires U/V=X. If X is irrational
there are none. Write X=A0/B0 in lowest terms. Since V is prime, B0 divides
V and is either 1 or V. B0=1 would force V|U, contradicting the three
distinct primes. Consequently V=B0 is fixed, A0=U, and there are at most
2 ordered representations. Their coefficient is <=8/sqrt(A0 B0)
=8/(B0 sqrt X)<=8/sqrt X. Negative signs are the conjugate cases.
The kernel is bounded by 1 even at exact aliases; its carrier is retained.

With P3=12001^2, a conservative D3 bound is
288*P3/sqrt X. For |c3 D3-A Q3| the corresponding bound is
288*(c3*P3+20*A*12001^4)/sqrt X, using 10 pair placements and hidden
absolute mass <=2. This is not a near-alias estimate. Mixed exact aliases
are possible at legal large scales, e.g. X=pq/2 with distinct large odd
primes and visible prime 2; no generic integrality restriction on T is assumed.

## 5. Genuine phase-compatible cubic contraction, not scalar cancellation

The older disjoint-support statement concerned ONLY D5,Q3,D6,Q4, with
visible degrees 5,3,6,4. Adding D3 creates an exact degree-three overlap
with Q3. Shared visible tuples have the same lambda and the same carrier
exp(iT lambda). Their path/root factors can differ and must not be identified.

There is a source-matched way to keep those differences. Let W be an
AUXILIARY centered Gaussian Hermitian matrix with the source covariance:
alpha covariance delta_ij/4; beta diagonal 1/6 and off-diagonal
-1/(2pi^2(i-j)^2); cross covariance zero. Use the SAME finite I, R=6000,
and Loewner entries W_ii=beta_i, W_ij=(alpha_i-alpha_j)/(pi(j-i)) for
0<|i-j|<=R. This auxiliary covariance represents a hidden paired prime
after PNT; it asserts no Gaussian law for Y. Define

    D=E W^2, V(H)=E[W H W].

Under the existing bounded complete signed gate, the proved C_ab->k_ab
lemma and collision removals imply

    Q3=5*tau(D Y^3)+5*tau(V(Y)Y^2)+o(1).                    (5)

Proof of the algebra: among the 10 unordered two-slot choices in the cyclic
five-word trace, 5 are adjacent, giving E tau(W W Y Y Y), and 5 are
separated, giving E tau(W Y W Y Y). Cyclicity gives (5).
Finite matrix multiplication preserves EVERY original five-path root and
prefix factor, including its boundary restriction. Restoring the three
visible primes' distinctness generates the already-closed repeated-visible
third populations. Excluding a hidden prime equal to a visible prime
generates the already-closed higher-multiplicity fifth populations.
PNT errors in the aggregated expression are o(1) by the bounded-gate
sixth-norm lemma, not by wordwise discrepancy times an uncontrolled sum.
Thus (5) is a valid conditional reduction, not a new unconditional bound
on Q3. The same gate is coercive even after adding c3 Y^3; it does not
require the desired numerical upper bound as a premise.

In particular,

    c3 D3-A Q3
      =tau[(c3 I-5A D)Y^3]-5A*tau[V(Y)Y^2]+o(1).           (6)

This is actual phase-compatible grouping. It does not imply a saving.
Indeed D>=I/6: its beta-diagonal contribution is I/6 and its independent
alpha contribution is E(H_alpha^2)>=0. Hence

    c3 I-5A D <= (c3-5A/6)I,
    c3-5A/6=-20362931/69562500<0.

But Y^3 is indefinite. V is completely positive, yet V(Y) need not be
positive. Neither trace in (6) has a certified favorable sign.
For the ALL-ZERO displacement subpopulation the conditional paired
coefficient is 1/6 and the compatible coefficient becomes exactly
c3-10A/6=-147397637/139125000. It is not c3, and it is not a bound
on the other paths. Replacing (5) by 10*tau(D Y^3) fails for explicit
noncommuting rational matrices in the independent replay.

Warning: doing the analogous unrestricted four-visible-slot restoration in
Q4 also generates the non-negligible triple-pair population. No positivity
of an unrestricted sixth polynomial Hessian is a proved positivity theorem
for the distinct-visible Q4 population. Pair6 is not removed here.

## 6. Hostile sign-method falsifier with the first two moments fixed

This is a Loewner-FORM diagnostic, NOT invented source prime data.
Take alpha=0 and diagonal Y with repeating beta=(1,-1/3,-1/3,-1/3)
on longer contiguous sections. It has mean 0 and second moment 1/3 exactly
on multiples of four. Its third moment is 2/9. Negating beta preserves the
first two moments and reverses (6). All 6000 bands of the AUXILIARY W are
retained; only Y is diagonal in this sign-method test.

The cyclic average of beta_i^2 beta_(i+r) is 2/9 for r=0 mod 4 and
-2/27 otherwise. With H_R=sum_(r<=R)r^-2, boundary terms vanish for fixed R:

    tau(D Y^3) -> (1/6+H_R/pi^2)*(2/9),
    tau(V(Y)Y^2) -> 1/27+(1/pi^2)*sum_(r<=R) a_r/r^2
                  >=1/27-(2/27)*(1/6)=2/81.

Using H_R/pi^2<1/6, the grouped cubic for this Y is at most
(2/9)c3-(25/81)A<0. Its negation has a strictly positive grouped cubic.
This falsifies a universal favorable sign deduction from covariance,
centering, variance, or coefficient negativity alone. It does not falsify
the proposed inequality for the actual prime matrix. No synthetic rows
enter an arithmetic estimate or a certificate of zeta moments.

## 7. Remaining ledger and first missing estimate

Let H3* be c3 D3-A Q3 after (4), the old mixed central removal, and all
exact aliases. Both cubic families now need only

* mixed U>N, |log(U/V)|>1, with approximate first aliases and all tails;
* same-sign U>N^2, with approximate second aliases and all tails.

These descriptions keep the original full prime cutoff and signed path
weights. Define Fother*=-A D5+B(D6+Q4) after the prior eight central
removals (avoid double-removing Q3's central terms). The sharp remaining
joint estimate is

    limsup Re[H3*+Fother*]
       <= Jcap-B*Pair6_6000-kappa-eta.                     (7)

All new removals pay o(1); their positive-magnitude negative saving is ZERO.
Thus (2), gnew, and every consumer coefficient remain unchanged. Equation
(6) is algebraic redistribution, not an additional variance credit.

If a separate same-section theorem gives limsup(-A mu5+B mu6)<=H,
the weakest separate sufficient third upper bound is
(Jcap-H-kappa-eta)/c3. At the UNPROVED reference H=-A/36+B*(34/135),
kappa=eta=0 gives the boundary
8558084052085891/43411664130988764996=0.00019713789423651305...;
a strict positive gap must still be reserved. With H unknown there is no
independent numerical third ceiling sufficient to close the consumer.

The first new unresolved arithmetic step is a one-sided bound on the
remaining high-product cubic sums, or directly on (7). For same signs,
u~X^2 at the second alias has coherent grid window |u-X^2|=O(X);
the elementary representation bound allows O(X) integers of weight O(1/X),
so gives only O(1), not o(1). Mixed aliases have U~XV and windows O(V).
Exact-alias sparsity does not control either neighborhood. Far tails retain
their signed kernel and cannot be discarded by localization. The generic
length-N^3 mean-value majorant N^(3/2)/T diverges at this cutoff.
These facts explain failure of the CURRENT PNT/divisor/Hilbert estimates;
they are not a counterexample or an impossibility theorem for number theory.
No existing source-matched theorem here supplies the joint signed saving.
Short-interval counting alone would not establish its favorable sign.

Prime-to-Weil identification, bounded-gate proper-power equivalence and
same-section high-moment transfer, the frozen band interface, and zero-side
block/tail/count transfer remain visible dependencies. Only the ordinary
source first/second moments and the new absolute population removals above
are unconditional within the stated source normalization. No GUE, selector,
rank, model-moment, or unconditional zero theorem is promoted.

## 8. Reproduction

Run Python 3 standard library only:

    python src/wp84_joint_cubic_alias_audit.py
    python src/wp84_joint_cubic_alias_replay.py
    python src/wp84_third_aware_margin_replay.py
    python src/wp84_referee_foundations_replay.py

The new producer emits WP84_JOINT_CUBIC_ALIAS_CERTIFICATE.json. The independent
replay imports no producer; it squares the frozen consumer, recomputes the
improved budget, enumerates all 10 pair placements, checks the noncommutative
trace identity, enumerates exact cubic alias rational classes and six-fold
same-sign representations, verifies the periodic diagnostic, and rejects
seven hostile mutations. These exact finite tests supplement the proofs
above; they do not certify an asymptotic prime estimate by finite data.
