# Fifth large-block exact rank: B. MAJOR PARTIAL SEPARATION

Parent df5cf745c8fc6acb5bbf2ba85211f86f6b93ac9d; isolated branch
codex/c5-c6-attack-20261006. Preserve all previous commits and
notebooklm_packet/. No push, main change, arithmetic consumer change,
sixth-sector optimization, or mu7/mu8 work.

The certified fifth bounds improve from 29--72 to **38--72**. All three
size-four target blocks now have exact full-column-rank carrier-jet minors.
The remaining four larger blocks have full rank in exact algebraic diagnostic
models, but their minors are NOT promoted to actual analytic rank. This
separation of evidence is essential. No genuine new analytic kernel is proved.

## Frozen seven-block inventory

Support is the pair of net valuation multisets, modulo reciprocal orientation.
The old rank lower bound was one in each block. A layout is the equality
partition in slot order; signs are shown below or fixed for its row. The
complete machine-readable source remains WP84_FIFTH_SHARED_BLOCK_TABLE.json.

| IDs | Support | Size / old lower / upper / old unresolved |
|---|---|---|
|15,20,26,28,31,32|[]/[1,1,1]|6 / 1 / 6 / 5|
|10,12,16,17,21,22,25,29|[]/[2,1]|8 / 1 / 8 / 7|
|36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69|[1]/[1,1]|16 / 1 / 16 / 15|
|34,37,39,43,53,56,60,63|[1]/[2]|8 / 1 / 8 / 7|
|18,23,27,30|[1]/[2,1,1]|4 / 1 / 4 / 3|
|41,45,58,67|[1,1]/[2,1]|4 / 1 / 4 / 3|
|40,44,57,66|[2]/[2,1]|4 / 1 / 4 / 3|

The first two rows have signs ++++- and layouts

    15:00120 20:01020 26:01121 28:01200 31:01230 32:01231
    10:00010 12:00100 16:00121 17:00122 21:01021 22:01022
    25:01120 29:01201.

The size-16 row has

    +++--: 36:00102 38:00120 42:01002 46:01200 47:01203
            48:01211 49:01213 50:01223
    ++-+-: 54:00012 59:01002 61:01020 62:01023 64:01112
            65:01123 68:01222 69:01223.

The second size-8 row has

    +++--: 34:00001 37:00112 39:00121 43:01012
    ++-+-: 53:00001 56:00112 60:01012 63:01102.

The size-four rows have

    ++++-: 18:00123 23:01023 27:01123 30:01203
    +++--: 41:00123 45:01023; ++-+-: 58:00123 67:01203
    +++--: 40:00122 44:01022; ++-+-: 57:00121 66:01202.

All original alias lists, ordinary-prime distinctness conditions, complete
root/section factors, and path coefficients are retained in the certificates.
In particular alias 2 belongs to every member of all three newly resolved
blocks. No formal atom labels have been used as actual prime inputs.

## General exact generating formula

Set u=1/log(T/(2*pi)), c0=2*pi*i, a=log p. Work on a frozen
combinatorial cell and remove ONLY the common degree-five factor a_phi^-5.
For section indices i,j and fixed band R, let D=diag(i) and
J_ij=1_{|j-i|<=R}. The actual signed matrix is

    E_p^eps(i,j)=1_{|j-i|<=R} exp(eps*c0*i*a*u) f_{j-i}^eps(a*u),
    f_0=1-a*u,
    f_l=(1-exp(eps*c0*l*a*u))/(eps*c0*l), l!=0.

It is transpose-symmetric for both signs. Its FULL Taylor expansion is

    E_p^eps=sum_{k>=0} a^k u^k Gamma_k(eps), Gamma_0=I,
    Gamma_k(eps)=eps^k*c0^k*D^k/k!
      -eps^(k-1)*c0^(k-1)/k! * sum_{t=0}^{k-1} D^t J D^(k-1-t).

Thus higher orders need no additional approximate matrix model. Multiplying
and tracing is exactly the closed-displacement/root sum. The J factors
retain every section and band restriction; cyclic trace plus transpose
reversal are valid identities, not guessed path equivalences.

