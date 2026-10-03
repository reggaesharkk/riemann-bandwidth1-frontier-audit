# Seam-aware scalar envelope lemma

## Status

Exact mathematical lemma used by the v0.2 A1294 finite search. It does not
certify the one-dimensional catalog pieces themselves; their soundness is a
separate upstream/Lean obligation.

## Lemma

Let K:I->R. Let I=[a,b] be partitioned by

a=x_0<x_1<...<x_m=b.

For each segment I_j=[x_{j-1},x_j], suppose a finite collection of functions
L_{j,r} is available such that

L_{j,r}(x) <= K(x) for x in I_j.

Define

ell_j = max_r inf_{x in I_j} L_{j,r}(x),
ell   = min_j ell_j.

Then K(x) >= ell for every x in I.

### Proof

For a fixed segment I_j, every L_{j,r} is a pointwise lower bound for K.
Therefore for every x in I_j,

K(x) >= L_{j,r}(x) >= inf_{y in I_j} L_{j,r}(y)

for every r. Taking the maximum over r gives K(x) >= ell_j. Taking the
minimum over segments gives K(x) >= min_j ell_j = ell on the whole interval.
QED.

## Application to the frozen catalog

The v0.2 checker partitions a partial-sum interval at every exact endpoint of
a stable/refinement catalog piece lying inside that interval. On each segment
it considers only catalog pieces whose declared validity interval contains
the entire segment.

Each catalog model is either a constant lower barrier or a convex quadratic
lower well with exact rational parameters. Its segment infimum is therefore
computed exactly with Fraction arithmetic by evaluating at the quadratic
center when the center lies in the segment, otherwise at the nearest endpoint.

The segmented result is used only when it is stronger than the single stable
parent model. Thus the seam handling does not assume continuity between
different models and does not interpolate across a gap.

## Remaining trust obligation

The lemma reduces seam soundness to the statement that every frozen catalog
piece really is a lower bound for the target scalar kernel on its declared
interval.

That statement is not proved by the branch-and-bound tree. It must be checked
against the frozen upstream one-dimensional certificates / Lean WellCert
chain before a new zeta-density theorem can be claimed.

The finite tree certificate and the one-dimensional catalog proof therefore
remain separate layers.
