# Source jet translation: exact operators and the unevaluated restriction

Input HEAD: `0de8810580164ca442e37043b59d88f2dd9f3f64`.
Branch: `codex/c5-c6-attack-20261006`. Date: 2026-10-08.
This audit makes additive local files. No push, main change, history rewrite,
Downloads checkout change, or notebooklm_packet change.

**Actual intertwining is UNDECIDED.** The exact complete-stack action and its
finite atom/wedge tests are derived below. No actual source-restricted kernel
test or determinant test has been performed. The current source does not
instantiate the source-legal matrix P_B or its coefficient-column space.
The diagnostic small-section matrices cannot supply either object.

The preceding note's decision label E meant that it had reduced the bridge to
a lemma. It did **not** establish the premise "INTERTWINING TRUE" of option E
in the present instruction. Its own certificate has
`frozen_real_row_stencil_closed=null` and `intertwining_matrices_H_x=null`.
This audit corrects that interpretation without altering the prior files.
None of the requested A--E conclusions can yet be asserted honestly:
missing matrix entries are not a nonzero residual, a counterexample, or an
intertwining proof. In particular this is not an option-C certificate with an
invented residual dimension.

## Actual source labels retained

| Block IDs | m | Reduced carrier | Alias | Relative jet orders | Ambient real coordinates per cell | Wedge polynomial degree bound |
|---|---:|---|---:|---|---:|---:|
|15,20,26,28,31,32|6|p q r|2|0..6|14|36|
|10,12,16,17,21,22,25,29|8|p^2 q|2|0..6|14|48|
|36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69|16|p q/r|1|0..8|18|128|
|34,37,39,43,53,56,60,63|8|p^2/r|1|0..6|14|48|

Jet h means coefficient order u^(5+h) after the existing common u^5
normalization. The source code freezes hmax at 6,6,8,6 respectively; the
previous common 0..8 embedding is a sufficient enlargement, not the smallest
block-specific ambient stack. These are **ambient** dimensions, not dim V_jet
or block ranks.

The exact hidden-column sets are respectively
{31,32}, {16,17,21,22,25,29}, {47,49,50,62,65,69},
{37,39,43,56,60,63}. Other columns have visible excess pairs. Hidden q is
summed over all ordinary primes <=N excluding visible carrier primes; the
finite visible exclusion is included in the visible coefficient. Master
moments are S_j(N)=sum_(q<=N prime) (log q)^j/q, j=2..10. Blocks of depth 6
need only j<=8; depth 8 can use j<=10. No moment coordinate is deleted by
this observation, and determinant-visible K is still unknown.

At each source cell retain

    T, L=log(T/(2pi)), N=floor(exp(L-sqrt L)),
    d=floor(TL/(2pi)), I=[a,a+n-1], n/d -> 1,
    carrier valuation, nearest alias, exact masks, a_phi(T),
    every ordered closed path ell in [-6000,6000]^5,
    every injective equality-block prime assignment, every admissible root.

The q mask has no extra slot windows. The older lazy amplitude constructor's
general source_mask parameter must not be replaced by an arbitrary callback.
The translation below is on a cell where that exact mask is unchanged and n
is fixed. If a translation crosses a source-cell boundary, one must subdivide
or separately justify it; no derivative of a Boolean mask is silently omitted.

## Exact source-derived generator, including imaginary companions

For a closed path let v_0=0, v_j=sum_(r<=j) ell_r and
rho=max(0,n-(max v-min v)). The normalized root factor is

    R_a(u)=exp(c0*(a-min v)*lambda*u)/n
           * sum_(r=0)^(rho-1) exp(c0*r*lambda*u), c0=2pi i.

Translate both endpoints by s, keeping n, T, carrier, assignments, paths,
normalization and masks fixed. Every root is translated by s, so exactly

    R_(a+s)(u)=exp(c0*s*lambda*u) R_a(u).

