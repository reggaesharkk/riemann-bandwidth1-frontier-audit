# Strict >79: global collision removals and existential-section transfer

Input research/verified backup commit:
`be82c32cc00fce6d1c880ee5a4fe4a1300a194d1`.
Branch `codex/c5-c6-attack-20261006`; 2026-10-08. Local additive audit only.
No push, merge, history rewrite, main change, or notebooklm_packet change.

**New proved reductions:** additional complete ordinary-prime equality-pattern
sums are o(1), including their unsplit alias tails; and a strict signed sextic
bound on the canonical full band matrix transfers to a common existential good
section with o(1) loss. **Inequality (12) itself remains OPEN.** These are
arithmetic mean-value and spectral estimates, not functional-rank compression.
No nonzero determinant, source-legal P_B, or new analytic rank is asserted.

## 1. Dependency audit: inequality (12) does not consume the rank programme

The exact consumer is the one in WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE, with

    A=11501/12500, B=137641/250000, R=6000,
    Jstar=64788151489666079/572357731837500000.

Its centered fourth coefficient is zero. With the inherited common-section
lower moments, bounded full-to-band payment, normalization and zero-side
transfer, the required arithmetic input is

    limsup Re[-A N5(T,I,6000)+B N6(T,I,6000)]
          <= Jstar-B Pair6_6000-eta, eta>0.                (1)

Here N_b removes exact lambda=0 from the actual filtered b-word sum. A strict
gap gives the inherited simple-zero coefficient at least .79+2eta-o(1).
There is no reference to rank(453 functionals), K in 73->9->K, determinant
stencils, or a historical P_B in this implication. Those objects describe an
auxiliary finite-family route to estimates. They are not necessary premises
of the direct signed arithmetic theorem. Their unresolved status is preserved.

The direct theorem needs **an admissible common good section**, not a uniquely
specified historical selection algorithm. The existing linear-field endpoint
sampling theorem proves existence of endpoints in o(d) quarantine windows,
with their finite R-neighborhood scores bounded. One may combine finitely many
such scores and choose endpoints simultaneously. This does not identify any
historical row tuple and does not license synthesizing determinant rows.
Section 5 proves a sufficient route that works for *any* such small deletion
once a canonical full-section signed bound is available.

## 2. Exact full source object, powers, actual roots and aliases

Keep, without alteration,

    X=T/(2pi), L=log X, N=floor(exp(L-sqrt L)),
    h=2pi/L, d=floor(TL/(2pi)), I=[a,a+n-1], n/d->1,
    c_m=-Lambda(m)/(a_phi(T)*L*sqrt m), a_phi->1,
    m=p^v<=N, v>=1, s_m=log(m)/L.

For every ordered sign word eps and ordered closed displacement word ell,
|ell_j|<=6000, sum ell_j=0, set q_0=0, q_j=sum_(t<=j) ell_t,

    span=max q-min q, rho=max(0,n-span), i_min=a-min q,
    lambda=sum_j eps_j log(m_j),
    W=prod_j c_(m_j) f_(ell_j)^(eps_j)(s_(m_j))
         *exp(2pi i sum_j eps_j q_(j-1) s_(m_j)),
    K_(I,ell)(lambda)=exp(iT lambda+2pi i i_min lambda/L)/n
         *sum_(r=0)^(rho-1) exp(2pi i r lambda/L).          (2)

Use f_0^eps(s)=1-s, f_l^+(s)=(1-exp(2pi i l s))/(2pi i l),
f_l^-=conj(f_l^+) for nonzero l. The exact compressed hard-band moment is

    M_b^pow(T,I)=sum_eps sum_closed_ell sum_(m_1,...,m_b<=N)
                       W K_(I,ell)(lambda), b=5,6.        (3)

Thus the signed compressed residual, before any reduction, is
Re[-A(M5^pow-E5^pow)+B(M6^pow-E6^pow)], with E restricted to lambda=0.
The first-strike B_b uses the single-compression root kernel on the full I;
its difference from (3) is the existing *aggregate* boundary-path error
o(1) on good sections. Formula (2) is kept here so no frequency-masked
reprojection bound is presumed.

Nearest aliases are m_alias=floor(lambda/L+1/2) and
delta=lambda-m_alias L in [-L/2,L/2). Since i_min,r are integers,

    K_(I,ell)(m_alias L+delta)
      =exp(iT*m_alias L) exp(i(T+h*i_min)*delta)/n
           *sum_(r=0)^(rho-1) exp(i h r delta).            (4)

