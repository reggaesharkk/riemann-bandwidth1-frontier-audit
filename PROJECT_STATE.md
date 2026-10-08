# Project state — 2026-10-03

## Current branch

Research is isolated on `research/bandwidth1-v0.1`. The `main` branch remains reserved for frozen and replayable milestones.

## Previous branch disposition

The prior Nyman–Beurling/divisor-cancellation exploration was frozen after:
- exact first-block divisor structure was derived;
- the Pareto tradeoff was weak;
- the generalized operator response did not reveal a stable tiny-dimensional mechanism.

Status: `FROZEN_EXPLORATORY_BRANCH_NOT_USED_AS_INPUT_TO_CURRENT_THEOREM`.

The prior R0.12/R0.13 files are provenance only. They are not inputs to any theorem or computation in this repository.

## Current work

- Phase 0: literature audit recorded in LITERATURE_LEDGER.md.
- Phase 1: source reconstruction and formula replay documented under research/rh_bandwidth1_20261003/.
- Formula replay: exact base constants and rational intervals for the Montgomery–Taylor constants and the conditional PairCeiling law fraction.
- Synthetic algebra tests: finite trace, Hilbert–Schmidt, symmetry, and rank–trace/inertia examples.
- No source Lean project has been cloned or rebuilt by this project.
- No public A1290/A1293 result is represented as an independently replayed theorem.

## Gates

- Literature inventory: PASS WITH OPEN NOVELTY CHECK. A1290 and A1293 source artifacts still require independent replay and a last-minute literature search before any new claim.
- Constant arithmetic replay: PASS when the test workflow runs successfully; exact status is recorded in replay.json.
- Full AF theorem machinery replay: NOT PASSED. The proof dependency chain is reconstructed from the paper, but upstream Lean/analytic derivations are not independently rebuilt.
- Certificate-class specification: recovered in CERTIFICATE_SPEC.md, with the external EnclOK limitation explicit.
- Small baseline pilot: PASS for constant arithmetic and synthetic matrix cases only.
- Heavy optimization: NOT AUTHORIZED. No optimizer is implemented or run.
