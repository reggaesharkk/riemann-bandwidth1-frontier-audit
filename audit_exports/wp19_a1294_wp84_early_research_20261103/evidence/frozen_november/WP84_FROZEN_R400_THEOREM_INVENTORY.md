# WP84 — frozen R400 theorem inventory

Base: `99712a495db3258f938f2509d1eaa37cbc966a03`  
Branch: `codex/wp84-frozen-theorem-inventory-20261103`  
Scope: extract independently checkable mathematics from the R400 audit chain. This record does not resume the endpoint-averaging proof attack.

## Frozen decisions

| Claim | Frozen status |
|---|---|
| Ordinary-prime physical connected aggregate | **OPEN** |
| Complete product-frequency endpoint selection | **INCOMPLETE** |
| R400 record budget | **OPEN** |
| Conditional 68.820273% route | **NOT PROMOTED; conditional only** |
| Strict greater-than-79% theorem | **OPEN** |
| Riemann Hypothesis | **OPEN** |

These statuses are consistent with the final endpoint-restricted audit at the base. The source-defined one-prime endpoint/boundary set is not silently identified with the missing fourth-order product-frequency gate. No older theorem statement or decision is edited here.

## Notation and source boundary

At finite \(T\), put \(L=\log(T/(2\pi))\), \(N=\lfloor e^{L-\sqrt L}\rfloor\), \(h=2\pi/L\), and \(I=[a,a+m-1]\). For a source frequency \(u=\log n/L\),
\[
D_I(u)=\frac1m\sum_{k\in I}e^{2\pi iku}.
\]
The source coefficients are (c_n=-\Lambda(n)/(a_\phi(T)L\sqrt n)). For (R) fixed, the physical hard-band matrix is the finite compression of
\[
H_{T,R}=M_{\beta}+ [M_{\alpha},J_R],\qquad
(J_R)_{ij}=\frac{1}{\pi(j-i)}\; (0<|i-j|\le R),
\]
with zero entries outside the band. A balanced fourth-order source tuple carries (Y=\log(A/B)), the carrier (e^{iTY}), the section-start phase exactly once, its original coefficient product, the common filtered overlap, and the physical row cumulant. The source measure is complex; it is not a probability measure and does not make the kernel positive.

## Candidate 1 — exact physical finite-trace/cumulant identity and kernel mismatch

### Theorem statement

Fix finite (T,R,I), the finite source pool and all labels admitted by the source. Let (X_1(k),\ldots,X_4(k)) be the four entries on a closed hard-band lag path rooted at row (k). Define their empirical joint cumulant using the 26 anchored ordered fourth-partition terms. Then the sum of physical row cumulants over all closed paths has the exact finite expansion
\[
\operatorname{Connected}_{4,\mathrm{row}}(T,R,I)
 =\int \Omega_{4,R}(v)\,\kappa_{m,I}(v)\,d\mu_{T,I}(v),
\]
where
\[
\kappa_{m,I}(v)=\sum_{\pi\in\Pi^{\mathrm{ord}}_{4,\mathrm{anch}}}
(-1)^{|\pi|-1}\prod_{B\in\pi}D_I\!\left(\sum_{j\in B}v_j\right).
\]
The partition ledger has respectively (1,7,12,6) ordered terms for one through four blocks and 75 block factors in total. It retains the selected section, carrier, source coefficient, hard cutoff and all six balanced orientations. The finite-compression root correction is a separate source term; it is not absorbed into this full-lattice row-cumulant identity.

Explicitly, with $n_j=p_j^{e_j}\le N$, $\epsilon_j\in\{-1,1\}$, $v_j=\epsilon_j\log(n_j)/L$, $S=\sum_jv_j$, and $a$ the first row of $I$, the finite source measure is
\[
d\mu_{T,I}=\sum_{\substack{n_j=p_j^{e_j}\le N\\\epsilon\in\{-1,1\}^4}}
\left(\prod_{j=0}^3c_{n_j}\right)e^{iTLS}e^{2\pi iaS}\,\delta_v.
\]
The six balanced words are the $2+2$ part of this labeled sum. In a local-row convention the start phase is outside the row means; in an absolute-row convention it is already in $D_I$. It is included exactly once.

### Proof

