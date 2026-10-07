# Carrier-aware degree-six consumer: exact common-frequency obstruction

Parent c402000ac35b9d06c05f7981d9c3ece7bde35807. 2026-10-07.
Branch codex/c5-c6-attack-20261006. Local additive audit; no push.

**D. COMMON-CARRIER FIFTH/SIXTH CANCELLATION DOES NOT EXIST**, for the
ordinary-prime object after the permanently CLOSED proper-power signed-gate
reduction. The first mismatch is exact prime-factor parity. This is an
algebraic theorem, not a sharp-kernel sign proxy or a new number-theory bound.
It does NOT prove every degree-six consumer impossible, and it does NOT
supply a true complex-dual lower bound exceeding the budget.

The user explicitly instructed stopping at gate 2 if no nontrivial common
classes exist. We stop consumer optimization there, while documenting the
exact amplitudes, symmetry, budget boundary and finite replay. No order-eight
optimization or fifth-free consumer search is performed.

## 1. Actual finite-T amplitudes, with exact selected roots

Keep L=log(T/(2pi)), N_prime=floor(exp(L-sqrt(L))), R=6000, h_grid=2pi/L,
I=[k_minus,k_plus], d'=|I|, a_phi and the same selected principal section.
Let n_j be ORDINARY primes <=N_prime, epsilon_j in {+1,-1}, |l_j|<=R,
sum_j l_j=0, u0=0, u_j=sum_{a<=j} l_a. Repeated primes are retained.

 c_p=-log p/(a_phi L sqrt p), alpha_p=log p/L,
 f0^epsilon(alpha)=1-alpha,
 f_l^+(alpha)=(1-exp(2pi i l alpha))/(2pi i l),
 f_l^-(alpha)=conjugate(f_l^+(alpha)).

The exact arithmetic frequency is

 lambda=sum_j epsilon_j log n_j=log(A/B),
 A=product_{epsilon_j=+1} n_j, B=product_{epsilon_j=-1} n_j.

