# Fifth legal stencil and prime realization: E. LEGALITY OBSTRUCTION

Parent e139eeab18f94a9888997ee6f132e6ef2dbf1145, isolated branch
codex/c5-c6-attack-20261006. No push. Preserve earlier audit commits and
notebooklm_packet/. This run does not change any arithmetic consumer.

The four diagnostic full-rank witnesses cannot presently be promoted to
legal full-block rank. The exact obstruction is **complete-cutoff carrier-jet
stencil injectivity at the source-selected large section and R=6000**.
Prescribed-prime realization is available; independent control of the full
canceled-prime sum and section is not. This is a missing theorem, not a proof
that no replacement legal stencil can ever exist. Fifth bounds remain 38--72;
453-family bounds remain 38--453. No new analytic kernel is proved.

## Four frozen targets and exact diagnostic minors

The following determinants are the exact selected square minors already
stored in WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json. They strip only
common row factors -1/(2 sqrt(P_v)) and retain every column-dependent extra
prime weight. The new sparse determinant file reconstructs them independently.

| IDs | Support modulo reciprocal | Size | Diagnostic full-rank depth | Actual certified rank bounds |
|---|---|---:|---:|---|
|15,20,26,28,31,32|[]/[1,1,1]|6|u^11|1--6|
|10,12,16,17,21,22,25,29|[]/[2,1]|8|u^11|1--8|
|36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69|[1]/[1,1]|16|u^13|1--16|
|34,37,39,43,53,56,60,63|[1]/[2]|8|u^11|1--8|

Exact diagnostic determinant values, in that order:

    -12557983112611329360672693682176/102245
    10600421523596981026223449144885838909524952959942656/7035070070035007
    208312094653703779352279160129708198096658241128693400939318034906430782940704744483310087439174860800/8550986578849
    1895256157300960313583604468406628034947611361280/74827563472190529

Every selected row index, column index and amplitude order is retained in
the old certificate and repeated as row labels in the new polynomial file.
Their diagnostic cells have n,R=(2,1),(3,1),(3,2), prime pool
(2,3,5,7,11,13), and three DIFFERENT rational log-surrogate vectors.
Neither the number of pool primes nor the section dimension is a tunable
parameter in the actual frozen consumer. These are the exact reasons the
stencils lack physical admission.

Equality layouts (five digits give the original equality partition):

    ++++-:
      15:00120 20:01020 26:01121 28:01200 31:01230 32:01231
      10:00010 12:00100 16:00121 17:00122 21:01021 22:01022
      25:01120 29:01201
    +++--:
      36:00102 38:00120 42:01002 46:01200 47:01203 48:01211
      49:01213 50:01223
      34:00001 37:00112 39:00121 43:01012
    ++-+-:
      54:00012 59:01002 61:01020 62:01023 64:01112 65:01123
      68:01222 69:01223
      53:00001 56:00112 60:01012 63:01102

All sign words, aliases, layouts and net carrier assignments remain exactly
those of WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json. A repeated-prime
slot cannot be relocated as a dummy variable: it changes path phase.

## Exact physical admission: an iff definition, not a free-parameter model

The source formulas are in WP84_NEAR_ALIAS_AND_LONG_TAIL_DISCHARGE.md,
WP84_FIFTH_BLOCK_5_7_EXACT_DIFFERENCE.md and the canonical ledger. Set

    X=T/(2*pi), L=log X, u=1/L,
    N=floor(exp(L-sqrt(L))), d=floor(T*L/(2*pi)),
    I(T)=[k_-(T),k_+(T)], n=d'=|I(T)|, n/d -> 1, R=6000,
    c_p=-log p/(a_phi(T)*L*sqrt p).

An individual prime/path atom is admissible iff ALL original masks and
factors are evaluated at a common source height T and the following hold:

