# Remaining signed near-alias survivor: exact reduction and evidence boundary

Parent b704d607fe08a656f5c7f5dfd2bc5e7f4149117d; isolated branch
codex/c5-c6-attack-20261006. Local additive audit only. Decision **F**.
First uncertified step: a quantitative bound on the actual signed, prime-restricted dilated-product primitive below the allocated allowance. Strict >79 remains OPEN. No charge is certified. Closed families and all previous consumers remain frozen.

## Complete survivor and normalization

Put X=T/(2*pi), L=log X, N=floor(exp(L-sqrt(L))), d=floor(T*L/(2*pi)).
Use the existing selected principal section I=[k_-,k_+], d'=k_+-k_-+1,
and its actual a_phi(T), not a diagnostic replacement. Fix R=6000.
Let omega_5=-11501/12500 and omega_6=137641/250000.
For each b=5,6, each ordered sign word epsilon in {+1,-1}^b,
each exact equality partition pi, assign distinct ordinary primes q_B<=N
(one for each block), and put p_j=q_[j], alpha_j=log(p_j)/L.
All original leaf-window restrictions are retained; a block window is their
intersection. In particular 0<alpha_B<=log(N)/L. Distinct blocks require
q_B!=q_C, hence distinct-prime blocks are coprime. Define

    nu_B=|B|, e_B=sum_(j in B) epsilon_j,
    A=prod_(e_B>0) q_B^e_B, Bden=prod_(e_B<0) q_B^(-e_B).

Then gcd(A,Bden)=1. Blocks e_B=0 disappear from the PHASE only:
their coefficient and Fourier/path weights remain. Exponents are integers
in [-nu_B,nu_B], congruent to nu_B modulo 2; nu_B<=b.
The number of prime factors with multiplicity is sum e_B^+ and sum e_B^-;
the numbers of distinct active factors are the corresponding block counts.
Every individual pattern is listed in the extractor CSV, with no quotient
by ordered signs or equality labels.

