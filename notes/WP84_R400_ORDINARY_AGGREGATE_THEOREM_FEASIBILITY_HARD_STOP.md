# WP84 — R400 ordinary-prime aggregate: theorem feasibility or hard stop

Base commit: `d81bb1b6e46fb571906e7098e11372a5c38e8a2c`; audit branch: `codex/wp84-ordinary-aggregate-feasibility-20261103`. Scope: local source-level feasibility audit. No source-prime counterexample or theorem is claimed.

## Decisions

| Gate | Decision |
|---|---|
| `PUBLISHED_SOURCE_TRANSFER` | **INSUFFICIENT** |
| `ENDPOINT_CORRECTION` | **OPEN** |
| `ORDINARY_CONNECTED_AGGREGATE` | **OPEN** |
| `R400_CONSUMER` | **OPEN** |
| `NEXT_ACTION` | **NEW_ANALYTIC_THEOREM_REQUIRED** |

The hard stop is on closing this aggregate with the audited published estimates. The source expression has not been shown to violate its bound. The proper-power absorption, physical positive-atom certificate, physical/geometric kernel discrepancy, endpoint cumulant identities, tensor identities, and predecessor negative results remain in the earlier commits and are hash-checked as unchanged inputs.

## 1. Frozen source expression and the required norm problem

Use the existing source normalization
\[
L=\log(T/(2\pi)),\quad N=\lfloor e^{L-\sqrt L}\rfloor,
\quad d=\lfloor TL/(2\pi)\rfloor,
\quad c_p=-\frac{\log p}{a_\phi(T)L\sqrt p}.
\]
The candidate section family is the source's Decision-B family
\(I_{u,v}=[b+u,b+d-1-v]\), with \(0\le u,v\le M_{end}=\lceil d e^{-\sqrt L/2}\rceil\), length \(m=d-u-v\), and its original uniform endpoint-pair measure unless the source explicitly conditions that measure. Thus \(m/d=1-O(e^{-\sqrt L/2})\); section start and length remain in the physical row means.
For the six balanced words \(\epsilon\in\{++--,+-+-,+--+,-++-,-+-+,--++\}\), put
\[
A=\prod_{j:\epsilon_j=+1}p_j,\quad B=\prod_{j:\epsilon_j=-1}p_j,
\quad Y=\log(A/B),\quad v_j=\epsilon_j\log(p_j)/L.
\]
The physical row cumulant is the source's 26 ordered anchored-partition sum
\[
\kappa_{m,I}(v)=\sum_{\pi}\mu(\pi)\prod_{D\in\pi}
D_{m,I}(v_D),\quad
D_{m,I}(x)=\frac1{m}\sum_{k\in I}e^{2\pi i kx/L},
\quad \mu(\pi)=(-1)^{|\pi|-1},
\]
with partition counts \(1,7,12,6\), signs \(+,-,+,-\), and 75 block factors in total. The filtered R400 overlap and the exact finite-compression/root correction remain attached to each labeled source tuple. In the parent ledger the full-lattice part is \(\Omega_{4,400}(v)\kappa_{m,I}(v)\); the finite root labels use their actual valid-root intervals, not a common substituted mask.

Writing \(\mathcal R^{root}_{T,I}(\epsilon,\mathbf p)\) for the exact additive finite path/root correction from those labels, the ordinary connected aggregate is grouped exactly as
\[
C^{ord}_{T,I}=\Re\sum_{\substack{A,B\le N^2\\A\ne B}}
\sum_{\substack{\epsilon\text{ balanced},\ p_0,p_1,p_2,p_3\le N\\
\prod_{\epsilon_j=+1}p_j=A,\;\prod_{\epsilon_j=-1}p_j=B}}
e^{iTY}\left(\prod_{j=0}^3c_{p_j}\right)
\left[\Omega_{4,400}(v)\kappa_{m,I}(v)
 +\mathcal R^{root}_{T,I}(\epsilon,\mathbf p)\right].
\]
Here the absolute-row convention for \(D_{m,I}\) includes the selected start phase; in a local-row convention the source carrier includes it once. Each root term is the original normalized sum over its valid interval \([a-\min q,a+m-1-\max q]\), divided by the source section length \(m\), with its own path, orientation, and coefficient; the root count is \(m-\ell\) and is not substituted as a new normalizer. There is no extra scalar copy of the row Fourier kernel. Each block character aliases according to its own \(v_D\bmod 1\); exact and near aliases are retained. This notation groups the frozen source formula and does not assert that the physical cumulant factors into a public geometric overlap. Every ordered tuple and its labels stay in the inner sum. The six words are counted once each. Exact \(A=B\) ordinary-prime tuples are removed into the pair contractions by unique factorization; all \(A\ne B\) near products, unequal product scales, and aliases remain.

