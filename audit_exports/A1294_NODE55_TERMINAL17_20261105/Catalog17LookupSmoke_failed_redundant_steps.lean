import Catalog17Identity
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
namespace Catalog17LookupSmoke
theorem catalog_0 : Catalog17.catalog[0]? = some macroPiece2 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]
  rw [Array.getElem?_append_left (by rw [Catalog17.size0]; decide)]
  rfl
theorem original_0 : Catalog17.original[0]? = some macroPiece2 := by
  rw [Catalog17Identity.original_eq_catalog]
  exact catalog_0
#print axioms original_0
theorem catalog_20 : Catalog17.catalog[20]? = some macroPiece31 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]
  rw [Array.getElem?_append_left (by rw [Catalog17.size0]; decide)]
  rfl
theorem original_20 : Catalog17.original[20]? = some macroPiece31 := by
  rw [Catalog17Identity.original_eq_catalog]
  exact catalog_20
#print axioms original_20
theorem catalog_21 : Catalog17.catalog[21]? = some refinementPiece0 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]
theorem original_21 : Catalog17.original[21]? = some refinementPiece0 := by
  rw [Catalog17Identity.original_eq_catalog]
  exact catalog_21
#print axioms original_21
theorem catalog_97 : Catalog17.catalog[97]? = some refinementPiece86 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]
  rw [Array.getElem?_append_right (by rw [Catalog17.size0]; decide)]
  norm_num only [Catalog17.size0, Nat.reduceSub]
  rfl
theorem original_97 : Catalog17.original[97]? = some refinementPiece86 := by
  rw [Catalog17Identity.original_eq_catalog]
  exact catalog_97
#print axioms original_97
theorem catalog_98 : Catalog17.catalog[98]? = some refinementPiece87 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]
theorem original_98 : Catalog17.original[98]? = some refinementPiece87 := by
  rw [Catalog17Identity.original_eq_catalog]
  exact catalog_98
#print axioms original_98
theorem catalog_174 : Catalog17.catalog[174]? = some refinementPiece167 := by
  unfold Catalog17.catalog
  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]
  norm_num only [Array.size_append, Catalog17.size0, Catalog17.size1, Nat.reduceAdd, Nat.reduceSub]
  rfl
theorem original_174 : Catalog17.original[174]? = some refinementPiece167 := by
  rw [Catalog17Identity.original_eq_catalog]
  exact catalog_174
#print axioms original_174
end Catalog17LookupSmoke
