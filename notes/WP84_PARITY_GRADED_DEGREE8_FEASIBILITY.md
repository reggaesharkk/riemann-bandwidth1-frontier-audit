# Parity-graded degree-eight feasibility: diagnostic gates and residual debt

Parent c819938650457a94d3e821c2407a0b1034202f31. Date 2026-10-07.
Branch codex/c5-c6-attack-20261006. Local audit; no push.

**A. DEGREE-EIGHT SAME-PARITY CANCELLATION IS STRUCTURALLY AVAILABLE.**
The statement is diagnostic: exact carrier dictionaries exist, connected
pair-inserted kernels do not all vanish, and a specified zero-displacement
pair subset factors exactly. A rational support-valid quartic square cancels
the limiting coefficients of that subset in both parity sectors. It does
NOT establish model >79, any paid arithmetic norm, or a reduced *analytic*
debt. The remaining seventh/eighth amplitudes must still be controlled.
The theorem/optimization branch stops because certified mu7/mu8 are absent.
No full seventh/eighth-moment theorem is launched.

## 1. Reusable ordinary-prime carrier theorem

For any ordinary-prime b-word, let r_p,s_p be positive/negative occurrence
counts and e_p=r_p-s_p. Unique factorization identifies its exact carrier
lambda=log(A/B) with e, after reducing numerator and denominator. Then

 Omega(A_red)+Omega(B_red)=sum_p |e_p|
   =sum_p(r_p+s_p)-2sum_p min(r_p,s_p)
   =b-2sum_p min(r_p,s_p).                                      (1)

Consequently two orders can share an exact frequency only when they have
the same parity. For a nonempty cutoff-prime alphabet, raw support is EXACTLY

 C_b={e supported on cutoff primes: ||e||1<=b, ||e||1=b mod 2}.     (2)

Sufficiency: realize the signed exponents, then add (b-||e||1)/2 cancelling
prime pairs from that SAME finite alphabet. This characterizes carriers,
not a claim that every summed filtered amplitude is nonzero. No unrestricted
prime outside the cutoff is inserted. For r<=s of the same parity,
C_r is contained in C_s. With an all-distinct restriction, ||e||1=b; such
higher-order configurations cannot share lower-order carriers.

The verifier generates the exact exponent supports for orders 1 through 10
and independently checks (2) against the full integer exponent cube over
three primes. It checks every opposite-parity intersection is empty. The
proof for all primes/orders is (1), not numerical extrapolation.

## 2. Global ratio erratum

Authoritative quantities are

 c5=-11501/12500, c6=137641/250000,
 c5/c6=-620/371, c6/c5=-371/620,
 -2|c5|/c6=-1240/371.                                            (3)

WP84_PARITY_GRADED_RATIO_ERRATUM.csv is the occurrence table for the current
text sources, with actual-ratio / coercivity / superseded-history categories.
It separately records the pre-correction BUG in
WP84_THEOREM_AWARE_DEGREE6_CONSUMER_DESIGN.md, previously line 241.
That live note's value was corrected with an explicit dated erratum quoting
the old wrong statement. Its prior commits remain intact. The exact
candidate JSON already contained the correct ratio; no polynomial or ledger
coefficient was changed. The raw scan is preserved as
WP84_PARITY_GRADED_PRECORRECTION_SCAN.txt and classified as historical evidence.
No NotebookLM packet file is rewritten. Regression scripts are rerun.

The generated erratum table and its evidence scans are excluded from their
own occurrence inventory to avoid recursive self-reporting. Source notes,
scripts and text packet sources are included; binary PDFs are not rewritten.
The audit script records the scan scope explicitly.

## 3. Why degree eight and exact SOS algebra

A globally nonnegative nonconstant real polynomial has even leading degree.
If c7 is nonzero, its degree cannot be seven, so degree at least eight is
necessary. The next SOS parameterization is

 P(X)=v(X)^T G v(X), v=(1,X,X^2,X^3,X^4), G PSD.

With symmetric indices 0,...,4,

 c0=G00,
 c1=2G01,
 c2=G11+2G02,
 c3=2G03+2G12,
 c4=G22+2G13+2G04,
 c5=2G23+2G14,
 c6=G33+2G24,
 c7=2G34,
 c8=G44.                                                       (4)