For a useful estimate, write the inner source coefficient as a two-index array \(G_{A,B}(I,T)\). A linear large-sieve bound on row frequencies would need, at minimum, a proved usable norm for this complete array (for example its trace norm against an operator kernel, or a jointly matched factorization \(G_{A,B}=x_A\overline{x_B}\)) and the corresponding uniform operator bound. The source has not supplied that factorization or a PSD kernel. A Frobenius norm alone would also require a kernel Frobenius norm or a valid operator/trace-duality structure. The known prime coefficient mass \(\sum_p|c_p|^2=O(1)\) does not state any of these coupled 26-term, section-dependent bounds. The direct target is a bound for the positive part of the complete real source sum, not just one of its formal coefficient norms.

## 2. Quantified budget and endpoint quantifiers

The remaining record allowance is exactly
\[
\Delta_{max}=\frac{3675673694911}{148250000000000}
=0.0247937517363305\ldots.
\]
With the already established endpoint-and-boundary-good density at least \(1/4-\epsilon\), the joint-selection premise is
\[
\limsup_{T\to\infty}\mathbb E_{I\in\mathcal C_T}
  (\Re C^{ord}_{T,I})_+
<(1/4-\epsilon)\Delta_{max}.
\]
For the explicit \(\epsilon=1/8\) route this requires the strict bound
\[
\mathbb E(\Re C^{ord}_{T,I})_+<\Delta_{max}/8
=\frac{3675673694911}{1186000000000000}
=0.0030992189670413\ldots.
\]
The limiting threshold \(\Delta_{max}/4=0.0061984379340826\ldots\) is only approached as \(\epsilon\downarrow0\), with a boundary threshold that grows like \(1/\epsilon\). Neither is proved. A signed mean does not suffice: the exact two-point example \((-1,1)\) has signed mean zero and mean positive part \(1/2\). The existing endpoint selection lemma is valid conditional on the positive-part premise; it does not prove that premise.

## 3. Published theorem compatibility

### Natalie Evans, *Correlations of Almost Primes*

The primary paper's Theorem 1.1 concerns the indicator correlation of restricted E2 numbers \(n=p_1p_2\), with one factor in a prescribed logarithmic-size interval, over additive shifts \(h\). Its range is \(\log^{19+\varepsilon}X\le H\le X\log^{-A}X\) (\(A>3\)); its conclusion is an asymptotic for all but \(O(H\log^{-\eta}X)\) shifts. Sections 3 and 6 split major/minor arcs and prove a global centered major-arc remainder mean-square bound of size \(B^2(X)\ll X\log^{-\eta}X\). The \(q=1\) arc is part of this global bound. Theorem 1.3 treats typical E2 factorizations with a larger lower shift range, and Theorem 1.4 treats prime/E2 correlations only for \(H\ge X^{1/6+\varepsilon}\); neither is the six-orientation, section-dependent four-prime ratio sum here.

There are three failures of direct transfer. First, Evans averages the unweighted additive correlation over shifts and proves an almost-all-shift statement; WP84 needs the actual complex, section-dependent coefficients \(G_{A,B}(I,T)\) and the mean positive part over endpoint sections. Second, Evans's q=1 estimate is an absolute global L2 estimate, while the WP84 expression is a signed 26-term physical row cumulant with a root correction; a cancellation after pair subtraction is not identified with Evans's centered E2 remainder. Third, the important WP84 weighted E2 frequencies lie on the q=1 principal arc, so a generic minor-arc estimate does not address them.

