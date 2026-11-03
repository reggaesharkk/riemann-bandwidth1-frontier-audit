# WP84 — direct smooth-taper proper-power absorption

**Audit branch:** `codex/wp84-direct-smooth-taper-20261103`
**Frozen reference:** `7f3394c5655238b1e9736f91233d0bcc4c49fd43`
**Scope:** proper-prime-power part of the finite Weil/Gabor prime matrix only.

This additive note proves a source-normalized Schatten-4 perturbation bound for
the proper-power summand of the actual smooth-taper finite matrix. It does not
replace the source taper by a sharp box. It makes no assertion about the
ordinary-prime aggregate, the raw fourth-trace difference, the zero-density
coefficient, or RH.

## Decisions

| Gate | Decision | Scope |
|---|---|---|
| `SMOOTH_ENTRY_IDENTITY` | **EXACT** | Exact prime-side prime-power decomposition of the finite source matrix, including both carriers and zero-extension boundary compression. |
| `SMOOTH_LARGE_SIEVE_TRANSFER` | **PROVED** | Full cutoff (n\le e^L); each sign branch separately; all consecutive sections of length (m\ge\eta e^L L). |
| `SMOOTH_SECOND_TRACE` | **PROVED** | Full displacement matrix, with Parseval used to sum the displacements. |
| `SMOOTH_OPERATOR_BOUND` | **PROVED** | Proper-power absolute coefficient mass and a compression row-sum/operator estimate. |
| `SMOOTH_SCHATTEN_ABSORPTION` | **PROVED** | Under the explicit source taper and section hypotheses below. |
| `FULL_WEIL_INTERFACE` | **ESTABLISHED_FOR_PROPER_POWERS** | The proper-power term is an exact summand of the source prime-side integral; all other terms, including the zero-tail correction, remain in the complementary matrix. |

The claim proved is
\[
 \tau_I(Q_I^2)\ll_{\eta,a_0,B}L^{-2},\qquad
 \|Q_I\|_{\rm op}\ll_{a_0,B}1,
\]
and hence
\[
 \tau_I(Q_I^4)\ll_{\eta,a_0,B}L^{-2},\qquad
 \left|\tau_I((A_I+Q_I)^4)^{1/4}-
             \tau_I(A_I^4)^{1/4}\right|
      \ll_{\eta,a_0,B}L^{-1/2}.
\]
Here \(\tau_I=m^{-1}\operatorname{Tr}\), and no bound on either full
fourth moment is assumed. This is a fourth-root perturbation statement; it
does not by itself give an \(o(1)\) raw fourth-trace difference.

## 1. Frozen source and hypotheses

The source is Alpöge–Furman, arXiv:2608.13637v2, §§2.1–2.3, equations
(2.6)–(2.11) and Lemma 2.1. It sets
\[
 L=\log(T/(2\pi)),\quad X=e^L=T/(2\pi),\quad h=2\pi/L,
 \quad d=\lfloor TL/(2\pi)\rfloor=\lfloor e^LL\rfloor,
 \quad \alpha_k=T+hk.
\]
For one of its even windows \(\psi\), and its fixed smooth step \(\chi\),
the actual taper is
\[
 \phi_L(x)=\chi(L/2+x)\chi(L/2-x)\sqrt{\psi(x/L)}.
\]
It is real and even, \(0\le\phi_L\le1\), supported on
\([-L/2,L/2]\), and belongs to \(C_c^2\). For the indicator window its
edge ramps have fixed \(O_\chi(1)\) width; for the Montgomery–Taylor window
the interior profile also varies with \(x/L\). The source normalization is
\[
 a=a_\phi(T)=L^{-1}\int_{\mathbb R}\phi_L(x)^2dx
   =\int_{-1/2}^{1/2}\psi(s)ds+O_\chi(L^{-1}).
\]
For either source window, \(a\ge a_0\) eventually; we use the weaker
explicit eventual hypothesis \(a\ge1/2\). Indeed the limiting integral is
1 for \(\psi_0\), and \(\sqrt2\sin(1/\sqrt2)>1/2\) for \(\psi_{MT}\);
the stated \(O_\chi(L^{-1})\) error then gives the eventual bound.

