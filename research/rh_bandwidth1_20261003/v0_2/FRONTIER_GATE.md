# Bandwidth-one v0.2 frontier gate — 2026-10-03

## Evidence hierarchy

1. **Independently source-replayed benchmark:** A1290,
   (A=129/10000), (B_6=1094977/5000000000), with directed lower bound

   [
   c_{1290}ge 0.6728005676668788382262765469ldots
   ]

   The exact replay checks 3,550,925 nodes and 1,775,463 leaves.

2. **Public exact-replay report, not yet source-free replayed here:** A1293,
   (A=1293/100000), (B=B_6). The pinned public report at upstream head
   `fba91d214655aaa1fd0504bb893c8859c20c79f9` records PASS with
   10,003,455 visited nodes and 5,001,728 leaves. Using the same directed
   analytic constants as our A1290 replay gives

   [
   c_{1293}ge0.6728039389347995417365322794ldots
   ]

3. **Constructive candidate under test:** A1294,
   (A=1294/100000), (B=B_6). If a full exact certificate closes, the
   same bridge yields

   [
   c_{1294}ge0.6728050626982810080982218842ldots
   ]

   This is about (1.124	imes10^{-6}) above the A1293 arithmetic value.

4. **Stretch candidate:** A1295, (A=259/20000). This would yield roughly
   (0.6728061864655), but it has less catalog slack and is not the primary
   target until A1294 is resolved.

## Why A1294 is primary

The frozen 666-piece catalog gives a numerical adversarial point near
(0.01296159) at (B=B_6). Therefore A1294=0.01294 has about
(2.16	imes10^{-5}) diagnostic slack, while A1295=0.01295 has only about
(1.16	imes10^{-5}). These are pointwise ceiling diagnostics, not proofs.

A1294 also isolates one change from the public A1293 report: only A is
increased, while B and all analytic inputs remain fixed.

## Seam obstruction discovered

The naive exact branch-and-bound implementation can become trapped at a
refinement seam. A tiny box may straddle two certified one-dimensional
refinement pieces, forcing fallback to the much weaker parent stable model.
Repeated dyadic splitting then drives depth upward without reflecting a
mathematical obstruction.

This was observed independently:

- the naive A1293 regeneration run 37117582078 hit depth 513 after only
  36,751 visited nodes and stopped at DEPTH_CAP;
- this does **not** contradict the public A1293 PASS report, because it is a
  different generator/lower-bound selection strategy.

The seam-aware A1294 checker instead partitions each affected scalar interval
at exact catalog boundaries and takes the minimum of the certified
piecewise lower envelope. Every accepted lower bound remains exact rational.

## A1294 scaling gate

GitHub Actions run `37117579760`, artifact `11272088005`
(`sha256:ebed6d4f37018688ba7549df066174f8c8ed9c690f4781bf868a65c9f6ea21ed`)
ran the seam-aware A1294 checker on the full root ([0,60]^5) for 250,000
nodes against the pinned input hashes.

Result:

- status: NODE_CAP, no counterexample;
- visited: 250,000;
- closed exact leaves: 124,983;
- pending stack: 35;
- maximum depth: 72;
- elapsed: 171.30 seconds;
- all closed leaves were exact quadratic leaves;
- smallest accepted rational margin remained positive.

This is strong scaling evidence but **not yet a certificate**, because the
pending boxes mean the root domain is not fully covered.

A 1,000,000-node scaling run has been launched next. Full certificate
generation is authorized only if scaling remains healthy.

## A1295 diagnostic

The independent 25k-node A1295 workflow completed its pilot wrapper, but the
underlying exact search stopped at NODE_CAP: 25,001 visited, 12,486 closed
leaves, 29 pending, maximum depth 80. It did not find a counterexample.
A1295 remains secondary until the seam-aware A1294 route is resolved.

## Required proof chain before any new theorem claim

A PASS search is not sufficient by itself. A publishable improvement requires:

1. complete exact coverage of ([0,60]^5);
2. a canonical certificate stream;
3. a verifier that checks the stream without trusting the search generator;
4. frozen catalog/input hashes;
5. independent replay of every terminal inequality with rational arithmetic;
6. catalog-soundness / one-dimensional kernel-envelope audit;
7. analytic bridge audit from the finite affine inequality to the density
   theorem;
8. renewed literature/novelty search;
9. preferably a Lean finite-certificate port or kernel replay.

Until those gates pass, A1294 is a **candidate certificate**, not a new
unconditional zero-density theorem and not an RH result.
