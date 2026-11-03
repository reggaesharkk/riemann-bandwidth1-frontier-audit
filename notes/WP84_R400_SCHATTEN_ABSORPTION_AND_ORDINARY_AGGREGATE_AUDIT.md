# WP84 — R400 Schatten absorption and physical ordinary-prime aggregate

Base commit: b1ff152df352216aa44c9a2535f04306a39df859
Audit branch: codex/wp84-r400-schatten-ordinary-aggregate-20261103

| Gate | Decision |
|---|---|
| PROPER_POWER_SCHATTEN_ABSORPTION | PROVED |
| ORDINARY_PHYSICAL_CONNECTED_AGGREGATE | OPEN |
| R400_CONSUMER | OPEN |

This is an additive local audit. Earlier commits, source files, evidence,
counterexamples, and the positive physical atom remain unchanged. Nothing is
merged, pushed, published, or presented as an unconditional theorem.

## 1. Exact finite-T matrix and source normalization

Set
\[
L=\log(T/(2\pi)),\quad h=2\pi/L,\quad
d=\lfloor TL/(2\pi)\rfloor,\quad
N=\lfloor e^{L-\sqrt L}\rfloor,\quad
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n}.
\]
The prime-source matrix is the centered prime-power contribution after the
scalar background split \(H_T=s_0(T)I+P_T\). The scalar \(s_0(T)I\) is
unchanged in the ordinary/proper-power split.

For \(S\) equal to either ordinary primes \(p\le N\) or proper powers
\(p^e\le N,\ e\ge2\), define
\[
F^S_k=\sum_{n\in S}c_ne^{iT\log n}e^{2\pi i k\log(n)/L},\quad
\alpha^S_k=\Im F^S_k,
\]
\[
\beta^S_k=2\Re\sum_{n\in S}c_n(1-\log(n)/L)
e^{iT\log n}e^{2\pi i k\log(n)/L}.
\]
For \(R=400\), let
\[
(J_R)_{ij}=\begin{cases}1/(\pi(j-i)),&0<|i-j|\le R,\\0,&\text{otherwise.}\end{cases}
\]
The exact finite-T full-lattice source matrix is
\[
H^S_{T,R}=M_{\beta^S}+[M_{\alpha^S},J_R],
\quad
(H^S)_{ii}=\beta^S_i,\quad
(H^S)_{ij}=\frac{\alpha^S_i-\alpha^S_j}{\pi(j-i)}
\quad(0<|i-j|\le R),
\]
and all other off-diagonal entries are zero. The prime-source split on the
one common section is exactly
\[
P_{400,I}=A_{400,I}+Q_{400,I},\qquad
A_{400,I}=E_IH^{ord}_{T,400}E_I,\quad
Q_{400,I}=E_IH^{pow}_{T,400}E_I.
\]
Here \(E_I\) is the principal-section projection. Compression only restricts
entries; it introduces no circular wrap or continuum limit. The hard
displacement cutoff is already present in \(J_R\).

The entry identity follows directly from the two signed translations. For
one frequency \(u=\log n/L\), \(z=c_ne^{iT\log n}\), put
\(w_k=ze^{2\pi iku}\). The positive and negative Fourier intervals are
\([0,1-u]\) and \([u,1]\). Their diagonal sum is
\(2(1-u)\Re w_i\). For \(i\ne j\), their combined Fourier coefficient is
\((\Im w_i-\Im w_j)/(\pi(j-i))\). Linearity gives the displayed matrix for
every source sum. The independent Gaussian-rational checker evaluates the
direct two-translation integral and commutator formula on every entry of a
5-by-5 section, including diagonal and out-of-band entries.

The matrices are Hermitian since \(J_R^*=-J_R\) and
\([M_\alpha,J_R]^*=[M_\alpha,J_R]\).

## 2. Proper-power operator norm

Let
\[
M_1^{pow}=\sum_{p^e\le N,\ e\ge2}|c_{p^e}|,\qquad
M_2^{pow}=\sum_{p^e\le N,\ e\ge2}|c_{p^e}|^2.
\]
Using \(\Lambda(p^e)=\log p\) and extending the exponent sum,
\[
M_1^{pow}\le
\frac{1}{|a_\phi|L}
\sum_{p\le\sqrt N}\frac{\log p}{p(1-p^{-1/2})}=O(1).
\]
Indeed \(1-p^{-1/2}\ge1-2^{-1/2}\), and dyadic summation from
\(\sum_{p\le x}\log p=O(x)\) gives \(\sum_{p\le x}\log p/p=O(\log x)\).
The first absolute mass is bounded, not small.