Physical x=X+1 has support x<=0 iff X<=-1. Keep c4=0 in X, P>=1 on that
half-line, and P>=0 globally. No sharp-kernel sign constraint is imposed.
An order-eight consumer still requires a new bounded realization and
curvature/section/zero-transfer payment; the old degree-six payment does
not become valid merely by changing coefficients.

## 4. Exact 5<->7 and 6<->8 dictionaries

The smallest reduced odd ratio can be 2, using repeated cancelling pairs
at orders 5 and 7. The smallest even reduced ratio can be 1, using three
or four opposite pairs. More informative all-distinct LOWER-word witnesses
are

 5: (+2,+3,-5,-7,-11), ratio 6/385;
 7: same five labels, followed by (+13,-13), same ratio;

 6: (+2,+3,-5,-7,-11,-13), ratio 6/5005;
 8: same six labels, followed by (+17,-17), same ratio.

They are valid once the natural cutoff contains the displayed primes. The
higher word repeats its inserted prime, as necessary for cancellation.
For any e in C_b, a b+2 word in its common class has at least one cancellable
opposite pair; removing ONE such pair gives some b-word in that class.
This characterizes the intersection completely. It does not say that an
arbitrary higher-word lag path reduces to an allowed lower lag path: geometry
must be tracked separately. The explicit lift in section 6 handles that.

Finite three-prime dictionary counts are C5=146, C6=231, C7=344, C8=489;
the intersections have respectively 146 and 231 classes. These are finite
structural diagnostics, not counts for the natural T cutoff.

## 5. Connected-cumulant survival: no universal subtraction kill

For ordinary scalar moments, moment-to-cumulant coefficients on a partition
with k blocks are (-1)^(k-1)(k-1)!. The forward expansion has coefficient
one per labeled partition. There are 21 partitions of shape {5,2} at order7
and 28 of shape {6,2} at order8. Their inverse two-block coefficient is -1.
Bell counts are 877 and 4140. With scalar kappa1=kappa3=0, formal forward
identities are

 M7=kappa7+21 kappa5 kappa2,
 M8=kappa8+28 kappa6 kappa2+35 kappa4^2
                    +210 kappa4 kappa2^2+105 kappa2^4.           (5)

These formulas are combinatorial identities. They are NOT actual matrix
spectator factorization identities. The repo uses ordered cyclic connected
overlap kernels with placement-dependent walk geometry; scalar cumulants
of trace moments are a different object. For example scalar fourth cumulant
of the frozen moments is 1/4-3*(1/3)^2=-1/12, whereas the cycle connected
fourth integral is -1/60. Do not interchange the conventions.

Using the repo's exact ordered-partition compiler, all terms are evaluated
with integer overlap lengths at the following pair-inserted vectors:

 v7=(.6,-.4,.6,-.4,-.4,.3,-.3):
   9366 terms, C7(v7)=-1/5, outer overlap=1/5,
   connected density=-1/25;

 v8=(-.7,.8,-.7,.6,-.4,.4,.2,-.2):
   94586 terms, C8(v8)=1/5, outer overlap=1/10,
   connected density=1/50.                                     (6)

The cancelling pair is explicit in both. Thus the algebraic connected
kernel does NOT universally vanish when a pair can cancel in the carrier.
These exact point evaluations are not full integrated C7/C8 constants and
not an arithmetic filtered-to-sharp bridge. They refute a universal
connected-kernel zero identity; they do not give a positive-measure transport.
Some pair lengths do give zero: the first vector with pair .2,-.2 is one.
No universal sign or pointwise factorization is inferred.

## 6. A usable canonical raw lift: exact finite-band factorization

The raw consumer ledger retains disconnected words. Specify a CANONICAL
subset, rather than call every pair-containing word the same sector:
append to an allowed b-word two leaves from the current ordinary-prime
alphabet with the SAME p, opposite signs and BOTH displacement zero.
Allow both sign orders (+,-) and (-,+). The original path is closed, so
the appended roots coincide with its starting root and admissibility does
not change. The diagonal matrices of that prime are

 D_p,+ = c_p(1-alpha_p) diag(exp(i tau_i log p)),
 D_p,- = conjugate(D_p,+),
 D_p,+ D_p,-=D_p,- D_p,+=c_p^2(1-alpha_p)^2 I.                    (7)

