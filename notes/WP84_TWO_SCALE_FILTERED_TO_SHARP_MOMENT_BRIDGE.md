# WP84 — two-scale filtered-to-sharp bridge and arithmetic boundary

Date: 2026-10-07. Parent: d629e53730058f1c13c97fcc0be10ef09cf40386.

Status: **CLOSED variable-R algebra and uniform continuum word convergence;
OPEN fixed-R fifth/sixth arithmetic continuum transfer; CONDITIONAL two-scale
moment and >79 assembly.** No source/model moment is promoted to a zeta moment.

## 1. CLOSED: arbitrary fixed positive integer R budget

Independently expanding the centered cubic square gives c4=0,
c5=-11501/12500, c6=137641/250000, c2=-26060119/430128125.
Let Erob=240421959557/2322691875000, pi_lo=333/106 and
Cband=128952763/15401250. The residual below 21/200 is exactly

    M(R)=21/200-Erob-[Cband+2|c2|/pi_lo^2]/R
        =1730343659/1161345937500-284757804319/(33959756250 R).

Thus the high-moment error gate is

    (11501/12500) eps5+(137641/250000) eps6 < M(R).

M(6000)=52897896569489/572357731837500000. Its limit is
1730343659/1161345937500, approximately 0.001489946796322263.
M(5627)<=0<M(5628), so the first positive integer is exactly 5628.
The independent sixth-model slack is

    34/135-157/630=1/378.

These statements are CLOSED algebra. The lower-moment, functional-band and
zero-side hypotheses remain necessary when using this budget as a theorem.

## 2. Four distinct objects, same selected Fourier section

Use the normalization of WP84_FIXED_BAND_WEIGHTED_REPROJECTION:
L~log T, d=floor(TL/(2pi)), h=2pi/L, a_phi->1, and
c_n=-Lambda(n)/(a_phi L sqrt(n)), n<=N<=exp(L).
Let U_y be the sharp partial translation on [0,L], V_y,R its infinite
Fourier-displacement filter, and define the infinite band operator

    S_T,R=sum_(n<=N, epsilon=+,-) c_n exp(i epsilon T log n) V_(epsilon log n,R).

For the good section I=[k_-,k_+], length d', define the PRIME moments

    A_b,T,R=d'^-1 tr((P_I S_T,R P_I)^b),
    B_b,T,R=d'^-1 tr(P_I S_T,R^b P_I), b=5,6.

A is the actual repeatedly compressed PRIME part of the centered matrix.
Identification with the centered zeta matrix also requires the scalar/ramp
reductions in this normalization; it is not part of the A->B proof.

For a tuple put s_j=epsilon_j log(n_j)/L and S=sum_j s_j. Then exactly

    B_b,T,R=sum_(tuples) product_j c_(n_j) exp(i T L S)
             exp(2pi i k_- S) D_d'(S) Omega_b,R(s).

