# Localize the exact Hermite projection before weak dualization

Date: 2026-10-09. Starting commit: `be51f8b9b6ca516ef92f2b2957897986d2c2b99e`.
Decision **C**: fixed-\(R\) covariance transfer closes after localization, while the source-prime dependent-phase law remains open. The large weak-dual coefficient sum is absent from the spatial localization inequality. The resulting certified radii are still about (10^{12}), but for every listed fixed (U) they make the pair localization error strictly smaller than \(\epsilon/4\). This is a finite, very large localization scale, not a divergence or a theorem obstruction. Strict (>79\%) remains OPEN.

This audit uses the frozen cap consumer only:

\[
c=3142/2415,\quad a=131/200,\quad z=c+ia,\quad
P(x)=1-\frac{43428}{13891}x+\frac{37704}{13891}x^2-\frac{9660}{13891}x^3,
\]
\[
f(x)=\frac{(c^2+a^2)^3P(x)^2}{((x-c)^2+a^2)^3},\quad
E_\infty=\frac{7761139416076220170204368647089}{1680256283972002400160000000000},
\]
\[
w_0=1415/13891,\quad \epsilon=21/200-w_0=8711/2778200,
\quad K=32,\quad \delta=1/100000.
\]
The previously proved global cap (0\le f\le E_\infty), (1-f\le\mathbf1_{x>0}) removes the large-\(u\) tail for this one-sided consumer. It does not identify any actual prime endpoint with a model value.

## 1. Project first: exact contraction

Use the real Gaussian probability space underlying the actual finite-\(T\) field and the normalized Hilbert space (L^2(\Omega;\mathrm{HS}_\tau)), where \(\|A\|_{2,\tau}^2=\mathbb E\,d^{-1}\mathrm{tr}(A^*A)\). Let (P_{\le K}) be the orthogonal projection onto total Hermite degree at most (K). For any (F,G) in this Hilbert space, Pythagoras gives

\[
\|P_{\le K}(F-G)\|_2\le\|F-G\|_2.
\]
With (S_K(F)=\|P_{\le K}F\|_2^2), factor the difference of squared norms and apply Cauchy--Schwarz:
\[
|S_K(F)-S_K(G)|\le(\|F\|_2+\|G\|_2)\|F-G\|_2.
\]
For (F=Q_{\rm cons}(H)), the exact consumer cap implies \(\|F\|_2^2=\mathbb E\tau f(H)\le E_\infty\). Therefore
\[
\boxed{|S_K(F)-S_K(G)|\le2\sqrt{E_\infty}\,\|F-G\|_2.}
\]
This is exact and independent of (K), the number of dual nodes, \(\Lambda_U\), or any mask-orbit count. The replay enumerates 3,125 rational vectors in a finite Hermite-coordinate basis and verifies the contraction. Its explicit (2I) expansive-map example fails the same inequality.

## 2. Translated block cuts and the new coefficient

Let (m=R+1). Average the (m) translated partitions into blocks of length (m), retaining short physical edge blocks. The source finite-cut identity gives for the random scalar field (v=a+\sqrt u\,\alpha)
\[
\mathbb E\,\|H-H_{\rm cut}\|_{2,\tau}^2
\le h_m\left(C_*+\frac{u}{4a_\phi^2}\right),\qquad
h_m=\frac{8(H_m+1)}{\pi^2m}.
\]
Here the cut changes only the off-diagonal commutator component; the diagonal component is retained. (C_*=2) is the eventual bound on the original prime-field marginal mass. Coupling (H,H_{\rm cut}) with the same Gaussian coordinates and using the established normalized Schatten-2 Lipschitz bound \(C_1\le10\),
\[
\|Q(H)-Q(H_{\rm cut})\|_{L^2(\mathrm{HS}_\tau)}
\le10\sqrt{h_m}\sqrt{C_*+u/(4a_\phi^2)}.
\]
The projection contraction yields
\[
e_{\rm proj}(u,R)=20\sqrt{E_\infty}\sqrt{h_m}\sqrt{C_*+u/(4a_\phi^2)}.
\]
In particular, the actual telescope uses both layers:
\[
\left|[S_{32}(U)-S_{32}(\delta)]-[S_{32}^{\rm cut}(U)-S_{32}^{\rm cut}(\delta)]\right|
\le20\sqrt{E_\infty}\sqrt{h_m}
\left[\sqrt{C_*+U/(4a_\phi^2)}+\sqrt{C_*+\delta/(4a_\phi^2)}\right].
\]

