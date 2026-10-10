# WP84 Decision F — exact signed deleted-block cubic

**Decision F3.** The exact deleted-block cube has a simple decomposition; its scalar and degree-at-most-two terms are (o(d)) on the existing Decision-D2 endpoint windows. No cyclic, Hermitian, or unique-factorization identity removes its cubic prime-power terms. The remaining theorem is one same-window estimate for the *absolute value of the full normalized residual*, including the dimension-normalization correction. No source-valid counterexample is obtained.

This audit starts at branch `codex/c5-c6-attack-20261006`, commit `31f869c4d60581131ecb06f23892b38a2f27d8cd`. The only pre-existing untracked path was `notebooklm_packet/`; it is preserved. No push or merge was performed.

## Frozen source and same-section inputs

Let (X=T/(2pi)), (L=log X), (N=lfloor Xe^{-sqrt L}floor), and (d=lfloor TL/(2pi)floor). The full index set is (I_0=[b,b+d-1]). The source pool is

\[
\mathcal P(N)=\{p^v:p\text{ prime},\ v\ge1,\ p^v\le N\},\quad
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
z_n=c_ne^{iT\log n},\quad \alpha_n=\frac{\log n}{L},\quad
w_n(k)=z_ne^{2\pi i k\alpha_n}.
\]

Every prime power is retained. The source fields and matrix are

\[
A_k=\sum_{n\in\mathcal P(N)}\Im w_n(k),\qquad
\beta_k=\sum_{n\in\mathcal P(N)}2(1-\alpha_n)\Re w_n(k),
\]
\[
H=s_0I+\operatorname{diag}(\beta)+[\operatorname{diag}(A),J],\qquad
J_{ij}=\frac1{\pi(j-i)}\ (i\ne j),\quad J_{ii}=0.
\]

Use the same trimmed section from Decision B/D2:
\(I_{u,v}=[b+u,b+d-1-v]\), (0\le u,v\le M=\lceil d e^{-\sqrt L/2}\rceil\), and (Q=I-P_I\) restricted to deleted rows of (I_0\), with (r=u+v\le2M=o(d)\). Decision D2 supplies consumer-admissible endpoint-pair density \(\gamma_T\ge1/4\); Decision B supplies the uniform pair-average crossing estimate \(\mathbb E E(I_{u,v})\le C_B\log d\). Decision E's local prime-power large sieve supplies
\[
\sum_{i\in Q}\beta_i^2+\sum_{i\in Q}A_i^2=O(M+NL),\quad
\|W\|_{HS}^2=O(M+NL),\quad \|W\|_{op}\le4S,
\]
where \(S=\sum_{n\in\mathcal P(N)}|c_n|=O(\sqrt N/L)\). These are the inherited estimates and their stated scopes; no moment of order three is imported.

## Exact deleted-block identity

On the deleted coordinate space, set
\[
D=QHQ=s_0I_Q+B+W,\qquad B=\operatorname{diag}(\beta_i)_{i\in Q},\qquad
W_{ij}=\begin{cases}(A_i-A_j)/(\pi(j-i)),&i\ne j,\\0,&i=j.\end{cases}
\]
The matrix (W) is real symmetric. Thus \(\operatorname{Tr}W=0\). Since \(B^2\) is diagonal and (W) has zero diagonal, \(\operatorname{Tr}(B^2W)=0\). Expanding all eight terms in the noncommutative cube and using trace cyclicity gives