Expand each finite matrix entry into its source frequencies. For a block (B), the empirical row moment is the finite average (D_I(\sum_{j\in B}v_j)), multiplied by the common tuple coefficient and carrier. The cumulant is the signed sum of products of these block moments. The four external path coefficients sum to the filtered overlap (\Omega_{4,R}). All sums are finite, so regrouping by source tuple and ordered partition is exact. No limit, independent-row assumption, Gaussian assumption, or replacement of a product of row means by a nested overlap is used.

### Exact nonidentity witness

For
\[
v=(1/5,-2/5,3/5,-2/5),\qquad \sum_jv_j=0,
\]
and (5\mid m), every nonempty proper block sum is a noninteger fifth. Hence each of its row means is exactly zero, and the 26 physical signed term totals by block count are ((1,0,0,0)); thus \(\kappa_{m,I}(v)=1\). The public nested-path geometric bracket has block-count totals
\[
1,\quad -21/5,\quad 24/5,\quad -8/5,
\]
and total zero. Its sharp outer overlap is (O_A=2/5). Therefore the physical sharp kernel equals (2/5), while the geometric product (O_AB_{4,nc}) equals zero. The R400 interval certificate gives a positive filtered physical value at this point (approximately (0.3997484808471383145) for the listed ordering).

This proves that the two kernels are not interchangeable. It does not prove a positive ordinary-prime aggregate. The exhibited physical tuple ((p,p^2,p^3,p^2)), with (T=2\pi p^5), is a proper-prime-power resonance; its complete one-base/permutation family is separately bounded by (O_R(L^{-4})). The actual filtered physical two-state connected matrix is also indefinite: the certified cross entry at product scale (4/5) is in ([1.5984986896906511955,1.5984986896906511956]), while one diagonal is zero, so its determinant is negative for every value of the other diagonal.

### Provenance, limitations and verification

Primary sources in the repository: [physical kernel reconciliation](/notes/WP84_PHYSICAL_KERNEL_PROPER_POWER_AGGREGATE_AUDIT.md), [actual filtered connected kernel](/notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md), [finite source ledger](/evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json), and their exact checker and interval certificate. The tuple identity and counterexample are standalone finite mathematics after the two kernel definitions are fixed. The filtered R400 decimal enclosure is a computer-assisted interval claim; independently check the interval implementation, root intervals, orientation ordering and coefficient convention. The source-admissible proper-power family bound is an asymptotic source-specific statement, not a consequence of the pointwise witness.

### Literature assessment

The moment/cumulant partition formula is classical Möbius inversion on the partition lattice, not a new identity; Speed’s treatment is a direct reference. The source-specific discrepancy is an exact example comparing two different kernels. No priority or novelty claim is made.

## Candidate 2 — complete proper-power Schatten absorption

### Theorem statement and hypotheses

Fix (R<\infty). Assume (a_\phi(T)\to1), (N=\lfloor e^{L-\sqrt L}\rfloor), and use the actual proper-power pool (n=p^e\le N), (e\ge2), with
\[
c_{p^e}=-\frac{\log p}{a_\phi(T)Lp^{e/2}}.
\]
Build (Q_{R,I}) from the source fields \(\alpha_k=\Im\sum c_ne^{iT\log n}e^{2\pi ik\log n/L}\) and the corresponding \(\beta_k\) with multiplier (2(1-\log n/L)\), using the exact commutator matrix above. Let (I) be any contiguous row interval of length
\[
m\ge d-2q,\qquad d=\lfloor TL/(2\pi)\rfloor,\quad q=\lfloor d/\sqrt L\rfloor,
\]
with arbitrary start row. With normalized trace \(\tau_I=m^{-1}\operatorname{tr}\), uniformly over such sections,
\[
\tau_I(Q_{R,I}^2)=O_R(L^{-2}),\qquad \|Q_{R,I}\|_{op}=O_R(1),
\]
and hence
\[
\tau_I(Q_{R,I}^4)=O_R(L^{-2}),\qquad
\left|\tau_I((A_{R,I}+Q_{R,I})^4)^{1/4}-\tau_I(A_{R,I}^4)^{1/4}\right|=O_R(L^{-1/2})
\]
for every Hermitian (A_{R,I}). The last estimate assumes no bound on either fourth moment.

### Proof

