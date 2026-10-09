# WP84 — exact no-wrap Fourier identity and cubic transfer obstruction

**Decision C — exact algebra closed; quantitative natural-cutoff transfer remains open.**

This audit tests the full sharp prime-field matrix with its natural prime-power cutoff and complete (J) kernel. It proves the no-wrap identity as an operator on (L^2(\mathbb T)), records the half-weight endpoint convention for generalized Fourier modes, and gives an explicit boundary trace-ideal bound. That bound is valid but does not tend to zero at the original cutoff. The infinite-lattice identity therefore does not close the actual finite-section cubic aliases. No source value (m_3=2), (0.105) energy bound, or strict (>79\%) theorem is claimed.

## 1. Original prime-field matrix and source scope

Use the checked-in source scale

\[
 L=\log(T/(2\pi)),\quad X=T/(2\pi),\quad N=\lfloor Xe^{-\sqrt L}\rfloor,\quad d=\lfloor TL/(2\pi)\rfloor,\quad \tau_k=T+2\pi k/L.
\]

All prime powers (n=p^v\le N) are retained, with
\[
 c_n=-\frac{\Lambda(n)}{a_\phi L\sqrt n},\quad Q_T(t)=\sum_{n\le N}c_ne^{it\log n},\quad z_n=c_ne^{iT\log n},\quad \alpha_n=\frac{\log n}{L}.
\]

