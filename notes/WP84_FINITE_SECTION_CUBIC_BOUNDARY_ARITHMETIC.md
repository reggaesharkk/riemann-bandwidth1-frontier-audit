# WP84 — finite-section cubic boundary correction: exact source decomposition

**Decision B:** the exact scalar-background summand is source-valid and is (o(1)) after normalization. The remaining signed cubic boundary correction is not shown to vanish. Strict (>79%) remains open.

This note accepts the previously replayed infinite-lattice no-wrap identity and its endpoint corrections. It addresses the distinct finite-section comparison, retaining the original prime field and contiguous section.

## Source object and conventions

Put (L=log X), (X=T/(2pi)), (N=lfloor Xe^{-sqrt L}floor), and (d=lfloor TL/(2pi)floor). The admissible contiguous section is (I=[k_-,k_-+d'-1]), with (d'/d	o1). Every prime power (n=p^vle N) is retained:

\[
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\qquad z_n=c_ne^{iT\log n},\qquad \alpha_n=\frac{\log n}{L}.
\]

For (k\in\mathbb Z), write
\[
A_k=\sum_{p^v\le N}\Im\!\left(z_{p^v}e^{2\pi i k\alpha_{p^v}}\right),\quad
\beta_k=\sum_{p^v\le N}2(1-\alpha_{p^v})\Re\!\left(z_{p^v}e^{2\pi i k\alpha_{p^v}}\right).
\]
With (J_{ij}=1/(\pi(j-i))) for (i\ne j), (J_{ii}=0), the source prime operator is (H=s_0(T)I+V), where (V=\operatorname{diag}(\beta)+[\operatorname{diag}(A),J]). Thus
\[
v_{ij}=\delta_{ij}\beta_i+(1-\delta_{ij})\frac{A_i-A_j}{\pi(j-i)}.
\]
The commutator is Hermitian because (J^*=-J); in particular (v_{ij}=v_{ji}\in\mathbb R). The scalar (s_0(T)I) has no (P)-to-(Q) block.

## Exact block identity

Let (P=P_I), (Q=I-P), and use the block names
\[
\mathcal A=PHP:P\mathcal H\to P\mathcal H,\quad
\mathcal B=PHQ:Q\mathcal H\to P\mathcal H,\quad
\mathcal C=QHP=\mathcal B^*,\quad
\mathcal D=QHQ:Q\mathcal H\to Q\mathcal H.
\]
Insertion of (P+Q) between the three factors gives
\[
PH^3P=\mathcal A^3+\mathcal A\mathcal B\mathcal C+\mathcal B\mathcal C\mathcal A+\mathcal B\mathcal D\mathcal C.
\]
Here (mathcal B) is Hilbert–Schmidt: only the commutator crosses the section, and its entries are bounded by (2S/(\pi|j-i|)) with (S=\sum_{p^v\le N}|c_{p^v}|). The products above are trace class. Cyclicity on the finite (P)-space turns the two middle trace terms into equal copies. Therefore, with traces on (P\mathcal H),
\[
\boxed{\operatorname{Tr}(PH^3P)-\operatorname{Tr}((PHP)^3)
=2\operatorname{Tr}(\mathcal A\mathcal B\mathcal C)+\operatorname{Tr}(\mathcal B\mathcal D\mathcal C).}
\]
The dimensions match: (mathcal A) acts on (P), (mathcal B:Q\to P), (mathcal C:P\to Q), and (mathcal D) acts on (Q). Hermiticity gives (\mathcal C=\mathcal B^*); both displayed traces are real.

Now split (H=s_0I+V). Since (P(s_0I)Q=0), (mathcal B=PVQ), (mathcal A=s_0P+V_{PP}), and (mathcal D=s_0Q+V_{QQ}). Hence the separation is exact:
\[
\boxed{\Delta_I=3s_0(T)\|PVQ\|_{HS}^2+R_I,}\qquad
R_I=2\operatorname{Tr}_P(V_{PP}\mathcal B\mathcal B^*)+
\operatorname{Tr}_P(\mathcal B V_{QQ}\mathcal B^*).
\]
The coefficient is (2s_0+s_0=3s_0). This also follows by expanding (operatorname{Tr}(P(s_0I+V)^3P)) and (operatorname{Tr}((s_0P+V_{PP})^3)); their scalar-dependent difference is (3s_0[\operatorname{Tr}(PV^2P)-\operatorname{Tr}(V_{PP}^2)]=3s_0\|PVQ\|_{HS}^2). No scalar term was dropped.

## Full prime-power expression and sector bookkeeping

For each (n=p^v\le N), define (V_n) by the preceding entry formula with (A_k,\beta_k) replaced by
\[
A_{n,k}=\Im(z_ne^{2\pi ik\alpha_n}),\qquad
\beta_{n,k}=2(1-\alpha_n)\Re(z_ne^{2\pi ik\alpha_n}).
\]
Then (V=\sum_{n=p^v\le N}V_n), a finite sum. The signed remainder has the exact source expansion
\[
R_I=\sum_{n_1,n_2,n_3\le N\atop n_j\text{ prime powers}}
\left\{2\operatorname{Tr}_P((V_{n_1})_{PP}(V_{n_2})_{PQ}(V_{n_3})_{QP})+
\operatorname{Tr}_P((V_{n_1})_{PQ}(V_{n_2})_{QQ}(V_{n_3})_{QP})\right\}.
\]
This is a convergent trace-class pairing for each fixed (T,N). It retains the actual (c_n), all carriers (e^{iT\log n}), all prime powers, both sign choices implicit in the real and imaginary parts, both terms of the block formula, and every path crossing out of the section and returning. No independent phases, arbitrary positive weights, or truncated prime pool are substituted. It is legitimate to regroup the finite prime-power triple sum into diagonal/mixed, repeated-base/proper-power, and all-distinct populations, but the regrouping does not itself bound any population.

In source entries,
\[
\|PVQ\|_{HS}^2=\frac1{\pi^2}\sum_{i\in I,\,j\notin I}\frac{(A_i-A_j)^2}{(j-i)^2}.
\]
For the remaining (R_I), writing (O=[\operatorname{diag}(A),J]), its exact diagonal/off-diagonal split is
\[
R_I=2\operatorname{Tr}_P((\operatorname{diag}(\beta)_P+O_{PP})\mathcal B\mathcal B^*)
+\operatorname{Tr}_P(\mathcal B(\operatorname{diag}(\beta)_Q+O_{QQ})\mathcal B^*).
\]
The (eta)-weighted terms need not be positive, and the Hermitian commutator blocks need not be positive. Cyclicity and conjugate pairing make the total real; they do not force it to vanish or have a favorable sign. The phases in the triple sum contain the actual signed products (e^{iT(\pm\log n_1\pm\log n_2\pm\log n_3)}); no arithmetic orthogonality follows merely from Hermiticity. Prior full-section repeated-base estimates cannot be transferred to these endpoint-weighted boundary traces without an additional proof.

## A source-valid (o(1)) sector

For a section of length (d'), exactly (2\min(r,d')) ordered pairs ((i\in I,j\notin I)) satisfy (|j-i|=r). Also (|A_i-A_j|\le2S). Thus
\[
\|PVQ\|_{HS}^2\le\frac{8S^2}{\pi^2}\sum_{r\ge1}\frac{\min(r,d')}{r^2}
\le\frac{8S^2}{\pi^2}(H_{d'}+1).
\]
The prime number theorem (or the standard Chebyshev upper bound) gives, for (a_\phi(T)\to1),
\[
S=\frac1{|a_\phi|L}\sum_{p^v\le N}\frac{\Lambda(p^v)}{\sqrt{p^v}}=O(\sqrt N/L),
\]
with prime powers included. Therefore
\[
\frac{|3s_0|}{d'}\|PVQ\|_{HS}^2
\le\frac{24|s_0|S^2(H_{d'}+1)}{\pi^2d'}
=O\!\left(\frac{N}{T L^2}\right)
=O\!\left(\frac{e^{-\sqrt L}}{L^2}\right)=o(1),
\]
using (s_0\to1), (d'\asymp TL), and (N\asymp T e^{-\sqrt L}). This is the exact scalar-background summand in the finite-section boundary correction. It is a genuine new source-defined sector bound, not a bound for the full correction.

## What remains open

The old trace-ideal argument bounds the signed remainder only absolutely:
\[
\frac{|R_I|}{d'}\le\frac{(2\|V_{PP}\|_{op}+\|V_{QQ}\|_{op})\|PVQ\|_{HS}^2}{d'}
=O\!\left(\frac{S^3(H_{d'}+1)}{d'}\right)
=O\!\left(\frac{N^{3/2}}{T L^3}\right).
\]
At (N\asymp T e^{-\sqrt L}), this is (O(T^{1/2}e^{-3\sqrt L/2}/L^3)), which does not tend to zero as a *bound*. It is not a lower bound or a counterexample. In this boundary-weighted sum, the all-distinct and repeated-base sectors still carry the complete natural prime pool, section endpoints, and near-alias phases. The previously proved global moment or collision statements do not supply this endpoint-local estimate.

The first unresolved estimate is therefore one formula:
\[
\sup_{I\ \mathrm{admissible}}\left|\frac1{d'}\sum_{n_1,n_2,n_3\le N\atop n_j\text{ prime powers}}
\left(2\operatorname{Tr}_P((V_{n_1})_{PP}(V_{n_2})_{PQ}(V_{n_3})_{QP})+
\operatorname{Tr}_P((V_{n_1})_{PQ}(V_{n_2})_{QQ}(V_{n_3})_{QP})\right)\right|=o(1).
\]
It must be proved with the actual prime coefficients, phases, and the same sampled section. The global coefficient (L^1) mass controls (S) but leaves the cubic factor (S^3); a global (L^2) bound does not imply concentration in the endpoint-weighted near-alias windows. No such arithmetic estimate is established here.

## Independent exact replay and scope

Run:

```powershell
python src/wp84_finite_section_boundary_cubic.py
python src/wp84_finite_section_boundary_cubic_replay.py
```

The replay independently builds a rational-frequency finite Hermitian source-form matrix, verifies the block identity and exact (3s_0\|PVQ\|_{HS}^2) split, checks shifted-section crossing counts, and rejects omission of (s_0) or reversal of the source commutator. That finite root-of-unity case is an algebra diagnostic only; it is not the natural prime pool or a zeta asymptotic computation.

No (m_3=2), (0.105) conditioned-energy bound, prime-to-Weil identification, zero-side result, or strict (>79\%) theorem is claimed. The finite-section boundary transfer remains incomplete.