On a close dyadic product cell, the exact reindexing is \(A=n\), \(B=n+h\) (or its reverse), with phase \(e^{iT\log(n/(n+h))}\). Evans's inner correlation is an E2 indicator product at \(n,n+h\); the WP84 coefficient is instead \(G_{n,n+h}(I,T)\), which depends on both products, all ordered prime splits, the section, and the row-cumulant partition. The match would require an identity reducing that coefficient to an admissible factorized E2 weight (or a proved weighted-shift extension with the corresponding norm). None is in the source record. In an E2-compatible sliced factor range, one product coefficient has scale \((\log P)/(|a_\phi|^2L^2\sqrt{M_{prod}})\) times the E2 weight; squaring it gives the \((\log P)^2/(|a_\phi|^4L^4M_{prod})\) factor below. This favorable slice still has the oversampling loss and does not represent all source tuples.

The normalization loss is explicit in the existing source-matched insertion. For product scale \(M_{prod}\), set \(H=M_{prod}/T\). The normalized WP84 factor slice carries \((\log P)^2/(|a_\phi|^4L^4M_{prod})\). Discrete-to-local oversampling multiplies the global integral bound by \(H\). Substituting Evans's global remainder gives only
\[
\ll \frac{H(\log P)^2}{|a_\phi|^4 L^4(\log M_{prod})^\eta}.
\]
At \(M_{prod}=T^s\), fixed \(s>1\), this is of order
\[
\frac{T^{s-1}(\log L)^2}{L^{4+\eta}},
\]
up to fixed constants, and diverges. It is not below \(\Delta_{max}\), much less the \(\Delta_{max}/8\) positive-part budget. This calculation only says the black-box estimate is too weak; it is not a lower bound on the WP84 sum.

The earlier scalar safe-lobe calculation proves \(\Re K_T(Y)\ge0\) for small detuning and pairs this with the public nested-overlap sign. It cannot remove the q=1 loss here: the preserved physical atom has \(\Omega>0,\kappa=1\) at a point where the public overlap values are \(O_A=2/5,B_4=0\). That witness is from the preserved proper-prime-power family and is not an ordinary-prime aggregate counterexample; it establishes kernel inequivalence only. No identity equating the public geometric kernel with \(\Omega\kappa_{m,I}\), including selected-section starts and root corrections, has been established. Reusing that lobe as a sign theorem for the physical cumulant would silently cross the known kernel discrepancy.

### Guth–Maynard, *New Large Value Estimates for Dirichlet Polynomials*

Theorem 1.1 assumes a single dyadic Dirichlet polynomial \(\sum_{N<n\le2N}b_n n^{it}\), coefficients \(|b_n|\le1\), and 1-separated sample heights \(t_r\in[0,T]\). It bounds the number \(R\) of sample heights at which the modulus exceeds a fixed threshold \(V\):
\[
R\le T^{o(1)}(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4}).
\]
The WP84 target is not a count of separated heights at which one fixed polynomial is large. It is a real signed four-prime ratio sum, whose coefficients vary with the selected section through the 26 row-cumulant products, the R400 filter, and path-root corrections. No exact source identity reduces it to the theorem's single polynomial and sample set. Even a hypothetical flattening would need coefficient rescaling to meet \(|b_n|\le1\), a matching threshold, and a large-value count over the actual endpoint family; the theorem supplies no signed mean or mean-positive-part estimate. It gives no calculable \(T,M,H\), or \(\log T\) saving in the WP84 normalization as currently matched, and hence no strict budget payment.

### Montgomery–Vaughan and checked repository bounds

The 1973 large-sieve Theorem 1 assumes separated sample points for a trigonometric polynomial and bounds its sampled square sum by \((d+\delta^{-1})\) times coefficient square mass. The repository's linear source-grid application uses the distinct one-prime points \(\log n/L\pmod1\), with \(\delta^{-1}=O(NL)\), and \(d\asymp TL\), so its normalized spacing cost is \(O(N/T)=o(1)\). That is a valid linear/quadratic source bound on the stated grid.

