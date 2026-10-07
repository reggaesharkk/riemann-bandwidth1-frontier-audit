# WP84 — collapsed semiprime operator norm and the variable-R stop condition

Date: 2026-10-07. Parent: `f166ccfaec20e1b43ca69a2043dad34ed1a68f0a`.
Branch: `codex/c5-c6-attack-20261006`. No push.

**Outcome: the proposed uniform operator-norm/L2-mass quartic rescue is
structurally blocked.** On the actual ordinary-semiprime coefficient Hilbert
space the error operator depends on T as well as R. For EVERY fixed R its
positive spectral norm is unbounded as T grows. Thus no finite constant
lambda_plus(R), uniform in T, can furnish the requested norm-times-mass
upper bound. Increasing a fixed R does not remove this obstruction.

This does NOT prove that the actual arithmetic coefficient vector has large
positive leakage, and does NOT falsify every possible quartic estimate. A
norm supremum may select coefficient directions unlike the actual prime
vector. It does rule out the requested uniform full-Hilbert-space operator
norm strategy. Under the user's stop condition this strategy is abandoned;
the primary next theorem route is the bounded rank-six resolvent route.
No new pointwise-sign search is performed.

## 1. Exact Hilbert space, collapse and coefficient mass

Let P_N be the ordinary primes p<=N, with

    a_p = -log p/(a_phi L sqrt(p)),
    L=log(T/(2pi)), N=exp(L-sqrt(L)+o(1)), a_phi->1.

The index set S_N consists of integers m=pq with p,q in P_N, unordered after
product collapse. Unique factorization gives ONE unordered factor pair for
each m, including m=p^2. The Hilbert space is ell2(S_N) with COUNTING measure.
This is not an artificial collection of different factorizations at the
same product scale. Define

    z_T(pq) = 2 a_p a_q, p<q;
    z_T(p^2) = a_p^2;
    c_T(m) = z_T(m) exp(-i tau_- log m), tau_-=T+(2pi/L)k_-.

The carrier and principal-section phase are in c_T; they do not change its
norm. R-band interval factors are retained in the kernel, not silently put
into this vector. The multiplicity 2 accounts exactly for the two internal
orders of each distinct-prime pair.

Write M1=sum_p |a_p|^2 and M2=sum_p |a_p|^4. EXACTLY,

    ||c_T||2^2 = 2 M1^2 - M2.

The prime-square theorem and log N/L->1 give

    M1 = (log N/L)^2/(2 a_phi^2) + O(a_phi^(-2) L^(-2)),
    M2 = O(a_phi^(-4) L^(-4)),
    ||c_T||2^2 = (log N/L)^4/(2 a_phi^4) + O(a_phi^(-4) L^(-2)) -> 1/2.

Thus the SHARP asymptotic coefficient square-mass constant is **1/2**.
For every epsilon>0, eventually the mass is at most 1/2+epsilon. No arbitrary
normalization constant or missing factor four is consumed.

For a bounded ordered-pair feature w(s,t), product collapse uses
a_p a_q[w(s_p,s_q)+w(s_q,s_p)]. Its square-mass limit is

    (1/2) integral_[0,1]^2 s t |w(s,t)+w(t,s)|^2 ds dt <=1/2

when |w|<=1. This is the concrete feature-mass interface. For example the
DIAGONAL beta feature w=(1-s)(1-t) has constant 1/72; that is a different
vector and cannot replace 1/2 in the complete four-word form. Taper factors
must stay in the displayed feature and coefficient normalization.

## 2. Exact connected quadratic operator

For m=pq, n=rs, use the actual row-cumulant kernel of the parent note. Average
over the internal factor orders and sum the six positive-position choices:

    H_R,T(m,n) = (1/4) sum_(two orders of p,q; two orders of r,s)
                         sum_(six interleavings sigma)
                         Omega4,R(v_sigma) kappa_d'(v_sigma),
    v_sigma = interleave(log p/L, log q/L, -log r/L, -log s/L).

