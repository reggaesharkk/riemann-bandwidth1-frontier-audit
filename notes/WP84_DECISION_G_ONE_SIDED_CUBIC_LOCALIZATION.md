# WP84 Decision G — one-sided cubic localization

**Decision G2.** The interaction between the two deleted endpoint blocks is (o(d)) by the inherited local source square-mass estimate and their separation. The mixed-boundary term in the exact self-normalized trace identity is (o(1)) after averaging with Decision B's actual uniform endpoint-pair weights. Consequently, the full deleted-block obstruction reduces to the sum of two one-sided centered cubic quantities. No bound for those quantities is proved, so full cubic deletion stability remains open.

Start state verified: branch `codex/c5-c6-attack-20261006`, HEAD `3e7672d63ef611917bbb51c0b6c4a4eb3441e803`; only pre-existing untracked `notebooklm_packet/`, preserved. Decisions B–F and their certificates were read before preparing this audit. No push or merge was performed.

## Source and endpoint geometry

Use
\[
X=T/(2\pi),\quad L=\log X,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,
\quad d=\lfloor TL/(2\pi)\rfloor,
\quad M=\lceil de^{-\sqrt L/2}\rceil.
\]
For (0\le u,v\le M), let
\[
I(u,v)=[b+u,b+d-1-v],\quad
Q_L=[b,b+u-1],\quad Q_R=[b+d-v,b+d-1],\quad r=u+v,
\]
with empty endpoint blocks omitted. Thus (d'=d-r\ge d-2M\sim d). The actual prime pool is every (n=p^q\le N) ((q\ge1)); with
\[
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
z_n=c_ne^{iT\log n},\quad \alpha_n=\log n/L,
\quad w_n(k)=z_ne^{2\pi i k\alpha_n},
\]
the source fields are (A_k=\sum_n\Im w_n(k)) and
\(\beta_k=\sum_n2(1-\alpha_n)\Re w_n(k)). The finite matrix is
\[
H=s_0I+\operatorname{diag}(\beta)+[\operatorname{diag}(A),J],
\quad J_{ij}=1/(\pi(j-i))\ (i\ne j),\quad J_{ii}=0.
\]
All powers, carrier phases, and the natural cutoff remain present. Since \(\log N\le L-\sqrt L\), the prime shifts satisfy \(0<\alpha_n\le1-1/\sqrt L\); the earlier partial-translation/no-wrap identities remain fixed-cutoff identities and are not being used as a uniform estimate for these endpoint cubic sums. (R=6000) enters the direct first-strike endpoint-consumer admissibility gate, not as a truncation of this prime matrix. No source-masked determinant compatibility is inferred.

Decisions B/D2 use the uniform measure on the exact pair square 
\(\mathcal W_T=\{0,\dots,M\}^2\). They give
\[
\mathbb E_{u,v} E(I(u,v))\le C_B\log d,
\qquad E(I)=\|P_IHQ_I\|_{HS}^2=\|P_IVQ_I\|_{HS}^2,
\]
and a consumer-admissible subset of pair weight (gamma_T\ge1/4) for the direct first-strike consumer. The local large sieve gives, uniformly on each endpoint interval of length at most (M),
\[
\sum A_k^2\le C_A(M+NL),\qquad
\sum \beta_k^2\le 4C_A(M+NL),
\]
with all prime powers retained. The fixed constants (C_A,C_B) denote the inherited constants from those estimates.

## Separated deleted blocks

In the (Q_L,Q_R) ordering write
\[
D=QHQ=\begin{pmatrix}D_L&C\\C^*&D_R\end{pmatrix},
\qquad C_{ij}=\frac{A_i-A_j}{\pi(j-i)},\quad i\in Q_L,\ j\in Q_R.
\]
The nearest endpoint distance is exactly
\[
\min_{i\in Q_L,j\in Q_R}(j-i)=d-u-v+1\ge d-2M+1.
\]
Block multiplication gives
\[
\boxed{\operatorname{Tr}(D^3)=\operatorname{Tr}(D_L^3)+\operatorname{Tr}(D_R^3)
+3\operatorname{Tr}(D_LCC^*)+3\operatorname{Tr}(D_RC^*C).}
\]
The coefficient 3 comes from the three cyclic placements of each two-crossing block path. It does not say that the two endpoint blocks are independent.

Using ((x-y)^2\le2x^2+2y^2), the source endpoint square-mass bounds, and the exact distance,
\[
\begin{aligned}
\|C\|_{HS}^2
&\le\frac{2}{\pi^2(d-2M+1)^2}
\left(v\sum_{i\in Q_L}A_i^2+u\sum_{j\in Q_R}A_j^2\right)\\
&\le\frac{4C_A M(M+NL)}{\pi^2(d-2M+1)^2}.
\end{aligned}
\]
The compressed operator norms satisfy 
\(\|D_L\|_{op},\|D_R\|_{op}\le K_T:=|s_0|+4S\), where
\(S=\sum_{p^q\le N}|c_{p^q}|=O(\sqrt N/L)\). Therefore
\[
\frac{|\operatorname{Tr}(D^3)-\operatorname{Tr}(D_L^3)-\operatorname{Tr}(D_R^3)|}{d}
\le\frac{24C_AK_TM(M+NL)}{\pi^2d(d-2M+1)^2}.
\]
Equivalently this is (O(K_TM(M+NL)/d^3)), since (M=o(d)). At the original cutoff, (NL/M=O(e^{-\sqrt L/2})\to0), (M/d=e^{-\sqrt L/2}+o(1)), and (d\asymp TL). Thus the bound is
\[
O\!\left(\frac{e^{-\sqrt L}}{TL}
+\frac{e^{-3\sqrt L/2}}{\sqrt T\,L^2}\right)=o(1).
\]
The cross block is generally nonzero. The exact rational hostile replay uses separated endpoint indices with (C\ne0) and a nonzero cubic interaction. The result is a decaying interaction bound, not exact factorization.

## Unknown finite-source normalization

Define only
\[
m_T=\operatorname{Tr}(H^3)/d;
\]
it is an unknown finite-source quantity. No value (2), uniform bound, or sign is assumed. With (A=PHP), (B=PHQ), (D=QHQ), and
\[
G(I)=3\operatorname{Tr}_P(ABB^*)+3\operatorname{Tr}_Q(DB^*B),
\]
the exact full-trace block identity is
\(\operatorname{Tr}(H^3)=\operatorname{Tr}(A^3)+\operatorname{Tr}(D^3)+G(I)\).
For (F(I)=\operatorname{Tr}(D^3)-r\tau_{d'}(A^3)), direct substitution, with (d'=d-r), yields
\[
\boxed{\frac{F(I)}d=\frac{\operatorname{Tr}(D^3)-r m_T}{d'}
+\frac{rG(I)}{dd'}.}
\]
The sign of the last term is positive. The correction by (r m_T) is essential and has not been dropped.

Let (E(I)=\|B\|_{HS}^2\). Since 
\(\|A\|_{op},\|D\|_{op}\le K_T\), 
\(|G(I)|\le6K_TE(I)\). Averaging in the exact uniform Decision-B pair measure gives
\[
\mathbb E_{u,v}\left|\frac{rG(I)}{dd'}\right|
\le \frac{12K_TC_BM\log d}{d(d-2M)}.
\]
At the natural cutoff this is
\[
O\!\left(\frac{e^{-\sqrt L/2}}T
+\frac{e^{-\sqrt L}}{\sqrt T\,L}\right)=o(1).
\]
This is an average bound only; no uniform-in-((u,v)) boundary estimate is asserted.

## One-sided centered cubic reduction

Set
\[
Z_L(u)=\operatorname{Tr}(D_L(u)^3)-u m_T,\qquad
Z_R(v)=\operatorname{Tr}(D_R(v)^3)-v m_T.
\]
Let (J_{sep}=3\operatorname{Tr}(D_LCC^*)+3\operatorname{Tr}(D_RC^*C)). Then
\[
\operatorname{Tr}(D^3)-r m_T=Z_L(u)+Z_R(v)+J_{sep}.
\]
Combining the exact identities above and (d'\ge d-2M) proves
\[
\boxed{\mathbb E_{u,v}\frac{|F(I(u,v))|}{d}
\le\frac{\mathbb E_u|Z_L(u)|+\mathbb E_v|Z_R(v)|}{d-2M}
+\varepsilon_T,}
\]
where the endpoint averages on the right are uniform on their actual (M+1) point windows, and one valid explicit remainder is
\[
\boxed{\varepsilon_T=
\frac{24C_AK_TM(M+NL)}{\pi^2(d-2M)(d-2M+1)^2}
+\frac{12K_TC_BM\log d}{d(d-2M)}=o(1).}
\]
Thus the sufficient remaining estimate is
\[
\frac{\mathbb E_u|Z_L(u)|+\mathbb E_v|Z_R(v)|}{d-2M}\longrightarrow0.
\]
This is not necessary: (Z_L) and (Z_R) could cancel in the pair sum. No such cancellation is presumed or proved.

## Exact one-row increments and the first arithmetic debt

For an old endpoint block (D_{old}), append the next row (k) as
\[
D_{new}=\begin{pmatrix}D_{old}&h\\h^*&a\end{pmatrix},
\qquad a=s_0+\beta_k,quad
h_j=H_{j,k}=\frac{A_j-A_k}{\pi(k-j)}.
\]
Block multiplication gives the exact increment
\[
\boxed{\operatorname{Tr}(D_{new}^3)-\operatorname{Tr}(D_{old}^3)
=a^3+3a\|h\|^2+3h^*D_{old}h.}
\]
For the left side (k=b+t) is added after (Q_L(t)=[b,b+t-1]); for the right side (k=b+d-1-t) is prepended to the rows already added from the right. Reordering the finite coordinates to the displayed block form does not change the trace. In both cases the entry orientation is (h_j=(A_j-A_k)/(\pi(k-j))), agreeing with (W_{j,k}).

The components are
\[
a^3=s_0^3+3s_0^2\beta_k+3s_0\beta_k^2+\beta_k^3,
\quad \|h\|^2=\frac1{\pi^2}\sum_{j\in Q_{old}}\frac{(A_j-A_k)^2}{(k-j)^2},
\]
\[
h^*D_{old}h=s_0\|h\|^2+\sum_j\beta_j|h_j|^2+\sum_{j,\ell}\overline h_jW_{j\ell}h_\ell.
\]
These are respectively a diagonal row score, a quadratic row coupling, and a signed old-block quadratic form. In source fields,
\[
a_k\|h\|^2=\frac{s_0}{\pi^2}\sum_{j\in Q_{old}}\frac{(A_j-A_k)^2}{(k-j)^2}
+\frac1{\pi^2}\sum_{j\in Q_{old}}\frac{\beta_k(A_j-A_k)^2}{(k-j)^2},
\]
\[
h^*D_{old}h=s_0\|h\|^2+
\sum_{j\in Q_{old}}\frac{\beta_j(A_j-A_k)^2}{\pi^2(k-j)^2}
+\frac1{\pi^3}\sum_{\substack{j,\ell\in Q_{old}\\j\ne\ell}}
\frac{(A_j-A_k)(A_j-A_\ell)(A_\ell-A_k)}
{(k-j)(\ell-j)(k-\ell)}.
\]
Using (u_{n,\sigma}(x)=c_n e^{i\sigma(T\log n+2\pi x\alpha_n)}),
\[
\beta_x=\sum_{n=p^q\le N}(1-\alpha_n)\sum_{\sigma=\pm1}u_{n,\sigma}(x),\qquad
A_x=\frac1{2i}\sum_{n=p^q\le N}\sum_{\sigma=\pm1}\sigma u_{n,\sigma}(x),
\]
and write \(\Delta_{n,\sigma}(x,y)=u_{n,\sigma}(x)-u_{n,\sigma}(y)\). The three-frequency products are explicitly
\[
\beta_k^3=\sum_{n_0,n_1,n_2}\prod_{t=0}^2(1-\alpha_{n_t})
\sum_{\sigma_0,\sigma_1,\sigma_2}u_{n_0,\sigma_0}(k)u_{n_1,\sigma_1}(k)u_{n_2,\sigma_2}(k),
\]
\[
\beta_x(A_y-A_z)^2=-\frac14\sum_{n_0,n_1,n_2}(1-\alpha_{n_0})
\sum_{\sigma_0,\sigma_1,\sigma_2}\sigma_1\sigma_2 u_{n_0,\sigma_0}(x)
\Delta_{n_1,\sigma_1}(y,z)\Delta_{n_2,\sigma_2}(y,z),
\]
\[
(A_j-A_k)(A_j-A_\ell)(A_\ell-A_k)
=\frac1{(2i)^3}\sum_{n_0,n_1,n_2}
\sum_{\sigma_0,\sigma_1,\sigma_2}\sigma_0\sigma_1\sigma_2
\Delta_{n_0,\sigma_0}(j,k)\Delta_{n_1,\sigma_1}(j,\ell)
\Delta_{n_2,\sigma_2}(\ell,k),
\]
where every (n_t) ranges over the complete (\mathcal P(N)). These are finite signed triple sums; their carrier factor is (e^{iT\sum_{t=0}^2\sigma_t\log n_t}), while the sampled phase keeps the actual row/column index belonging to each factor. The scalar (s_0\|h\|^2) pieces have two prime frequencies. No factor is deleted or replaced by a continuum variable.

Writing (\delta_k=\operatorname{Tr}(D_{new}^3)-\operatorname{Tr}(D_{old}^3)), exact telescoping gives
\[
Z_L(u)=\sum_{t=0}^{u-1}(\delta_{b+t}-m_T),\qquad
Z_R(v)=\sum_{t=0}^{v-1}(\delta_{b+d-1-t}-m_T).
\]
The first genuinely three-frequency term is the diagonal score (\beta_k^3):
\[
\beta_k^3=\sum_{n_0,n_1,n_2\in\mathcal P(N)}
\prod_{j=0}^2(1-\alpha_{n_j})c_{n_j}
\sum_{\sigma_0,\sigma_1,\sigma_2=\pm1}
e^{iT\sum_j\sigma_j\log n_j}
e^{2\pi i k\sum_j\sigma_j\alpha_{n_j}}.
\]
The term (a\|h\|^2) also has (\beta_k A^2) interactions; (h^*D_{old}h) includes signed (\beta A^2) and (A^3) correlations. Existing local S2 and operator estimates yield at best a cumulative absolute majorant (O(K_T(M+NL))), hence (O(K_TM/d)), which does not tend to zero. They do not control centered sums because (m_T) itself is unknown. No deterministic source-matched three-frequency estimate is established.

For each sign triple the exact carrier resonance condition is
\[
\Omega=\sum_{j=0}^2\sigma_j\log n_j=0
\quad\Longleftrightarrow\quad
\prod_{\sigma_j=+1}n_j=\prod_{\sigma_j=-1}n_j.
\]
With three prime powers, a zero carrier can only be a two-factor versus one-factor relation (or its reversal); unique factorization forces the two factors to be powers of the same prime and their exponents to add to the singleton exponent, as (2\cdot4=8). The valid triple (2,3,5) instead has ratio (6/5) and nonzero carrier (\log(6/5)). It is not deleted as a “near alias.” In expanded (h)-products, each difference assigns a frequency to one of two endpoint indices; the resulting finite phase forms are endpoint-dependent. A scalar (\Omega/L\in\mathbb Z) test alone does not collapse those terms. Exact resonances may be separated from nonzero frequencies, but all near-alias and nonresonant sums remain until estimated. The source cutoff, all (p^v\), and the unknown (m_T) are retained.

## Same-section selection

If the one-sided sufficient estimate above is proved, then the derived pair-weight average (a_T=\mathbb E|F|/d\) is (o(1)). At threshold (8C_B\log d), the crossing-energy-bad pairs have weight at most (1/8). At threshold (sqrt{a_T}), the cubic-residual-bad pairs have weight at most (sqrt{a_T}). D2's admissible pair set has weight at least (1/4), so its intersection with both good sets has positive weight for large (T). This uses the same exact uniform pair measure, no independence assumption, and only the direct first-strike consumer. It does not transfer to the hidden-prime source-mask determinant consumer.

The hostile replay includes an endpoint configuration where a cubic-good pair can lie entirely outside the admissible set; this falsifies selection without a joint estimate. It also checks the valid Markov intersection calculation and that signed mean cancellation need not control absolute fluctuations.

## Decision and open boundary

**G2 — one-sided localization proved; arithmetic remains open.** The separated endpoint-block interaction and averaged mixed-boundary self-normalization are rigorously negligible at the original cutoff. The full residual is thereby reduced to the one-sided centered quantities in the boxed inequality. Local square mass and operator bounds alone do not close them. No source-valid counterexample or deterministic signed saving has been proved.

The exact first open target is the one-sided estimate
\[
\boxed{\frac{\mathbb E_u|\operatorname{Tr}(D_L(u)^3)-u m_T|
+\mathbb E_v|\operatorname{Tr}(D_R(v)^3)-v m_T|}{d-2M}=o(1),}
\]
or an equally strong pairwise signed-cancellation estimate compatible with the D2 admissible set. This is a genuine three-frequency prime-power problem, beginning with (\beta_k^3); no random-phase, Gaussian, independent-phase, uniform sixth-moment, or model moment assumption is used.

The (m_3=2) claim, conditioned energy (<0.105), signed fifth/sixth gate, prime-to-Weil identification, zero-side transfer, determinant compatibility, and strict (>79\%) theorem remain **OPEN**.

## Reproduction

```powershell
python src/wp84_decision_g_one_sided_cubic_localization.py
python src/wp84_decision_g_one_sided_cubic_localization_replay.py
```

The producer writes the JSON certificate; the independent replay uses only exact rational arithmetic and does not import the producer. These checks validate finite identities and hostile logical mutations, not the unresolved asymptotic prime estimate.
