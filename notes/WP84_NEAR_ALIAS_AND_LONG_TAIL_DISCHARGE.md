# Near-alias and long-tail discharge audit

Date: 2026-10-07. Parent: 6667160c71f198a2419d9f93000a4afdfb23b425.
Worktree: C:/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit.
Branch: codex/c5-c6-attack-20261006. Local only; no push.

**F. INCONCLUSIVE.** The first uncertified step is a small signed bound for
the weighted nonexact near-alias prime-product primitive, or an alternative
estimate directly on its kernel integral. Long-tail primitives are also
uncontrolled. Neither side sector is discharged by this audit. This does NOT
prove that either actual prime sector is large, intrinsically hard, or exceeds
the budget. Therefore decision D (a hardness claim) and decision E (budget
exhaustion) would overstate the result. No central-only reduction is obtained.

The direct audit and all 9,216 exponent-box classifications are FROZEN. This
note does not alter them, change cutoff, reopen physical-mask reconstruction,
search consumers or compute higher moments. Strict >79 remains OPEN.

## 1. Exact signed three-sector decomposition

Use exactly the parent normalization:

    X=T/(2pi), L=log X, N=floor(exp(L-sqrt(L))),
    d=floor(TL/(2pi)), I=[k_-,k_+], d'=|I|<=d, d'/d->1,
    tau_i=T+2pi*i/L, c_p=-log p/(a_phi L sqrt p), a_phi->1,
    alpha_p=log p/L, ordinary primes 2<=p<=N,
    A=11501/12500, B=137641/250000, omega5=-A, omega6=B.