All remaining summand factors are independent of this root shift. Therefore
the **full** complex amplitude Z, including every cancelled q, satisfies the
same identity before and after taking its constant/master-moment coefficient
columns. The external exp(iT lambda) can be retained; it commutes with this
action. No path enumeration or prime approximation is required to prove it.

For J_h=[u^h](Z/u^5), at one fixed cell x,

    J_h(a+s)=sum_(r=0)^h (i eta_x s)^(h-r)/(h-r)! J_r(a),
    eta_x=2pi lambda_x.

Use ordered coordinates (Re J_0,Im J_0,...,Re J_H,Im J_H). Put
C=[[0,-1],[1,0]] and define the infinitesimal generator N_x by

    (N_x y)_0=0,
    (N_x y)_h=eta_x C y_(h-1), 1<=h<=H,

on cell x and zero on other cells. N_x^(H+1)=0, and the translation is

    T_x(s)=exp(s N_x)=sum_(r=0)^H s^r N_x^r/r!.

The certificate serializes the complete sparse matrix N_x/eta_x and every
rational matrix coefficient of T_x in the symbolic variable eta_x*s. These
are source-derived operators on the ambient full stack, **not a basis of the
unknown actual V_jet**. No generic toy stack is substituted for V_jet.

The first real-row equations are

    Re J_1(a+s)=Re J_1(a)-eta_x*s Im J_0(a),
    Re J_2(a+s)=Re J_2(a)-eta_x*s Im J_1(a)
                           -(eta_x*s)^2/2 Re J_0(a).

For a selected real row (x,h), h>0, the first companion covector is

    evaluation(Re,h) N_x = -eta_x evaluation(Im,h-1).       (1)

Whether (1), **restricted to actual V_jet**, belongs to the selected row span
is the remaining test. Its coefficient is explicitly known; its nonzero
class modulo that row span is not. It cannot be reported as a source-legal
failing coefficient without that restriction.

For h=0, evaluation(Re,0) N_x=0 on the entire source stack. Thus the zeroth
real jet is genuinely fixed, with induced generator zero and translation 1.
This does not prove any higher-jet block closure or a nonzero block minor.

The carrier is lambda, not delta=lambda-mL. Removing an integer alias phase
works at physical u=1/L, not coefficientwise at u=0. Replacing lambda by
delta changes N_x. The reduced ordinary-prime carriers in this table are not
1 (unique factorization); their lambda is nonzero. This audit retains all
real/imaginary couplings and all original root and slot orderings.

## Finite kernel test and explicit quotient construction

This paragraph is a conditional algorithm, not an executed actual-source
kernel computation. Let C contain every actual visible and S_j coefficient
column, keeping distinct heights' moments distinct. Let

    V=span{C, N_x^r C : every cell x, 1<=r<=H_x}.

Operators for distinct cells have disjoint supports: N_x N_y=0 for x!=y.
The displayed span is therefore the full invariant Krylov completion, with
no missing mixed words. It is finite even though C involves enormous full
source sums. A basis A of V gives restricted operators D_x through
N_x A=A D_x. Put Q=P_B A, v=number of basis columns, r=rank Q, and let K_0
be a v-by-(v-r) exact nullspace basis of Q.

The necessary and sufficient whole-kernel test is

    F=vertical_stack_x(Q D_x K_0)=0.                       (2)

No numerical translation samples are needed. If (2) holds, N_x ker P is
contained in ker P, so every polynomial exp(s N_x) preserves it. Conversely
translation invariance for all real s implies (2) by differentiation at zero.
Even invariance for every integer shift suffices: the finite polynomial
P exp(sN_x)k vanishes at infinitely many integers and hence coefficientwise.
A finite candidate list of shifts alone does not justify this converse.

An exact residual dimension, **once the matrices are known**, is

    rank F = rank(vertical_stack(Q,{Q D_x}_x))-rank Q.

Its basis and the first nonzero entry of F would give a genuine option C or D
witness. At present v, r, K_0 and F are all unevaluated. The ambient bound
14 or 18 per cell cannot be used as their dimensions.