The nonperiodic carrier exp(iT*m_alias L) is retained. The sum includes every
sign population, exact and near aliases, all transition/far frequencies,
repeated primes and proper powers. There is no claimed localization to delta
near zero and no sign inferred from a sharp C5 overlap.

Proper powers are present in (3). The existing complete signed-gate theorem
allows (only at the level of a bounded complete signed gate) replacement of
the SAME matrix by its ordinary-prime part: for the power difference P,
||P||op=O_R(1), ||P||_(2,n)=O_R(L^-1), so ||P||_(6,n)=O_R(L^-1/3).
Coercivity and Schatten Holder then give the complete signed-polynomial
difference o(1) when either gate is bounded. This is reused, not a new
per-class or per-alias absolute disposal theorem. The argument also applies
on the canonical full section: the operator bound is global and the degree-two
sample estimate is uniform over contiguous intervals of length asymptotic d.
All powers remain explicitly accounted for by this aggregate equivalence.

For this canonical-section application, the uniform bounds can also be read
directly from the source: sum_(p^v<=N,v>=2)|c_(p^v)|=O(1) (squares use
sum_(p<=sqrt N)log p/p=O(L), higher powers converge), while their coefficient
second mass is O(L^-2). Finite-R row sums then bound ||P||op. The same
linear-field grid sampling argument used below, now at log(p^v) frequencies
with separation >=1/(N+1), bounds tau_n P^2 by O_R(L^-2). Interpolation gives
the stated S6 bound. Once one signed gate is bounded, coercivity bounds that
matrix's S6 norm and the triangle inequality bounds the other's. Telescoping
the fifth/sixth powers and normalized Holder bounds their complete moment
differences by O(||P||_(6,n))=o(1). No high-order masked power sum is estimated.

## 3. New global ordinary-prime collision theorem

After the preceding gate reduction, use ordinary primes only. Partition slots
by their exact prime equality pattern pi. Distinct prime blocks have
multiplicity nu_j and exponent e_j=sum of signs in that block. For a fixed
path each block has a separable coefficient a_j(p) satisfying

    |a_j(p)| <= |c_p|^(nu_j),
    Z_j(t)=sum_(p<=N) a_j(p) exp(i e_j t log p).           (5)

All filters and prefix phases remain inside a_j. They have modulus <=1 for
0<s<=log N/L<1. The factor c_p includes its original sign and normalization.
Deleting block-distinctness temporarily factors the root sum into the grid
average of product_j Z_j(t). Restoring it is exact partition-lattice
inclusion/exclusion. The merged blocks retain the original ordered slot
factors; they are not synthetic features or unrestricted divisor weights.

### 3.1 Uniform field bounds at the natural cutoff

Let M2=sum_p |c_p|^2=O(1). For nu>=3,

    sum_p |c_p|^nu = O(L^-nu),
    sum_p |c_p|^4 = O(L^-4).                              (6)

The sums over all integers of (log m)^nu/m^(nu/2) converge for nu>=3;
the prime bound is smaller. M2 follows from the source prime-square estimate.
No cancellation or prime cutoff shortening is used in (6).

For e!=0, real frequencies e log p have separation at least |e|/(N+1),
and |e log p|<=|e|L. Apply the real-frequency mean square and the source
disjoint-cell sampling inequality on rho grid points. If U=rho h~T,

    (1/rho) sum_roots |Z_j(T+h i)|^2
      <= 2(1+4pi^2 e_j^2)
           [1+2pi(N+1)/(|e_j|U)] sum_p |a_j(p)|^2.        (7)

