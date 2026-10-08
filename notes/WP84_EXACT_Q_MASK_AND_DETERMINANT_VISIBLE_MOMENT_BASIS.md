# Exact q masks and determinant-visible fifth moments

Parent `990ccbd8f340eea8abccbc0c05dd6fb939e4022b`; branch
`codex/c5-c6-attack-20261006`. Local only; **NO PUSH**. This note supersedes
the earlier conditional 73-coordinate catalogue. It corrects its source-mask
conclusion using the actual source trace.

## Result and evidence boundary

For a fixed source carrier assignment, the exact hidden-prime domain is
\[
Q(T;V)=\{q\le N(T):q\text{ ordinary prime},\ q\notin V\},
\quad N(T)=\lfloor e^{L-\sqrt L}\rfloor,
\]
where (V) is the set of visible carrier primes. The hidden block has net
exponent zero, so q is absent from the carrier, alias test, and root interval.
There are no extra slot intervals in the source trace: each prime variable
has the same natural cutoff (2\le p\le N(T)). Distinct equality-block
primes are pairwise coprime because they are distinct ordinary primes; the
hidden q is excluded exactly when it equals a visible prime.

The exact domain at fixed V is (\mathcal P_{\le N}\setminus V). Two such
domains are identical iff their visible exclusion sets agree. They are not
heuristically clustered. For every exponent j,
\[
\sum_{q\in Q(T;V)}\frac{(\log q)^j}{q}
=S_j(N)-\sum_{p\in V}\frac{(\log p)^j}{p},\qquad
S_j(N)=\sum_{q\le N,\ q\ prime}\frac{(\log q)^j}{q}.
\]
The finite exclusion belongs to the visible-prime coefficient sum. The
universal hidden-prime basis is therefore exactly
\[
S_2(N),S_3(N),\ldots,S_{10}(N),\qquad 73\text{ pair candidates}\to J=9.
\]
The domain-specific corrections are explicit finite sums, not additional
hidden-prime moment coordinates. All (S_j) are real and positive; the
source path coefficients are complex before the prescribed real-part and
conjugate-orientation pairing. Conjugation preserves the q-domain and
conjugates only the coefficient.

For two fixed visible sets V1,V2, the q domains are exactly equal iff
V1 intersect P_{<=N} equals V2 intersect P_{<=N}. If they differ, their
indicator functions are not scalar multiples: both domains contain all
sufficiently large primes below N, forcing any such scalar to be 1, while a
prime in the symmetric difference contradicts equality. Their moment sums
differ by the explicit finite signed sum over V1 symmetric-difference V2;
that difference is O_j(1) for the at-most-three visible primes and is lower
order than S_j(N).

This exact reduction closes the q-mask equivalence question. It does **not**
compute the determinant-visible subset (K\subseteq\{2,\ldots,10\}): that
requires evaluating the source-selected large-section row coefficient
vectors and reducing their exterior polynomial. No rank promotion follows
from reducing J alone.

## Source-linked exact q predicate

The source formulas are `WP84_FULL_WEIGHT_EVALUATION_MAP_KERNEL.md`
(complete map, (q_B\le N), distinct block primes, alias indicator and
root interval), `WP84_NEAR_ALIAS_AND_LONG_TAIL_DISCHARGE.md` (exact sampled
kernel and carrier factorization), and
`WP84_FIFTH_BLOCK_5_7_EXACT_DIFFERENCE.md` (trace/path equivalence and
natural cutoff). For each of the 20 hidden layouts, the executable
`q_mask(layout, block, jet, path, section, q, source_state)` implements:

\[
\mathbf1_{\substack{q\text{ prime},\ 2\le q\le N(T)}}
\mathbf1_{q\notin V}
\mathbf1_{\text{carrier nearest-alias mask}}
\mathbf1_{\rho_I(\ell)>0}
\mathbf1_{\ell\in[-6000,6000]^5,\ \sum\ell=0}.
\]