Write (M_1=\sum_{e\ge2,p^e\le N}|c_{p^e}|) and (M_2=\sum|c_{p^e}|^2). Chebyshev’s bound and the geometric sum over exponents give (M_1=O(1)). The elementary bounds in the source ledger give
\[
M_2\le\frac{1}{|a_\phi|^2L^2}\sum_p\frac{(\log p)^2}{p(p-1)}\le\frac{64}{|a_\phi|^2L^2}=O(L^{-2}).
\]
The matrix row-sum estimate gives
\[
\|Q_{R,I}\|_{op}\le 2M_1(1+2H_R/\pi)=O_R(1).
\]
For the finite grid, $u_n=\log n/L$ has circular spacing $\delta\ge((N+1)L)^{-1}$. Dual Montgomery–Vaughan large sieve on any $m$-row interval gives
\[
\frac1m\sum_{k\in I}\left|\sum_n a_ne^{2\pi iku_n}\right|^2
\le (1+\delta^{-1}/m)\sum_n|a_n|^2.
\]
Since $\delta^{-1}/m=O(N/T)=o(1)$ uniformly, apply this to the alpha and beta source fields. Substitution into the exact finite-matrix formula for $\tau_I(Q^2)$ yields $O_R(M_2)=O_R(L^{-2})$. For Hermitian $Q$, $\tau(Q^4)\le\|Q\|_{op}^2\tau(Q^2)$. Finally use the normalized Schatten-4 triangle inequality. This gives a fourth-root perturbation, not an unqualified difference of fourth powers.

### Provenance, limitations and verification

Primary source: [Schatten and ordinary-aggregate audit](/notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md), [finite operator ledger](/evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json), and `src/wp84_r400_schatten_absorption_audit.py`. The arbitrary-matrix implication \(\tau(Q^2)\ll L^{-2}\Rightarrow\|Q\|_{op}\ll1\) is false; the ledger gives (Q=\mathrm{diag}(n,0,\ldots,0)) in dimension (n^4). The separate source \(\ell^1\) estimate is essential. This absorption does not prove a bounded ordinary-prime fourth moment or an additive (o(1)) difference of raw fourth traces.

The large-sieve input is the dual form of Montgomery–Vaughan’s separated-frequency theorem; the Schatten triangle inequality is standard trace-ideal theory. The nontrivial WP84 content is the coefficient and finite-grid transfer under the displayed hypotheses. Both inputs should be independently checked before reuse.

## Candidate 3 — fourth-cumulant endpoint sensitivity

### Theorem statement