For a square factor pair the duplicated internal orders coincide; the same
averaging formula remains valid with multiplicity 1 in z_T. The exact
balanced ordinary-prime connected row cumulant is

    Connected4,balanced,ordinary = c_T* H_R,T c_T.

The full ordinary-prime signed trace also has unbalanced sign populations;
proper-power coefficients are separate. Blocking a uniform norm bound on
this balanced ordinary subspace already blocks the proposed full operator
strategy. No claim that those other populations are o(1) is needed for the
obstruction below.

The kernel is Hermitian by full ordering/trace-adjoint symmetry. One must not
use C24=4 C6 for individually filtered words: averaging both internal orders
is required. After integration against the ordered-pair coefficient sum, this
averaging is exact and adds no orientation charge.

Its dependence on T is essential:

    kappa_d'(v) = sum_(26 anchored partitions) sign(pi)
                              product_(B in pi) D_d'(sum_B v),
    D_m(u)=m^(-1) sum_(k=0)^(m-1) exp(2pi i k u).

Fourier banding does not truncate this sampled product-frequency frame to a
space of dimension depending only on R.

## 3. Exact negative-anchor decomposition

For product states with 1<=s_m=log m/L<=2, write
r_m=min(log p/L,log q/L), c_m=s_m-1. The existing global Brownian anchor is

    G(m,n)=2 min(c_m,c_n)
                [min(r_m,r_n)-max(c_m,c_n)]_+.

It is PSD by its two indicator Gram integrals. The product-frequency frame

    K_T(m,n)=D_d'(s_m-s_n)

is also PSD. Thus -G o K_T is negative semidefinite. Define EXACTLY

    E_R,T = H_R,T + G o K_T,
    H_R,T = -G o K_T + E_R,T.

Below we restrict to a supercritical ordinary-prime block where all these
formulas are defined. Extending G by zero outside that block is still PSD.
Adding G o K_T cannot reduce the top eigenvalue:

    lambda_max(E_R,T) >= lambda_max(H_R,T).

This is a valid decomposition, not an assertion that E_R,T is small or
identical to the old sharp detuning residual. The pointwise audit already
ruled out that identification; the present obstruction is on the ACTUAL
collapsed ordinary-prime space.

## 4. Finite Fourier feature form, including the one-tail term

For every closed Fourier lag path |r_j|<=R, sum r_j=0, write

    Omega4,R(v)=sum_r product_j g_(r,j)(v_j),
    g_(r,j)(v)=a_rj(v) exp(2pi i h_j v), h_j=sum_(l>j) r_l,
    a_r(v)=integral_Jv exp(-2pi i r x) dx.

Each |g|<=1. On either signed interval branch,

    |g'|<=1+6pi R.

For each sign orientation the four factors separate into a function of the
positive product state and a function of the negative product state.
Consequently the FULL-BLOCK part of kappa, D_d'(sum v), gives finite sums

    D_A K_T D_B

of diagonal feature multipliers and the product-frequency Gram frame. The
cross-pair block terms give similarly multiplied prime-frame tensor products.
This is the relevant exact finite-feature structure. It is not a fixed-size
Toeplitz matrix in integer semiprime index.

The surviving one-tail contribution has the SAME operator form. With exactly
one |r_j|>R and the other three <=R, closure forces that tail index to be at
most 3R, so this one-tail component is itself a finite feature sum. The mode
(401,-399,-2,0) from the parent certificate is one instance. Its diagonal
multipliers depend on the TWO prime factors, not just the product ratio.

It is therefore not generally a scalar Toeplitz convolution on semiprimes.
The product frame is stationary in log m-log n; on the actual nonuniform
semiprime set this is a generalized Fourier Gram matrix. No scalar Fourier
symbol of only R controls the full operator. Conjugate modes and orientations
make the assembled operator Hermitian, not skew. Mean-zero in the physical
Fourier coordinate does not remove its positive quadratic action.

