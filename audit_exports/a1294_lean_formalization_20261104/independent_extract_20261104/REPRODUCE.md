# Reproduction instructions

## Verify packet inputs

1. Run `python scripts/verify_packet.py` to verify `SHA256SUMS.json` and test the ZIP CRC of
   `source/input_v2/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip`.
2. Extract the V2 ZIP to a temporary directory and run its `preflight.py` from the package
   directory. The recorded preflight is metadata-only; do not confuse it with the full
   source-free replay.
3. Run `scripts/compare_catalogs.py <extracted-V2-root> <pinned-zeta23-root>` to reproduce
   the exact 56 + 216 + 394 catalog field comparison.
4. Run `scripts/extract_tail_subtree.py <extracted-V2-root> <output.json>` to reproduce the
   selected tail terminal and path. It reads the serialized topology prefix through that
   node and checks the source's weighted split-axis rule. It does not evaluate quadratic
   terminal payloads.

To verify the outer packet archive, run
`python scripts/verify_archive.py <packet.zip> <new-empty-directory>`. It tests the outer
ZIP CRC, checks paths before extraction, extracts the archive, and verifies each manifested
file. `scripts/create_packet_zip.py` documents the non-overwriting archive creation step.

## Rebuild the Lean pilot

The packet contains the exact `zeta23` project lockfiles and relevant upstream Lean source
modules, but does not vendor Mathlib's 7.2 GB working tree/cache. Restore Mathlib at the
revision in `lake-manifest.json` (`51e6992efd06126df61a496bebf8f49482a4e129`) and use
`leanprover/lean4:v4.33.0-rc2` only.

From the `zeta23` project root:

```sh
elan run leanprover/lean4:v4.33.0-rc2 lake exe cache get
elan run leanprover/lean4:v4.33.0-rc2 lake build Zeta23.ThmD.Sextuple.AffineTree
```

Copy `A1294Pilot.lean` to `Zeta23/ThmD/Sextuple/A1294Pilot.lean`, then run:

```sh
elan run leanprover/lean4:v4.33.0-rc2 lake build Zeta23.ThmD.Sextuple.A1294Pilot
```

The successful build log includes `#print axioms` output for each pilot theorem and the
upstream `sextupleEnergy_nonneg` lemma. Review it for the absence of `sorryAx` and custom
axioms.

The prior source-free full replay result is included as historical evidence. It reports
13,454,121 visited nodes and 6,727,061 leaves, but the full replay was not rerun for this
pilot. Do not infer full A1294 kernel verification from that Python result or from the
successful small Lean build.