The weak-dual route instead pays
\[
43\sqrt{h_m}\left[\Lambda_U\sqrt{C_*+U/(4a_\phi^2)}+\sqrt{C_*+\delta/(4a_\phi^2)}\right],
\]
where exact replay of the (K=32) witness gives
\[
\Lambda_U=\frac{505188015348196189693235774226141659495879806382496275807827042414664568918197834015309}{16107689666801183743028326831779334846580946960663900516250658618048401530900000000}
\approx31363.1579573708766.
\]
The old terminal \(\sqrt{h_m}\) coefficient is (43\Lambda_U). The new coefficient is exactly (20\sqrt{E_\infty}), enclosed above by the rational \(2149190827101/50000000000\) and numerically about (42.98381654202). Their ratio is about (31,374.9662). Thus the \(\Lambda_U\) amplification is removed algebraically, before any Mehler dual is introduced. The one initial \(\delta\) layer remains explicitly paid.

Using (\pi>3), (H_m\le1+\lceil\log_2m\rceil), (C_*=2), (a_\phi\to1), and outward rational square-root enclosures, the following are sufficient fixed radii for pair error (<\epsilon/4):

| fixed (U) | sufficient (m) | sufficient (R=m-1) | upper bound / \(\epsilon/4\) |
|---:|---:|---:|---:|
| 1 | 953,368,280,617 | 953,368,280,616 | (<1) |
| 2 | 1,007,195,524,156 | 1,007,195,524,155 | (<1) |
| 4 | 1,137,699,372,207 | 1,137,699,372,206 | (<1) |
| 8 | 1,339,733,575,174 | 1,339,733,575,173 | (<1) |
| 16 | 1,715,712,785,960 | 1,715,712,785,959 | (<1) |
| 32 | 2,463,125,307,051 | 2,463,125,307,050 | (<1) |

These are certified sufficient thresholds from a conservative envelope, not claimed global minima and not a choice of theorem-optimal (U). They are astronomically large. No (R(T)) is used: first hold this finite (R) fixed, take (T\to\infty), then consider increasing (R). The physical edge payment is separate and also improves when projection is kept intact. There are at most (2R) edge sites. At each site, componentwise projection contraction gives (mathbb E|(P_{\le32}Q)_{jj}|^2\le\mathbb E|Q_{jj}|^2\le E_\infty), so each projected diagonal energy lies in ([0,E_\infty]). The pair cylinder lies in ([-E_\infty,E_\infty]); replacing edge windows costs at most
\[
|e_{\rm edge}^{\rm proj}|\le4E_\infty R/d.
\]
It tends to zero only after (T\to\infty) at fixed (R), and is not folded into the displayed spatial error or counted twice. The old (4(\Lambda_U+1)E_\infty R/d) was the weak-dual edge estimate and is unnecessary for the projected-energy cylinder.

## 3. Fixed-\(R\) covariance transfer and chaos coordinates

After localization, the Gaussian cylinder has (4(2R+1)) real coordinates. For fixed (R), let its covariance matrices be (C_{T,R}\to C_{{\rm ref},R}) in operator norm, as given by the existing fixed-\(R\) prime-square covariance transfer. Choose their canonical positive semidefinite roots and use one standard real Gaussian vector (g):
\[
W_{T,R}=C_{T,R}^{1/2}g,\qquad W_{{\rm ref},R}=C_{{\rm ref},R}^{1/2}g.
\]
The operator square-root map is (1/2)-Hölder on PSD matrices, including singular matrices:
\[
\|C_{T,R}^{1/2}-C_{{\rm ref},R}^{1/2}\|_{\rm op}
\le\|C_{T,R}-C_{{\rm ref},R}\|_{\rm op}^{1/2}\to0.
\]
With fixed pole distance (a>0), the resolvent consumer is bounded and Lipschitz. The common-\(g\) coupling therefore gives (L^2) convergence of (Q(H_T+\sqrt u W_{T,R})); applying the same fixed orthogonal (P_{\le32}) and the difference-of-squares bound proves (S_{32,T,R}(u)\to S_{32,{\rm ref},R}(u)). This uses no derivatives through (2K+2). It is a fixed-\(R\) statement, not uniform in (R), and does not exchange the (T,R) limits.

