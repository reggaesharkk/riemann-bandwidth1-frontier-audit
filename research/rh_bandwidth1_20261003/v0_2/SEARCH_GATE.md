# Bandwidth-one v0.2 constructive search gate

## Frozen baseline

Independent A1290 replay passes with exact finite arithmetic at A=129/10000 and B6=1094977/5000000000. Using the directed HD(1) lower bound and pi upper bound from the replay gives

c(A1290,B6) >= 0.6728005676668788382262765469...

The public upstream A1293 report at the pinned PR #17 head records PASS for A=1293/100000 at the same B6. Its report is public and exact-replay metadata are available, but the full A1293 stream bundle is not yet independently replayed in this repository. Its arithmetic feedback value from the same directed constants is

c(A1293,B6) >= 0.6728039389347995417365322794...

Treat this as a public reported exact-certificate benchmark, not yet our independently replayed benchmark.

## New constructive direction

The upstream catalog ceiling-vs-B sweep shows the best catalog upper ceiling near B=(21/20) B6:

B = 22994517/100000000000 = 0.00022994517.

At this B, the catalog pointwise ceiling recorded upstream is about

A* <= 0.013521670981544505,

with feedback ceiling about 0.6728129728595.

This ceiling is not a constructive certificate. It only says no certificate using that catalog can exceed the ceiling.

## First search target

To beat the public A1293 arithmetic value at B=(21/20)B6, the affine constant must satisfy

A > 0.01344128887629523133949...

Therefore the first deliberately non-extremal constructive target is

A = 269/20000 = 0.01345,
B = 22994517/100000000000.

If certified, the directed feedback lower bound is

c >= 0.6728049179424652451314118136...,

which exceeds the public A1293 arithmetic value by about 9.79e-7.

The target sits about 7.17e-5 below the upstream catalog ceiling, leaving materially more margin than an attempt near A=0.01352.

## Gate

Do not launch a large certificate tree immediately. First build a small exact feasibility pilot for A=269/20000, B=(21/20)B6 using the same exact catalog semantics.

PASS: local branch-and-bound closes representative hard cells and no counterexample point below A is found.

FAIL: a source-backed exact point or box proves E6(g)+B sum(g)<A.

Only after PASS should a full exact tree be generated.

No RH claim. No new density theorem claim until the full certificate, analytic bridge, replay and novelty audit pass.
