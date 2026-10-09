# Fixed-pole analyticity and the trace-grid transfer

**Decision C.** The actual fixed-pole response has a certified simultaneous
polystrip, and its individual high-height Bohr coefficients decay
exponentially in a source-derived height. This does not yet give the
p-summed weighted trace-grid estimate: fixed-contour Parseval bounds depend
on the signed contour, and the number of sign orthants grows with the
retained prime pool. A many-prime exact periodic-alias family remains in the
aggregate problem. This is an unresolved contribution, not evidence that its
actual signed contribution is nonzero.

The result concerns only the frozen cylinder
\[
\Psi_R=s_{32,R,U}-s_{32,R,\delta},\quad
K=32,\quad\delta=1/100000,\quad a=131/200,
\]
with the natural cutoff \(N=\lfloor X e^{-\sqrt{\log X}}\rfloor\), fixed
\(R\) followed by \(T\to\infty\), and all prime powers grouped at their base.
Strict \(>79\%\) remains OPEN.

## Reconciliation of the preceding audit counts

The preceding certificate lists **20 named hostile-mutation scenarios**.
Its replay performs **21 hostile-inference evidence checks**; those checks
verify that the certificate rejects invalid inferences and do not mutate
source files at runtime. It also has eight rational-arithmetic assertion
statements, six source-hash comparisons, and seven certificate/schema/field
consistency assertions. The earlier note's count of 19 was a typo; the prior
final report's 21 referred to replay checks.

While reconstructing the actual current coefficients, I also found and
corrected a separate explanatory error in the prior certificate: the source
envelope for the first-order coefficient l1 mass is not O(1). Indeed,
\[
\sum_{p\le N}\frac{\log p}{L\sqrt p}
 \sim \frac{2\sqrt N}{L}\longrightarrow\infty
\]
by the prime number theorem and partial summation, since
\(\log N=L-\sqrt L+o(1)\). This invalidates that triangle-bound claim; it
does not imply that the signed A1 sum diverges.

## Complex perturbation of one grouped prime base

Write the real-phase q-base block as a Laurent polynomial
\[
G_q(z_q)=\sum_{1\le j\le J_q}
 \big(A_{q,j}z_q^j+A_{q,-j}z_q^{-j}\big),\qquad
J_q=\max\{j:q^j\le N\}.
\]
All powers use the same \(z_q\). Fourier coefficient extraction from the
real-phase block and the source bound give
\[
\|A_{q,\pm j}\|_{\rm op}\le \frac{4\log q}{Lq^{j/2}}.
\]
For \(z_q=e^{i\theta_q+s}\), \(|s|\le\rho\), subtracting the real-phase
value gives the rigorous grouped bound
\[
B_q(\rho)=\frac{8\log q}{L}
 \sum_{j=1}^{J_q}q^{-j/2}(e^{j\rho}-1),
\qquad \|\Delta_q(s)\|_{\rm op}\le B_q(\rho).
\]
This includes every retained proper power and uses no independent phase for
any \(q^j\).

For the pole \(z=c+ia\), \(c=3142/2415\), and a Hermitian real-phase base
state H, \(\|R(H,z)\|\le1/a\). If the total complex perturbation satisfies
\(\|\Delta\|\le\theta a\), \(\theta=1/2\), then
\[
R(H+\Delta,z)=(I+R(H,z)\Delta)^{-1}R(H,z),\qquad
\|R(H+\Delta,z)\|\le\frac1{a(1-\theta)}=\frac{400}{131}.
\]
This follows from the convergent Neumann series. The same estimate is used
at the conjugate pole. The Hermitian \(1/a\) bound is not used after
complexification.

## Explicit bounds for the holomorphic responses

For \(0<\eta\le1/4\), put \(\rho_q=\eta\log q\). Extending the finite
proper-power sum to infinity and integrating the exponential difference
gives
\[
B_q(\eta\log q)
 \le \frac{8\eta(\log q)^2}{L}
       \frac{q^{-1/4}}{(1-q^{-1/4})^2}
 \le \frac{128\eta}{L}.
\]
The last inequality is exact: with \(u=(\log q)/4\),
\((\log q)^2q^{-1/4}/(1-q^{-1/4})^2
=16(u/(e^u-1))^2\le16\).

