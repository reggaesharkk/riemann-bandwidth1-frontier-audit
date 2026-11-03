# WP84 — Physical cumulant endpoint difference and tensor lift

Base commit: `0d3bc919451df298ef2a945569d8c3b1eb65192f`

Audit branch: `codex/wp84-physical-cumulant-tensor-lift-20261103`

This is an additive local audit. It preserves the preceding endpoint audit,
its certificates, source files, proper-power result, positive physical atom,
and physical/geometric kernel discrepancy. Nothing was pushed, merged, or
published.

| Decision | Result |
|---|---|
| `CUMULANT_ENDPOINT_IDENTITY` | **PROVED** |
| `TENSOR_AVERAGING` | **EXACT** |
| `SOURCE_WEIGHTED_CORRECTION` | **OPEN** |
| `ORDINARY_CONNECTED_RECORD_BOUND` | **OPEN** |
| `R400_CONSUMER` | **CONDITIONAL** |

## 1. The 26-term variation identity

For a finite row interval `I`, let
\[
\mu_I(k)=|I|^{-1}\mathbf 1_{k\in I},\qquad
D_I(x)=\sum_k\mu_I(k)e^{2\pi i kx}.
\]
For each anchored, ordered partition `pi` of the four labels, write
\[
\kappa_I(v)=\sum_{\pi}\mu(\pi)\prod_{B\in\pi}D_I(v_B),
\quad v_B=\sum_{j\in B}v_j,
\quad \mu(\pi)=(-1)^{|\pi|-1}.
\]
Anchoring the block containing label 0 and ordering the other blocks gives
exactly 26 products: 1, 7, 12, and 6 terms with respectively 1, 2, 3, and
4 block factors. Their total block-factor count is
\[
1+7\cdot2+12\cdot3+6\cdot4=75.
\]
The machine ledger compares every ordered term and coefficient against the
committed source ledger.

Since (|D_I(x)|\le1), telescope each product in its ordered block list:
\[
\left|\prod_{B\in\pi}D_I(v_B)-\prod_{B\in\pi}D_J(v_B)\right|
\le |\pi|\,\|\mu_I-\mu_J\|_1,
\]
because
\[
|D_I(x)-D_J(x)|\le\sum_k|\mu_I(k)-\mu_J(k)|.
\]
Summing the 26 absolute Möbius coefficients yields the uniform inequality
\[
\boxed{|\kappa_I(v)-\kappa_J(v)|\le75\,\|\mu_I-\mu_J\|_1.}
\]
This holds for every real four-vector `v`, including zero detuning and exact aliases.

If both sections lie in one `d`-row grid and each omits at most `r` rows,
then
\[
\|\mu_I-\mu_d\|_1=2(d-|I|)/d\le2r/d,
\quad \|\mu_J-\mu_d\|_1\le2r/d,
\]
so the triangle inequality gives
\[
|\kappa_I(v)-\kappa_J(v)|\le300r/d.
\]
The constant is a safe bound and need not be sharp for overlapping sections.
For one endpoint deletion from an (m)-row interval, the exact measure
distance is `2/m`, hence the sharper one-step bound is `150/m`.

For the actual Decision-B candidates, `r=u+v<=2*M_end` rows are removed
relative to the untrimmed `d`-row section. The direct one-section distance
gives the sharper `150*r/d` cumulant bound, hence
`M_end=ceil(d exp(-sqrt(L)/2))`. Thus
\[
|\kappa_{I_{uv}}-\kappa_{[b,b+d-1]}|
\le300M_{end}/d=O(e^{-\sqrt L/2}),
\]
and any two candidates differ by at most `600*M_end/d` via the common
untrimmed reference. This is a per-frequency/per-tuple kernel estimate.

## 2. Exact single-endpoint formulas term by term