Total-degree Hermite spaces are invariant under orthogonal changes of standard Gaussian coordinates. Adding unused independent coordinates embeds the same chaos decomposition with degree zero in those directions. Isometric changes between Gaussian factorizations preserve degree; singular covariance is handled by an ambient PSD root and continuity across rank changes. A general nonorthogonal coordinate transform does not preserve Hermite degree unless it is whitened/reduced to the corresponding orthogonal or isometric map. The common-coordinate argument uses only this valid invariance.

## 4. The localized prime cylinder and its derivatives

For the real prime-window vector (x=X_{T,R}), write its finite linear Loewner sample map as (M_R(x)). For a fixed reference covariance root,
\[
F_{R,u,x}(g)=Q_{\rm cons}(M_R(x)+\sqrt u\,C_{{\rm ref},R}^{1/2}g),
\quad s_{32,R,u}(x)=\|P_{\le32}F_{R,u,x}\|_{L^2(g;\mathrm{HS}_\tau)}^2,
\]
\[
\Psi_R(x)=s_{32,R,U}(x)-s_{32,R,\delta}(x).
\]
The projection is independent of $x$, so $D_x^j(PF)=P D_x^jF$, $j=1,2,3$. For the Cayley polynomial $Q=q(U)$, \(\|U\|_{\rm op}=1\) and \(\|D^rU[B_1,\ldots,B_r]\|_{\rm op}\le2r!a^{-r}\prod\|B_i\|_{\mathrm{op}}\). Using the source-certified exact rational enclosures \(|q_1|,|q_2|<442/1000\), \(|q_3|<634/1000\), and input map norm \(\le6\), the replay obtains
\[
C_1(Q)=6456/655,\quad C_2(Q)=1266560/17161,\quad C_3(Q)=1453440000/2248091,
\]
and sampled-matrix derivative bounds
\[
D_1=38736/655,\quad D_2=45596160/17161,\quad D_3=313943040000/2248091.
\]
For a single $s_{32,R,u}$, differentiating the squared norm gives
\[
|Ds[h]|\le2\sqrt{E_\infty}D_1\|h\|,\quad
|D^2s[h,k]|\le2(D_1^2+\sqrt{E_\infty}D_2)\|h\|\|k\|,
\]
\[
|D^3s[h,k,l]|\le(6D_1D_2+2\sqrt{E_\infty}D_3)\|h\|\|k\|\|l\|.
\]
Taking the difference of the (U) and \(\delta\) layers doubles these envelopes. Thus valid derivative constants for \(\Psi_R\) are
\[
C_\Psi^{(1)}=4\sqrt{E_\infty}D_1,\quad
C_\Psi^{(2)}=4(D_1^2+\sqrt{E_\infty}D_2),\quad
C_\Psi^{(3)}=4(3D_1D_2+\sqrt{E_\infty}D_3),
\]
approximately (508.4034, 36,830.9439, 3,086,087.1986). These are finite-\(R\) cylinder bounds and contain no \(\Lambda_U\). They do not by themselves make the prime error small.

## 5. The prime comparison is still the same missing law

