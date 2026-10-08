# Fifth full-pool and large-section lift: F. PRECISE MISSING THEOREM

Parent fc04f3b3440adb2862a47e73e1a02db3f0deb0e3, branch
codex/c5-c6-attack-20261006. No push. The old diagnostic determinants remain
formally nonzero. This audit finds an exact source-level decomposition and an
exact large-section formula, but neither supplies a legal full-block minor.
No new functional is promoted. The certified fifth bounds remain 38--72.

## Four blocks and their individual result

| Block | Formal rank | Full-pool lift | Large-section lift | R=6000 | Certified analytic rank |
|---|---:|---|---|---|---:|
|B6 `{15,20,26,28,31,32}`|6 by diagnostic minor through u^11|not promoted; omitted moment vectors not bounded and slot masks may differ|jet h is exact Laurent polynomial in n, powers -1..h; first surviving determinant coefficient unknown|n>=12001 makes every path nonempty; determinant leading coefficient unknown|1--6|
|B8a `{10,12,16,17,21,22,25,29}`|8 by diagnostic minor through u^11|same precise obstruction; h=0 omitted term has fixed sign|same Laurent Faulhaber formula; leading exterior coefficient unknown|same threshold; determinant coefficient unknown|1--8|
|B16 `{36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69}`|16 by diagnostic minor through u^13|same; up to h=8 needs moments S_2,...,S_10 for each window signature|same Laurent Faulhaber formula through h=8; 16-row exterior coefficient unknown|R is exactly 6000 in the path formulas; no R asymptotic substitute|1--16|
|B8b `{34,37,39,43,53,56,60,63}`|8 by diagnostic minor through u^11|same precise obstruction|same Laurent Faulhaber formula; leading exterior coefficient unknown|same threshold; determinant coefficient unknown|1--8|

“Formal rank” is rank of the specified rational-log, finite-pool, small-section
matrix. It is not asserted as the rank of the full source sum. Formal
nonzero determinant values and row/column identities remain in the prior
certificate; all four exact values are reproduced in
WP84_FIFTH_LEGAL_STENCIL_DETERMINANT_POLYNOMIALS.json.

## Exact source matrix and exact matrix difference

Use the source definitions in WP84_FULL_WEIGHT_EVALUATION_MAP_KERNEL.md and
WP84_NEAR_ALIAS_AND_LONG_TAIL_DISCHARGE.md. Let L=log(T/(2*pi)),
u=1/L,
N=floor(exp(L-sqrt(L))), d=floor(TL/(2*pi)), and let
I(T)=[k_-(T),k_+(T)] be the actual selected interval, of size n=d', with
n/d->1. Set R=6000, c0=2*pi*i, and

    rho_I(v)=max(0,n-(max_j v_j-min_j v_j)),
    v_0=0, v_j=l_1+...+l_j.

For column F_j with signs eps and equality partition pi, visible carrier
vector v, and each assignment P_b of distinct ordinary primes to equality
blocks, define

    lambda=sum_b e_b log P_b,  e_b=sum_(slots in b) eps_slot,
    alpha_b=log P_b/L,
    c(P_b)=-log P_b/(a_phi(T)*L*sqrt(P_b)).

The exact positive-carrier amplitude entry is

    A_j(T;v)= (1/2) sum_{P injective, val(P)=v}
       chi_j(P,T) * product_slots c(P_pi(slot))
       * sum_{l in [-6000,6000]^5, sum l=0}
          (1/n)
          * product_slots f_(l_s)^eps_s(alpha_pi(s))
          * exp(c0/L * sum_s eps_s*v_(s-1)*log P_pi(s))
          * exp(i*T*lambda + c0*k_-(T)*lambda/L)
          * sum_{r=0}^{rho_I(v(l))-1} exp(c0*r*lambda/L).

Here chi_j is the complete source mask: original slot-window intersections,
equality/distinctness, carrier/alias admission and conjugate orientation.
The sum is finite at each T but is not truncated to a chosen core. Empty root
ranges contribute zero. The external alias character and real-part pairing
are shown explicitly. For jet calculations one strips the common
(-1)^5*a_phi(T)^-5*u^5 factor only within degree five; it cannot be replaced
by setting a_phi=1 in the source functional.

