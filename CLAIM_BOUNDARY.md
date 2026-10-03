# Claim boundary

This file is permanent project policy.

- This repository does **not** claim the Riemann Hypothesis.
- It does **not** claim that all zeros lie on the critical line.
- Numerical optimization is not a theorem.
- No new constant is claimed until its analytic dependencies, finite certificate, independent verifier, replay, and literature novelty check all pass.
- Every conditional input must be labeled conditional at the point of use.
- A machine-checked finite implication must be distinguished from external analytic hypotheses.
- A branch audit or a reported external replay is evidence to inspect; it is not our independent replay.
- An arXiv preprint, open pull request, numerical certificate, and peer-reviewed theorem are separate evidence classes.
- The ceiling for a certificate class is not an achieved lower bound.
- A decimal comparison is not an analytic proof.

Allowed descriptions for current material:
- Alpöge–Furman baseline: unconditional theorem stated in arXiv and accompanied by a Lean formalization; upstream proof not rebuilt by this project yet.
- Montgomery–Taylor constants: exact source formulas evaluated here with rigorous rational intervals.
- A1290: public open-PR Lean source candidate with source-reported build and axiom audits; no independent local Lean replay here.
- A1293/100000: source-reported external replay whose serialized streams are not committed in the cited branch; unverified by this project.
- Bandwidth-one ceiling near 0.6818287: conditional on external EnclOK enclosures; not an unconditional achieved density.