For a layout pi, write nu_l for multiplicity and e_l for net signed
valuation of its block prime. Let A(pi,v) be ALL injective assignments to
block primes matching the fixed reduced carrier v, including assignments
of canceled e_l=0 primes over the entire admissible frozen cutoff. Put
P_v=product_p p^|v_p| and W_assignment=product_slots log(p_slot)
 divided by product_blocks p_l^((nu_l-|e_l|)/2).
The normalized positive carrier coefficient at order u^(5+h) is exactly

    -1/(2*n*sqrt(P_v)) * sum_assignment W_assignment
      * sum_{k1+...+k5=h} Tr product_slots
           ((log p_slot)^k_slot Gamma_k_slot(eps_slot)).       (1)

Any common alias/window factor is retained; on the chosen alias-2 cell it
is the common nonzero factor. Differences use (1) with the signed layout
coefficients. Formula (1) is the general leading-difference rule: the first
h whose fully assignment-summed expression is nonzero is the first jet.
It is testable at arbitrary depth, and separates path phase, prime logs,
root/section sums and multiplicity weights. It does NOT assert that every
such expression factors into a single positive invariant. That stronger
assertion is false as a general algebraic shortcut.

When the expression reduces to a nonzero section invariant times a
prime-log polynomial, nonvanishing must be proved at actual legal primes.
For rank k the relevant k coefficient functionals must form a nonzero minor;
k pairwise differences do not suffice. A rational evaluation of (1)
proves a formal polynomial is nonzero, but does not by itself prove that
the complete actual arithmetic carrier amplitude is nonzero.

## Exact section identities used for promotion

Define Z1=sum(i-j)^2 J_ij^2,
Z12=sum(i-j)^2 J_ij*(J^2)_ij,
Z2=sum(i-j)^2*(J^2)_ij^2.
For every n>=2,R>=1, adjacent pairs give

    Z1>=2(n-1), Z12>=4(n-1), Z2>=8(n-1).

Exactly,

    Tr(DJDJ-DDJJ)=-Z1/2,
    Tr(DJDJJ-DDJJJ)=-Z12/2,
    Tr(DDJJJJ-DJJDJJ)=Z2/2.

These follow by expanding the squared commutators [D,J], [D,J^2] and
symmetrizing (i,j). They hold for R=6000 and arbitrary actual large section
size. Neither a small section nor J^2=nJ is needed for the promoted proofs.
The universal symbolic verifier expands Gamma_k, retains prime-log monomials,
and groups traces only by cyclic rotation/transposition. It proves the
identities below before any rational specialization.

## Block 18,23,27,30: rank four

Carrier p^2*q*r/s; logs a,b,c,d respectively; positive singleton assignments
q/r are both retained. Set

    G0=F18, G1=F27-F18, G2=F30-F18, G3=2F23-F27-F30.

G1 and G2 vanish through order u^9; G3 vanishes through u^10.
Their first complete positive carrier coefficients are

    [u^10]G1= 2*pi^2*Z12/n * a^3*b^2*c^2*d^2*(b+c-2*a)/(p*sqrt(q*r*s)),
    [u^10]G2=-2*pi^2*Z12/n * a^4*b*c*d^2*(b^2+c^2-a*(b+c))/(p*sqrt(q*r*s)),
    [u^11]G3=-pi^2*Z2/n * a^4*b^2*c^2*d*(b-a)*(c-a)/(p*sqrt(q*r*s)).

The leading G0 coefficient is -a^2*b*c*d/(p*sqrt(q*r*s)).
The ratio of the order-ten coefficients is

    r=-a*(b^2+c^2-a*(b+c))/(b*c*(b+c-2*a)).