It does not directly control the fourth-order ratio points. Flattening each two-prime product to length \(M_{prod}\) invokes the recorded product-block Gram bound \(1+16\pi M_{prod}/T=1+16\pi H\), which loses the growing factor \(H\) on supercritical product cells. At the natural cutoff,
\[
N/T\sim e^{-\sqrt L}/(2\pi)\to0,\qquad
N^2/T\sim e^{L-2\sqrt L}/(2\pi)\to\infty.
\]
If the whole array is instead flattened by distinct ratios \(A/B\) with \(A,B\le N^2\), the denominator-only spacing guarantee for distinct reduced rational ratios is no better than order \(N^{-4}\); after log-frequency scaling and \(d\asymp TL\) row samples, the generic large-sieve spacing term can reach order \(N^4/T\). This is a worst-case guarantee for all integer ratios, not a claim that the ordinary-prime product subset attains that spacing. These are losses of generic bounds, not lower bounds on the source sum. A continuous mean-value theorem for a length-X Dirichlet polynomial similarly gives \((1+X/T)\sum|a_n|^2\) after normalization; taking \(X=N^2\) leaves \(N^2/T\), and it still needs a source-matched single-polynomial factorization.

The checked repository has linear and quadratic large-sieve/operator estimates, a product-block Gram estimate, and exact finite tensorization of the cumulant. It has no proved analytic multilinear mean-value theorem for the physical section-dependent 26-term coefficients. The exact tensor identities are finite rearrangements, not a bound for the tensor's trace/projective norm or its positive part.

| Candidate | Hypothesis / matching object | Type of control | Normalization result |
|---|---|---|---|
| Evans | Restricted E2 indicator correlations; almost all additive shifts; global major-arc centered L2 | Correlation asymptotic / squared mean, not WP84 weighted positive part | Direct insertion pays \(H=M_{prod}/T\), giving \(T^{s-1}(\log L)^2/L^{4+\eta}\); fails |
| Guth–Maynard | One dyadic polynomial, \(|b_n|\le1\), 1-separated heights, large-value count | Cardinality of large values, neither signed sum nor second/fourth moment of sections | No source reduction or value of the positive-part sum; no strict budget |
| Montgomery–Vaughan | Separated one-dimensional frequencies and coefficient square mass | Squared mean / operator norm for the matched linear or Gram form | One-prime \(N/T=o(1)\); product \(H\) diverges; flattened ratio spacing may cost \(N^4/T\) |
| Repository endpoint tensor | Exact finite row measures per partition, preserving Möbius signs | Algebraic identity; weighted tensors can be complex | No analytic norm gain; endpoint correction remains open |

No candidate as stated provides the required source-weighted positive-part estimate.

## 4. Hostile no-go checks

### Second mass does not imply a fourth bound

For integer \(k\ge2\), take a matrix of dimension \(k^8\) with one diagonal entry \(k^3\) and all other entries zero. Exactly,
\[
\tau(Q_k^2)=k^{-2}\le1,\qquad \tau(Q_k^4)=k^4\to\infty,
\quad \|Q_k\|_{op}=k^3.
\]
Thus second-mass control alone cannot imply a fourth-moment or connected aggregate bound. The earlier proper-power absorption adds its separate source-valid operator-norm and finite-grid transfer hypotheses and is retained; it does not provide the missing ordinary-prime estimate.

### Endpoint correction versus absolute prime tuple mass

The exact endpoint sensitivity is \(|\kappa_I-\kappa_J|\le75\|\mu_I-\mu_J\|_1\). One endpoint deletion gives \(150/m\); trimming the Decision-B endpoints gives the recorded \(300M_{end}/d=O(e^{-\sqrt L/2})\) per tuple. But the ordinary-prime absolute coefficient mass is only crudely \(S^4\), with \(S=\sum_{p\le N}|c_p|=O(\sqrt N/L)\), hence \(S^4=O(N^2/L^4)\). Multiplying the trim correction by this absolute mass gives the failed majorant
\[
O\!\left(\frac{N^2e^{-\sqrt L/2}}{L^4}\right)
=O\!\left(\frac{T^2e^{-5\sqrt L/2}}{L^4}\right),
\]
which diverges. A single-row correction times the same crude mass is \(O(N^2/(T L^5))=O(T e^{-2\sqrt L}/L^5)\), also divergent. These are upper-bound failures, not positive lower bounds. No source-specific cancellation estimate offsets them.

