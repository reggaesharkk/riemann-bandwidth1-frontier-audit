import Catalog17Identity
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
namespace Catalog17BoundaryBlocks
theorem local_block1_0 : Catalog17.block1[0]? = some refinementPiece0 := by rfl
theorem boundary_block1_0 : Catalog17.catalog[21]? = some refinementPiece0 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]
  rw [Array.getElem?_append_right (by rw [Catalog17.size0])]
  norm_num only [Catalog17.size0, Nat.reduceSub]
  exact local_block1_0
theorem local_block2_0 : Catalog17.block2[0]? = some refinementPiece87 := by rfl
theorem boundary_block2_0 : Catalog17.catalog[98]? = some refinementPiece87 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog17.size0, Catalog17.size1])]
  norm_num only [Array.size_append, Catalog17.size0, Catalog17.size1, Nat.reduceAdd, Nat.reduceSub]
  exact local_block2_0
#print boundary_block1_0
#print boundary_block2_0
#print axioms boundary_block1_0
#print axioms boundary_block2_0
end Catalog17BoundaryBlocks