Keep geometry label gamma consisting of ordered leaves, signs, lag path,
section and any hard-window or coprimality restriction. For the exact repeated
compression the admissible roots are

 i_min=k_minus-min_j u_j, i_max=k_plus-max_j u_j,
 m_l=max(0,d'-(max_j u_j-min_j u_j)).

For m_l>0 define the root factor

 S_l(lambda)=d'^(-1) sum_{i=i_min}^{i_max} exp(i h_grid i lambda)
            =(m_l/d')exp(i h_grid i_min lambda)D_m_l(lambda/L),
 D_m(z)=m^(-1)sum_{k=0}^{m-1}exp(2pi i k z).                      (1)

Set it to zero for an empty root interval. This retains every selected
section restriction, without using an o(1) boundary replacement. The
carrier-free configuration amplitude is

 a_b,T(gamma)= [product_j c_nj f_lj^epsilon_j(alpha_nj)]
             exp(2pi i sum_j epsilon_j u_(j-1) alpha_nj)
             S_l(lambda_gamma).                                (2)

The consumer coefficient is NOT inside a_b. Then the exact ordinary trace is

 tau_I X_R,I^b = sum_gamma exp(i T lambda_gamma) a_b,T(gamma).

If roots are replaced by the common full-section factor, (1) becomes
exp(i h_grid k_minus lambda)D_d'(lambda/L) and the previously separated
weighted endpoint/reprojection charge is required. We use (1), so no such
replacement is hidden in the new representation.

Group by the reduced rational ratio r=A/B (or the equivalent signed prime
exponent vector). Sum ALL permitted paths and labels within that class:

 A_b,T(r)=sum_{gamma: A/B=r} a_b,T(gamma),
 B_c,T(r)=c5 A_5,T(r)+c6 A_6,T(r),
 contribution=Re sum_r exp(iT log r) B_c,T(r).                     (3)

Refining by additional gamma labels is allowed, but summing them first
permits more within-degree cancellation and gives the strongest classwise
TV bound. Restrictions defining U must be applied before summing; full trace
amplitudes and unresolved-subset amplitudes are distinct. Coprimality is an
additional mask for all-distinct product sectors, not an assumption about
all repeated-label configurations. Near aliases remain in (3) at their
EXACT lambda, with their original Dirichlet/root factor.

## 2. Exact carrier equivalence classes and the parity theorem

For each prime p let r_p and s_p be its occurrence counts on the positive
and negative sides. Let e_p=r_p-s_p. After cancelling A and B, unique
factorization gives the reduced ratio

 r=product_p p^e_p,
 Omega(numerator(r))+Omega(denominator(r))=sum_p |e_p|.

Since every ordinary-prime leaf contributes one occurrence,

 b=sum_p(r_p+s_p),
 sum_p |e_p|=b-2 sum_p min(r_p,s_p).                              (4)

Therefore the reduced prime-factor count is congruent to b modulo 2.
Degree five has ODD reduced count; degree six has EVEN reduced count.
If lambda5=lambda6, injectivity of log gives equal positive rational ratios,
and unique factorization gives equal e_p. Equation (4) would make the SAME
integer both odd and even. Contradiction.

Thus E_lambda has configurations from at most ONE of degrees five/six.
The theorem includes every sign pattern, all repeated primes, all filters,
all lag paths, all root intervals and all alias partitions, because none
of those changes (4). Additional geometry labels cannot create an overlap.
Zero frequency occurs only for the even degree, not degree five.

For an all-five-distinct hard tuple, no cross-side cancellation is possible,
so sum |e_p|=5 exactly. It also cannot share a carrier with first/third-order
ordinary words, whose reduced count is <=1 or <=3. Lower-order scalar gates
cannot be repurposed as a free aligned fifth cancellation theorem. Repeated
fifth words may share lower odd frequencies, but their complete lower-order
contribution is the already inherited o(1) gate, not a new model gain.

Exact lifts clarify the mismatch: adding an opposite-sign p/p pair changes
leaf count by TWO. Splitting an ordinary prime into two ordinary primes is
impossible. Adding one unrestricted prime changes the ratio and carrier.
Using a composite pq as one leaf violates the ordinary prime restriction
unless it is a proper prime power, which belongs to the disposed population.
No allowed exact fifth-to-sixth ordinary lift exists.

## 3. Proper powers and alias caveats: scope must remain explicit

The RAW prime-power object can have common fifth/sixth carriers. For example

 (4,3,5,7,11) with signs (+,-,+,-,+),
 (2,2,3,5,7,11) with signs (+,+,-,+,-,+)

both give ratio 220/21. This is a real scope counterexample: one p^2 leaf
can split into two same-sign p leaves. It does not contradict (4), which
counts ordinary-prime leaves. The exact grouping verifier tests it.

The permanently CLOSED reduction is COMPLETE bounded signed-gate equivalence:
proper-power matrix Schatten-6 norm O_R(L^(-1/3)), plus coercivity and Holder,
yields o(1) difference of the complete signed fifth/sixth functional when
either gate is bounded. It is not a per-class L1/TV disposal theorem. We
apply that gate reduction BEFORE the carrier partition. Consequently the
surviving theorem-relevant ordinary object has no common carrier, but this
run does not assert that raw proper-power amplitude TV is o(1).

Periodicity of D does not change exact frequency. If lambda differs by mL,
its base phase differs by exp(iTmL), which is not uniformly one. Heights
with accidental equal phase do not define a common exact lambda class or
a phase-uniform identity. Exact nonzero aliases stay CLOSED; near aliases
cannot evade the ordinary parity theorem. Approximate frequency agreement
is not exact agreement, and exploiting it would require a new estimate.

## 4. Carrier-free joint amplitude and the exact ratio certificate

Extend each degree's amplitude by zero outside its support. For every r,

 B_c(r)=c5 A5(r) on odd-parity support,
 B_c(r)=c6 A6(r) on even-parity support.                           (5)

There is no cross-degree vector cancellation before the base carrier.
The frozen centered coefficients have c5/c6=-620/371, equivalently
c6/c5=-371/620. This directly verified ratio is recorded, but cannot pair spectra
with disjoint support.

The requested rho=-A5/A6 is undefined on fifth-only nonzero classes because
A6=0. On sixth-only classes with A6!=0 it is exactly zero because A5=0.
On zero-amplitude classes it is 0/0 and undefined. The common-carrier domain
is EMPTY EXACTLY, so real/imaginary parts, modulus, variation and concentration
of a nontrivial common ratio have no domain. The interval ratio certificate
records an empty set, rather than rounded near-equal frequencies.

## 5. Exact +/-lambda symmetry

Hold L, cutoff, section and filters fixed while viewing the base phase t
as an independent real variable. Each ordinary-prime Fourier matrix satisfies
M_(p,-)=M_(p,+)^*, as follows directly from

 f_l^+(alpha) exp(-2pi i l alpha)=conjugate(f_l^+(alpha)).

Thus X_R,I(t) is Hermitian for every real t. Adjoint reverses each closed
word, reverses its directed displacements and changes all prime signs. It
preserves exact root admissibility and maps lambda to -lambda. Summing all
adjoint configurations yields

 A_b(-lambda)=conjugate(A_b(lambda)).                             (6)

The statement holds on U when its masks include their adjoint images; if a
refined cell is not invariant, pair it with that image instead. Zero-frequency
amplitude is real. With B=a+ib, each nonzero pair contributes

 2 Re(exp(iTlambda)B)=2[a cos(Tlambda)-b sin(Tlambda)].             (7)

The TOTAL imaginary part vanishes, but the sine term does not disappear.
There is no proof that individual amplitudes are real. The full finite-band
replay explicitly contains nonzero imaginary coefficients. Pairing +/-lambda
therefore does not create a fifth/sixth common carrier or erase the carrier.

## 6. Norm audit and budget boundary

For counting-measure norms on exact classes, disjoint support proves

 TV(B_c)=|c5|TV(A5)+c6 TV(A6), c6>=0,
 ||B_c||2^2=c5^2 ||A5||2^2+c6^2 ||A6||2^2.                       (8)

Any shared nonnegative frequency weight gives the analogous identity.
Summing path amplitudes first may reduce each degree's norm, but introduces
no fifth/sixth overlap. Phase evaluation obeys Re sum exp(iTlambda)B<=TV(B).
For M nonzero classes Cauchy only gives <=sqrt(M)||B||2. Thus if a VALID
residual reference has already been subtracted, a sufficient TV allowance
is epsilon, or an L2 allowance epsilon/sqrt(M); for +/- pairs use their
factor-two norm convention consistently. The norm in (8) is not itself a
bound on the signed arithmetic gate without this evaluation inequality.

Formal independent prime phases give exact Laurent-polynomial Parseval:
integrating over their Haar torus makes different exponent vectors orthogonal.
The theorem does NOT contain that torus average. Nor is there a new base-T
average: its root sample average is already precisely (1). Sampled inner
products of two carriers are Dirichlet factors, generally nonzero, rather
than Kronecker deltas. Near products are precisely the regime in which this
orthogonality fails. Hilbert/large-sieve estimates depend on frequency spacing
and the actual interval length; the earlier long-product gap is not fixed
by parity. Schatten estimates may bound the entire signed polynomial, but
no new normalized bound is obtained here. There is no unproved norm saving.

The exact accepted slack values are

 epsilon_ideal=27704610381502/17886179119921875,
 epsilon_relaxed=52897896569489/572357731837500000.

These pay ERRORS relative to a proved favorable reference/model, together
with all other unpaid charges. For a reference with error amplitudes E_b,
a sufficient condition is

 |c5|TV(E5)+c6 TV(E6)+other certified positive charges
       < the chosen epsilon,                                   (9)

or the analogous valid evaluation bound in a different norm. No positive
reference-measure or error-amplitude comparison is supplied by this run.
Replacing E_b by the unreferenced A_b and claiming (9) proves the old model
gain would be incorrect. The reference itself is part of the arithmetic debt.

Indeed the frozen sharp pair-only reference has consumer defect
334737684433/2064615000000. Adding the inherited band/variance payments
exceeds 21/200 by 66998281104243827/1144715463675000000. This reference requires
a NEGATIVE arithmetic gain, not merely a small positive bound on the raw
nonexact amplitude. It is a sharp-model diagnostic, not a replacement for
the filtered pair theorem. No finite numerical amplitude allowance for the
unreferenced actual U has been proved. The slack is not silently reused.

## 7. The hard N^(1/6) region and search stop

The ordinary 2-vs-3 all-distinct geometry p,p~X^(3/5) versus q,q,q~X^(2/5)
has reduced count five. Every ordinary sixth companion, including 2-vs-4
and 3-vs-3, has even reduced count. Its exact N_cell=X^(6/5), shift range
O(H N_cell^(1/6)), restricted arrays, coprimality and K_T(n,h) are unchanged.
No carrier-aligned lift reduces the required shifted correlation theorem.
One can still seek a GLOBAL joint signed inequality using distinct phases,
but it is not exact pre-carrier cancellation and remains new arithmetic.
This result does not compare the difficulty of every possible norm theorem;
it rules out the specific aligned-fifth/sixth mechanism requested here.

The best single-square and best SOS searches are NOT rerun because gate 2
fails exactly and the user instructed stopping there. The preserved rational
consumer is verified again, but is not called a new carrier-safe optimum.
Its exact support is X<=-1, c4=0, and frozen ratio -620/371. The c4=c5=0
model bound <=3574/4725 remains frozen; no fifth-free retry occurs.
No true complex dual Delta_min>budget is proved: disjoint spectra establish
norm decomposition, not a lower bound on either degree's actual amplitudes.
It remains possible that within-degree cancellation or another arithmetic
estimate makes them small; this run does not certify that.

Order eight is not optimized. The stop gate makes that diagnostic unnecessary.
Algebraically parity separates every odd order from every even order; orders
5 and 7 can share carriers by adding a cancelling prime pair, and 6 and 8
can do likewise. That observation is not a permitted unrestricted free-prime
insertion theorem, an amplitude cancellation certificate or a >79 result.

## 8. Verification files and evidence boundary

wp84_carrier_aware_exact_grouping.py verifies all signed ordered configurations
of degrees 5/6 over primes 2,3,5: 7776 and 46656 tuples, 146 and 231 exact
rational frequency classes, intersection EMPTY. It also checks reciprocal
closure, the fifth absence of zero frequency, and the raw proper-power
counterexample. The all-prime theorem is (4), not extrapolation from this
finite enumeration.

wp84_carrier_aware_amplitude_recon.py computes COMPLETE numerical amplitudes
by Laurent matrix multiplication for a toy finite section I={2,3,4,5}, R=1,
L=7, primes={2,3,5}, a_phi=1, base phase T=13. Every path and admissible root
is included. It independently reconstructs traces, conjugacy and spectral
support. This is algebra reconnaissance, not the natural-height R6000
arithmetic theorem. The frozen-coefficient toy TV is approximately .00984137
and counting L2 approximately .00154757; neither is compared as a theorem
payment to the real slack. Full amplitudes contain nonzero imaginary parts.
No floating equality is used to group frequencies: integer exponent vectors
are the keys. The ratio certificate is exact support separation.

The previously exact consumer verifier is rerun: rational Gram/support,
c5-zero quadrature and scoped dual flags remain unchanged. No new exact
consumer or complex-dual certificate is fabricated after the stop gate.
Strict >79 remains OPEN. Existing local commits, main, Downloads and
notebooklm_packet are preserved; no push occurs.

wp84_carrier_aware_consumer_verify.py separately saves the preserved exact
consumer certificate, rechecking support, all principal minors, c4=0,
ratio=-620/371 and the exact sharp pair-reference deficit. It certifies
no new amplitude payment.

## 9. Exact correction to the requested frozen ratio

The support/Gram regression exposed a factor-two error in earlier prose and
in the continuation's quoted value. The actual preserved square has
c5=-11501/12500 and c6=137641/250000, so

 c5/c6=-620/371, c6/c5=-371/620,
 -2*abs(c5)/c6=-1240/371.

The last quantity is the negative signed-functional coercivity radius,
not the coefficient ratio. The prior exact candidate JSON already recorded
-620/371; the earlier human reports were wrong. No coefficients are changed
to match the erroneous ratio, no prior commits are rewritten, and every
amplitude computation uses the original correct rational coefficients.
This correction does not affect carrier support separation or Decision D.