This is an exact identity even if p also occurs in the original b-word.
The appended two slots define the subset unambiguously; each resolved higher
configuration in it has a unique lower prefix. No independence assumption,
root approximation or extra coprimality mask is inserted.

For each exact lambda, summing only this subset gives

 A_(b+2),T^lift(lambda)=k_T A_b,T(lambda),
 k_T=2S0_T,
 S0_T=sum_{p<=N_prime} (log p)^2/(a_phi^2 L^2 p)
                                (1-log p/L)^2.                  (8)

If a lower mask selects a near alias/hard sector, use its lifted image so
the original exact lambda mask is preserved. Additional new-leaf windows
restrict the p-sum and require that restricted coefficient instead. (8)
does not identify the FULL {b,2} cyclic placement class with this subset.

The CLOSED prime-square/PNT measure upgrade, applied after this exact
signed reduction, gives

 S0_T -> integral_0^1 s(1-s)^2 ds=1/12,
 k_T ->1/6.                                                    (9)

This is a diagonal pair factor, not the full second raw moment 1/3.
The natural cutoff 1-1/sqrt(L) and a_phi->1 are retained. No proper-power
or new arithmetic correlation is hidden in S0. Both matrices (7) and the
rational integral in (9) are verified exactly.

Full pair/spectator classes are not known scalar multiples of lower words.
The already certified lower analogy disproves that inference:
15*mu2*Phi4=15*(1/3)*(-1/60)=-1/12, whereas actual {4,2}=-23/420.
The seventh {5,2} is itself an unresolved model constant. Knowing the
second TRACE moment does not identify all interleaved pair contractions.

Even a scalar field z+z^-1 has nonconstant full-amplitude ratios. At reduced
exponents 1,3,5, A7/A5=(7/2,21/5,7) times the squared leaf coefficient;
at exponents 0,2,4,6, A8/A6=(7/2,56/15,14/3,8) times that square.
These are exact binomial coefficients. They refute a universal FULL
A7=constant*A5 or A8=constant*A6 identity, while (8) remains exact for its
specified subset.

## 7. Parity-graded amplitudes and a rational support-compatible candidate

At ordinary-prime level define the rational Liouville character
chi(A/B)=(-1)^(Omega(A_red)+Omega(B_red)). Then

 nu=nu_odd+nu_even,
 B_odd(lambda)=c5 A5(lambda)+c7 A7(lambda),
 B_even(lambda)=c6 A6(lambda)+c8 A8(lambda).                      (10)

Lower odd orders 1/3 and lower even orders 0/2/4 are retained separately
under their inherited gates. They are not part of a free common-pair bound.
Define exact remainder amplitudes R7=A7-k_T A5, R8=A8-k_T A6. Hence

 B_odd=(c5+k_T c7)A5+c7 R7,
 B_even=(c6+k_T c8)A6+c8 R8.                                    (11)

These equations are genuine pre-carrier identities. The remainders include
noncanonical pair placements and genuinely higher reduced-count channels;
they are not known small or supported only outside the old hard region.

The limiting coefficient conditions are

 c4=0, c5+c7/6=0, c6+c8/6=0.                                    (12)

Unlike the degree-six disjoint sign proxy, these are compatible with PSD
and support. An exact rank-one example is

 q(X)=(144000 X^4+14400 X^3-12720 X^2-1128 X-449)/117559,
 P=q^2.

Its coefficient vector, over denominator 13820118481, is

 (201601,1012944,12694944,15765120,0,
  -691200000,-3456000000,4147200000,20736000000).                 (13)

The Gram is the outer product of its five rational coefficients. q(-1)=1
and every coefficient of q(-1-y)-1 is nonnegative:

 y^4:144000/117559, y^3:43200/9043,
 y^2:62160/9043, y:508488/117559, constant:0.

