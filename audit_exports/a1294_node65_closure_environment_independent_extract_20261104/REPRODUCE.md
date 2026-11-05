# Integrity and next gate

Verify SHA256SUMS.txt, then run preserve_inputs.py in a disposable copy. Repeat with -O and -OO. This confirms byte preservation and the recorded environment/status distinction; it does not compile Lean or establish any new theorem. The embedded predecessor ZIP retains the successful global sources/objects/logs and its earlier failed/draft work.

Before any proof command, the existing WSL pinned project must respond to `lean --version` and `lake --version`. No compiler output was obtained from WSL in this attempt. Native Windows Lean responds, but no matching native Mathlib environment has been established by this audit. Do not download, reinstall, rebuild Mathlib, restart WSL or change dependencies as an implicit workaround.

Once the matching existing environment is responsive, compile the unchanged CheckpointSmoke.lean first, writing only new logs/objects. If the proof fails, preserve the exact error and use targeted coordinate reasoning before running SourceNode65.lean. Do not launch SourceNode65 or CombinedTree until preceding gates pass cleanly. All prepared files here are UNVERIFIED for this attempt; no default PASS premise or root axiom is provided.

The precise pending checkpoint is box0.lowerHalf (2 : Fin 5) = box1, where box0 = initialGapBox 60. The broader required source-connected subtree and complete root predicate remain open. No larger subtree is authorized by this reproduction note.
