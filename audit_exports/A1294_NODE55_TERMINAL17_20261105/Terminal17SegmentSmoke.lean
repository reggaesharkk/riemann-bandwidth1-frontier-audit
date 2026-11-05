import Catalog17AllLookups
import Zeta23.ThmD.Sextuple.CompositionalLeaf
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
open A1294GenericChecker A1294FifteenBridge A1294Compact
noncomputable section
namespace Terminal17SegmentSmoke
def catalog : Array MacroPiece := Catalog17.catalog
theorem catalog_ref_0 : catalog[0]? = some macroPiece2 := by
  exact Catalog17AllLookups.catalog_lookup_0
theorem decode_segment_0 : interpSegment catalog {lo := ⟨195, 32⟩, hi := ⟨250723, 40000⟩, pieceRef := 0} =
    some {lo := (195/32), hi := (250723/40000), piece := macroPiece2} := by
  simp only [interpSegment, catalog_ref_0]
  rfl
theorem source_segment_0 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000)
    {lo := (195/32), hi := (250723/40000), piece := macroPiece2} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece2, MacroPiece.box]
#print decode_segment_0
#print axioms decode_segment_0
#print axioms source_segment_0
end Terminal17SegmentSmoke