Thus a support set S admits simultaneous radii
\[
\rho_q=\eta_T(S)\log q,\qquad
\eta_T(S)=\min\left(\frac14,\frac{131L}{51200|S|}\right),
\]
because \(\sum_{q\in S}B_q(\rho_q)\le131/400=\theta a\). In particular,
for one coordinate and \(L\ge100\), \(\rho_q=(\log q)/4\) is valid:
\(B_q\le32/L\le8/25<131/400\).

Here are explicit uniform response bounds on that domain. The consumer is
\(Q=q(U_C)\), \(U_C=I+2iaR\), with source enclosures
\(|q_1|,|q_2|\le221/500\), \(|q_3|\le317/500\). From the exact Cayley
polynomial, \(|q_0|<22\). The input map has real norm at most 6; its
complexification is bounded by \(6\sqrt2<9\). With
\[
u_*=5,\quad d_1=72/a,\quad d_2=2592/a^2,
\]
the Neumann resolvent estimate gives \(\|U_C\|\le u_*\),
\(\|D_xU_C\|\le d_1\), and \(\|D_x^2U_C\|\le d_2\). Define the exact
rational constants
\[
Q_*=22+\sum_{j=1}^3|q_j|5^j,
\quad
Q_1=d_1\sum_{j=1}^3j|q_j|5^{j-1},
\]
\[
Q_2=\sum_{j=1}^3|q_j|
\left(j5^{j-1}d_2+j(j-1)5^{j-2}d_1^2\right),
\quad
M_{1,R}=4Q_*Q_1,\quad
M_{2,R}=4(Q_1^2+Q_*Q_2).
\]
Their exact rational values are in the certificate. They bound the gradient
and Hessian response norms for \(\Psi_R\), uniformly in the Gaussian
variables in the hybrid state. The scalar norm-square is continued by its
real-analytic bilinear polarization; no Hermitian norm is asserted for a
complexified state.

