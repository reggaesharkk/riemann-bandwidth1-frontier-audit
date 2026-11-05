import Source59
open Zeta23.ThmD.Sextuple
namespace Source57
open A1294Source
set_option maxRecDepth 6000
set_option maxHeartbeats 2000000
def path : Path := [(2,false),(1,false),(3,false),(0,false),(4,false),(2,false),(1,false),(3,false),(0,false),(4,false),(2,false),(1,false),(3,false),(0,false),(4,false),(2,true),(1,true),(3,true),(0,true),(4,true),(2,true),(1,true),(3,true),(0,true),(4,true),(2,false),(1,false),(3,false),(0,false),(4,false),(2,true),(1,true),(3,true),(0,true),(4,true),(2,false),(1,true),(3,true),(0,true)]
def typedPath : List (Fin 5 × Bool) := [(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,false),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true)]

def parentBox : GapBox := box39
theorem locate57 : locate 57 topologyBytes kindBytes = some (path,18) := by decide
theorem locate58 : locate 58 topologyBytes kindBytes = some (path ++ [(4,false)],18) := by decide
theorem typed_path : decodePath path = some typedPath := by rfl
theorem source_path : walk (initialGapBox 60) typedPath = parentBox := by
  change walk box0 typedPath = box39
  simp only [typedPath, walk]
  rw [checkpoint0, checkpoint1, checkpoint2, checkpoint3, checkpoint4, checkpoint5, checkpoint6, checkpoint7, checkpoint8, checkpoint9, checkpoint10, checkpoint11, checkpoint12, checkpoint13, checkpoint14, checkpoint15, checkpoint16, checkpoint17, checkpoint18, checkpoint19, checkpoint20, checkpoint21, checkpoint22, checkpoint23, checkpoint24, checkpoint25, checkpoint26, checkpoint27, checkpoint28, checkpoint29, checkpoint30, checkpoint31, checkpoint32, checkpoint33, checkpoint34, checkpoint35, checkpoint36, checkpoint37, checkpoint38]
theorem node57_box : sourceBoxAt 57 = some (parentBox,18) := by
  unfold sourceBoxAt
  rw [locate57]
  change (decodePath path).bind (fun typed => some (walk (initialGapBox 60) typed,18)) = _
  rw [typed_path]
  change some (walk (initialGapBox 60) typedPath,18) = some (parentBox,18)
  rw [source_path]
theorem right_box : parentBox.upperHalf (⟨4,by decide⟩ : Fin 5) = Source59.parentBox := checkpoint39
theorem source_topology : (topologyBytes.drop 57).mapM decodeAffineTreeToken =
    some [.split 4,.terminal,.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal] := by rfl
theorem terminal_kinds : (kindBytes[18]?,kindBytes[19]?,kindBytes[20]?,kindBytes[21]?,kindBytes[22]?,kindBytes[23]?) = (some 1,some 1,some 1,some 1,some 1,some 1) := by rfl
theorem quadratic_cursors : (quadraticIndex 18,quadraticIndex 19,quadraticIndex 20,quadraticIndex 21,quadraticIndex 22,quadraticIndex 23) = (18,19,20,21,22,23) := by rfl
theorem anchors18 : (List.range 5).mapM (anchorCode 18) = some [0,0,0,0,0] := by rfl
#print axioms node57_box
#print axioms right_box
#print axioms terminal_kinds
#print axioms anchors18
end Source57
