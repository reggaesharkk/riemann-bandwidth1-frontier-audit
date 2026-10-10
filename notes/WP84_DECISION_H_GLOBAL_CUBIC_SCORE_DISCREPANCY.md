# WP84 Decision H — global cubic-score discrepancy

**Decision H2.** The full-matrix cubic diagonal gives an exact and useful localization of the remaining trace discrepancy. The inherited source large sieve also yields a new endpoint-local square bound for the cubic scores. Its natural-cutoff majorant is still too large to prove the required discrepancy is (o(1)). No prime-source counterexample or signed saving is established.

The audit starts on `codex/c5-c6-attack-20261006` at `13e87db74bd273349dc6db94aeb2e38e95a34fe7`; the only pre-existing untracked path is `notebooklm_packet/`, left untouched. The Decision B and C–G prerequisites listed in the certificate were replayed before this audit. No push or merge was performed.

## Source and window

Set
\[
X=T/(2\pi),\quad L=\log X,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,
\quad d=\lfloor TL/(2\pi)\rfloor,
\quad M=\lceil de^{-\sqrt L/2}\rceil.
\]
The original interval is (I_0=[b,b+d-1]). Its full prime-power pool is
\[
\mathcal P(N)=\{p^v:p\text{ prime},\ v\ge1,\ p^v\le N\},\qquad
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
z_n=c_ne^{iT\log n},\quad \alpha_n=\frac{\log n}{L}.
\]
All powers, the natural cutoff and carrier phases are retained. Define
\[
w_n(k)=z_ne^{2\pi i k\alpha_n},\quad
A_k=\sum_{n\in\mathcal P(N)}\Im w_n(k),\quad
\beta_k=\sum_{n\in\mathcal P(N)}2(1-\alpha_n)\Re w_n(k),
\]
\[
H=s_0I+\operatorname{diag}(\beta)+[\operatorname{diag}(A),J],
\qquad J_{ij}=\frac1{\pi(j-i)}\ (i\ne j),\quad J_{ii}=0.
\]
Thus (H_{ii}=a_i=s_0+\beta_i), and its real symmetric off-diagonal is
\[
W_{ij}=\frac{A_i-A_j}{\pi(j-i)}\quad(i\ne j),\qquad W_{ii}=0.
\]
Let (I_{u,v}=[b+u,b+d-1-v]), (0\le u,v\le M), (Q=I_0\setminus I_{u,v}=Q_L\sqcup Q_R), (r=u+v), and (d'=d-r\ge d-2M).

The existing source gates are (s_0\to1), (a_\phi\to1), (S=\sum_{n\in\mathcal P(N)}|c_n|=O(\sqrt N/L)), and
\[
\|H\|_{op}\le K_T:=|s_0|+4S.
\]
The local discrete large sieve, uniformly in translated integer intervals (J) of length (h), gives
\[
\sum_{k\in J}A_k^2=O(h+NL),\qquad
\sum_{k\in J}\beta_k^2=O(h+NL),
\]
including the full prime-power coefficient square mass. In particular (NL/M\to0), (M/d\sim e^{-\sqrt L/2}), and (d\asymp TL\).

## Exact full-score identity

Put (g_k=(H^3)_{kk}) and leave (m_T=\operatorname{Tr}(H^3)/d) unknown. For (P=P_I), (Q=I-P), and the rectangular block (B=PHQ), let (A=PHP|_P), (D=QHQ|_Q). Since
\[
\operatorname{Tr}(PH^3P)=\operatorname{Tr}(A^3)+2\operatorname{Tr}(ABB^*)+\operatorname{Tr}(DB^*B),
\]
and (sum_{k\in Q}g_k=\operatorname{Tr}(H^3)-\operatorname{Tr}(PH^3P)), direct normalization gives
\[
\boxed{\tau_d(H^3)-\tau_{d'}(A^3)=
\frac{\sum_{k\in Q}(g_k-m_T)}{d'}+
\frac{2\operatorname{Tr}(ABB^*)+\operatorname{Tr}(DB^*B)}{d'}.}
\]
This distinguishes compression of (H^3) from cubing (PHP). The trace spaces are (A: P\to P), (B:Q\to P), (D:Q\to Q); the products in the formula have the indicated square trace spaces. The sign of both mixed contributions is positive in the identity.

With (E(I)=\|B\|_{HS}^2) and (|A\|_{op},\|D\|_{op}\le K_T),
\[
|2\operatorname{Tr}(ABB^*)+\operatorname{Tr}(DB^*B)|
\le(2\|A\|_{op}+\|D\|_{op})E(I)\le3K_TE(I).
\]
Decision B supplies the actual uniform endpoint-pair average 
\(\mathbb E_{u,v}E(I_{u,v})\le C_B\log d\). Since (d'\ge d-2M), its normalized contribution is at most
\[
\frac{3K_TC_B\log d}{d-2M}
=O\!\left(\frac{C_B}{T}+
\frac{C_Be^{-\sqrt L/2}}{\sqrt T L}\right)=o(1).
\]
No uniform-in-section estimate is used here.

The deleted diagonal-score sum separates without approximation:
\[
\sum_{k\in Q}(g_k-m_T)=Y_L(u)+Y_R(v),
\]
where (Y_L(u)=\sum_{k=b}^{b+u-1}(g_k-m_T)) and
\(Y_R(v)=\sum_{k=b+d-v}^{b+d-1}(g_k-m_T)). Under Decision B's exact uniform pair measure,
\[
\boxed{\mathbb E_{u,v}|\tau_d(H^3)-\tau_{d'}(A^3)|
\le\frac{\mathbb E_u|Y_L(u)|+\mathbb E_v|Y_R(v)|}{d-2M}
+\frac{3K_TC_B\log d}{d-2M}.}
\]

## Exact diagonal score and prime expansion

From (g_k=\sum_{j,\ell\in I_0}H_{kj}H_{j\ell}H_{\ell k}), partition the index triples by repetitions. The all-equal term is (a_k^3); for each (j\ne k), the two walks with diagonal (a_k) and one with diagonal (a_j) give the coefficient (2a_k+a_j); the remaining ordered triples are pairwise distinct. Thus
\[
\boxed{g_k=a_k^3+
\sum_{j\ne k}(2a_k+a_j)W_{kj}^2+
\sum_{\substack{j,\ell\in I_0\\k,j,\ell\ \text{pairwise distinct}}}
W_{kj}W_{j\ell}W_{\ell k}.}
\]
The last sum is ordered in ((j,\ell)); no factor of (1/2) or (1/6) is inserted. Equivalently,
\[
g_k=s_0^3+3s_0^2\beta_k+3s_0\beta_k^2+\beta_k^3
+\frac1{\pi^2}\sum_{j\ne k}\frac{(3s_0+2\beta_k+\beta_j)(A_k-A_j)^2}{(j-k)^2}
+\frac1{\pi^3}\sum_{\substack{j,\ell\in I_0\\k,j,\ell\text{ pairwise distinct}}}
\frac{(A_k-A_j)(A_j-A_\ell)(A_\ell-A_k)}{(j-k)(\ell-j)(k-\ell)}.
\]
Every row and column index here belongs to the original finite (I_0). This is not an infinite-lattice trace identity.

For a fully signed source expansion set
\[
u_{n,\sigma}(x)=c_n\exp\{i\sigma(T\log n+2\pi x\alpha_n)\},\quad
\Delta_{n,\sigma}(x,y)=u_{n,\sigma}(x)-u_{n,\sigma}(y).
\]
Then
\[
\beta_x=\sum_{n\in\mathcal P(N)}(1-\alpha_n)\sum_{\sigma=\pm1}u_{n,\sigma}(x),\qquad
A_x=\frac1{2i}\sum_{n\in\mathcal P(N)}\sum_{\sigma=\pm1}\sigma u_{n,\sigma}(x).
\]
The quadratic diagonal piece is the finite double sum
\[
\beta_k^2=\sum_{n_0,n_1\in\mathcal P(N)}
\prod_{q=0}^1(1-\alpha_{n_q})c_{n_q}
\sum_{\sigma_0,\sigma_1=\pm1}
e^{iT\sum_q\sigma_q\log n_q}
e^{2\pi ik\sum_q\sigma_q\alpha_{n_q}}.
\]
The linear term is (\beta_k=\sum_n(1-\alpha_n)\sum_\sigma u_{n,\sigma}(k)). In particular the genuine three-factor diagonal term is the finite sum
\[
\beta_k^3=\sum_{n_0,n_1,n_2\in\mathcal P(N)}
\prod_{q=0}^2(1-\alpha_{n_q})c_{n_q}
\sum_{\sigma_0,\sigma_1,\sigma_2=\pm1}
e^{iT\sum_q\sigma_q\log n_q}
e^{2\pi ik\sum_q\sigma_q\alpha_{n_q}}.
\]
The quadratic difference and mixed terms are exactly
\[
(A_x-A_y)^2=-\frac14\sum_{n_1,n_2\in\mathcal P(N)}
\sum_{\sigma_1,\sigma_2}\sigma_1\sigma_2\Delta_{n_1,\sigma_1}(x,y)\Delta_{n_2,\sigma_2}(x,y),
\]
\[
\beta_x(A_y-A_z)^2=-\frac14\sum_{n_0,n_1,n_2\in\mathcal P(N)}(1-\alpha_{n_0})
\sum_{\sigma_0,\sigma_1,\sigma_2}\sigma_1\sigma_2
u_{n_0,\sigma_0}(x)\Delta_{n_1,\sigma_1}(y,z)\Delta_{n_2,\sigma_2}(y,z),
\]
and the cubic cycle factor is
\[
(A_k-A_j)(A_j-A_\ell)(A_\ell-A_k)=
\frac1{(2i)^3}\sum_{n_0,n_1,n_2\in\mathcal P(N)}
\sum_{\sigma_0,\sigma_1,\sigma_2}\sigma_0\sigma_1\sigma_2
\Delta_{n_0,\sigma_0}(k,j)\Delta_{n_1,\sigma_1}(j,\ell)
\Delta_{n_2,\sigma_2}(\ell,k).
\]
These formulas retain every prime power, coefficient sign, carrier and finite section endpoint.

For a triple of prime powers, a zero carrier
\(\Omega=\sum_{q=0}^2\sigma_q\log n_q=0\) means equality of the products on the two sign sides. An all-plus or all-minus triple cannot equal the empty-side product (1). In the (2\)-versus-(1) case unique factorization forces the two powers to share the singleton's prime base and their exponents to add; e.g. (2\cdot4=8). A valid nonclosure is (2\cdot3/5=6/5\). This classifies exact source resonances only; it removes no nonzero carrier or near alias.

For a term in the endpoint score expansion, freeze all indices except the varying endpoint index (k). Its (k)-dependent phase has frequency (\omega) equal to the signed sum of the (\alpha_n)'s attached to factors evaluated at (k); the full carrier (e^{iT\Omega}) is separate. The exact finite geometric sum obeys
\[
\left|\sum_{k=k_0}^{k_0+u-1}e^{2\pi ik\omega}\right|
=u\quad(\omega\in\mathbb Z),\qquad
\left|\sum_{k=k_0}^{k_0+u-1}e^{2\pi ik\omega}\right|
=\frac{|\sin(\pi u\omega)|}{|\sin(\pi\omega)|}
\le\min\!\left(u,\frac1{|\sin(\pi\omega)|}\right)
\quad(\omega\notin\mathbb Z).
\]
The constant in the second bound is exactly (1). In the (\beta_k^3) terms, (\omega=\Omega/L). In terms involving (W_{kj}), different factors can be evaluated at (k) or at fixed other indices, so the correct alias frequency is the (k)-attached sum, not automatically the total (\Omega/L). Near aliases remain in the unresolved finite sums.

## What the existing source estimates buy

Let (q_k=(H^2)_{kk}=\|He_k\|_2^2=a_k^2+\sum_{j\in I_0,j\ne k}W_{kj}^2\ge0). For either maximum endpoint window (J) of length (M), the existing local sieve implies
\[
\sum_{k\in J}q_k=O(M+NL).
\]
Here is the needed finite-boundary argument for the (W)-part. From
\((A_k-A_j)^2\le2A_k^2+2A_j^2), the (A_k^2) contribution is at most (C\sum_{J}A_k^2). For the (A_j^2) contribution use
\(w_j=\sum_{k\in J,k\ne j}(j-k)^{-2}\). On the (O(M))-neighborhood of (J), (w_j=O(1)), and the large sieve bounds the (A_j^2) mass by (O(M+NL)). On a dyadic shell at distance (R\ge M), (w_j=O(M/R^2)), while its (A_j^2) mass is (O(R+NL)); summing (R=2^qM\) gives (O(1+NL/M)). Thus the whole weighted sum is (O(M+NL)), without discarding the finite interval's exterior rows. The same sieve on (I_0) gives
\[
\operatorname{Tr}(H^2)=\sum_{I_0}q_k=O(d+NL)=O(d),
\]
because (NL/d=O(e^{-\sqrt L})\). Hence
\[
|m_T|=\frac{|\operatorname{Tr}H^3|}{d}
\le\frac{K_T\operatorname{Tr}(H^2)}d=O(K_T).
\]
No value or sign of (m_T) is inferred.

As (g_k=(He_k)^*H(He_k)),
\[
|g_k|\le K_Tq_k,\qquad q_k\le K_T^2.
\]
Consequently the following **source-valid localized score-square bound** is proved for either endpoint window:
\[
\boxed{\sum_{k\in J}|g_k-m_T|^2
\le2K_T^2\sum_Jq_k^2+2M|m_T|^2
=O\bigl(K_T^4(M+NL)+MK_T^2\bigr).}
\]
The direct absolute-value bound is
\[
\mathbb E_u|Y_L(u)|+\mathbb E_v|Y_R(v)|
\le O\bigl(K_T(M+NL)\bigr),
\]
so its normalized scale is (O(K_TM/d)) when (M\gg NL). Neither estimate uses random phases, a global sixth moment, a model moment, or an infinite-lattice replacement.

For the second-moment route, Cauchy gives for each endpoint side
\[
|Y(u)|^2\le M\sum_{k\in J}|g_k-m_T|^2,
\qquad \mathbb E_u|Y(u)|\le\sqrt{M\sum_{k\in J}|g_k-m_T|^2}.
\]
Writing (S_2=\sum_{J_L\cup J_R}|g_k-m_T|^2), a sufficient condition for the required discrepancy is
\[
\boxed{S_2=o(d^2/M).}
\]
This endpoint-local condition is strictly weaker than a uniform source bound (\tau_d(|H|^6)=O(1)): the latter implies \(\sum_J|g_k|^2\le\operatorname{Tr}(H^6)=O(d)\) by Cauchy on each diagonal entry, and it bounds (m_T), so it implies (S_2=O(d+M)=o(d^2/M)). Conversely, an abstract diagonal matrix can place a growing eigenvalue strictly inside (I_0), away from the endpoint windows: for dimensions (d=t^3), one eigenvalue (t) gives (\tau_d(H^6)=t^3\to\infty\) while the endpoint centered score-square remains (O(M)\ll d^2/M). This example proves only that the endpoint condition does not entail global S6; it is not a prime-source counterexample.

A separate abstract deletion spike checks the normalized identity's scale: in dimension \\(d=t^3\\), put a single diagonal eigenvalue \\(t\\) on a deleted coordinate and zeros on retained coordinates. Then \\(m_T=1\\), \\(\\tau_d(H^3)=1\\), \\(\\tau_{d-1}(A^3)=0\\), and the centered deleted score contributes exactly \\(1\\). It shows why a rank fraction tending to zero alone cannot replace the endpoint estimate. It is not an admissible prime-source example.

The currently certified upper majorant relative to the required scale is
\[
\frac{K_T^4(M+NL)+MK_T^2}{d^2/M}
=O\!\left((K_T^4+K_T^2)(M/d)^2\right)
=O\!\left((1+N^2/L^4+N/L^2)e^{-\sqrt L}\right).
\]
Its leading available envelope is (e^{2L-3\sqrt L}/L^4\), which grows. Likewise the direct normalized envelope (K_TM/d) has leading term (e^{L/2-\sqrt L}/L\), which also grows. These diverging *upper bounds* show the present estimates fail to certify the target; they are neither lower bounds nor evidence that the actual prime-source discrepancy is large.

## Selection, decision and first missing estimate

If the one-sided endpoint discrepancy were shown to be (o(1)), Decision D2's admissible pair set (weighted density at least (1/4)) could be intersected with the energy-good set (density at least (7/8), by Markov at threshold (8C_B\log d)) and the score-good set (density (1-o(1)), by Markov on the averaged absolute discrepancy). Their intersection is positive for large (T), under the original uniform pair weights and without independence. This only selects a section for the direct first-strike consumer; it does not transfer to the source-masked determinant consumer.

**H2 — quantitative estimate proved, transfer open.** The single first missing estimate is a source-matched bound for the centered full-matrix cubic-score partial sums on the two length-(M) endpoint windows, strong enough to give
\[
\boxed{\mathbb E_u|Y_L(u)|+\mathbb E_v|Y_R(v)|=o(d).}
\]
An endpoint-local score-square theorem (S_2=o(d^2/M)\) would suffice, and is weaker than uniform S6, but the large-sieve/operator consequence above misses it by the displayed growing factor. Signed mean cancellation alone cannot replace absolute partial-sum control. No attempt is made to continue through algebraically equivalent reductions.

The following remain **OPEN**: (m_3=2), conditioned Cayley energy below (0.105), signed fifth/sixth gate, prime-to-Weil identification, zero-side transfer, determinant compatibility, and the strict (>79\%\) theorem.

## Verification

Run:

```powershell
python src/wp84_decision_h_global_cubic_score_discrepancy.py
python src/wp84_decision_h_global_cubic_score_discrepancy_replay.py
```

The producer records the analytic hypotheses and a rational finite-matrix regression. The independent replay does not import the producer. These scripts check identities and certificate consistency; they do not prove the unresolved prime-source discrepancy.