Let `I=[a,a+m-1]`, and let `I^-=[a+1,a+m-1]` or
`I^+=[a,a+m-2]`. If `q` is the deleted endpoint, then for either side
\[
D_{I'}(x)-D_I(x)
=\frac{D_{I'}(x)-e^{2\pi i qx}}m.
\tag{1}
\]
This is an equality of finite sums. Apply (1) to each block factor in each
ordered partition. With the partition's original coefficient `mu(pi)`,
the exact change is
\[
\mu(\pi)\sum_{B_j\in\pi}
\big(D_{I'}(v_{B_j})-D_I(v_{B_j})\big)
\prod_{i<j}D_{I'}(v_{B_i})
\prod_{i>j}D_I(v_{B_i}).
\tag{2}
\]
Equation (2) is checked separately for both sides and all 26 terms in exact
Gaussian-rational arithmetic.

For a source tuple `sigma=(epsilon,p_0,p_1,p_2,p_3)`, retain
\[
c_\sigma=\prod_j\frac{-\log p_j}{a_\phi(T)L\sqrt{p_j}},\quad
Y=\sum_j\epsilon_j\log p_j=\log(A/B),\quad
v_j=\epsilon_j\log(p_j)/L,
\]
all 16 source sign words, the six balanced words in the unresolved balanced
sector, the height carrier `exp(i*T*Y)`, and the source-filtered R400
coefficient. In local-row coordinates the start carrier is
`exp(2*pi*i*a*Y/L)`; deleting the left endpoint multiplies it by
`exp(2*pi*i*Y/L)`, while deleting the right endpoint leaves it fixed. If
absolute row indices are used in `D_I`, that start phase is already inside
the Fourier characters and must not be multiplied a second time. The
coefficient `c_sigma`, orientation, and `exp(i*T*Y)` remain attached to
every term of (2).

For the finite compressed trace, a closed R400 path `r` has prefixes
\(q_0=0, q_j=\sum_{t\le j}r_t\). Its valid roots for section
`I=[a,a+m-1]` are exactly
\[
K_I(r)=[a-\min_jq_j,\ a+m-1-\max_jq_j].
\]
For a valid nonempty root interval `[s,t]`, a left deletion changes its
normalized root sum by exactly
\[
\frac1{m(m-1)}\sum_{k=s+1}^{t}e^{2\pi ikY/L}
-\frac1m e^{2\pi isY/L};
\tag{3L}
\]
a right deletion changes it by
\[
\frac1{m(m-1)}\sum_{k=s}^{t-1}e^{2\pi ikY/L}
-\frac1m e^{2\pi itY/L}.
\tag{3R}
\]
The root measures have per-path `l1` change at most `2/m`. The closed
four-lag span is at most `2R=800`: a difference of prefixes is a consecutive
partial sum and the negative of its complement, so it is at most
`min(t,4-t)*R<=2R`. Equality is attained by `(400,400,-400,-400)`, so
the exact count is `m-ell` when `m>ell`. Equations (3L) and (3R) keep
the actual path interval and endpoint; they are not a uniform estimate after
summing the source-weighted paths.

## 3. Tensorized section average

Let `S` be any nonempty family of candidate sections with exact probabilities
`rho_I >= 0` and `sum_I rho_I = 1`. For an ordered partition `pi` with
`q = |pi|`, define the joint row measure
\[
W_\pi((k_B)_{B\in\pi})
=\mathbb E_{I\sim\rho}\left[
|I|^{-q}\prod_{B\in\pi}\mathbf1_{\{k_B\in I\}}
\right].
\tag{4}
\]
It is nonnegative and normalized for every partition:
\[
\sum_{(k_B)}W_\pi((k_B))
=\mathbb E_I\left[|I|^{-q}\prod_{B\in\pi}\sum_{k_B\in I}1\right]=1.
\]
Expanding the finite row means and interchanging finite sums gives the exact
identity
\[
\mathbb E_I\kappa_I(v)
=\sum_\pi\mu(\pi)\sum_{(k_B)}W_\pi((k_B))
\exp\!\left(2\pi i\sum_{B\in\pi}k_Bv_B\right).
\tag{5}
\]
All Möbius signs and all block labels remain. The rows (k_B) are jointly
coupled by the shared section choice; (5) does not replace the average of a
product by a product of averages.

For the physical source, do not factor a finite-section R400 coefficient
or root mask out of (4). Let (a_{\sigma,\pi,\lambda}(I,v)) denote the
exact source coefficient for one labeled tuple \(\sigma\), ordered
partition \(\pi\), and finite source path/root label \(\lambda\), outside
the \(q=|\pi|\) empirical row factors. It retains the original coefficient
product, height carrier, orientation, filtered Fourier coefficients,
section dependence, aliases, and whichever path/root normalization and
indicator the exact finite expansion assigns to that summand. Its exact
weighted tensor is
\[
\widetilde W_{\sigma,\pi,\lambda}((k_B))
=\mathbb E_I\left[
\rho_I a_{\sigma,\pi,\lambda}(I,v)|I|^{-q}
\prod_{B\in\pi}\mathbf1_{\{k_B\in I\}}
\right].
\tag{6}
\]
Then that labeled contribution is exactly
\[
\mu(\pi)\sum_{(k_B)}\widetilde W_{\sigma,\pi,\lambda}((k_B))
\exp\!\left(2\pi i\sum_B k_Bv_B\right),
\]
with any additional path-row Fourier character still summed with its source
path label. If a particular summand contains an explicit normalized root
sum, its additional exact tensor coordinate is
\[
\mathbb E_I\left[\rho_I a_{\sigma,\pi,\lambda}(I,v)|I|^{-q-1}
\prod_B\mathbf1_{\{k_B\in I\}}
\mathbf1_{\{k\in K_I(\lambda)\}}\right];
\]
this extra coordinate is included only for the source summands that actually
have that root average. This is finite-sum Fubini, not a claim that one
common root mask multiplies every partition. Absolute row indices \(k_B\)
already carry the section-start phase. The weighted tensor has total mass
equal to the source average of \(a_{\sigma,\pi,\lambda}(I,v)\), not one,
and is generally complex. Where the parent's full-lattice reduction has
common \(\Omega_{4,400}(v)\), it is the special case independent of the
section, partition, and path; the separate finite-compression correction
remains explicit. The index \(\lambda\) must enumerate the actual finite
source expansion before this rearrangement is used; the formula does not
assert a new common factorization. No such independence is assumed for the
actual section-weighted expansion.

The bare `W_pi` is a probability measure, so its Fourier transform is a
positive-definite function on its block-frequency variables. This is the
precise termwise PSD fact. The cumulant is a signed sum with both Möbius
signs, and the physical overlap/carrier/source-weighted measure `W_tilde` is
generally complex and has no unit-mass or PSD property.
Thus (5) yields no sign for the physical aggregate. The endpoint difference
(1) is an exact boundary exponential, but no source-matched endpoint
commutator identity turning the full filtered cumulant into a nonpositive
quadratic form was found.

## 4. What the endpoint polynomials do and do not give

After expanding (1), each fixed source tuple contributes finite exponentials
in block sums. Summing over the original primes therefore gives a finite
multilinear Dirichlet polynomial supported on the actual source tuples
`p_j<=N`; regrouping it by (A=pq), (B=rs) retains all labeled splits,
including (A\ne B), near products, and aliases. This establishes the
formal source support, not the required norm estimate.

The coefficients of this new family are precisely the grouped
\(\widetilde W_{\sigma,\pi,\lambda}\) values: they include the section/path
filtered coefficients, row products from the other blocks, endpoint/section
selection, and path-root indicators. The existing one-prime endpoint-score
\(\ell^2\) hypotheses do not
bound their grouped ℓ2 mass. Montgomery--Vaughan/large-sieve inequalities
allow arbitrary coefficients, but they still require a usable coefficient
square mass or a separation/correlation estimate. Neither is provided for
these (A,B) coefficients; the product-frequency aliases and close
noncoincidences remain. Treating the source terms by absolute values is
already too large: the ordinary-prime ℓ1 mass is only bounded crudely by
\(O(\sqrt N/L)\), so its fourth power is (O(N^2/L^4)). Multiplying by
the per-tuple endpoint size (O(M_{end}/d)=O(e^{-\sqrt L/2})) still grows
like (T^2e^{-5\sqrt L/2}/L^4), not (o(1)). This is a failed majorant,
not a lower bound on the signed aggregate.

The exact diagnostics check zero detuning and the zero cumulant at
`v=(0,0,0,0)`, the near-product indices `10403` and `10379` (gap 24), unequal
product scales, different left/right endpoints, and the root interval for
`(2,-2,0,0)`. The near-alias row test uses exact `x=1/6000`: for
`0<=k<60`, `|2*pi*k*x|<11/175`, hence
`Re exp(2*pi*i*k*x)>=1-(11/175)^2/2>998/1000`. These are finite algebra
checks only. No additional search over
near-product tuples was run, and no numerical sample is used as asymptotic
prime evidence. The previous physical positive atom
`(p,p^2,p^3,p^2)`, its `O_R(L^-4)` one-base family, and the
physical/geometric kernel discrepancy remain unchanged.

## 5. Missing aggregate lemma and record quantifiers

Let `C_T(I)` be the complete source-matched ordinary-prime connected
contribution after the exact pair contractions, with all 26 terms, source
coefficients, balanced orientations, endpoint carrier, R400 filtered
coefficients, and finite root corrections retained. Let
\[
G_T(I)=\max(0,\Re C_T(I)),\qquad
\Delta_{max}=3675673694911/148250000000000.
\]
The endpoint/boundary argument guarantees density at least
`1/4-epsilon` for fixed `0<epsilon<1/4`. The joint-selection implication
is valid if
\[
\limsup_{T\to\infty}\mathbb E_{I\text{ uniform on }\mathcal W_T}G_T(I)
<(1/4-\epsilon)\Delta_{max}.
\tag{7}
\]
Then fewer than `1/4-epsilon` of the candidate pairs have
`Re C_T(I)>Delta_max`, leaving a common endpoint- and boundary-good section. The
record threshold at ε=1/8 is exactly
`3675673694911/1186000000000000`; as ε tends to zero the supremal
threshold tends to `3675673694911/593000000000000`. This is a **mean positive
part** condition: a bound on `Re E C_T(I)` alone is not enough (the exact
values `+1,-1` have mean zero and mean positive part `1/2`).

The smallest unresolved estimate remains (7), or a direct source-valid
selection of a common admissible (I_T) with
\(\Re C_T(I_T)\le\Delta_{max}+o(1)\). The tensor lift has no demonstrated
dimension-uniform bound for the actual Ω-weighted, 26-term, root-corrected
source sum, and the inherited record threshold cannot be claimed. Therefore
`SOURCE_WEIGHTED_CORRECTION=OPEN`,
`ORDINARY_CONNECTED_RECORD_BOUND=OPEN`, and
`R400_CONSUMER=CONDITIONAL`.

The proper-power absorption, 68.820273% route, strict greater-than-79%
theorem, and Riemann Hypothesis remain at their existing statuses; this
audit proves none of those gates.

## 6. Reproduction

Exact identities and ledgers: `src/wp84_r400_cumulant_endpoint_tensor.py`
and `evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json`.
Independent regressions: `tests/test_wp84_r400_cumulant_endpoint_tensor.py`.
The source-hash inventory, parent replay log, test logs, and SHA-256 manifest
are listed in `evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SHA256_MANIFEST.json`
and its `.sha256` sidecar. Normal, `-O`, and `-OO` runs check exact finite
identities; they do not verify (7). The initial test assertion-path failure
is preserved in the evidence directory.