1. T lies in the theorem's admitted large-height domain. The equality
partition pi and signs are the frozen source descriptor. Block primes are
ordinary primes, injective across different blocks; slots with equal pi
have exactly the same prime. Any ordering convention used to enumerate
assignments is strict, and its full permutation orbit is included once.
Distinct blocks do not require distinct limiting normalized log exponents.
2. Every prime satisfies the original slot-window intersections, including
p<=N. Real parameters z_j cannot replace log of those actual primes.
3. The reduced rational A=product p_block^e_block, lambda=log A, matches
the target carrier. The original alias is an allowed m, is the nearest
alias m=floor(lambda/L+1/2), and 0<|lambda-mL|<=H/T. All original
negative/conjugate pairing and mask factors are retained.
4. I is the section actually selected by the source, lies in the source
matrix index set, and uses its exact endpoints. n is not chosen independently
of T. The source's boundary/taper normalization a_phi is retained and
nonzero. Removing a common a_phi^-5 is permitted only within degree five.
5. Integer displacements l_1,...,l_5 satisfy |l_j|<=6000 and sum l_j=0.
With v_0=0,v_j=sum_{h<=j}l_h, the integer root i_0 satisfies
k_- -min(v)<=i_0<=k_+ -max(v). Empty root ranges contribute zero.
Thus every intermediate endpoint lies in I. The exact filtered entry,
row phase, sampled root kernel and 1/n are used, not sharp overlaps.
6. A COMPLETE carrier-amplitude row sums every injective block-prime
assignment matching A and all admitted paths/roots. In particular canceled
e_block=0 primes range over the complete source cutoff. Selecting finitely
many of them is not an evaluation of that complete amplitude.
7. To use the frozen-cell analytic-germ argument, these admission data
must be constant on a positive-length source combinatorial branch, with
the already required selector/boundary extension. The carrier exponent
exp(i*T*lambda) is external; amplitude Taylor jets are not Taylor jets of
the whole oscillatory functional.

These conditions are necessary and sufficient BY equality with the full
source summand/masks; they are not a new relaxed sufficient surrogate.
A numerical prime tuple alone does not certify conditions 4,6,7. Our legal
cell certificate explicitly leaves full legal minor=None for every target.

A formal algebraic specialization instead substitutes independent real or
rational logs, independent reciprocal-prime weights, and arbitrary D,J.
It may test polynomial identities. It does not satisfy this iff definition.
For example, the surrogate for prime 2 in the first diagnostic row is 1;
log 2<1 because exp(1)>1+1+1/2>2. The rational log assignment is therefore
not a physical log assignment, even before checking the other masks.

## Exact determinant polynomials and extracted factors

Let c0=2*pi*i, D=diag(section indices), J_ij=1_{|i-j|<=R}. The full
signed entry series is

    E_p^eps=sum_{h>=0} (log p)^h*u^h*Gamma_h(eps), Gamma_0=I,
    Gamma_h=eps^h*c0^h*D^h/h!
      -eps^(h-1)*c0^(h-1)/h! * sum_{t=0}^{h-1}D^t J D^(h-1-t).

For any target layout and fixed carrier, the exact coefficient is

    [u^(5+h)](a_phi^5 F)
      = -1/(2*n*sqrt(P_v)) sum_matching_assignments
          W_assignment * sum_{k1+...+k5=h}
          Tr product_slots ((log p_slot)^k_slot Gamma_k_slot),
    P_v=product p^|v_p|,
    W_assignment=product_slots log(p_slot)
       /product_blocks p^((nu_block-|e_block|)/2).              (1)

Formula (1) includes all root/path constraints through D,J and all
assignment multiplicities. In these four supports every assignment has
exactly ONE extra occurrence pair beyond its net carrier. Consequently
its reciprocal-prime weight is x_j=1/p_j, not a free constant to drop.

The builder constructs each selected minor entry as the EXACT polynomial

    M_ij(z_s,x_s,c0) = sum_{alpha,h,beta} C_ij(alpha,h,beta)
                       z_s^alpha c0^h x_s^beta,

where C_ij is an integer, sum alpha equals that row's amplitude order,
and sum beta=1. Here s labels that row's diagnostic cell and p_j the fixed
six-prime model labels. Each row has a certified positive denominator Q_i
clearing its n and factorial denominators. The exact determinant formula is

    D_B = det(M_B)/product_i Q_i
        = (sum_sigma sign(sigma) product_i M_i,sigma(i))/product_i Q_i. (2)