### Circular moment transfer check

The proper-power result proves its own \(\tau(Q^4)\) small using the operator bound and \(\tau(Q^2)\), and its Schatten-root perturbation is recorded without assuming a target fourth moment. That valid isolated result cannot be turned into an additive fourth-trace error for \(P=A+Q\) from a small root-norm gap alone: converting \(|\tau(P^4)^{1/4}-\tau(A^4)^{1/4}|\) into \(|\tau(P^4)-\tau(A^4)|\) multiplies by a cubic norm factor, which needs a bounded fourth norm. Assuming that bound for the ordinary-prime target would be circular. This audit does not make that assumption.

## 5. Smallest new theorem required

The cleanest sufficient new analytic input, avoiding a stronger nonpositivity claim, is the source-specific joint-selection estimate
\[
\limsup_{T\to\infty}\frac1{|\mathcal C_T|}\sum_{I\in\mathcal C_T}
\left(\Re\sum_{\substack{\epsilon\text{ balanced},\ p_0,\ldots,p_3\le N\\
A(\epsilon,\mathbf p)\ne B(\epsilon,\mathbf p)}}
e^{iT\log(A/B)}\prod_{j=0}^3c_{p_j}\,
\mathcal K^{phys}_{T,I}(\epsilon,\mathbf p)\right)_+
< (1/4-\epsilon)\Delta_{max}
\]
for one fixed \(0<\epsilon<1/4\), with \(\mathcal K^{phys}_{T,I}\) exactly the filtered physical 26-term cumulant, all six orientations, selected-section Fourier carrier and finite root corrections from the source. The sum uses all ordinary primes through the actual cutoff, exact pair contractions removed, and all off-diagonal near products and aliases retained. For the concrete \(\epsilon=1/8\) endpoint route the right side is exactly \(3675673694911/1186000000000000\). This theorem must be uniform along the admissible source sequence and use the actual section measure; it is a positive-part bound, not a signed average.

An equivalent direct common-section theorem could prove \(\Re C^{ord}_{T,I_T}<\Delta_{max}+o(1)\) for one section that also meets all endpoint, boundary, row-deletion, normalization, and consumer conditions. Neither theorem follows from currently matched published inputs. No finite computation can replace it, and no actual ordinary-prime source counterexample is known from the evidence reviewed.

## 6. Preservation and reproducibility

The predecessor's positive physical atom is a proper-prime-power tuple and its one-base \(O_R(L^{-4})\) family remains controlled; it is not reclassified as an ordinary-prime aggregate counterexample. The source/geometric discrepancy remains visible and blocks transfer of the public overlap sign. The existing proper-power Schatten absorption and endpoint/tensor identities are not weakened by this audit.

Exact arithmetic checks are in `src/wp84_r400_theorem_feasibility.py` and `tests/test_wp84_r400_theorem_feasibility.py`. The source inventory and new-artifact SHA-256 manifest are `evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SOURCE_HASHES.json` and `evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.json`; the manifest sidecar excludes its own hash. Test runs in normal Python, `-O`, and `-OO`, plus predecessor-manifest replay, are stored in the evidence directory. Passing these checks verifies arithmetic and evidence integrity only.

Primary sources checked:

- Natalie Evans, [*Correlations of Almost Primes*](https://arxiv.org/abs/2102.12297), especially Theorem 1.1 and Sections 3, 5–6.
- Larry Guth and James Maynard, [*New Large Value Estimates for Dirichlet Polynomials*](https://annals.math.princeton.edu/2026/203-2/p06), Theorem 1.1 in the accepted manuscript.
- H. L. Montgomery and R. C. Vaughan, [*The Large Sieve*](https://doi.org/10.1112/S0025579300004708), Mathematika 20 (1973), 119–134.

The conditional 68.820273% route, strict greater-than-79% theorem, and Riemann Hypothesis remain open.