Here D_d'(S)=d'^-1 sum_(k=0)^(d'-1) exp(2pi i k S), and Omega is the
periodic filtered overlap on the unit circle, including its wrap sectors.

C_b,R denotes a proposed FILTERED MODEL moment: start from an explicit
continuum/model signed-measure ledger, and replace its interval overlaps by
Omega_b,R, including every merged-word overlap in its cumulant expansion.
D_b denotes the corresponding sharp model moment. The frozen sharp values
are D5=1/36 and D6=157/630. This defines a geometric model operation; it does
not define a limit of B or prove B->C. A fully normalized arithmetic measure
ledger for B5/B6 is not supplied by the cited prime-measure notes.

There is another identification to check when constructing that ledger:
Fourier-displacement filtering is linear but not multiplicative. Filtering
a merged sharp translation is not generally the product of the individually
filtered translations. Either construction has the uniform geometric limit
proved below, but they need not define the same finite-R C. The arithmetic
derivation must specify which interval factors are actually produced; it
cannot justify a finite-R cumulant formula merely by substituting filters
into an existing sharp formula.

Diagram (arrows and their evidence are separate):

    actual centered zeta moment -> A_b,T,R -> B_b,T,R -> C_b,R -> D_b
                  CONDITIONAL       CLOSED       OPEN      see Sections 5–6

## 3. CLOSED: what A->B actually proves

The previous commit proves, for every fixed R, on ONE common selected section,

    |A_b,T,R-B_b,T,R| <= 4bR K_R^b/d', b=5,6,

where K_R=O_R(1). Its hypotheses include bounded coefficient second mass and
N/(qh)->0, with q=floor(d/sqrt(L)). The adaptive range
N<=T exp(-sqrt(L)+o(1)) suffices. The endpoints are selected using linear
alpha/beta fields in neighborhoods of radius 12R. No global sixth-moment
bound, no coefficient l1 sum, and no original-section raw moment stability
is proved. Constants can be arbitrarily large in R, which is fixed FIRST.

## 4. OPEN: exact obstruction to B->C

WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE proves BV testing of the one-prime
measure L^-2 sum_p (log p)^2/p delta_(log p/L) against s ds. Its product
version transfers exact pair sectors after those sectors have been derived.
WP71_PRIME_MEASURE_CONTINUUM_TRANSFER similarly starts with an ALREADY
REDUCED Lambda(n)/n product measure and expressly leaves its spectral
mass/bridge interface open. Neither transfers a signed high-product
near-collision measure from the tuple expression in Section 2.

Even though Omega_b,R has fixed-R bounded variation, the complete tuple test
also contains exp(i T L S) D_d'(S). Differentiating this factor has the
scale T L+d', of order T L; a direct BV-discrepancy estimate consequently
offers no o(1) bound. Kernel regularity is not the regularity of the complete
arithmetic test. Exact pair reduction removes this oscillation on S=0;
near-product sectors require a separate signed argument.

The obstruction persists even at R=0. The diagonal field is

    beta_k=2 Re sum_n w_n exp(i(T+hk)log n), w_n=c_n(1-log n/L).

Define a_r(u)=sum_(n1...nr=u) product_j w_(nj), with a_0(1)=1.
The entire diagonal contribution is EXACTLY

    d'^-1 sum_(k in I) beta_k^b
      =sum_(r=0)^b binom(b,r) sum_(u,v)
         a_r(u) a_(b-r)(v) exp(i T log(u/v))
         exp(2pi i k_- log(u/v)/L) D_d'(log(u/v)/L).

Real weights are used here. For complex weights the negative-side
coefficient is conjugated. This formula is not itself the whole B for R>0;
it exhibits an unsuppressed high-product sector in the retained operator.

Near u=v, |log(u/v)|<=O(1/T), the Dirichlet factor can be order one.
The fifth degree has hard 2-vs-3 sectors; the sixth has 2-vs-4 and 3-vs-3
sectors, besides the sign populations with smaller side zero or one.
Product support reaches N^2 and N^3. N/T->0 does NOT imply N^2/T or N^3/T->0.
The smallest generic product-frequency spacing is of order N^-3.
Montgomery--Vaughan applied to a cubic product polynomial therefore gives
a normalized bound containing N^3/T, which diverges at the retained range.
This is failure of a proposed estimate, not falsification of convergence.

The Fourier grid also has aliases at log(u/v)/L near nonzero integers.
Filtering removes the sharp no-wrap support restriction. These sectors must
be included in any arithmetic bridge; smoothness of Omega alone does not
remove the T-dependent Dirichlet/carrier kernel.

Multiplicity ledger:

| Class | Evidence and remaining obligation |
| --- | --- |
| Exact ordinary-prime equality at degree 5 | CLOSED: impossible with an odd total of prime factors; contribution zero |
| Exact degree-6 ordinary equality | CLOSED: equal triples give the pair permutations; repeated prime bases have vanishing normalized mass |
| Coincident primes in the already paired measure | CLOSED: sum_p |c_p|^4=O(L^-4); bounded fixed-R tests preserve negligibility |
| Proper powers in a linear or paired measure | CLOSED: squared mass O(L^-2) |
| Exact balanced equalities with proper powers | CLOSED: any non-pair prime-base group has total exponent >2 and an absolutely convergent p^-exponent/2 sum, with a negative power of L |
| Nonexact tuples with proper powers or repeated bases | OPEN: second mass alone does not bound the fifth/sixth multilinear sums |
| Nonexact ordinary 2-vs-3 / 2-vs-4 / 3-vs-3 | OPEN: weighted signed product-correlation transfer including selected-section carriers |
| Same-sign / smaller population one, aggregated at degrees 5/6 | OPEN here: individual word spacing is not an aggregate estimate; periodic wrap sectors also require control |
| Carrier-2T current-prime D2 | CLOSED only in the stated bounded-resolvent setting; high-degree raw polynomial states are not covered |

For the exact-equality claims, group tuples by prime base. A group has j
occurrences, exponent sum E, and weight at most (log p)^j/(L^j p^(E/2)).
Balance forces E even. The only leading group is j=E=2, two ordinary
opposite-sign primes. Every other group has E>=4, and its prime sum converges
absolutely. There are finitely many group patterns at fixed degree. This
proves the exact diagonal negligibilities, not nearby-product negligibility.

In particular the sharp fifth value 1/36 cannot follow from ordinary-prime
exact equalities alone. Nonexact arithmetic is load-bearing. A finite BV
kernel cannot replace the missing signed near-product-correlation theorem.

## 5. CLOSED: continuum word convergence, uniform in all interval shifts

Now set T aside. Work on the unit circle with normalized Lebesgue measure.
For any interval indicator f, including empty/full intervals, put f_R=F_R f.
The Fourier coefficient estimate gives

    ||f_R-f||_2 <= e_R=sqrt(2)/(pi sqrt(R)),
    ||f_R||_infinity <= L_R=1+2H_R/pi,
    ||f||_infinity <=1.

The second bound is direct coefficient l1 summation of ONE interval Fourier
series; no prime coefficient l1 sum is taken. Translates have the same bounds.
For k factors telescoping and normalized L1<=L2 give

    |integral product_(j=1)^k f_(j,R)(x+p_j) dx
      -integral product_(j=1)^k f_j(x+p_j) dx|
      <= w_k(R)=k e_R L_R^(k-1).

This is uniform over the interval parameters and prefixes, including periodic
wraps. Since H_R<=1+log R, w_k(R)=O_k(log^(k-1)(R)/sqrt(R))->0.
Each merged sharp word again supplies an interval indicator; the same proof
applies to any fixed finite merged-word or cumulant ledger.

For the anchored CONNECTED kernels alone the explicit uniform bounds are

    kappa5(R)=150*5*e_R*L_R^4,
    kappa6(R)=1082*6*e_R*L_R^5.

Term counts were independently enumerated in the new verifier. A term with
fewer factors obeys the corresponding larger b-factor bound. These are
kernel bounds, not yet fully normalized moment losses.

## 6. CLOSED abstract finite-measure theorem / CONDITIONAL model moment bridge

Suppose the complete sharp full-moment ledger is specified as

    D_b=sum_t integral K_t(v) dmu_t(v),

with fixed finite signed measures and W_b=sum_t ||mu_t||_TV<infinity,
all coefficients absorbed in the measures. Let C_b,R replace every interval
factor in that SAME ledger by its Fourier partial sum. If there are at most
2b interval factors in an expanded term (outer word plus merged/cumulant
words), the word proof gives the explicit bound

    |C_b,R-D_b| <= delta_b(R),
    delta_b(R)=2b W_b e_R L_R^(2b-1), b=5,6.

More generally replace 2b by the actual finite maximum number of factors.
This finite-measure theorem is CLOSED and independent of T. Applying it to
the complete proposed normalized model is CONDITIONAL on exhibiting that
ledger and its W_b. The 150/1082 connected term counts alone do not specify
full-moment measures: sixth degree also has {4,2}, {3,3}, {2,2,2}, and fifth
degree may have a filtered {3,2} term even though its sharp value vanishes.
They cannot be silently omitted before filtering. These extra finitely many
terms also converge once the same model ledger is fixed.

Thus geometric filtering is not the enduring two-scale obstruction. The
unproved arithmetic B->C and its normalization are. No numerical delta5 or
delta6 for the actual zeta moments is certified by these kernel estimates.

## 7. CONDITIONAL: the requested epsilon argument

IF B_b,T,R=C_b,R+o_T(1) for each fixed R on the selected section, and IF the
complete model ledger in Section 6 has the frozen values D5,D6, then choose
ONE finite R with

    delta6(R)<1/378,
    (11501/12500)delta5(R)<M(R).

Such R exists because both deltas tend to zero and M(R) tends to a positive
rational. Strict inequalities leave positive room for all o_T(1) errors.
Only after fixing this R take T sufficiently large. Set eps5=delta5(R),
eps6=0 in the limiting budget, using the strict sixth slack. This proves the
arithmetic gate CONDITIONALLY on the missing arrows and lower moments.
It is not a proof that any R currently works for the actual prime state.
No R(T) is used.

## 8. Selected section and bounded zero transfer

For any fixed large R, the 12R endpoint neighborhoods remain finite. Their
mean-square score is O_R(1), while at most 2q=O(d/sqrt(L)) rows are removed.
Embedding the selected section with zero rows changes a Hermitian matrix by
rank at most twice the number removed. For the fixed rational bounded
consumer, bounded-variation rank comparison and normalization correction
cost O(q/d)=o_T(1). Its variation is finite because it is rational with no
real poles and finite limits at infinity. None of this requires R=6000.
It does not imply stability of the original raw fifth/sixth moments.

The functional band charge is Cband/R for the same consumer and any fixed R,
under the source assumptions in WP84_FUNCTIONAL_BAND_THEOREM_DELTA80 and
the robust cubic note. The zero-side count stays attached to the FULL matrix.
WP84_R400_ZERO_SIDE_TRANSFER_SOURCE_AUDIT_2026_10_06 explicitly corrects the
feature normalization to hat(phi)/(sqrt(a_phi) L) and preserves a conditional
prime-side boundary. This audit checks R-independence and rank costs; it does
not independently re-prove that complete analytic zero-side chain.
Selected-section lower moments and the full centered-zeta/prime identification
must be audited in the same normalization before theorem promotion.

## 9. Preserved structural diagnostics and evidence boundary

The exact C5 supercritical sign theorem and mixed-sign C6 witnesses are
unchanged. Under a future CLOSED two-scale full-moment transfer their signs
would be non-load-bearing diagnostics for this >79 argument. That relabeling
is presently CONDITIONAL because the full transfer remains OPEN.

CLOSED: variable-R rational gate, sixth slack, A->B on selected sections,
uniform filtered-word convergence, abstract finite-model-ledger convergence,
fixed-R endpoint rank cost.

OPEN: normalized high-product arithmetic B5/B6->C5/C6, high-degree nonexact
proper-power/alias estimates, selected lower-moment/common-normalization audit.

CONDITIONAL: finite-R full-moment closure and the arithmetic >79 gate.
No unconditional >79 result is claimed. Parent commit is preserved; no push,
merge, rebase or modification of main/Downloads is performed.
