# Fifth shared-carrier block rank: partial separation (B)

Parent: 4ab72a687d6a6801f1d374309d23fa023466c2fe. Local isolated branch
codex/c5-c6-attack-20261006. No remote mutation. This is an analytic
independence result for the frozen full path functionals, not an arithmetic
moment estimate. Fifth lower bound 20 -> 29; upper bound 72. Nine new
independent dimensions; seven blocks remain unresolved. No new kernel is
claimed. The mixed-degree intersection and strict >79 theorem remain OPEN.

## Evidence boundary and full representation

Definitions are the 72 degree-five entries of
WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json, including all listed aliases,
prime assignments, section/root factors and closed band paths. The complete
19-block inventory, with every equality layout, sign word and alias list,
is WP84_FIFTH_SHARED_BLOCK_TABLE.json. Neither an abstract word nor an
unweighted displacement proxy replaces these definitions.

On a fixed combinatorial cell set u=1/log(T/(2*pi)), a=log p, c0=2*pi*i.
Strip the common same-degree factor a_phi^-5 only. The exact section matrix is

    E_p^eps(i,j) = 1_{|j-i|<=R} f_{j-i}^eps(a*u) exp(eps*c0*i*a*u),
    f_0=1-a*u,
    f_l^eps=(1-exp(eps*c0*l*a*u))/(eps*c0*l), l!=0.

Multiplying and tracing these matrices, divided by section size n, sums the
actual closed displacements and actual root phases. Each prime slot also
has coefficient -a*u/sqrt(p). Group assignments by the exact reduced
rational carrier; positive carrier amplitude has the factor 1/2 from Re.
Aliases are retained, not discarded. Unique factorization separates these
support blocks (including reciprocal pairing), by the existing frozen-cell
carrier-germ uniqueness argument. Continuation of a frozen formula is not
continuation of the physical prime cutoff. This proof uses that distinction.

Both signs give transpose-symmetric matrices: the off-diagonal entry is
(exp(eps*c0*i*a*u)-exp(eps*c0*j*a*u))/(eps*c0*(j-i)).
Transpose symmetry does not mean Hermitian symmetry.

For D=diag(i) and J_ij=1_{|i-j|<=R}, the expansion is

    E_p^eps=I+a*u*H_eps+a^2*u^2*K_eps+O(u^3),
    H_eps=eps*c0*D-J,
    K_eps=c0^2*D^2/2-eps*c0*(DJ+JD)/2.
    L=[H_+,K_+]=-c0/2*[D,J^2],
    M=[H_+,H_-]=-2*c0*[D,J].

Therefore [E_p+,E_q+]=a*b*(b-a)*u^3*L+O(u^4), whereas
[E_p+,E_q-]=a*b*u^2*M+O(u^3).

Define

    Z1=sum_ij (i-j)^2 J_ij^2,
    Z12=sum_ij (i-j)^2 J_ij (J^2)_ij,
    Z2=sum_ij (i-j)^2 (J^2)_ij^2.

For n>=2,R>=1 adjacent pairs prove Z1>=2(n-1), Z12>=4(n-1),
Z2>=8(n-1). Exactly Tr(M^2)=16*pi^2*Z1,
Tr(LM)=4*pi^2*Z12, Tr(L^2)=pi^2*Z2. These formulas hold for the
band matrix; J^2=nJ is not assumed. Translating the section roots leaves the
commutators unchanged.

## Exact generating identities and criterion

Products below are full matrices. Tr denotes cyclic trace. Direct expansion
and cyclic grouping prove

    sum_perm(Y,Z,W) Tr(X^2YZW-XYXZW)
      =-sum_perm(Y,Z,W) Tr([X,Y][X,Z]W).
    Tr(X^3YZ+X^3ZY-X^2YXZ-X^2ZXY)
      =-2 Tr([X,Y][X,Z]X).

For transpose-symmetric X,Y,Z the two summands on the left agree by
transpose and cyclic trace, so the single-order difference equals
-Tr([X,Y][X,Z]X). This is not a physical interchange of differently signed
prime assignments. The factor 2 is essential in the symmetrized identity.

For A=Tr(X^2Y^2Z+Y^2X^2Z),
B=Tr(X^2YZY+Y^2XZX), C=Tr(XYXYZ+YXYXZ), expansion gives

    A-B=-1/2 Tr([X,Y^2][X,Z]+[Y,X^2][Y,Z]),
    B-C=-Tr([X,Y]^2 Z).

Polarizing the first identity at X=X_s+t*X_t and taking coefficient t gives

    -sum_perm(Y,Z,W) Tr(([X_s,Y][X_t,Z]+[X_t,Y][X_s,Z])W).

These are exact generating forms. A sufficient testable pair criterion is:
(1) assignment-summed words satisfy one of these full matrix identities;
(2) the leading carrier amplitudes are equal and nonzero;
(3) after inserting the displayed commutator expansions the first coefficient
is a nonzero section invariant times a prime-log polynomial at a legal cell.
Then any pair relation first has coefficients summing to zero, and its
next nonzero carrier jet forces both coefficients zero. Distinct words
alone do not meet the criterion. Higher block rank requires an actual minor.

