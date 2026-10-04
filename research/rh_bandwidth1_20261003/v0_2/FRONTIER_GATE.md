# Bandwidth-one v0.2 frontier gate — frozen 2026-10-04

## Current evidence hierarchy

1. **A1290 — independently source-replayed benchmark**

   [
   A=129/10000,qquad B=B_6=1094977/5000000000.
   ]

   The exact replay checks 3,550,925 nodes and 1,775,463 leaves. The pinned
   upstream Lean development integrates this target and proves the fixed
   coefficient `0.6728005676`.

2. **A1293 — public external exact replay**

   [
   A=1293/100000,qquad B=B_6.
   ]

   The pinned upstream report records PASS with 10,003,455 visited nodes and
   5,001,728 leaves. Upstream explicitly says this closes externally and has
   been independently replayed, but is not integrated into the Lean theorem
   chain.

3. **A1294 — this project, finite exact certificate PASS**

   [
   A=1294/100000=0.01294,qquad B=B_6.
   ]

   GitHub Actions run `37133363690` completed successfully:

   - visited: **13,454,121**
   - leaves: **6,727,061**
   - max depth: **80**
   - full stack exhaustion: **true**
   - independent Fraction-only verifier: **PASS**
   - final artifact ID: `11286675906`
   - downloaded ZIP SHA-256:
     `11c1ab1820039284f60e492fe609f6a497175284acdd0c3c53d6ab62b8b1cd19`

   The publication-safe directed analytic arithmetic proves the fixed
   coefficient

   [
   oxed{0.67280506}
   ]

   conditional only on admitting the externally verified affine certificate
   into the already generic upstream analytic bridge.

4. **A1296 — diagnostic only**

   A 5M-node local full-root run did not close: 5,057,564 visited, 1,024
   pending, depth 79. The deepest frontier is highly structured and has been
   localized for future catalog refinement work. No theorem claim is made.

## Structural contribution of v0.2

The naive checker can lose strength when a scalar partial-sum interval crosses
a refinement seam: no single refinement piece covers the whole interval, so a
weak parent may be used repeatedly.

The v0.2 checker instead partitions at exact catalog boundaries. On every
atomic segment it takes the strongest certified model infimum and then takes
the minimum across segments. This is a valid lower bound without any
continuity assumption between neighboring pieces.

The seam composition has now passed three distinct checks:

- elementary mathematical proof;
- exact finite implementation/replay;
- all-666 JSON ↔ Lean catalog identity plus upstream model soundness chain.

## Closed A1294 gates

- [x] complete exact coverage of the five-dimensional root;
- [x] canonical certificate streams;
- [x] independent verifier not importing the search generator;
- [x] frozen input/stream hashes;
- [x] exact replay of every terminal inequality;
- [x] positive smallest terminal margin;
- [x] all 666 JSON model definitions matched to the pinned Lean definitions;
- [x] upstream one-dimensional model soundness chain identified;
- [x] exact seam-domain structural coverage checked;
- [x] analytic feedback/ledger chain audited as generic in A,B;
- [x] directed arithmetic corrected to use a certified pi upper bound;
- [x] conservative fixed headline `0.67280506` established.

## Remaining release gates

- [ ] source-free full replay outside the generating GitHub CI environment;
- [ ] final broad novelty/priority audit;
- [ ] preferably a Lean kernel integration of the A1294 seam-aware finite
      certificate;
- [ ] final rights/provenance audit and immutable release/DOI deposit.

## Freeze rule

No further A1294 optimization search is authorized.

Do not merge PR #2 or publish a theorem-level release until the external replay
and final release gates pass.

A1294 is now classified:

**CERTIFIED_FINITE_EXACT + CATALOG_IDENTITY_PASS + ANALYTIC_BRIDGE_STRUCTURE_PASS**

This is not a claim of the Riemann Hypothesis.