For construction of H, select independent rows Q_0 of Q and an exact right
inverse L_0 with Q_0 L_0=I_r. Then

    H_x=Q_0 D_x L_0,
    Q_0 D_x=H_x Q_0,
    Q=(Q L_0) Q_0.

The middle equality must be checked on **all** basis columns. H_x is the
unique induced map on im P in these image coordinates; it is not a separate
fit for each determinant column. Including all moment coefficient columns
in V is essential to establish moment independence. H_x acts on row values,
not on the list of functional columns. It can mix row values but uses the
same action for every column.

H_x is nilpotent and the induced maps commute. For a nonzero image dimension
det H_x=0 and H_x has no inverse. The invertible object is instead

    U(s)=exp(sum_x s_x H_x), det U(s)=1, U(s)^(-1)=U(-s).

Its total polynomial degree is at most max H_x, here at most 8. This resolves
the instruction's ambiguity between generator and exponential: N_x is
infinitesimal; T_x(s), or U(s), is the group action.

On the ambient stack a certified bound is

    ||T_x(+-s)||_2 <= sum_(r=0)^H |eta_x*s|^r/r!.

For an induced quotient one can use

    ||U(+-s)|| <= ||P|_V|| ||L|| max_x sum_(r=0)^(H_x) |eta_x*s_x|^r/r!,

where L is a right inverse of P|_V in the chosen norms. No uniform bound on
this right inverse or on its height dependence is proved here. Invertibility
alone is insufficient to transfer a quantitative endpoint score to arbitrary
jets. The previous physical endpoint bound is not re-proved or spent here.

## Exact determinant-level test if the atom test fails

For m=6,8,16,8 put omega=wedge^m P_B, a scalar determinant covector. The
infinitesimal exterior operator is the **derivation**

    D_x^(m)(v_1 wedge ... wedge v_m)
       =sum_(j=1)^m v_1 wedge ... wedge N_x v_j wedge ... wedge v_m.

It is not wedge^m N_x. The correct group identity is

    wedge^m T_x(s)=exp(s D_x^(m)).

Use the actual determinant subspace D generated by the coefficients of the
full source column wedge as a polynomial in its moment variables. Shared
moments require summing their coefficient contributions before taking this
span; allowing independent moments separately in each determinant column
can enlarge it and erase real cancellations. At distinct heights keep their
actual different moment labels.

Every determinant is a polynomial in translations of total degree <=mH.
Thus the sufficient coefficient bounds are exactly 36,48,128,48 in the table.
Let f_alpha be omega times the coefficient of s^alpha in the exterior action,
restricted to D; f_0=omega|D. To test a scalar intertwiner on this potentially
non-invariant D, inspect **every** coefficient:

    f_alpha=j_alpha f_0 for all multi-indices |alpha|<=mH.    (3)

If f_0!=0, choose d_0 with f_0(d_0)!=0, set
j_alpha=f_alpha(d_0)/f_0(d_0), and test
f_alpha(d)-j_alpha f_0(d)=0 on an exact basis of D. This determines the scalar
polynomial J(s). Its nonvanishing on all required source translations is a
separate obligation. If f_0=0, every f_alpha must vanish; otherwise no scalar
intertwiner exists. If all vanish, the determinant is identically zero on
this subspace and supplies no nonzero minor or rank improvement.

If D is itself invariant under all exterior derivations, then a nonzero
one-dimensional quotient has nilpotent generators zero. In that stronger
case (3) reduces to omega D_x^(m)|D=0 for each x and J(s)=1. Without invariant
D, that first-derivative shortcut is unjustified; higher coefficients may
fail. Similarly full atom kernel invariance implies wedge closure on the
full generated image, but atom failure need not imply wedge failure.

No actual D or omega is instantiated in the existing source. Therefore this
audit derives the exact finite wedge test and degree bounds but does not
claim its obstruction disappears under antisymmetrization.

## Existing identities: precise scope and dictionaries

The current local source files listed in the certificate were read, together
with the packet's frozen manifest. Existing packet sources are earlier
snapshots; they do not supply new current P_B entries. Packet PDFs were also
searched read-only for evaluation, gauge, wedge and commutator identities.