The F5/F7 order 11 is five prime coefficients plus two order-three
same-sign commutators. The path-phase defect is encoded by [D,J^2]; its
squared root sum is Z2. Singleton assignment summation leaves the polynomial
S=bc(b-a)(c-a)+bd(b-a)(d-a)+cd(c-a)(d-a).
The parent coefficient is pi^2*Z2/n*a^4*b*c*d*S/(p*sqrt(q*r*s)).
Choosing repeated p smallest makes S>0. This also explains why a bare slot
swap argument is insufficient.

## All 19 blocks

The two support tuples below are prime valuation multiplicities on each
side, canonicalized against reciprocity. Old/new are certified lower bounds.
The full layout table is in the companion JSON, not compressed away there.

| Support | IDs | Size | Old | New | Unresolved |
|---|---|---:|---:|---:|---:|
| []/[1,1,1] |15,20,26,28,31,32|6|1|1|5|
| []/[1,1,1,1,1] |8|1|1|1|0|
| []/[2,1] |10,12,16,17,21,22,25,29|8|1|1|7|
| []/[2,1,1,1] |5,7|2|2|2|0|
| []/[2,2,1] |3,4,6|3|1|3|0|
| []/[3,1,1] |1,2|2|1|2|0|
| []/[4,1] |0|1|1|1|0|
| [1]/[1,1] |36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69|16|1|1|15|
| [1]/[1,1,1,1] |33|1|1|1|0|
| [1]/[2] |34,37,39,43,53,56,60,63|8|1|1|7|
| [1]/[2,1,1] |18,23,27,30|4|1|1|3|
| [1]/[2,2] |14,19,24|3|1|3|0|
| [1]/[3,1] |11,13|2|1|2|0|
| [1]/[4] |9|1|1|1|0|
| [1,1]/[1,1,1] |52,71|2|1|2|0|
| [1,1]/[2,1] |41,45,58,67|4|1|1|3|
| [1,1]/[3] |35,55|2|1|2|0|
| [1,1,1]/[2] |51,70|2|1|2|0|
| [2]/[2,1] |40,44,57,66|4|1|1|3|

## First separating positive carrier amplitudes

All coefficients include the five slot weights, 1/n and the Re factor 1/2,
and refer to a_phi^5 times the functional. Let a=log p,b=log q,c=log r.
The first orders below have no lower nonzero difference jet, by the exact
identities. Coefficients belong to the actual logarithmic field; algebraic
independence of prime logarithms is not assumed.

| Difference | Order | Coefficient |
|---|---:|---|
|F1-F2|11|pi^2 Z2/n * a^5 b^2 c^2(b-a)(c-a)/(p^(3/2)sqrt(qr))|
|F11-F13|10|2 pi^2 Z12/n * a^5 b^2 c^2(b-a)/(p^(3/2)sqrt(qr))|
|F35-F55|9|16 pi^2 Z1/n * a^5 b^2 c^2/(p^(3/2)sqrt(qr))|
|F51-F70|9|16 pi^2 Z1/n * w^4 abc(ab+ac+bc)/(s sqrt(pqr))|
|F52-F71|9|32 pi^2 Z1/n * abc v^2 w^2(ab+ac+bc)/sqrt(pqrst)|

In the last two rows w=log s and v=log t (interchanging v,w has no effect).
F51 has repeated negative s; F52 has two distinct negative primes.
Assignment counts are respectively 2,1,2,6,12. No extra permutation factor
is appended. For F1 choose p<q,r; for F11 choose p<q. The other polynomials
are strictly positive for distinct primes. Legal cells are the previously
constructed interior prime exponent cells: p^3qr, p^3q/r, p^3/(qr), pqr/s^2,
pqr/(st), with the listed alias channel. Ordering primes within disjoint
constant-factor intervals preserves their interior logarithmic exponents.
At sufficiently large height each such interval contains primes by PNT.
All actual section sizes are >=2; hence positivity is uniform across their
possible selector branches. This is an analytic existence argument, not a
weighted prime sum asymptotic.

## Three-column certificates, not pairwise rank inference

For block (3,4,6), use G0=F6,G1=F3-F4,G2=F4-F6.
Their first difference coefficients at order 11 are respectively

    G1: pi^2 Z2/(2n)*a^3 b^3 c^2(b-a)^2(a+b-c)/(pq sqrt r),
    G2: pi^2 Z2/(2n)*a^4 b^4 c(b-a)^2/(pq sqrt r).

The leading order-five coefficient of G0 is -a^2*b^2*c/(pq sqrt r),
while both differences vanish to that order. Their ratio at order 11 is
R(c)=c(a+b-c)/(ab). Choose the same two large doubled primes p!=q and
use two legal cells with singleton r=2 and r=3. The alias-2 carrier centers
are X0=pq sqrt(r); at these heights both doubled primes are below cutoff,
and each frozen formula extends over a positive-length cell. In the prior
alias parametrization their logarithmic exponent is interior (approximately
1/2). Increasing p,q keeps section size >=2 and pq>6.

