import Catalog18Lookup
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
namespace Catalog18
theorem local_57 : block1[0]? = some refinementPiece75 := by rfl
theorem boundary_57 : catalog[57]? = some refinementPiece75 := by
  unfold catalog
  rw [Array.getElem?_append_left (by rw [Array.size_append, size0, size1]; decide)]
  rw [Array.getElem?_append_right (by rw [size0]; decide)]
  norm_num only [size0, Nat.reduceSub]
  exact local_57
#print axioms boundary_57
theorem local_114 : block2[0]? = some refinementPiece135 := by rfl
theorem boundary_114 : catalog[114]? = some refinementPiece135 := by
  unfold catalog
  rw [Array.getElem?_append_right (by rw [Array.size_append, size0, size1]; decide)]
  norm_num only [Array.size_append, size0, size1, Nat.reduceAdd, Nat.reduceSub]
  exact local_114
#print axioms boundary_114
end Catalog18