Choose a large prime p, distinct q,r in [p^k,2*p^k], and s=2, with k=2
or 3. Then b/a,c/a belong to [k,k+epsilon] with epsilon=log 2/log p.
At alias 2 the center is X0=p*sqrt(q*r/2). All primes lie below the actual
cutoff N=X0*exp(-sqrt(log X0)) for sufficiently large p:
X0/max(q,r) is at least p/(2*sqrt(2)), so its logarithmic slack grows like
log p, whereas the cutoff loss is O(sqrt(log p)). The other primes are
smaller still. PNT supplies distinct primes in both intervals for all
sufficiently large p. Perturb the center slightly to the admissible
nonzero-detuning side, then choose a positive-length combinatorial cell;
no use is made of the removed exact-center point. The actual sections have
n>=2. The cells need not have the same n.

The ratio tends to -1/k. The legal coefficient rows in the G basis normalize to

    [1,    0,    0, 0],
    [star, 1,   r2, 0],
    [star, 1,   r3, 0],
    [star, star, star, 1].

The last row is order eleven on either cell, normalized by its nonzero G3
coefficient. Unknown earlier-column entries do not affect the determinant.
The determinant is r3-r2, tending to 1/6. The basis change from the
original four columns has nonzero determinant 2 (up to column ordering).
No pairwise-rank inference is used.

For p>=2^100, epsilon<=1/100. Exact interval arithmetic gives

    r2 in [-20401/40000, -1990000/4080501],
    r3 in [-60601/180000, -5990000/18210801],
    r3-r2 in [1369352579/9067780000, 131918551201/728432040000].

The entire determinant interval is positive. This is a rational certified
minor at legal prime-order cells, not a numerical log surrogate proof.
The displayed threshold controls the ratio enclosure; PNT and cutoff
admissibility require p sufficiently large in addition.

## Blocks 41,45,58,67 and 40,44,57,66: rank four each

For the first take carrier p^2*q/(r*s), with logs a,b,c,d. Use

    G0=F41, G1=F58-F41, G2=F67-F41, G3=F45-F41.

The leading G0 coefficient is -a^2*b*c*d/(p*sqrt(q*r*s)); its two negative
singleton assignments are included. The first difference coefficients are

    [u^9]G1=-16*pi^2*Z1/n*a^3*b^2*c^2*d^2/(p*sqrt(q*r*s)),
    [u^9]G2= -8*pi^2*Z1/n*a^3*b*c^2*d^2*(a+b)/(p*sqrt(q*r*s)),
    [u^10]G3=-2*pi^2*Z12/n*a^4*b^2*c*d*(c+d)*(b-a)/(p*sqrt(q*r*s)).

G1,G2 vanish through u^8 and G3 through u^9. The universal proof uses
16abcd and 8acd(a+b) multiplying c0^2 Tr(DJDJ-DDJJ), and
2a^2*b*(c+d)*(b-a) multiplying c0^2 Tr(DJDJJ-DDJJJ), respectively.

For the second take carrier p^2*q/r^2 and logs a,b,c. Use

    G0=F40, G1=F57-F40, G2=F66-F40, G3=F44-F40.

Here leading G0 is -a^2*b*c^2/(2*p*r*sqrt(q)); there is one assignment.
The first coefficients are

    [u^9]G1= -8*pi^2*Z1/n*a^3*b^2*c^4/(p*r*sqrt(q)),
    [u^9]G2= -4*pi^2*Z1/n*a^3*b*c^4*(a+b)/(p*r*sqrt(q)),
    [u^10]G3=-2*pi^2*Z12/n*a^4*b^2*c^3*(b-a)/(p*r*sqrt(q)).

The corresponding trace polynomials are 8abc^2, 4ac^2(a+b), and
2a^2*b*c*(b-a), with the same section traces as above. These universal
identities and every lower zero are machine-checked, not fitted from samples.

For both blocks G2/G1 at order nine is r=(a+b)/(2*b). Fix negative primes
at 2 and 3 for the first block, at 2 for the second. Let p be large prime,
q in [p^k,2*p^k] for k=6/5 and 3/2. Alias-2 centers are respectively
X0=p*sqrt(q/6) and X0=p*sqrt(q)/2. Since 1<k<2, log(X0/q)
 grows as (1-k/2)log p, and log(X0/p) as (k/2)log p. Thus every prime
