# Fifth block 5/7: exact difference and first nonzero amplitude jet

Parent 10aabac9aaab51470c9324ab0f927d299a17899b; isolated branch
codex/c5-c6-attack-20261006. No push. **Decision B: pair analytic rank 2.**
The first nonzero grouped carrier-amplitude jet is u^11, after removing
the common a_phi(T)^(-5) normalization. The complete difference has no
nonzero amplitude jet through u^10. No new global kernel exists for this
pair. The fifth analytic bounds improve to 20..72. Strict >79 remains OPEN.

## Independent source reconstruction and exact physical formulas

The frozen raw extractor WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv contains
representatives +++++/00123 and +++++/01023 with aliases 2,3,4.
These are canonical functional IDs 5 and 7. Reconstruction starts from
these signs/partitions, not the old jets. Let p be the doubled ordinary
prime, and choose an UNORDERED triple {q,r,s} of distinct ordinary primes,
all four distinct and <=N=floor(exp(L-sqrt(L))), L=log(T/(2*pi)), u=1/L.
The six permutations of the singleton triple cover the original ordered
block-prime assignments exactly once. An ordered triple followed by
another six-permutation sum would incorrectly multiply the answer by six.

Let I=[k_-,k_+], n=d'=|I|, R=6000 and c_p=-log p/(a_phi L sqrt p).
Define the n-by-n exact matrices, indexed by actual section integers:

    E_p(i,j)=1_(|j-i|<=R) f_(j-i)^+(log p*u)
                          exp(2*pi*i*i*log p*u),
    f_0^+(a*u)=1-a*u,
    f_l^+(a*u)=(1-exp(2*pi*i*l*a*u))/(2*pi*i*l), l!=0.

The i in the exponential after 2*pi denotes the imaginary unit, while
the final i is the row index. No taper replacement or a_phi=1 is made.
The matrices contain exactly the Fourier filter, row/displacement phase,
endpoint membership and band restriction of the frozen path sum.

For A=p^2*q*r*s, lambda=log A, define the original common mask

    M_A(T)=sum_(m=2,3,4) 1_(m is nearest alias,
                              0<|lambda-mL|<=H/T).

H is the original one fixed positive near-alias width, not optimized.
All natural prime-window indicators are retained. The exact functionals are

    F5=Re sum_(p,{q,r,s}) M_A*c_p^2*c_q*c_r*c_s*exp(i*T*lambda)/n
                   *sum_(sigma in S3)Tr(E_p^2 E_sigma(q) E_sigma(r) E_sigma(s)),
    F7=Re sum_(p,{q,r,s}) M_A*c_p^2*c_q*c_r*c_s*exp(i*T*lambda)/n
                   *sum_(sigma in S3)Tr(E_p E_sigma(q) E_p E_sigma(r) E_sigma(s)).

Both have raw cumulant coefficient 1. Their external frozen consumer
coefficients remain the old orbit-size multiples of omega_5; those
coefficients are not folded into the definitions above or redesigned.

To verify equivalence to the raw path definition, expand each trace over
i_0,...,i_4 in I with i_5=i_0. Put l_j=i_j-i_(j-1),
u_j=sum_(t<=j)l_t, so i_j=i_0+u_j, sum l_j=0.
The allowable root interval is
[k_- -min u, k_+ -max u], M=max(0,n-range u).
The product of row phases is
exp(2*pi*i*(i_0*lambda+sum_j u_(j-1)*log p_j)/L).
Summing i_0 reproduces the FULL sampled Dirichlet kernel
exp(i*T*lambda+2*pi*i*imin*lambda/L)/n
sum_(k=0..M-1)exp(2*pi*i*k*lambda/L). Every factor and normalization
therefore matches the original prime/path atoms, including empty paths.

## Slot swap: exact defect, not a symmetry