The source-field coordinates are
\[
 A_k=\Im Q_T(\tau_k),\qquad B_k=2\Re Q_T(\tau_k)-2\Im Q'_T(\tau_k)/L.
\]
For one prime-power summand, writing (w_n(k)=z_ne^{2\pi i k\alpha_n}), differentiation gives
\[
 \Im(c_ne^{i\tau_k\log n})=\Im w_n(k),\qquad \Im(c_ni\log(n)e^{i\tau_k\log n})/L=\alpha_n\Re w_n(k),
\]
so its exact contributions are
\[
 A_n(k)=\Im w_n(k),\qquad B_n(k)=2(1-\alpha_n)\Re w_n(k).
\]
The sign is fixed by the minus (2\Im Q'_T/L) in (B).

With (J_{ij}=1/(\pi(j-i))) for (i\ne j), (J_{ii}=0), the full finite prime-field matrix on a contiguous section is
\[
 H_{\rm pr}=s_0(T)I+\operatorname{diag}(B)+[\operatorname{diag}(A),J].                 \tag{1}
\]
The source gates are (a_\phi(T)\to1), (s_0(T)\to1), the natural cutoff above, and the stated contiguous sections. If (P_I) projects onto that section, the finite prime matrix is exactly (P_IH_{\rm pr}P_I), including (s_0(T)P_I). This is the prime-field matrix identity. Any identification with a separate Weil/zero matrix still requires its own source error estimate.

The scalar formulas are explicit finite sums. The earlier regression program `wp84_sharp_loewner_dirichlet_gate.py` checks their algebra on a small synthetic exponential sum; that regression is not a large-(T) prime-matrix calculation. The source scale, prime-power coefficients, and section kernel are also recorded in `WP84_DIRECT_PRIME_FIELD_STATE_LAW.md` and `WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER.md`.

## 2. Fourier multiplier and no-wrap identity

On finitely supported sequences, (J) is convolution with coefficients (1/(\pi r)), (r\ne0). Under the Fourier transform (\ell^2(\mathbb Z)\simeq L^2(\mathbb T)), its multiplier is
\[
 j(x)=\frac1\pi\sum_{r\ne0}\frac{e^{2\pi i r x}}r=i(1-2x),\qquad 0<x<1.                                  \tag{2}
\]
This is a bounded multiplier of norm one, with its symmetric Fourier-series value (j(0)=0) at the jump. The Fourier series is interpreted in the usual principal-value/(L^2) sense. Generalized waves (e_x(k)=e^{2\pi ikx}) are not vectors of \(\ell^2(\mathbb Z)); equations on such waves below are shorthand for the corresponding (L^2(\mathbb T)) translation operators, or pointwise coefficient identities away from the measure-zero jump set.

For (0<\alpha<1), define partial translations on (L^2(0,1)):
\[
 (S_\alpha^+f)(y)=\mathbf1_{(\alpha,1)}(y)f(y-\alpha),\qquad (S_\alpha^-f)(y)=\mathbf1_{(0,1-\alpha)}(y)f(y+\alpha).
\]
They are contractions and ((S_\alpha^+)^*=S_\alpha^-). Multiplication by (A_n(k)=\Im(z_ne^{2\pi ik\alpha})) shifts Fourier frequency by (\pm\alpha). Applying (2), the plus coefficient in (M_{B_n}+[M_{A_n},J]) on an interior wave is
\[
 (1-\alpha)z_n+\frac{z_n}{2i}\big(j(x)-j(x+\alpha\bmod1)\big)=\begin{cases}z_n,&x+\alpha<1,\\0,&x+\alpha>1,\end{cases}
\]
and the minus coefficient is
\[
 (1-\alpha)\bar z_n-\frac{\bar z_n}{2i}\big(j(x)-j(x-\alpha\bmod1)\big)=\begin{cases}\bar z_n,&x>\alpha,\\0,&x<\alpha.\end{cases}
\]
Consequently, as a bounded-operator identity (equality almost everywhere),
\[
 M_{B_n}+[M_{A_n},J]=z_nS_\alpha^+ +\bar z_nS_\alpha^-.                 \tag{3}
\]
The task's pointwise candidate is correct away from endpoints. At (x=1-\alpha) and (x=\alpha), the symmetric multiplier convention gives coefficients (z_n/2) and \(\bar z_n/2), respectively, not zero or a full coefficient. For example ((\alpha,x,z)=(1/5,4/5,1)) gives a plus coefficient (1/2). These endpoint values do not affect the (L^2) operator, but they falsify the unqualified pointwise formula for all generalized waves.

The operator in (3) is self-adjoint: (A_n,B_n) are real, (J^*=-J), so ([M_{A_n},J]^*=[M_{A_n},J]); equivalently the partial translations are adjoints with conjugate coefficients. Adding all prime powers and the scalar yields
\[
 H_{\rm pr}=s_0I+\sum_{p^v\le N}(z_{p^v}S_{\alpha_{p^v}}^+ +\bar z_{p^v}S_{\alpha_{p^v}}^-).                    \tag{4}
\]

## 3. What no-wrap proves for the infinite cubic

At fixed (T,N), (4) is a finite sum of bounded operators. In a product of three prime-power terms, let the signed total frequency displacement be (\delta=\epsilon_1\alpha_{n_1}+\epsilon_2\alpha_{n_2}+\epsilon_3\alpha_{n_3}). The composition is supported only where every intermediate translated coordinate remains in ((0,1)), without wrap. If (\delta=m\ne0) is an integer, an initial (x\in(0,1)) cannot end at (x+m\in(0,1)); that product operator is identically zero. Thus exact nonzero integer aliases are eliminated in the infinite no-wrap operator, not by unique factorization but by partial-shift support.

For noninteger total displacement, the corresponding lattice diagonal contains the carrier (e^{2\pi ik\delta}); its Cesàro mean over an infinite interval is zero. Exact zero displacement is the only possible infinite-volume diagonal resonance. This statement takes section length to infinity at fixed finite (T,N); it is not uniform in the natural growing prime pool and does not identify the finite-section trace with that limit.

For the cubic expansion, the existing source audit classifies:

- Exact zero-frequency ordinary-prime closures: none in the (1:2) split by unique factorization. Repeated-base and proper-power populations have only the previously proved (o(1)) scopes recorded in the source cubic audit; those scopes are not extended here.
- Mixed signs: six placements, three (1:2) and three (2:1). For an ordered two-prime side, a distinct-prime product has at most two ordered presentations. At fixed (R=6000), the closed lag-path count is ((2R+1)^2=12001^2).
- All-same signs: two placements; first and second periodic aliases lie within the natural product range.
- Nonzero integer aliases: killed in the infinite operator by (4), but finite compression can break the cancellation through paths leaving the section.
- Near aliases: the finite root sum remains order one when (|\lambda-mL|\lesssim1/T).
- Long tails: not controlled by the no-wrap identity or by fixed-(R) algebra; they remain part of the full source sum.

The source third-moment note gives the exact finite path/root expression and removes its specified repeated-base and central contributions. The remaining all-distinct nonzero/near-alias and tail correlation has no certified signed bound. This audit does not assume a value or sign for that remainder.

## 4. Exact finite-section compression and boundary estimate

The actual finite prime matrix is exactly the compression in (1); this is an identity, not an approximation. The transfer question is different: compare the cubic of the compression with the compression of the full infinite-lattice cubic. Put (P=P_I), (Q=I-P), and (H=H_{\rm pr}). Inserting (P+Q) between the three factors gives exactly three omitted terms. Schatten Cauchy--Schwarz yields
\[
 \left|\operatorname{Tr}(PHP)^3-\operatorname{Tr}(PH^3P)\right|\le 3\|H\|_{op}\,\|PHQ\|_2^2.                     \tag{5}
\]
Let (S=\sum_{p^v\le N}|c_{p^v}|). Since ‖J‖op=1, (0<\alpha_{p^v}<1), and (sup_k|A_k|\le S, sup_k|B_k|\le2S),
\[
 \|H\|_{op}\le |s_0|+4S.                                  \tag{6}
\]
Only the commutator crosses the section boundary. For displacement (r\ne0), there are exactly (2\min(|r|,d')) ordered crossing pairs, and (|A_i-A_j|\le2S). Hence
\[
 \|PHQ\|_2^2\le \frac{8S^2}{\pi^2}(H_{d'}+1),             \tag{7}
\]
where (H_{d'}=\sum_{r=1}^{d'}1/r). Combining (5)--(7),
\[
 \frac1{d'}\left|\operatorname{Tr}(PHP)^3-\operatorname{Tr}(PH^3P)\right|\le \frac{24(|s_0|+4S)S^2(H_{d'}+1)}{\pi^2d'}.            \tag{8}
\]
The prime number theorem gives (S=O(\sqrt N/L)) (ordinary primes dominate; higher powers contribute lower order). With (d'\asymp TL), the leading term in (8) is (O(N^{3/2}\log d'/(T L^4))). At (N\asymp T e^{-\sqrt L}), this is (O(T^{1/2}e^{-3\sqrt L/2}/L^3)), which diverges as an upper bound. Thus (8) is a valid quantitative finite-section estimate but is not useful at the original cutoff. It is not a lower bound and does not prove that the actual transfer error is large.

## 5. Finite carrier kernel and the first missing estimate

For every finite section (I=[k_-,k_-+d'-1]), the exact sampled kernel is
\[
 K_I(\lambda)=e^{i(T+2\pi k_-/L)\lambda}\frac1{d'}\sum_{j=0}^{d'-1}e^{2\pi i j\lambda/L}.                 \tag{9}
\]
If (\lambda=mL+\delta), the integer (m) disappears from the geometric sum but not from the carrier. At (|\delta|\le c/T) and (d'\asymp TL), the normalized sum need not be small. At each fixed (T), its infinite-length Cesàro limit kills noninteger frequencies; that does not justify taking (T\to\infty) with (d'=d'(T)) and (N=N(T)).

After the already justified central and repeated-base removals, the first unproved estimate is the source-weighted signed bound
\[
 \sup_{I\ \mathrm{admissible}}\left|\sum_{\substack{\text{all-distinct cubic paths and prime powers}\\\text{nonzero, near-alias, and tail terms}}}W_{\ell,\epsilon}(n_1,n_2,n_3)K_I(\lambda)\right|=o(1),                 \tag{10}
\]
with actual coefficients, the full prime-power cutoff, all root paths, carrier phases, and section endpoints. For ordinary-prime (1:2) and (2:1), the six sign placements, two ordered pair presentations, and (12001^2) paths remain. The existing generic sampled-product majorant has scale logarithmic factors times (N^{3/2}/T); at (N=T^{1-o(1)}) it is not (o(1)). This shows insufficiency of that majorant only, not failure of (10).

The no-wrap identity removes exact nonzero alias operators in the infinite-lattice expression. It does not supply (10), eliminate near aliases at finite section length, or bound finite-section boundary leakage at the natural cutoff. The two-atomic spectral witness is unchanged. Even a future proof that (m_3=2) would not alone establish the conditioned-Cayley (0.105) energy inequality.

## 6. Reproduction and evidence boundary

Run:

```powershell
python src/wp84_infinite_no_wrap_cubic.py
python src/wp84_infinite_no_wrap_cubic_replay.py
python src/wp84_sharp_loewner_dirichlet_gate.py
```

The producer writes `certificates/WP84_INFINITE_NO_WRAP_CUBIC_CERTIFICATE.json`. The replay independently checks rational interior/endpoint coefficients, Fourier-multiplier convergence with a Dirichlet tail enclosure, a finite compression regression, boundary-pair counts, and hostile sign/endpoint/near-alias mutations. These verify the algebra and finite estimates, not the open natural-cutoff estimate (10).

No new source moment, concentration law, prime-to-Weil transfer, or conditioned energy bound is established. **Strict (>79\%) remains OPEN.**

## Appendix — exact full-prime cubic path coefficient

Write V=H_pr-s0 I. For an ordered triple of partial shifts set

    q_0=0,
    q_j=sum_{t<=j} epsilon_t alpha_(n_t),
    delta=q_3,
    omega=[1-(max_j q_j-min_j q_j)]_+,

with z_n^(+)=z_n and z_n^(-)=conjugate(z_n). The path support is the
intersection of 0<x+q_j<1; it is an interval of length omega. Thus the
finite-section cubic of V has the exact full-prime-power formula

    tau_I(V^3)=sum_{n_1,n_2,n_3<=N} sum_{epsilon in {+,-}^3}
       omega * product_t z_(n_t)^(epsilon_t)
       * exp(2*pi*i*k_-*lambda/L) * D_(d')(lambda/L),
    lambda=sum_t epsilon_t*log(n_t)=L*delta,
    D_(d')(u)=d'^(-1) sum_(j=0)^(d'-1) exp(2*pi*i*j*u).

Here the T-carrier is already in each z_n; the displayed section factor is
only exp(2*pi*i*k_-*lambda/L). If instead raw coefficients c_n are used,
the combined kernel is exp(i*(T+2*pi*k_-/L)*lambda)*D_(d')(lambda/L).
This identity retains the actual carrier, all prime powers, and section
endpoints. More strongly, omega=0 whenever |delta|>=1, not just at exact
integer aliases. Thus every second-or-higher alias strip is killed in
Tr(P_I V^3 P_I); the first alias can survive only on the side |delta|<1.
Exact zero-frequency terms may remain. The s0 contribution is separate:

    tau_I((s0 I+V)^3)=s0^3+3*s0^2*tau_I(V)
                         +3*s0*tau_I(V^2)+tau_I(V^3).

Rational checks: increments 1/4, 1/3, -1/5 give omega=5/12; increments
1/4, 1/2, 1/4 give delta=1 and omega=0. The formula is finite-cutoff
algebra, not an asymptotic evaluation. The 12001^2 lag-path count applies
only to the distinct fixed-band R=6000 expansion; the full J formula has
no finite lag cutoff.

For the surviving first-alias strip, write delta=1-epsilon, with
0<=epsilon<=1/2. Then omega<=epsilon. Since d'~T L/(2*pi), the finite
section kernel obeys |D_(d')(delta)|<=min(1,C/(T L epsilon)) with an
absolute C for this strip. Therefore omega*|D|<=C/(T L). The same bound
holds at the negative first alias by conjugation. The full coefficient
L1 mass is S^3, so this source-valid absolute majorant is

    O(S^3/(T L))=O(N^(3/2)/(T L^4))
      =O(T^(1/2)*exp(-3*sqrt(L)/2)/L^4)

at the natural cutoff. It diverges as an upper bound. This is a strict
improvement by one logarithm over the unweighted alias majorant, but it is
not o(1) and provides no signed saving. The actual prime-weighted signed
alias sum remains the first missing estimate.

The sharper finite-section statement is exact: for 0<epsilon<=1/2,
|sin(pi*epsilon)|>=2*epsilon, so

    omega*|D_(d')(1-epsilon)|
       <= epsilon/(d'*|sin(pi*epsilon)|)
       <= 1/(2*d').

The same holds for delta=-1+epsilon. This proves a uniform O(1/d') kernel
payment on the entire surviving first-alias strips, not merely the O(1/(TL))
asymptotic restatement. It still leaves the full coefficient mass S^3/d',
which is not o(1) at the natural cutoff.
