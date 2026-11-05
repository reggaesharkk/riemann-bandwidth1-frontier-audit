# Reproduction and status boundaries

Only GenericGlobalization.lean and GlobalInterface.lean are successful new proof modules. Verify their hashes and recorded successful logs. They require pinned Lean 4.33.0-rc2, upstream fba91d214655aaa1fd0504bb893c8859c20c79f9 and Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. Full toolchain/Mathlib caches are not bundled.

In an isolated directory under `lake env` from the matching pinned project, add this directory to LEAN_PATH and compile GenericGlobalization.lean, then GlobalInterface.lean, with -M 6800 and bounded timeouts. The compiled global theorem has an EXPLICIT unproved root hypothesis. Do not instantiate it with an axiom or Python PASS flag.

GenericGlobalization contains the exact upstream theorem excerpt because the pinned ParametricAdapter object was absent. It retains the original qualified theorem name. Do not import both this excerpt and a later compiled full ParametricAdapter into one Lean environment: they would declare the same name. When the full upstream object is available, integration should use its direct import instead of the excerpt. That compatibility switch has not been built in this audit.

Run verify_audit.py in normal Python, -O and -OO. These checks authenticate local packet bytes, prefix extraction and compiler evidence; they do not prove the root or replace Lean. The frozen V2 archive is included for bounded literal comparison, not permission for a full replay.

Status of other Lean files:

- SourceNode65_failed_v1.lean: FAILED; source_failed_v1.log and source_build.log record the same failed build. Its dependent box proofs contain sorryAx and must not be counted.
- SourceNode65.lean: revised Fin.ext_iff-free source, PREPARED BUT UNTESTED. Its invocation never reached a Lean log because WSL was unresponsive.
- CheckpointSmoke.lean: isolated first checkpoint, PREPARED BUT UNTESTED for the same reason. Its pending Windows client invocation was canceled; no Lean log or resumed build was observed. Any later appearance of such a log requires reassessing this status.
- CombinedTree.lean: UNCOMPILED DRAFT of universal adapters and source-connected replay/chunk lemmas; NOT an accepted tree or proved chunk theorem. It also needs the previous matching CompositionalLeaf/CompositionalRight objects from the preserved compact parent environment. Those facts are intended as leaf Boolean lemmas, not as a replacement for source replay.
- reference/ and upstream/: provenance source copies, not new build successes.

The generator reads the actual first 68 topology bytes and 24 kind/240 anchor bytes from the included hash-pinned archive. It regenerates the revised SourceNode65 file. Full catalog field equality, original archive authentication and Python byte-to-literal conversion remain external. The global anchor stream advances only at quadratic terminals. No further checkpoint variants, subtree selection, WSL restart or full tree run are authorized by this note.
