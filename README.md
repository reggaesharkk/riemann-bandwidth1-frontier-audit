# Riemann Bandwidth-One Frontier Audit

A reproducible investigation of finite Weil-form and matrix certificates for unconditional lower bounds on the proportion of simple nontrivial zeros of the Riemann zeta function lying on the critical line.

Operating rule:

**BUILD → FORMALIZE → COMPUTE → BREAK → CERTIFY → REPLAY → FREEZE**

This repository starts with the literature frontier and a small source-backed constant replay. It does not claim a new density bound.

## Current snapshot

- Research branch: research/bandwidth1-v0.1
- Scope: phases 0 and 1; reproduce published constants from source, then specify the certificate class.
- No optimizer or heavy computation is included.
- See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md), [PROJECT_STATE.md](PROJECT_STATE.md), [UPSTREAM_PROVENANCE.md](UPSTREAM_PROVENANCE.md), and [LITERATURE_LEDGER.md](LITERATURE_LEDGER.md).

## Reproduce the arithmetic replay

Requires Python 3.11+; the replay implementation uses only the standard library and exact fractions.

```sh
python src/replay_alpoge_furman.py --output research/rh_bandwidth1_20261003/replay.json
python -m unittest discover -s tests -v
```

The interval calculation encloses the transcendental Montgomery–Taylor expression using rational bisection and alternating Taylor bounds. The tests exercise exact finite-dimensional identities and synthetic cases of the matrix inequality. They do not independently prove the analytic number-theory inputs or replay the full upstream Lean development.

## Project map

- `research/rh_bandwidth1_20261003/`: source notes, derivations, certificate specification, and replay outputs.
- `src/`: transparent arithmetic replay.
- `tests/`: exact arithmetic and finite matrix pilot tests.
- `results/replay/`: generated snapshot.
- `.github/workflows/`: lightweight replay tests only.

The other requested directories will be added when they contain actual certificates, adversarial cases, Lean code, or a standalone verifier.