\[
\boxed{\operatorname{Tr}(D^3)=rs_0^3+3s_0^2\operatorname{Tr}B
+3s_0\{\operatorname{Tr}(B^2)+\operatorname{Tr}(W^2)\}
+C_1+C_2+C_3,}
\]
\[
C_1=\operatorname{Tr}(B^3)=\sum_{i\in Q}\beta_i^3,
\]
\[
C_2=3\operatorname{Tr}(BW^2)=\frac3{\pi^2}\sum_{i\in Q}\beta_i
\sum_{\substack{j\in Q\\j\ne i}}\frac{(A_i-A_j)^2}{(j-i)^2},
\]
\[
C_3=\operatorname{Tr}(W^3)=\frac1{\pi^3}
\sum_{\substack{i,j,k\in Q\\i,j,k\text{ pairwise distinct}}}
\frac{(A_i-A_j)(A_j-A_k)(A_k-A_i)}{(j-i)(k-j)(i-k)}.
\]
The ordered triples in (C_3) count every unordered triangle six times. A rational three-vertex test (A=(0,1,3)) gives \(\operatorname{Tr}(W_0^3)=-18\) for \(W_0=\pi W\). Therefore “the commutator is antisymmetric” or “cyclicity kills the cube” is false: (W) itself is symmetric Hermitian, and its cubic trace need not vanish. (C_2) and (C_3) have different powers \(\pi^{-2}\) and \(\pi^{-3}\); no universal coefficient cancellation is available.

## Degree at most two: controlled

On (Q), the local square-mass estimate gives
\[
|\operatorname{Tr}B|\le\sqrt r\,O(\sqrt{M+NL}),\qquad
\operatorname{Tr}(B^2)+\operatorname{Tr}(W^2)=O(M+NL).
\]
Since (r\le2M), (M/d\asymp e^{-\sqrt L/2}\), and (NL/M\to0),
\[
\frac1d\left|rs_0^3+3s_0^2\operatorname{Tr}B
+3s_0\{\operatorname{Tr}(B^2)+\operatorname{Tr}(W^2)\}\right|
=O\!\left(\frac Md+\frac{\sqrt{r(M+NL)}}d\right)=o(1).
\]
This uses the exact deleted endpoint intervals and the existing local large sieve, with all prime powers in its coefficient square mass.

For the cubic terms, only the majorant
\[
|C_1|+|C_2|+|C_3|\le O\bigl(S(M+NL)\bigr)
\]
follows from \(\|B\|_{op},\|W\|_{op}\le4S\) and the square-mass bounds. After normalization this is
\[
O(SM/d)=O\!\left(\frac{\sqrt T\,e^{-\sqrt L}}L\right),
\]
which does not tend to zero as an available bound. This is not a lower bound and does not falsify the prime-source theorem.

## Complete signed prime-power forms

For \(\sigma\in\{-1,+1\}\), define
\[
u_{n,\sigma}(k)=c_n\exp\{i\sigma(T\log n+2\pi k\alpha_n)\}.
\]
Because \(c_n\) is real,
\[
\beta_k=\sum_n(1-\alpha_n)\sum_\sigma u_{n,\sigma}(k),\qquad
A_k=\sum_n\frac1{2i}\sum_\sigma\sigma u_{n,\sigma}(k).
\]
The three terms above are therefore the following finite, exact sums over (n_t=p_t^{v_t}\le N), with no prime truncation:

\[
C_1=\sum_{i\in Q}\sum_{n_0,n_1,n_2\in\mathcal P(N)}
\prod_{t=0}^2(1-\alpha_{n_t})c_{n_t}
\sum_{\sigma_0,\sigma_1,\sigma_2=\pm1}
e^{iT\sum_t\sigma_t\log n_t}
e^{2\pi i i\sum_t\sigma_t\alpha_{n_t}}.
\]
For (C_2), with \(\Delta_{n,\sigma}(i,j)=u_{n,\sigma}(i)-u_{n,\sigma}(j)\),
\[
C_2=-\frac3{4\pi^2}
\sum_{\substack{i,j\in Q\\j\ne i}}\frac1{(j-i)^2}
\sum_{n_0,n_1,n_2\in\mathcal P(N)}(1-\alpha_{n_0})
\sum_{\sigma_0,\sigma_1,\sigma_2}\sigma_1\sigma_2\,
u_{n_0,\sigma_0}(i)\Delta_{n_1,\sigma_1}(i,j)\Delta_{n_2,\sigma_2}(i,j).
\]
For (C_3),
\[
C_3=\frac1{(2i)^3\pi^3}
\sum_{\substack{i,j,k\in Q\\\text{pairwise distinct}}}
\frac1{(j-i)(k-j)(i-k)}
\sum_{n_0,n_1,n_2\in\mathcal P(N)}
\sum_{\sigma_0,\sigma_1,\sigma_2}\sigma_0\sigma_1\sigma_2
\Delta_{n_0,\sigma_0}(i,j)\Delta_{n_1,\sigma_1}(j,k)\Delta_{n_2,\sigma_2}(k,i).
\]
These retain all carrier phases, finite endpoint indices, ordered multiplicities, conjugate signs, and proper powers. They are legitimate finite expansions at each ((T,N)), not estimates.

