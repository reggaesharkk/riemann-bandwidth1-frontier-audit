# Compact semantic correspondence: partial result

The new theorem A1294Compact.compactSegmentCheck_sound is kernel checked. CompactRat uses Int/Nat fields; its executable validity check requires positive denominator and coprimality. interpRat is exact rational division. CompactSegment stores rational endpoints and a Nat catalog reference. interpSegment resolves the reference into the actual upstream MacroPiece, returning none for an invalid reference. compactSegmentCheck includes rational checks and the previously proved certifiedPiecewiseCheck on the interpreted singleton interval. The soundness theorem derives the actual mtKernel lower bound for every real point of the interpreted interval. No model soundness premise is supplied externally.

This is a segment-level semantic theorem only. The catalog is a parameter, not yet a formally connected pinned 666-entry table. The proof does not establish concrete source acceptance. No authentic segment instance, complete compact leaf, or compact two-leaf parent has yet been checked in this revision. The old parent theorem is preserved and is not used to discharge the new checker.

First exact remaining obligation: define interpQuadraticLeaf so that its fifteen interpreted rows (including direct rank models, segmented floors and zero terms) yield a Fin 15 -> RankOneModel; prove its executable model checks imply every one of the fifteen pointwise energy bounds required by rankTangentCheck_energy_sound, and then check actual source data. This is unfinished implementation/proof work, not a demonstrated mathematical impossibility. interpBox, interpAnchor, pinned catalog correspondence, source-prefix decoder, concrete acceptance and adversarial rejection tests remain unimplemented here.

COMPACT_REPRESENTATION_IMPLEMENTED: PARTIAL_RATIONAL_AND_SEGMENT
SEMANTIC_INTERPRETATION_SOUND: SEGMENT_ONLY_KERNEL_PROVED
FIFTEEN_MODEL_CORRESPONDENCE_KERNEL_PROVED: OPEN
CONCRETE_COMPACT_LEAF_ACCEPTED: NO
COMPACT_TWO_LEAF_PARENT_KERNEL_PROVED: NO_NEW_COMPACT_PROOF
STEP_INDEXED_DECODER_KERNEL_PROVED: NO
SOURCE_PREFIX_CORRESPONDENCE: EXTERNAL_ONLY
ADVERSARIAL_REJECTION_TESTS: NOT_RUN
SOURCE_AND_OLEAN_COMPRESSION_RATIO: NOT_ESTABLISHED_NO_CONCRETE_CERTIFICATE
ACTUAL_PEAK_MEMORY: 5587860 KiB; successful build elapsed 71.51 seconds
FULL_CERTIFICATE_SCALING_FEASIBILITY: OPEN
FULL_A1294_THEOREM_STATUS: NOT_YET_PROVED

Successful build_v3.log reports exit 0 and only propext, Classical.choice, Quot.sound for compactSegmentCheck_sound. Failed initial source and logs are retained. The virtual-memory-limited build failed while reading a mapped Mathlib object; it was not a mathematical rejection. The successful run had a 240-second time bound; a reliable physical-RSS limiter has not been demonstrated. No larger compilation was attempted.

Environment: Lean 4.33.0-rc2, upstream fba91d214655aaa1fd0504bb893c8859c20c79f9, Mathlib 51e6992efd06126df61a496bebf8f49482a4e129. Existing two-leaf source remains hash 338c8f6a3a4eadc10a013a932fe6ea6a16a14ca7259bdc7e956bc5cf41a3cee0. authentic_input.json and frozen_source_inventory.json are external evidence, not Lean byte-decoding proofs. All old packets remain unchanged. WP84 findings remain frozen.