The estimates below require only the following source-compatible hypotheses:
\(\phi_L\) real and even, supported in \([-L/2,L/2]\) (or translated
there; a common translation changes Fourier phases but not these bounds),
\(\|\phi_L\|_\infty\le B\), \(a=L^{-1}\|\phi_L\|_2^2\ge a_0>0\),
full cutoff \(n\le X=e^L\), and a consecutive section \(I\) of integer
rows with
\[
 I=\{k_0,k_0+1,\ldots,k_0+m-1\}\subseteq\{0,1,\ldots,d-1\},
 |I|=m\ge\eta e^L L,
 \qquad 0<\eta\le1.
\]
The exact Weil identity also needs the source's smoothness and support
conditions; the norm estimates themselves do not use derivatives of \(\phi\).
The argument therefore covers general real even source-admissible tapers,
not just a linear ramp. We do not claim the source matrix identity for a
non-even taper, since the source uses the non-conjugated Fourier product
specific to its even real window.

## 2. Exact smooth overlap and finite matrix entries

Extend functions by zero outside \([-L/2,L/2]\). For \(0\le y\le L\),
put
\[
 f_y(x)=\phi_L(x-y/2)\phi_L(x+y/2),\qquad
 G_r(y)=\frac1{aL}\int_{\mathbb R}f_y(x)e^{ihrx}dx
 \quad(r\in\mathbb Z).
\]
This is the actual smooth overlap coefficient. It is not the sharp overlap
\(1-y/L\) or its Fourier coefficient.

Let \(e_k(x)=L^{-1/2}e^{ihkx}\) on the length-\(L\) interval, and let
\(P_d\) project onto the source modes \(0\le k<d\). Define the non-wrapping
translation \((U_y^+g)(x)=g(x+y)\), using the zero extension. Set
\[
 B_y=P_dM_{\phi_L}U_y^+M_{\phi_L}P_d.
\]
For \(l=k+r\), changing variables to the overlap centre gives, exactly,
\[
\begin{aligned}
 \langle e_k,B_y e_{k+r}\rangle
 &=\frac1L\int\phi_L(x-y/2)\phi_L(x+y/2)
        e^{ihrx}dx\ e^{ih(k+r/2)y}\\
 &=aG_r(y)e^{ih(k+r/2)y}.
\end{aligned}
\]
There is no periodic shift: the integral is over the literal intersection of
the two translated supports. Since \(f_y\) is real and even,
\(G_r(y)=G_{-r}(y)\in\mathbb R\). The adjoint entry at the same matrix
position is
\[
 (B_y^*)_{k,k+r}=aG_r(y)e^{-ih(k+r/2)y}.
\]

To compare this with the exact source matrix, let
\[
 A_r(y)=\int f_y(x)\cos(rhx)dx=aL G_r(y).
\]
Using \(\widehat\phi(\xi)=\int\phi(u)e^{-iu\xi}du\), Fourier inversion
in the \(\tau\)-integral gives
\[
\begin{aligned}
 &\int_{\mathbb R}\widehat\phi(\tau-\alpha_k)
       \widehat\phi(\tau-\alpha_l)e^{i\tau y}d\tau\\
 &=2\pi e^{i(\alpha_k+\alpha_l)y/2}
   \int_{\mathbb R}\phi(x-y/2)\phi(x+y/2)
                    e^{i(\alpha_k-\alpha_l)x}dx.
\end{aligned}
\]
Here the delta constraint is \(u+v=y\); the change of variables is
\(u=x+y/2,v=-x+y/2\), and evenness changes \(\phi(v)\) to
\(\phi(x-y/2)\). Since \(f_y\) is even, the last integral is
\(A_{k-l}(y)\). Taking the real part gives the exact source block
\[
 C(y)_{kl}=\frac{2\pi}{aL^2}A_{k-l}(y)
             \cos\!\left(\frac{\alpha_k+\alpha_l}{2}y\right).
\]
Define the complex branch \(C^+(y)_{kl}=\frac{2\pi}{aL^2}A_{k-l}(y)
e^{i(\alpha_k+\alpha_l)y/2}\). Because \(A_r=A_{-r}\),
\[
 C^+(y)=\frac{2\pi}{aL}e^{iTy}B_y,
 \qquad C(y)=\tfrac12(C^+(y)+C^+(y)^*).
\]
Both equalities are entrywise exact, including at the ends of the Fourier
band. They retain the smooth \(A_r(y)\), all source normalization factors,
and the carrier \(e^{iTy}\).

