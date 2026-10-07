# Signed near-alias attack: support reduction and the smaller missing lemma

Date: 2026-10-08. Parent: 72b4775f2833f105b4513f97bd4350ee8a0f8ecf.
Branch: codex/c5-c6-attack-20261006. Worktree:
C:/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit.
Local only; no push. Prior audits and the 9,216 exponent boxes are frozen.

**C. NEAR-ALIAS REDUCES TO ONE EXPLICIT NEW SMALLER LEMMA.** Three pattern
families close with limiting charge zero: one active prime block; no singleton
prime blocks; one-sided residual product at |m|=1. The survivor lemma below
is NOT proved. No survivor charge is invented. Strict >79 remains OPEN.
This is a proper-subset reduction, not a unique-hardest-subcase claim or
hardness equivalence to the frozen central theorem. No consumer, central,
physical-mask, Gaussian, SOS, mu7/mu8 or higher-moment work is reopened.

## 1. Exact normalized near-alias sum

Keep X=T/(2pi), L=log X, N=floor(exp(L-sqrt(L))), a_phi->1,
d=floor(TL/(2pi)), selected I=[k_-,k_+], d'=|I|<=d, d'/d->1.
For ordinary p<=N let alpha_p=log p/L, c_p=-log p/(a_phi L sqrt p),
f0^eps=1-alpha, f_l^+=(1-exp(2pi*i*l*alpha))/(2pi*i*l),
f_l^-=conj(f_l^+). Consumer weights remain omega5=-A=-11501/12500,
omega6=B=137641/250000. R=6000 is fixed; H is a separate frequency cutoff.