Thus q>=1 on X<=-1 and P>=1 there; P>=0 globally. Equations (12) hold
exactly. This certifies ALGEBRAIC support/cancellation feasibility only.
A useful general rank-one family uses a3/a4=t and

 a2/a4=-t^2/2-1/12,
 a1/a4=t^3/2-t/12,
 a0/a4=-5t^4/8+t^2/24-1/288;

normalize q(-1)=1 when valid. The example takes t=1/10.

Because k_T is not exactly 1/6, (11) for this candidate retains
(k_T-1/6)(c7 A5+c8 A6). The coefficient tends to zero, but multiplying by
an unbounded amplitude norm is not an o(1) proof. An eventual bounded
signed degree-eight gate with positive leading c8 would bound the eighth
Schatten moment by polynomial coercivity and thus bound lower scalar traces;
that is a conditional route to dispose the aggregate coefficient error,
not a gate closed here. No TV error is declared small without its norm bound.

## 8. Higher-model inventory and theorem branch stop

Existing authoritative sources:

* WP84_M7_BELL_ASSEMBLY and wp84_m7_bell_assembly.py: exact PHYSICAL raw
  identity m7=1717/90+SPEC52+C7; no certified values for the last two terms.
  Since m7=E(1+X)^7 and frozen lower moments give exactly 1717/90,
  centered mu7=SPEC52+C7.
* WP80_C7_FULL_EXACT_CERTIFICATE: status LAUNCHED/FAIL-CLOSED, not PASS.
  WP80_C7_PARTIAL_RECOVERY_0_23: 301/397 orbits recovered, 96 missing.
  Proposed C7=-17/360 is not consumed as exact.
* WP81_SPEC52_NUMERICAL_IDENTIFICATION: explicit numerical identification
  only; proposed SPEC52=1/8 and m7=862/45 are CONDITIONAL.
  The independent verifier requires all 450 primitive exact rows; a source
  script capable of verification is not a completed evidence receipt.
* WP84_K8_80_GONOGO_MAP and WP84_K8_MODEL_GONOGO: exact conditional corridor,
  actual model m7/m8 location UNKNOWN.

No completed full exact aggregate/receipt or exact eighth model value was
found in this worktree. Exact mu7/mu8 are therefore unavailable for the
consumer ledger. The rational candidate's model objective is

 known_part=c0+c2/3+c5/36+c6*157/630,
 E_model=known_part+c7 mu7+c8 mu8.                               (14)

The verifier records the exact known_part; it does not guess the missing
moments. There is no certified >79 model value, no numerical moment inserted,
and no theorem percentage. No model SDP is run without its exact objective.
The degree-six model consumer embeds in degree eight with a4=0, but that
trivial embedding supplies no new same-parity amplitude reduction.

Existing exact machinery could in principle complete the finite model work:
C7's remaining 96 orbit integrals, all SPEC52 placement integrals, then the
centered eighth classes {2,2,2,2}, {4,2,2}, {4,4}, {6,2}, {8}. Their labeled
partition counts are 105,210,35,28,1. Placement geometry is retained;
these counts do not turn the classes into products of scalar moments.
C8 has 94586 connected ordered terms in seven free coordinates. This audit
does not run that global polytope calculation or a new moment theorem.

## 9. What arithmetic remains, and what is not an improvement yet

The structurally reduced amplitude target is an upper bound on the complete
real sum of (11), with all frequencies, aliases, repeated labels, root masks,
filters and endpoints, plus lower-order and bounded-transfer payments.
Phase-uniform norms may be applied to these actual odd/even amplitudes;
Haar Parseval on formal prime phases does not become the theorem's base-T
average. The trace does not supply orthogonality of neighboring carriers.
Parity merely separates support in frequency space; it does not justify
paying an L2 evaluation bound without a frame/spacing theorem.