The actual row matrix M_B^full has one such coefficient column per F_j,
using actual source cells and their source-selected I(T). For each fixed exact
carrier entry, let K={2,3,5,7,11,13} be the diagnostic pool for an independent
net-zero excess block. Define M_B^core by keeping the visible carrier-prime
assignment fixed and restricting only that independent q to K, with the same
T, R, I, actual prime logs, masks and normalization. If the excess pair is
visible, there is no independent q cutoff coordinate and E_pool is zero for
that fixed-carrier entry. Partitioning the q assignments gives the exact
identity, entry by entry and at every jet order,

    M_B^full(T)-M_B^formal
      = [M_B^full(T,N,6000,I,log P,a_phi,chi)
          - M_B^core(T,N,6000,I,log P,a_phi,chi)]       E_pool
        +[M_B^core(T,N,6000,I,log P,a_phi,chi)
          - M_B^core(T,N,R0,I,log P,a_phi,chi)]         E_band
        +[M_B^core(T,N,R0,I,log P,a_phi,chi)
          - M_B^core(T,N,R0,I0,log P,a_phi,chi)]        E_section
        +[M_B^core(T,N,R0,I0,log P,a_phi,chi)
          - M_B^core(T,N,R0,I0,z,a_phi,chi)]            E_logs
        +[M_B^core(T,N,R0,I0,z,a_phi,chi)
          - M_B^core(T,N,R0,I0,z,1,chi)]                E_norm
        +[M_B^core(T,N,R0,I0,z,1,chi)
          - M_B^formal(z,n0,R0,I0,chi0)]                E_mask/model.

R0,n0,z,I0,chi0 are exactly the row-labelled formal specialization from the
prior determinant certificate (values differ by row). This telescoping
identity is a decomposition for a fixed carrier assignment; passing from
these entries to a determinant still requires the source-legal carrier
selection and row alignment. E_pool is the complete omitted q mass for
net-zero layouts (zero for visible-excess layouts); E_band, E_section,
E_logs, E_norm and E_mask/model are distinct exact changes. The formal and
source matrices are compared only after their rows
are aligned by the certificate's jet-order labels. The symbolic source
constructor and its assumptions are in
src/wp84_fifth_full_pool_amplitude.py and
WP84_FIFTH_FULL_POOL_LIFT_CERTIFICATE.json.

## Exact core plus omitted-prime formula at every used jet

Every one of the 38 layout descriptors has

    sum_b (nu_b-|e_b|)/2 = 1.

This counts one excess pair, but it does **not** imply that the pair is always
an independent canceled prime. Let b* be the unique block with
nu_b*>|e_b*|. Its multiplicity is two. If e_b*=0, b* is a net-zero block
and carries an independent prime q absent from the carrier; this creates an
omitted-prime tail. If |e_b*|=1, its two occurrences are a repeated copy of
the carrier-visible prime, and there is no independent q sum. The exact
classification is:

| Block | Independent net-zero q layouts | Visible repeated-prime layouts |
|---|---|---|
| B6 | 31, 32 | 15, 20, 26, 28 |
| B8a | 16, 17, 21, 22, 25, 29 | 10, 12 |
| B16 | 47, 49, 50, 62, 65, 69 | 36, 38, 42, 46, 48, 54, 59, 61, 64, 68 |
| B8b | 37, 39, 43, 56, 60, 63 | 34, 53 |

Only in the net-zero case, for an assignment tau of the visible primes and an
admissible q, the five slot coefficients contain

    (log q)^2/q * V_tau,
    V_tau=product_visible (log P_b)^nu_b / P_b^(nu_b/2),

apart from the common a_phi^-5*u^5 and the section/path factors. q must be
distinct from the visible primes. It ranges over every source-admitted prime
up to N. The exact core/remainder split for jet h in a net-zero layout is

    J_(j,h)^full = J_(j,h)^core + E_(j,h),
    E_(j,h)=sum_window_signature eta sum_(r=2)^(2+h)
                  C_(j,h,r,eta)(visible primes;6000,I,chi) * S_(r,eta),
    S_(r,eta)=sum_(q prime<=N, q not visible, q not in K,
                   source window signature eta) (log q)^r/q.

For clarity, the coefficient is specified by the following exact generating
expression. Let J be the two slot positions in the balanced equality block,
let tau assign the visible carrier primes, let P_tau denote those primes,
and set x=log q. Write

    R_(ell)(u)=exp(c0*i_min*lambda*u)/n
                 *sum_(r=0)^(n-span(ell)-1) exp(c0*r*lambda*u),
    Phi_(tau,q,ell)(u)=exp(c0*u*sum_s eps_s*prefix_(s-1)*log p_s),