is below the same natural cutoff for sufficiently large p. PNT gives q,
and the same admissible perturbation and frozen-cell construction apply.
In particular b>a, so the order-ten pivot is nonzero on every actual
section branch. The ratio tends to (1+1/k)/2, namely 11/12 and 5/6.

Use the same normalized triangular-shaped four-row matrix as for block 18,
with its middle rows now order nine, and final row order ten. Its determinant
is r_(3/2)-r_(6/5). For epsilon<=1/100,

    r_(6/5) in [221/242,11/12],
    r_(3/2) in [251/302,5/6],
    determinant in [-155/1812,-29/363].

The interval is strictly negative. Each basis change has determinant +/-1.
All three promoted minors are valid for the original functionals, arbitrary
large section sizes, fixed R=6000, and actual prime logarithms.

## Adaptive matrices for ALL seven targets: exact but scoped

WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json contains every complete row,
row label, assignment count, exact selected square minor, determinant,
column list and depth history. The builder uses (1) and groups ALL matching
assignments for its specified finite model. In canceled-prime blocks it
sums all extra balanced primes in the six-prime model pool, instead of
silently retaining one prime atom. Column-varying multiplicity weights are
retained: after factoring sqrt(P_v), each extra positive/negative occurrence
pair contributes 1/p. Omitting that weight would change the carrier amplitude.

The three diagnostic specializations use pool (2,3,5,7,11,13), rational
log surrogates (1,2,3,4,5,6), (2,5,7,11,13,17), (3,4,8,9,12,16), and
sections (n,R)=(2,1),(3,1),(3,2), respectively. c0=1 in this universal
algebra test. These are explicitly NOT legal evaluations of the repository's
R6000 selected operator. Prime labels in the pool are genuine integers,
but their assigned rational logs are not log p. No analytic rank is deduced
from these diagnostic minors alone, including the three promoted blocks;
their promotion instead comes from the universal identities/legal minors above.

| Target block | Diagnostic rank by amplitude depth | Actual new lower / upper |
|---|---|---|
|15,20,26,28,31,32|u^9:2; u^11:6|1 / 6|
|10,12,16,17,21,22,25,29|u^9:2; u^11:8|1 / 8|
|36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69|u^9:6; u^11:12; u^13:16|1 / 16|
|34,37,39,43,53,56,60,63|u^9:5; u^11:8|1 / 8|
|18,23,27,30|u^9:1; u^11:4|4 / 4|
|41,45,58,67|u^9:3; u^11:4|4 / 4|
|40,44,57,66|u^9:3; u^11:4|4 / 4|

The search stops at full column rank in each diagnostic stencil; the
size-16 block required depth thirteen, not an imposed order-eleven cap.
The exact determinant values are stored as rational strings in the JSON
(the large numerators/denominators are not rounded). These are evidence of
formal injectivity of those finite evaluation maps only.

At every intermediate depth the exact rational kernel is stored. Independent
replay applies each earlier vector to the final deeper rows and finds a
nonzero residual. Thus these candidates are **FINITE-JET COINCIDENCES IN
THE DIAGNOSTIC MODEL**, not true analytic identities. No surviving candidate
is left ambiguously labeled a kernel. This does not prove absence of every
identity specific to the actual prime/cutoff operator: those would require
testing on its actual carrier sums. No exact path involution proves a new
kernel in this run.

The four unresolved larger blocks therefore remain open at their inherited
lower bound one. The first/smallest is (15,20,26,28,31,32), size six.
Its carrier p*q*r contains both triple occurrences of a carrier prime and
balanced extra primes invisible in the reduced rational. The exact missing
object is an actual legal six-row nonzero minor of (1), with the entire
admissible canceled-prime sum and actual selected-section moments retained.
A sufficient missing theorem would transfer the displayed finite evaluation
stencil to those complete legal amplitudes, without treating the rational
log surrogates, six-prime pool or small R as physical inputs. Merely proving
the formal determinant polynomial nonzero does not supply that theorem.
No higher diagnostic jet is needed to exhibit formal injectivity; the
remaining problem is legality and nonvanishing after summation.

