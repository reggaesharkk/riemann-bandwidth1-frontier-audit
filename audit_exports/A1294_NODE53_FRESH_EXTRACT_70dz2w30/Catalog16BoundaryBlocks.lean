import Catalog16Identity
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
namespace Catalog16BoundaryBlocks
theorem local_block1_0 : Catalog16.block1[0]? = some refinementPiece0 := by rfl
theorem boundary_block1_0 : Catalog16.catalog[22]? = some refinementPiece0 := by
  unfold Catalog16.catalog
  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog16.size0, Catalog16.size1]; decide)]
  rw [Array.getElem?_append_right (by rw [Catalog16.size0])]
  norm_num only [Catalog16.size0, Nat.reduceSub]
  exact local_block1_0
theorem local_block2_0 : Catalog16.block2[0]? = some refinementPiece80 := by rfl
theorem boundary_block2_0 : Catalog16.catalog[94]? = some refinementPiece80 := by
  unfold Catalog16.catalog
  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog16.size0, Catalog16.size1])]
  norm_num only [Array.size_append, Catalog16.size0, Catalog16.size1, Nat.reduceAdd, Nat.reduceSub]
  exact local_block2_0
#print axioms boundary_block1_0
#print axioms boundary_block2_0
end Catalog16BoundaryBlocks