The [Hilbert's Inequality, Theorem 2 and Corollary 2, pp. 74--75]
(https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
supplies the continuous bound; the cell inequality is proved in the existing
weighted reprojection note. Differentiation costs |e|L, and hL=2pi, which
explains the constant. The starting height and fixed prefix phases do not
change it. Since N/T->0, (7) is uniform on every relevant section/path.

Consequently a singleton block has bounded grid L2 norm O(1). A multiplicity-two
block with e=+-2 has grid L2 norm O(L^-2), despite being supported at frequencies
log(p^2). Its separation is governed by the prime parameter p, not the pooled
integer length N^2. A multiplicity-two block with e=0 is constant and bounded
by M2. Every multiplicity-two block has sup norm <=M2. This is the saving
missed by applying only the long-product mean value to the entire word.
Sampling includes aliases automatically; (7) is not a replacement of the
sampled kernel by a continuous trace.

A singleton alone also has small **signed mean**. For p<=N,
min(log p/L,1-log p/L)>=log 2/L eventually. The geometric sum and
|sin(pi s)|>=2 min(s,1-s) imply |K_(I,ell)(+-log p)|=O(1/T).
Together with sum_p |c_p|=O(sqrt N),

    |(1/n) sum_roots Z_singleton(T+h i)|=O(sqrt N/T).      (8)

This uses the complete natural prime interval, not a prescribed finite pool.

### 3.2 Classes removed without a thin-window assumption

If some nu>=3 and at most two blocks are singletons, take the large-multiplicity
field in sup norm using (6), all other nonsingletons in bounded sup norm,
and the at-most-two singleton fields in grid L2 using Cauchy--Schwarz.
The complete pattern sum is O_R(L^-nu)=o(1). This includes fifth shapes
{5},{4,1},{3,2},{3,1,1} and sixth shapes
{6},{5,1},{4,2},{4,1,1},{3,3},{3,2,1}.

For fifth shape {2,2,1}, if either pair has e!=0, use its O(L^-2) grid L2
norm, the singleton's bounded L2 norm, and the other pair's bounded sup norm.
If both pairs have e=0, their product is a constant and (8) applies to the
singleton. This removes the **complete** {2,2,1} contribution globally.

For sixth shape {2,2,2}, if any pair has e!=0, its grid L2 norm is O(L^-2)
and the other two fields are uniformly bounded. The complete distinct-base
contribution is o(1). If every pair has e=0, it is the exact three-pair
diagonal main term; it is kept.

All collision corrections required to restore block-distinctness remain
closed: merging creates a block of multiplicity >=3, with at most two
singletons remaining. For {2,2,1} and {2,2,2}, every nonidentity merge has
this property. For the earlier large-multiplicity cases, merging cannot
remove the large block or increase singleton count. Thus inclusion/exclusion
is justified term by term with the original coefficient factors. No unsupported
distinctness deletion occurs.

The total discarded noncentral sums are
O_R(L^-2+sqrt N/T)=o(1). They are **unsplit** equality-pattern sums.
This proof does not say that each separately frequency-masked near-alias,
central or far piece is small: those masks prevent the factorization in (5).
The previous near-alias-only no-singleton result remains valid in its own
scope; this theorem additionally removes the complete long tails by grid
mean square. Closed global classes are removed before any further alias split.

### 3.3 Remaining exact signed arithmetic object

Define S5(T,I) as (3) over ordinary primes and equality shapes

    {1,1,1,1,1}, {2,1,1,1},

and S6(T,I) over shapes

    {1,1,1,1,1,1}, {2,1,1,1,1}, {2,2,1,1}, {3,1,1,1}.    (9)

Every equality indicator is exact; all ordered signs/paths remain. These
shapes have singleton prime blocks, hence by unique factorization lambda!=0.
The exact three-pair main term D6(T,I,R), evaluated with the actual filters
and root counts, converges to Pair6_R by the existing *post-diagonal* PNT/BV
theorem. Coincident-pair bases were included in the discarded corrections.
Uniformly for n/d->1 at fixed R,

    M5^prime(T,I)=S5(T,I)+o(1),
    M6^prime(T,I)=Pair6_R+S6(T,I)+o(1).                   (10)

No filtered-to-sharp substitution enters (10). Pair6_R is the existing finite
filtered integral, not 131/420, 157/630, or 34/135. Exact nonzero aliases in
the surviving sums can additionally be removed by the existing absolute
O_R((1+L)^7 X^-1/2) bound. Near aliases and far terms remain in S5,S6.

The exhaustive ordered sign/equality census is:

|Degree|All classes|Globally o(1) classes|Exact three-pair main|Remaining arithmetic classes|
|---|---:|---:|---:|---:|
|5|52*32=1664|1312|0|352|
|6|203*64=12992|7688|120|5184|

The fifth removals comprise 832 large-multiplicity classes, 360 oscillatory-pair
classes and 120 constant-pair/singleton-mean classes. Sixth removals comprise
6848 large-multiplicity classes and 840 oscillatory-pair classes. These counts
concern raw ordered equality/sign patterns, not ranks, canonical orbit labels,
the prior 8740 surviving alias classes, or the 453-functional catalogue.
They are not claimed to be independent arithmetic inequalities.
Of the 7688 small sixth classes, 200 have all block exponents zero (180
of shape {4,2}, 20 of shape {6}); their small exact mass was already closed.
The other 7488 are noncentral. The new progress is the source-matched global
mean-value removal, especially oscillatory pair fields and large-multiplicity
fields multiplied by up to two singleton fields, not rediscovery of the
previous exact-diagonal or complete absolute-mass bounds.

For the fifth one-pair shape, every nonidentity merge is now closed. Its
distinctness constraints may therefore be removed *in the aggregate* with
o(1) error. For a balanced pair in slots a,b, its exact finite coefficient is

    C_ab(T,ell)=sum_(p<=N) c_p^2 f_(ell_a)^(eps_a)(s_p)
                    f_(ell_b)^(eps_b)(s_p)
                    exp(2pi i (eps_a q_(a-1)+eps_b q_(b-1))s_p).

Its remaining value is C_ab times the actual three-singleton field product
averaged over the same roots, plus o(1). If the pair has equal signs, retain
the oscillatory pair field Z_pair(t) instead. The hidden-prime pool is full.
Replacing C_ab by its PNT limit is **not** yet justified against an uncontrolled
triple correlation. Nor does scalar mu3=o(1) erase these differently weighted
triple correlations. This isolates a real missing interface without introducing
jets, moments S2..S10, or determinant-visible K.

## 4. What is the earliest missing arithmetic estimate now?

Within the first-strike note's inherited lower-moment/source assumptions,
the high-order debt is precisely

    limsup Re[-A S5(T,I)+B S6(T,I)]
           <= Jstar-B Pair6_6000-eta.                    (11)

Equations (9)--(10) have fewer genuinely uncontrolled arithmetic populations
than the starting residual, with zero limiting charge for the newly removed
ones. No favorable signed contribution of the survivors is proved. In
particular the fifth model 1/36 cannot come from ordinary exact equality,
and the sixth connected model constants are not additional exact prime types.
The remaining estimate must preserve signs, carriers, near aliases and tails.

The wordwise smaller-side spacing bound O(N/T) in the old sign-balance note
does not itself bound an aggregate prime-weighted third moment. Summing it
against unrestricted singleton l1 weights is unjustified. The fixed-R transfer
audit already treats scalar mu3 as an inherited conditional input at the
natural cutoff. This run does not newly prove that input. Thus a complete
unconditional >79 claim also requires a genuinely matched lower-third theorem
and the inherited source/zero-side obligations. The weighted triple family
above needs more than a scalar third-moment statement even if that scalar
statement is granted.

Second mass, PNT on prime-square measures, exact aliases, and the new repeated-base
estimates do not bound the surviving all-singleton long correlations. The
ordinary high-product mean values retain losses N^(5/2)/T and N^3/T at this
cutoff, up to fixed logarithmic factors. Shortening N would change the theorem
and the fifth arithmetic target, so it is not used. No public additive comb,
sharp continuum value, or fabricated root/evaluation rule discharges (11).

## 5. New one-sided good-section theorem from the canonical full matrix

This provides a selector-free sufficient arithmetic target with a proof of
compatibility with the required endpoint choice. Let Y be the actual ordinary
prime hard-band Hermitian matrix on I0={0,...,d-1}, and set

    J_d(Y)=-A tau_d(Y^5)+B tau_d(Y^6),
    ||Y||_(p,d)=(tau_d |Y|^p)^(1/p).

There is no arbitrary global operator-norm assumption. Put

    t0=5A/(3B), C=(A/6)t0^5.

For x>=0, with z=x/t0,

    B x^6-A x^5 -(B/2)x^6+C
      =C(5z^6-6z^5+1)
      =C(z-1)^2(5z^4+4z^3+3z^2+2z+1)>=0.

For x<0 positivity follows directly from -A x^5>0. Hence

    g(x)=B x^6-A x^5 >= (B/2)|x|^6-C,
    ||Y||_(6,d)^6 <= 2(J_d(Y)+C)/B.                      (12)

Suppose the canonical signed gate is bounded above, as it would be under
the desired strict bound. Then ||Y||_(6,d)=O(1). Let P compress to any
n=d-r dimensional section, and let Z=PYP embedded with zero rows in d
dimensions. Exactly,

    rank(Y-Z)<=2r, ||Z||_(6,d)<=||Y||_(6,d),
    ||Y-Z||_(6,d)<=2||Y||_(6,d).

For 1<=b<=5 telescope Y^b-Z^b into b ordered words with one Y-Z factor.
Apply Schatten Holder with that factor in p=6/(7-b), and the other b-1
factors in S6. The normalized finite-rank norm inequality gives

    |tau_d(Y^b-Z^b)|
      <=2b ||Y||_(6,d)^b (2r/d)^((6-b)/6).              (13)

For b=6, positive even-power compression gives instead
tau_d Z^6<=tau_d Y^6, which is the favorable one-sided direction. Thus

    J_n(Y_I)
      <=(d/n)[J_d(Y)+10A ||Y||_(6,d)^5 (2r/d)^(1/6)].    (14)

With r/d=O(L^-1/2), the additional term is O(L^-1/12)=o(1) and d/n=1+o(1).
This proves upper-gate transport; it does **not** claim two-sided sixth-moment
stability. Fifth and lower moments are stable here because of the newly
identified bounded sixth mass, not because rank-small deletion alone controls
raw moments. Formula (13) also transfers canonical lower moments 1,2,3 when
their source-matched full-section estimates are available.

Consequently the stronger, unambiguous sufficient arithmetic theorem is

    limsup Re[-A S5(T,I0)+B S6(T,I0)]
          <=Jstar-B Pair6_6000-eta, eta>0.                (15)

If (15) is proved, (10) bounds the canonical ordinary J, the complete proper-power
equivalence bounds the canonical full-power J, and (12)--(14), applied to that
full-power matrix, transfer it to **any** common admissible good section chosen
by the existing endpoint mean-square argument. Aggregate A->B reprojection
then yields the original first-strike inequality (12), with the same limiting
gap. This requires no historical endpoint selector and no P_B invariant kernel.
There is no converse assertion: a special good-section bound might hold even
if the full-section upper gate fails.

The new sufficient theorem has a canonical, fully specified evaluation
domain and preserves all natural arithmetic data. It does not invent a source
selector: it starts with the already existing full matrix and only afterwards
uses a proved existential compression. No determinant optimization is resumed.

## 6. Payments, falsifier checks, and what is actually certified

The existing payments remain exactly

    e_band=128952763/92407500000,
    e_var=26060119/12734908593750,
    M=52897896569489/572357731837500000.

They are already in Jstar. Global collision removal, exact alias disposal,
post-diagonal PNT, proper-power gate equivalence, conditional section transfer
and good-section weighted reprojection have limiting charge zero in their
stated scopes. These are successive reductions, not separate copies of a
masked error payment. No filtered-to-sharp error is introduced or waived.

The proof refuses the following shortcuts:
* replacing the actual geometric root sum by a continuous time average;
* applying global factorization after an alias/far mask has coupled prime blocks;
* inferring a triple tensor bound from one scalar third trace;
* replacing exact finite pair features by a sharp C6 constant;
* treating a bounded sixth norm as available before the signed gate is bounded;
* inferring two-sided sixth stability from a rank-small compression;
* changing N, R, slot order, prime pool, a_phi, roots, or historical row data.

Producer `src/wp84_strict79_source_matched_reduction.py` creates the exact
constants and complete equality/sign census. Independent replay
`src/wp84_strict79_source_matched_replay.py` imports none of that producer.
It enumerates restricted-growth equality words independently, checks all
14,656 classifications and all 37,224 block-coarsening corrections for the
discarded patterns, checks exact coercivity factorization and Holder exponents,
and reconstructs the signed consumer budget. Thirteen hostile metadata
mutations are rejected. Every pinned source and packet byte hash is checked.
No shortened prime pool, toy row, numerical phase sample or Monte Carlo is used.
The analytic estimates are the proofs above; finite enumeration does not
pretend to verify (11) or (15) numerically.

|Result|Status|
|---|---|
|Additional full-pattern global removals, (6)--(10)|PROVED at the natural cutoff, all aliases included in the unsplit sums|
|Bounded signed gate implies sixth mass and one-sided section transport, (12)--(14)|PROVED finite spectral inequalities; arithmetic gate remains a premise|
|Exact filtered three-pair diagonal|REUSED CLOSED reduction after unique factorization|
|Complete proper-power signed-gate equivalence|REUSED CLOSED aggregate theorem; no per-mask claim|
|Canonical sufficient arithmetic target (15)|OPEN|
|Inherited scalar lower-third/source/zero-side inputs|CONDITIONAL as stated in the first-strike chain; not newly discharged|
|Inequality (12) of the first-strike note and strict >79|OPEN|

The genuinely smaller missing high-order estimate is now the actual signed
sum over (9), on I0 if using (15), with its full sampled kernel. Nothing in
this audit proves the required favorable gain. Existing rank bounds, K,
determinant coefficients, legal minors and packet contents are preserved.
