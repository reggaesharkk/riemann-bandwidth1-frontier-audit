# Reproduce the independent leaf

Verify SHA256SUMS.txt first. Run verify_source.py and verify_packet.py in normal Python, -O and -OO. These external checks verify provenance, data reconstruction and recorded proof outputs; they do not replace Lean.

Pinned environment: Lean leanprover/lean4:v4.33.0-rc2, compiler d8b18978322de05a8f3dba51ef03cf5461676c17; upstream formal-math fba91d214655aaa1fd0504bb893c8859c20c79f9; Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. The toolchain and full 8-GB imported module artifact closure are not bundled. Use the matching installed environment. Source excerpts/locks are retained under upstream and exact complete import-source inventories are included.

The new proof modules are top-level StandaloneCore.lean and StandaloneTerminal22.lean, deliberately outside the historical Zeta23 concrete-acceptance namespace. From the pinned zeta23 project, run `lake env bash /path/to/this-packet/build.sh`. The script adds only this experiment's root to LEAN_PATH, compiles core then leaf, caps allocation at -M 6800, and times out each process after 240 seconds. It does not modify the pinned checkout or import an old acceptance module. Read-only matching upstream objects must be available on Lake's normal search path.

For deterministic regeneration, run generate.py in a disposable copy and verify the generated source hashes against source_hashes.json. It needs authentic_input.json, GenericReference.lean and the preserved baseline source for the unchanged tangent proof template. That template is Lean proof text, not an imported theorem or an externally asserted result: its exact arithmetic is checked afresh. The generator outputs interned typed data, unique segment checks and concrete Boolean lemmas, not decompressed old Lean source.

For a separate old-version timing comparison only, baseline_and_audit.sh compiles the exact old source and runs two independent import inventories. The old import audit uses the previously compiled matching original object from the installed environment; its module is never present in the new theorem's import set. resolve_closure.py and complete_closure.py stat object companions and hash source files from the environment. complete_closure.py contains the exact local pinned toolchain path used in this experiment; adapt that path for another host. Do not sum audit build times into acceptance build times or compare a warm leaf alone against a self-contained old proof.

SourcePath.lean and SourcePath_v2.lean are FAILED bounded path-normalization attempts; their logs are intentionally bundled. Neither is an acceptance proof or dependency. Do not count the emitted failed theorem/any sorryAx axiom report as success. There is no instruction to keep trying these files or to run a larger subtree.

All historical inputs remain read only. No remote access, provider call, private key, publication or full certificate replay is needed or authorized by this reproduction note.
