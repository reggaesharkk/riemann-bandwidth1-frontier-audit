# Target 70% attack board — support escape / higher-moment route

Date: 2026-10-04  
Branch: `research/70pct-support-escape-v0.1`

## Decision

We will not try to reach 70% by scaling the current q=8 branch-and-bound machinery.

The reason is structural, not computational.

The current exact-retuned working headline is

[
C>0.6735000520898147.
]

The Anthropic paper's Remark 1.1 states that no configuration-by-configuration
certificate reading only the bandwidth-one pair-correlation information used
by Theorem B can certify more than approximately

[
0.68185.
]

Therefore

[
0.70-0.68185=0.01815
]

is outside the information content of that entire certificate class.
No amount of additional q=8/q=12 optimization can cross this barrier if it
continues to consume only the same bandwidth-one data.

This branch therefore changes the **analytic input**, not merely the optimizer.

## Official barrier

The pinned formal-math repository now contains `Zeta23/PairCeiling/`.
Its explicit N=256 law records a simple-point fraction around

[
0.681828687463832ldots
]

and the formal stability layer quantifies the bandwidth-one obstruction.
The public Lean source keeps one displayed hypothesis, `EnclOK`, for the
external interval enclosure certificate; the downstream ceiling inequalities
are kernel checked.

This is enough to impose a research kill rule:

> Any proposed unconditional 70% route that uses only the same bandwidth-one
> pair data configuration-by-configuration is rejected before computation.

## What 70% actually requires

The paper gives two escape mechanisms.

### Route A — support beyond one

For the same general pair-correlation route, the paper states that 70%, 80%,
and 90% would require Fourier support roughly

- 70%: **1.04**
- 80%: **1.26**
- 90%: **1.70**

respectively.

The obstruction is on the prime side.  If

[
X=(T/2pi)^lambda
]

with (lambda>1), the off-diagonal prime sums in Proposition 5.6 are no
longer dominated by the diagonal.  The paper says their evaluation requires
prime-pair information of Hardy--Littlewood strength (equivalently the
pair-correlation conjecture beyond alpha=1).

For the elementary flat-window constant

[
H(lambda)=2-rac1lambda-rac{lambda}{3},
]

the exact equation (H(lambda)=0.70) is

[
10lambda^2-39lambda+30=0,
]

so the first relevant root is

[
lambda_{70,mathrm{flat}}
=
rac{39-sqrt{321}}{20}
=
1.0541763566415541ldots
]

The optimized certificate architecture reduces the paper's estimated
requirement to about 1.04.

**Primary analytic target A70:**
prove enough unconditional weighted prime-pair cancellation to control the
off-diagonal prime side for at least

[
oxed{lambda=1.04+arepsilon}
]

with explicit error terms small enough to preserve a >0.70 zero-side
certificate.

This is a genuinely new analytic-number-theory theorem, not a larger finite
search.

### Route B — fourth spectral moment

Section 7.5 of the paper gives a second escape hatch.

If the fourth trace asymptotic `HL*(4,lambda)` were available throughout
(lambda<1), the Christoffel/moment argument would give

[
oxed{rac{13}{18}=0.722222ldots}
]

simple critical-line zeros.

That already clears 70% by

[
rac{13}{18}-rac7{10}
=
rac1{45}
=
0.022222ldots
]

The needed fourth-moment input encodes Hardy--Littlewood-type additive
correlations of the convolution (Lambda*Lambda).  The paper explicitly
notes that current unconditional diagonal technology only supplies moments
in the Rudnick--Sarnak range (klambda<2), so the useful fourth moment near
(lambda=1) is not currently available.

**Primary analytic target B72:**
obtain a rigorous fourth-trace estimate strong enough near bandwidth one to
activate the degree-two Christoffel bound.  The full target would yield
13/18 = 72.222...%.

This is the preferred stretch target because a success is automatically
above 70%.

## Research ordering

### WP70-0 — barrier lock
- reproduce the official PairCeiling constants from the pinned Lean source;
- record the exact external trust boundary `EnclOK`;
- stop all bandwidth-one-only attempts that pretend they can reach 70.

### WP70-1 — fourth-moment derivation
Write the exact prime-side expansion of (operatorname{tr} G^4) for the
same Gabor/Weil compression and separate:
1. fully diagonal multiplicative relations;
2. semi-diagonal terms;
3. genuinely additive ((Lambda*Lambda)(m)(Lambda*Lambda)(m+h)) terms.

The deliverable is a theorem statement with the *weakest* correlation estimate
that would already force a coefficient >0.70, not the full Hardy--Littlewood
conjecture if less is enough.

### WP70-2 — 1.04 support bridge
Independently derive the exact off-diagonal term that first breaks when
(X>T), specialize to (X=T^{1.04}), and quantify the maximum admissible
error before the 70% certificate collapses.

The deliverable is an explicit inequality of the form

[
|mathcal O_{1.04}(T)|le delta,N(T)
Longrightarrow
N_{0}^{s}(T,2T)ge (0.70+epsilon)N(T,2T),
]

with exact (delta,epsilon>0).

### WP70-3 — hybrid route
Test whether a partial fourth-moment estimate plus a support extension smaller
than 1.04 beats either ingredient alone.  Optimize the information budget,
not just the numerical certificate.

### WP70-4 — finite certificate only after new input
Only after WP70-1 or WP70-2 produces a valid analytic inequality do we build
the corresponding finite exact certificate.  Branch-and-bound is the final
verification layer, not the source of the 70% jump.

## Non-negotiable evidence classes

- **KNOWN:** published/formalized bandwidth-one facts.
- **DERIVED:** exact algebra we can reproduce independently.
- **CONDITIONAL TARGET:** consequences of an unproved prime-correlation input.
- **CERTIFIED:** finite exact certificate after the analytic input is proved.
- **THEOREM:** only after all analytic and finite bridges are closed.

No conditional 72.22% calculation will be presented as an unconditional
result.

## Immediate target

The project now has two numerical milestones:

[
oxed{70%}
]

as the first structural escape, and

[
oxed{13/18=72.222ldots%}
]

as the higher-moment stretch target.

The active research question is no longer "how many more B&B nodes do we
need?"  It is:

> What is the weakest new prime-correlation statement that is both provable
> unconditionally and strong enough to push the zero certificate across 70%?
