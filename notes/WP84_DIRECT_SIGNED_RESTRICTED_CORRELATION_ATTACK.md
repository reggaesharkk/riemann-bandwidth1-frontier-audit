# Direct signed restricted correlation attack

Date: 2026-10-07. Parent HEAD: 3cc57d259e6bd4f4e2a312bb272145bd9a08d89a.
Repository: C:/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit.
Branch: codex/c5-c6-attack-20261006. Local audit only; no push.

**Decision F. INCONCLUSIVE.** The first uncertified analytic step is an upper
bound for the joint signed, factor-restricted, sampled long-product residual
in (12), including its near-alias and long-tail terms. Exact Vaughan and
Heath-Brown identities do not provide that bound. No uniquely dominant piece,
all-but-one-subcase closure, or reduction of the ENTIRE residual to an ordinary
short additive shift has been established. Strict >79 remains OPEN.

This audit freezes the original degree-six consumer. It computes no mu7/mu8,
introduces no new consumer and preserves every earlier falsifier. The positive
model witness is not arithmetic evidence. Every sharp/model number below is a
budget reference, not a substitution for the filtered arithmetic trace.

## 1. Exact target and normalization

Use the source conventions of WP84_SIGNED_NEAR_PRODUCT_CELL_DECOMPOSITION,
WP84_POWER_SCALE_CENTRAL_WINDOW_AND_DENSITY_BRIDGE and the selected-section
reprojection theorem. Set

    L=log(T/(2pi)), X=exp(L)=T/(2pi),
    N=floor(exp(L-sqrt(L))), h_grid=2pi/L,
    d=floor(TL/(2pi)), I=[k_-,k_+], d'=|I|~d,
    tau_i=T+h_grid*i, a_phi->1, alpha_p=log(p)/L,
    c_p=-log(p)/(a_phi L sqrt(p)), 2<=p<=N, p ordinary prime.

The original cutoff and section are retained. In particular N^3/T is NOT
small. R is fixed; the frozen >79 ledger uses R=6000. Define

    f_0^eps(alpha)=1-alpha,
    f_l^+(alpha)=(1-exp(2pi*i*l*alpha))/(2pi*i*l), l!=0,
    f_l^-(alpha)=conj(f_l^+(alpha)).