* Root-origin gauge: old prefixes v_j -> v_j+c and old i_min -> i_min-c
  correspond to simultaneous prefix compensation and root translation -c.
  Their full phase change is c lambda-c lambda=0. Current physical root
  translation has no prefix compensation, and its action is exp(s N_x), not
  identity. The old gauge identity supplies no invariance of P_B.
* LRSC masked evaluation matrices: old evaluation rows would have to be the
  actual rows of P_B A; old channel columns would have to be actual full-pool
  coefficient columns A; old nonzero injective stencil minor would have to
  be a legal minor of that matrix. These equalities have not been supplied.
  Distinct surrogate nodes or diagonal feature labels cannot instantiate
  them. No LRSC evaluation-rank claim is imported.
* Sharp Fourier commutator: old D=diag(0,...,d-1) acts on Fourier indices;
  old U_y^+ is a sharp partial interval shift and [D,U_y^+] has rank <=2.
  Current N_x acts on jet order and real/imaginary components, while P_B
  restricts source evaluation rows. There is no supplied pullback mapping
  those two spaces/operators. Rank-two displacement therefore gives no
  rank-two actual kernel residual.
* Carrier Gram commutator: old Z=diag(exp(2pi i s_i)) acts on carrier labels
  and [Z,K] is a two-endpoint outer-product difference. It is not the
  nilpotent jet-order generator N_x. The exact Gram endpoint identity does
  not remove the imaginary companion in (1).
* Existing first large-section wedge formula: its common leading direction
  is the exact v_B(S_2), not the vector of ones. Repeated copies vanish by
  antisymmetry, but mixed subleading rows remain. This is compatible with
  the exterior derivation above; it supplies no actual values for (3).

## Replay and current output

Producer: `src/wp84_source_jet_intertwining_audit.py`.
Independent replay: `src/wp84_source_jet_intertwining_replay.py`.
Artifact: `notes/WP84_SOURCE_JET_INTERTWINING_CERTIFICATE.json`.

The replay does not import the producer. It derives the generator directly
from the real/imaginary differential equations, multiplies its exact rational
powers, and compares every polynomial coefficient for composition and inverse.
It checks the universal root-shift binomial coefficients for orders 0..8,
source block/hidden-pair labels, input git blobs, raw file hashes, and every
packet byte hash. These are operator identities for the actual source formula,
not numerical translation samples or full-source kernel evaluations.

Result: **273 exact polynomial/operator coefficient checks passed; 15 hostile
metadata mutations rejected.** The hostile checks cover missing real/imaginary
coupling, arbitrary rows, changed mask, finite prime core, dropped moment
labels, reordered roots/slots, sampled translations, pairwise-only testing,
column-specific H, R400 substitution, and false kernel/wedge/rank promotion.
These rejection checks enforce the stated evidence boundary. They do not
validate source rows that have never been supplied.

The actual block fields dim V, rank P, dim ker P, kernel basis, residual rank,
first actual nonzero residual, H, actual wedge subspace and wedge result are
all explicitly null. This is a deliberate failed prerequisite, not a PASS of
the requested intertwining lemma. No historical selector search, abstract
determinant optimization, endpoint theorem restart, or >79 optimization was
performed. An exact dimension or source counterexample cannot be manufactured
from the source-linked ambient matrices alone.

The next executable calculation requires the actual source row tuple and the
corresponding full-pool coefficient columns (or an exact theorem identifying
their restricted row relations). This is the already-known matrix input
boundary, not a request to reopen its provenance audit. Once those objects
exist, (2) and, if necessary, (3) specify the precise finite calculation.
Until then no A/B premise exists for the requested determinant cash-out:
73 -> 9 is retained, K is unknown, C_(m-1) is unevaluated, correction ranks and
legal visible minors are unknown, fifth rank stays 38--72, V5 intersect V6 is
not computed, and strict >79 remains OPEN. No error is paid or counted twice.
