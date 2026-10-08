# WP84 hidden-prime moments and large-section determinant

Parent `b299cbdb12a525739ac17fc489eb7992e8f316ff`; branch
`codex/c5-c6-attack-20261006`. Local only; no push. **Decision F: precise
hidden-prime moment theorem required.** This run stays within the two stated
open objects. It does not change a fifth-rank claim.

## Blockwise result

| Block | Formal size | Independent hidden-q layouts | Visible repeated-prime layouts | Candidate moment coordinates* | Correction rank | First nonzero legal section coefficient | (R=6000) | Certified rank |
|---|---:|---:|---:|---:|---|---|---|---:|
| B6 `{15,20,26,28,31,32}` | 6 | 2: `{31,32}` | 4: `{15,20,26,28}` | 14 | unknown | unknown; first possible section deficit 5 | root/jet identity passes; determinant open | 1 |
| B8a `{10,12,16,17,21,22,25,29}` | 8 | 6: `{16,17,21,22,25,29}` | 2: `{10,12}` | 28 | unknown | unknown; first possible section deficit 7 | root/jet identity passes; determinant open | 1 |
| B16 `{36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69}` | 16 | 6: `{47,49,50,62,65,69}` | 10: `{36,38,42,46,48,54,59,61,64,68}` | 45 | unknown | unknown; first possible section deficit 15 | root/jet identity passes through (u^{13}); determinant open | 1 |
| B8b `{34,37,39,43,53,56,60,63}` | 8 | 6: `{37,39,43,56,60,63}` | 2: `{34,53}` | 35 | unknown | unknown; first possible section deficit 7 | root/jet identity passes; determinant open | 1 |

*These are exact counts only for the **slot-pair-indexed candidate basis**, before
any source-mask splitting. There are 73 such pair/power coordinates across the
four blocks. They are not claimed to be the exact minimal source moment count:
the checked-in source records name the original mask `chi` but do not provide
an executable q-window predicate or equality certificate between masks.
Consequently the actual moment basis can refine this candidate basis, and its
minimal dimension is not determined here. No unproved mask merging is used.

The four prior formal determinant values and their small-section rational-log
specializations are not large-section or full-pool margins. They cannot be
used to promote a block.

## Exact q-local jet expansion

Fix a hidden layout, its net-zero excess block, and its two slot positions
(J=(s,t)). Write (x=log q), (c_0=2\pi i),
(v_0=0, v_r=\ell_1+\cdots+\ell_r), and

\[
A_J(\ell)=\epsilon_s v_{s-1}+\epsilon_t v_{t-1}.
\]

Since the block has net exponent zero, q cancels from the carrier
\(\lambda=\sum_B e_B\log P_B\), from the sampled root geometric sum, and
from the alias test on that carrier. Its only q-dependent analytic factors
are the two slot filters and their prefix phase, along with the two base
prime coefficients. Their exact local factor is

\[
\frac{x^2}{q}\, f_{\ell_s}^{\epsilon_s}(xu)
 f_{\ell_t}^{\epsilon_t}(xu)\exp(c_0 A_J(\ell)xu).
\]

Define (g_{\ell,\epsilon}(a)) by
\(f_\ell^\epsilon(xu)=\sum_{a\ge0}g_{\ell,\epsilon}(a)x^a u^a\).
The coefficients are exactly

\[
g_{0,\epsilon}(0)=1,\quad g_{0,\epsilon}(1)=-1,\quad
g_{0,\epsilon}(a)=0\ (a\ge2),
\]
\[
g_{\ell,\epsilon}(0)=0,\quad
g_{\ell,\epsilon}(a)=-\frac{(\epsilon\ell)^{a-1}c_0^{a-1}}{a!}
\quad(\ell\ne0,\ a\ge1).
\]
Thus, for each (k\ge0), the completely expanded coefficient is

\[
\kappa_{J,k}(\ell)=
\sum_{a=0}^k\sum_{b=0}^{k-a}
g_{\ell_s,\epsilon_s}(a)g_{\ell_t,\epsilon_t}(b)
\frac{(c_0 A_J(\ell))^{k-a-b}}{(k-a-b)!}.
\]

Equivalently, the exact polynomial at total amplitude jet (h) is