For an ordered sign word eps=(eps_1,...,eps_b), eps_j in {+1,-1}, a closed
lag path l has |l_j|<=R, sum l_j=0, u_0=0 and u_j=sum_(a<=j)l_a. Its actual
admissible root interval is

    i_min=k_- - min_j u_j, i_max=k_+ - max_j u_j,
    M_l=max(0,d'-(max_j u_j-min_j u_j)).

With D_M(z)=M^-1 sum_(k=0..M-1) exp(2pi*i*k*z), define zero when M=0,

    K_l(lambda)= (M_l/d') exp(i*T*lambda)
                  exp(2pi*i*i_min*lambda/L) D_(M_l)(lambda/L).       (1)

This is exactly d'^-1 times the sum over admissible roots, not a continuous
time integral. For a tuple p=(p_1,...,p_b),

    P_+=product_(eps_j=+) p_j, P_-=product_(eps_j=-) p_j,
    lambda=log(P_+/P_-),
    W_(eps,l)(p)=product_j c_(p_j) f_(l_j)^(eps_j)(alpha_(p_j))
                  exp(2pi*i*sum_j eps_j*u_(j-1)*alpha_(p_j)).       (2)

The finite resolved ordinary-prime moment is

    M_b(T,R)=sum_eps sum_closed_l sum_(ordinary p_j<=N)
                    W_(eps,l)(p) K_l(log(P_+/P_-)).                (3)

Repeated primes ARE allowed in (3). If splitting by equality pattern, use an
exact indicator chi_pi(p) for each ordered set partition pi, including all
within-side and cross-side equalities. Coprimality/distinctness masks belong
inside the tuple sum. Summing the partition indicators equals one. They may
not be discarded or replaced by an unrestricted divisor coefficient. Prime
windows C_j are disjoint half-open intervals in alpha; all endpoint conventions
are carried into their indicators. Splitting by windows is an exact partition,
not a PNT approximation. Complex individual cells become real only after the
complete adjoint/reversal-conjugate pairing.

Canonical fifth and sixth sectors: for r positive and s=b-r negative positions,
let S_(b,r;C,pi,l) denote (3) restricted to those signs, windows and equality
pattern. Sum over ALL ordered sign placements. The principal sectors are
S_(5,2) and its 3:2 conjugates, S_(6,2) and its 4:2 conjugates, and S_(6,3).
Every remaining sign sector stays in the complement unless already controlled.
No extra combinatorial multiplicity is inserted after summing sign placements.

For a separable cell without chi_pi, define one-slot sequences

    a_j(p)=c_p f_(l_j)^+(alpha_p) exp(2pi*i*u_(j-1)*alpha_p) 1_Cj,
    A_r=a_(positive 1)*...*a_(positive r),
    B_s=a_(negative 1)*...*a_(negative s),
    F_r(t)=sum_n A_r(n) exp(i*t*log n),
    G_s(t)=sum_m B_s(m) exp(i*t*log m).

Then its exact value is d'^-1 sum_(i_min<=i<=i_max) F_r(tau_i)
conj(G_s(tau_i)). This is the useful signed L2 inner product BEFORE any
triangle inequality. Equality/coprimality masks require a labelled tuple
version or an exact projector; they are not generally separable A_r,B_s.

## 2. Minimal quantitative gate, without a continuum assumption

The frozen polynomial is q(x)^2, with

    q=(-19101/185500)+(961/3710)x+(31/50)x^2-(371/500)x^3.

Independent coefficient convolution gives

    c0=364848201/34410250000,
    c1=-18356061/344102500,
    c2=-26060119/430128125,
    c3=21981971/46375000, c4=0,
    c5=-A=-11501/12500, c6=B=137641/250000.

All moments use the SAME section. The inherited lower inputs are mu1,mu3=o(1),
mu2>=1/3-2/(pi^2 R)+o(1). The paid terms at R=6000 are

    e_band=128952763/92407500000,
    e_var=26060119/12734908593750,
    Jstar=21/200-c0-c2/3-e_band-e_var
         =64788151489666079/572357731837500000.                     (4)

The weakest upper gate retained here is: there exists eta>0 such that

    limsup_T [-A M5(T,6000)+B M6(T,6000)] <= Jstar-eta.              (5)

This does not ask that every correlation be o(1), that every cell have a
specified sign, or that both higher moments equal their sharp models. Existing
source/zero-side interfaces remain inherited obligations; this audit does not
newly certify them. The strict arithmetic gap alone is the target here.

For explicit reference allowances, equivalent sufficient inequalities are

    limsup [-A(M5-1/36)+B(M6-157/630)] <= Delta_ideal-eta,
    Delta_ideal=27704610381502/17886179119921875
               =0.00154893955806605...;                             (6)

or, using the relaxed sixth reference,

    limsup [-A(M5-1/36)+B(M6-34/135)] <= Delta_relaxed-eta,
    Delta_relaxed=52897896569489/572357731837500000
                 =0.00009242103954753147....                        (7)

For example eta=Delta_relaxed/2 is an explicit sufficient target, leaving half
the relaxed allowance. It is stronger than merely asking for SOME eta>0;
(5) is the minimal gate. No finite-R geometry error is secretly paid twice:
(5) uses actual filtered moments, so it needs no filtered-to-sharp replacement.
The ideal/relaxed references do not establish any limiting main term.

## 3. What can actually be removed

The following are reused CLOSED reductions, with their original scope.

1. Proper powers: write the SAME-section matrix X=Y+P. The established
   ||P||op=O_R(1), tau|P|^2=O_R(L^-2), hence normalized Schatten6 norm
   O_R(L^-1/3), together with coercivity of -A tau X^5+B tau X^6, give
   equivalence of bounded signed gates for X and the ordinary matrix Y.
   This is not o(1) for every separately masked proper-power population.
2. Selected-section reprojection: weighted full-path boundary errors
   rho_b=4bR K_R^b/d'=o(1) for b=5,6. Only this aggregate is closed;
   arbitrary masked total variation is not inferred.
3. Exact nonzero aliases: if exp(mL) is irrational, P_+/P_-=exp(mL)
   is empty. If rational a/b in lowest terms, products are ak,bk.
   The established weighted sum is <=C_R(1+L)^7 X^-1/2 for b<=6,
   uniformly in the allowed nonzero alias bins. Near aliases are NOT removed.
4. Ordinary exact central equality: b=5 has no equality by unique
   factorization, since total multiplicities on opposite sides would have
   to agree. At b=6 the leading equality consists of three distinct primes,
   each once with each sign. Two-prime and one-prime higher multiplicity
   equalities are lower mass, controlled by sum c_p^4=O(L^-4).
   Their fixed-R diagonal main term is D6(R), the finite filtered covariance
   sum, not the sharp constant 157/630. The covariance/PNT diagonal reduction
   was proved separately; no off-diagonal PNT substitution is made.
5. Fixed-gap product-length cells: grouped second mass and the discrete
   Hilbert/mean-value row bound give

       O_(R,b)((1+L)^C [sqrt(UV)/T+X^-1/2]).                       (8)

   A cell whose product upper exponents satisfy u_max+v_max<2-delta,
   delta>0 fixed, therefore closes. Central resonance-support-empty cells
   have no central contribution when separated by a fixed log gap, but
   their alias/tail contributions are not removed by support alone.

The explicit fixed-R covariance diagonal can be read without a sharp model.
Put x=-1/(4pi^2). For a paired positive/negative leaf with lags l,m and
path displacement difference t, its covariance is

    C(0,0,0)=1/6, C(0,0,t)=2x/t^2 for t!=0;
    C(l,0,t)=C(0,m,t)=0 for nonzero l or m;
    C(l,m,t)=-x/(lm) [1_(t=0)-1_(t+l=0)-1_(t-m=0)+1_(t+l-m=0)].

Sum the products of three covariances over the 15 pairings, all compatible
opposite sign assignments and all closed lags |l_j|<=R, in the source row
convention. This defines D6(R) exactly; src/wp84_repaired_open_diagonal.py
implements it with rational polynomials in x. It has NOT been numerically
evaluated at R6000 here. Keeping the exact finite expression prevents a free
sharp replacement. Root fractions tend to one at fixed R.

Define O5 and O6 as the remaining nonexact ordinary sums after the above
closed aggregate errors, diagonal subtraction and fixed-gap short cells.
They retain every uncovered sign sector, transition box, central long box,
near alias and long-product FAR contribution. Then

    M5=O5+o(1), M6=D6(R)+O6+o(1),
    residual E_T=-A O5+B O6,
    limsup E_T <= Jstar-B D6(6000)-eta                              (12)

is the exact irreducible joint gate. The closed errors are o(1), not charged
as a second finite defect. Neither exact D6 nor the absence of fifth exact
equalities computes the off-diagonal fifth main term 1/36.

## 4. Exponent cells and actual shift size

Let alpha_j>0, alpha_j<=1-L^-1/2 (up to the floor cutoff), and
u=sum_positive alpha_j, v=sum_negative alpha_j. The asymptotic CENTRAL
hard polytopes are

    P_(2,3)={alpha in (0,1)^5: u=v=gamma, 1<=gamma<2},
    P_(2,4)={alpha in (0,1)^6: u=v=gamma, 1<=gamma<2},
    P_(3,3)={alpha in (0,1)^6: u=v=gamma, 1<=gamma<3}.               (13)

At gamma=1 logarithms and the cutoff make a transition; gamma>1 is
supercritical for (8). These are possible-support geometries, not proven
prime tuple densities. Away from central balance, near-alias hyperplanes
are u-v=m, m a nonzero integer, with u+v>=2 for uncovered length cells.
The off-hyperplane transition/FAR domains also remain in (12).

The CSV enumerates every quarter-log box: 4^5+2*4^6=9216 boxes. If plus
interval is [l_p,u_p] and minus [l_m,u_m], central support is empty when
u_p<l_m or u_m<l_p; equality is labelled a resonance boundary, not silently
empty. If support overlaps, u_p+u_m<2 is fixed-gap short; l_p+l_m>2 is
supercritical long; the rest is a transition. These labels concern central
geometry. Boundaries and prime cutoff slices are retained; open endpoints
are not converted into an exact finite-T emptiness theorem. Counts are
machine-generated in the JSON and independently replayed.

Clear the CENTRAL product relation with n=P_+, z=P_-=n-h_shift. For each
separable cell the exact shifted sum is

    sum_(n,h_shift: n-h_shift>=1) A_r(n) conj B_s(n-h_shift)
                        K_l(log(n/(n-h_shift))).                  (14)

Insert chi_pi at tuple level when necessary. The central window |lambda|<=H/T
is EXACTLY

    n(1-exp(H/T)) <= h_shift <= n(1-exp(-H/T)).                     (15)

For n~X^gamma, H/T=o(1), its width is O(H X^(gamma-1)); relative to
N_cell=X^gamma this is N_cell^(1-1/gamma) times H and fixed constants.
The interior cell (3/5,3/5;2/5,2/5,2/5) has gamma=6/5, hence width
H N_cell^(1/6). The frozen prime cutoff, lag closure and ordinary-prime
restrictions do not reduce this exponent. It is an UPPER WINDOW WIDTH,
not a proof that every surviving shift is comparable to that width or that
a positive fraction of primes occupies it. Fixed/subpower H leaves exponent
1/6+o(1). Power H=N_cell^zeta changes it to 1/6+zeta and needs a new tail
payment; choosing it does not close the existing long tails.

General sixth central examples have the same formula: the 2:4 cell
(.6,.6;.3,.3,.3,.3) again has width N_cell^1/6; the 3:3 cell
(.4,.4,.4;.4,.4,.4) does too. Larger gamma in (13) gives larger widths.
There is no universal 1/6 shift exponent for the entire residual.

For alias m!=0 set xi=lambda-mL. Then

    K_l(lambda)=exp(i*T*mL) (M_l/d') exp(2pi*i*i_min*xi/L)
                  exp(i*T*xi)D_M(xi/L).

The resonance is n approximately X^m z, generally around a NONINTEGER dilated
center, not n-z a small integer shift. Only the sampled Dirichlet kernel is
periodic. Treating all aliases as copies of (14) would be an invalid reduction.

## 5. Legitimate prime decompositions and coefficient norms

Define Lambda_ord=Lambda-E, where E(n)=Lambda(n) on proper prime powers
and zero elsewhere. Every slot has weight

    -Lambda_ord(n)/(a_phi L sqrt(n))
       *f_l^eps(log n/L)*exp(2pi*i*eps*u*log n/L)*1_C(n), n<=N.    (16)

The multiplicative identity is applied to Lambda_ord, not to a retained
prime indicator times an arbitrary divisor decomposition. Retaining that
indicator would make the factorization tautological on primes.

Exact Vaughan identity for arbitrary U,V>=1 is

    Lambda=mu_(<=U)*log -mu_(<=U)*1*Lambda_(<=V)
             +Lambda_(<=V)+mu_(>U)*1*Lambda_(>V).                 (17)

The last term is sum_(at=n,a>U,t>V) mu(a) beta_V(t), with
beta_V(t)=sum_(c|t,c>V) Lambda(c), so 0<=beta_V(t)<=log t. Applying
(17)-E to EACH slot produces a finite expansion indexed by five choices
per slot (two Type I, one short term, one Type II, one compensation), with
all signs retained. Thus fifth and sixth expansions have at most 5^5 and
5^6 labelled terms BEFORE dyadic splitting; these are identities, not bounds.
All original product windows and Fourier factors are functions of at or abc,
not independent rectangles. Dyadic splitting retains their indicators.

At U=V=X^1/10 and a slot n~X^alpha:

- first Type I: a<=U, b~X^alpha/a, weight mu(a)log b;
- second Type I: a<=U,c<=V,b~X^alpha/(ac), weight -mu(a)Lambda(c);
- short term Lambda<=V: empty in windows whose lower exponent exceeds .1;
- Type II: a~X^rho, t~X^(alpha-rho), .1<rho<alpha-.1,
  weight mu(a)beta_V(t);
- compensation E: proper powers retained in the exact identity.

A boundary a just above U is retained; inequalities here describe exponent
interiors. The sample averaging remains one common root index; the dyadic
factors and shifts are summation variables, not independent time averages.
On M<=a<2M and Q<=t<2Q, exact useful bounds are

    sum |mu(a)|^2<=#a, sum |beta_V(t)|^2<=#t*(log(2Q))^2,
    sum |mu(a)|^2/a<=2,
    sum |beta_V(t)|^2/t<=2*(log(2Q))^2,

for M,Q>=1. Consequently the rectangular Type-II leaf weighted second mass
is <=4(log(2Q))^2/(|a_phi|^2 L^2) before bounded Fourier multipliers.
After grouping equal products the exact norm is sum_n|sum_(at=n)w(a,t)|^2;
collisions introduce divisor multiplicities. Bounds O((1+L)^C) suffice for
(8), but they do not supply a power saving. The same exact definition applies
to Type-I grouped norms. No new global matrix norm is assumed.

Heath-Brown identity with k=3 and integer z=ceil(N^(1/3)) is

    Lambda=sum_(j=1..3) (-1)^(j-1) binom(3,j)
                 mu_(<=z)^{*j} * 1^{*(j-1)} * log, n<=N.         (18)

Each j term has 2j factor variables, j short mu factors, j-1 unrestricted
one factors, one logarithmic factor. Subtract E per slot, giving at most
4^b labelled choices before dyadic splitting. Proof: R0=delta-mu_(<=z)*1
has support n>z; R0^{*3} vanishes for n<=z^3; expand (delta-R0)^3 and
convolve with Lambda, using 1*Lambda=log. Thus all coefficients and the
valid product-length cutoff in (18) are exact.

The verifier checks both identities using formal logarithms (prime exponent
vectors, not floating point) through n=250. The independent replay enumerates
divisor tuples, without the producer's convolution helpers, through n=120.
Finite tests support the implementation; the displayed convolution proofs
establish the identities for all n in their ranges.

## 6. A retained hard multilinear configuration; dominance not proved

In the fifth gamma=6/5 cell, choosing every Vaughan Type-II slot gives

    positive leaf factors: X^.3 times X^.3, twice;
    negative leaf factors: X^.2 times X^.2, three times.

Thus it is FOUR factor variables against SIX, with original grouped products
n~X^1.2 and |h_shift|<=O(H n^1/6). Mu factors are bounded; beta factors are
log bounded. Every original slot's product window, Fourier filter and the
common carrier K_l stay in place. Sixth 2:4 yields four versus eight factors;
sixth 3:3 yields six versus six. The rho intervals in Section 5 give all dyadic
variants. HB produces additional higher multilinear variants.

This is a concrete surviving obstacle to a generic mean-value proof. It has
NOT been shown to dominate the signed sum, and the other decomposition terms
have not all been closed. Cancellation between identity terms is possible.
The exact joint theorem (12) is weaker than uniformly controlling each of
these terms. Consequently decision B or C would overstate this audit.

## 7. Fresh primary literature and applicability audit

The reduction above precedes this literature audit. Inspected primary sources:

- Topacogullari, The Shifted Convolution of Divisor Functions,
  https://arxiv.org/pdf/1506.02608, Theorems 1.1, 1.2, 2.1.
- Baier, Browning, Marasingha, Zhao, Averages of shifted convolutions of d3(n),
  https://arxiv.org/pdf/1101.5464, Theorems 1, 2.
- Matomaki, Radziwill, Tao, Correlations of the von Mangoldt and higher divisor
  functions II: Divisor correlations in short ranges,
  https://arxiv.org/pdf/1712.08840, Theorem 1.1 and Proposition 3.4.
- Topacogullari, The shifted convolution of generalized divisor functions,
  https://arxiv.org/abs/1605.02364 (scope: d_k against d_2).

No theorem found in this audit states the required window-restricted mu/beta
multilinear correlation with all sampled carrier/alias weights. This is not a
claim that no such theorem or future proof exists.

|Candidate/tool|Actual input and saving|Hypothesis mismatch/payment|Normalized closure|
|---|---|---|---|
|Discrete Hilbert/MV, repository (8)|Grouped coefficient second mass; sqrt(UV)/T times log powers|At gamma=6/5 balanced supports this is X^1/5, rather than a negative power|YES fixed-gap short; NO hard cell|
|Topacogullari Thm 1.1|Unrestricted d3*d2, shift <=const n^2/3, error n^(8/9+epsilon)|1/6 shifts fit, but prime-factor windows and mu/beta sequences are not d3/d2|No application certified|
|Topacogullari Thm 1.2|Smooth unrestricted d3*d2; error n^(5/6+theta/3+epsilon), paper's bound 7/8|Needs specified coefficient structure and controlled smooth weight; sharp factor windows and arbitrary mu pieces not covered|No application certified|
|BBMZ Thm 1|Signed shift average of unrestricted d3*d3 discrepancy; Q^2+Q^1/2 n^13/12 times n^epsilon|At Q=n^1/6 second term is n^7/6, equal exponent to nQ; useful relative saving requires Q>=n^(1/6+epsilon)|No critical-scale saving; coefficient/carrier mismatch also remains|
|BBMZ Thm 2|Second shift moment for Q>=n^(1/3+epsilon)|Our critical Q=n^1/6 below range; different arrays|NO|
|MRT Thm 1.1|Leading divisor/divisor or Mangoldt/divisor correlations for almost all shifts, Q above a specified large log power|Shift size itself can fit; exceptional shifts, restricted factor arrays and weighted aggregate have not been controlled|No application certified|
|Generalized divisor shifted convolution|d_k*d2, uniform shift and power saving|Does not replace arbitrary factor-restricted prime convolutions by d_k; 3:3 not d_k*d2|No application certified|
|Dispersion|Cauchy gives exact cross-shift variance, Section 8|Needs new off-diagonal shifted mu/beta estimates; no free main-term subtraction|NO certified gain|
|Delta/circle|Exact detection of n-z=h by additive characters|Requires major/minor arc estimates for THESE arrays and exceptional/alias payment|Identity only|
|Voronoi|Transforms specified divisor/automorphic coefficients (e.g. Topacogullari Thm 2.1)|No supplied transform for arbitrary windowed mu/beta convolutions|No certified gain|
|Kuznetsov/spectral large sieve|Kloosterman spectral averages after a valid transform, with moduli/smoothness conditions|No valid transformation with our factor restrictions and complete modulus ranges established|No normalized error certified|
|Additive large sieve|Generic second-mass estimate for separated frequencies|Close product ratios cluster below 1/T; norm loss persists|NO, generic counterexample Section 9|
|Kloosterman bilinear/Deshouillers-Iwaniec style estimates|Savings require specified bilinear variables/moduli and coefficient norms|No derivation of a form with all lengths in its admissible region; naming the estimate is not a bound|No application certified|
|BV/BDH|Average prime AP discrepancies at their stated level, not arbitrary multi-prime shift correlations|Freezing p1~X^.6 in the fifth cell leaves q3~X^.4 modulo p1~X^.6, above BV level X^.2; other regroupings require an additional proof|Does not alone close this reduction|
|Type I/II prime estimates|Useful cancellation in their stated linear/bilinear phase ranges|Our equation couples several such factors plus n-dependent carrier, windows and aliases; identities provide no estimate|No whole-residual closure|

The BV line diagnoses one literal freezing, not a proof all possible regroupings
fail. Likewise Kuznetsov/DI rows record a missing reduction, not an impossibility
theorem. Strongest nearby quantitative theorem is the stated d2*d3 result;
strongest estimate actually applicable to generic original arrays is (8).

Even a hypothetical direct import of pointwise divisor errors would not pay
an absolute shift sum in the actual normalization: on n~N_cell, the slot
product weights have size n^-1 times logarithmic factors. Summing Q=n^1/6
pointwise errors n^(8/9+epsilon) gives n^1/18+epsilon after dividing by n;
the smoothed paper exponent 7/8 gives n^1/24+epsilon. These are growth,
not savings. No hidden division by Q is present in (14). Log powers cannot
repair these positive exponents. A genuinely averaged SIGNED result could
be better; that result for the actual arrays is not supplied by this audit.
No explicit spectral constant is certified against 9.24210395e-5.

## 8. Signed dual and exact dispersion expansion

The sampled inner product in Section 1 retains all signs and phases. Cauchy
bounds it by the two product-polynomial mean squares; their long support
reintroduces the same length loss. Carrier conjugacy makes the complete sum
real and sixth trace nonnegative, but does not give a signed upper bound on
-A M5+B M6. Positivity of B M6 alone is in the costly direction.

For a fixed central separable cell let

    S=sum_n a(n) Z(n),
    Z(n)=sum_h conj b(n-h) K(n,h),
    K(n,h)=K_l(log(n/(n-h)))1_(exact window).

The exact Cauchy variance is

    |S|^2 <= (sum_n|a(n)|^2) V,
    V=sum_(h,h') sum_n conj b(n-h) b(n-h')
                         K(n,h)conj K(n,h').                    (19)

Diagonal h=h' is a weighted second mass. Off-diagonal, putting z=n-h,
is a correlation of b(z) and b(z+h-h'), with |h-h'|<=2Q on a local
shift window. This does not shorten the shift exponent; it retains the prime
factor restrictions and adds coupled carrier weights. It gives h,h' averaging,
but no available estimate for it is proved. Nonseparable chi_pi introduces
additional labelled indices, not fewer constraints. No expectation/main term
may be subtracted without proving it. This dispersion subroute stops at (19).

## 9. Soft-bound necessity test and numerical scope

There is a rigorous generic coefficient-norm counterexample, not a prime
counterexample. Take integer m tending to infinity, T=m^5, n0=m^6,
K=floor(m/100), arrays a=b=1/sqrt(K) on [n0,n0+K-1], zero elsewhere.
Both squared l2 norms equal one. For ANY sampled tau_i in [T,2T], and any
two distinct cluster indices,

    |tau_i log(n/z)|<=2T(K-1)/n0<1/50,
    Re exp(i*tau_i log(n/z))>=1-(1/50)^2/2=4999/5000.

Thus the normalized sampled nonexact real correlation is at least
(4999/5000)(K-1), tending to infinity. Products have scale T^(6/5), and
these shifts lie INSIDE the critical n0^1/6 window. This proves that l2
norms and common time averaging alone cannot imply the desired cancellation.
It does NOT satisfy ordinary-prime factor restrictions, PNT normalization,
BV discrepancy or the matrix filter identities. Therefore it disproves no
prime theorem and is not decision E. PNT-alone/BV-alone impossibility has
NOT been established by a prime-compatible counterexample.

The producer certifies this inequality with exact rational arithmetic at
m=1000 as a regression, and the proof above gives the growing family.
The CSV is exponent reconnaissance, not finite-T prime-density evidence.
No empirical exponent/sign or finite prime correlation is promoted. No claim
of numerical convergence toward (5) is made; doing so without the unresolved
alias/tail bounds would not certify the arithmetic gate.

## 10. Extra structure and physical twists

Fixed R gives finitely many lag patterns with T-independent constants; it
does not shorten product length. Bounded displacement and zero total lag
close paths and control the selected-boundary error, already removed once.
Exact interval filters are smooth bounded slot factors; their nonvanishing
on the interior hard cell does not prove complete signed noncancellation.
Prime equality patterns can be represented exactly, but any PNT/BV transfer
requires the product reduction first. The common trace index is the existing
average of length about T, not several independent averages. A fixed signed
consumer permits the weaker joint gate (5); this is the genuine budget
advantage retained here, with no newly proved analytic saving.

The parent physical twist audit gives exact finite-T arithmetic auxiliary
extraction. Slot coefficient phases, lag characters and prime-code/equality
phase averages can preserve every original label. For a chosen lag character
the reconstruction norm is exactly 1: its Fourier projection has total
variation 1 and sends its own unit character to 1, proving the lower bound.
This is the smallest norm for that projection, at any fixed R.

For the FULL hard mask the known raw reconstruction upper bound is 24 (12
for its distinctness part); the prior trimmed inverse-consumer bound is about
4.960437739e11. These are not certified global minima. A smallest global norm
for the entire chosen finite-T family at R6000 has NOT been computed; the
family includes T-dependent prime-code characters. Saying norm=1 for that
whole reconstruction would be false. The optional uniform auxiliary theorem
would require a discrepancy bound epsilon_twist with

    sum_twists |weight_twist| * epsilon_twist <= allowance-eta.

With norm bound 24 and relaxed allowance this would demand epsilon_twist
<= (Delta_relaxed-eta)/24, about 3.851e-6 before reserving eta, IF the same
joint discrepancy has an exact applicable reconstruction. No such uniform
arithmetic estimate is proved. The direct gate (5) is weaker and does not
need this stronger family-wide hypothesis. The finite linear algebra does
not produce cancellation. Useful twists are arithmetic auxiliaries only;
common unitary conjugation is spectrally inert. The zero-side class is frozen.

## 11. Minimal new lemma and final decision

The minimal new input is the joint signed restricted-product estimate (12),
with explicit weights (1)-(2), natural cutoff, SAME selected section and
finite bandwidth, and SOME positive eta. Equivalently (6) or (7) specifies
the exact available excess with ideal or relaxed references. A proof of a
central averaged multilinear lemma for (14), with gamma in (13), would be
valuable but INSUFFICIENT without the uncovered near-alias and long-tail
bounds. Their kernels are part of the target, not an o(1) remainder.

No individual power saving is logically necessary if the complete signed
sum can be bounded directly inside (5). If a stronger approach supplies
main terms plus errors, its total coefficient-weighted normalized excess
must be below Delta_ideal or Delta_relaxed after every error is charged once.
A pointwise spectral bound with unspecified constant/main term does not meet
this requirement. Required numeric budget is verified; obtained analytic
saving on the hard residual is NONE CERTIFIED.

Requested report:

1. Fifth residual: O5 in (12), principal 2:3 sums (1)-(3), no exact ordinary
   fifth diagonal, with every uncovered companion/alias/tail retained.
2. Sixth residuals: 2:4,4:2,3:3 parts of O6, with exact D6(R) removed only.
3. Hard central polytopes: (13); near-alias hyperplanes and transition/FAR
   complements are additionally retained.
4. Shift: exact (15); gamma=6/5 gives width N_cell^1/6 times H, no universal
   exact-size assertion and no exponent reduction certified.
5. Prime decomposition: exact (17)-(18), proper-power compensation retained;
   finite labelled expansions and dyadic length/norm rules in Section 5.
6. Single hardest piece: NOT established; explicit retained four-vs-six
   Vaughan Type-II example in Section 6.
7. Existing theorem: unrestricted d2*d3 is closest; (8) actually closes short
   original cells. No strongest theorem closing the hard arrays is identified.
8. Mismatch: factor restrictions/mu weights, carrier/alias scope, and lack of
   coefficient-weighted signed shift-average payment.
9. New lemma: full joint gate (12), not a falsely unique central subcase.
10. Required excess: Delta_ideal=0.00154893955806605... or relaxed
    0.00009242103954753147..., leaving SOME eta>0.
11. Twists: exact extraction; no analytic saving, no global minimum certified.
12. Strict >79: OPEN. Neither budget exhaustion nor arithmetic success proved.
13. Local commit: supplied by git after this additive audit is committed.

Decision F is deliberate: the exact identities, hard-cell classification and
generic soft-norm falsifier are proved; the requested prime-restricted signed
arithmetic inequality remains the first uncertified step. No sideways route
is started.

Artifacts: src/wp84_direct_signed_correlation_attack.py;
src/wp84_direct_signed_correlation_replay.py;
notes/WP84_DIRECT_SIGNED_CORRELATION_CERTIFICATE.json;
notes/WP84_DIRECT_CORRELATION_EXPONENT_CELLS.csv. The replay checks 9216 boxes,
consumer convolution, both exact allowances, shift/loss exponents, formal-log
prime identities and the rational norm counterexample. These checks do not
certify the open analytic theorem. notebooklm_packet/ remains untouched.
