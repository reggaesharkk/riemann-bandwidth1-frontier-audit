# Node-65 closure attempt — blocked before Lean

Research owner: Prince. 2026-11-04. No new mathematical proof is claimed.

## Environment result

The approved, unsandboxed WSL invocation was:

`wsl -e bash -lc 'cd /home/reggaeshark/a1294_lean_formalization_20261104/formal-math/zeta23 && lean --version && lake --version && printf "WSL_RESPONSIVE\n"'`

It returned no output from its launch at 23:04:40 +05:30 through cancellation at 23:07:46 +05:30 (over 186 seconds). It did not reach a compiler version response or a Lean build. Only the identified clients for this audit were canceled, with command lines and creation times preserved in wsl_pending_clients.json. The tool session exited 1 after client cancellation; that is NOT a Lean build exit or a mathematical rejection. No WSL restart, service termination, unrelated job termination, reinstall or Mathlib rebuild occurred.

The native Windows compiler did respond:

Lean 4.33.0-rc2, x86_64-w64-windows-gnu, compiler d8b18978322de05a8f3dba51ef03cf5461676c17, Release.

That verifies only the host compiler, not availability of its matching Mathlib/upstream environment. The two known export-cache paths under the earlier delivery source copy lacked Mathlib.olean and AffineTree.olean. This is NOT a claim that all research files or all host caches are absent. No broad personal-directory scan was performed, and no alternative dependency version was substituted.

## Gated proof status

CheckpointSmoke.lean, SourceNode65.lean and CombinedTree.lean were copied unchanged into this separate additive directory. Gate 1 never reached Lean, so the prepared checkpoint proof was not compiled or rejected. It would be incorrect to claim that the revised proof failed, that a targeted repair passed, or that any later gate ran. The old historical recursion failure remains historical evidence in the preserved predecessor packet.

The next exact mathematical expression is still:

`box0.lowerHalf (⟨2, by decide⟩ : Fin 5) = box1`.

Here box0 is initialGapBox 60 and box1 has coordinate 2 in [0,30], all other coordinates in [0,60]. There is no newly normalized compiler goal because no compiler ran in this audit. Targeted coordinate proof repair must wait for a responsive matching environment and an actual smoke-build result. No maximum recursion depth was raised and no previous boxes were recursively unfolded again.

| Required decision | Status |
|---|---|
| CHECKPOINT0_KERNEL_PROVED | NOT_VERIFIED; environment blocked before compilation |
| ALL_43_PATH_CHECKPOINTS_PROVED | OPEN; not run |
| SOURCE_NODE65_BOX_KERNEL_PROVED | OPEN; not run |
| COMBINED_THREE_NODE_REPLAY_ACCEPTED | OPEN; not run |
| NODE65_SOURCE_CONNECTED_PREDICATE_PROVED | OPEN |
| CURSOR_EXHAUSTION_PROVED | OPEN for this source-connected replay; upstream generic facts unchanged |
| EXTERNAL_AUTHENTICATION_BOUNDARY | UNCHANGED: byte-to-literal/catalog identity/hash authentication remain external |
| ROOT_BOX_PREDICATE_STATUS | OPEN |
| FULL_A1294_THEOREM_STATUS | NOT_YET_PROVED |

The already proved global theorem conditional on the complete root predicate remains unchanged and was not rederived. The root hypothesis was not asserted. Existing compact leaf/parent and standalone results are preserved. Source terminal and quadratic-anchor cursors remain distinct in the supplied source; no cursor semantics were changed here.

## Resource and preservation evidence

New Lean build exits, objects, axiom reports, compilation time, proof RSS and major faults: all unavailable, because no Lean build began. Native compiler version query: successful. WSL client cancellation: exit 1. The packet tests check integrity/status only, not mathematical acceptance.

The predecessor packet remains SHA-256 151048a061e5aef71befb0150c6d44e034855171c9b5c7949ac875e7eabf53ba. Its source hashes bind the successful GenericGlobalization/GlobalInterface sources, objects and logs. preserve_inputs.py verifies those original files against that inventory and checks that the three copied proof sources match their originals exactly. Both research worktrees retain clean tracked-file status.

A responsive WSL session with the already installed pinned dependencies is the immediate prerequisite. Under the current prohibition on restarting WSL or rebuilding dependencies there is no authorized environment repair to perform. Stop here. No later checkpoint, subtree, full-tree replay, API call, push, merge, publication, license change or destructive file operation was attempted.