Since \(\|\alpha^{pow}\|_\infty\le M_1^{pow}\),
\(\|\beta^{pow}\|_\infty\le2M_1^{pow}\), and the absolute row-sum estimate
gives \(\|J_{400}\|_{op}\le2H_{400}/\pi\), every section satisfies
\[
\|Q_{400,I}\|_{op}
\le 2M_1^{pow}(1+2H_{400}/\pi)=O_{400}(1).
\]
This is a source-valid \(\ell^1\) argument, independent of the fourth moment.

## 3. Source-grid transfer of proper-power square mass

The coefficient square mass obeys
\[
M_2^{pow}\le\frac{1}{|a_\phi|^2L^2}
\sum_p\frac{(\log p)^2}{p(p-1)}
\le\frac{64}{|a_\phi|^2L^2}.
\]
For the last inequality, \(\log x\le4x^{1/4}\),
\(p(p-1)\ge p^2/2\), and \(\sum_{n\ge2}n^{-3/2}\le2\) suffice. As
\(a_\phi(T)\to1\), eventually \(M_2^{pow}\le256L^{-2}\).

This coefficient estimate alone does not imply a matrix trace estimate.
Here the transfer is proved on the actual Fourier grid. Put \(u_n=\log n/L\).
For distinct integers \(2\le m<n\le N\),
\[
u_n-u_m\ge\frac{\log(1+1/N)}L\ge\frac{1}{(N+1)L}.
\]
The wrap gap is at least \(1/\sqrt L\), because \(u_n\le1-1/\sqrt L\).
Thus the distinct source frequencies have circular spacing
\(\delta\ge1/((N+1)L)\) for large \(T\). The dual Montgomery–Vaughan large
sieve gives, for every interval of \(m\) consecutive rows and any starting
row,
\[
\frac1m\sum_{k\in I}\left|\sum_n a_ne^{2\pi iku_n}\right|^2
\le(1+\delta^{-1}/m)\sum_n|a_n|^2.
\]
This is the dual of Theorem 1 in Montgomery–Vaughan, *The Large Sieve*;
the theorem permits arbitrary complex coefficients and points separated
modulo one. The start row is absorbed into unit phases. The \(\delta^{-1}\)
term pays for close frequencies and aliases; no diagonal-only estimate is
used. See [the author-hosted theorem](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf).

Every permitted good-endpoint section has \(m\ge d-2q\), where
\(q=\lfloor d/\sqrt L\rfloor\). Consequently
\[
\delta^{-1}/m\le\frac{(N+1)L}{d-2q}=O(e^{-\sqrt L})=o(1)
\]
uniformly over all such sections and all starting rows. Apply the inequality
to \(F^{pow}\), then to the beta field with coefficients
\(c_n(1-u_n)\); \(|\Im F|\le|F|\) and \(2|\Re G|\le2|G|\) yield
\[
\operatorname{avg}_I|\alpha^{pow}|^2\le(1+o(1))M_2^{pow},\quad
\operatorname{avg}_I|\beta^{pow}|^2\le4(1+o(1))M_2^{pow}.
\]

The exact finite-matrix trace is
\[
\tau_I(Q^2)=\operatorname{avg}_I(\beta_i^{pow})^2+
\frac{2}{\pi^2m}\sum_{r=1}^{400}\frac1{r^2}
\sum_{i,i+r\in I}(\alpha_i^{pow}-\alpha_{i+r}^{pow})^2.
\]
Using \((x-y)^2\le2x^2+2y^2\),
\[
\tau_I(Q^2)\le
\left(4+\frac8{\pi^2}\sum_{r=1}^{400}r^{-2}\right)
(1+\delta^{-1}/m)M_2^{pow}=O_{400}(L^{-2}),
\]
uniformly over every permitted section. This calculation transfers the
coefficient mass through the actual band entries, including close
frequencies and aliases.