The row/column labels and EVERY coefficient of M_B are saved in
WP84_FIFTH_LEGAL_STENCIL_DETERMINANT_POLYNOMIALS.json. Its compact term
encoding is [integer coefficient, six log powers, c0 power, six reciprocal
prime powers]. Thus (2) is a fully specified polynomial/rational function,
not an unspecified determinant symbol or a rounded sampled value. It has
9,600; 10,330; 78,533; 8,477 stored monomial terms respectively.

The independent replay evaluates those polynomials at the pinned rational
surrogates and recovers all four exact determinant values above. It also
extracts row integer gcds and common log, reciprocal-prime and c0 powers;
the complete factors are in WP84_FIFTH_LEGAL_CELL_CERTIFICATE.json.
At actual primes the log factors and reciprocal factors are strictly
positive and c0 is nonzero. Positive row denominators cannot cause a zero.
The residual sparse determinant is NOT further factorized and no fixed-sign
claim for it on an actual legal domain is made. The displayed diagnostic
nonzero values prove the residual formal polynomial nonzero, but cannot
remove its geometric/pool legality obligations.

For arbitrary selected I and the FULL source prime pool, (1) likewise gives
an exact polynomial after freezing the finite pool and section. Replacing
that pool or I changes the polynomial, not just its evaluation point.
This is the precise obstacle to reusing (2) as a physical certificate.

## Prime realization: the minimal theorem actually proved

Let finitely many prescribed ordinary-prime roles have net exponents e_j.
Choose an allowed nonzero alias m and normalized exponents gamma_j with

    0<epsilon<=gamma_j<=1-epsilon<1,
    sum e_j*gamma_j=m,

and any finite strict ordering inequalities compatible with this cone.
Choose disjoint constant-factor windows

    p_j in [C_j Y^gamma_j, 2 C_j Y^gamma_j],

with fixed positive C_j; for equal gamma_j use C_j=3^j to separate windows.
For unequal gamma_j the windows are disjoint for sufficiently large Y.
Repeated slots use the same chosen role prime, not additional draws.

PNT gives pi(2x)-pi(x)~x/log x; hence for sufficiently large x it is at
least x/(2 log x). Require this lower bound larger than the finite number
of primes needed in a window. Thus every role can be chosen, and strict
inequalities between normalized log coordinates persist: the error is
O(1/log Y), so any fixed positive inequality slack dominates it.
No short-interval PNT or density of unscaled prime logs is asserted.

Define A=product p_j^e_j and choose the HEIGHT AFTER THE PRIMES:
X0=A^(1/m), T0=2*pi*X0. Then log X0=log Y+O(1), and

    log X0-sqrt(log X0)-log p_j
       >= epsilon log Y-O(1)-O(sqrt(log Y)) -> infinity.

All natural cutoff constraints hold for large Y, including floor rounding.
A small continuous perturbation of T0 realizes the original nonzero near-alias
mask 0<|lambda-mL|<=H/T while preserving strict cutoff/order margins.
Avoid the finite prime/floor mask boundaries and use a source-admitted
selector branch when applying the existing frozen-cell theorem. This
constructs unbounded heights with admitted tuples. It does NOT prove a
near-alias tuple exists at every prespecified T, and does not prove a new
selector-extension theorem. At fixed T, the H/T product condition is not
supplied by the multiplicative-window PNT statement.

For the four supports there are explicit nonempty relative-open cones:

    block15: e=(1,1,1), m=1, gamma=(1/3,1/3,1/3);
    block10: e=(2,1), m=1, gamma=(1/3,1/3);
    block36: e=(1,1,-1), m=1, gamma=(2/3,2/3,1/3);
    block34: e=(2,-1), m=1, gamma=(2/3,1/3).

Here e lists visible carrier roles; any extra canceled prime can have
interior gamma=1/2. The certificate also stores the first representative's
full layout exponents, which contain repeated positive slots and may omit
an extra canceled role. Permissible small perturbations of the visible
gammas in the hyperplane e.gamma=m give open ordering cells. These choices
establish admission of individual tuples and leading carrier coefficients.
They do not let us choose the other primes contributing to the SAME carrier.