The three normalized carrier-jet rows, in the displayed basis, are

    [1,       0,       0],
    [star1, R(log 2),   1],
    [star2, R(log 3),   1].

The determinant is exactly

    (log 2-log 3)*(log p+log q-log 2-log 3)/(log p*log q) != 0.

These rows may come from different cells. A global analytic relation must
satisfy every frozen-cell carrier equation, so a multi-cell minor is valid.
Unknown G0 higher jets cancel from the determinant. No common section size
between cells is required; it cancels in the row ratios.

For block (14,19,24), use G0=F19,G1=F14-F24,G2=F24-F19.
Their first nonzero difference coefficients are

    G1 order 10: -2*pi^2*Z12/n*a^3*b^3*c^2*(b-a)^2/(pq sqrt r),
    G2 order 11: pi^2*Z2/(2n)*a^4*b^4*c*(b-a)^2/(pq sqrt r).

Here r is negative, and p,q doubled positive. The leading G0 coefficient is
again -a^2*b^2*c/(pq sqrt r). The order-five, order-ten, order-eleven rows
normalize to a lower triangular matrix with diagonal 1. Before normalization
its determinant is the product of these three displayed nonzero pivots.
Any interior legal p^2*q^2/r alias cell with p!=q suffices. The transpose
identity relating the B layout to its swapped assignment preserves signs;
it is not a replacement of negative r by a positive singleton.

All basis changes above are invertible integer row/column operations. The
certificate therefore concerns the original functionals, not just formal
differences. Baseline ranks of the remaining blocks use the established
nonzero leading carrier coefficient. Combining the separated support blocks
produces the following explicit 29-functional witness:

    0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,18,19,24,
    33,34,35,36,40,41,51,52,55,70,71.

Its certificate is the direct combination of the support-separated
nonzero baseline pivots, six pair minors (including parent F5/F7), and the
two three-column minors above. Carrier-germ uniqueness, rather than a
numeric determinant of sampled T values, justifies the combination.

## Unresolved scope and mixed degree

The seven rows with positive unresolved dimension are not certified beyond
rank one. The first is (15,20,26,28,31,32): canceled prime valuations introduce
multiple multiplicity groups within a fixed reduced carrier, so the simple
repeated-X assignment identity above does not supply a complete carrier
coefficient matrix. The same limitation affects the other six larger blocks.
Their full source definitions and all slot layouts are retained in the block
table. This run has not computed their full low-order matrices or exhausted
all possible higher jets. In particular, their unresolved dimensions are
not kernel vectors. No candidate relation has been promoted to a genuine
identity by a raw-path involution. Decision B is partial, not a claim that
all fifth blocks have been analyzed to their first separating order.

The fifth/sixth disjoint carrier supports still do not establish a direct
sum of the actual normalized families. One needs a common normalization
under which every mixed-degree coefficient is an analytic slow germ on
admissible selector/boundary cells, with the corresponding uniqueness
extension. The fact a_phi tends to 1 supplies no such analyticity theorem.
The present same-degree proof removes a_phi^-5 exactly and cannot remove
both degree factors simultaneously. Thus V5 intersect V6 remains OPEN.
The certified 453-family bounds remain 35 <= rank <= 453: the new fifth
bound 29 cannot be added to the sixth lower bound without this lemma.
There is no consequence for the strict >79 arithmetic estimate, which is
OPEN. No consumer budget or moment bound changes.

## Reproducibility and failure-test boundary

Builder: src/wp84_fifth_shared_block_rank.py. Witness:
WP84_FIFTH_SHARED_RANK_WITNESS.json. Verifier:
src/wp84_fifth_shared_block_verify.py. Independent replay:
src/wp84_fifth_shared_block_replay.py and its JSON output.

Replay reads the actual sign/equality descriptors and enumerates all
same-exponent prime assignments. It independently constructs both signed
entry series and checks nine first coefficients on sections (n,R)=(2,1),
(3,1),(3,2), including all lower zeros. This is 27 exact Fraction checks.
The algebraic identities above, not finitely many section tests, establish
the universal theorem. In rational replay c0=1, so
Tr(M^2)=-4Z1, Tr(LM)=-Z12, Tr(L^2)=-Z2/4; restoring c0=2*pi*i
recovers the displayed signs. No floating rank computation occurs.

Failure tests detect an unclosed altered displacement, uncompensated root
change in the exact phase, a missing singleton assignment (six becomes
five), an altered prime-log exponent, and forcing the parent first
coefficient to zero. These are integrity/algebra detectors, not a proof of
all conceivable path involutions. Source hashes are checked by the
certificate verifier. An initial derivation missed the factor two in the
symmetrized cube identity; independent replay rejected it, and the final
coefficients above include the correction.