The obstruction to a generic square-mass-to-operator implication is exact:
for integer \(L=n\), \(m=n^4\), and
\(Q=\operatorname{diag}(n,0,\ldots,0)\),
\(\tau(Q^2)=L^{-2}\) but \(\|Q\|_{op}=L\). The source \(\ell^1\) bound above
is the separate ingredient that excludes this concentration.

## 4. Schatten absorption without a fourth-moment assumption

For Hermitian \(Q\),
\[
\tau_I(Q^4)\le\|Q_{400,I}\|_{op}^2\tau_I(Q^2)=O_{400}(L^{-2}).
\]
The normalized Schatten triangle inequality gives
\[
\left|\tau_I((A+Q)^4)^{1/4}-\tau_I(A^4)^{1/4}\right|
\le\|Q\|_{4,\tau_I}
=O_{400}(L^{-1/2}).
\]
Neither \(\tau_I(A^4)\) nor \(\tau_I((A+Q)^4)\) is assumed bounded. The
root perturbation alone does not assert a raw fourth-moment difference
\(o(1)\); that follows if one side later has a bounded fourth root. This is
the noncircular proper-power closure proved here.

## 5. Replay of the positive proper-power atom

The independent exact parent replay preserves the source sequence
\[
T=2\pi p^5,\quad L=5\log p,\quad N=\lfloor e^{L-\sqrt L}\rfloor,
\quad (n_0,n_1,n_2,n_3)=(p,p^2,p^3,p^2),\quad
\epsilon=(+,-,+,-).
\]
For every prime \(p\ge5\), \(p^5e^{-\sqrt{5\log p}}>p^3\), so all four
entries lie below the actual cutoff. The signed logarithmic sum is zero,
and the coefficient product is
\[
+\frac{(\log p)^4}{a_\phi(T)^4L^4p^4}.
\]
The four signed source intervals in slot order are
\([0,4/5]\), \([2/5,1]\), \([0,2/5]\), and \([2/5,1]\).
The 48 labeled source/conjugate placements reduce to 24 unique rational
vectors. A new outward-rounded R400 interval replay certifies all 24
external overlaps above \(799/4000\); every placement has the same exact
row-cumulant lower bound
\[
\kappa_m\ge1-7(2/m)^2-12(2/m)^3-6(2/m)^4\ge384/625
\quad(m\ge10).
\]
At \(m=10\), the exact signed 26-term vector is \(e_1\). Thus this physical
atom is pointwise positive, with
\(\Omega_{4,400}\kappa_m>9588/78125\), on every selected section once
\(m\ge10\). Its complete same-base/permutation family has coefficient mass
\(O_{400}(L^{-4})\), because the number of placements is finite and
\(\sum_p(\log p)^4/p^4<\infty\). This one-family estimate is compatible with
the global proper-power Schatten bound and does not replace it.

The kernel mismatch remains visible. At
\(v=(1/5,-2/5,3/5,-2/5)\), the public nested-overlap bracket has
\(O_A=2/5\), \(B_{4,nc}=0\), while the physical row cumulant at \(5\mid m\)
is \(1\). The actual physical kernel is one common external filtered
overlap times the product-of-row-means cumulant; the public kernel uses a
different nested-path overlap for each partition. Pair subtraction is not
the cause of this pointwise discrepancy. The parent interval replay also
retains the positive physical R400 witness and its supercritical Gram
counterexample; these invalidate importing the public Brownian/endpoint
identity without a source-matching proof, but do not settle the ordinary
prime arithmetic aggregate.

## 6. Exact ordinary-prime physical kernel

Set all proper-power coefficients to zero in the exact source operator. The
ordinary arithmetic measure is
\[
d\mu^{ord}_{T,I}=
\sum_{\substack{p_0,\ldots,p_3\le N\\
                 \epsilon\in\{+,-\}^4}}
\left(\prod_{j=0}^3c_{p_j}\right)e^{iTLS}e^{2\pi ik_-S}
\delta_{(v_0,\ldots,v_3)},\quad
v_j=\epsilon_j\log(p_j)/L,\quad S=\sum_jv_j.
\]
All ordered prime tuples and all 16 sign words occur exactly as written.
There are six balanced words; no extra orientation multiplier is inserted.
For \(I=[k_-,k_+]\), \(m=|I|\), the exact row average is
\[
D_m(u)=\frac1m\sum_{r=0}^{m-1}e^{2\pi iru}.
\]

