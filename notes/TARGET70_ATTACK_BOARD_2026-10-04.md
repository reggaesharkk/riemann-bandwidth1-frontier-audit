# Target 70% attack board — support escape / higher-moment route

Date: 2026-10-04  
Branch: \`research/70pct-support-escape-v0.1\`

## Decision

We will not try to reach 70% by scaling the current q=8 branch-and-bound machinery.

The reason is structural, not computational.

The current exact-retuned working headline is

\[
C>0.6735000520898147.
\]

The Anthropic paper's Remark 1.1 states that no configuration-by-configuration
certificate reading only the bandwidth-one pair-correlation information used
by Theorem B can certify more than approximately

\[
0.68185.
\]

Therefore

\[
0.70-0.68185=0.01815
\]

is outside the information content of that entire certificate class.
No amount of additional q=8/q=12 optimization can cross this barrier if it
continues to consume only the same bandwidth-one data.

This branch therefore changes the **analytic input**, not merely the optimizer.

## Official barrier

The pinned formal-math repository contains \`Zeta23/PairCeiling/\`.
Its explicit N=256 law records a simple-point fraction around

\[
0.681828687463832\ldots
\]

and the formal stability layer quantifies the bandwidth-one obstruction.
The public Lean source keeps one displayed hypothesis, \`EnclOK\`, for the
external interval enclosure certificate; the downstream ceiling inequalities
are kernel checked.

This gives a research kill rule:

> Any proposed unconditional 70% route that uses only the same bandwidth-one
> pair data configuration-by-configuration is rejected before computation.

## Route A — support beyond one

For the same general pair-correlation route, the paper states that 70%, 80%,
and 90% require Fourier support roughly

- 70%: **1.04**
- 80%: **1.26**
- 90%: **1.70**

respectively.

The obstruction is on the prime side. If

\[
X=(T/2\pi)^\lambda
\]

with \(\lambda>1\), the off-diagonal prime sums in Proposition 5.6 are no
longer dominated by the diagonal. Their evaluation requires prime-pair
information of Hardy--Littlewood strength, equivalently pair-correlation
information beyond \(\alpha=1\).

For the flat-window constant

\[
H(\lambda)=2-\frac1\lambda-\frac{\lambda}{3},
\]

the exact equation \(H(\lambda)=0.70\) is

\[
10\lambda^2-39\lambda+30=0,
\]

so the first relevant root is

\[
\lambda_{70,\mathrm{flat}}
=
\frac{39-\sqrt{321}}{20}
=
1.0541763566415541\ldots
\]

The optimized Montgomery--Taylor window has

\[
c_\lambda^*
=
\frac{\sqrt2\tan\theta}{1+\theta\tan\theta},
\qquad
\theta=\frac{\lambda}{\sqrt2},
\]

and the simple-zero constant is \(2-1/c_\lambda^*\). Solving

\[
2-\frac1{c_\lambda^*}=0.70
\]

gives the sharper numerical target

\[
\boxed{\lambda_{70,\mathrm{MT}}\approx1.042654521180776}.
\]

That is the quantitative version of the paper's “roughly 1.04”.

**Primary analytic target A70:** prove enough unconditional weighted
prime-pair cancellation to control the prime side at at least

\[
\boxed{\lambda>1.0426546}
\]

with explicit error terms small enough to preserve a strict \(>0.70\) result.

## Route B — fourth spectral moment

Section 7.5(f) provides a different escape hatch.

If the fourth trace asymptotic \`HL*(4,lambda)\` were available throughout
\(\lambda<1\), the Christoffel/moment argument would give

\[
\boxed{\frac{13}{18}=0.722222\ldots}
\]

simple critical-line zeros.

That clears 70% by exactly

\[
\frac{13}{18}-\frac7{10}
=
\frac1{45}
=
0.022222\ldots
\]

The missing fourth-moment input encodes Hardy--Littlewood-type additive
correlations

\[
\sum_m
(\Lambda*\Lambda)(m)
(\Lambda*\Lambda)(m+h),
\qquad
|h|\lesssim X^2/T.
\]

Current unconditional diagonal technology only supplies moments in the
Rudnick--Sarnak range \(k\lambda<2\), so the useful fourth moment near
\(\lambda=1\) is not presently available.

**Primary analytic target B72:** obtain a fourth-trace estimate strong enough
near bandwidth one to activate the degree-two Christoffel bound. The full
target would give 13/18 = 72.222...%.

## New lead: use the fact that the missing shift range is long

Write \(X=T^\lambda\). Then the fourth-trace off-diagonal range is

\[
H=X^2/T=T^{2\lambda-1}
=X^{\,2-1/\lambda}.
\]

Near \(\lambda=1\), this is a very long shift average:

| lambda | exponent beta in \(H=X^\beta\) |
|---:|---:|
| 0.80 | 0.750000 |
| 0.90 | 0.888889 |
| 0.95 | 0.947368 |
| 0.98 | 0.979592 |
| 1.00 | 1.000000 |

This suggests a potentially weaker target than pointwise Hardy--Littlewood:
derive the exact fourth-trace weights and determine whether a **weighted
average over shifts** is sufficient.

That matters because there is substantial unconditional technology for
averaged shifted correlations over long ranges, whereas fixed-shift prime
correlations remain far harder.

This is only a lead. The coefficient is \(\Lambda*\Lambda\), not plain
\(\Lambda\), and the exact trace weights and required error norm must be
derived before any existing average-shift theorem can be claimed relevant.

## Research ordering

### WP70-0 — barrier lock
- reproduce the official PairCeiling constants from the pinned Lean source;
- record the exact external trust boundary \`EnclOK\`;
- reject all bandwidth-one-only “70%” proposals.

### WP70-1 — fourth-moment reduction
Derive \(\operatorname{tr} G^4\) on the prime side and separate:
1. diagonal multiplicative relations;
2. semi-diagonal terms;
3. genuine shifted correlations of \(\Lambda*\Lambda\).

Then solve for the **weakest weighted-average correlation error** that still
forces a coefficient \(>0.70\).

### WP70-2 — support 1.042655 bridge
Derive the exact first off-diagonal obstruction for
\(X=T^{1.042655}\) and solve for the maximum admissible prime-side error before
the 70% certificate collapses.

Desired theorem shape:

\[
|\mathcal O_{1.042655}(T)|
\le
\delta\,N(T)
\quad\Longrightarrow\quad
N_0^s(T,2T)
\ge
(0.70+\varepsilon)N(T,2T)
\]

with explicit \(\delta,\varepsilon>0\).

### WP70-3 — hybrid
Test whether a partial fourth-moment estimate plus a support extension smaller
than 1.042655 beats either ingredient alone.

### WP70-4 — certificate
Only after a new analytic inequality is proved do we spend large compute on a
finite certificate.

## Evidence classes

- **KNOWN:** published/formalized facts.
- **DERIVED:** algebra independently reconstructed here.
- **CONDITIONAL TARGET:** consequence of an unproved correlation input.
- **CERTIFIED:** exact finite certificate after the analytic input is proved.
- **THEOREM:** all analytic and finite bridges closed.

No conditional 72.22% calculation will be advertised as an unconditional
result.

## Numerical mission

First structural escape:

\[
\boxed{70\%}.
\]

Stretch target:

\[
\boxed{13/18=72.222\ldots\%}.
\]

The active question is now:

> What is the weakest new prime-correlation statement that is provable
> unconditionally and strong enough to push the zero certificate across 70%?