The last three factors are independent of q. The alias mask uses
\(\lambda=\sum_B e_B\log P_B\), in which the hidden (e_B=0) block
contributes nothing. The root count
\(\rho_I(\ell)=\max(0,d'-\operatorname{range}(v(\ell)))\) depends on the
section and path, not q. Jet order affects the weight, not admissibility.
The q block appears in exactly its two equal slots; it is assigned once, so
there is no factor 2. No additional gcd or Möbius factor occurs in the source
ordinary-prime sum. The external raw-orbit and consumer coefficients remain
outside this mask.

Thus slot position and Fourier path change the q-dependent **weight** but
not its prime domain. Slot permutations preserve the master domain. Carrier
reversal preserves it when V is unchanged; otherwise the two fixed-assignment
domains differ by the exact finite symmetric difference of V. For fixed-size
V, their moment difference is (O_j(1)), while
\(S_j(N)\sim(\log N)^j/j\); this is asymptotic equivalence only, not exact
equality.

## Complete q-polynomial at each jet

For hidden slots (J=(s,t)), put (x=\log q), (c_0=2\pi i), prefixes
\(v_0=0, v_r=\sum_{a\le r}\ell_a\), and
\[
A_J(\ell)=\epsilon_s v_{s-1}+\epsilon_t v_{t-1}.
\]
The q-local factor, including the two base prime coefficients but omitting
the explicit common normalization, is
\[
\frac{x^2}{q}\,f_{\ell_s}^{\epsilon_s}(xu)
 f_{\ell_t}^{\epsilon_t}(xu)e^{c_0A_Jxu}.
\]
Writing (f_\ell^\epsilon(xu)=\sum_{a\ge0}g_{\ell,\epsilon}(a)x^au^a),
\[
g_{0,\epsilon}(0)=1,\quad g_{0,\epsilon}(1)=-1,\quad
g_{0,\epsilon}(a)=0\ (a\ge2),
\]
\[
g_{\ell,\epsilon}(0)=0,\quad
g_{\ell,\epsilon}(a)=-\frac{(\epsilon\ell)^{a-1}c_0^{a-1}}{a!}
\quad(\ell\ne0,\ a\ge1).
\]
The exact coefficient of (x^{2+k}u^k/q) is
\[
\kappa_{J,k}(\ell)=\sum_{a=0}^k\sum_{b=0}^{k-a}
 g_{\ell_s,\epsilon_s}(a)g_{\ell_t,\epsilon_t}(b)
 \frac{(c_0A_J(\ell))^{k-a-b}}{(k-a-b)!}.
\]
At total jet h, every q-power has now been expanded:
\[
P_{J,h}(x)=\sum_{k=0}^{h}
 B_{h-k}(T,d,d',6000;\tau,\ell,\text{source})
 \kappa_{J,k}(\ell)x^{2+k}.
\]
Here (B_r) is not a free coefficient or a q-tail: it is exactly the
coefficient of (u^r) in the remaining three visible-slot factors, their
prefix phases, and
\[
R_{I,\ell,\lambda}(u)=\frac{e^{c_0 k_-\lambda u}}{d'}
\sum_{r=0}^{\rho_I(\ell)-1}e^{c_0r\lambda u},
\]
with the source alias, path, assignment, and real-part factors retained.
The source matrix entry is the finite sum over all injective visible-prime
assignments, all closed paths at (R=6000), and all allowed carrier aliases
of these explicit terms, followed by
\(S_{2+k}(N)-\sum_{p\in V}(\log p)^{2+k}/p\). This is the exact
coefficient-extraction construction used by the moment/determinant builder.

Across all 20 layouts, every universal power (j=2,\ldots,10) occurs in
some required jet. In blocks with maximum excess jet h=6, only (S_2\) through
\(S_8\) occur; B16 reaches (S_{10}\). The 18 visible repeated-prime layouts
have no q-variable and remain outside this correction.

## Correction matrices and first section coefficient

For each block B and moment (S_j), define (E_{B,j}) entrywise by the
finite source sum just specified, with (k=j-2), summing all hidden layouts
in the column. Then exactly
\[
M_B^{\rm full}=M_B^{\rm visible}+\sum_{j=2}^{h_{\max}+2}S_j(N)E_{B,j}.
\]
The finite visible exclusions have already been moved into
\(M_B^{\rm visible}). Each (E_{B,j}) is a source-defined matrix, not a
generic placeholder. The symbolic constructor records its exact row/column
indexing and full finite sum. Its numerical rank, common-row/common-column
dimensions, and determinant-null span require actual source row cells and
the evaluation of these sums; no rank-one or rank-two assertion is made.
The span-rank upper bound is 7 for the size-6/8 blocks and 9 for B16.

More explicitly, for source row i of jet h_i, column c, and hidden layout
with pair slots J=(s,t), the coefficient entry for S_j, k=j-2, is

    (E_(B,j))_(i,c) = -1/(2*a_phi(T)^5*L^5) * Re
      sum over injective visible-prime assignments tau, all closed paths
      |ell_a|<=6000, sum ell_a=0, and allowed carrier aliases m of
        chi_visible(tau,ell,T,I,m)
        * 1_(0<|lambda_tau-mL|<=H/T) * 1_(rho_I(ell)>0)
        * exp(i*T*lambda_tau) * kappa_(J,k)(ell)
        * [u^(h_i-k)]{R_(I,ell,lambda_tau)(u)
          * product_(a notin J)[log(P_tau(a))/sqrt(P_tau(a))
              * f_(ell_a)^(eps_a)(u*log(P_tau(a)))
              * exp(c0*u*eps_a*v_(a-1)*log(P_tau(a)))]}.

The sum over hidden layouts in column c is explicit; a column with no
independent hidden-q layout contributes zero. Distinctness applies to all
visible block primes. The at-most-three q exclusions V were moved into the
visible matrix. The factor -1/(2*a_phi^5*L^5) is the product of the three
visible negative coefficients and the prescribed real-part pairing; the
normalized root sum R already contains 1/d'. This gives each correction
matrix entry as a finite source sum, with no unspecified q-tail.

Let (v_B(S_2)) be the exact common order-five carrier row vector. For
source row i with jet h_i, write its first subleading row coefficient as
\[
r_i(S)=r_i^{\rm visible}+\sum_{j=2}^{h_i+2}S_j e_{i,j},
\]
where every (e_{i,j}) is the corresponding row of (E_{B,j}) after exact
section coefficient extraction. The coefficient at total section deficit
m−1 is exactly the polynomial
\[
C_{m-1,B}(S_2,\ldots,S_{10})=
\sum_{k=1}^m a_k\det(r_1(S),\ldots,r_{k-1}(S),
v_B(S_2),r_{k+1}(S),\ldots,r_m(S)),
\quad a_k=\frac{(c_0\lambda_k)^{h_k}}{(h_k+1)!}.
\]
Its explicit permutation expansion is

    sum_(k=1)^m a_k * sum_(sigma in S_m) sign(sigma)
      (v_visible[B,sigma(k)] + S_2*e_lead[B,sigma(k),2])
      * product_(i!=k)(r_visible[i,sigma(i)]
          + sum_(j=2)^(h_i+2) S_j*e[i,sigma(i),j]).

Here e[i,c,j] is exactly the finite source sum defining (E_(B,j))_(i,c)
above, using k=j-2; j>h_i+2 gives zero. Thus this is a polynomial in the
nine named master moments with coefficients given as explicit finite source
sums, although those coefficients and its collected support are not
evaluated. It corrects the earlier
all-ones shorthand: the leading direction is the exact order-five carrier
vector, generally column-dependent. A term with two copies of this common
vector vanishes, giving the established first possible deficit (m-1).

The exact support (K_B=\operatorname{Supp}(C_{m-1,B})), exact correction
span rank, and whether this coefficient vanishes identically are **not
computed**. Their evaluation needs the source-selected section row map and
actual complete visible-prime/path sums, which are not numerically or
symbolically specialized by the stored finite-core determinant file. The
formal diagnostic determinants use small sections and surrogate logs and
cannot supply these coefficients. No term is deleted as “determinant-null”
without an exact cancellation identity. Likewise, if (C_{m-1,B}) vanishes,
the next coefficient cannot be tested until these source coefficient vectors
are evaluated.

The exact PNT main terms for the master moments are
\[
S_j(N)=\frac{(\log N)^j}{j}+o((\log N)^j),\quad
\log N=L-\sqrt L+o(1),\quad 2\le j\le10.
\]
For fixed normalized prime intervals \,\(N^\alpha<q\le N^\beta\),
partial summation gives \,\((\beta^j-\alpha^j)(\log N)^j/j\); the exact
source mask here is the full interval minus V, not an invented subinterval.
These scalar asymptotics do not determine whether the signed polynomial
\(C_{m-1,B}\) cancels or has a nonzero main term. No determinant margin or
finite (T_0) is available. Hence PNT has not closed the block.

## Visible-only subsystem and block status

| Block | Hidden-q columns | Visible columns | Exact master moments | Correction span rank | Visible-only legal minor | Fifth bound |
|---|---:|---:|---|---|---|---:|
| B6 | 2 | 4 | 7: S2–S8 | unknown, at most 7 | none certified | 1–6 |
| B8a | 6 | 2 | 7: S2–S8 | unknown, at most 7 | none certified | 1–8 |
| B16 | 6 | 10 | 9: S2–S10 | unknown, at most 9 | none certified | 1–16 |
| B8b | 6 | 2 | 7: S2–S8 | unknown, at most 7 | none certified | 1–8 |

The visible columns have been isolated exactly and carry no hidden-q
uncertainty. Their large-section matrices still need source-legal minors;
the existing formal minors are not such certificates. Therefore no visible
rank contribution is promoted. Global fifth rank remains **38–72**.

The only remaining theorem is now a source-determinant-level statement over
the nine exact master moments: evaluate the explicit (E_{B,j}) and
(C_{m-1,B}) on the actual (R=6000), source-selected section rows, determine
their exact moment support, and prove either a nonzero coefficient with a
quantified remainder or continue to the next section deficit. PNT may then
be applied to that final signed polynomial. Separate estimates for all nine
moments are not required unless the reduced polynomial truly depends on all
nine.

## Reproducible artifacts and hostile tests

Run the mask extractor, exact equivalence certifier, coefficient builder,
wedge reducer, visible-only builder, and replay:

```text
python src/wp84_source_q_mask_extractor.py
python src/wp84_mask_equivalence_certificate.py
python src/wp84_exact_determinant_coefficient_builder.py
python src/wp84_wedge_support_reducer.py
python src/wp84_visible_prime_minor_builder.py
python src/wp84_exact_q_mask_replay.py
```

The independent replay checks 20 hidden and 18 visible descriptors, the
exact (73\to9) master-moment reduction, the finite visible-exclusion
identity, and 12 corruptions: merging distinct masks, splitting identical
masks, deleting an exclusion, truncating q, changing multiplicity, changing
carrier net sign, shifting a log power, zeroing moments, changing R, using
d=2, deleting a visible layout, and perturbing (C_{m-1}). The structural
section replay continues to pass through (u^{13}). The wedge-support
reducer deliberately records determinant-visible support as unresolved
rather than claiming a computed (K_B).