Let $X_{T,R}=(\Re\xi_{K+r},\Im\xi_{K+r},\Re\chi_{K+r},\Im\chi_{K+r})_{|r|\le R}$ be the actual full-cutoff prime-window vector, with the original masks, carrier phases, and proper powers retained. At an ordinary prime, its complex vector contribution is
\[
V_p(K)=c_p e^{iT\log p}e^{2\pi iKs_p}
\left(e^{2\pi irs_p},\; i s_p e^{2\pi irs_p}\right)_{|r|\le R},\quad
c_p=-\frac{\log p}{a_\phi L\sqrt p},\quad s_p=\frac{\log p}{L}.
\]
Use its real and imaginary parts; contributions of (p^v) are grouped at the prime-base step. In a fixed prime-base ordering let (Y_p(K,g)) be the hybrid state before replacing the current prime group, and \(\Sigma_p\) its independent-circle covariance. Ordinary multivariate Taylor/Lindeberg gives
\[
A_{1,T,R}=\sum_p\mathbb E[D\Psi_R(Y_p)\cdot V_p(K)],
\]
\[
A_{2,T,R}=\frac12\sum_p\mathbb E\left[D^2\Psi_R(Y_p):(V_p(K)V_p(K)^T-\Sigma_p)\right],
\]
\[
\mathbb E\Psi_R(X_{T,R})-\mathbb E\Psi_R(G_R)
=A_{1,T,R}+A_{2,T,R}+O_R(L^{-3}).
\]
The remainder follows from the existing grouped-prime-base cubic mass with fixed (R); proper-power deletion remains only within its previously proved Lipschitz scope. Each (Y_p) depends on the same trace index (K) as (V_p(K)). Mean zero does not kill (A_1), and covariance matching does not kill (A_2); the existing pairwise-independent (X,Y,XY) example remains a valid warning. No translated-center averaging, conjugation, or circularity identity presently proves either term (o(1)). Localization constants improve, but the dependent-phase obstruction is unchanged in kind.

The first missing theorem is exactly: for each fixed (R), the source-exact full-prime sums above satisfy \( A_{1,T,R}+A_{2,T,R}\to0\), or directly \(\mathbb E\Psi_R(X_{T,R})-\mathbb E\Psi_R(G_R)\to0\), with same-index dependence, full cutoff, masks, carrier phases, and proper powers respected. This is not proved here. Separately, the actual fixed-\(U\) signed curvature lower bound and zero-side transfer obligations remain open.

The optional weak-dual multiplier replay scans (n=0,\dots,2047) exactly and uses \((127/128)^{128}<3/8\) for the remaining tail. It gives
\[
3175.564307960185\ldots=|\lambda_0|\le M_q=\sup_{n\ge0}|q_\lambda(n)|<3175.574307960186\ldots,
\]
compared with \(\Lambda_U\approx31363.1579573708766\). The chaos operator (T_q=\lambda_0I+\sum_j\lambda_jP_{\rho_j}) acts on degree (n) by (q_\lambda(n)), so its operator norm is exactly (M_q). This independent bound is not used in the new projected localization.

## 6. Two-stage band/block check

The existing (O(1/r)) one-point resolvent and repeated-pole estimates are scalar trace statements. Applying the available Schatten-2 consumer Lipschitz bound to a Hilbert-tail truncation incurs the square-root rate (O(r^{-1/2})) at the matrix-input level; it does not yield a better projected-energy estimate. The proposed boundary-rank shortcut also fails to pass through Hermite projection. For a standard Gaussian divided into (d) equal-probability intervals, set \(\Delta(g)=e_je_j^T\) on interval (j). Then \(\Delta(g)\) has rank one for every (g), but its degree-zero Hermite projection is \(\mathbb E\Delta=I/d\), of rank (d). Hence pointwise (O(r)) boundary rank cannot be promoted to an (O(r/m)) bound for \(\|P_{\le K}\Delta\|_2^2\) without an additional theorem. No two-stage improvement or (r,m) optimization is claimed.

## Verification and scope

Run:

```powershell
python src/wp84_localize_first_hermite_projection.py
python src/wp84_localize_first_hermite_projection_replay.py
```

The independent replay checks exact rational localization thresholds, the fixed constants and derivative formulas, finite Hermite contraction, the optional (M_q) enclosure, source SHA-256 hashes, and rejects all 20 required hostile mutations. The machine certificate lists source hashes and all exact values. No raw high-moment expansion, selector recovery, model-to-actual substitution, or strict (>79\%) claim is made. `notebooklm_packet/` is outside this audit and remains untouched.
