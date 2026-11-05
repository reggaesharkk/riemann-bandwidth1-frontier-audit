import Source61
open Zeta23.ThmD.Sextuple
namespace Source59
open A1294Source
set_option maxRecDepth 6000
set_option maxHeartbeats 2000000
def path : Path := [(2,false),(1,false),(3,false),(0,false),(4,false),(2,false),(1,false),(3,false),(0,false),(4,false),(2,false),(1,false),(3,false),(0,false),(4,false),(2,true),(1,true),(3,true),(0,true),(4,true),(2,true),(1,true),(3,true),(0,true),(4,true),(2,false),(1,false),(3,false),(0,false),(4,false),(2,true),(1,true),(3,true),(0,true),(4,true),(2,false),(1,true),(3,true),(0,true),(4,true)]
def typedPath : List (Fin 5 × Bool) := [(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,false),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true)]

def parentBox : GapBox := box40
theorem locate59 : locate 59 topologyBytes kindBytes = some (path,19) := by decide
theorem locate60 : locate 60 topologyBytes kindBytes = some (path ++ [(2,false)],19) := by decide
theorem typed_path : decodePath path = some typedPath := by rfl
theorem source_path : walk (initialGapBox 60) typedPath = parentBox := by
  change walk box0 typedPath = box40
  simp only [typedPath, walk]
  rw [checkpoint0, checkpoint1, checkpoint2, checkpoint3, checkpoint4, checkpoint5, checkpoint6, checkpoint7, checkpoint8, checkpoint9, checkpoint10, checkpoint11, checkpoint12, checkpoint13, checkpoint14, checkpoint15, checkpoint16, checkpoint17, checkpoint18, checkpoint19, checkpoint20, checkpoint21, checkpoint22, checkpoint23, checkpoint24, checkpoint25, checkpoint26, checkpoint27, checkpoint28, checkpoint29, checkpoint30, checkpoint31, checkpoint32, checkpoint33, checkpoint34, checkpoint35, checkpoint36, checkpoint37, checkpoint38, checkpoint39]
theorem node59_box : sourceBoxAt 59 = some (parentBox,19) := by
  unfold sourceBoxAt
  rw [locate59]
  change (decodePath path).bind (fun typed => some (walk (initialGapBox 60) typed,19)) = _
  rw [typed_path]
  change some (walk (initialGapBox 60) typedPath,19) = some (parentBox,19)
  rw [source_path]
theorem right_box : parentBox.upperHalf (⟨2,by decide⟩ : Fin 5) = Source61.parentBox := checkpoint40
theorem source_topology : (topologyBytes.drop 59).mapM decodeAffineTreeToken =
    some [.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal] := by rfl
theorem terminal_kinds : (kindBytes[19]?,kindBytes[20]?,kindBytes[21]?,kindBytes[22]?,kindBytes[23]?) = (some 1,some 1,some 1,some 1,some 1) := by rfl
theorem quadratic_cursors : (quadraticIndex 19,quadraticIndex 20,quadraticIndex 21,quadraticIndex 22,quadraticIndex 23) = (19,20,21,22,23) := by rfl
theorem anchors19 : (List.range 5).mapM (anchorCode 19) = some [0,0,16384,0,0] := by rfl
#print axioms node59_box
#print axioms right_box
#print axioms terminal_kinds
#print axioms anchors19
end Source59