For any two probability measures \(\mu,\nu\) on a finite row set, define (D_\mu(x)=\sum_k\mu(k)e^{2\pi ikx}) and the 26-term fourth-cumulant expression \(\kappa_\mu(v)\) above. For every (v\in\mathbb R^4),
\[
|\kappa_\mu(v)-\kappa_\nu(v)|\le75\|\mu-\nu\|_1.
\]
If (I,J) are each obtained from a common (d)-row set by deleting at most (r) rows, then \(|\kappa_I-\kappa_J|\le300r/d\). If one section is the full grid and the other deletes (r) rows, the sharper bound is (150r/d). A one-row endpoint deletion has the exact identity
\[
D_{I'}(x)-D_I(x)=\frac{D_{I'}(x)-e^{2\pi iqx}}{m},
\]
where (q) is the removed row and (I') has length (m-1). For each ordered partition product, the exact change is the finite telescoping sum retaining the original Möbius coefficient.

### Proof

Each Fourier mean has modulus at most one and \(|D_\mu(x)-D_\nu(x)|\le\|\mu-\nu\|_1\). For a product with (q) block factors, replace its factors one at a time; its change is at most (q\|\mu-\nu\|_1). Sum this over the 26 terms: the total number of factors is 75, giving the first inequality. For a uniform (d)-point measure and its restriction to (d-r) points, the exact (\ell^1) distance is (2r/d); the two-section estimate follows by a triangle inequality. The endpoint formula follows by separating the deleted summand and changing the denominator. The product identity is the standard finite telescoping expansion.

### Provenance, limitations and verification

Primary source: [physical cumulant endpoint difference and tensor lift](/notes/WP84_R400_PHYSICAL_CUMULANT_ENDPOINT_DIFFERENCE_AND_TENSOR_LIFT.md), [exact rational ledger](/evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json), and `src/wp84_r400_cumulant_endpoint_tensor.py`. Exact regressions check all 26 terms, both endpoint directions, zero detuning, aliases and the (300r/d) consequence. The bound is per tuple/frequency. Summing it against the absolute prime-tuple mass does not control the full aggregate; that failure is recorded in the ordinary-aggregate audits.

This is an elementary stability inequality and a source-shaped application of the classical partition formula. It is self-contained but has low standalone novelty absent a new application or sharper source-weighted estimate.

## Candidate 4 — tensorized averaging over finite sections

### Theorem statement

Let \(\{I_s\}\) be a finite nonempty family of finite row sets with probabilities \(\rho_s\ge0\), \(\sum_s\rho_s=1\). For an ordered partition \(\pi\) with (q=|\pi|), define
\[
W_\pi((k_B)_{B\in\pi})=
\sum_s\rho_s |I_s|^{-q}\prod_{B\in\pi}\mathbf1_{\{k_B\in I_s\}}.
\]
Then (W_\pi\ge0), \(\sum_{(k_B)}W_\pi=1\), and
\[
\sum_s\rho_s\kappa_{I_s}(v)
=\sum_\pi(-1)^{|\pi|-1}\sum_{(k_B)}W_\pi((k_B))
\exp\!\left(2\pi i\sum_{B\in\pi}k_Bv_B\right).
\]
This is an exact identity for the average of products of row means; it does not replace that average by a product of averages.

### Proof

Expand each $D_{I_s}(v_B)$ as its normalized finite row sum. For each fixed partition, the product expansion gives the joint row tuple $(k_B)$ with mass $|I_s|^{-q}\prod_B1_{k_B\in I_s}$. Average this expression with weights $\rho_s$ and interchange finite sums. Nonnegativity is immediate; summing over all row tuples gives $\sum_s\rho_s |I_s|^{-q}|I_s|^q=1$. Sum over partitions with their unchanged Möbius signs.

### Provenance, limitations and verification

The source tensor ledger is in [the endpoint tensor audit](/notes/WP84_R400_PHYSICAL_CUMULANT_ENDPOINT_DIFFERENCE_AND_TENSOR_LIFT.md) and [its exact ledger](/evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json). For the physical aggregate, the source coefficient, carrier, filtered overlap and root/path factor depend on the section and must remain inside the same average. The resulting weighted tensor can be complex and need not have unit total mass. The unweighted probability normalization therefore proves no sign or norm estimate for the physical sum.

This is finite Fubini expansion, not a new averaging theorem; it is fully self-contained and standard.

## Candidate 5 — exact fixed-scale geometric balanced kernel

### Theorem statement

This statement is about the public **geometric nested-overlap model only**. Fix exact product scale (1\le s\le2), choose (x,y\in[s-1,1]), and let
\[
d_s(x)=\min(x-s+1,1-x),\qquad d_s(y)=\min(y-s+1,1-y).
\]
Let (C_s(x,y)) be the sum of the six balanced sign interleavings of the public connected geometric overlap kernel, with the positive pair ((x,s-x)) and negative pair ((y,s-y)). Then
\[
C_s(x,y)=-2(s-1)\min(d_s(x),d_s(y)).
\]
Thus (C_s) is negative semidefinite on each exact scale: for any finite points (x_i) and complex coefficients (z_i), \(\sum_{i,j}\overline z_i C_s(x_i,x_j)z_j\le0\). If (K_{ij}=d^{-1}\sum_{k\in I}e^{i\tau_k\log(m_i/m_j)}), then (K\succeq0) as a Gram matrix; the Schur product theorem consequently gives \(C_s\circ K\preceq0\).

### Proof

The six-word piecewise-linear overlap calculation reduces by pair swaps and positive/negative exchange to the chamber (s-1\le x\le y\le s/2). On each min/cutoff chamber, the exact ordered-partition bracket and overlap lengths simplify to the displayed expression; the repository’s exact rational checker refines the chamber by all branch hyperplanes and checks the identity with no floating decision. The PSD claim follows from
\[
\min(d_s(x),d_s(y))=\int_0^{s/2-(s-1)}
\mathbf1_{u\le d_s(x)}\mathbf1_{u\le d_s(y)}\,du.
\]
For each $u$, the matrix of indicator products is rank-one positive semidefinite. The Fourier matrix $K$ is the Gram matrix of $d^{-1/2}(e^{i\tau_k\log m_i})_k$. Apply the Schur product theorem.

### Provenance, limitations and verification

Sources: [fixed-scale connected kernel](/notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md), [orientation normalization](/notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md), and exact checkers `src/wp84_fixed_scale_connected_kernel.py`, `src/wp84_balanced_orientation_normalization.py`, and `src/wp84_phi4_equal_scale_brownian_kernel.py`. These scripts replayed successfully at the frozen base. The Brownian/min kernel and Schur product steps are standard. The finite six-orientation chamber identity is source-specific exact algebra. It is independent of the later WP84 consumer, but it is not an identity for the physical (\Omega_{4,R}\kappa_{m,I}) kernel. The positive physical witness and indefinite physical Gram matrix are explicit counterexamples to that transfer. No publication-priority claim is made.

## Candidate 6 — fixed-band pair-pair trace formula

### Theorem statement

Assume a centered stationary Hermitian band field has covariances
\[
\mathbb E\alpha_i\alpha_j=\tfrac14\delta_{ij},\quad
\mathbb E\alpha_i\beta_j=0,\quad
\mathbb E\beta_i\beta_j=\begin{cases}\tfrac16&i=j,\\-\tfrac1{2\pi^2(i-j)^2}&i\ne j.\end{cases}
\]
For the fixed hard band (R), let (P_R=M_\beta+[M_\alpha,J_R]). The pair-pair contraction sector is exactly
\[
\mathrm{Pair}_R=2t_{\mathrm{adj}}(R)+t_{\mathrm{opp}}(R)
=\frac1{12}+\frac{2H_2(R)}{3\pi^2}
+\frac1{\pi^4}\left(\frac{E_4(R)}8+2H_2(R)^2-\frac{3H_4(R)}4\right),
\]
where $H_j(R)=\sum_{r=1}^Rr^{-j}$,
\[
s_r=\sum_{\substack{0<|j|\le R\\0<|r-j|\le R}}\frac1{j(r-j)},\qquad
E_4(R)=4H_2(R)^2+2\sum_{r=1}^{2R}s_r^2.
\]
In particular, an exact rational enclosure for $\pi$ yields $\mathrm{Pair}_{400}<266329/10^6$.

### Proof and scope

The covariance tensor gives the adjacent/nested and crossing pairings. The adjacent term is the Parseval integral of the squared Toeplitz symbol (b_R(\theta)=1/6+(|h_R(\theta)|^2+2H_2(R))/(4\pi^2)); expanding its finite Fourier polynomial gives (E_4(R)). Direct covariance contraction gives (t_{opp}). The six balanced sign positions have the exact 4:2 orientation split, hence the factor (2t_{adj}+t_{opp}). The checker uses rational harmonic sums and Machin’s alternating arctangent bounds for π; it certifies the strict threshold with margin about (8.7810\times10^{-7}).

This is a theorem about the pair-pair contraction under the stated covariance data. It does not assume the complete field is Gaussian and does not bound the connected fourth cumulant. The covariance formulas are source inputs that require their own independent analytic verification before this can be used in a new model.

### Provenance and literature assessment

Primary source: [exact R400 pair layer](/notes/WP84_R400_EXACT_PAIR_LAYER.md), checker `src/wp84_r400_pair_layer_exact.py`, and the covariance ledger included in the R400 manifests. Toeplitz/Fourier trace manipulations and the finite convolution are standard; the exact R=400 rational certificate and covariance constants are WP84-specific. The derivation follows standard Fourier/Toeplitz methods as in Grenander–Szegő, but no claim of novelty is made.

## Independence and remaining consumer boundary

Candidates 1, 3, 4, and 5 are finite statements independent of the record consumer. Candidate 2 is an asymptotic theorem under explicit WP84 source hypotheses but is isolated from the ordinary-prime target moment. Candidate 6 is a source-covariance theorem; its finite arithmetic certificate is verified, while its covariance input is a separate hypothesis. None proves the ordinary-prime connected estimate. The exact missing source definition is the product-frequency endpoint feature/gate map; the smallest missing analytic inequality after that map is fixed is the conditional mean positive part of the complete physical connected sum on the complete common admissible set, strictly below \(3675673694911/148250000000000\).

The strict greater-than-79% theorem, conditional 68.820273% route, 79.62709668% benchmark and RH remain separate and unproved/open.