For the source prime polynomial
\[
 P_X(\tau)=-\frac1\pi\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
                          \cos(\tau\log n),
\]
the exact prime-side matrix is \(-\pi^{-1}\sum_{n\le X}
\Lambda(n)n^{-1/2}C(\log n)\). Thus its proper-power summand is
\[
 Q=\sum_{\substack{p^e\le X\\e\ge2}}
       \gamma_{p^e}\left(e^{iT y_n}B_{y_n}
                         +e^{-iT y_n}B_{y_n}^*\right),
 \quad y_n=\log n,\quad
 \gamma_n=-\frac{\Lambda(n)}{aL\sqrt n}.
\]
In an individual row entry the effective scalar coefficient is
\[
 \lambda_n=a\gamma_n=-\frac{\Lambda(n)}{L\sqrt n},
\]
and, for \(l=k+r\),
\[
 Q_{k,k+r}=\sum_{p^e\le X,e\ge2}\lambda_nG_r(y_n)
 \left[e^{iTy_n}e^{ih(k+r/2)y_n}
       +e^{-iTy_n}e^{-ih(k+r/2)y_n}\right].
\]
This establishes the requested exact source entry identity and keeps the
positive and negative branches separate. A selected section is just the
principal compression \(E_IQE_I\), where the section is an actual
consecutive principal submatrix of the finite source index set
\(\{0,\ldots,d-1\}\); it adds no boundary or wrap term. The estimates are
uniform in its valid start row and endpoints.
The original source Weil matrix is dense in the displacement variable. If a
WP84 consumer imposes the additional hard band \(|k-l|\le R\), it is the
literal entry mask of this same identity; no new smooth-overlap formula is
introduced. The full-matrix theorem below covers the source matrix, and the
explicit hard-band bounds below cover this masked variant.

## 3. Bounds for the smooth coefficients

Cauchy–Schwarz with the exact normalization gives
\[
 |G_r(y)|\le\frac{\|\phi_L(\cdot-y/2)\|_2
                      \|\phi_L(\cdot+y/2)\|_2}{aL}=1.
\]
This holds for every integer \(r\) and every \(0\le y\le L\).
Parseval for the Fourier series on the length-\(L\) interval gives
\[
 \sum_{r\in\mathbb Z}|G_r(y)|^2
 =\frac1{a^2L}\int|f_y(x)|^2dx
 \le\frac{B^2}{a}.
\]
Indeed \(|\phi(x-y/2)|^2\le B^2\), while the integral of the other
translated square is at most \(aL\). For the source taper \(B=1\), the
right side is \(1/a\). These are bounds on the smooth overlap itself; no
comparison with a sharp overlap is used.

## 4. Full-cutoff separated-frequency transfer

Write \(u_n=\log n/L\). For distinct integers \(4\le m<n\le N:=\lfloor
e^L\rfloor\),
\[
 u_n-u_m\ge\frac{\log(1+1/N)}L
             \ge\frac1{(N+1)L}.
\]
The circular wrap gap for the proper-power set is at least
\(\log4/L\): its least frequency is at least \(\log4/L\), and its greatest
frequency is at most \(1\). If \(N=X\) is an integer, the endpoint source
frequency \(u_X=1\) aliases to zero modulo one, but the least source
frequency remains at least \(\log4/L\); there is no \(n=1\) proper-power
term. Thus all distinct proper-power points \(u_n\pmod1\) have circular
separation
\[
 \delta\ge\frac1{(N+1)L}.
\]
The negative branch points \(-u_n\pmod1\) have the same separation. We do
not apply a separation claim to their union: cross-branch near-collisions,
including the exact positive/negative collision when \(u_X=1\), are handled
by the later inequality \(|S^++S^-|^2\le2|S^+|^2+2|S^-|^2\).