On exact ordinary distinct-prime product equality, unique factorization
identifies the two unordered pairs. The leading empirical connected
cumulant there tends to zero; it is not identically zero at finite d'. Prime
squares have a repeated-base correction with negligible coefficient mass.
These diagonal facts do not remove the dense NEAR-product off-diagonal
frame, which causes the norm obstruction. No arithmetic phase averaging
improvement for the actual vector is established here.

## 5. Spectral reconnaissance before the uniform-norm decision

There is no T-independent finite matrix representing E_R,T. Rather than
report invented finite values for lambda_plus(R), the verifier diagonalizes
a clearly labeled AUXILIARY product-frequency feature frame and evaluates
its common-factor coefficient with 55-digit arithmetic.

At theta=3/4, let A=V_theta,R and f=F_R 1_[0,1/4]. The six exterior words
have the exact common-factor coefficient

    k_R(theta) = 2 integral f^4
                  + 4 integral f(x)^2 f(x-1/4)^2.

The auxiliary frame has 16 distinct closely spaced product-frequency
features and 64 Fourier rows, with top eigenvalue
15.998881789510189381382046552650564. It is NOT a prime discretization,
not a replacement for the true arithmetic operator, and not a Delta_R
certificate. Its purpose is to test whether the R-filter removes the
positive product-frame channel.

| R | k_R(3/4), numerical | Auxiliary top eigenvalue k_R*frame |
| --- | --- | --- |
| 50 | 0.49573080204583971 | 7.93113850135046548 |
| 100 | 0.49803749859606193 | 7.96804306678174175 |
| 200 | 0.49900500063446924 | 7.98352201752533045 |
| 400 | 0.49949850548544344 | 7.99141754329861646 |
| 800 | 0.49974811452637042 | 7.99541100883800018 |
| 1600 | 0.49987373781023287 | 7.99742084090652562 |
| 3200 | 0.49993678031363744 | 7.99842945046621020 |

There is no decay: k_R tends to 1/2. The arithmetic conclusion comes from
the actual-prime proof below, not this auxiliary table. The uniform-in-T
lambda_plus(R) table, for every listed R, is **+infinity**.

## 6. The actual-prime operator obstruction: theorem and proof

**Theorem.** Fix ANY nonnegative integer R. On the canonical semiprime
ell2 counting space above,

    lim_(T->infinity) max(0,lambda_max(E_R,T)) = +infinity.

The same assertion holds for H_R,T. The proof uses ordinary primes with
distinct bases, not different factorizations of one product and not the
proper-power pointwise witnesses from the parent audit.

Choose theta=3/4, P=exp(theta L), and take the primes in [P,2P]. They lie
below N for all sufficiently large L because theta L+log 2<L-sqrt(L).
Let Kp be their count, and restrict to distinct-prime semiprimes pq with
p<q in this block. Their number is

    M_T=binom(Kp,2) ~ P^2/[2 (log P)^2].

Every such state has its two normalized prime logarithms in
[theta,theta+log 2/L]. The products are DISTINCT by unique factorization.
For the actual selected section, m=d'~exp(L)L. The product frame has
diagonal one and rank at most m, hence

    lambda_max(K_T)>=M_T/m,
    M_T/m ~ (8/9) exp(L/2)/L^3 -> infinity.

This elementary trace/rank bound alone does not prove the same for the
connected matrix: its covariance subtractions must be controlled.

### 6a. The positive full-block channel survives every fixed R

At the common factor theta,

    k_R(theta)=4 tau(A^2 (A*)^2)+2 tau((A A*)^2)
              =4 integral f(x)^2 f(x+theta)^2+2 integral f^4.

Both terms are nonnegative. Since integral f=1-theta, Jensen gives the
R-INDEPENDENT rigorous lower bound

    k_R(3/4)>=2(1-3/4)^4=1/128.

Let n_R=6(2R+1)^3, an upper bound on the number of separated exterior
features, including the six sign positions. Internal-order averaging does
not increase a norm bound. The feature derivative estimate in §4 yields

    ||H_full - k_R K_T||op <= eta_R(L) ||K_T||op,
    eta_R(L)<=4 n_R(1+6pi R) log 2/L.