For every b=5,6, ordered sign word eps, closed path l with |l_j|<=R and
sum l_j=0, and ordered tuple of ordinary primes, retain

    u_0=0, u_j=sum_(t<=j)l_t,
    i_min=k_- -min_j u_j, i_max=k_+ -max_j u_j,
    M_l=max(0,d'-(max_j u_j-min_j u_j)),
    W=product_j c_(p_j) f_(l_j)^(eps_j)(alpha_(p_j))
                   exp(2pi*i*sum_j eps_j*u_(j-1)*alpha_(p_j)),
    lambda=log(P_+/P_-), P_+=product_positive p_j,
    P_-=product_negative p_j.

Here f0=1-alpha and f_l^+=(1-exp(2pi*i*l*alpha))/(2pi*i*l),
f_l^-=conj(f_l^+). The exact kernel is

    K_l(lambda)= exp(i*T*lambda) exp(2pi*i*i_min*lambda/L)
                  /d' *sum_(k=0..M_l-1)exp(2pi*i*k*lambda/L).      (1)

It is zero if M_l=0. Every prime-window indicator and equality/coprimality
pattern is retained inside W. Repeated primes are allowed in the unpartitioned
trace; masks partition them exactly. Nothing is replaced by continuum or
sharp geometry.

Let Omega_T be the remaining tuple set after subtracting ONLY the previously
closed exact resonances and already certified fixed-gap short contributions.
Its definition uses the parent frozen classes; no new reclassification of the
9,216 boxes occurs. Exact central diagonal and exact nonzero aliases are
removed separately, with their established o(1) or main-term scopes.
The finite diagonal before its PNT limit is D6,T(R), not 157/630.

Choose a cutoff H=H(T)>0 with H/T<L/2; to retain the critical central
exponent require H=X^o(1), including a fixed H. Define

    m=floor(lambda/L+1/2), delta=lambda-mL in [-L/2,L/2), a=H/T.

The tie convention is exact. On Omega_T, delta!=0. Set

    C_T=sum_(Omega_T, m=0, 0<|delta|<=a) omega_b W K_l(lambda),
    Q_T=sum_(Omega_T, m!=0, 0<|delta|<=a) omega_b W K_l(lambda),
    F_T=sum_(Omega_T, |delta|>a) omega_b W K_l(lambda).

Then, with NO triangle inequality,

    E_T=C_T+Q_T+F_T.                                             (2)

LongTail includes the old TRANSITION and FAR sectors for EVERY m, including
m=0. No annulus between H/T and another cutoff is omitted. All ordered sign
placements are summed once; no extra factor two for conjugates is inserted.
The exact finite signed moment is B D6,T(R)+E_T plus the explicitly removed
short and exact-alias sums. Their asymptotic aggregate is o(1). Proper powers
remain removed through the already proved signed-gate equivalence, not a
new termwise masked o(1) assertion.

In particular the weighted reprojection theorem is an AGGREGATE theorem.
Its o(1) boundary bound cannot automatically be allocated independently to
Q_T and F_T after frequency masking. This note retains the actual M_l and
i_min in (1), so no unproved masked reprojection is required or charged.

## 2. Exact alias support and nonexact target

For r positive and s=b-r negative slots the finite support satisfies

    r log2-s logN <= lambda <= r logN-s log2.                     (3)

Intersect this interval with the half-open nearest bin
[(m-1/2)L,(m+1/2)L). For a near-alias core intersect again with
[mL-H/T,mL+H/T], assigning the endpoints as in Section 1. Eventually nearest
bins lie among -s,...,r; extreme cores m=-s,r are excluded for subpower H
by the sqrt(L) cutoff deficit. The remaining possible nonzero cores are
m=-s+1,...,r-1 with zero omitted. These are possible supports, not proven
prime occupancies. Empty sides and special sign patterns are retained if
allowed by (3); they do not all vanish by central support arguments.

Write n=P_+, v=P_-. The exact near-alias condition is

    n exp(-H/T) <= X^m v <= n exp(H/T),
    n/v!=X^m, m!=0.                                            (4)

Unlike exact aliases, (4) imposes no divisibility n=ak,v=bk. For irrational
X^m exact equality is empty, but closeness to an irrational dilated lattice
is NOT empty by unique factorization. For rational X^m=a0/b0, a0,b0 coprime,
nonexact pairs satisfy |b0*n-a0*v|>=1. The elementary lower separation gives
roughly |delta|>=1/(b0*n+a0*v), which can be much smaller than 1/T in long
cells. Since T varies, no uniform Diophantine hypothesis on X^m is supplied.

The carrier factorization is EXACT:

    K_l(mL+delta)=exp(i*T*mL) exp(i*tau_(i_min)*delta)
                    g_l(delta),
    g_l(delta)=1/d' sum_(k=0..M_l-1)exp(2pi*i*k*delta/L).          (5)

Only the sampled geometric sum is periodic. The alias carrier exp(i*T*mL)
is not erased. Q_T in (2), including omega5 and omega6, is the exact total
normalized near-alias contribution still requiring an upper bound.

Uncovered possible alias geometry has u-v=m and u+v>=2, where u and v here
are product LOG EXPONENTS. Example fifth 2:3: positive exponents (.8,.8),
negative (.2,.2,.2), so u=1.6,v=.6,m=1, and sqrt(UV)/T has exponent .1
in X. The point is loss of a fixed-gap short bound, not a density proof.
Analogous sixth regions remain in the frozen decomposition.

## 3. Near-alias bounds actually obtained

Keep Q_T signed until after forming the complete measure in Section 5. A
universally available envelope is

    |Q_T| <= V_A(T),
    V_A=sum_(near-alias Omega_T) |omega_b W| M_l/d'.              (6)

This is a valid finite quantity, not a certified small limiting charge.
For a fixed ordered sign/path and dyadic product supports n in [U,2U),
v in [V,2V), with U,V positive integers and H/T<=1, there is a more explicit
unconditional lattice-count upper bound. Each ordinary r-prime product has
at most r! ordered representations, including repetitions, and

    |A_r(n)|<=r! |a_phi|^-r n^-1/2,
    |B_s(v)|<=s! |a_phi|^-s v^-1/2,                              (7)

because alpha_p<=1 and |f_l|<=1. The same bound holds after taking absolute
tuple weights with additional masks, since those only restrict tuples.
For a nonempty row of (4), the possible n interval has length at most
2U(exp(2H/T)-1)<=14U H/T; an interval of length ell contains at most ell+1
integers. Sum at most V rows and divide by sqrt(UV). Counting in the inverse
direction too gives

    |fixed ordered alias cell|
       <= r!s! |a_phi|^-b
            [14H sqrt(UV)/T + sqrt(min(U,V)/max(U,V))].          (8)

M_l/d'<=1 was used. All constants in this elementary bound are explicit;
14 follows from exp(2)<8 and convexity on [0,1]. The bound may be summed
over the finite alias/sign/path/window sets with omega_b included. It is
NOT small in all uncovered cells: in the fifth example its first term is
of order H X^.1. An upper bound that grows does NOT establish that the
actual contribution grows.

The parent discrete Hilbert/second-mass estimate also closes fixed-gap short
cells, with O_R((1+L)^C[sqrt(UV)/T+X^-1/2]). It supplies no vanishing bound
in this example. Its constants are not newly evaluated against the margin.
Take the minimum of available bounds (6), (8), and that established bound
when its hypotheses apply. No one of them certifies the TOTAL Q_T charge.

|Test|Available information|First missing step|Discharge?|
|---|---|---|---|
|Log spacing/rational products|Distinct ratios n/v,n'/v' are separated by at least inverse product denominators; rational X^m gives the integer numerator above|Long denominators exceed T; closeness to X^m not excluded|No|
|Multiplicative energy|Exact ordinary product multiplicities <=r!; grouped second mass controlled|Energy at n=v does not bound n approximately X^m v|No|
|Hilbert inequality|Frequency gap/second-mass estimates; fixed-gap short cells closed|Sampled phases require modulo-L gaps and dense long-cell near-resonances|No new long-cell bound|
|Large sieve|Bounds depend on separation or local frequency density|Folded frequencies need a new short-window density estimate, not just l2 norms|No|
|Short-interval divisor bounds|Majorize ordinary products by unrestricted integers/divisor-bounded arrays; (8) is unconditional|Logarithmic sparsity alone does not repair the positive X^.1 length loss|No certified payment|
|Selberg/upper-bound sieve|Can majorize prime populations if the required AP/distribution remainders are controlled|No audited signed uniform estimate for the dilated multi-prime product window with actual carrier|No|
|Almost-all short-interval almost-prime results|Existence/distribution results in their specified interval averages|Our dilated centers, coupled prime products, fixed windows and signed weighted total are different|No direct application|

The primary Hilbert reference is [Montgomery-Vaughan, Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).
Sieve search leads include [Holowinsky, A Sieve Method for Shifted Convolution
Sums](https://arxiv.org/abs/0809.1669), whose stated scope is multiplicative
shifted sums with suitable hypotheses, and [Matomaki, Almost primes in almost
all very short intervals](https://arxiv.org/abs/2012.11565), whose stated
result concerns finding a product of at most two primes in almost all short
intervals. Neither statement asserts the present signed dilated correlation.
No unexplored extension of either is treated as a theorem here.

## 4. Long-tail decay and the normalization loss

For 0<|delta|<=L/2, the exact geometric quotient gives

    |g_l(delta)|
       = |sin(pi*M_l*delta/L)|/[d'|sin(pi*delta/L)|]
       <= min(M_l/d', L/(2d'|delta|)).                          (9)

The carrier in (5) has unit modulus. Therefore

    |F_T| <= sum_(LongTail Omega_T) |omega_b W|
                         min(M_l/d',L/(2d'|delta|))
           <= min(1,LT/(2d'H)) V_F(T),
    V_F(T)=sum_(LongTail Omega_T)|omega_b W|.                   (10)

This is the certified tail bound. It is an explicit weighted envelope, NOT
a bound by a small number. Let S=sum_(ordinary p<=N)|c_p| and
F_R=1+(2/pi)sum_(l=1..R)1/l. Since |f0|<=1, |f_l|<=1/(pi|l|), sum the
first b-1 lags freely, use the forced last lag with |f|<=1, and sum signs:

    V_F(T)<= A*2^5*S^5*F_R^4+B*2^6*S^6*F_R^5,
    S<=2 sqrt(N)/|a_phi|.                                    (11)

The last inequality follows by bounding alpha_p<=1 and summing n^-1/2 over
integers. Formula (11) is deliberately an explicit envelope; PNT could improve
log factors, but not the positive product-length power. For subpower H, the
sixth leading envelope in (10) is of size O_R(N^3/H), so it does not tend to
zero. Even the parent harmonic-row bound costs sqrt(UV)/T in uncovered
balanced cells, X^1/5 at gamma=6/5, up to logarithms. A fixed away-from-core
band |delta|>=delta0>0 has pointwise O(1/T) decay, but its product coefficient
first mass can be O(sqrt(UV)); this again leaves sqrt(UV)/T, not a free o(1).

No squared Parseval tail for UNIFORM frequency measure can replace (10).
Our prime-product measure is weighted and atomic. Finite R controls the
number and size of lag factors and the selected root loss; it does not supply
an extra T power. The existing second mass, rather than total variation,
helps short cells, but requires additional local correlation information to
control the masked long tail. Reclassifying all bins into enlarged cores by
choosing H~TL would make tails empty by definition while destroying the
central N_cell^1/6 target; that is not a discharge at the stated shift scale.

## 5. Signed Abel bound BEFORE population absolute values

There is a sharper conditional formulation retaining cancellations. Group
all tuples by kappa=(M_l,i_min,m,sigma), sigma=sign(delta), and sector. In
a group use x=|delta| and form the COMPLEX signed measure

    nu_kappa=sum_(tuples in group) omega_b W exp(i*T*mL)
                         exp(i*tau_(i_min)*sigma*x) delta_x.    (12)

Fifth and sixth weights are combined wherever the kernel data match, rather
than bounded individually first. Define g_kappa(x)=g_l(sigma*x). The exact
sector is sum_kappa integral g_kappa(x) d nu_kappa(x). Equality masks and
windows are inside the measure. Nonmatching M_l cannot be silently combined
using a masked boundary approximation.

For NearAlias let P_kappa(x)=nu_kappa((0,x]), 0<=x<=a; removed exact atoms
ensure P_kappa(0)=0. Abel summation is exact:

    Q_T=sum_kappa [g_kappa(a)P_kappa(a)
                        -integral_0^a P_kappa(x)g'_kappa(x)dx]. (13)

For LongTail use P_kappa(x)=nu_kappa((a,x]), a<=x<=L/2. Assign the negative
nearest-bin boundary consistently; empty boundary points make no difference.
Then

    F_T=sum_kappa [g_kappa(L/2)P_kappa(L/2)
                        -integral_a^(L/2) P_kappa(x)g'_kappa(x)dx]. (14)

These are signed formulas; the only absolute values in the following bounds
are applied AFTER forming P. Exact derivative bounds are

    |g'_kappa(x)|<=pi*M_l*(M_l-1)/(d'L)
                  <=pi*(d'-1)/L,
    |g'_kappa(x)|<=pi/x+pi*L/(4d'x^2), 0<x<=L/2.               (15)

The second follows by differentiating the geometric quotient, including its
phase, using sin(pi*x/L)>=2x/L and M_l<=d'. The consumer coefficients are
already inside P; they must not be charged a second time.

Define epsilon_A(T)=sum_(near groups) sup_(0<=x<=a)|P_kappa(x)|,
and epsilon_F(T)=sum_(tail groups) sup_(a<=x<=L/2)|P_kappa(x)|. Then

    |Q_T| <= epsilon_A(T) [1+pi*(d'-1)H/(LT)]
          <= epsilon_A(T) (1+H/2),                            (16)

because d'<=d<=TL/(2pi). For the incremental tail primitives,

    |F_T| <= epsilon_F(T) Phi_F(T,H),
    Phi_F=1/d'+pi log(TL/(2H))
                      +pi L/(4d') [T/H-2/L].                 (17)

Only the final endpoint is charged: the incremental primitive is zero at a.
An often-used full primitive from zero would require both endpoints instead;
this distinction prevents paying a fictitious smaller bound. Integrating the
minimum of the two bounds (15) can sharpen (17) without changing the missing
primitive estimate. No bound for epsilon_A or epsilon_F on actual prime
products is established here. If a joint oriented primitive cancellation can
be proved without separating kappa, the resulting signed payment can be
weaker than (16)-(17); a per-group uniform bound is sufficient, not minimal.

Carrier conjugacy gives paired real parts, 2 Re(z), rather than zero. Degree
five and degree six terms are homogeneous of different degree, so their
coefficients alone cannot yield an algebraic cancellation identity for all
amplitudes: scaling amplitudes would separate degree five from degree six.
This observation is not a counterexample to a special prime cancellation.
No source identity cancels Q_T or F_T for the actual prime amplitudes.

## 6. Falsifier-first scope: soft norms do not control near aliases

A rigorous generic norm counterexample tests any claimed inference from l2
mass plus sampling alone. Let integer z0 tend to infinity, X=z0^5,
T=2pi X, L=log X, v0=z0^3, K=floor(v0/10000). Put b(v0)=1 and

    a(X*v0+j)=1/sqrt(K), 1<=j<=K,

zero elsewhere. Each array has squared l2 norm 1. Every ratio is NONEXACT
near alias m=1, with

    delta_j=log(1+j/(X*v0)),
    0<T*delta_j<=2pi K/v0<1/100.

For any actual sample tau_i in [T,2T], the folded phase obeys
|tau_i delta_j|<=4pi K/v0<1/50. At each grid root
exp(i*tau_i*L)=exp(i*T*L), a common constant. Rotate a by its inverse.
Then the normalized real sampled sum is at least

    (4999/5000) sqrt(K),                                     (18)

using cos y>=1-y^2/2. No exact alias term is involved. The positive length
is X^1.6 and negative X^.6, within the possible alias exponent geometry.
The script certifies the inequalities rationally at z0=1000 with
333/106<pi<355/113; the proof above supplies the growing family.

IMPORTANT: these arrays are NOT prime-factor convolutions, do not satisfy
the pointwise envelope (7), and are not a PNT/BV counterexample. Equation
(18) therefore invalidates only a soft l2/sampling-alone argument. It does
not invalidate the parent bounds that additionally use prime weights, and
does not prove actual near aliases large. No prime-compatible lower-bound
falsifier or signed budget exhaustion has been constructed. For LongTail,
(9) is genuine kernel decay; the gap is the atomic weighted population or
primitive bound, not a falsification of that decay formula.

## 7. Budget certificate: no missing charge is entered as zero

The frozen same-section consumer threshold and two reference allowances are

    Jstar=64788151489666079/572357731837500000,
    Delta_ideal=27704610381502/17886179119921875
                =0.00154893955806605...,
    Delta_relaxed=52897896569489/572357731837500000
                  =0.00009242103954753147....

Closed short/exact-alias/aggregate boundary/proper-power gates have ZERO
limiting additional charge in their established scopes. The two side sectors
have NO certified finite limiting charge. Their sum and the paid remaining
allowance are therefore UNKNOWN, not zero and not exhausted. The reference
allowances remain unchanged, but cannot be called available AFTER discharge.

For a quantitative conditional check only, take H=400 (this is a frequency
cutoff example, not changing Fourier bandwidth R=6000). Formula (16) costs
at most 201 epsilon_A. If allocated the ENTIRE respective allowance, the
required primitive bound would be

    epsilon_A < Delta_ideal/201 =0.000007706166955552487...,
    epsilon_A < Delta_relaxed/201 =0.00000045980616690314163....   (19)

The exact rational divisions are in the JSON. A positive strict gap eta and
any tail charge would reduce those thresholds. No epsilon_A satisfying (19)
has been proved. Similarly (17) would need epsilon_F<allocation/Phi_F, whose
worst-case multiplier grows roughly like pi log(TL/H). These are targets,
not charges.

If actual one-sided bounds Q_T<=q+o(1), F_T<=f+o(1) were obtained, they
would leave allowance Delta_ref-q-f in a suitably centered residual theorem.
Negative signed q or f can help; absolute bounds are not logically necessary.
As presently neither q nor f is certified, that arithmetic subtraction cannot
be performed. No sharp-model transport is silently used to supply a main
term for either side.

## 8. Central object, and why it is not yet the only debt

C_T in (2) is exact and can be described without either side term, but it is
NOT equivalent to the original gate unless Q_T+F_T is paid. Its principal
central supports are, with alpha_j>0 and alpha_j<=1-L^-1/2,

    fifth 2:3: sum_positive alpha=sum_negative alpha=gamma,
                 1<=gamma<2 in the limiting hard polytope;
    sixth 2:4: same equality, 1<=gamma<2;
    sixth 3:3: same equality, 1<=gamma<3.

Transition/boundary cells and all other unclosed central sign sectors are
also retained. This statement uses the frozen classifications unchanged.
For a separable fixed sign/path/window, retain slot arrays

    a_j(p)=c_p f_(l_j)^+(alpha_p)
                       exp(2pi*i*u_(j-1)*alpha_p) 1_Cj(p),
    A_r=convolution of positive slots,
    B_s=convolution of negative slots.

The central sum is (with tuple masks retained when nonseparable)

    sum_(n,h:0<|log(n/(n-h))|<=H/T)
             A_r(n) conj B_s(n-h) K_l(log(n/(n-h))).            (20)

Its normalization is 1/d' already in K_l; there is NO extra 1/H or reciprocal
number of shifts. The exact shift bounds are

    n(1-exp(H/T))<=h<=n(1-exp(-H/T)).                           (21)

At n~X^gamma, shift WIDTH is H X^(gamma-1). At gamma=6/5 this is
H N_cell^1/6, with N_cell=X^6/5. Fixed/subpower H retains exponent 1/6+o(1).
For larger gamma it is N_cell^(1-1/gamma), up to H; it is not universally
N_cell^1/6. No frozen constraint has eliminated those other central cells.
The smoothing is the exact sampled Dirichlet kernel with its carrier,
Fourier-path phase and selected roots, not a free smooth divisor weight.

The weakest ORIGINAL sufficient theorem is still

    limsup [C_T+Q_T+F_T] < Jstar-B D6(6000).                    (22)

D6 is the exact filtered finite-covariance diagonal from the parent, not a
sharp substitution. A conditional central-only statement, IF signed charges
q,f were proved, would be

    limsup C_T <= Jstar-B D6(6000)-q-f-eta, eta>0.              (23)

Equivalently with a justified central reference main term, one can express an
excess below the remaining Delta_ref. That main term and q,f are NOT supplied
here. An absolute |C_T|<=Delta_ref statement would be a stronger, differently
centered theorem and is not the minimal required gate. Therefore there is
NO weakest numerical central-only epsilon certified by this audit.

## 9. Conditional central theorem match, with first mismatch explicit

Since no final central-only reduction is obtained, this is a CONDITIONAL
comparison, not a claim of applicability. It does not reopen the frozen
direct literature audit.

|Source|Relevant stated hypotheses|Match at gamma=6/5|First mismatch|
|---|---|---|---|
|Topacogullari, https://arxiv.org/pdf/1506.02608, Thm 1.1/1.2|Unrestricted d3*d2; shifts <=constant n^2/3; specified sharp/smooth n weights|Shift exponent 1/6 is allowed|Coefficient arrays are window-restricted prime convolutions, not d2/d3; no permitted replacement theorem|
|BBMZ, https://arxiv.org/pdf/1101.5464, Thm 1|Unrestricted d3*d3 shifted discrepancy average; useful relative saving above n^(1/6+epsilon)|Critical shift width is n^1/6 for fixed H|Arrays mismatch first; even ignoring it, the stated averaged error has no power saving at the critical exponent|
|MRT, https://arxiv.org/pdf/1712.08840, Thm 1.1|Leading divisor/divisor or Mangoldt/divisor correlations for almost all shifts in stated ranges|A critical power-sized shift interval can meet the size condition|Restricted arrays and exceptional weighted shifts are uncontrolled; no stated carrier-weighted joint error|

Even for unrestricted coefficients, summing the Topacogullari pointwise
errors over n^1/6 shifts after the actual n^-1 amplitude gives positive
exponents 1/18 (8/9 error) or 1/24 (7/8 smooth error), not a paid normalized
saving. The parent independent replay already certified these exponents.
The required signed averaged theorem is stronger in structure than importing
those pointwise errors. No theorem here controls the side sectors for free.

## 10. Evidence and requested result

Artifacts:

- src/wp84_near_alias_long_tail_discharge.py: exact tuple/selected-root
  constructor; rational logarithm intervals with explicit remainder;
  nearest-alias classifier for certified nonboundary examples; natural prime
  cutoff validation; sine-quotient interval tail checks; joint budget and soft
  norm falsifier certificate. Boundary ambiguity is not numerically guessed.
- src/wp84_near_alias_long_tail_replay.py: independent cosine-Gram evaluation
  of squared geometric kernels, elementary-log classification checks,
  displacement-root counts, rational budget and frozen-file hash replay.
- notes/WP84_NEAR_ALIAS_LONG_TAIL_CERTIFICATE.json: all exact targets and
  scopes; unresolved charges are JSON null, not zero.

The interval verifier checks 284 nonzero frequency cases with varying M_l
and d'; the independent replay uses the cosine-Gram expansion instead of the
producer's sine quotient. Both PASS. Finite checks validate implementations;
(9), (15) and the Abel identities are proved analytically above. The examples
use ordinary primes below the natural cutoff, but do not assert that the
chosen small-height full interval is a selected good section or certify any
asymptotic trace sign/density.

Requested report:

1. Exact decomposition: (2), with actual omega5=-A, omega6=B and (1).
2. Near-alias bound: signed primitive identity (13); valid unconditional
   envelopes (6),(8); NO small finite limiting charge certified.
3. Tail bound: (9)-(11), or conditional signed primitive payment (14)-(17);
   NO small finite limiting charge certified.
4. Total charged side amount: UNKNOWN. Closed removed limiting charge is 0.
5. Remaining paid allowance: UNKNOWN; ideal/relaxed references preserved.
6. Final minimal central theorem: NOT obtained. Conditional (23) cannot be
   promoted without q,f, and central cells have more than one shift exponent.
7. Strict >79: OPEN.
8. Local commit: provided in the final response after committing this audit.

**Decision F.** The first missing near-alias primitive bound (or direct signed
kernel bound) remains uncertified; long-tail signed cancellation is likewise
not established. The source-level split is exact, and its conditional payments
are explicit. No claim of actual arithmetic hardness, side-sector budget
exhaustion, or a single central N^1/6 debt is made.
