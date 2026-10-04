# WP70-2E — public tail-envelope reproduction failure

Date: 2026-10-04  
Status: **FIRED PUBLIC FALSIFIER / REPRODUCIBILITY BLOCKER**

## Scope

This note records a clean rerun of the public helper

\`scripts/tail_bound.py\`

from \`JoshuaHKU/zeta-0.7947-reproduction\`, pinned at

\`d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8\`.

It does **not** claim that the 79.62% preprint is false.  It records that one
of the public package's own preregistered tail falsifiers does not reproduce
the small tail charge consumed in the paper.

## Registered criterion in the public script

The script itself states for F-E3c:

- \`env_total <= 0.02\`: tail gate closed;
- \`0.02 < env_total <= 0.1\`: partial fire;
- \`env_total > 0.1\`: **structural fire**.

The registered example is \(T=2400,P=40,\mathrm{DCAP}=2\times10^4\).

## Clean pinned rerun

GitHub Actions run:

\`37182902963\`

completed successfully as infrastructure.

The scientific outputs were:

\[
T=2400:\qquad
\mathrm{env\_total}=0.98700,
\]

and

\[
T=4800:\qquad
\mathrm{env\_total}=0.95217.
\]

Therefore both heights trigger the public script's own

\[
\boxed{\text{STRUCTURAL FIRE}}
\]

criterion.

The preceding partial-sum identity subgate F-E3d did pass on all four printed
tests, so the failure is localized to the attempted absolute tail envelope,
not to the basic signed partial-sum identity.

## Conflict with the paper

The public preprint states tail charges

\[
\varepsilon_{\rm tail}\le0.0115\quad(T=2400),
\qquad
\varepsilon_{\rm tail}\le0.0111\quad(T=4800),
\]

and describes them as decreasing.

A repository-wide search found those two numerical values in the paper and in
the quadrature consumer, but did not locate a public generated output or
script invocation reproducing them directly.

The public \`REPRODUCTION.md\` lists \`tail_bound.py\` as a helper dependency
but does not instruct the reader to run its \`env\` mode.  The file has been
present since the initial reproduction-package commit and was not modified by
the later headline/certification commits.

## Interpretation

At least four explanations remain logically possible:

1. \`tail_bound.py env\` is a stale failed experiment that should have been
   retired but was left in the package;
2. it is using a different normalization/convention from the paper's
   \(0.0115/0.0111\) charge;
3. a correction exists in non-public archived material;
4. the paper's tail bookkeeping is genuinely incomplete.

Until one of these is resolved, the \(0.0111\) number cannot be treated as an
independently reproduced theorem input.

## Consequence for our 70% line

Our exact rational geometry

\[
C_{\rm core}=-\frac1{48}
\]

is unaffected.

The exact one-sided threshold is also unaffected:

\[
R<-\frac1{180}.
\]

But the conditional value

\[
\frac{1082}{1539}=0.7030539\ldots
\]

uses the public \(0.0111\) tail charge.  Therefore it remains classified

**CONDITIONAL / NOT YET A THEOREM**.

## Repair plan

1. Reproduce the alternative public \`mains_envelope.py env\` and \`env2\`
   routes at both heights.
2. Trace the exact algebraic definition of the paper's
   \(\varepsilon_{\rm tail}\).
3. Identify whether F-E3c is obsolete, mis-normalized, or genuinely
   contradictory.
4. If necessary, replace the public tail argument with an independent
   signed-\(\gamma\) / Abel estimate.
5. Consume a tail bound only after its normalization matches the exact
   \(-1/48\) continuum convention.

The kill gate is explicit: no public \(>70\%\) claim from this branch until the
tail discrepancy is discharged.