This is an OPERATOR estimate: expand each diagonal feature around its
common-factor value in D_A K_T D_B and use the sup norm of each diagonal
multiplier. It is not an entrywise estimate multiplied by a prime count.
For example, pi<22/7 and log 2<1 show eta_R<=1/256 once

    L >= 1024 n_R [1+(132/7)R].

The threshold may be enormous; R is fixed first. Its size does not alter
the asymptotic theorem.

### 6b. Cross-pair covariance subtractions have bounded operator norm

On the PRIME block define

    B_T(p,r)=D_m((log p-log r)/L).

This is the normalized sampled linear-prime frame. Its frequency separation
is at least 1/(2P+1). The elementary disjoint-cell sampling inequality and
Montgomery--Vaughan linear-polynomial mean square give

    ||B_T||op
      <=2[1+h^2 log^2(2P)] [1+2pi(2P+1)/(m h)] <=164

eventually, since h=2pi/L, mh~T, P/T->0 and log(2P)<=L.
The first inequality applies to arbitrary coefficients on this prime block,
not just the actual Lambda weights. It is the same linear sampling proof
already used in the selected-section reprojection note.

The two opposite-sign pair partitions in kappa give B_T tensor B_T,
one with the factor interchange, compressed to the unordered-pair space
and multiplied by the separated diagonal Fourier features. Therefore

    ||H_cross_pair||op <=2 n_R 164^2=53792 n_R.

Compression/internal-order averaging cannot increase this conservative bound.
This proves the needed operator control rather than summing small entries
over all semiprimes.

### 6c. All remaining partition terms are small in operator norm

For L>=16 log 2, individual signed factors, same-sign pairs, and the
singleton-complement triples on this block stay at torus distance at least
1/8 from integers. Thus each such D_m is at most 4/m in modulus.

The same-sign 2+2 partition has two such factors. The four singleton/triple
partitions also have two. Each of the twelve 1+1+2 anchored terms has at
least two, and each of the six four-singleton terms has four. Together
with |Omega|<=n_R this gives the conservative Schur/row-sum bound

    ||H_remaining||op <=1808 n_R M_T/m^2 = o(1).

Here 1808=16+(4+12)*16+6*256. This fixed finite combinatorial bound is used
only to prove a norm obstruction, NOT to pay a record error or to claim
sharp truncation cancellation. Since P<T,
M_T/m^2 decays exponentially in L. No unspecified large coefficient mass
is hiding in the bound.

### 6d. Assemble the positive spectral lower bound

Weyl's inequality and §§6a–6c yield eventually

    lambda_max(H_R,T)
      >= M_T/(256m) - 53792 n_R - 1808 n_R M_T/m^2
      -> +infinity.

Adding the PSD Brownian Schur anchor proves the same for E_R,T. This is a
rigorous actual-ordinary-prime operator lower bound for each fixed R.

The small positive square mass of the ACTUAL coefficients on this block
does not contradict it: an operator eigenvector may be concentrated in
another direction. The theorem rules out a uniform estimate valid for
ALL vectors in this Hilbert space, not a signed estimate specialized to
the actual Lambda/carrier vector.

## 7. Variable-R consumer tolerance: closed exact/interval algebra

For arbitrary positive integer R, retain the full finite-lag pair formula

    Pair_R=1/12 + 2 H2(R)/(3pi^2)
                   + [E4(R)/8+2 H2(R)^2-3 H4(R)/4]/pi^4,
    E4(R)=4 H2(R)^2+2 sum_(r=1)^(2R) s_r^2,

with the exact harmonic convolution s_r from WP84_R400_EXACT_PAIR_LAYER.
Define, for the same frozen displayed conservative ledger inputs,

    W_R=(2000/593)[0.163249981456072-1/2000-213/3000-2.1728342265/R],
    Tol_R=W_R-Pair_R.

Outward interval computations give the following; decimals in this table
are rounded for display, while the verifier prints complete enclosures.

