# WP84 signed aggregate: exact Boolean-mask extremal reduction

**Decision C — the uniform-mask debt reduces exactly to one positive-part
majorant.** This is an exact finite-dimensional optimization identity at each
fixed height and supplied section. It proves no positive arithmetic saving.
The relaxed budget remains unpaid and strict `>79%` remains **OPEN**.

## Frozen state and evidence boundary

The run started on branch `codex/c5-c6-attack-20261006` at
`9401b38a8d2b8be8fc9f9597988dd93c1d6c86c1`, whose parent is
`4f0375b2ebc7a263ca3a59133e46d3449bf89989`. The tracked tree was clean;
the pre-existing untracked `notebooklm_packet/` was preserved. No push,
merge, history search, packet read, source-selector reconstruction, or change
to the frozen consumer was made.

The inherited exact reductions remain as recorded: 8,740 surviving raw
sign/equality classes (1,132 fifth and 7,608 sixth), with 21,588 retained
class/alias pairs, represented under the certified full-mask symmetries by
453 real correlation functionals. The near-alias survivor list and orbit
replay were independently rerun. Their symmetry/orbit identities do not
automatically hold for arbitrary callbacks: applying them to an enlarged
Boolean-mask class requires mask equivariance, which the callback API itself
does not impose.

## Exact signed aggregate and retained weights

Put

\[
 X=T/(2\pi),\quad L=\log X,\quad N=\lfloor e^{L-\sqrt L}\rfloor,
 \quad R=6000,\quad I=[k_-,k_+],\quad d'=|I|.
\]