Swap zero-based slots 1 and 2: (p,p,q,r,s)->(p,q,p,r,s), carrying their
lags with their primes. Prime coefficients, filter products, carrier,
prime windows and 1/n are unchanged. The prefix displacement sequence
changes, so its prime-weighted phase and sometimes its range/root support
change. This is the first broken factor; the slot order is not a dummy
prime-label permutation.

Explicitly take l=(1,-1,0,0,0). Original prefixes are (0,1,0,0,0,0);
the swapped lags (1,0,-1,0,0) give (0,1,1,0,0,0).
Both root counts are n-1 and imin is unchanged, but the new path phase
is multiplied by exp(2*pi*i*log q/L). This factor is not one for an
allowed ordinary prime, since 0<log q/L<1. The filter factors for the
prime p have lags 1,-1 in both paths and the other filters have lag zero.
Near a sufficiently small nonexact alias residual the root kernel is
also nonzero, so this is an actual termwise defect, not just a label test.
For general paths the exact defect is the changed phase exponential
TOGETHER WITH changed root indicators; a quotient of kernels is used
only where its denominator is nonzero. No raw-path involution proving
F5=F7 exists in this calculation.

## Exact generating difference before Taylor expansion

For arbitrary matrices X,Y,Z,W, cyclic trace algebra gives

    sum_(perms Y,Z,W)Tr(X^2 Y Z W-X Y X Z W)
      =-sum_(perms Y,Z,W)Tr([X,Y][X,Z]W).                 (1)

Expand each commutator into four words and cyclically normalize; all
terms cancel exactly against the left side. This identity does not assume
commuting, symmetric or Riemann-specific matrices. Thus the exact physical
D=F5-F7 is the same outer prime/mask/normalization sum as above, with

    -sum_(sigma in S3)Tr([E_p,E_sigma(q)]
                        [E_p,E_sigma(r)]E_sigma(s)).     (2)

This is a finite exact exponential-polynomial generating expression on
each fixed-combinatorics cell. No jet truncation defines it. It is the
small exact expression for the defect; its commutators need not vanish.
The low-order cancellation is structural commutator cancellation, not
an exact permutation invariance or an all-orders zero identity.

## First commutator coefficient for the ACTUAL finite band

Let a=log p, c=2*pi*i, D0=diag(i:i in I), and J=J_R be the symmetric
0/1 band matrix J(i,j)=1_(|i-j|<=R), including its diagonal. Direct Taylor
expansion of the exact matrix entries gives

    E_p(u)=Id+a*u*H+a^2*u^2*K+O(u^3),
    H=c*D0-J,
    K=c^2*D0^2/2-c*(D0*J+J*D0)/2.

Consequently

    [E_p,E_q]=a*b*(b-a)*u^3*[H,K]+O(u^4), b=log q,
    [H,K]=-c/2*[D0,J^2]=-pi*i*[D0,J^2].                (3)

For the second equality, the c^2[D0^2,J] terms cancel exactly and only
[J,D0*J+J*D0]=J^2 D0-D0 J^2 remains. This calculation retains the
finite R band: replacing J^2 by nJ is valid only in a FULL band.
A shift of the section index origin adds c*k_-*Id to H and corresponding
polynomials in H to K, leaving their commutator unchanged.

Writing W_ij=(J^2)_ij, an exact nonnegative integer intersection count,

    W_ij=max(0,min(k_+,i+R,j+R)-max(k_-,i-R,j-R)+1),
    Z(n,R)=sum_(i,j in I)(i-j)^2*W_ij^2,
    Tr([H,K]^2)=pi^2*Z(n,R).                            (4)

Z depends only on n and R. It is strictly positive for n>=2 and R>=1:
each adjacent ordered pair has W_ij>=2, so Z>=8*(n-1)>0.
For a full band R>=n-1, Z=n^4*(n^2-1)/6. The square in (4) is positive
because the imaginary unit changes the sign of the real antisymmetric
commutator's squared trace; omitting this sign would reverse the result.

## Sequential jets and first nonzero coefficient