The canceled-prime pool is all admitted primes up to N, excluding visible
roles where distinctness requires it. Choosing six primes via PNT cannot
remove the other members. This is why finite-tuple realization fails to
supply the needed complete-amplitude realization lemma.

## Section/root obstruction and alternative legal stencil search

At theorem heights d=floor(TL/(2*pi)) tends to infinity and n/d tends to1.
The frozen selected section is therefore unbounded and not an independently
adjustable 2- or 3-dimensional test section. Band R is fixed at6000, not
1 or2. It has no legal continuous parameter in this run. The diagnostic
polynomials use those discrete values as defining coefficients; changing
them changes the polynomial before any prime-log evaluation.

A small-section nonzero witness alone cannot justify passage to large
sections, even with the SAME band. Let M_n(r)=max(0,n-r), the exact number
of roots for a closed path of range r. At R6000 the paths with displacements
(r,-r,0,0,0) for r=1,2,3 are allowable. Then

    H_n=M_n(1)-2M_n(2)+M_n(3),
    H_2=1, but H_n=0 for every n>=3.

For n>=3 the affine combination is (n-1)-2(n-2)+(n-3)=0.
This is an exact counterexample to a general small-section root-count
injectivity rule, NOT a claimed identity among the four target functionals.
Their prime/filter weights also matter. A missing section theorem must use
their actual weighted jets rather than assume that small-section rank survives.

Likewise a nonzero finite-prime projection need not remain injective after
adding more assignment vectors. Signed Fourier jets need not have a common
sign. No positivity proof for the residual four full-block determinants was
obtained, so omitted atoms cannot be dismissed as harmless.

Replacement searches assessed here:

* Changing prime ordering within the strict-slack cone preserves individual
admission but cannot fix the absent full-cutoff sum or small sections.
* Using different legal heights is valid for global independence, as in the
previous three size-four proofs, if every row is a genuine amplitude jet
of the SAME source-defined family. Different arbitrary sections at one
height are not selectable evaluations of that family.
* Higher jets are exactly obtainable from Gamma_h without a model change.
The diagnostic size-16 matrix already needed u^13. Increasing that depth
again does not cure wrong band, pool or section; hence no diagnostic depth
increase was promoted in this run.
* Derivatives in T on an actual frozen cell are legal. Derivatives with
respect to independent log-prime coordinates or section size are derivatives
of an algebraic lift, not evaluations of the source family without an
additional faithfulness theorem.

No full-rank replacement stencil using source-selected sections and complete
prime pools was constructed. This is a stated limitation of this audit,
not an impossibility theorem for every conceivable replacement.

## Analytic continuation: two distinct statements

For a fixed finite prime-pool cardinality, fixed I and R, the matrix entries
and carrier amplitudes have analytic lifts in continuous log coordinates.
A nonzero diagnostic determinant proves the corresponding formal polynomial
is nonzero. This concerns exactly that discrete branch's algebraic model.
It does not imply that the legal physical branch has the same determinant.

One can strengthen the formal statement: clearing row denominators gives
a polynomial in log variables, reciprocal weights x_j and c0 with rational
coefficients. Since c0=2*pi*i is transcendental, a nonzero rational polynomial
coefficient in c0 cannot vanish there. Replacing x_j by exp(-z_j) gives a
finite exponential-polynomial sum in the independent real log coordinates.
Distinct exponent vectors are linearly independent over polynomials: restrict
to a generic line with distinct exponential rates, divide by the dominant
rate, and let its parameter tend to infinity; repeat. Thus this formal
analytic lift is not identically zero, and its zero set contains no real
open region on its fixed finite-pool/small-section branch.

This still leaves TWO separate failures of the desired physical inference:
actual prime logs are discrete at a fixed pool, so no fixed-height open
region of arbitrary real coordinates is prime-realizable; and the large-height
realization construction changes the full cutoff pool and source section.
Those are different analytic branches, not points on the same fixed model.
Analytic continuation in T of a frozen source formula keeps its actual
prime set and section fixed; it does not change N, n or R to diagnostic
values. The physical family is cellwise analytic, not an independently
connected open domain in all diagnostic coordinates.

