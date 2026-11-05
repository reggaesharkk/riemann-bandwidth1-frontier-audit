import Zeta23.ThmD.Sextuple.AffineTree
open Zeta23.ThmD.Sextuple
namespace ReplayTransport
theorem transport {α : Type} (check : GapBox → α → Bool)
    (ts ts' : CursorStream AffineTreeToken) (ps ps' : CursorStream α)
    (dt dp : Nat) (ht : ∀ i, ts'.get? (dt+i) = ts.get? i)
    (hp : ∀ i, ps'.get? (dp+i) = ps.get? i)
    {fuel tc pc a b : Nat} {box : GapBox}
    (h : replayAffineTree check ts ps fuel tc pc box = some (a,b)) :
    replayAffineTree check ts' ps' fuel (dt+tc) (dp+pc) box = some (dt+a,dp+b) := by
  induction fuel generalizing tc pc a b box with
  | zero => simp [replayAffineTree] at h
  | succ fuel ih =>
    cases htok : ts.get? tc with
    | none => simp [replayAffineTree, htok] at h
    | some token =>
      cases token with
      | terminal =>
        cases hpay : ps.get? pc with
        | none => simp [replayAffineTree, htok, hpay] at h
        | some value =>
          by_cases hc : check box value = true
          · simp only [replayAffineTree, htok, hpay, hc, ite_true, Option.some.injEq, Prod.mk.injEq] at h
            rcases h with ⟨rfl,rfl⟩
            simp only [replayAffineTree, ht, hp, htok, hpay, hc, ite_true, Nat.add_assoc]
          · simp [replayAffineTree, htok, hpay, hc] at h
      | split axis =>
        cases hleft : replayAffineTree check ts ps fuel (tc+1) pc (box.lowerHalf axis) with
        | none => simp [replayAffineTree, htok, hleft] at h
        | some cursors =>
          have hl := ih hleft
          have hr : replayAffineTree check ts ps fuel cursors.1 cursors.2 (box.upperHalf axis) = some (a,b) := by
            simpa only [replayAffineTree, htok, hleft] using h
          have rr := ih hr
          simp only [replayAffineTree, ht, htok]
          rw [show dt+tc+1 = dt+(tc+1) by omega, hl]
          exact rr
#print axioms transport
end ReplayTransport