Multivariable Cauchy on the coordinates in the support of \(\nu\) now gives
\[
\|c_{j,p,\nu}\|_{L^2(g)}
\le M_{j,R}e^{-\Gamma_T(\nu)},\quad j=1,2,
\]
where
\[
\Gamma_T(\nu)=\sup_{\rho_q\ge0,\ \sum_{q\in S}B_q(\rho_q)\le\theta a}
                  \sum_{q\in S}|\nu_q|\rho_q.
\]
The optimizer is characterized exactly by the KKT equations
\(|\nu_q|=\mu B_q'(\rho_q)\) on the nonzero coordinates and
\(\sum B_q(\rho_q)=\theta a\), with \(\mu>0\). The feasible explicit choice
above proves the height bound
\[
\Gamma_T(\nu)\ge
\min\left(\frac14,\frac{131L}{51200|S|}\right)
h(\nu),\qquad
h(\nu)=\sum_q|\nu_q|\log q.
\]
That is, the right side is the displayed minimum multiplied by \(h(\nu)\).
This is a simultaneous perturbation estimate; it does not multiply
independent one-variable strips.

## Two alias tests

For the earlier p-adic L2 counterexample, take p=2, current exponent 1, and
\(\nu_3=253891,\nu_5=-173308\). At T=7800, L>6 and |S|=2, so
\(\eta_T(S)\ge393/51200\). Since \(\log3,\log5>1\),
\(\Gamma_T(\nu)>3279\). Therefore a response coefficient at this index,
if present, is at most
\[
M_{1,R}2^{-3279}\quad\hbox{or}\quad M_{2,R}2^{-3279},
\]
using \(e>2\). This is a bound on a hypothetical actual coefficient; it
does not claim the adversarial monomial occurs in the response. The exact
rational constants satisfy \(M_{1,R}<10^7\), \(M_{2,R}<10^9\), and
\(2^{3279}>10^{981}\); consequently these coefficient bounds are respectively
below \(10^{-974}\) and \(10^{-972}\).

Many small exponents also produce exact aliases. For each y let
\[
X_y=2\prod_{\substack{q\le y\\q\ {\rm prime},\ q\ne2}}q,\qquad
T_y=2\pi X_y,\qquad \nu_q=1\ (q\ne2,\ q\le y).
\]
Then max \(|\nu_q|=1\) and
\[
\lambda_\nu+\log2=\log X_y=L_y,
\]
an exact \(m=1\) periodic alias. For y=31, the ten support primes are
3,5,7,11,13,17,19,23,29,31. The exact integer \(X_{31}\) obeys
\(1323\cdot32<X_{31}<2^{38}\); \(e<3\), \(e^3<21\), and \(\log2<1\)
give \(X_{31}e^{-\sqrt{\log X_{31}}}>32\), hence all ten primes are under
the natural cutoff. As y grows, PNT gives \(L_y\sim y\) and
\(|S_y|/L_y\to0\). Consequently the certified height estimate yields
\(\Gamma_{T_y}(\nu)\ge(L_y-\log2)/4\) eventually. The kernel for this
coefficient is exactly one, but its individual analytic coefficient bound
decays exponentially. Neither that bound nor this exact alias constructs a
nonzero response coefficient or controls the sum over all aliases.

## The weighted norm that Parseval actually proves

For any one fixed signed contour vector s satisfying
\(\sum_qB_q(|s_q|)\le\theta a\), shift the selected torus coordinates to
\(z_q=e^{i\theta_q+s_q}\). Parseval gives the valid source-response estimate
\[
\sum_\nu e^{2\sum_qs_q\nu_q}
 E_g\|c_{j,p,\nu,g}\|^2\le M_{j,R}^2,\qquad j=1,2.
\]
This is a genuine weighted L2 statement. It is **not** the absolute-height
weight \(e^{2\Gamma_T(\nu)}\). To pass to absolute values one must split by
sign orthants; summing those bounds costs \(2^{|S|}\), with |S| growing with
the retained prime pool. Pointwise Cauchy bounds alone do not prove a global
weighted l2 response norm.

## A1, A2, and remaining aliases

With exact current coefficients \(\gamma_{p,a,\epsilon}\), the A1
trace-grid expression has frequencies
\(\lambda_\nu+\epsilon a\log p\), and A2 has
\(\lambda_\nu+(\epsilon a+\epsilon'b)\log p\), excluding the opposite
equal-power covariance diagonal. A fixed-contour Cauchy bound for each
orthant is \(M_{1,R}\) or \(M_{2,R}\) times the square root of its weighted
kernel mass, further multiplied by the exact current coefficient or
coefficient product. The certificate records these formulas.

- **Existing degree 1/2 results:** exact equal-power covariance diagonal
  and ordinary covariance normalization in their original scope.
- **New analytic weight:** individual high-height response coefficients,
  including the two displayed alias examples.
- **Still open:** the p-summed A1 and A2 weighted dual masses over current
  powers, sign orthants, masks, periodic aliases and near aliases. A
  fixed-p estimate does not settle the p-sum.
- **Exact m=0:** excluded for a nonzero current p-adic exponent by unique
  factorization.
- **m nonzero:** possible; X need not be irrational. The primorial family
  above realizes m=1.
- **Near aliases:** the kernel may be order one in an O(1/T) window. No
  source-matched count or signed estimate pays the whole family.
- **Far frequencies:** the geometric kernel decay remains valid, but its
  sum against the actual response coefficients has not been bounded.

Conjugation pairs produce \(2\operatorname{Re}(\cdot)\), not zero.
Unequal current powers retain their nonzero p-adic frequencies. The common
trace index and carrier phase remain in the kernel, and the U-minus-delta
difference supplies no proved fixed sign. No new signed saving is obtained.

Even if this particular fixed-R cylinder comparison were proved, it would
establish only the expectation comparison for \(\Psi_R\); it would not imply
full original-scale prime-field Gaussian convergence or alter prior
fifth-moment/nonexact-correlation audits.

The single next theorem is a source-matched p-summed signed or weighted-l2
estimate for A1 and A2 on the common trace-index path, with the actual
response coefficients, grouped current weights, all sign orthants, and
near and periodic aliases. The fixed-contour Parseval estimates above do
not imply that theorem. Thus the dependent-phase law and strict >79 remain
OPEN.

## Reproduction

    python src/wp84_analytic_response_trace_grid_transfer.py
    python src/wp84_analytic_response_trace_grid_transfer_replay.py

The replay independently reconstructs the rational constants and cutoff
checks, verifies all ten source hashes, and rejects 22 mutated-certificate
tests. It does not treat the exact-alias character as an actual response
coefficient.