The applicable Montgomery–Vaughan large-sieve inequality is: if points
\(x_j\pmod1\) have circular separation at least \(\delta\), then for
arbitrary complex \(b_j\) and any \(m\) consecutive integers \(k\),
\[
 \sum_{k\in I}\left|\sum_j b_je^{2\pi ikx_j}\right|^2
       \le (m+\delta^{-1})\sum_j|b_j|^2.
\]
This is the direct discrete separated-point form of Theorem 1 of
Montgomery–Vaughan, *The Large Sieve*, Mathematika 20 (1973), 119–134;
arbitrary starting row is absorbed into the coefficients by unit phases.
It allows arbitrary complex coefficients, so it applies after including
\(G_r(y_n)\), \(e^{\pm iTy_n}\), and \(e^{\pm i\pi r u_n}\).

Since \(m\ge\eta e^LL\),
\[
 K:=1+\delta^{-1}/m
 \le1+\frac{N+1}{\eta e^L}
 \le1+\frac2\eta.
\]
The bound is independent of \(T\), the starting row, the section endpoint,
and whether \(X\) is an integer. This checks the source grid including the
full cutoff and modulo-one wrap.

## 5. Full-matrix second trace

Let \(Q_I=E_IQE_I\), and \(\tau_I=m^{-1}\operatorname{Tr}\). Group its
entries by displacement \(r=l-k\). For each fixed \(r\), the entry is a
sum of the positive and negative exponential polynomials displayed in
Section 2. The row set \(\{k\in I:k+r\in I\}\) is a subset of \(I\), so
the nonnegative sum can be bounded by the full-\(I\) large-sieve sum.
For the two branches use
\[
 |S^+_{r,k}+S^-_{r,k}|^2\le2|S^+_{r,k}|^2+2|S^-_{r,k}|^2,
\]
paying exactly a factor 4 after the two separate large-sieve applications.
There is no assumption that positive and negative frequencies are mutually
separated.

Also
\[
 \sum_{p^e\le X,e\ge2}|\lambda_{p^e}|^2
 =\frac1{L^2}\sum_p\frac{(\log p)^2}{p(p-1)}
 \le\frac{64}{L^2}.
\]
For the last inequality, \(\log x\le4x^{1/4}\),
\(p(p-1)\ge p^2/2\), and \(\sum_{n\ge2}n^{-3/2}\le2\) suffice.
Therefore, summing over all displacements and then using the smooth
Parseval bound,
\[
\begin{aligned}
 \tau_I(Q_I^2)
 &\le 4K\sum_{p^e\le X,e\ge2}|\lambda_{p^e}|^2
                                  \sum_{r\in\mathbb Z}|G_r(y_{p^e})|^2\\
 &\le \frac{256B^2}{aL^2}\left(1+\frac2\eta\right).
\end{aligned}
\]
In the first line the inner sum is understood termwise in \(p^e\).
This estimates the full source compression, whose displacement set has
\(2m-1\) possible diagonals; it does not pay that crude factor. For the
literal hard displacement mask \(Q_R=1_{|k-l|\le R}\circ Q\), discard
Parseval and retain the exact \(2R+1\) diagonals instead. The same
fixed-displacement large-sieve estimate gives
\[
 \tau_I(Q_{R,I}^2)\le
   \frac{256(2R+1)}{L^2}\left(1+\frac2\eta\right).
\]
This pays the two carrier branches and every retained diagonal explicitly.

## 6. Independent operator-norm estimate