\[
P_{J,h}(x;\ell)=\sum_{k=0}^{h}
  B_{h-k}(T,d,d',R;\text{visible primes},\ell,\chi)
  \kappa_{J,k}(\ell)x^{2+k},
\]

where (B_r) is the coefficient of (u^r) in the product of the
q-independent visible-slot factors, carrier root sum, visible prefix phases,
and exact source normalization. It is not an unspecified q-tail: the only q
dependence in each displayed monomial is the explicit (x^{2+k}/q).
The common normalization (a_\phi(T)^{-5}L^{-5}), real-part pairing,
assignment multiplicity, all path constraints and all source masks remain in
the outer coefficient (B_r\kappa_{J,k}).

For an exact q-mask signature \(\eta\), define

\[
Q_\eta(T;P_{\rm vis})=\{q\le N(T):q\text{ ordinary prime},\ q\notin
P_{\rm vis},\ \chi_\eta(q;T,d,d',R)=1\},
\qquad
M_{\eta,j}=\sum_{q\in Q_\eta}\frac{(\log q)^j}{q}.
\]

Then the exact omitted contribution to one row/column at jet (h) is
\[
E_h=\sum_{k=0}^h\sum_\eta
  B_{h-k,\eta}\kappa_{J,k,\eta}M_{\eta,2+k}.
\]
The exponent range is exactly (2\le j\le2+h). The required source rows
reach (h=6) in the size-6 and size-8 blocks and (h=8) in B16. Hence
the candidate powers are 2–8 and 2–10, respectively. The corresponding
pair-slot signatures found from the 20 descriptors are

`(0,4),(1,4),(2,4),(3,4),(0,3),(1,3),(2,3),(0,2),(1,2)`.

If and only if the source masks for q depend on this pair signature alone,
the block candidate counts in the table follow: B6 (2\times7=14), B8a
(4\times7=28), B16 (5\times9=45), B8b (5\times7=35). Across blocks,
the corresponding union has (4\times7+5\times9=73) coordinates. The
actual exact count is
\(\sum_\eta(1+h_{\max}(\eta))\), with h starting at zero, **after** exact
source-mask signatures have been read and merged only on proved equality.
Those executable signatures are absent from the source ledger, so 73 is a
transparent structural count, not a falsely certified minimal count.

The scalar moments (M_{\eta,j}) are real and nonnegative. The path
coefficients are generally complex because (c_0=2\pi i); the conjugate
orientation/path contributes its complex conjugate. The source real part
therefore uses real pair sums. No independent rank-two complex moment is
introduced by conjugation.

The constructor [wp84_hidden_prime_moment_constructor.py](/C:/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit/src/wp84_hidden_prime_moment_constructor.py)
records the exact descriptor pairs and coefficient formula. It preserves
unresolved q-mask signatures instead of treating pair positions as proof of
identical windows.

## Correction rank and determinant-preserving operations

At order (h=0), only (M_{\eta,2}) occurs. A single common scalar would
give a rank-one column update only if all columns have the same exact q-mask
and the same coefficient vector up to one fixed common row vector. The
source-defined matrix has path/layout-dependent pair signatures; equality of
those coefficient vectors is not proved. For (h>0), the triangular rule
(M_{\eta,2},\ldots,M_{\eta,2+h}) is exact, but their coefficient vectors
also include distinct path phase (A_J(\ell)) and visible/source factors.
No determinant-preserving column difference annihilates them without an
identity between those exact vectors. No such identity is in the repository.

Therefore the exact correction-matrix ranks are **undetermined**, not
assumed low. The algebraic template is
\[
M_B^{\rm full}=M_B^{\rm visible}+\sum_{\eta,j}M_{\eta,j}C_{B,\eta,j},
\]
where (C_{B,\eta,j}) is the exact coefficient matrix obtained by summing
the (B_{h-k}\kappa_{J,k}\) factors over admitted paths, roots, assignments,
and rows with (j=2+k). Its entries are complex before conjugate pairing
and real after the source real-part operation. Determining
\(\dim\operatorname{span}\{C_{B,\eta,j}\}\) requires the omitted executable
mask/selector data and the complete source sums.

## Exterior power and large-section expansion

For each fixed path and row jet (h_i), the exact source section formula
gives a Laurent polynomial in the actual section length (n_i=d'_i), with
powers (-1,\ldots,h_i). Its leading coefficient is
\[
 a_i\mathbf1_m,\qquad a_i=(c_0\lambda_i)^{h_i}/(h_i+1)!,
\]
the same all-ones column vector for all (m) entries in that row. Thus the
top exterior term vanishes. Any determinant monomial with two rows using
their leading coefficient also vanishes. The first *possible* total section
deficit from the maximal powers is (m-1), with coefficient
\[
\Delta^{\rm poss}_B=
\sum_{k=1}^m a_k\det(r_1,\ldots,r_{k-1},\mathbf1_m,
                         r_{k+1},\ldots,r_m),
\]
where (r_i\) is the coefficient vector of (n_i^{h_i-1}) in that source
row (using its exact hidden moments and masks). This is an exact symbolic
coefficient formula, not a claimed nonzero number. It may cancel; if it does,
the first possible order is later. We have not computed the (r_i) from the
complete source pool, so we cannot call (m-1) the first nonzero order or
give its rational/symbolic evaluated coefficient.

At (R=6000), every closed five-step displacement has prefix range at most
12000, so the source root formula applies for (d'\ge12001). The existing
exact replay verifies its jet identity through (u^{13}). Since the source
only supplies (d'/d\to1), it supplies no numerical (T_0) at which
(d'\ge12001) begins; more critically, it gives no lower bound for
\(\Delta^{\rm poss}_B\). There is no legal sign or nonvanishing conclusion.

The 18 visible repeated-prime layouts have no independent q moment and are
not charged with (M_{\eta,j}). Their source entries still depend on the
actual large section, paths, visible carrier primes, and masks. Their
visible-only rectangular subsystems have not yielded a square nonzero minor,
so none is promoted.

## PNT and the exact remaining theorem

If a q signature is the full interval of ordinary primes up to (N(T)),
excluding the at-most-three visible carrier primes, ordinary PNT and partial
summation give, for each fixed (j\ge2),
\[
M_j(T)=\frac{(\log N(T))^j}{j}+o((\log N(T))^j)
 =\frac{(L-\sqrt L)^j}{j}+o(L^j).
\]
The finite visible-prime exclusions are (O_j(1)). For a verified fixed
normalized interval (N^\alpha<q\le N^\beta), (0<\alpha<\beta\), the
main term is \((\beta^j-\alpha^j)(\log N)^j/j\). No such interval may be
substituted for a mask signature that has not been shown to be that interval.
These scalar PNT asymptotics do not evaluate the row/path coefficient
matrices or prove that the exterior coefficient avoids cancellation. They
also give no explicit error constant adequate for a determinant margin.

The precise missing theorem is a complete-source, vector-valued moment
asymptotic. For each block (B), let (Q_\eta(T)) be the exact source set
above and form (C_{B,\eta,j}(T,d,d',6000)) by the displayed coefficient
formula, with the source-selected rows and all conjugates. Prove uniformly
over the actual selector branch that
\[
\left\|\sum_{\eta,j} C_{B,\eta,j}(T,d,d',6000)
 \left(M_{\eta,j}(T)-\operatorname{Main}_{\eta,j}(T)\right)
 +\mathcal R_B(T)\right\|_{\wedge^m}
 < \frac12\left|\Delta^{\rm Main}_B(T)\right|,
\]
where `R_B` is the exact higher-section remainder and
\(\Delta^{\rm Main}_B\) is the first nonzero coefficient of the exterior
expansion after inserting those Main terms. The q-range is the full exact
source-admissible set (Q_\eta(T)\subseteq\{q\le N(T):q\text{ prime}}),
the weight is exactly (1/q), and all powers (j=2,\ldots,10) that occur
in the block are required. Uniformity must include the source-selected
(d'/d\to1) sections and all exact masks; (R) is fixed at 6000. The
required error is less than half the actual main exterior margin.

At present neither (Q_\eta) as an executable predicate nor a positive
lower bound for \(|\Delta^{\rm Main}_B|\) is available, so no numerical
constant or (T_0) can be honestly supplied. This is the exact boundary: a
scalar PNT main term is known in the unmasked interval case, but it does not
close the signed matrix/wedge theorem. No fifth block rank is promoted;
global fifth rank remains 38–72.

## Replay and hostile tests

Run:

```text
python src/wp84_hidden_prime_moment_constructor.py
python src/wp84_hidden_prime_wedge_certificate.py
python src/wp84_hidden_prime_moment_replay.py
```

The independent replay checks all 38 descriptors, the 20/18 split, the
conditional 73-coordinate structural basis, and exact q-local filter
coefficients. Its corruption suite rejects: a visible layout labeled hidden;
one deleted hidden moment; a changed log exponent; all hidden moments set to
zero; replacing the complete q-range with six primes; replacing the source
section with (d=2); changing (R); and perturbing the first possible
exterior coefficient. The wedge certificate records the exact leading-row
cancellation and explicitly marks the first possible coefficient as
undetermined rather than fabricating a rank or a sign.
