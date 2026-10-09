# Conditioned Cayley energy: exact moment-feasibility obstruction

**Decision: the moment-only route from the source-certified first two sharp
spectral moments is falsified.** There is an exact finite spectrum satisfying
those moments and the rank-two displacement ceiling whose conditioned-cubic
Cayley energy is (0.2501715\ldots>0.105). This is an abstract spectral
counterexample, not a matrix sampled from the WP84 Gaussian ensemble and not a
zeta-side counterexample. Strict (>79\%) remains **OPEN**.

The starting state was branch `codex/c5-c6-attack-20261006`, HEAD
`495a20b28d1fe0c10943814fa9420a2f5e0eb74a`; the only pre-existing untracked
path was `notebooklm_packet/`, which this audit did not access or modify.

## Exact object and applicable constraints

For (U=(H+iI)(H-iI)^{-1}), the frozen cubic is
\[
q(u)=\frac{1936u^3+(-192-5495i)u^2+(-5695+169i)u+(44+2205i)}{5000},
\]
and 
\[
\tau(q(U)^*q(U))=\int p(x)\,d\nu_H(x),\quad
p(x)=\frac{12502645x^6-82863712x^5+221347891x^4-303496416x^3+
224073135x^2-84028544x+12502001}{12500000(x^2+1)^3}.
\]
The consumer threshold is (21/200=0.105).

The same sharp normalized spectral variable (H) has the source-closed
constraints
\[
\int x\,d\nu_H=1+o(1),\qquad
\int x^2\,d\nu_H=4/3+o(1),
\]
as recorded in `WP84_SINE_MEAN_VARIANCE_GATE.md`. The exact finite feasibility
test imposes their limiting values. The (m_3=2) pinned value and the
six-moment vector ((1,1,4/3,2,13/4,101/18,12809/1260)) belong to the
conditional/model moment law; they are not imported as constraints on this
source spectral variable. The available centered third-moment obligation is
still open. The covariance formulas for (W) constrain the added Gaussian
heat direction; by themselves they are not moment constraints on
\(\nu_{H_T}\). The heat variable (H_u=H_1+\sqrt u W), for (u>0), is a
different random spectral variable and is not substituted for (H_T).

The extremal question tested is
\[
\sup_{\nu\in\mathcal P(\mathbb R)}\left\{\int p\,d\nu:
 \int x\,d\nu=1,\;\int x^2\,d\nu=4/3\right\}.
\]
To falsify a universal (<0.105) consequence it suffices to give one
feasible law above the threshold; computing the exact supremum is unnecessary.

## Exact finite-atomic counterexample

Take
\[
\nu=\tfrac14\delta_0+\tfrac34\delta_{4/3}.
\]
Then 
\[
\int1\,d\nu=1,\qquad \int x\,d\nu=1,\qquad
\int x^2\,d\nu=4/3,
\]
while
\[
p(0)=\frac{12502001}{12500000},\qquad
p(4/3)=\frac{34241593}{195312500000},
\]
so
\[
\int p\,d\nu=\frac{48861622601}{195312500000}
=0.25017150771712.
\]
The excess over the required threshold is exactly
\[
\frac{48861622601}{195312500000}-\frac{21}{200}
=\frac{28353810101}{195312500000}
=0.14517150771712>0.
\]
For dimensions divisible by four, this is realized by
\(H=\operatorname{diag}(0,4/3,4/3,4/3)\) repeated in blocks of four.
With (D=\operatorname{diag}(0,1,2,3,\ldots)), ([D,H]=0), so the
displacement rank is zero and satisfies the rank-six consumer's rank ceiling.
The (0.105) universal bound is therefore infeasible from these spectral
constraints alone. The model energy (0.1022554\ldots) is one feasible
measure's value, not an extremal upper bound.

As a stress test only, the non-source-certified moment (m_3=2) can also be
added without closing the gap: 
\[
\widetilde\nu=\tfrac1{54}\delta_{-2}+\tfrac{26}{27}\delta_1+
\tfrac1{54}\delta_4
\]
has (m_0=1,m_1=1,m_2=4/3,m_3=2), but
\[
\int p\,d\widetilde\nu=
\frac{2921277517807}{23029687500000}
=0.1268483351242608>0.105.
\]
This does not promote (m_3=2) to a theorem-side premise.

## Scope and remaining obstruction

The falsifier rules out deriving the conditioned energy target from the first
two source moments plus displacement rank, even in finite dimension. It does
not falsify the actual prime-generated matrix law, the fixed Gaussian
heat-flow expectation, or the zeta theorem: the diagonal examples have not
been shown to arise from the source Gaussian ensemble. Exact covariance of
the added (W), arbitrary Hermitian rank-six structure, and the conditional
six-moment model cannot be silently combined into a spectral law for the
actual source.

The smallest next ingredient is a source-specific one-sided energy or
resolvent inequality for the actual prime-generated (H_T) (or a proved
additional spectral constraint strong enough to exclude the displayed
measure). No such inequality is supplied by the already-certified first and
second moments, the rank bound, or the model Christoffel quadrature. No new
dual-mass search is opened here.

## Replay

```powershell
python src/wp84_conditioned_cayley_spectral_falsifier.py
python src/wp84_conditioned_cayley_spectral_falsifier_replay.py
```

Both programs use exact rational arithmetic. The replay independently
recomputes the rational Cayley energy, moments, finite-matrix realization,
strict threshold excess, and optional non-certified (m_3) stress test.
