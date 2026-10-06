# WP84 — full changed-notes/source audit (2026-10-06)

Status: **REPOSITORY-COVERAGE AUDIT; NO UNCONDITIONAL ZERO-PROPORTION THEOREM ESTABLISHED**

## Audit basis and coverage

PR #5 was open, draft, unmerged at start head
`cd6e39e67d95d16db337dd1557eae7b20820a5a5`. Its 456 changed paths comprise
244 notes, 185 Python sources, 25 workflows, and 2 certificates. The full text
of all 244 notes and 185 sources was fetched at that head and indexed. All 185
Python sources passed `compileall`.

This is a repository-wide content and reproducibility audit, not a
line-by-line independent proof of every analytic lemma. The active proof
interfaces and every changed source were checked for status, dependencies,
cross-references, and executable behavior.

## Reproduction results

The 127 WP84 scripts were run without arguments under per-script time limits.
Before the repair recorded below, 87 passed; 30 could not import SymPy, 2
could not import mpmath, 5 timed out, one correctly requested explicit m7/m8
inputs, one failed because its asserted pinned source
`upstream/gpu/exact_connected.py` was unavailable at the audited repository
head, and one failed a false smoke threshold. The workflows that install the
higher-moment dependencies install SymPy; the missing packages here are a
limitation of this execution environment.

The 58 other changed scripts were also attempted: 42 passed, 10 correctly
required their documented data/CLI inputs, 4 were blocked by unavailable
dependencies or input data, and 2 timed out.

The false smoke threshold in
`src/wp84_infinitesimal_prime_blocks.py` asserted that a finite dyadic sum
was below 100, although it computes 195.87058680741777. The convergence
argument in the note is unaffected. Commit
`a8fb19eec7e76959e213bc9baf77a02dd432b41f` changes the assertion to a loose
195–200 diagnostic range and removes the script's claim that it emits a
rigorous infinite-sum bound. The repaired script was rerun and passes. This
script remains a numerical diagnostic, not the proof of convergence.

## Documentation and audit-trail defects

Fourteen changed Markdown files contain literal backslash-n sequences instead
of actual line breaks, causing the documents to render as one long line. This
includes active proof-interface notes. The affected paths are:

- `notes/WP71_JFIRST_GENERIC_LOCAL_FACTOR.md`
- `notes/WP71_JFIRST_LOCAL_AUDIT.md`
- `notes/WP71_JFIRST_PADIC_LIFT.md`
- `notes/WP71_JFIRST_SPECIAL_LOCAL_LEVEL1.md`
- `notes/WP83_EC_STAR_HOSTILE_AUDIT.md`
- `notes/WP83_FAR_FIELD_DECOUPLING.md`
- `notes/WP83_FULL_LATTICE_FROBENIUS_ENERGY.md`
- `notes/WP83_LOCAL_COUNT_ECSTAR_INSUFFICIENCY.md`
- `notes/WP83_MV_INGHAM_CLUSTER_BRIDGE.md`
- `notes/WP83_PT_STAR_COUNTEREXAMPLE.md`
- `notes/WP84_BOUNDED_RESOLVENT_CONSUMER.md`
- `notes/WP84_INFINITESIMAL_PRIME_BLOCKS.md`
- `notes/WP84_LOCALIZATION_SZEGO_AUDIT.md`
- `notes/WP84_R3_FIXED_POLE_CERTIFICATE.md`

The following audit records embed earlier internal PR heads and do not audit
the current head: `WP84_CURRENT_MISSING_INPUT_AUDIT_2026_10_06.md`
(2b1780e7…), `WP84_R400_ZERO_SIDE_TRANSFER_SOURCE_AUDIT_2026_10_06.md`
(a295c0fc…), `WP84_DELTA144_STRICT_MARGIN_AUDIT_2026_10_06.md`
(d3ff5511…), and `WP84_UNCONDITIONAL_THEOREM_CHAIN_REVIEW_2026_10_06.md`
(4e032b97…). Their recorded historical bases should remain intact; this note
does not relabel them as current-head reviews.

## Canonical route conflict

The notes do not give one consistent active attack contract:

- The missing-input audit at head 2b1780e7 identifies the fixed-δ, six-pole
  bounded Christoffel/Bernoulli-resolvent inequality as active. Its remaining
  bound is the integrated actual-state aggregate involving
  `E tau(R_t P R_t)` and `E Psi_res(R_t,z_j)`.
- The final section of the large `WP84_RESOLVENT_KILL_GATE_2026_10_05.md`
  instead labels the shifted one-point rank-six energy /
  differentiated-`T12` inequality as the active >79/full-frontier
  obstruction.

These are distinct analytic routes. The user's explicit project instruction
selects the shifted exact-frontier one-point rank-six/heat-curvature route as
the primary attack. Treat the fixed-parameter six-pole family as a separate
bounded-resolvent route and R=400 as the lower-risk conditional route, not as
substitutes for the selected primary target. Their exact/model algebra does
not make the arithmetic transport theorem automatic.

## Mathematical status after audit

1. The exact Christoffel/Hankel consumers, fixed-matrix displacement
   identities, and finite regression calculations establish model or
   finite-algebra facts.
2. The R=400 assembly computes the conditional coefficient
   68.82027318675% from its stated bounds. The source/normalization audit still
   says the prime-side full-to-band, fixed-band covariance, and complete
   degree-four estimates are conditional. This is not an unconditional
   68.82% theorem.
3. The 79.62709668% value is an exact moment/model frontier. The actual
   large-`T` arithmetic resolvent/positive-energy transport remains open.
4. The script repair above fixes a false diagnostic failure; it does not close
   either arithmetic gap.

The current theorem-grade obstruction is the missing asymptotic comparison
between the actual prime-state resolvent evolution and the model consumer.
Finite algebra, exact rational ledgers, and small numerical residuals do not
supply that comparison.