## Structural theorem proved here and its boundary

For fifth words in the three size-four classes above, the following exact
criterion proves full rank: the assignment-summed cyclic/transposed Gamma
jets reduce to the displayed two order-h section-trace polynomials and one
order-(h+1) pivot; the leading coefficient is nonzero; two admissible prime
cells make the order-h ratio differ; the later pivot is nonzero for every
admissible section. Then the explicit four-row triangular minor proves
independence. The independent symbolic verifier supplies the hypotheses
for h=5 (block18) and h=4 (blocks40/41).

This is a shared generating/stencil method, not three numerical rank
computations. It includes ordinary sign-mixed singletons and opposite-sign
repeated primes. No assertion that arbitrary distinct path words are
independent is proved. Additional canceled multiplicity groups require
complete carrier summation before applying the criterion; this is the
boundary of the theorem established here.

## Global witness, cross-block and mixed-degree status

Add IDs 23,27,30,45,58,67,44,57,66 to the previous 29-function witness.
The resulting explicit 38-function witness, stored in the certificate, is

    0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,18,19,23,24,27,30,
    33,34,35,36,40,41,44,45,51,52,55,57,58,66,67,70,71.

Its proof certificate combines the previous support-separated minors with
the three new exact legal minors. The new blocks' basis operations replace
the old single representative, so each contributes exactly three additional
dimensions, not four additional dimensions. Nine new dimensions give lower38.
The four remaining blocks have sizes 6,8,16,8; inherited lower1 each leaves
34 dimensions unresolved. Hence 38+34=72; upper72 remains valid.

Cross-block independence uses the existing same-degree rational-carrier
uniqueness theorem: a frozen-cell analytic relation forces every reduced
carrier amplitude to vanish. Unique factorization assigns each rational
valuation pattern to one of the disjoint support blocks, including the
reciprocal convention. Apply the block minor on its legal cells. Continuation
is of the frozen formula, not of the moving prime cutoff. Common a_phi^-5
factors exactly; section-selector branches cause no zero pivot because all
three new proofs use positive invariants for every n>=2. This supports the
combined lower38, but not full rank72 because four blocks remain open.

V5 intersect V6 remains OPEN. Disjoint ordinary rational carrier sets by
valuation parity are unchanged. A common mixed-degree normalization with
analytic slow germs and selector/boundary extension is still missing;
a_phi -> 1 alone is insufficient. These same-degree minors do not prove it.
No sixth optimization was done. The 453-family now has certified bounds
38--453 because it contains the fifth witness; the sixth lower35 cannot be
added without the mixed-degree theorem. Strict >79 remains OPEN.

## Replay, corruption and artifacts

The builder, universal symbolic expansion, three block certificates, legal
rational interval certificate, verifier and independent replay are
src/wp84_fifth_large_block_*.py. Corresponding JSONs carry all exact rows,
minors, intervals, witness IDs, layouts and source SHA256s.

Independent replay builds signed entries from the Fourier-filter times root
exponential convolution, propagates scalar polynomial states root by root,
and independently enumerates injective block-prime assignments. It checks
ALL seven saved matrices and their selected determinants using a separate
fraction-free Bareiss algorithm. It does not call the producer's entry,
assignment, matrix-series or determinant routines. Universal polynomial
identities are also checked by exact cyclic-transpose dictionaries; finite
section checks are not substituted for those proofs.

Six hostile mutations are rejected: an unclosed displacement; a changed
repeated-prime location in the frozen layout; an altered stored jet coefficient;
deleting one matching singleton assignment; replacing an exact minor entry;
and forcing a genuinely nonzero saved determinant to zero. Each test checks
a defined integrity or algebra assertion, not hypothetical analytic
independence. The independent report identifies all rejected mutations and
counts the intermediate finite-model kernel vectors broken at deeper depth.
No float rank, tolerance, genericity assumption or arithmetic estimate is used.