where p_s=q on J and p_s=P_(tau(block(s)) otherwise. Define

    G_(j,eta)(x,u)= -1/2 * sum_tau,ell
       chi_(j,eta)(tau,q,ell,T) * R_(ell)(u) * Phi_(tau,q,ell)(u)
       * product_(s notin J) [log(P_tau(block(s)))/sqrt(P_tau(block(s)))
                              * f_(ell_s)^eps_s(log(P_tau(block(s)))*u)]
       * product_(s in J) [x*f_(ell_s)^eps_s(x*u)].

Then C_(j,h,r,eta)=[u^h*x^r]G_(j,eta)(x,u), with source masks fixed
on that cell; the q^-1 is outside in S_(r,eta). This coefficient-extraction
formula explicitly includes every path and root, visible assignment,
balanced-slot location and sign. The identity follows by substituting
log q=x in the two balanced-slot factors and extracting [u^h*x^r]; all
other slot logs, assignment permutations and root/path factors go into C. At order h the two
base slot coefficients give x^2; at most h more powers can come from the
Taylor factors, so 2<=r<=2+h. For the largest certificate depth u^13,
h<=8 and the exact moment list is S_2 through S_10. The coefficient formula
is finite and exact, with R and the source interval fixed; it is not an
absolute-value estimate.

For a visible repeated-prime layout, the omitted independent-q contribution
is exactly zero: the excess block prime is forced by the carrier, and the
full/core comparison must instead track whether that visible prime is in the
chosen core. It is incorrect to attach an independent S_r tail to those
descriptors. If the balanced-slot window intersection is the same for every
net-zero column, the h=0 omitted correction is exactly a scalar S_2 times the
visible-assignment column vector: rank one at that jet row. If different slot pairs have

different original window signatures, keep their S_(2,eta) separate; no
common scalar or rank-one assertion is made. The ledger preserves the
intersected masks but does not provide a proof that all these intersections
coincide. Across all five slots there are at most ten pair signatures.

At h=0 only zero displacement survives, every E_p(0)=Identity, and the
normalized trace is exactly one. Thus every omitted q term in a net-zero
layout has the same negative sign before its nonnegative source-window indicator.
There is no cancellation, Möbius factor, or Gram subtraction at this jet.
Under the all-primes-to-N mask,

    S_2(N;A,K)=sum_(q<=N, q prime, q notin A union K) (log q)^2/q
              ~ (log N)^2/2 ~ L^2/2.

More generally a fixed normalized prime window
N^alpha<=q<=N^beta, 0<alpha<beta, contributes
((beta^2-alpha^2)/2+o(1))*L^2. These follow by partial summation from the
PNT. Hence the omitted h=0 term is not asymptotically small relative to a
fixed finite core; it grows like L^2 for any such nonshrinking window.
More generally, for r>=1, PNT partial summation gives S_r(N)~(log N)^r/r; on a fixed normalized window [N^alpha,N^beta], the leading constant is (beta^r-alpha^r)/r. Thus the h-th source contribution u^(5+h)*S_(2+h) is of order L^-3, while the corresponding fixed-core contribution is O(L^-(5+h)); the full-pool correction is larger by L^2 at its top log degree, not a negligible core tail. The q sum is not absolutely summable to infinity with this weight. For
h>=1, coefficients can have signs; this audit proves no exact cancellation,
symmetry, or small bound for their moment combinations. There is no
certified singular-value or determinant-lemma rank-stability estimate.

Thus for blocks containing net-zero descriptors, the finite-core determinant
is not automatically a small perturbation problem. Their exact h=0 correction
is large; higher corrections need controlled complete prime moments, and the
determinant uses column-specific coefficients. The visible repeated-prime
descriptors have a different obstruction: their full carrier primes need
source-legal treatment, but no independent balanced-prime tail. Absolute
bounds alone would not reveal the h=0 sign or common moment structure, so none
are substituted for the exact decomposition.

## Exact large-section dependence and the R=6000 check

For any closed five-step displacement path, every difference of two prefix
sums is a sum of k consecutive increments, 1<=k<=4 (the k=5 sum is zero).
Closure bounds its absolute value by min(k,5-k)R<=2R. Therefore

    range(v_0,...,v_5)<=2R=12000.

For n>12000 every path has roots, but higher jets retain the root-phase
sum. Strip the common translation factor exp(c0*k_-*lambda*u). If the
prefix minimum is m and the path span is s, the exact root factor left is

    exp(-c0*m*lambda*u)/n * sum_(r=0)^(n-s-1) exp(c0*r*lambda*u).

Therefore its order-h coefficient is exactly

    c0^h*lambda^h/n * sum_(j=0)^h
       (-m)^(h-j)/( (h-j)! j! ) * S_j(n-s),
    S_j(M)=sum_(r=0)^(M-1) r^j.

The S_j are exact Faulhaber polynomials, generated without approximation by
S_0(M)=M and

    S_j(M)=(M^(j+1)-sum_(t=0)^(j-1) binom(j+1,t)*S_t(M))/(j+1).

Thus each fixed path's h-jet is a Laurent polynomial in n with powers -1
through h. After multiplying by n it is a polynomial of degree at most h+1;
it is not generally affine in 1/n. Its leading term is
(c0*lambda)^h*n^h/(h+1)!; lower powers depend on the path minimum, span
and filter placement. The leading root term is common across columns for a
fixed carrier and can be removed by row elimination, but this fact alone
does not show the remaining large-n determinant is nonzero. The h=0
coefficient reduces to 1-s/n, as expected.

The determinant is an exact Laurent polynomial in the row sizes n_i, with coefficients
that themselves depend on the complete N(T)-prime pool and source masks.
For rows h_i and sections n_i it is obtained by inserting the exact
Faulhaber-polynomial entries into the determinant; the top n_i powers have
common carrier-root directions and cancel in exterior products. The formal
small-section determinant gives no value for the first surviving exterior
coefficient. A leading-coefficient proof would have to compute that
coefficient after the full prime sums, for every selector branch.

At R=6000 the exact root formula applies whenever n>=12001. Since d'/d->1,
if d>=24002 and d'/d>=1/2, then n>=12001. Thus d0=24002 is a valid
conditional threshold in d once the ratio bound holds. The source gives
only the limit d'/d->1, not an explicit T at which the 1/2 bound starts.
More importantly, the first surviving large-n determinant coefficient for
each full-pool block has not been shown nonzero. R=6000 is included exactly;
no large-R limit is used. There is no R0 requiring extrapolation.

The earlier root-count combination H(n)=max(0,n-1)-2max(0,n-2)+max(0,n-3)
still shows that zero-phase counts alone can vanish for every n>=3 after
being nonzero at n=2. For the full filtered jets the exact Faulhaber root
moments above replace that count, and no relation among target columns is
inferred from H. This is a warning against transferring a diagnostic section
minor without computing its actual root moments.

## Rank stability, asymptotics, and block results

For every block:

* Formal rank: respectively 6, 8, 16, 8.
* Full-sum lift: not certified. The h=0 omitted moment has fixed sign and
grows as L^2 on nonshrinking admissible windows; it is not small. At higher
orders the exact S_(r,eta) combinations are retained but uncontrolled.
* Large-section lift: coefficient expansion is an exact Laurent polynomial
in n, with powers -1..h for jet h. Top carrier-root directions cancel in the determinant. The first
surviving full-pool exterior coefficient is unknown, so no nonzero threshold
can be certified.
* R=6000: exact root cutoff n>=12001 is available, but does not settle the
first surviving determinant coefficient.
* Certified rank: inherited rank one only. No rank(V5) increase this run.

A reusable full-pool/large-section theorem must show that for at least one
source-legal collection of rows the exact determinant

    D_B=det( J_(i,j)(N_i,6000,I_i,chi_i) )

 is nonzero. Here each entry is expanded as a Laurent polynomial
J_(i,j)=sum_(r=-1)^(h_i) C_(i,j,r)(N_i,chi_i)*n_i^r, with C containing
the complete S_(s,eta) prime moments and exact path factors. Substitution gives

    D_B=sum_permutation sigma sign(sigma)
             product_i sum_(r=-1)^(h_i) C_(i,sigma(i),r)*n_i^r.

A sufficient asymptotic route would identify its first nonzero joint
large-section/full-pool coefficient and prove a uniform error bound over
source selector branches and masks. The formal core determinant is not that
coefficient. No lower bound for this first surviving exterior coefficient
or uniform error is available. This exact determinant nonvanishing statement
is the remaining theorem, separately for each block.

Cross-block carrier uniqueness stays as before but cannot add dimensions
inside these blocks. Fifth rank remains 38--72; the 453-family remains
38--453. No full rank(V5)=72 or V5 direct-sum conclusion follows. The
mixed-degree V5 intersect V6 check is conditional on all four closing and
is not reached. Strict >79 remains OPEN.

## Verifier and deliberate failures

src/wp84_fifth_full_pool_amplitude.py stores the exact source matrix schema,
block descriptors, core set and moment decomposition. It distinguishes the 20
net-zero layouts with an independent omitted-prime variable from the 18
visible repeated-prime layouts. The omitted sum is represented by explicit
source-window moment classes, not silently truncated.
src/wp84_fifth_full_pool_replay.py checks all 38 layouts have exactly one
excess pair and verifies whether its net exponent is zero, checks the exact
R=6000 span and n threshold using rational arithmetic, and records the
finite-core/full-pool split. It rejects:
truncating the pool, replacing n by 2, changing R, changing d'/d, removing a
path/section term, altering normalization, fake rational logs, or violating
the full source cutoff. These are obstruction tests; no matrix is promoted.
The replay also verifies the small-section root counterexample exactly.

Outputs: WP84_FIFTH_FULL_POOL_LIFT_CERTIFICATE.json and
WP84_FIFTH_FULL_POOL_REPLAY.json. No float rank, approximate singular value,
smallness assumption, or consumer change is used.
