# Bandwidth-one v0.2 frontier gate — 2026-10-03

## Evidence hierarchy

The project now distinguishes three levels of the six-translate frontier.

1. **Independently source-replayed benchmark:** A1290, with
   (A=129/10000), (B_6=1094977/5000000000), and fixed public coefficient
   (0.6728005676). The independent exact replay in the review package
   checks 3,550,925 nodes and 1,775,463 leaves.

2. **Public external exact-replay report, not source-replayable from committed
   streams:** A1293, with (A=1293/100000). The public A1290 frontier package
   contains an exact-replay report, manifest, and generator log whose SHA-256
   values match the upstream SHA256SUMS. The canonical ~200 MB tree streams
   are not committed, so this project does not promote A1293 to the
   source-replayed benchmark.

3. **Method ceiling diagnostics:** the upstream v3 catalog reports a surrogate
   ceiling near (A=0.0129616); direct numerical minimization of the true
   Montgomery–Taylor kernel objective is reported near (A=0.0129938).
   These are ceiling diagnostics, not constructive density theorems.

## Arithmetic

Using the same directed lower endpoint for the Montgomery–Taylor constant and
the same directed upper bound for pi as the A1290 audit,

[
c(A,B_6)=\frac{6C_0-10\pi B_6}{6-A}.
]

For (A=1293/100000), the directed arithmetic gives approximately

[
c=0.6728039389347995417\ldots.
]

Thus future work should beat the *reported* A1293 level, not merely A1290,
before making any novelty claim.

The next constructive target is

[
A=0.01295=259/20000,
]

which would give approximately

[
c=0.6728061864655164551\ldots,
]

strictly above the reported A1293 level.

## Feasibility evidence

The upstream A1290 frontier notes record:

- A=0.01293 closes with catalog v3;
- A=0.01295 reached a 12,000,000-node resource cap with only 37 boxes pending
  at depth 83;
- A=0.01298 exceeds the v3 catalog ceiling and is not a valid target for that
  surrogate without further one-dimensional refinement.

Therefore A=0.01295 is a **resource/partition problem, not a known mathematical
obstruction**.

A local independent exact-B&B prototype has been started from the pinned
stable, v1, and v3 rational catalogs. Its first 10,000-node probes reproduce
the expected weighted-split tree behavior and preserve exact Fraction
comparisons at every accepted leaf. No full A1295 certificate is claimed yet.

## Next gate

Build a checkpointable independent A1295 search and attempt to close
(A=259/20000). A successful search must produce canonical streams, exact
input hashes, an independent replay, and then a separate analytic/Lean bridge
audit before any unconditional coefficient is claimed.

Claim boundary: this is a certificate-search program for a zero-density
constant. It does not claim RH or that all zeta zeros lie on the critical
line.