Each commutator in (2) starts at u^3, so their product starts at u^6.
The last E_s has constant term Id. Hence the matrix-trace difference has
zero coefficients at orders 0..5, exactly, covering all paths and roots.
The prime coefficient product starts at u^5. Therefore the FULL normalized
carrier-amplitude difference has zero jets through u^10: in particular
the requested orders 9 and 10 vanish. At order 11 the first possible
term is explicitly nonzero, so the sequential search stops there.

Put a=log p,b=log q,c1=log r,d=log s and

    S=b*c1*(b-a)*(c1-a)+b*d*(b-a)*(d-a)
                                  +c1*d*(c1-a)*(d-a).

The order-u^6 trace coefficient in (2) is

    -2*a^2*S*pi^2*Z(n,R),                               (5)

since the six singleton permutations give two ordered copies of each
unordered commutator pair. Meanwhile
c_p^2*c_q*c_r*c_s=-a^2*b*c1*d*u^5/(a_phi^5*p*sqrt(q*r*s)).
Taking the real part halves the positive complex carrier coefficient.
Thus the exact coefficient of u^11 in the POSITIVE grouped carrier
amplitude of a_phi(T)^5*(F5-F7) is

    c11=pi^2*Z(n,R)/n
          * a^4*b*c1*d*S/(p*sqrt(q*r*s)).                (6)

The negative carrier coefficient is its conjugate, here the same real
number. Formula (6) includes all SIX singleton assignments exactly once.
There is no extra six factor. If p<min(q,r,s), every factor and every
summand in S is positive, so c11>0 for every admissible n>=2.
This is an exact sign proof using actual prime logarithms, not their
formal algebraic independence or a floating evaluation.

The physical observable as a whole is not a Taylor function at u=0:
its carrier exp(i*T*lambda), T=2*pi*exp(1/u), has an essential behavior
there. The jet statements concern its faithful grouped amplitudes,
after removing the common degree normalization, exactly as in the parent
cell theorem. No assertion of an actual globally fixed prime set at
T->infinity is made.

## Legal carrier cell and global pair independence

Choose p=2 and distinct large primes q<r<s, for example via successive
Bertrand intervals about a large parameter Y. Their sizes are within
fixed constant factors of Y. Put X0=(4*q*r*s)^(1/2), so L0=(3/2)log Y+O(1).
Then log s<=log X0-sqrt(log X0) for large Y, so all four primes belong
to the ACTUAL natural cutoff. The carrier is an m=2 alias at X0, not a
fake free-carrier point. At the center delta=0 is removed; perturb to a
punctured open residual interval
0<|log(4*q*r*s)-2 log X|<H/(2*pi*X). This exists for ANY fixed H>0.
Avoid the finitely many cutoff, dimension, alias and endpoint-count
boundaries to obtain a fixed-combinatorics cell containing that tuple.
The actual selected section has n asymptotic to d, hence n>=2 at these
large heights. This proof does not claim a small finite endpoint pair
is certified good; the nonzero coefficient holds for EVERY section n>=2.

The reduced carrier 4*q*r*s has its squared prime uniquely identified by
unique factorization. The singleton primes have exactly the six assignments
summed above, and no other assignment of this pair of equality patterns
has this carrier. Thus (6) is the complete carrier coefficient, not a
subset possibly canceled by more assignments. Distinct other carriers
cannot cancel this coefficient by the parent analytic-germ uniqueness
lemma on a fixed cell.

To prove rank TWO, not merely inequality of two functions, suppose
alpha*F5+beta*F7 is globally zero. Their positive-carrier u^5 leading
coefficients on this cell are equal and nonzero, so carrier uniqueness
forces alpha+beta=0. If alpha is nonzero, the relation reduces to a
nonzero multiple of D, whose u^11 coefficient (6) is nonzero, contradiction.
This is valid over Q (indeed over constant real scalars). If the endpoint
selector varies, there are finitely many section branches on this cell;
the same leading/u^11 argument makes the combination nonzero analytic
on EVERY admissible branch. A finite union of their isolated zeros cannot
cover the cell. This supplies global independence without assuming the
actual selector is analytic or assigning a freely chosen section.