Since \(\|B_y\|_{op}\le\|\phi_L\|_\infty^2\le B^2\),
\[
 \|Q_I\|_{op}\le 2B^2 M_1,
 \qquad
 M_1=\frac1{aL}\sum_{p^e\le X,e\ge2}\frac{\log p}{p^{e/2}}.
\]
Extending the exponent sum and using
\(1-p^{-1/2}\ge1-2^{-1/2}=:c_0\),
\[
 M_1\le\frac1{ac_0L}\sum_{p\le\sqrt X}\frac{\log p}{p}.
\]
The elementary Chebyshev bound \(\theta(x)=\sum_{p\le x}\log p\le
4(\log2)x\), followed by partial summation, gives
\[
 \sum_{p\le x}\frac{\log p}{p}
 \le4(\log2)(1+\log x).
\]
Thus, for \(L\ge1\),
\[
 M_1\le\frac{6\log2}{ac_0},\qquad
 \|Q_I\|_{op}\le\frac{12B^2\log2}{ac_0}.
\]
For the actual taper \(B=1,a\ge1/2\), this gives the explicit
\(T\)-independent bound \(24\log2/(1-2^{-1/2})<56.8\). It holds for all
principal sections by compression and pays the full prime-power cutoff.

For the hard-band mask, the full-shift operator norm does not automatically
pass through a Schur band mask. Instead use the source entry formula,
\(|G_r|\le1\), and a row sum. Since
\[
 S_1:=\sum_{p^e\le X,e\ge2}|\lambda_{p^e}|
 \le\frac{6\log2}{1-2^{-1/2}}\quad(L\ge1),
\]
each masked entry is at most \(2S_1\), and a row has at most \(2R+1\)
entries. Hermitianity and the row-sum bound give
\[
 \|Q_{R,I}\|_{op}\le
 \frac{12(2R+1)\log2}{1-2^{-1/2}}.
\]
Thus the finite hard-band proper-power matrix also has a uniform operator
bound, with its explicit R dependence shown.

## 7. Schatten conclusion and exact Weil interface

The compressed \(Q_I\) is Hermitian. Hence
\[
 \tau_I(Q_I^4)\le\|Q_I\|_{op}^2\tau_I(Q_I^2)
 \le\frac{256B^2}{aL^2}\left(1+\frac2\eta\right)
       \left(\frac{12B^2\log2}{ac_0}\right)^2.
\]
For fixed \(a\ge a_0>0,B,\eta\), this is \(O(L^{-2})\).
For the hard-band operator the explicit bound is
\[
 \tau_I(Q_{R,I}^4)\le
 \left(\frac{12(2R+1)\log2}{c_0}\right)^2
 \frac{256(2R+1)}{L^2}\left(1+\frac2\eta\right),
\]
so its normalized fourth-root contribution is \(O_{R,\eta}(L^{-1/2})\)
as well.
The normalized Schatten-4 triangle inequality gives for every Hermitian
\(A_I\),
\[
 \left|\tau_I((A_I+Q_I)^4)^{1/4}-
             \tau_I(A_I^4)^{1/4}\right|
 \le\tau_I(Q_I^4)^{1/4}=O(L^{-1/2}).
\]
This is noncircular: no full fourth-moment bound is used.

At source level, equations (2.10)–(2.11) state that
\(\widetilde G+\widetilde E\) equals the finite prime-side integral matrix.
The prime polynomial has the exact disjoint decomposition into ordinary
primes and proper powers. The formula above is exactly the proper-power
summand of that integral matrix on the original finite band. For
\(\widetilde G\) itself, put the remaining prime terms, \(\mu\), \(\Pi_X\),
and \(-\widetilde E\) into \(A\). The source separately proves the tail
trace-norm estimate for \(\widetilde E\); no tail is being silently
identified with a prime-power term. No conclusion here bounds the ordinary
prime part or its fourth moment.

## 8. Hostile checks and limitations