New reduced-count 7 and 8 carriers are outside every lower-order dictionary.
For instance all-distinct seven/eight leaves have ||e||1=7/8 and cannot
cancel lower-degree amplitude. Their balanced nonclosed products include
7:2-vs-5,3-vs-4; 8:2-vs-6,3-vs-5,4-vs-4 and conjugates, together with
all other finite partition populations not disposed by valid support tests.
If c7/c8 are nonzero, these channels require new bounds or exact amplitude
identities, plus noncentral/alias and finite-band comparison control.
They are not automatically harder by a proved lower bound, but they extend
the arithmetic debt rather than eliminate it by (8).

To eliminate ALL possible highest-order channels coefficientwise would
require c8=0; PSD then kills Gram row 4 and c7=0, returning to degree six.
This is a coefficient-level annihilation observation, not a proof that all
higher-channel arithmetic is necessarily large. No claim that degree eight
has a smaller fully paid arithmetic debt is made. No curvature or zero-side
charge is inherited for (13); a bounded realization must be certified anew.

## 10. Liouville projectors and translation diagnostic

Multiplying every ordinary-prime coefficient by -1 changes the ordinary
field X to -X. Each b-word then changes by (-1)^b=chi(carrier). Therefore

 Pi_even P(X)=(P(X)+P(-X))/2,
 Pi_odd P(X)=(P(X)-P(-X))/2                                      (15)

are algebraically exact parity projectors. They preserve within-degree
frequencies and are verified as polynomial identities. The physical matrix
I+X would change to I-X, reflecting the physical spectrum about 1. It has
no proved same zero-side interpretation. The reflected support region and
positive index are different, so this auxiliary observable is not a free
second zero-side certificate. This subroute stops at zero-side compatibility.

Frequency parity projectors commute with translations because both act
diagonally on exact lambda. For the noncentral spectral projector and the
previous averaged bridge multiplier M_a(lambda), the exact reconstruction
is just the sum over parity sectors of M_a^(-1) M_a nu_sector, plus central
and any original endpoint terms. The same multiplier zeros/central debt
and complex primitive bounds remain. Parity creates no proved translation
saving or averaging variable, and the accepted failed strategy is not reopened.

## 11. Exact scoped degree-six necessity statement

Under the current centered model support/SOS conditions c4=0, setting c5=0
gives model coefficient <=3574/4725 by the existing positive quadrature.
With c5 nonzero, ordinary fifth/sixth exact carrier cancellation is impossible
by (1). Together these facts show that fifth information cannot simply be
removed or exactly paired with sixth information in that degree-six program.
They do NOT prove every degree-six arithmetic proof impossible, nor do they
supply a positive lower bound on the actual unresolved amplitude norm.

## 12. Verification and decision scope

wp84_parity_graded_degree8_verify.py checks orders1..10, exact witnesses,
connected survival (6), Bell counts, SOS formulas, exact diagonal pair product,
prime-measure integral, rational quartic support/coefficient constraints,
scalar-factorization counterexamples and parity projectors.

wp84_parity_graded_degree8_recon.py extends the complete small-section Laurent
matrix replay to degrees5..8. It includes all roots/paths at toy R=1,L=7,
primes2,3,5. Same-parity ratios vary across frequencies: 7/5 real range
about [-.765,27.213], 8/6 about [-.181,10.631]. These are numerical
reconnaissance, not natural-height amplitudes or certified concentration
bounds. Exact scalar counterexamples already rule out a universal full
factorization identity. No toy norm is entered into the theorem ledger.

The ratio erratum is explicit and old audit commits remain intact. Consumer
and carrier regressions pass. Decision A means precisely the raw carrier
and canonical-lift gates are available, with the residual debt (11) stated.
It does not assert the full pair class is scalar, exact model feasibility,
fully paid >79 or any seventh/eighth arithmetic transfer. Those remain OPEN.


Proper-power scope for a future degree-eight theorem: the established
bounded-degree-six deletion is not an unconditional raw eighth-moment
bound. The same small-HS/bounded-operator proper-power matrix gives normalized
Schatten-8 norm O_R(L^(-1/4)). For a fixed polynomial with c8>0, a bounded
upper signed polynomial gate forces a bounded eighth norm by coercivity;
Holder then gives o(1) proper-power deletion for all its words. This is a
conditional extension of the existing method, not a closed degree-eight
arithmetic gate. The structural audit uses ordinary prime leaves explicitly.