For l_j in [-R,R], sum l_j=0, define u_0=0, u_j=sum_(i<=j) l_i,
imin=k_- - min_j u_j, M=max(0,d'-max_j u_j+min_j u_j).
Use the convention of the frozen constructor:

    c_p=-log p/(a_phi L sqrt p),
    f_0^epsilon(alpha)=1-alpha,
    f_l^+(alpha)=(1-exp(2*pi*i*l*alpha))/(2*pi*i*l),
    f_l^-=conj(f_l^+).
    W=chi * prod_j[c_(p_j) f_(l_j)^(epsilon_j)(alpha_j)]
      * exp(2*pi*i*sum_j epsilon_j*u_(j-1)*alpha_j).
    lambda=log(A/Bden),
    K_l(lambda)=exp(i*T*lambda+2*pi*i*imin*lambda/L)
               /d' * sum_(k=0..M-1) exp(2*pi*i*k*lambda/L).

Here chi is exactly the product of original window indicators, not a new
smooth substitute. Empty M contributes zero. The complete finite-T sum is

    Q_surv=Re sum_(b=5,6) omega_b sum_epsilon sum_pi sum_(distinct q_B<=N)
            sum_(closed Fourier paths l) sum_(m selected for pi,epsilon)
            W K_l(lambda) 1_(0<|lambda-mL|<=H/T),

with nearest alias chosen in the same half-open [-L/2,L/2) residual cell as
the frozen classifier. Exact aliases delta=0 are excluded. The selected
(pi,epsilon,m) are precisely rows whose frozen status is
remaining_signed_dilated_product. This enumeration retains finite support
constraints and all path-dependent masks. No extra factor two is inserted.
H is fixed positive, or one explicitly declared admissible H=X^o(1);
H/T<L/2 is needed for uniqueness. We do not optimize H.

Counts: 1,132 fifth and 7,608 sixth sign/equality classes, total 8,740.
There are 1,956 and 19,632 pattern/alias pairs, total 21,588.
There are 105 oriented reduced exponent patterns without m, 336 with m,
and 398 decorated (nu_B,e_B,m) patterns. Canonicalization does not merge
weights or windows. The three previously closed families are simply
excluded; this note does not reopen their proofs.

## Exact arithmetic window

Write delta=lambda-mL and a=H/T. The sharp condition is

    X^m Bden exp(-a)<=A<=X^m Bden exp(a), A!=X^m Bden.
    A-X^m Bden in X^m Bden [exp(-a)-1,exp(a)-1].

The asymmetric interval is more precise than an absolute bound; the latter
is <=X^m Bden*(exp(a)-1). If X^m=a0/b0 in lowest positive terms,

    h=b0 A-a0 Bden !=0,
    a0 Bden*(exp(-a)-1)<=h<=a0 Bden*(exp(a)-1),
    h congruent -a0 Bden (mod b0).

For irrational X^m the center is real, not an integer additive shift.
The factor 2*pi is retained by T=2*pi*X throughout.
For example the all-distinct 2:3 cell with exponents .8,.8 versus .2,.2,.2
has A about X^(8/5), Bden about X^(3/5), m=1, and displacement width
O(H X^(3/5)) at integer X. This is a dilated product correlation, not an
ordinary n,n+h restricted d2-d3 theorem. Other patterns have other factor
counts and powers; there is no single d2-d3 representation for all rows.

## Exact signed primitive, without destroying fifth/sixth signs

Let kappa=(M,imin,m,sigma), sigma=sign delta, x=|delta|. Define the complex
atomic measure with each original atom weighted by

    omega_b W exp(i*T*mL) exp(i*(T+2*pi*imin/L)*sigma*x).

All b, signs and equality classes sharing kappa are combined before taking
any absolute value. P_kappa(Y) is its mass on (0,Y], 0<=Y<=a. Define

    g_kappa(Y)=1/d' sum_(k=0..M-1) exp(2*pi*i*k*sigma*Y/L).
    Q_surv=Re sum_kappa [g_kappa(a)P_kappa(a)
                         - integral_0^a P_kappa(Y)g'_kappa(Y)dY].

This is exact finite atomic Stieltjes integration by parts, with P(0)=0.
A single scalar sum of primitives is insufficient because kernels differ.
The correct norm is P_surv=sum_kappa sup_(0<=Y<=a)|P_kappa(Y)|. Thus

    |Q_surv|<= C_exact P_surv,
    C_exact=max_kappa (|g_kappa(a)|+integral_0^a |g'_kappa(Y)|dY)
      <= max_kappa [M/d'+pi*M*(M-1)*H/(d'*L*T)]
      <= 1+pi*(d'-1)*H/(L*T)<=1+H/2.

The last step uses d'<=d. This is a bound, not an achieved primitive estimate.
The constructor includes a genuine nonexact prime tuple (2,3,11,13,17),
++---, X=405, m=-1, coprime ratio 6/2431, zero lag, H=10.

Exact reference slacks are

    Delta_ideal=27704610381502/17886179119921875,
    Delta_rel=52897896569489/572357731837500000.

A share s in {1,1/2,1/4,1/10} is sufficient if
P_surv<=s*Delta_rel/(1+H/2). At H=400 these are respectively
4.598061669031416e-7, 2.299030834515708e-7,
1.149515417257854e-7, 4.598061669031416e-8. NONE ACHIEVED.
The certificate verifies exact rational allocations for H=1,10,100,400.

## Prime decomposition: exhaustive finite generator

For a distinct block q of multiplicity nu, the ordinary-prime weight is

    (-1)^nu Lambda_ord(q)(log q)^(nu-1)/(a_phi^nu L^nu q^(nu/2))

times its original filters, windows and path phase. Lambda_ord=Lambda-E,
where E is supported on proper prime powers. These compensators are exact
identity terms and do not reopen a closed proper-power gate.
Apply the following identity ONCE per distinct block:

    Lambda=mu_(<=U)*log - mu_(<=U)*1*Lambda_(<=V)
            +Lambda_(<=V)+mu_(>U)*1*Lambda_(>V).

The tags I1,I2,SHORT,II,POWER_COMP give every one of 5^k products for k
blocks. The executable piece_words enumerates the complete Cartesian list.
For I1 q=ab, a<=U, coefficient mu(a)log b.
For I2 q=acb, a<=U,c<=V, coefficient -mu(a)Lambda(c).
SHORT q<=V. II q=at, a>U,t>V, coefficient mu(a)beta_V(t),
beta_V(t)=sum_(c|t,c>V)Lambda(c)<=log t. POWER_COMP is -E(q).
Each dyadic choice has products constrained to its original q-window,
q<=N; lengths of free variables are q divided by the recorded short factors.
No sharp window is replaced by a smooth one.

Heath-Brown order three with z=ceil(N^(1/3)) gives, for q<=z^3,

    Lambda=sum_(j=1..3) (-1)^(j-1) binom(3,j)
             mu_(<=z)^{*j} * 1^{*(j-1)} * log.

HBj has 2j variables, j bounded by z, j-1 coefficients 1, one log,
product q in the original block interval. Together with -E these enumerate
4^k products. Exact identity regression is included; no estimates are
inferred from the identity. For every tag tuple the shift, alias m, root
average M<=d', and primitive cutoff Y<=H/T are unchanged. There is one
sampled root average, not independent time averages for each block.

For an II dyadic rectangle a in [M0,2M0),t in [Q0,2Q0), the unfiltered
block coefficient has squared l2 norm bounded by

    4*(M0 Q0)^(1-nu)*(log(4 M0 Q0))^(2nu-2)*(log(2Q0))^2
       /(|a_phi|^(2nu)*L^(2nu)).

This uses |mu|<=1 and beta<=log; actual filters multiply this bound by
their squared suprema. Grouping products creates divisor collisions,
which are retained rather than assigned a free power saving. Composite
intermediate blocks still obey q_B!=q_C. Finite-R Fourier factors are
analytic but the prime and block windows are sharp. There is no certified
unique hardest tag tuple. For example all-II in the 2:3 cell already yields
four versus six factor variables; this is an example, not a dominance claim.

## Dispersion test and its precise loss

For a separable cell write P=sum_n a(n)Z_n, where

    Z_n=sum_v conj(b(v)) F_Y(n,v),
    F_Y(n,v)=exp(i*tau*log(n/(X^m v)))
             1_(0<sigma*log(n/(X^m v))<=Y),
    tau=T+2*pi*imin/L.

Constant carrier and omega are retained outside this expression. Original
nonseparable masks are inserted into F, not discarded. Cauchy gives exactly

    |P|^2<=||a||_2^2 sum_(v,v') conj(b(v))b(v')
                 sum_n F_Y(n,v)conj(F_Y(n,v')).

The diagonal is sum_v |b(v)|^2 times the number of allowed n; its interval
length is at most X^m v*(exp(Y)-exp(-Y)), with an extra one for integer
counting. On the off-diagonal, a necessary condition is
v'/v in [exp(-2Y),exp(2Y)], hence |v-v'|<=v*(exp(2Y)-1).
The n-carrier cancels in the product, leaving exp(i*tau*log(v'/v))
and the exact intersection count and masks. This is the complete variance;
it does not introduce an independent prime average.

In the 2:3 example v about X^(3/5), fixed H, distinct v off-diagonals
are eventually empty because H*v/T tends to zero. This useful geometric
simplification STILL gives only ||a||_2||b||_2*sqrt(1+O(H X^(3/5))),
which grows if the available norms are O(1). Reversing Cauchy creates
nearby n,n' inside intervals of length O(H X^(3/5)), recovering the
original short dilated rows. In other cells v can exceed T/H, and the
new off-diagonal shifts must themselves be estimated with the prime,
Möbius and window weights. No quantitative gain within the allowance
has been established. Stop at this unestimated variance rather than
iterating dispersion and claiming a free saving.

## Applicability and sieve boundary

The companion CSV is a hypothesis-by-hypothesis rejection table, not a
claim that all possible theorems have been exhausted. The verified public
candidates are Topacogullari's affine binary divisor problem
https://arxiv.org/abs/1512.05770 and shifted d3,d2 convolution
https://arxiv.org/abs/1506.02608. Their stated divisor objects do not supply
an estimate for these restricted signed prime/Möbius arrays. The first
mismatch is the coefficient class; affine integer forms additionally need
rational clearing and parameter control. No unrestricted divisor saving
is imported. Voronoi/Kuznetsov or spectral large sieve would require a
valid transformation into their automorphic/Kloosterman coefficient
systems and control of sharp masks; that transformation is not provided.
Large sieve/Hilbert mean-value norm bounds alone fail the soft falsifier.

Vaughan/HB identities have ZERO transference remainder algebraically,
but leave every tagged sum unestimated. Replacing coefficients by their
absolute divisor envelopes is an inequality, not a signed transference
with small remainder. In the 2:3 box with coefficients about U^-1/2 and
V^-1/2, U=X^(8/5), V=X^(3/5), coherent mass has scale
H*sqrt(UV)/T=O(H X^(1/10)), before log factors. This upper-bound route
cannot pay a constant allowance. It is not a lower bound on the actual
prime sum, so does NOT certify decision E. No sieve remainder small
in the frozen normalization has been proved; the route stops here.

## Conjugacy and equality-poset structure

Negating all epsilon preserves pi and sends e,m,delta to -e,-m,-delta.
For the same path the Fourier/path weight and K conjugate, while omega
is real. The pair contributes 2*omega*Re(WK); imaginary parts cancel
exactly. The primitive can likewise be paired before evaluating its norm.
The real part need not vanish: its cosine component is even in delta.
Also sum |e_B| is congruent b modulo 2, so fifth and sixth reduced
factor multiplicities have opposite parity. No identical reduced factor
pattern occurs across both degrees; no coefficient-only cancellation of
matching factors is possible. Cancellation between different frequencies
is neither ruled out nor assumed.

For exact equality mask D_pi and unconstrained equality mask E_sigma,

    D_pi=sum_(sigma coarser than pi) mu(pi,sigma) E_sigma,
    mu(pi,sigma)=prod_(C in sigma) (-1)^(r_C-1)*(r_C-1)!,

where r_C counts pi-blocks inside C. For every fixed b,epsilon,m,
c_sigma=sum_(selected pi refining sigma)mu(pi,sigma). The producer checks
56,960 identities sum_(sigma refining rho)c_sigma=1_(rho selected).
There are 24,944 nonzero coefficients. The independent replay instead
solves the triangular zeta recurrence and matches all of them.
This is equality-mask inversion, not a new cumulant expansion. It
reconstructs an indicator equal to one on every survivor; it does not
annihilate the survivor. Raw coefficients grouped by reduced factors are
provided both before inversion and after inversion. These formal scalar
sums cannot merge different signed Fourier weights or path/window masks.
Consequently no lower-complexity connected correlation has been proved.

## Soft falsifier, including conjugacy

Use the frozen certified generic construction: even z, X=z^5,T=2*pi*X,
V=z^3,U=XV=z^8,K=V/10000,H=.01; arrays n^-1/2 on [U,2U),
v^-1/2 on [V,2V), rotating the first by exp(-i*T*L).
Both squared l2 masses are <=1 and their envelopes are <=1/sqrt(variable).
The nonexact core n=Xv+j, V<=v<3V/2, 1<=j<=K lies in m=1.
For root carrier tau between T and 2T its phase magnitude is <=.02,
so real part is >=4999/5000. Counting just this core gives

    Re P >= (4999/5000)*K/(4*sqrt X).

The other atoms in the complete same-sign near window also have positive
cosines; the subset is therefore a valid lower bound. At z=10^10 the
square of this bound exceeds one by exact rational arithmetic. Attach
the conjugate swapped arrays at m=-1: imaginary parts cancel and the
real contribution doubles. Fixed rescaling to restore unit joint l2 mass
only changes a constant, not the X^(1/10) divergence. Sampled Dirichlet
kernel decay is its usual decay, and the near core remains coherent.
Thus support, l2/divisor envelopes, kernel decay and conjugacy alone do
not imply the required primitive bound. These arrays are NOT ordinary
prime arrays, do not satisfy PNT/BV hypotheses, and do not certify a
consumer obstruction. Arithmetic cancellation is necessary beyond the
soft assumptions tested. The independent replay verifies the rational
core lower bound and its comparison with the exact allowance.

## Actual-prime discovery, deliberately scoped

The diagnostic uses all ordinary primes up to the natural cutoff at
X=63,100,215,405, H=100. It evaluates ONLY the original zero-lag path
subset, natural full section [0,d-1], diagnostic a_phi=1. It does not
certify that section as selected-good, include all R6000 paths, or include
proper powers. For an actual finite taper each degree-b component must
be rescaled by a_phi(T)^(-b) before combination. Floating classification
has boundary skips recorded in JSON; this is not interval certification.

    X     unique ratio atoms   sum sup primitive       signed kernel real
    63    70                   .004264313762414169      -.000185757555166153
    100   144                  .008818148912506780      -.000141572772358490
    215   754                  .007884446897366995       .000908853174345317
    405   2090                 .007753910811230841       .000899086240603241

The JSON supplies cancellation ratios, dominant reduced classes and
adjacent log slopes. Ratios at identical frequencies are aggregated
before prefixes. These mixed finite slopes provide no asymptotic decay
theorem, and these charges are not full-survivor ledger charges.

## One minimal sufficient lemma and the decision

Choose ONE declared H0>0 (or one admissible H(T)), retain fixed R6000,
actual a_phi, all original windows and selected principal section above.
For the EXACT jointly signed survivor Q_surv above, prove

    limsup_(T->infinity) Q_surv <= q_alias

with an explicitly certified q_alias and the chosen ledger allocation,
for example q_alias<=s*Delta_rel with s<1. This one-sided bound is weaker
than asking absolute cancellation in every pattern or the vector
primitive target; it asks no auxiliary-family uniformity. The primitive
estimate displayed above is a sufficient stronger route. A quantitative
rate is needed only to the extent required by the declared finite-error
ledger; no unearned o(1) or power-saving is stipulated as proved.

Central is the frozen identity-slope object; this survivor is a dilated
coprime product object. Replacing A by A/X^m fails to preserve integers,
prime-block ranges and weights in general. No reduction in either
direction, or strict hardness ordering, is established. It is therefore
STRUCTURALLY DIFFERENT, with comparison unproved, not decision C or D.

Let J*=64788151489666079/572357731837500000 and preserve the frozen
other excess G_ref=Central+LongTail+B*D6(R)+A/36-B*M6_ref. Total excess
is G_ref+Q_surv+o(1). If a survivor charge q is certified, the reference
allowances become Delta_ideal-q and Delta_rel-q, with a strict reserve
also needed for the other obligations. No such q has been obtained:
charge UNKNOWN, paid remaining allowances UNKNOWN; the reference slacks
are unchanged. This is not a proof that the consumer cannot afford it.

**F. INCONCLUSIVE.** First uncertified step: the prime-restricted signed
primitive/one-sided correlation estimate after exact decomposition.
No uniquely dominant subpiece or applicable saving theorem is certified.
All three closed families stay closed; strict >79 stays OPEN.

Artifacts: survivor extractor/classifier/constructor and identity checks
in src/wp84_near_alias_survivor_lemma.py; independent triangular replay
in src/wp84_near_alias_survivor_replay.py; prime diagnostics in
src/wp84_near_alias_survivor_diagnostics.py. CSVs give every extracted
pattern, reduced factor, equality coefficient and formal reduced sum.
The certificate records exact allocations, counts and SHA256 pins of
frozen sources. Local commit hash is reported after verification.