For any sign triple, the carrier frequency is
\[
\Omega=\sum_t\sigma_t\log n_t
=\log\!\left(\frac{\prod_{\sigma_t=+1}n_t}{\prod_{\sigma_t=-1}n_t}\right).
\]
It is exactly zero precisely when the two integer products agree. For three prime powers this can happen only in the (2\)-versus-(1) pattern (or its reversal); unique factorization then forces both factors on the two-term side to be powers of the same prime, with exponents adding to the singleton exponent. Example: (2\cdot4=8). The (2\cdot3) versus (5) triple has nonzero frequency \(\log(6/5)\), despite all three entries being actual prime powers. In the discrete index sums, aliasing also occurs when \(\Omega/L\in\mathbb Z\), and near aliases when it is close to an integer. Such terms are not removed by the exact multiplicative classification or by finite endpoint averaging.

## Normalization and simultaneous selection

The full normalized deletion difference has the exact form
\[
\tau_d(H^3)-\tau_{d'}((PHP)^3)
=\frac{\operatorname{Tr}(D^3)-r\tau_{d'}((PHP)^3)}d
+\frac{\text{cross-block cubic}}d.
\]
Decision B/D2 controls the last term on the same selected interval. Thus the residual is
\[
F(I)=\operatorname{Tr}(D^3)-r\tau_{d'}((PHP)^3).
\]
No certified bound makes \(r\tau_{d'}((PHP)^3)=o(d)\); no cancellation with \(\operatorname{Tr}(D^3)\) is established. It must remain inside (F).

An adequate exact joint-selection input is the full Decision-B endpoint-weight estimate
\[
a_T=\frac1{(M+1)^2}\sum_{u,v=0}^M\frac{|F(I_{u,v})|}{d}\longrightarrow0.
\]
Indeed, the D2-admissible set has weighted density at least (1/4). Markov applied to nonnegative crossing energy shows that the set where \(E(I)>8C_B\log d\) has weight at most (1/8). Markov applied to \(|F|/d\) shows that the set where \(|F|/d>\sqrt{a_T}\) has weight at most \(\sqrt{a_T}\). Hence the admissible, boundary-good, cubic-good intersection has positive weight eventually. This uses the same uniform pair weights and makes no independence assumption. A small signed average of (F) is insufficient: the exact abstract values (+1,-1) have signed mean zero and absolute mean one.

## Decision and remaining boundary

**F3 — conditional.** The exact algebra, low-degree bounds, prime-power expansions, and same-section selection implication are established. The one missing estimate is
\[
\boxed{\frac1{(M+1)^2}\sum_{u,v=0}^M
\frac{|\operatorname{Tr}((Q_{u,v}HQ_{u,v})^3)
-(u+v)\tau_{d-u-v}((P_{u,v}HP_{u,v})^3)|}{d}=o(1),}
\]
for the original prime-power coefficients, natural cutoff, finite (R=6000) source, and Decision-B endpoint weights; an equally strong estimate directly on the D2-admissible subset would also suffice. Existing S2/local large-sieve and operator bounds yield only the growing (O(SM/d)) cubic majorant. There is no source-valid counterexample, so this is unresolved rather than falsified.

This does not establish a uniform sixth Schatten bound, (m_3=2), conditioned Cayley energy below (0.105), the signed fifth/sixth gate, prime-to-Weil transfer, zero-side transfer, determinant compatibility, or strict (>79\%\). Those remain open.

## Reproduction

```powershell
python src/wp84_decision_f_exact_signed_deleted_block_cubic.py
python src/wp84_decision_f_exact_signed_deleted_block_cubic_replay.py
```

The producer writes the JSON certificate. The replay imports no producer module and checks exact rational matrix identities and hostile mutations; neither script can prove the asymptotic prime-source estimate.