The per-carrier amplitudes are finite exponential-polynomials in u and
are entire: all matrix entries are exponentials times linear factors or
constant index-denominator quotients. They are not merely asymptotic
series, and a function flat to all orders would be identically zero by
the analytic identity theorem. Here the u^11 coefficient already rules
out flatness. Extending a frozen cell expression analytically is a test
of identity, not an identification with the moving physical cutoff
outside that cell.

Combining this two-dimensional block with one independent representative
from each of the other eighteen fifth carrier-support patterns gives
rank_5>=20 by the same carrier uniqueness and positivity arguments.
No global rank-72 claim follows; the upper bound remains 72. The sixth
block was not attacked. No new fifth kernel vector (1,-1) exists; the
previous truncated jet kernel disappears at order 11. Formal label rank
remains 72, since it was already an upper bound, not a theorem to reduce.

## Independent replay, defects and corruption

The producer expands arbitrary noncommutative trace words and proves (1)
by exact cyclic cancellation. The independent replay checks that identity
on nonsymmetric integer matrices and separately constructs exact matrix
power series from the ENTRY definitions, using rational c=1 and rational
prime-log surrogates solely to verify the universal algebra. It computes
the complete six-permutation trace sums through their first possible
order 6, verifies exact zero coefficients 0..5, and matches (5) in its
rational c=1 specialization for several full/truncated bands. It also
checks [H,K]=-c/2[D0,J^2] and Tr([H,K]^2)=-c^2 Z/4 exactly. Restoring
c=2*pi*i and the actual logarithms is justified by the symbolic formulas
and positivity proof, not by these surrogate points being legal inputs.

The source reconstruction checks both frozen sign/partition/m lists.
The raw slot-swap example detects the changed log-q path phase even
when its root counts agree. Mutating a first nonzero coefficient destroys
its exact replay; flipping the commutator sign or omitting the band
square would likewise fail the recorded formula. The source SHA256 pins
preserve the original 8,740-class extractor and canonical definitions.
No interval finite-T fallback is needed because the exact coefficient
and legal-cell proof settle independence. No ordinary float is used as
an analytic-rank witness.

## Reusable criterion and short mixed-degree side check

Reusable exact criterion: for a same-sign five-slot family with two
occurrences of one prime and three singleton primes, full singleton
assignment summation, the same fixed band and selected section, compare
X^2YZW with XYXZW. The exact commutator identity (1) applies. If its
matrix germ has the H,K above and the repeated prime is smallest, (6)
proves independence whenever the alias/cutoff support has a legal cell.
In the current catalogue this directly applies to IDs 5 and 7 and their
already paired conjugate raw classes. Other multiplicity/sign layouts
have different words and do not follow without a separate identity.
No full fifth-rank search or sixth investigation is launched.

The mixed-degree carrier sets remain exactly disjoint by valuation parity.
To infer zero intersection of the physically normalized spans one still
needs a common-normalization carrier-germ uniqueness theorem: after
multiplying by a_phi^6, a_phi*H5+H6 must remain in the analytic slow-germ
amplitude class, and the actual global selector/boundary convention must
be determined by its cell identities. For example a fixed translated
edge profile yields a_phi=1-c*u and satisfies the normalization part,
but that profile/extension condition was not proved from a_phi->1 alone.
The pair analysis does not close this mixed-degree lemma, and no mixed
intersection dimension is promoted here.

**B. EXACT INDEPENDENCE:** first nonzero amplitude jet u^11, coefficient
(6), pair rank 2. No new exact kernel. Revised fifth rank 20..72.
Strict >79 and the remaining algebraic-compression/arithmetic debts stay
OPEN. Artifacts are src/wp84_fifth_5_7_exact_difference.py,
src/wp84_fifth_5_7_difference_replay.py, the exact difference certificate
and independent replay JSON. Prior commits and notebooklm_packet are
preserved; no push or consumer change occurs. Local commit is supplied
following additive verification.