| R | Pair_R | W_R | Tol_R |
| --- | --- | --- | --- |
| 50 | 0.26393937014950819 | 0.16287789857022597 | -0.10106147157928222 |
| 100 | 0.26530715096962250 | 0.23616067180800000 | -0.02914647916162250 |
| 200 | 0.26598850372830560 | 0.27280205842688702 | 0.00681355469858142 |
| 400 | 0.26632812189892278 | 0.29112275173633052 | 0.02479462983740774 |
| 800 | 0.26649756251083758 | 0.30028309839105228 | 0.03378553588021470 |
| 1600 | 0.26658216508764879 | 0.30486327171841315 | 0.03828110663076436 |
| 3200 | 0.26662443060144744 | 0.30715335838209359 | 0.04052892778064615 |

The exact R400 pair value gives Tol400>0.0247937, slightly more than the
old rounded Pair400 ceiling. As R->infinity, Pair_R->4/15 and

    Tol_infinity = 4756243046027/111187500000000
                 =0.04277677837910736...

The limit Pair_R->4/15 follows from H2->pi^2/6, H4->pi^4/90 and the
L4 convergence of the bounded sawtooth Fourier sums, giving E4->pi^4/5.
It is not a higher-prime arithmetic transfer.

The tolerance is finite. The uniform full-space spectral error from §6
is unbounded at every fixed R, so multiplying it by the sharp coefficient
mass 1/2 never supplies a usable theorem budget. No finite R can be certified
by this proposed uniform-norm method.

## 8. Consumer insertion, best R and stop decision

IF some different argument proved the actual signed bound
Connected4_actual<=Delta_R+o(1), including other sign/power sectors or
separately paying them, the same consumer algebra would give

    w_R<=Pair_R+Delta_R+o(1),
    defect<=1/2000+213/3000+(593/2000)(Pair_R+Delta_R)+Cmatch/R+o(1),
    margin>=Erec-defect,
    conditional simple coefficient>=1-2 defect-o(1).

No such Delta_R is obtained here. There is therefore NO best certified R,
NO corrected numerical consumer margin and NO repaired percentage.
The auxiliary feature eigenvalues cannot be inserted as Delta_R; conversely
the divergent full operator norm is not a lower bound on the actual-vector
quadratic value.

Under the requested stop condition, abandon the **uniform operator-norm
fixed-band quartic rescue**. Do not continue pointwise sign searches or
optimize R around this obstruction. The primary next target should be the
bounded rank-six resolvent route, where the test function and evolving state
remain bounded and a large raw semiprime-frame norm need not be consumed.
The quartic scalar inequality itself and the special actual weighted form
remain mathematically undecided; this audit does not assert their falsity.

Remaining source/zero-side obligations are preserved: corrected Weil/prime
normalization, covariance substitution, any actual endpoint-feature second
mass, full-to-band resolvent tail, zero-side blocks and tail-Weyl transfer,
and selected-section lower moments. None is promoted by a spectral norm
obstruction or by the variable-R algebra.

## 9. Verification and preserved history

Run:

    python src/wp84_filtered_connected_operator_norm.py --spectral

The standard Fraction checks certify the product-collapse multiplicity,
sharp mass constants, exact rational Tol_infinity, a Machin-enclosed R400
pair/tolerance, and the common-factor lower constant 1/128. mpmath interval
arithmetic gives all finite-R pair budgets. The 55-digit auxiliary spectral
diagnostics are explicitly ordinary numerical calculations, not interval
certificates of an arithmetic spectrum.

The actual-prime divergence theorem is proved in §6; the script does not
pretend to enumerate its enormous asymptotic prime block. Fail-closed checks
reject Python optimized mode. Expected final status:

    RESULT: VARIABLE_R_BUDGET_PASS; UNIFORM_IN_T_OPERATOR_NORM_ROUTE_BLOCKED;
            ACTUAL_WEIGHTED_FORM_UNDECIDED

All earlier local commits, including f166ccf and 3303e03, remain unchanged.
Only this note and the associated verifier are added. No push, merge, rebase,
or modification of main or Downloads is performed.
