# Bandwidth-one v0.2 constructive search gate

## Baseline

A1290 is independently replayed in the review package.

Pinned public upstream PR #17 also contains an exact replay report for A1293 at the same sextuple penalty coefficient

A = 1293/100000,
B = 1094977/5000000000.

Using the same directed HD(1) lower bound and pi upper bound as our replay, this gives the arithmetic feedback value

c(A1293,B) >= 0.6728039389347995417365322794...

The A1293 report is public source evidence, but its full stream bundle has not yet been independently source-free replayed in this repository. It is therefore a public reported exact-certificate benchmark, not yet our independently replayed benchmark.

## First constructive target

The cleanest next search keeps B fixed and increases only A.

A 666-piece catalog point search using the frozen stable + A1275 + A1290-v3 lower models found a candidate adversarial value near

A_catalog_point ~= 0.01296157144

at B = 1094977/5000000000.

This is an upper ceiling witness for what that catalog could ever certify; it is not a constructive proof.

The first deliberately conservative target is

A = 1294/100000 = 0.01294,
B = 1094977/5000000000.

If certified, the directed feedback lower bound is

c >= 0.6728050626982810...

which improves on the A1293 arithmetic value by about 1.124e-6.

The target remains about 2.16e-5 below the current catalog point ceiling estimate, giving materially more slack than immediately changing B or pushing close to the apparent ceiling.

## Why same-B first

1. It changes one finite parameter only.
2. It reuses the A1293 geometry and refinement catalog directly.
3. Any failure can be attributed to the A increment rather than a simultaneous B shift.
4. It gives a larger safety margin than the initial B=(21/20)B6, A=0.01345 proposal.

The B-sweep remains a second-stage option. The old catalog sweep suggests possible additional gain around B approximately 1.05 B6, but a full 666-piece search shows that region is much tighter than the older 272-model ceiling suggested.

## Gate

Do not launch a massive full tree immediately.

First run a small exact branch-and-bound feasibility pilot at A=1294/100000 with the same B and the frozen 666-piece catalog.

PASS:
- no exact counterexample point/box below A is found;
- hard cells close with positive rational margins in a representative pilot;
- generator semantics match the A1293/A1290 verifier semantics.

FAIL:
- an exact point or box gives E6(g)+B sum(g)<A;
- or branch growth indicates the target is computationally impractical without new refinements.

Only after PASS should a full exact tree be generated.

No RH claim. No new density theorem claim until the full certificate, analytic bridge, independent replay, and novelty audit pass.