The exact regression checks in `tests/test_wp84_direct_smooth_power_absorption.py`
and `src/wp84_direct_smooth_power_absorption.py` verify the normalization
ledger, both branches, the full-cutoff circular spacing bound on endpoint
examples, the section-length factor, and smooth-vs-sharp overlap discrepancies.
For the even compactly supported quintic smoothstep taper, at
\(y=L-\varepsilon\) the smooth overlap is
\[
 \varepsilon\int_0^1g((\varepsilon/w)t)g((\varepsilon/w)(1-t))dt,
 \quad g(t)=10t^3-15t^4+6t^5,
\]
not the sharp-box overlap \(\varepsilon\). At \(\varepsilon/w=1/10\),
the exact rational test finds a strict, large discrepancy. This is a
negative control against replacing \(G_r\) by sharp coefficients. This
quintic function is a \(C^2\) diagnostic, not a claim about the source's
unspecified fixed \(\chi\). The source class also permits an explicit true
\(C^\infty\) step
\[
 E(t)=\begin{cases}e^{-1/t},&t>0,\\0,&t\le0,\end{cases}\qquad
 \chi_*(t)=\frac{E(t)}{E(t)+E(1-t)}\quad(0<t<1),
\]
extended by 0 and 1 outside \((0,1)\). At \(t\le1/10\),
\(\chi_*(t)\le e^{-1/t+1/(1-t)}\le e^{-80/9}<10^{-3}\), since the
exact rational partial sum \(\sum_{j=0}^{10}8^j/j!=3830591/1575>1000\)
shows \(e^8>1000\), and \(80/9>8\). For \(L\) large enough that the
opposite step factors equal 1, this gives the rigorous endpoint estimate
\(A_0(L-1/10)/(1/10)\le10^{-6}\), whereas the sharp-box overlap ratio is
1. For the source's actual but unspecified choice of \(\chi\), smooth
flatness at 0 still implies this ratio tends to zero as \(\varepsilon\to0\);
the exact numerical rate depends on that choice and is not asserted here.

Additional cases covered in the proof are arbitrary real even bounded
profiles with the same norm lower bound, arbitrary section starts, endpoint
rows, modulo-one alias at \(n=X\), distinct positive and negative branches,
and all displacements without circular compression. Smoothness matters only
for matching the original Weil test-family interface, not for the operator
inequalities. If \(a\) is not bounded below, the displayed constants
degrade as shown and no uniform absorption follows from this argument.

The result is not a bound for the unweighted ordinary-prime contribution,
not an estimate on \(\tau((A+Q)^4)-\tau(A^4)\), and not an R400 connected
aggregate theorem. The previously recorded physical positive atom and
physical/geometric kernel discrepancy remain in the frozen history and are
untouched.

## 9. Reproduction

From the repository root run:

```powershell
python -m unittest tests.test_wp84_direct_smooth_power_absorption
python -O -m unittest tests.test_wp84_direct_smooth_power_absorption
python -OO -m unittest tests.test_wp84_direct_smooth_power_absorption
python src/wp84_direct_smooth_power_absorption.py
```

The evidence directory records the frozen source hashes, the dependency map,
all three test outputs, the checker output, and the SHA-256 manifest. For
each artifact, the manifest records both the exact worktree-byte hash and the
LF-normalized Git text hash, since this checkout uses CRLF conversion. The
manifest sidecar hashes the manifest itself.

## Source references

- Alpöge–Furman, *More than two thirds of the zeros of the Riemann zeta
  function are simple and on the critical line*, arXiv:2608.13637v2,
  §§2.1–2.3, equations (2.6)–(2.11), Lemma 2.1:
  <https://arxiv.org/html/2608.13637v2>.
- H. L. Montgomery and R. C. Vaughan, *The Large Sieve*, Mathematika 20
  (1973), 119–134, Theorem 1 (separated-point discrete large sieve).
- The frozen local derivation of the prime-side overlap normalization is
  `notes/WP84_BOUNDED_RESOLVENT_CONSUMER.md` at the reference commit.