For every ordered sign placement eps, closed path |l_j|<=R, sum l_j=0,
u0=0, uj=sum_(t<=j)l_t, retain

    i_min=k_- -min uj, i_max=k_+ -max uj,
    M_l=max(0,d'-(max uj-min uj)),
    P=product_positive p_j, Q=product_negative p_j,
    lambda=log(P/Q), m=floor(lambda/L+1/2),
    delta=lambda-mL in [-L/2,L/2),
    W=chi product_j c_(p_j) f_(l_j)^(eps_j)(alpha_(p_j))
                   exp(2pi*i*sum_j eps_j*u_(j-1)*alpha_(p_j)),
    K_l(lambda)=exp(i*T*lambda) exp(2pi*i*i_min*lambda/L)
                 /d' sum_(k=0..M_l-1)exp(2pi*i*k*lambda/L).      (1)

Chi retains every original prime window, equality and coprimality mask.
The unpartitioned trace includes repeated primes. No continuum or sharp
substitution occurs. Actual root counts remain; aggregate reprojection does
not license replacing roots independently on a frequency mask.

For a=H/T<L/2, H fixed positive or declared subpower H=X^o(1), exactly

    Q_T(H)=sum_(b=5,6) sum_eps sum_closed_l sum_ordinary_tuples
             omega_b W K_l(lambda) 1_(m!=0,0<|delta|<=H/T).      (2)

Use the frozen remaining tuple set: prior short-cell removals keep their
original scope; EXACT nonzero aliases delta=0 are excluded even at tuned
rational heights. Proper powers stay removed by the complete signed-gate
equivalence, not a new masked-TV assertion. Split (2) into m>0 and m<0
WITHOUT absolute values; m=0 is CENTRAL, outside this attack. There is no
extra 1/H or reciprocal shift count: normalization is 1/d' in (1).

## 2. Every factor-pattern support, including cancellation

With r positive and s=b-r negative slots,

    r log2-s logN<=lambda<=r logN-s log2.                       (3)

Asymptotic necessary nonzero core lists for subpower H are:

|b|r:s|possible m from product-size support|
|---|---|---|
|5|0:5|-4,-3,-2,-1|
|5|1:4|-3,-2,-1|
|5|2:3|-2,-1,1|
|5|3:2|-1,1,2|
|5|4:1|1,2,3|
|5|5:0|1,2,3,4|
|6|0:6|-5,-4,-3,-2,-1|
|6|1:5|-4,-3,-2,-1|
|6|2:4|-3,-2,-1,1|
|6|3:3|-2,-1,1,2|
|6|4:2|-1,1,2,3|
|6|5:1|1,2,3,4|
|6|6:0|1,2,3,4,5|

These are SUPPORT possibilities, not assertions that primes occupy the core.
For every ordered prime-equality partition pi, distinct prime blocks q_j have

    nu_j=slot multiplicity, e_j=sum of slot signs in block j,
    n_plus=sum max(e_j,0), n_minus=sum max(-e_j,0),
    lambda=sum e_j log q_j=log(U/V),
    U=product_(e_j>0)q_j^e_j, V=product_(e_j<0)q_j^(-e_j).       (4)

Common factors cancel in the PHASE exactly. The weight retains c_q^nu,
all filters, all path phases, block-distinctness, and intersected slot windows.
Balanced e=0 blocks remain in the weight. If every e=0, lambda=0 and the
nonzero alias sector is identically empty. Otherwise the pattern-specific
asymptotic list is

    m in {1-n_minus,...,n_plus-1}, m!=0.                       (5)

Proof: logN<=L-sqrt(L) gives lambda_max<=n_plus L-n_plus sqrt(L)
-n_minus log2 and the reciprocal lower bound. The extreme deficits exceed
H/T for all sufficiently large T. Empty-side log2 terms exclude spurious
zero cores. These support-empty classes are rigorously eliminated.

For EXACT finite-T support, take lambda_min,max over injective allowed-prime
assignments to blocks. Without windows, assuming pi(N)>=number of blocks,
rearrangement gives attained extrema: largest primes assigned to positive e
in descending coefficient order, smallest to negative e in descending absolute
coefficient order for the maximum; reverse for the minimum. Zero blocks use
unused primes. Too few primes means empty support. With windows, each block
uses the intersection of its slots' prime windows; exact extrema are a finite
injective assignment problem. The producer's mask dynamic program computes
min/max rational U/V, or returns empty when no matching exists.

The exact INTERVAL-SUPPORT core integers satisfy

    ceil((lambda_min-H/T)/L)<=m<=floor((lambda_max+H/T)/L), m!=0. (6)

Core intersection belongs to its nearest bin because H/T<L/2. Discrete
prime-product values can leave holes in this interval: (6) does not certify
occupancy. Actual occupancy is still the literal finite sum (2).

The CSV enumerates all 14,656 sign/equality patterns: 52*32 for fifth and
203*64 for sixth. It is separate from the FROZEN 9,216 exponent boxes. At
X=1000, natural N=72,H=10, it additionally records exact extrema and (6).
Producer logarithm intervals and independent exponential intersections certify
the same finite support lists. Arbitrary-window matching is checked separately.

## 3. Sharp multiplicative and integer displacement

For arbitrary real X^m the EXACT equivalence is

    X^m V exp(-a)<=U<=X^m V exp(a), U!=X^m V,
    X^m V(exp(-a)-1)<=U-X^m V<=X^m V(exp(a)-1).                (7)

Equivalently U exp(-a)<=X^m V<=U exp(a). The additive endpoints are
asymmetric. Its length is 2X^m V sinh(a)<=3X^m V a for 0<=a<=1.
If X^m=a0/b0 in lowest terms, the correct INTEGER shift is

    h=b0 U-a0 V!=0,
    a0 V(exp(-a)-1)<=h<=a0 V(exp(a)-1),
    h congruent to -a0 V modulo b0.                           (8)

For irrational X^m the displacement in (7) is real; an integer additive-shift
reduction needs an additional argument. For m<0 swap U,V, m to |m| and
delta to -delta, retaining its own weights. This does not delete that half.

The surviving all-distinct fifth example (.8,.8;.2,.2,.2) has
U~X^1.6,V~X^.6,m=1. At integer X the window in h=U-X V has width
O(H X^.6). It is a dilated unequal-length correlation, not the central
N_cell^1/6 equation. No hardness equivalence is asserted.

## 4. Three new CLOSED families, with proofs

Absolute values are taken only AFTER the exact block reduction. All proofs
retain the ordinary-prime weights. Their limiting charges are zero.

### 4.1 One active prime block

Exactly one e_j is nonzero, |e_j|=k. Its sign fixes m's sign, with
1<=|m|<=k-1; k=1 has no alias. The active prime is in

    X^(|m|/k) exp(-a/k)<=q<=X^(|m|/k) exp(a/k).                (9)

Length <=3H X^(|m|/k-1)/(2pi k). Because k<=6 and |m|<=k-1, subpower H
makes this <1 eventually. At most one integer prime can occur per m, including
tuned heights. Active multiplicity nu>=k gives, since alpha<=1,

    |c_q|^nu<=|a_phi|^-nu exp(nu*a/(2k)) X^(-nu|m|/(2k))
               =O(X^-1/2).                                 (10)

Every inactive block has balanced signs and nu>=2. Dropping its masks permits
sum_(p<=N)p^(-nu/2)<=1+logN. There are at most two such blocks when b<=6
and one active block is present. Filters and kernel have modulus <=1;
a_phi is bounded away from zero eventually. Finite fixed-R path/sign/pattern
sums therefore cost O_R((1+L)^3 X^-1/2)=o(1). This is uniform for a declared
subpower H, without any Diophantine assumption on T.

### 4.2 No singleton prime blocks

If every nu>=2 and at least one nu>=3, the COMPLETE absolute pattern mass is
o(1): S_nu=sum_p|c_p|^nu=O(L^-nu) for nu>=3, since
sum_p(log p)^nu/p^(nu/2) converges, while S2=O(1) by the frozen normalization.
Distinctness/windows only reduce mass. This concerns repeated ordinary-prime
leaves, not proper-power leaves.

The remaining case is b=6, three blocks each of multiplicity two. Define

    mu_T=sum_(p<=N)(log p)^2/(|a_phi|^2 L^2 p) delta_(log p/L),
    mu(dalpha)=alpha dalpha on [0,1],
    D_T=sup_x|mu_T([0,x])-mu([0,x])|->0.                       (11)

This is the existing PNT prime-square upgrade with natural cutoff and a_phi.
Continuous limiting CDF implies uniform CDF discrepancy. After EXACT block
reduction, the near-alias slab is |sum e_j alpha_j-m|<=w, w=H/(TL).
For nonzero e at least one |e_j|=2. Fixing other coordinates bounds the
limiting product mass by 2w/max|e_j|<=w. A product-measure telescope, each
one-coordinate interval indicator having variation at most two, gives

    actual slab mass<=2w/max|e_j|+2k D_T M^(k-1),              (12)
    k<=3, M=max(1,mu_T([0,1]),mu([0,1])).

Each integration replaces one measure; every conditional interval mass differs
by at most 2D_T (a difference of two CDF values), while other measures contribute
at most M^(k-1). Distinctness/windows
only decrease this unsigned upper bound. All phase factors have modulus one
and filters <=1. Finite m/path/sign sums tend to zero when H/(TL)->0.
All-zero e has no nonzero alias. PNT has been used only AFTER block/product
reduction on a genuine squared-prime measure, never on the singleton first
mass. Formula (12) is a quantitative bound in the existing discrepancy;
no numerical rate for D_T is invented.

### 4.3 One-sided reduced product at |m|=1

If nonzero e all have the same sign, take the reciprocal if necessary. At
|m|=1 the reduced INTEGER product n is in [X exp(-a),X exp(a)], length
<=3H/(2pi)<H. Thus at most H+1 integers occur. Each has at most
n_plus!<=6! ordinary ordered representations with the specified exponents.
The active weight is <=|a_phi|^-b n^-1/2, since nu_j>=|e_j|, and
n^-1/2<=2X^-1/2 for a<=1. Inactive balanced blocks are bounded as before.
The complete absolute contribution is

    O_R((H+1)(1+L)^3 X^-1/2)=o(1).                            (13)

This closes first aliases with singleton blocks too, but not higher one-sided
aliases. In all proofs fixed R permits finite constants; no bulk norm is added.

For disjoint reporting the classifier orders families: one-active, no-singleton,
then one-sided first alias. Counts are candidate (pattern,m) PAIRS, not prime
populations or masses:

|b|all pairs|one active|no singleton|one-sided first|survivors|
|---|---|---|---|---|---|
|5|2726|108|320|342|1956|
|6|26932|1036|3240|3024|19632|

8,070 candidate pairs are newly removed; 21,588 survive this support-level
classification. Frozen short-window closures can further restrict survivors.

## 5. Exact surviving signed correlation and energy

Let S_T be the surviving tuple set from (2), with all frozen removals. Put

    Q_T^hard(H)=sum_(S_T) omega_b W exp(i*T*mL)
                          exp(i*tau_(i_min)*delta) g_l(delta),
    g_l(delta)=1/d' sum_(k=0..M_l-1)exp(2pi*i*k*delta/L).

The new proofs establish

    Q_T(H)=Q_T^hard(H)+o(1).                                  (14)

All exact aliases remain excluded. This is a proper-subset reduction, not an
evaluation. Separable slot arrays are Dirichlet convolutions of the original
prime weights/filters; equality and coprimality masks require the labelled
tuple or block version, retaining all slot phases. The weakest ledger input
is a ONE-SIDED bound on Q_T^hard, not an unsigned solution count or energy.

For r ordinary-prime slots, unique factorization bounds ordered representations
by r!. Cauchy on each product representation set gives

    sum_n |A_r(n)|^2<=r! product_j sum_p|a_j(p)|^2.             (15)

For identical slots this is r! S2^r. The verifier uses the exact rational
regression a(p)=1/p, p in {2,3,5,7},r=3; the proof establishes the general
inequality. This is exact PRODUCT energy, not near-alias ratio energy.
Localized alias energy involves two tuples with ratio near X^m. Common-factor
cancellations mean ratio representations cannot all be bounded by r!s!.
Equation (15) does not give a localized signed bound. The prime-square proof
above cannot be extended to singleton first mass without additional input.

For a fixed ordered word/path with product supports n in [U,2U),v in [V,2V),
the previous valid dyadic first-mass bound is

    r!s! |a_phi|^-b [14H sqrt(UV)/T+
                                  sqrt(min(U,V)/max(U,V))].    (16)

Its integer-window proof uses pointwise prime weights, not merely l2 mass.
At U=X^1.6,V=X^.6, it permits H X^.1. Take its minimum with the exact
finite envelope and applicable frozen sampled row bound. No whole-survivor
small charge is thereby certified. Growth of an upper bound is not a lower
bound on the actual contribution.

## 6. True-height spacing and large-sieve audit

Within fixed m, distinct ratios have integer determinant UV'-U'V!=0, hence

    |log(U/V)-log(U'/V')|>=1/max(UV',U'V).                     (17)

Example heights are X^2.2, not X or X^1.2. Known separation can be X^-2.2
while the core radius is H/X. Spacing-only counting can allow
O(1+H X^1.2) distinct ratios. Rational X^m=a0/b0 gives integer h!=0 in (8)
and distance roughly >=1/(a0 V+b0 U), of size X^-1.6 at integer X,m=1
in the example. This too is below 1/T. Irrational X^m has no supplied uniform
Diophantine separation from product ratios.

|Tool|Actual hypothesis|Result/gap in surviving example|
|---|---|---|
|Continuous Montgomery-Vaughan|Time integral with length/gap and second-mass hypotheses|A sampled alias near lambda=mL is not a zero-frequency resonance in the continuous kernel; replacing sampling by an integral loses it|
|Frozen sampled Hilbert/row bound|Folded bins and prime coefficient controls|sqrt(UV)/T=X^.1 up to log factors; no vanishing charge|
|Additive large sieve|Modulo-one spacing delta/L|Normalized loss 1+1/(T*gap) may permit X^1.2 from (17); needs stronger local density or cancellation|
|Dual large sieve|The dual of the same frequency operator|Same gap/density loss; no new arithmetic input|
|Multiplicative/character large sieve|Character/modulus averaging with specified lengths|Our average is one time/root grid; no controlled conversion to that average supplied|
|Multiplicative energy|Exact product collision control|Does not count the dilated short-window correlations|

These are unavailable-saving diagnoses, not hardness lower bounds. Fixed R
and selected root counts supply finite constants, not an extra time average.
Using Hilbert without the folded spacing is not a valid alias estimate.

## 7. Signed primitive, cancellation and requirements for general H

Group survivors by kappa=(M_l,i_min,m,sigma), sigma=sign(delta),x=|delta|.
Combine omega5 and omega6 wherever kernel data match BEFORE absolute values:

    nu_kappa=sum_(tuples in group) omega_b W exp(i*T*mL)
                       exp(i*tau_(i_min)*sigma*x) delta_x,
    P_kappa(x)=nu_kappa((0,x]), 0<=x<=a=H/T,
    g_kappa(x)=1/d' sum_(k=0..M_l-1)exp(2pi*i*k*sigma*x/L).

Then exact Abel summation gives

    Q_T^hard=sum_kappa [g_kappa(a)P_kappa(a)
                          -integral_0^a P_kappa(x)g'_kappa(x)dx]. (18)

Exact aliases were removed, so P(0)=0. All prime windows, equality/coprimality
and consumer weights are inside P. No comparison main term is presumed.
For E_A(T,H)=sum_kappa sup_(0<=x<=H/T)|P_kappa(x)|,

    |Q_T^hard|<=E_A[1+pi*(d'-1)H/(LT)]<=E_A(1+H/2),           (19)

using |g'|<=pi M_l(M_l-1)/(d'L) and d'<=d<=TL/(2pi). This is sufficient
absolute control AFTER signed aggregation, not the weakest possible theorem.
A one-sided bound on (18) may be weaker.

Frozen reference allowances are

    Delta_I=27704610381502/17886179119921875
             =0.00154893955806605...,
    Delta_R=52897896569489/572357731837500000
             =0.00009242103954753147....

If the full respective allowance is assigned to aliases with reserve eta>0,
a sufficient primitive requirement is

    limsup E_A(T,H)<=(Delta_I-eta)/(1+H/2), or
    limsup E_A(T,H)<=(Delta_R-eta)/(1+H/2).                    (20)

H=400 gives multiplier 201 and UNRESERVED relaxed target
Delta_R/201=4.5980616690314163e-7. H=1 gives multiplier 3/2 and target
2Delta_R/3=6.161402636502098e-5. Exact rational targets are in JSON.
They are requirements, not obtained bounds. For example a half-allocation
requires Delta_R/[2(1+H/2)], leaving the other half for remaining excesses.

Conjugacy sends lambda to -lambda and pairs terms into 2 Re(z), not zero.
Insertion/sign orientation sums and zero total lag are already in W. There
are no new cumulant coefficients to subtract: the raw consumer weights are
-A and B. Different homogeneous degrees exclude a universal cancellation
identity solely from these two constants under arbitrary amplitude scaling.
No actual-prime survivor cancellation identity is proved. Fifth and sixth
errors are not separately charged again after they are combined in P.

## 8. What the H optimization rigorously says

H changes the sector partition, not Fourier R or the prime cutoff. Increasing
H enlarges alias and central cores and transfers the same annulus out of the
frozen tail. Signed sector values need not be monotone; unsigned alias mass
increases and unsigned tail mass decreases. The exact total is unchanged.
The permitted primitive threshold Delta/(1+H/2) strictly DECREASES in H.

Thus the near-requirement-only surrogate has supremum Delta as H->0+, no
attained positive optimizer. If an EXTRA range H>=1 is imposed, H=1 maximizes
the permitted primitive error. No H>=1 hypothesis is silently added here.
The script checks exact rational requirements at H=1/100,1,10,100,400,1000.
These statements are conditional optimization, not a feasible arithmetic H.

Normalization-only tail comparison, without reopening its attack: the prior
envelope is <=K(T)/H, where K(T)=LT/(2d') times a declared whole weighted
first-mass upper bound. If an H-independent primitive bound E0 were PROVED,
the surrogate E0(1+H/2)+K/H has minimum at

    H*=sqrt(2K/E0),                                          (21)

clipped to any specified admissible interval. Neither E0 nor a small K is
available; central's charge function is also unknown. The actual E_A depends
on H. Consequently there is NO certified numerical global optimum or feasible
H. Shrinking below all finite nonexact distances can empty aliases at a given
height, but shifts that debt to tails and has no uniform subpower guarantee
as T is tuned. This is not budget closure.

For the new lemma it suffices to declare ONE H0>0 beforehand, e.g. H0=1,
and require uniformity in T on the selected sections at fixed R,H0. Uniformity
over all H is stronger than necessary. A chosen subpower H(T) requires a
proof for THAT function; a fixed-H theorem cannot be substituted for it.

## 9. Exact prime decomposition on surviving blocks

On each DISTINCT ordinary prime block the scalar weight is

    (-1)^nu Lambda_ord(q)(log q)^(nu-1)
                     /(a_phi^nu L^nu q^(nu/2)),
    Lambda_ord=Lambda-E, E=Lambda on proper prime powers.

Block filters are original slot filters; block windows are their intersections.
Keep distinct block integer labels in the expansion. At U0=V0=X^1/20,
Vaughan's exact identity gives four terms plus compensation E per block:

    mu_(<=U0)*log;
    -mu_(<=U0)*1*Lambda_(<=V0);
    Lambda_(<=V0);
    mu_(>U0)*1*Lambda_(>V0); minus E.

For q~X^alpha, the corresponding lengths are:

- first Type I: a<=U0,b=q/a, coefficient mu(a)log b;
- second Type I: a<=U0,c<=V0,b=q/(ac), coefficient -mu(a)Lambda(c);
- short term: support alpha<=1/20 plus boundary;
- Type II: q=a t, a>U0,t>V0, coefficient mu(a)beta_V0(t),
  beta_V0(t)=sum_(c|t,c>V0)Lambda(c), 0<=beta<=log t;
- E compensation, retained exactly.

There are at most 5^k block-labelled choices before dyadic splitting. The
frozen Heath-Brown identity k_HB=3,z=ceil(N^(1/3)) gives three terms with
2j variables (j short mu, j-1 one, one log) and E per block: at most 4^k
choices. These identities do not themselves estimate the alias correlation.
Every piece retains e_j powers in the ratio, nu_j in the weight, block masks,
(7), and the sampled carrier. No new masked proper-power disposal is claimed.

For Type II a~M,t~Q, a valid squared rectangular block-norm bound is

    4(MQ)^(1-nu)(log(4MQ))^(2nu-2)(log(2Q))^2
                            /(|a_phi|^(2nu)L^(2nu)),

by sum |mu(a)|^2/a^nu<=2M^(1-nu), and the corresponding beta bound.
Grouped norms retain divisor collisions. In the distinct fifth example,
positive .8 slots can split .4+.4 and negative .2 slots .1+.1, yielding
four variables against six with dilation X. This is a retained piece, not
proven dominant. Reduced 1:2 and higher one-sided patterns also survive;
no uniquely hardest alias piece is identified.

## 10. Primary literature match AFTER this reduction

This is an alias-specific audit, not a restarted central search.

|Primary result|Stated hypotheses|First mismatch/payment|
|---|---|---|
|[Topacogullari, On a certain additive divisor problem](https://arxiv.org/pdf/1512.05770), Thm 1.1/1.2|Unrestricted d(r1 n+f1)d(r2 n+f2); integer coefficients, stated smooth/sharp weights and offsets|Rational aliases can clear to an affine equation, but our arrays are prime-window convolutions, not d2; irrational X^m has no exact integer clearing. No charge imported|
|[Evans, Correlations of Almost Primes](https://arxiv.org/pdf/2102.12297), Thm 1.1/1.3/1.4|E2/E2 or prime/E2 at n,n+h, almost all shifts in stated ranges, sometimes restricted small factor sizes|Unequal scales and dilation X^m, different prime windows and exceptional carrier-weighted shifts are uncontrolled. No charge imported|
|[Montgomery-Vaughan, Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)|Gap-weighted bilinear/mean-value control|Needs folded spacing; Section 6 gives the loss. No survivor budget estimate|

The closest affine divisor result's first mismatch is coefficient structure,
even in the rational case. Its smooth error for coprime r1,r2 is
(r2*x1)^(1/2+theta+epsilon), with stated small offsets. For fixed H and
integer X choose r1=X,r2=1,x1~X^1.6,x2~X^.6,f1=h~X^.6,f2=0.
Those size conditions can fit: rejecting it solely because r1 is large would
be incorrect. But prime-window coefficients still fail the theorem. A
hypothetical pointwise import at theta=7/64 costs X^(39/40) per h; dividing
by sqrt(x1*x2)=X^(11/10) and summing O(H X^3/5) shifts permits
H X^(19/40), not decay. This exponent is checked independently; no such
import is asserted for the actual arrays. A signed averaged estimate might
differ, but is not the cited theorem.

Evans distinguishes primes from divisors, but the additive equation and
factor ranges do not match our survivors. PNT gives marginal prime measures;
BV gives its stated AP discrepancies. Neither audited hypothesis supplies
this signed dilated-product estimate. This is a bounded applicability finding,
not a proof no future theorem or alternative regrouping can work.

## 11. Stronger soft-bound necessity test

The old soft norm example did not meet the pointwise envelope. This one
meets that envelope AND l2 bounds and uses the natural sampled grid. It is
still NOT prime-compatible.

For even z->infinity take X=z^5,T=2pi X,L=log X,V=z^3,U=XV=z^8,
K=floor(V/10000),H=1/100. Put a(n)=n^-1/2 on U<=n<2U and
b(v)=v^-1/2 on V<=v<2V, zero elsewhere; rotate a by exp(-i*T*L).
Both squared l2 norms are <=1 and the pointwise inverse-square-root envelope
holds exactly. These are divisor-bounded soft weights.

All core ratios have nearest m=1 for large X. Exact n=Xv pairs are removed.
For |delta|<=H/T and samples tau_i in [T,2T], every rotated core phase has
real part >=cos(2H)>=4999/5000. Thus other nonexact pairs in this SAME
core cannot cancel the exhibited positive pairs. For V<=v<3V/2,1<=j<=K,
n=Xv+j is in support and T delta<=2pi K/V<H. There are (V/2)K such
pairs, each weight >=1/(2sqrt(UV)). The COMPLETE nonexact near-alias real
correlation is at least

    (4999/5000) K/(4sqrt X),                                  (22)

which grows like X^.1/40000. At z=10^10 its exact rational squared lower
bound exceeds one. No huge supports are enumerated; uniform inequalities
certify it. The grid alias exp(i*tau_i*L)=exp(i*T*L) is retained.

This rules out deriving the required charge from l2 mass, pointwise divisor-
bounded envelopes, common sampling and generic large-sieve data ALONE.
The arrays do not satisfy prime-factor convolution restrictions or PNT/BV
marginal/distribution conditions. Thus they prove no PNT/BV-alone obstruction,
no actual consumer budget exhaustion and no realizable matrix lower bound.
The necessity test identifies a soft-bound gap, not decision E.

## 12. One precise smaller lemma and the ledger

The survivor set is: e not all zero; m from (5)/(6), m!=0; at least two
active blocks; at least one singleton block; and not one-sided |m|=1.
All frozen tuple removals are retained. This is a proper subset of the parent
NearAlias. The new lemma is

    for ONE declared H0>0, fixed R=6000, on the selected sections,
    limsup_(T->infinity) Q_T^hard(H0)<=q_alias,                 (23)

with literal kernel/weights (1),(14), ordinary primes, original slot windows
and masks, exact integer m, and 0<|log(P/Q)-mL|<=H0/T. If H(T) is used,
name it and prove the required uniformity. No auxiliary operators or new
zero-side class are requested. By (14) its charge is the charge for original
Q_T; the removed families have zero limiting charge.

For relaxed allocation q_alias<Delta_R with positive reserve for the other
centered excesses; for ideal allocation q_alias<Delta_I. No positive power
saving is logically necessary if a finite one-sided constant fits the ledger.
An explicit sufficient illustrative allocation is

    q_alias=Delta_R/2=52897896569489/1144715463675000000,

leaving Delta_R/2 for the OTHER centered excesses IF their remaining gate is
proved. The direct one-sided estimate (23) is weaker than the absolute
primitive condition (20); it is the minimal alias target here. It is not
being claimed as proved or enough by itself for strict >79.

For precision, let M6_ref be 157/630 or 34/135. In the frozen three-sector
split the OTHER centered excess is

    G_ref(T)=Central(T)+LongTail(T)+B D6(R)+A/36-B M6_ref.

Then the full excess is G_ref+Q_T^hard+o(1), and strict arithmetic closure
requires its limsup below Delta_ref. Thus a certified alias bound q leaves
Delta_ref-q for this exact G_ref, with a positive strict reserve. D6 remains
the filtered covariance diagonal; its numerical value is not substituted.
No theorem for G_ref is proved or reopened here. A choice q<Delta_ref is
an allocation with positive remaining reference slack, not a necessary
condition when an independently negative G_ref might compensate a larger q.

Obtained: support removals, zero limiting charges for Section 4, energy (15),
general envelope (16). Obtained survivor primitive estimate: NONE CERTIFIED.
Obtained q_alias: NONE CERTIFIED. Remaining paid ideal/relaxed budget:
UNKNOWN. Reference slacks unchanged; no missing charge is recorded as zero.
Central and LongTail stay frozen; strict >79 remains OPEN.

Requested report:

1. Exact signed formula: (1)-(2), actual section and all coefficients.
2. Alias m: full table, exact pattern-specific (5)-(6), all CSV records.
3. Resonance: (7); integer displacement (8) only at rational X^m.
4. Weighted object: (14)/(18); no unsigned count theorem is demanded.
5. Spacing/energy: (15)-(17), no small survivor charge.
6. Cancellations: exact prime-factor phase reduction plus three closed
   families; no survivor conjugacy/cumulant identity.
7. H: conditional requirement optimum H->0, unattained; H=1 only on an
   additionally prescribed H>=1 range. Global feasible optimum undetermined.
8. Primitive target: (20), H400 regression 4.598061669e-7; obtained none.
9. Literature: first coefficient/dilation/weighted-average mismatches above.
10. Minimal lemma: the ONE smaller signed survivor estimate (23), not a
    uniquely hardest-pattern claim.
11. Charge: removed families 0 limiting; surviving charge unknown.
12. Remaining paid budget: unknown, no invented subtraction.
13. Strict >79: OPEN.
14. Local commit: supplied in final response after the additive commit.

Artifacts: src/wp84_signed_near_alias_attack.py,
src/wp84_signed_near_alias_replay.py,
notes/WP84_SIGNED_NEAR_ALIAS_SUPPORT.csv,
notes/WP84_SIGNED_NEAR_ALIAS_CERTIFICATE.json. Producer checks all 14,656
records, window matching, energy, H requirements, closed-family width thresholds, 864 rational uniform-slab volume bounds,
and the strengthened generic falsifier. Replay uses exponential core intersections
instead of logarithm rounding, independently rechecks every pattern/count,
energy, budgets, exponents and frozen hashes. Finite examples validate algebra,
not selected-good-section existence or asymptotic signed trace success.
All prior commits and untracked notebooklm_packet/ are preserved.