Therefore formal nonzero -> nonzero analytic lift is established; nonzero
set intersects the COMPLETE admissible physical amplitude domain is NOT.
The two steps must not be merged.

## Actual legal jets and kernel classification

The available inherited fully legal jet in each remaining block is its
order-five carrier row. Its j-th entry is exactly

    w_j=-1/2 sum_ALL_matching_assignments
              product_blocks (log p_block)^nu_block/p_block^(nu_block/2).

Zero-displacement roots cancel n; this coefficient is strictly negative
on any admitted nonempty carrier. It is a rank-one row. Its exact kernel
has basis w_0 e_j-w_j e_0 for j>0. This is a symbolic constant-field basis
at that actual cell, not a rational-log substitute. Beyond this row the
actual complete legal matrices have not been computed/certified here.
These vectors are classified **LEGALITY-UNRESOLVED**, not true identities.

The earlier diagnostic intermediate kernels were broken at deeper
order eleven/thirteen and are **FINITE-JET COINCIDENCES IN THEIR FORMAL
MODEL**. Those tests do not classify the actual legal leading-row kernel.
No vector is proved a TRUE ANALYTIC IDENTITY, and no candidate is counted
as an analytic nullity merely because a finite available legal jet annihilates it.

The smallest missing witness is an actual six-row nonzero minor for
(15,20,26,28,31,32), using formula (1) with complete admissible canceled
primes, R6000 and source-selected large sections. A sufficient general
bridge would prove these complete carrier-coefficient maps injective on
admissible prime-log cones while controlling their root sums. The finite
multiplicative-window realization lemma alone is strictly weaker.

## Rank and evidence boundary

No additional full block closes. Remaining rank bounds are 1--6,1--8,1--16,
1--8, respectively; exact ranks are UNKNOWN. Fifth global bounds remain
38--72 and the previously certified 38-function witness is preserved.
The inherited same-degree carrier uniqueness combines support-separated
legal minors; it does not supply missing within-support minors. Rank72
and a full cross-block direct-sum endpoint therefore are not established.

The user permits the V5 intersect V6 check only if all four close. That
condition was not met, so no new mixed-degree analysis is undertaken.
Its existing status is OPEN, with the common mixed-degree analytic
normalization/selector-extension obstruction unchanged. The 453-family
bounds remain 38--453. Strict >79 remains OPEN; no consumer or arithmetic
estimate was touched.

## Verifier and corruption boundary

src/wp84_fifth_legal_stencil_determinants.py builds every sparse polynomial.
The compact JSON includes complete exact data, not a summary/hash substitute.
src/wp84_fifth_legal_stencil_replay.py independently evaluates its entries
and determinants against the prior full path replay, checks every homogeneous
log degree and reciprocal weight degree, verifies source hashes and extracts
common factors. src/wp84_fifth_legal_stencil_verify.py runs those checks.

The legality certificate distinguishes FORMAL_ONLY from full legal admission;
no new legal minor is claimed. Admission-rule tests reject reversed ordering,
illegal merging, an illegal section and diagnostic-band replacement.
Artifact checks reject a repeated-slot relocation, changed jet coefficient
and zeroed minor entry by comparing with the canonical source and prior
independently replayed exact rows. The synthetic all-conditions-declared
rule fixture is NOT a physical cell certificate. No unknown selector or
prime-pool proof is conjured from a boolean flag.

This suite audits formal witness integrity and necessary admission rules.
It does not certify sufficiency of physical inputs that were never supplied,
and cannot report a newly legal minor. There is no floating-point rank,
tolerance test, new theorem on short prime intervals, or hidden consumer change.

Root translation alone is not the principal section obstruction: replacing
i by i+k in all entries multiplies a fixed carrier amplitude by
exp(c0*k*lambda*u), a common nonzero analytic factor. Its jet transform is
lower triangular with nonzero diagonal and can be inverted on sufficient
orders. Changing section cardinality/band or the complete prime pool has
no such common-factor justification. The replay also checks the root-count
counterexample's zero affine coefficients for every n>=3.