For \(|v|<1\), put
\[
J_v=[\max(0,-v),\min(1,1-v)],\quad
\mathcal F_R1_{J_v}(x)=\sum_{|r|\le R}
\left(\int_{J_v}e^{-2\pi iry}\,dy\right)e^{2\pi irx}.
\]
For a closed lag path \(r_1+\cdots+r_4=0\), \(|r_j|\le R\), let
\(q_0=0,\ q_j=\sum_{a\le j}r_a\), and
\(X_j(k)=P_{k+q_{j-1},k+q_j}\). With
\(p_j=\sum_{a<j}v_a\), the original external filtered overlap is
\[
\Omega_{4,R}(v)=\int_0^1\prod_{j=0}^3
(\mathcal F_R1_{J_{v_j}})(x+p_j)\,dx.
\]
This retains the original root intervals, all four Fourier coefficients,
the hard band, and the ordering phases. The exact number of ordered paths is
\[
\sum_{s=-2R}^{2R}(2R+1-|s|)^2;
\]
at \(R=400\) this is \(342615201\). The selected section contributes the
actual carrier \(e^{iTLS}e^{2\pi ik_-S}\). Exact aliases \(S\in\mathbb Z\)
and all near-alias windows remain in the measure.

For each labeled subset \(B\subseteq\{0,1,2,3\}\), let
\(M_B=\mathbb E_{k\in I}\prod_{j\in B}X_{j+1}(k)\). The physical connected
factor is exactly
\[
\kappa_m^{ord}(v)=
\sum_{\pi\ {\rm anchored,\ ordered}}
(-1)^{|\pi|-1}\prod_{B\in\pi}D_m\!\left(\sum_{j\in B}v_j\right),
\qquad
\Phi_{4,400,m}^{ord}(v)=\Omega_{4,400}(v)\kappa_m^{ord}(v).
\]
Its complete 26-term grouped expansion is
\[
M_{0123}
-M_0M_{123}-M_1M_{023}-M_2M_{013}-M_3M_{012}
-M_{01}M_{23}-M_{02}M_{13}-M_{03}M_{12}
+2M_0M_1M_{23}+2M_0M_2M_{13}+2M_0M_3M_{12}
+2M_1M_2M_{03}+2M_1M_3M_{02}+2M_2M_3M_{01}
-6M_0M_1M_2M_3.
\]
The exact ledger lists every anchored ordered block product and its
coefficient; the block-count multiplicities are \(1,7,12,6\), with signs
\(+,-,+,-\). Thus every pair subtraction is retained.

The pair-plus-connected trace decomposition also has a singleton remainder.
For fixed \(R\), \(\sup_k|X_j(k)|=O_R(\sqrt N)\), since
\(\sum_{n\le N}|c_n|=O(\sqrt N)\). For either sign,
\[
|D_m(\log n/L)|\le
\frac{C}{m\min(\log n/L,1-\log n/L)}\le C/T,
\]
because \(m\asymp TL\), \(\log n\ge\log2\), and \(L-\log n\ge\sqrt L\).
Hence \(|M_{single}|\le C_R\sqrt N/T\). The full coefficient square mass is
\(O(1)\), and the same large-sieve transfer gives \(M_2=O_R(1)\).
Consequently \(M_3=O_R(\sqrt N)\). The singleton terms are
\(O_R(N/T+N/T^2+N^2/T^4)=o(1)\), uniformly over the permitted sections.

For each fixed edge displacement \(|r|\le400\), the proper-power edge field
has normalized row \(L^2\) norm \(O_R(L^{-1})\), directly from the entries
and the same large sieve. The ordinary-prime coefficient square mass is
\[
|a_\phi|^{-2}L^{-2}\sum_{p\le N}\frac{(\log p)^2}{p}=O(1),
\]
since
\(\sum_{p\le x}\log p/p=O(\log x)\). Its edge-field row norm is \(O_R(1)\).
Cauchy–Schwarz changes each two-edge empirical moment by \(O_R(L^{-1})\).
The fixed-band pair layer is a finite polynomial in these moments with
bounded factors. Its ordinary/full-source difference is therefore
\(O_R(L^{-1})=o(1)\), uniformly on the same sections. This transfers the
pair layer; it does not infer a raw fourth-moment bound from the Schatten
root estimate.