For a raw origin of degree \(b\in\{5,6\}\), sign word
\(\epsilon\in\{\pm1\}^b\), and exact equality partition \(\pi\), assign
distinct ordinary primes \(q_B\le N\) to its blocks and set
\(p_j=q_{[j]}\),
\(\lambda=\sum_j\epsilon_j\log p_j\). For each closed path
\(\ell\in[-6000,6000]^b\), \(\sum_j\ell_j=0\), let
\(u_0=0, u_j=\sum_{a\le j}\ell_a\),
\(i_{\min}=k_- -\min_j u_j\), and
\(M_\ell=\max(0,d'-(\max_j u_j-\min_j u_j))\). The exact finite trace factors
are

\[
c_p=-\frac{\log p}{a_\phi(T)L\sqrt p},\qquad
f_0^\epsilon(\alpha)=1-\alpha,\qquad
f_\ell^+(\alpha)=\frac{1-e^{2\pi i\ell\alpha}}{2\pi i\ell},\qquad
f_\ell^- =\overline{f_\ell^+},
\]
\[
W_{\epsilon,\ell}(p)=\prod_j c_{p_j}f_{\ell_j}^{\epsilon_j}(\log p_j/L)
 \exp\!\left(\frac{2\pi i}{L}\sum_j\epsilon_j u_{j-1}\log p_j\right),
\]
\[
K_\ell(\lambda)=\frac{e^{iT\lambda+2\pi i i_{\min}\lambda/L}}{d'}
 \sum_{r=0}^{M_\ell-1}e^{2\pi i r\lambda/L},
\]
with the sum zero when \(M_\ell=0\). This keeps the actual sampled root
sum, endpoint phases, prime weights, and the full path; it makes no sharp or
continuum substitution.

For the surviving near-alias origins, the exact debt is

\[
Q_{\rm surv}(T;\chi)=\Re\sum_{b=5,6}\omega_b
 \sum_{(\epsilon,\pi)\in\mathcal D_b^{\rm surv}}
 \sum_{\substack{q_B\le N\text{ ordinary, block-distinct}}}
 \sum_{\substack{|\ell_j|\le6000\\\sum\ell_j=0}}
 \sum_{m\in\mathcal M_{\epsilon,\pi}}
 \chi(\mathrm{fid},p,\ell,T,I,m)
 W_{\epsilon,\ell}(p)K_\ell(\lambda)
 \mathbf1_{0<|\lambda-mL|\le H/T}.
\]

Here \(\mathcal D_b^{\rm surv}\) and the listed aliases are the exact
remaining rows of `WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv`; the ordinary-prime
domain is the complete natural pool, not the six-prime core. The coefficients
are
\[
\omega_5=-11501/12500,\qquad \omega_6=137641/250000.
\]

The total noncentral debt also retains the exact long-tail piece
\[
Q_{\rm tail}(T;\chi)=\Re\sum_{b=5,6}\omega_b
 \sum_{(\epsilon,\pi)\in\mathcal D_b^{\rm tail}}
 \sum_{q_B\le N\;\mathrm{ordinary,\ block-distinct}}
 \sum_{\ell\in[-6000,6000]^b,\,\sum\ell=0}\sum_{m\ne0}
 \chi(\mathrm{fid},p,\ell,T,I,m)W_{\epsilon,\ell}(p)K_\ell(\lambda)
 \mathbf1_{H/T<|\delta|\le L/2},
\]
where \(m=\lfloor\lambda/L+1/2\rfloor\),
\(\delta=\lambda-mL\in[-L/2,L/2)\), exact aliases \(\delta=0\) are
excluded, and \(\mathcal D_b^{\rm tail}\) contains every raw pattern not
proved removable for this tail. Nothing in this audit discards a long-tail
class. The already separately ledgered central \(m=0\) contribution is not
part of this particular near-alias/dilated-product debt. Define
\(S_T(\chi)=Q_{\rm surv}(T;\chi)+Q_{\rm tail}(T;\chi)\).

## How the callback mask enters

The callback contract is Boolean admission on
`(fid, slots, lag, T, section, m)`. All known outer restrictions remain fixed:
natural prime cutoff, equality-block assignment and distinctness, exact
carrier, closed path, allowed alias/detuning and positive root interval. The
unresolved original slot-window/row-admission part is the Boolean variable.
For each fixed \(T,I\), the full prime and path index set is finite, though
astronomical. Terms with exactly the same callback key share one bit and must
be combined before optimization.

Let \(\mathcal K_{T,I}\) be those callback keys after fixed, source-independent
gates. For each key \(k\), combine every raw origin, near/tail contribution,
and repeated appearance with that key into the exact real coefficient
\[
a_k(T,I)=\sum_{\substack{\text{all retained atoms }\nu\\
                         \mathrm{key}(\nu)=k}}
 \omega_{b(\nu)}\,G_\nu(T,I)\,\Re\!\left(W_\nu K_\nu\right),
\]
where \(G_\nu\) is the product of the fixed exact alias, natural-pool,
equality, path and root indicators. Then, without taking absolute values of
the original signed terms,
\[
\boxed{\displaystyle S_T(\chi)=\sum_{k\in\mathcal K_{T,I}}\chi_k a_k(T,I),
\qquad \chi_k\in\{0,1\}.}
\]

Thus the dependence is a diagonal linear functional on a Boolean hypercube,
not a nonlinear mask dependence. It is not automatically a positive
semidefinite or Gram form: arbitrary bits can remove one side of a signed
cancellation. For the literal executable-contract class, every bit can be
chosen independently. The exact support function is
\[
\boxed{\displaystyle
 \sup_\chi S_T(\chi)=\sum_{k\in\mathcal K_{T,I}}[a_k(T,I)]_+,
 \quad
 \inf_\chi S_T(\chi)=\sum_k\min(a_k(T,I),0),
 \quad
 \sup_\chi|S_T(\chi)|=\max\!\left(\sum_k[a_k]_+,-\sum_k\min(a_k,0)\right).}
\]
The maximizer \(\chi_k=\mathbf1_{a_k>0}\) is a finite truth-table adversary
allowed by the callback interface. It is **not** a claim about the historical
source selector and is not an arithmetic counterexample to the budget.

If a narrower class explicitly requires covariance under a certified finite
symmetry group \(G\), replace keys by the orbits \(C\) of the generated
equivalence relation and set \(A_C=\sum_{k\in C}a_k\). Then exactly
\(\sup S=\sum_C[A_C]_+\). Such covariance must be stated as a constraint;
the callback API does not enforce it. In particular, the 453 coefficient
table \(c_\alpha=|O_\alpha|\omega_b\) is justified for the original
covariant source mask, but not for every API-admissible mask. Without
covariance the 8,740 raw origins remain separate. This is why a signed
coefficient sum over the 453 collapsed functionals cannot by itself prove a
uniform-mask bound.

The exact coefficient table for the 453 covariant functionals is still
reconstructed and checked: its total absolute mass is
\(163444421/31250\). It is a provenance/budget check only, not the coefficient
mass of an arbitrary mask after collapsing symmetry orbits.

## Frozen budget replay and consequence

The independent exact-arithmetic replay reconvolves
\[
q(x)=-\frac{19101}{185500}+\frac{961}{3710}x+\frac{31}{50}x^2-
 \frac{371}{500}x^3
\]
and verifies
\[
(c_0,\ldots,c_6)=\left(\frac{364848201}{34410250000},
-\frac{18356061}{344102500},-\frac{26060119}{430128125},
\frac{21981971}{46375000},0,-\frac{11501}{12500},
\frac{137641}{250000}\right),
\]
the frozen paid terms
\(e_{band}=128952763/92407500000\),
\(e_{var}=26060119/12734908593750\), and
\(J_*=64788151489666079/572357731837500000\). It then verifies
\[
\Delta_{\rm ideal}=\frac{27704610381502}{17886179119921875},\qquad
\Delta_{\rm relaxed}=\frac{52897896569489}{572357731837500000}.
\]
At \(H=400\), the previously used multiplier 201 yields the exact primitive
scale
\[
\Delta_{\rm relaxed}/201=
\frac{52897896569489}{115043904099337500000}.
\]
These are reference allowances, not new optimal budgets; still-unpaid
transfers can reduce the available amount.

The uniform-mask implication would require the single analytic estimate
\[
\boxed{\displaystyle
\limsup_{T\to\infty}\sum_{k\in\mathcal K_{T,I(T)}}
       [a_k(T,I(T))]_+\le\Delta_{\rm available},\qquad
\Delta_{\rm available}\le\Delta_{\rm relaxed},}
\]
uniformly for the allowed sections. This is an exact reduction of
\(\sup_\chi S_T(\chi)\), but the sum has not been bounded or evaluated. No
positive signed saving is earned and the relaxed budget is **UNPAID**.

No Montgomery–Vaughan, large-sieve, shifted-convolution or divisor theorem
was invoked: the mask support-function identity is finite-dimensional and
does not create cancellation in its positive-part sum. Nor was a Gram/PSD
identity or carrier-frequency orthogonality proved. The existing orbit,
consumer-budget, and direct-correlation replay suites pass, but those do not
establish the new asymptotic positive-part estimate.

## Falsification and limits

The maximizer \(\chi_k=\mathbf1_{a_k>0}\) demonstrates that orbit symmetry
alone cannot control the aggregate uniformly unless the mask is constrained
to transform covariantly. The full prime stream remains the input domain;
this adversarial Boolean table does not replace it by a finite prime core.
No actual coefficient signs or positive-part mass were numerically fabricated.
Thus it falsifies a *symmetry-only cancellation argument*, not the underlying
zeta inequality and not the numerical budget inequality.

The independent replay also rejects mutations that reverse a consumer sign,
drop either survivor degree, remove the natural prime restriction, alter
`R=6000`, replace the full pool by a six-prime core, delete aliases, replace
the signed objective by atomwise absolute values, remove exact carrier/equality
gates, omit the long tail, insert diagnostic rows, invent a source selector,
perturb an exact coefficient, or alter the required allowance. A separate
exact brute-force check enumerates all 28 masks on three small rational LP
examples and verifies the support-function formula.

## Reproduction and first remaining theorem

Run from the repository root:

```powershell
python src/wp84_signed_aggregate_mask_uniform.py
python src/wp84_signed_aggregate_mask_uniform_replay.py
python src/wp84_near_alias_orbit_replay.py
python src/wp84_direct_signed_correlation_replay.py
```

The machine certificate is
[`WP84_SIGNED_AGGREGATE_MASK_UNIFORM_CERTIFICATE.json`](WP84_SIGNED_AGGREGATE_MASK_UNIFORM_CERTIFICATE.json).

The first remaining theorem is the source-weighted positive-part inequality
boxed above for the complete natural prime pool, actual aliases and carrier
phases, all `R=6000` paths and roots, and the entire long-tail term. To exploit
the smaller 453-functional signed ledger instead, one must first prove the
source mask's precise equivariance and original slot-window rule. The old
selector is not reconstructed here. Fifth analytic rank remains `38–72`;
strict `>79%` remains **OPEN**.
