import Init
universe u
namespace CatalogArrayIdentity
variable {α : Type u}

theorem toArray_append3 (xs ys zs : List α) :
    ((xs ++ ys) ++ zs).toArray = (xs.toArray ++ ys.toArray) ++ zs.toArray := by
  rw [← List.append_toArray, ← List.append_toArray]

variable (a0 a1 a2 a3 a4 a5 : α)
theorem six_split :
    #[a0, a1, a2, a3, a4, a5] =
      (#[a0, a1] ++ #[a2, a3]) ++ #[a4, a5] := by
  change (([a0, a1, a2, a3, a4, a5] : List α).toArray) =
    (([a0, a1].toArray ++ [a2, a3].toArray) ++ [a4, a5].toArray)
  exact toArray_append3 [a0, a1] [a2, a3] [a4, a5]

variable (a0 a1 a2 a3 a4 a5 a6 a7 a8 : α)
theorem nine_split :
    #[a0, a1, a2, a3, a4, a5, a6, a7, a8] =
      (#[a0, a1, a2] ++ #[a3, a4, a5]) ++ #[a6, a7, a8] := by
  change (([a0, a1, a2, a3, a4, a5, a6, a7, a8] : List α).toArray) =
    (([a0, a1, a2].toArray ++ [a3, a4, a5].toArray) ++ [a6, a7, a8].toArray)
  exact toArray_append3 [a0, a1, a2] [a3, a4, a5] [a6, a7, a8]
end CatalogArrayIdentity
#print axioms CatalogArrayIdentity.toArray_append3
#print axioms CatalogArrayIdentity.six_split
#print axioms CatalogArrayIdentity.nine_split