For an exact balanced ordinary-prime product closure,
\(p_0p_2=p_1p_3\), unique factorization forces
\(\{p_0,p_2\}=\{p_1,p_3\}\), which is the pair layer. Nonpair exact
closures are excluded, but near products and nonzero aliases are not. For
example, positive slots \((101,103)\) and negative slots \((97,107)\) are
admitted once \(N\ge107\), with products \(10403\) and \(10379\), difference
24. This is an actual prime summand with unresolved carrier phase, not a
positive aggregate counterexample.

## 7. Ordinary aggregate and consumer status

No source-admissible positive ordinary-prime connected aggregate was found,
and no nonpositivity proof was obtained. The 26-term physical kernel is not
identified with the public nested-overlap kernel. The earlier exact
weight-cone diagnostics remain preserved: an abstract nonnegative
reweighting changes \(-1/12\) to \(1187/1200\), and a separate zero-bracket
rational-grid vector has signed entries \(+1,-1\) with no robustness margin.
Neither is legal arithmetic source evidence.

The exact R400 pair certificate gives
\(\mathrm{Pair}_{400}<0.266329+o(1)\). The stronger target
\(w_{400}\le0.266329+o(1)\) needs the ordinary connected aggregate to be
nonpositive. The weaker centered-record budget is
\[
\Delta_{\max}=\frac{3675673694911}{148250000000000}
=0.02479375173633052276559865092748\ldots.
\]
If the ordinary connected term were proved at most \(\Delta_{\max}\), the
pair-plus-connected ceiling would be
\[
0.266329+\Delta_{\max}
=\frac{43158947944911}{148250000000000}
=0.2911227517363305\ldots.
\]
The current direct envelope \(|D_m|\le1\) gives
\(|\Phi^{ord}|\le26G_{400}^4\), \(G_{400}=1+2H_{400}/\pi\). Its product
with the tuplewise absolute coefficient-mass bound
\((2\sum_{p\le N}|c_p|)^4=O(N^2/(a_\phi^4L^4))\) is far above this budget.
It is only a pre-collision upper bound for total variation and gives no
useful signed estimate.

The smallest unresolved inequality, in the requested uniform form, is
\[
\limsup_{T\to\infty}\sup_{I\in\mathcal G_T}
\Re\int\Phi_{4,400,m}^{ord}(v)\,d\mu^{ord}_{T,I}(v)
\le\Delta_{\max},
\]
where \(\mathcal G_T\) is the family of permitted good-endpoint principal
sections, including their actual starting-row carriers. The zero right-hand
side is the stronger nonpositivity gate. The 68.82027318675% route requires
that stronger gate and remains conditional. The 79.627% model benchmark,
strict greater-than-79% theorem, and complete RH claim remain open.

## 8. Reproduction and evidence

The exact rational finite-matrix and source-ledger checker is
src/wp84_r400_schatten_absorption_audit.py. The explicit 26-term ledger is
evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json. The independent outward
interval replay of the 48 labeled atom placements is
src/wp84_r400_source_interval_replay.py, with its result in
evidence/WP84_R400_SOURCE_INTERVAL_REPLAY.json. The inherited atom, interval,
and pair certificates were rerun into new evidence logs; historical
certificates were not overwritten.

All eight regression tests pass in normal Python, optimized Python, and
double-optimized Python:

    python -m unittest tests.test_wp84_r400_schatten_absorption_audit
    python -O -m unittest tests.test_wp84_r400_schatten_absorption_audit
    python -OO -m unittest tests.test_wp84_r400_schatten_absorption_audit

The source-hash inventory is evidence/WP84_R400_SOURCE_HASHES.json. The
complete SHA-256 evidence manifest and sidecar are
evidence/WP84_R400_SHA256_MANIFEST.json and
evidence/WP84_R400_SHA256_MANIFEST.sha256. The manifest verifier checks the
historical source blobs against base commit b1ff152df352216aa44c9a2535f04306a39df859
after EOL normalization, and checks every new artifact hash.
