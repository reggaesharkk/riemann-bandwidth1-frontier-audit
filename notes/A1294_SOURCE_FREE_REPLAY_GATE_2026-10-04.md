# A1294 source-free replay gate — 2026-10-04

## Purpose

This is the final independent-environment gate before release packaging.

The replay package contains only:

- the frozen final certificate streams and manifest;
- the three frozen exact catalog JSON inputs;
- a standalone verifier written against the certificate format using only the
  Python standard library.

It does **not** import the search generator, the project `Checker`, or the
GitHub CI verifier.

## Package identity

Local distribution filename:

`A1294_SOURCE_FREE_REPLAY_PACKAGE.zip`

SHA-256:

`14db7449078ff7f60962c1dca8a5bc5ca2b414be2ee66d173870e6f05ffdd124`

Expected immutable certificate identity:

- visited nodes: 13,454,121
- leaves: 6,727,061
- final GitHub certificate artifact ZIP SHA-256:
  `11c1ab1820039284f60e492fe609f6a497175284acdd0c3c53d6ab62b8b1cd19`

## PASS criteria

The external replay must:

1. hash-match all three frozen catalog inputs;
2. hash-match all three canonical certificate streams;
3. reconstruct every deterministic split from the root;
4. consume the topology, terminal-kind, and anchor streams exactly;
5. recompute every terminal inequality using `fractions.Fraction`;
6. reproduce the exact leaf counts;
7. reproduce the exact smallest tail and quadratic margins;
8. end with an empty reconstructed stack and `status: PASS`.

The expected output filename is:

`A1294_SOURCE_FREE_REPLAY_RESULT.json`

## Evidence rule

A PASS generated on the user's Windows ARM64 laptop is evidence independent of
the GitHub runner environment. The result and log must be frozen before the DOI
release bundle is created.

Do not substitute a partial/node-capped run for this gate.
