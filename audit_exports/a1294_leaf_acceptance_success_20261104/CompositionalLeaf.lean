import Zeta23.ThmD.Sextuple.AffineTree
import Zeta23.ThmD.Sextuple.Macro.AffineAdapter
import Zeta23.ThmD.Sextuple.A1275.RefinementData

open Zeta23.ThmD.Sextuple
open Zeta23.ThmD.Sextuple.MacroPrototype

noncomputable section

namespace A1294GenericChecker

def clampRational (q lo hi : ℚ) : ℚ :=
  if q < lo then lo else if hi < q then hi else q

def segmentMinimum (piece : MacroPiece) (lo hi : ℚ) : ℚ :=
  match piece with
  | .base p => p.a + p.c * (clampRational p.q lo hi - p.q) ^ 2
  | .well p => match p.side with
      | .left => 2 * (p.v + p.m * (p.q - hi)) ^ 2
      | .right => 2 * (p.v + p.m * (lo - p.q)) ^ 2

theorem clampRational_sq_le (q lo hi : ℚ) {x : ℝ}
    (hord : lo ≤ hi) (hlo : (lo : ℝ) ≤ x) (hhi : x ≤ (hi : ℝ)) :
    (((clampRational q lo hi - q) ^ 2 : ℚ) : ℝ) ≤
      (x - (q : ℝ)) ^ 2 := by
  by_cases hqlo : q < lo
  · simp [clampRational, hqlo]
    have hdist : ((lo : ℚ) : ℝ) - (q : ℚ) ≤ x - (q : ℝ) := by
      exact sub_le_sub_right hlo (q : ℝ)
    have hnonneg : 0 ≤ ((lo : ℚ) : ℝ) - (q : ℚ) := by
      exact_mod_cast sub_nonneg.mpr (le_of_lt hqlo)
    have hdiff : 0 ≤ (x - (q : ℝ)) - (((lo : ℚ) : ℝ) - (q : ℚ)) := sub_nonneg.mpr hdist
    have hsum : 0 ≤ (x - (q : ℝ)) + (((lo : ℚ) : ℝ) - (q : ℚ)) := by linarith
    nlinarith [mul_nonneg hdiff hsum]
  · by_cases hhiq : hi < q
    · simp [clampRational, hqlo, hhiq]
      have hdist : ((q : ℚ) : ℝ) - (hi : ℚ) ≤ (q : ℝ) - x := by
        exact sub_le_sub_left hhi (q : ℝ)
      have hnonneg : 0 ≤ ((q : ℚ) : ℝ) - (hi : ℚ) := by
        exact_mod_cast sub_nonneg.mpr (le_of_lt hhiq)
      have hdiff : 0 ≤ ((q : ℚ) : ℝ) - x - (((q : ℚ) : ℝ) - (hi : ℚ)) := sub_nonneg.mpr hdist
      have hsum : 0 ≤ ((q : ℚ) : ℝ) - x + (((q : ℚ) : ℝ) - (hi : ℚ)) := by linarith
      nlinarith [mul_nonneg hdiff hsum]
    · have hloq : lo ≤ q := le_of_not_gt hqlo
      have hqhi : q ≤ hi := le_of_not_gt hhiq
      simp [clampRational, hqlo, hhiq]
      positivity

theorem segmentMinimum_le_model {piece : MacroPiece} (hcheck : piece.check = true)
    {lo hi : ℚ} (hord : lo ≤ hi)
    (hfit : piece.box.lo ≤ lo ∧ hi ≤ piece.box.hi)
    {x : ℝ} (hxlo : (lo : ℝ) ≤ x) (hxhi : x ≤ (hi : ℝ)) :
    ((segmentMinimum piece lo hi : ℚ) : ℝ) ≤ piece.model x := by
  cases piece with
  | base p =>
      have hp : p.check = true := by simpa [MacroPiece.check] using hcheck
      have ha : 0 ≤ p.a := by
        by_contra hn
        have hdec : decide (0 ≤ p.a) = false := decide_eq_false_iff_not.mpr hn
        simp [LowerPiece.check, hdec] at hp
      have hc : 0 ≤ p.c := by
        by_contra hn
        have hdec : decide (0 ≤ p.c) = false := decide_eq_false_iff_not.mpr hn
        simp [LowerPiece.check, hdec] at hp
      have hdist := clampRational_sq_le p.q lo hi hord hxlo hxhi
      change ((p.a + p.c * (clampRational p.q lo hi - p.q) ^ 2 : ℚ) : ℝ) ≤
        p.model x
      simp only [LowerPiece.model]
      have hcR : (0 : ℝ) ≤ p.c := by exact_mod_cast hc
      have hmul := mul_le_mul_of_nonneg_left hdist hcR
      simp only [Rat.cast_add, Rat.cast_mul, Rat.cast_pow, LowerPiece.model]
      have hfinal := add_le_add_right hmul (p.a : ℝ)
      simpa only [Rat.cast_add, Rat.cast_mul, Rat.cast_pow] using hfinal
  | well p =>
      have hp : p.check = true := by simpa [MacroPiece.check] using hcheck
      have hvalid := (WellCert.check_iff_valid p).mp hp
      rcases hvalid with ⟨_, _, _, hv, hm, hside, _, _⟩
      cases hs : p.side with
      | left =>
          have hq : p.q = p.box.hi := by simpa [hs] using hside
          have hle : hi ≤ p.q := by rw [hq]; exact hfit.2
          have hdist : (0 : ℝ) ≤ (p.q : ℝ) - (hi : ℝ) := by exact_mod_cast sub_nonneg.mpr hle
          have hqR : (hi : ℝ) ≤ (p.q : ℝ) := by exact_mod_cast hle
          have hdistX : (0 : ℝ) ≤ (p.q : ℝ) - x := sub_nonneg.mpr (le_trans hxhi hqR)
          have hvR : (0 : ℝ) ≤ p.v := by exact_mod_cast hv
          have hmR : (0 : ℝ) ≤ p.m := by exact_mod_cast hm
          have hu : p.v + p.m * ((p.q : ℝ) - (hi : ℝ)) ≤
              p.v + p.m * ((p.q : ℝ) - x) := by
            have hmul := mul_le_mul_of_nonneg_left
              (sub_le_sub_left hxhi (p.q : ℝ)) hmR
            linarith
          have hsq : (p.v + p.m * ((p.q : ℝ) - (hi : ℝ))) ^ 2 ≤
              (p.v + p.m * ((p.q : ℝ) - x)) ^ 2 := by
            have hleft : 0 ≤ p.v + p.m * ((p.q : ℝ) - (hi : ℝ)) :=
              add_nonneg hvR (mul_nonneg hmR hdist)
            have hright : 0 ≤ p.v + p.m * ((p.q : ℝ) - x) :=
              add_nonneg hvR (mul_nonneg hmR hdistX)
            nlinarith [mul_nonneg (sub_nonneg.mpr hu) (by positivity :
              0 ≤ p.v + p.m * ((p.q : ℝ) - (hi : ℝ)) +
                (p.v + p.m * ((p.q : ℝ) - x)))]
          simp only [segmentMinimum, hs, MacroPiece.model, WellCert.model]
          have hcast : ((2 * (p.v + p.m * (p.q - hi)) ^ 2 : ℚ) : ℝ) =
              2 * ((p.v : ℝ) + (p.m : ℝ) * ((p.q : ℝ) - (hi : ℝ))) ^ 2 := by
            push_cast
            ring
          rw [hcast]
          exact mul_le_mul_of_nonneg_left hsq (by norm_num)
      | right =>
          have hq : p.q = p.box.lo := by simpa [hs] using hside
          have hle : p.q ≤ lo := by rw [hq]; exact hfit.1
          have hdist : (0 : ℝ) ≤ (lo : ℝ) - (p.q : ℝ) := by exact_mod_cast sub_nonneg.mpr hle
          have hqR : (p.q : ℝ) ≤ (lo : ℝ) := by exact_mod_cast hle
          have hdistX : (0 : ℝ) ≤ x - (p.q : ℝ) := sub_nonneg.mpr (le_trans hqR hxlo)
          have hvR : (0 : ℝ) ≤ p.v := by exact_mod_cast hv
          have hmR : (0 : ℝ) ≤ p.m := by exact_mod_cast hm
          have hu : p.v + p.m * ((lo : ℝ) - (p.q : ℝ)) ≤
              p.v + p.m * (x - (p.q : ℝ)) := by
            have hmul := mul_le_mul_of_nonneg_left (sub_le_sub_right hxlo (p.q : ℝ)) hmR
            linarith
          have hsq : (p.v + p.m * ((lo : ℝ) - (p.q : ℝ))) ^ 2 ≤
              (p.v + p.m * (x - (p.q : ℝ))) ^ 2 := by
            have hleft : 0 ≤ p.v + p.m * ((lo : ℝ) - (p.q : ℝ)) :=
              add_nonneg hvR (mul_nonneg hmR hdist)
            have hright : 0 ≤ p.v + p.m * (x - (p.q : ℝ)) :=
              add_nonneg hvR (mul_nonneg hmR hdistX)
            nlinarith [mul_nonneg (sub_nonneg.mpr hu) (by positivity :
              0 ≤ p.v + p.m * ((lo : ℝ) - (p.q : ℝ)) +
                (p.v + p.m * (x - (p.q : ℝ))))]
          simp only [segmentMinimum, hs, MacroPiece.model, WellCert.model]
          have hcast : ((2 * (p.v + p.m * (lo - p.q)) ^ 2 : ℚ) : ℝ) =
              2 * ((p.v : ℝ) + (p.m : ℝ) * ((lo : ℝ) - (p.q : ℝ))) ^ 2 := by
            push_cast
            ring
          rw [hcast]
          exact mul_le_mul_of_nonneg_left hsq (by norm_num)

structure SourceSegment where
  lo : ℚ
  hi : ℚ
  piece : MacroPiece
  deriving DecidableEq

def sourceSegmentCheck (floor : ℚ) (s : SourceSegment) : Bool :=
  decide (s.lo ≤ s.hi ∧ s.piece.box.lo ≤ s.lo ∧
    s.hi ≤ s.piece.box.hi ∧ floor ≤ segmentMinimum s.piece s.lo s.hi)

def sourceCoverFrom (cur last : ℚ) : List SourceSegment → Bool
  | [] => decide (cur = last)
  | s :: ss => decide (s.lo = cur) && decide (s.lo ≤ s.hi) &&
      sourceCoverFrom s.hi last ss

def sourcePiecewiseCheck (first last floor : ℚ) (ss : List SourceSegment) : Bool :=
  (decide (0 < ss.length) && sourceCoverFrom first last ss) &&
    ss.all (sourceSegmentCheck floor)

lemma sourceCoverFrom_sound {cur last : ℚ} {ss : List SourceSegment} {x : ℝ}
    (hne : ss ≠ []) (hc : sourceCoverFrom cur last ss = true)
    (hxlo : (cur : ℝ) ≤ x) (hxhi : x ≤ (last : ℝ)) :
    ∃ s ∈ ss, (s.lo : ℝ) ≤ x ∧ x ≤ (s.hi : ℝ) := by
  induction ss generalizing cur with
  | nil => exact (hne rfl).elim
  | cons s ss ih =>
      simp only [sourceCoverFrom, Bool.and_eq_true, decide_eq_true_eq] at hc
      obtain ⟨⟨hfirst, hord⟩, hrest⟩ := hc
      subst cur
      by_cases hx : x ≤ (s.hi : ℝ)
      · exact ⟨s, by simp, hxlo, hx⟩
      · cases ss with
        | nil =>
            simp only [sourceCoverFrom, decide_eq_true_eq] at hrest
            have hlast : ((s.hi : ℚ) : ℝ) = (last : ℝ) := by exact_mod_cast hrest
            exact (hx (by rw [hlast]; exact hxhi)).elim
        | cons next rest =>
            obtain ⟨found, hmem, hholds⟩ := ih (by simp) hrest (le_of_not_ge hx)
            exact ⟨found, by simp [hmem], hholds⟩

theorem sourcePiecewiseCheck_sound {first last floor : ℚ} {ss : List SourceSegment}
    (hc : sourcePiecewiseCheck first last floor ss = true)
    (hcert : ∀ s ∈ ss, s.piece.check = true) {x : ℝ}
    (hxlo : (first : ℝ) ≤ x) (hxhi : x ≤ (last : ℝ)) :
    ((floor : ℚ) : ℝ) ≤ 2 * mtKernel x ^ 2 := by
  simp only [sourcePiecewiseCheck, Bool.and_eq_true, decide_eq_true_eq] at hc
  obtain ⟨⟨hlen, hcover⟩, hAll⟩ := hc
  have hne : ss ≠ [] := by
    cases ss with
    | nil => simp at hlen
    | cons s rest => simp
  have hall := List.all_eq_true.mp hAll
  obtain ⟨s, hmem, hxs⟩ := sourceCoverFrom_sound hne hcover hxlo hxhi
  have hrow := hall s hmem
  have hrow := of_decide_eq_true hrow
  rcases hrow with ⟨hord, hfitlo, hfithi, hfloor⟩
  have hmodel := segmentMinimum_le_model (hcert s hmem) hord
    ⟨hfitlo, hfithi⟩ hxs.1 hxs.2
  have hpiece : RatInterval.Holds s.piece.box x := by
    constructor
    · have hfitloR : (s.piece.box.lo : ℝ) ≤ (s.lo : ℝ) := by exact_mod_cast hfitlo
      exact hfitloR.trans hxs.1
    · have hfithiR : (s.hi : ℝ) ≤ (s.piece.box.hi : ℝ) := by exact_mod_cast hfithi
      exact hxs.2.trans hfithiR
  have hkernel := MacroPiece.check_sound (hcert s hmem) hpiece
  have hfloorR : (floor : ℝ) ≤ (segmentMinimum s.piece s.lo s.hi : ℝ) := by
    exact_mod_cast hfloor
  exact hfloorR.trans (hmodel.trans hkernel)


def certifiedPiecewiseCheck (first last floor : ℚ) (ss : List SourceSegment) : Bool :=
  sourcePiecewiseCheck first last floor ss && ss.all (fun s => s.piece.check)

theorem certifiedPiecewiseCheck_sound {first last floor : ℚ} {ss : List SourceSegment}
    (h : certifiedPiecewiseCheck first last floor ss = true) {x : ℝ}
    (hlo : (first : ℝ) ≤ x) (hhi : x ≤ (last : ℝ)) :
    (floor : ℝ) ≤ 2 * mtKernel x ^ 2 := by
  simp only [certifiedPiecewiseCheck, Bool.and_eq_true] at h
  apply sourcePiecewiseCheck_sound h.1 _ hlo hhi
  exact List.all_eq_true.mp h.2

#print axioms certifiedPiecewiseCheck_sound
end A1294GenericChecker

namespace A1294Compact
open A1294GenericChecker
structure CompactRat where
  num : Int
  den : Nat
  deriving DecidableEq

def CompactRat.check (q : CompactRat) : Bool :=
  decide (0 < q.den ∧ Nat.gcd q.num.natAbs q.den = 1)

def interpRat (q : CompactRat) : ℚ := (q.num : ℚ) / (q.den : ℚ)

structure CompactSegment where
  lo : CompactRat
  hi : CompactRat
  pieceRef : Nat
  deriving DecidableEq

def interpSegment (catalog : Array MacroPiece) (s : CompactSegment) : Option SourceSegment :=
  match catalog[s.pieceRef]? with
  | none => none
  | some p => some { lo := interpRat s.lo, hi := interpRat s.hi, piece := p }

def compactSegmentCheck (catalog : Array MacroPiece) (floor : CompactRat)
    (s : CompactSegment) : Bool :=
  floor.check && s.lo.check && s.hi.check &&
    match interpSegment catalog s with
    | none => false
    | some t => certifiedPiecewiseCheck t.lo t.hi (interpRat floor) [t]

theorem compactSegmentCheck_sound {catalog : Array MacroPiece} {floor : CompactRat}
    {s : CompactSegment} (h : compactSegmentCheck catalog floor s = true) :
    ∃ t, interpSegment catalog s = some t ∧
      ∀ x : ℝ, (t.lo : ℝ) ≤ x → x ≤ (t.hi : ℝ) →
        (interpRat floor : ℝ) ≤ 2 * mtKernel x ^ 2 := by
  unfold compactSegmentCheck at h
  cases he : interpSegment catalog s with
  | none => simp [he] at h
  | some t =>
    refine ⟨t, rfl, ?_⟩
    have hc : certifiedPiecewiseCheck t.lo t.hi (interpRat floor) [t] = true := by
      simp only [he, Bool.and_eq_true] at h
      exact h.2
    intro x hlo hhi
    exact certifiedPiecewiseCheck_sound hc hlo hhi

#print axioms compactSegmentCheck_sound
end A1294Compact



namespace A1294FifteenBridge
open A1294GenericChecker
open A1294Compact
inductive ModelRow where
  | direct (piece : MacroPiece)
  | floor (value : ℚ) (segments : List SourceSegment)

def interpModel (row : ModelRow) (p : Fin 15) : RankOneModel :=
  match row with
  | .direct piece => macroPieceRankModel (fun _ => piece) p
  | .floor value _ => { base := value, weight := 0, offset := 0, coeff := fun _ => 0 }

def modelCheck (box : GapBox) (p : Fin 15) (row : ModelRow) : Bool :=
  match row with
  | .direct piece => piece.check && decide
      (piece.box.lo ≤ (distanceInterval box p).lo ∧
       (distanceInterval box p).hi ≤ piece.box.hi)
  | .floor value segments => certifiedPiecewiseCheck
      (distanceInterval box p).lo (distanceInterval box p).hi value segments

theorem modelCheck_sound {box : GapBox} {p : Fin 15} {row : ModelRow}
    (h : modelCheck box p row = true) {g : Fin 5 → ℝ} (hg : box.Holds g) :
    (interpModel row p).value g ≤ 2 * mtKernel (gapDistance g p) ^ 2 := by
  have hd := distanceInterval_holds hg p
  cases row with
  | direct piece =>
    simp only [modelCheck, Bool.and_eq_true, decide_eq_true_eq] at h
    have hmem : RatInterval.Holds piece.box (gapDistance g p) := by
      constructor
      · have hlo : (piece.box.lo : ℝ) ≤ ((distanceInterval box p).lo : ℝ) := by
          exact_mod_cast h.2.1
        exact hlo.trans hd.1
      · have hhi : ((distanceInterval box p).hi : ℝ) ≤ (piece.box.hi : ℝ) := by
          exact_mod_cast h.2.2
        exact hd.2.trans hhi
    simpa [interpModel] using MacroPiece.check_sound h.1 hmem
  | floor value segments =>
    have hb := certifiedPiecewiseCheck_sound h hd.1 hd.2
    simpa [interpModel, RankOneModel.value, RankOneModel.dot] using hb

def fifteenCheck (A B : ℚ) (box : GapBox) (anchor : Fin 5 → ℚ)
    (rows : Fin 15 → ModelRow) : Bool :=
  decide (∀ p, modelCheck box p (rows p) = true) &&
    rankTangentCheck A B box anchor (fun p => interpModel (rows p) p)

theorem fifteenCheck_sound {A B : ℚ} {box : GapBox} {anchor : Fin 5 → ℚ}
    {rows : Fin 15 → ModelRow} (h : fifteenCheck A B box anchor rows = true) :
    ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →
      (A : ℝ) ≤ sextupleEnergy g + (B : ℝ) * sextupleSpan g := by
  simp only [fifteenCheck, Bool.and_eq_true, decide_eq_true_eq] at h
  apply rankTangentCheck_energy_sound h.2
  intro g hg p
  exact modelCheck_sound (h.1 p) hg

#print axioms fifteenCheck_sound
end A1294FifteenBridge

namespace A1294FifteenBridge
open A1294GenericChecker A1294Compact
inductive CompactRow where
  | direct (ref : Nat)
  | floor (value : CompactRat) (segments : List CompactSegment)

def interpCompactRow (catalog : Array MacroPiece) : CompactRow → Option ModelRow
  | .direct ref => (catalog[ref]?).map ModelRow.direct
  | .floor value segments =>
      (segments.mapM (interpSegment catalog)).map (ModelRow.floor (interpRat value))

def compactRowCanonical : CompactRow → Bool
  | .direct _ => true
  | .floor value ss => value.check && ss.all (fun s => s.lo.check && s.hi.check)

def decodedRow (catalog : Array MacroPiece) (r : CompactRow) : ModelRow :=
  (interpCompactRow catalog r).getD (.floor 0 [])

def compactRowCheck (catalog : Array MacroPiece) (box : GapBox) (p : Fin 15)
    (r : CompactRow) : Bool :=
  compactRowCanonical r && match interpCompactRow catalog r with
  | none => false
  | some row => modelCheck box p row

theorem compactRowCheck_sound {catalog : Array MacroPiece} {box : GapBox}
    {p : Fin 15} {r : CompactRow} (h : compactRowCheck catalog box p r = true)
    {g : Fin 5 → ℝ} (hg : box.Holds g) :
    (interpModel (decodedRow catalog r) p).value g ≤
      2 * mtKernel (gapDistance g p) ^ 2 := by
  unfold compactRowCheck at h
  cases he : interpCompactRow catalog r with
  | none => simp [he] at h
  | some row =>
    have hc : modelCheck box p row = true := by
      simp only [he, Bool.and_eq_true] at h
      exact h.2
    simpa [decodedRow, he] using modelCheck_sound hc hg

def compactQuadraticLeafCheck (catalog : Array MacroPiece) (A B : ℚ)
    (box : GapBox) (anchor : Fin 5 → ℚ) (rows : Fin 15 → CompactRow) : Bool :=
  decide (∀ p, compactRowCheck catalog box p (rows p) = true) &&
    rankTangentCheck A B box anchor
      (fun p => interpModel (decodedRow catalog (rows p)) p)

theorem compactQuadraticLeafCheck_sound {catalog : Array MacroPiece} {A B : ℚ}
    {box : GapBox} {anchor : Fin 5 → ℚ} {rows : Fin 15 → CompactRow}
    (h : compactQuadraticLeafCheck catalog A B box anchor rows = true) :
    ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →
      (A : ℝ) ≤ sextupleEnergy g + (B : ℝ) * sextupleSpan g := by
  simp only [compactQuadraticLeafCheck, Bool.and_eq_true, decide_eq_true_eq] at h
  apply rankTangentCheck_energy_sound h.2
  intro g hg p
  exact compactRowCheck_sound (h.1 p) hg

#print axioms compactQuadraticLeafCheck_sound
end A1294FifteenBridge

namespace AuthenticCompactLeaf
open A1294FifteenBridge A1294Compact
def catalog : Array MacroPiece := #[refinementPiece3, refinementPiece4, refinementPiece5, refinementPiece6, refinementPiece7, refinementPiece8, refinementPiece9, refinementPiece10, refinementPiece11, macroPiece11, refinementPiece48, refinementPiece49, refinementPiece50, refinementPiece51, refinementPiece52, refinementPiece53, refinementPiece54, refinementPiece55, refinementPiece56, refinementPiece57, refinementPiece58, refinementPiece59, refinementPiece60, refinementPiece61, refinementPiece62, refinementPiece63, refinementPiece64, refinementPiece65, refinementPiece66, refinementPiece67, refinementPiece68, refinementPiece69, refinementPiece70, refinementPiece84, refinementPiece85, refinementPiece86, refinementPiece87, refinementPiece88, refinementPiece89, refinementPiece90, refinementPiece91, refinementPiece92, refinementPiece93, refinementPiece94, refinementPiece95, macroPiece24, refinementPiece98, refinementPiece99, refinementPiece100, refinementPiece101, refinementPiece102, refinementPiece103, refinementPiece104, refinementPiece105, refinementPiece106, refinementPiece107, refinementPiece108, refinementPiece109, refinementPiece110, refinementPiece111, refinementPiece112, refinementPiece113, refinementPiece114, refinementPiece160, refinementPiece161, refinementPiece162, refinementPiece163, refinementPiece164, refinementPiece165, refinementPiece166, refinementPiece167, macroPiece30, macroPiece31, refinementPiece12, refinementPiece13, refinementPiece14, refinementPiece15, refinementPiece16, refinementPiece17, refinementPiece18, refinementPiece41, refinementPiece42, refinementPiece43, refinementPiece44, refinementPiece45, refinementPiece46, macroPiece9, macroPiece10, refinementPiece71, macroPiece18, refinementPiece115, refinementPiece116, refinementPiece117, refinementPiece118, refinementPiece119, macroPiece25, macroPiece2, refinementPiece0, refinementPiece1, refinementPiece2]
def row0 : CompactRow := .floor ⟨(5170581624709583018970186520240204081), 3200000000000000000000000000000000000000⟩ [
{ lo := ⟨(405), 64⟩, hi := ⟨(253223), 40000⟩, pieceRef := 0 },
{ lo := ⟨(253223), 40000⟩, hi := ⟨(31731), 5000⟩, pieceRef := 1 },
{ lo := ⟨(31731), 5000⟩, hi := ⟨(254473), 40000⟩, pieceRef := 2 },
{ lo := ⟨(254473), 40000⟩, hi := ⟨(127549), 20000⟩, pieceRef := 3 },
{ lo := ⟨(127549), 20000⟩, hi := ⟨(255723), 40000⟩, pieceRef := 4 },
{ lo := ⟨(255723), 40000⟩, hi := ⟨(64087), 10000⟩, pieceRef := 5 },
{ lo := ⟨(64087), 10000⟩, hi := ⟨(256973), 40000⟩, pieceRef := 6 },
{ lo := ⟨(256973), 40000⟩, hi := ⟨(128799), 20000⟩, pieceRef := 7 },
{ lo := ⟨(128799), 20000⟩, hi := ⟨(825), 128⟩, pieceRef := 8 }]
def row1 : CompactRow := .direct 9
def row2 : CompactRow := .floor ⟨(1755263779336959657910023102330969), 7812500000000000000000000000000000000000⟩ [
{ lo := ⟨(1215), 64⟩, hi := ⟨(4748093), 250000⟩, pieceRef := 10 },
{ lo := ⟨(4748093), 250000⟩, hi := ⟨(19007997), 1000000⟩, pieceRef := 11 },
{ lo := ⟨(19007997), 1000000⟩, hi := ⟨(9511811), 500000⟩, pieceRef := 12 },
{ lo := ⟨(9511811), 500000⟩, hi := ⟨(19039247), 1000000⟩, pieceRef := 13 },
{ lo := ⟨(19039247), 1000000⟩, hi := ⟨(2381859), 125000⟩, pieceRef := 14 },
{ lo := ⟨(2381859), 125000⟩, hi := ⟨(19070497), 1000000⟩, pieceRef := 15 },
{ lo := ⟨(19070497), 1000000⟩, hi := ⟨(9543061), 500000⟩, pieceRef := 16 },
{ lo := ⟨(9543061), 500000⟩, hi := ⟨(19101747), 1000000⟩, pieceRef := 17 },
{ lo := ⟨(19101747), 1000000⟩, hi := ⟨(4779343), 250000⟩, pieceRef := 18 },
{ lo := ⟨(4779343), 250000⟩, hi := ⟨(19132997), 1000000⟩, pieceRef := 19 },
{ lo := ⟨(19132997), 1000000⟩, hi := ⟨(9574311), 500000⟩, pieceRef := 20 },
{ lo := ⟨(9574311), 500000⟩, hi := ⟨(19164247), 1000000⟩, pieceRef := 21 },
{ lo := ⟨(19164247), 1000000⟩, hi := ⟨(599371), 31250⟩, pieceRef := 22 },
{ lo := ⟨(599371), 31250⟩, hi := ⟨(19195497), 1000000⟩, pieceRef := 23 },
{ lo := ⟨(19195497), 1000000⟩, hi := ⟨(9605561), 500000⟩, pieceRef := 24 },
{ lo := ⟨(9605561), 500000⟩, hi := ⟨(19226747), 1000000⟩, pieceRef := 25 },
{ lo := ⟨(19226747), 1000000⟩, hi := ⟨(4810593), 250000⟩, pieceRef := 26 },
{ lo := ⟨(4810593), 250000⟩, hi := ⟨(19257997), 1000000⟩, pieceRef := 27 },
{ lo := ⟨(19257997), 1000000⟩, hi := ⟨(9636811), 500000⟩, pieceRef := 28 },
{ lo := ⟨(9636811), 500000⟩, hi := ⟨(19289247), 1000000⟩, pieceRef := 29 },
{ lo := ⟨(19289247), 1000000⟩, hi := ⟨(2413109), 125000⟩, pieceRef := 30 },
{ lo := ⟨(2413109), 125000⟩, hi := ⟨(19320497), 1000000⟩, pieceRef := 31 },
{ lo := ⟨(19320497), 1000000⟩, hi := ⟨(2475), 128⟩, pieceRef := 32 }]
def row3 : CompactRow := .floor ⟨(6876046637736468087644507155946023489), 80000000000000000000000000000000000000000⟩ [
{ lo := ⟨(3255), 128⟩, hi := ⟨(5086319), 200000⟩, pieceRef := 33 },
{ lo := ⟨(5086319), 200000⟩, hi := ⟨(1272361), 50000⟩, pieceRef := 34 },
{ lo := ⟨(1272361), 50000⟩, hi := ⟨(5092569), 200000⟩, pieceRef := 35 },
{ lo := ⟨(5092569), 200000⟩, hi := ⟨(2547847), 100000⟩, pieceRef := 36 },
{ lo := ⟨(2547847), 100000⟩, hi := ⟨(5098819), 200000⟩, pieceRef := 37 },
{ lo := ⟨(5098819), 200000⟩, hi := ⟨(637743), 25000⟩, pieceRef := 38 },
{ lo := ⟨(637743), 25000⟩, hi := ⟨(5105069), 200000⟩, pieceRef := 39 },
{ lo := ⟨(5105069), 200000⟩, hi := ⟨(2554097), 100000⟩, pieceRef := 40 },
{ lo := ⟨(2554097), 100000⟩, hi := ⟨(5111319), 200000⟩, pieceRef := 41 },
{ lo := ⟨(5111319), 200000⟩, hi := ⟨(1278611), 50000⟩, pieceRef := 42 },
{ lo := ⟨(1278611), 50000⟩, hi := ⟨(5117569), 200000⟩, pieceRef := 43 },
{ lo := ⟨(5117569), 200000⟩, hi := ⟨(2560347), 100000⟩, pieceRef := 44 },
{ lo := ⟨(2560347), 100000⟩, hi := ⟨(5123819), 200000⟩, pieceRef := 45 },
{ lo := ⟨(5123819), 200000⟩, hi := ⟨(160217), 6250⟩, pieceRef := 45 },
{ lo := ⟨(160217), 6250⟩, hi := ⟨(5130069), 200000⟩, pieceRef := 46 },
{ lo := ⟨(5130069), 200000⟩, hi := ⟨(2566597), 100000⟩, pieceRef := 47 },
{ lo := ⟨(2566597), 100000⟩, hi := ⟨(5136319), 200000⟩, pieceRef := 48 },
{ lo := ⟨(5136319), 200000⟩, hi := ⟨(1284861), 50000⟩, pieceRef := 49 },
{ lo := ⟨(1284861), 50000⟩, hi := ⟨(5142569), 200000⟩, pieceRef := 50 },
{ lo := ⟨(5142569), 200000⟩, hi := ⟨(2572847), 100000⟩, pieceRef := 51 },
{ lo := ⟨(2572847), 100000⟩, hi := ⟨(5148819), 200000⟩, pieceRef := 52 },
{ lo := ⟨(5148819), 200000⟩, hi := ⟨(643993), 25000⟩, pieceRef := 53 },
{ lo := ⟨(643993), 25000⟩, hi := ⟨(5155069), 200000⟩, pieceRef := 54 },
{ lo := ⟨(5155069), 200000⟩, hi := ⟨(2579097), 100000⟩, pieceRef := 55 },
{ lo := ⟨(2579097), 100000⟩, hi := ⟨(5161319), 200000⟩, pieceRef := 56 },
{ lo := ⟨(5161319), 200000⟩, hi := ⟨(1291111), 50000⟩, pieceRef := 57 },
{ lo := ⟨(1291111), 50000⟩, hi := ⟨(5167569), 200000⟩, pieceRef := 58 },
{ lo := ⟨(5167569), 200000⟩, hi := ⟨(2585347), 100000⟩, pieceRef := 59 },
{ lo := ⟨(2585347), 100000⟩, hi := ⟨(5173819), 200000⟩, pieceRef := 60 },
{ lo := ⟨(5173819), 200000⟩, hi := ⟨(323559), 12500⟩, pieceRef := 61 },
{ lo := ⟨(323559), 12500⟩, hi := ⟨(3315), 128⟩, pieceRef := 62 }]
def row4 : CompactRow := .floor ⟨(7594713117315031921983662976367761841), 80000000000000000000000000000000000000000⟩ [
{ lo := ⟨(4065), 128⟩, hi := ⟨(1587913), 50000⟩, pieceRef := 63 },
{ lo := ⟨(1587913), 50000⟩, hi := ⟨(6354777), 200000⟩, pieceRef := 64 },
{ lo := ⟨(6354777), 200000⟩, hi := ⟨(3178951), 100000⟩, pieceRef := 65 },
{ lo := ⟨(3178951), 100000⟩, hi := ⟨(6361027), 200000⟩, pieceRef := 66 },
{ lo := ⟨(6361027), 200000⟩, hi := ⟨(795519), 25000⟩, pieceRef := 67 },
{ lo := ⟨(795519), 25000⟩, hi := ⟨(6367277), 200000⟩, pieceRef := 68 },
{ lo := ⟨(6367277), 200000⟩, hi := ⟨(3185201), 100000⟩, pieceRef := 69 },
{ lo := ⟨(3185201), 100000⟩, hi := ⟨(6373527), 200000⟩, pieceRef := 70 },
{ lo := ⟨(6373527), 200000⟩, hi := ⟨(6448527), 200000⟩, pieceRef := 71 },
{ lo := ⟨(6448527), 200000⟩, hi := ⟨(4155), 128⟩, pieceRef := 72 }]
def row5 : CompactRow := .floor ⟨(12892869620170946020955818564495929), 50000000000000000000000000000000000000⟩ [
{ lo := ⟨(825), 128⟩, hi := ⟨(258223), 40000⟩, pieceRef := 8 },
{ lo := ⟨(258223), 40000⟩, hi := ⟨(8089), 1250⟩, pieceRef := 73 },
{ lo := ⟨(8089), 1250⟩, hi := ⟨(259473), 40000⟩, pieceRef := 74 },
{ lo := ⟨(259473), 40000⟩, hi := ⟨(130049), 20000⟩, pieceRef := 75 },
{ lo := ⟨(130049), 20000⟩, hi := ⟨(260723), 40000⟩, pieceRef := 76 },
{ lo := ⟨(260723), 40000⟩, hi := ⟨(65337), 10000⟩, pieceRef := 77 },
{ lo := ⟨(65337), 10000⟩, hi := ⟨(261973), 40000⟩, pieceRef := 78 },
{ lo := ⟨(261973), 40000⟩, hi := ⟨(105), 16⟩, pieceRef := 79 }]
def row6 : CompactRow := .floor ⟨(0), 1⟩ [
{ lo := ⟨(405), 32⟩, hi := ⟨(633077), 50000⟩, pieceRef := 80 },
{ lo := ⟨(633077), 50000⟩, hi := ⟨(2535433), 200000⟩, pieceRef := 81 },
{ lo := ⟨(2535433), 200000⟩, hi := ⟨(1269279), 100000⟩, pieceRef := 82 },
{ lo := ⟨(1269279), 100000⟩, hi := ⟨(2541683), 200000⟩, pieceRef := 83 },
{ lo := ⟨(2541683), 200000⟩, hi := ⟨(318101), 25000⟩, pieceRef := 84 },
{ lo := ⟨(318101), 25000⟩, hi := ⟨(2547933), 200000⟩, pieceRef := 85 },
{ lo := ⟨(2547933), 200000⟩, hi := ⟨(1275529), 100000⟩, pieceRef := 86 },
{ lo := ⟨(1275529), 100000⟩, hi := ⟨(12755291), 1000000⟩, pieceRef := 87 },
{ lo := ⟨(12755291), 1000000⟩, hi := ⟨(825), 64⟩, pieceRef := 9 }]
def row7 : CompactRow := .floor ⟨(29727308394007168144031841183195847081), 500000000000000000000000000000000000000000⟩ [
{ lo := ⟨(2445), 128⟩, hi := ⟨(19101747), 1000000⟩, pieceRef := 17 },
{ lo := ⟨(19101747), 1000000⟩, hi := ⟨(4779343), 250000⟩, pieceRef := 18 },
{ lo := ⟨(4779343), 250000⟩, hi := ⟨(19132997), 1000000⟩, pieceRef := 19 },
{ lo := ⟨(19132997), 1000000⟩, hi := ⟨(9574311), 500000⟩, pieceRef := 20 },
{ lo := ⟨(9574311), 500000⟩, hi := ⟨(19164247), 1000000⟩, pieceRef := 21 },
{ lo := ⟨(19164247), 1000000⟩, hi := ⟨(599371), 31250⟩, pieceRef := 22 },
{ lo := ⟨(599371), 31250⟩, hi := ⟨(19195497), 1000000⟩, pieceRef := 23 },
{ lo := ⟨(19195497), 1000000⟩, hi := ⟨(9605561), 500000⟩, pieceRef := 24 },
{ lo := ⟨(9605561), 500000⟩, hi := ⟨(19226747), 1000000⟩, pieceRef := 25 },
{ lo := ⟨(19226747), 1000000⟩, hi := ⟨(4810593), 250000⟩, pieceRef := 26 },
{ lo := ⟨(4810593), 250000⟩, hi := ⟨(19257997), 1000000⟩, pieceRef := 27 },
{ lo := ⟨(19257997), 1000000⟩, hi := ⟨(9636811), 500000⟩, pieceRef := 28 },
{ lo := ⟨(9636811), 500000⟩, hi := ⟨(19289247), 1000000⟩, pieceRef := 29 },
{ lo := ⟨(19289247), 1000000⟩, hi := ⟨(2413109), 125000⟩, pieceRef := 30 },
{ lo := ⟨(2413109), 125000⟩, hi := ⟨(19320497), 1000000⟩, pieceRef := 31 },
{ lo := ⟨(19320497), 1000000⟩, hi := ⟨(9668061), 500000⟩, pieceRef := 32 },
{ lo := ⟨(9668061), 500000⟩, hi := ⟨(19351747), 1000000⟩, pieceRef := 88 },
{ lo := ⟨(19351747), 1000000⟩, hi := ⟨(1245), 64⟩, pieceRef := 89 }]
def row8 : CompactRow := .floor ⟨(6876046637736468087644507155946023489), 80000000000000000000000000000000000000000⟩ [
{ lo := ⟨(3255), 128⟩, hi := ⟨(5086319), 200000⟩, pieceRef := 33 },
{ lo := ⟨(5086319), 200000⟩, hi := ⟨(1272361), 50000⟩, pieceRef := 34 },
{ lo := ⟨(1272361), 50000⟩, hi := ⟨(5092569), 200000⟩, pieceRef := 35 },
{ lo := ⟨(5092569), 200000⟩, hi := ⟨(2547847), 100000⟩, pieceRef := 36 },
{ lo := ⟨(2547847), 100000⟩, hi := ⟨(5098819), 200000⟩, pieceRef := 37 },
{ lo := ⟨(5098819), 200000⟩, hi := ⟨(637743), 25000⟩, pieceRef := 38 },
{ lo := ⟨(637743), 25000⟩, hi := ⟨(5105069), 200000⟩, pieceRef := 39 },
{ lo := ⟨(5105069), 200000⟩, hi := ⟨(2554097), 100000⟩, pieceRef := 40 },
{ lo := ⟨(2554097), 100000⟩, hi := ⟨(5111319), 200000⟩, pieceRef := 41 },
{ lo := ⟨(5111319), 200000⟩, hi := ⟨(1278611), 50000⟩, pieceRef := 42 },
{ lo := ⟨(1278611), 50000⟩, hi := ⟨(5117569), 200000⟩, pieceRef := 43 },
{ lo := ⟨(5117569), 200000⟩, hi := ⟨(2560347), 100000⟩, pieceRef := 44 },
{ lo := ⟨(2560347), 100000⟩, hi := ⟨(5123819), 200000⟩, pieceRef := 45 },
{ lo := ⟨(5123819), 200000⟩, hi := ⟨(160217), 6250⟩, pieceRef := 45 },
{ lo := ⟨(160217), 6250⟩, hi := ⟨(5130069), 200000⟩, pieceRef := 46 },
{ lo := ⟨(5130069), 200000⟩, hi := ⟨(2566597), 100000⟩, pieceRef := 47 },
{ lo := ⟨(2566597), 100000⟩, hi := ⟨(5136319), 200000⟩, pieceRef := 48 },
{ lo := ⟨(5136319), 200000⟩, hi := ⟨(1284861), 50000⟩, pieceRef := 49 },
{ lo := ⟨(1284861), 50000⟩, hi := ⟨(5142569), 200000⟩, pieceRef := 50 },
{ lo := ⟨(5142569), 200000⟩, hi := ⟨(2572847), 100000⟩, pieceRef := 51 },
{ lo := ⟨(2572847), 100000⟩, hi := ⟨(5148819), 200000⟩, pieceRef := 52 },
{ lo := ⟨(5148819), 200000⟩, hi := ⟨(643993), 25000⟩, pieceRef := 53 },
{ lo := ⟨(643993), 25000⟩, hi := ⟨(5155069), 200000⟩, pieceRef := 54 },
{ lo := ⟨(5155069), 200000⟩, hi := ⟨(2579097), 100000⟩, pieceRef := 55 },
{ lo := ⟨(2579097), 100000⟩, hi := ⟨(5161319), 200000⟩, pieceRef := 56 },
{ lo := ⟨(5161319), 200000⟩, hi := ⟨(1291111), 50000⟩, pieceRef := 57 },
{ lo := ⟨(1291111), 50000⟩, hi := ⟨(5167569), 200000⟩, pieceRef := 58 },
{ lo := ⟨(5167569), 200000⟩, hi := ⟨(2585347), 100000⟩, pieceRef := 59 },
{ lo := ⟨(2585347), 100000⟩, hi := ⟨(5173819), 200000⟩, pieceRef := 60 },
{ lo := ⟨(5173819), 200000⟩, hi := ⟨(323559), 12500⟩, pieceRef := 61 },
{ lo := ⟨(323559), 12500⟩, hi := ⟨(5180069), 200000⟩, pieceRef := 62 },
{ lo := ⟨(5180069), 200000⟩, hi := ⟨(2591597), 100000⟩, pieceRef := 90 },
{ lo := ⟨(2591597), 100000⟩, hi := ⟨(5186319), 200000⟩, pieceRef := 91 },
{ lo := ⟨(5186319), 200000⟩, hi := ⟨(1297361), 50000⟩, pieceRef := 92 },
{ lo := ⟨(1297361), 50000⟩, hi := ⟨(5192569), 200000⟩, pieceRef := 93 },
{ lo := ⟨(5192569), 200000⟩, hi := ⟨(2597847), 100000⟩, pieceRef := 94 },
{ lo := ⟨(2597847), 100000⟩, hi := ⟨(1665), 64⟩, pieceRef := 95 }]
def row9 : CompactRow := .floor ⟨(21287960894909617826490440080249), 5000000000000000000000000000000000⟩ [
{ lo := ⟨(795), 128⟩, hi := ⟨(250723), 40000⟩, pieceRef := 96 },
{ lo := ⟨(250723), 40000⟩, hi := ⟨(62837), 10000⟩, pieceRef := 97 },
{ lo := ⟨(62837), 10000⟩, hi := ⟨(251973), 40000⟩, pieceRef := 98 },
{ lo := ⟨(251973), 40000⟩, hi := ⟨(126299), 20000⟩, pieceRef := 99 },
{ lo := ⟨(126299), 20000⟩, hi := ⟨(405), 64⟩, pieceRef := 0 }]
def row10 : CompactRow := .floor ⟨(0), 1⟩ [
{ lo := ⟨(405), 32⟩, hi := ⟨(633077), 50000⟩, pieceRef := 80 },
{ lo := ⟨(633077), 50000⟩, hi := ⟨(2535433), 200000⟩, pieceRef := 81 },
{ lo := ⟨(2535433), 200000⟩, hi := ⟨(1269279), 100000⟩, pieceRef := 82 },
{ lo := ⟨(1269279), 100000⟩, hi := ⟨(2541683), 200000⟩, pieceRef := 83 },
{ lo := ⟨(2541683), 200000⟩, hi := ⟨(318101), 25000⟩, pieceRef := 84 },
{ lo := ⟨(318101), 25000⟩, hi := ⟨(2547933), 200000⟩, pieceRef := 85 },
{ lo := ⟨(2547933), 200000⟩, hi := ⟨(1275529), 100000⟩, pieceRef := 86 },
{ lo := ⟨(1275529), 100000⟩, hi := ⟨(12755291), 1000000⟩, pieceRef := 87 },
{ lo := ⟨(12755291), 1000000⟩, hi := ⟨(825), 64⟩, pieceRef := 9 }]
def row11 : CompactRow := .floor ⟨(1755263779336959657910023102330969), 7812500000000000000000000000000000000000⟩ [
{ lo := ⟨(1215), 64⟩, hi := ⟨(4748093), 250000⟩, pieceRef := 10 },
{ lo := ⟨(4748093), 250000⟩, hi := ⟨(19007997), 1000000⟩, pieceRef := 11 },
{ lo := ⟨(19007997), 1000000⟩, hi := ⟨(9511811), 500000⟩, pieceRef := 12 },
{ lo := ⟨(9511811), 500000⟩, hi := ⟨(19039247), 1000000⟩, pieceRef := 13 },
{ lo := ⟨(19039247), 1000000⟩, hi := ⟨(2381859), 125000⟩, pieceRef := 14 },
{ lo := ⟨(2381859), 125000⟩, hi := ⟨(19070497), 1000000⟩, pieceRef := 15 },
{ lo := ⟨(19070497), 1000000⟩, hi := ⟨(9543061), 500000⟩, pieceRef := 16 },
{ lo := ⟨(9543061), 500000⟩, hi := ⟨(19101747), 1000000⟩, pieceRef := 17 },
{ lo := ⟨(19101747), 1000000⟩, hi := ⟨(4779343), 250000⟩, pieceRef := 18 },
{ lo := ⟨(4779343), 250000⟩, hi := ⟨(19132997), 1000000⟩, pieceRef := 19 },
{ lo := ⟨(19132997), 1000000⟩, hi := ⟨(9574311), 500000⟩, pieceRef := 20 },
{ lo := ⟨(9574311), 500000⟩, hi := ⟨(19164247), 1000000⟩, pieceRef := 21 },
{ lo := ⟨(19164247), 1000000⟩, hi := ⟨(599371), 31250⟩, pieceRef := 22 },
{ lo := ⟨(599371), 31250⟩, hi := ⟨(19195497), 1000000⟩, pieceRef := 23 },
{ lo := ⟨(19195497), 1000000⟩, hi := ⟨(9605561), 500000⟩, pieceRef := 24 },
{ lo := ⟨(9605561), 500000⟩, hi := ⟨(19226747), 1000000⟩, pieceRef := 25 },
{ lo := ⟨(19226747), 1000000⟩, hi := ⟨(4810593), 250000⟩, pieceRef := 26 },
{ lo := ⟨(4810593), 250000⟩, hi := ⟨(19257997), 1000000⟩, pieceRef := 27 },
{ lo := ⟨(19257997), 1000000⟩, hi := ⟨(9636811), 500000⟩, pieceRef := 28 },
{ lo := ⟨(9636811), 500000⟩, hi := ⟨(19289247), 1000000⟩, pieceRef := 29 },
{ lo := ⟨(19289247), 1000000⟩, hi := ⟨(2413109), 125000⟩, pieceRef := 30 },
{ lo := ⟨(2413109), 125000⟩, hi := ⟨(19320497), 1000000⟩, pieceRef := 31 },
{ lo := ⟨(19320497), 1000000⟩, hi := ⟨(9668061), 500000⟩, pieceRef := 32 },
{ lo := ⟨(9668061), 500000⟩, hi := ⟨(19351747), 1000000⟩, pieceRef := 88 },
{ lo := ⟨(19351747), 1000000⟩, hi := ⟨(1245), 64⟩, pieceRef := 89 }]
def row12 : CompactRow := .floor ⟨(12892869620170946020955818564495929), 50000000000000000000000000000000000000⟩ [
{ lo := ⟨(825), 128⟩, hi := ⟨(258223), 40000⟩, pieceRef := 8 },
{ lo := ⟨(258223), 40000⟩, hi := ⟨(8089), 1250⟩, pieceRef := 73 },
{ lo := ⟨(8089), 1250⟩, hi := ⟨(259473), 40000⟩, pieceRef := 74 },
{ lo := ⟨(259473), 40000⟩, hi := ⟨(130049), 20000⟩, pieceRef := 75 },
{ lo := ⟨(130049), 20000⟩, hi := ⟨(260723), 40000⟩, pieceRef := 76 },
{ lo := ⟨(260723), 40000⟩, hi := ⟨(65337), 10000⟩, pieceRef := 77 },
{ lo := ⟨(65337), 10000⟩, hi := ⟨(261973), 40000⟩, pieceRef := 78 },
{ lo := ⟨(261973), 40000⟩, hi := ⟨(105), 16⟩, pieceRef := 79 }]
def row13 : CompactRow := .direct 9
def row14 : CompactRow := .floor ⟨(12892869620170946020955818564495929), 50000000000000000000000000000000000000⟩ [
{ lo := ⟨(405), 64⟩, hi := ⟨(253223), 40000⟩, pieceRef := 0 },
{ lo := ⟨(253223), 40000⟩, hi := ⟨(31731), 5000⟩, pieceRef := 1 },
{ lo := ⟨(31731), 5000⟩, hi := ⟨(254473), 40000⟩, pieceRef := 2 },
{ lo := ⟨(254473), 40000⟩, hi := ⟨(127549), 20000⟩, pieceRef := 3 },
{ lo := ⟨(127549), 20000⟩, hi := ⟨(255723), 40000⟩, pieceRef := 4 },
{ lo := ⟨(255723), 40000⟩, hi := ⟨(64087), 10000⟩, pieceRef := 5 },
{ lo := ⟨(64087), 10000⟩, hi := ⟨(256973), 40000⟩, pieceRef := 6 },
{ lo := ⟨(256973), 40000⟩, hi := ⟨(128799), 20000⟩, pieceRef := 7 },
{ lo := ⟨(128799), 20000⟩, hi := ⟨(258223), 40000⟩, pieceRef := 8 },
{ lo := ⟨(258223), 40000⟩, hi := ⟨(8089), 1250⟩, pieceRef := 73 },
{ lo := ⟨(8089), 1250⟩, hi := ⟨(259473), 40000⟩, pieceRef := 74 },
{ lo := ⟨(259473), 40000⟩, hi := ⟨(130049), 20000⟩, pieceRef := 75 },
{ lo := ⟨(130049), 20000⟩, hi := ⟨(260723), 40000⟩, pieceRef := 76 },
{ lo := ⟨(260723), 40000⟩, hi := ⟨(65337), 10000⟩, pieceRef := 77 },
{ lo := ⟨(65337), 10000⟩, hi := ⟨(261973), 40000⟩, pieceRef := 78 },
{ lo := ⟨(261973), 40000⟩, hi := ⟨(105), 16⟩, pieceRef := 79 }]
def rows (p : Fin 15) : CompactRow := match p.val with | 0 => row0 | 1 => row1 | 2 => row2 | 3 => row3 | 4 => row4 | 5 => row5 | 6 => row6 | 7 => row7 | 8 => row8 | 9 => row9 | 10 => row10 | 11 => row11 | 12 => row12 | 13 => row13 | _ => row14
def box : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (825/128) | 2 => (795/128) | 3 => (825/128) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (825/128) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
def anchor : Fin 5 → ℚ := box.lo

open A1294GenericChecker
theorem canonical_0 : compactRowCanonical row0 = true := by decide
def segments0 : List SourceSegment := [
{lo := (405/64), hi := (253223/40000), piece := refinementPiece3},
{lo := (253223/40000), hi := (31731/5000), piece := refinementPiece4},
{lo := (31731/5000), hi := (254473/40000), piece := refinementPiece5},
{lo := (254473/40000), hi := (127549/20000), piece := refinementPiece6},
{lo := (127549/20000), hi := (255723/40000), piece := refinementPiece7},
{lo := (255723/40000), hi := (64087/10000), piece := refinementPiece8},
{lo := (64087/10000), hi := (256973/40000), piece := refinementPiece9},
{lo := (256973/40000), hi := (128799/20000), piece := refinementPiece10},
{lo := (128799/20000), hi := (825/128), piece := refinementPiece11}
]
theorem decode_0 : interpCompactRow catalog row0 = some (.floor (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) segments0) := by rfl
theorem segment_0_0 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (405/64), hi := (253223/40000), piece := refinementPiece3} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]
theorem segment_0_1 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (253223/40000), hi := (31731/5000), piece := refinementPiece4} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece4, MacroPiece.box]
theorem segment_0_2 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (31731/5000), hi := (254473/40000), piece := refinementPiece5} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece5, MacroPiece.box]
theorem segment_0_3 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (254473/40000), hi := (127549/20000), piece := refinementPiece6} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece6, MacroPiece.box]
theorem segment_0_4 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (127549/20000), hi := (255723/40000), piece := refinementPiece7} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece7, MacroPiece.box]
theorem segment_0_5 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (255723/40000), hi := (64087/10000), piece := refinementPiece8} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece8, MacroPiece.box]
theorem segment_0_6 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (64087/10000), hi := (256973/40000), piece := refinementPiece9} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece9, MacroPiece.box]
theorem segment_0_7 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (256973/40000), hi := (128799/20000), piece := refinementPiece10} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece10, MacroPiece.box]
theorem segment_0_8 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) {lo := (128799/20000), hi := (825/128), piece := refinementPiece11} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]
theorem coverage_0 : sourceCoverFrom (405/64) (825/128) segments0 = true := by
  norm_num [sourceCoverFrom, segments0]
theorem piecewise_0 : certifiedPiecewiseCheck (405/64) (825/128) (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) segments0 = true := by
  have hlen : decide (0 < segments0.length) = true := by norm_num [segments0]
  have hall : segments0.all (sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000)) = true := by
    simp only [segments0, List.all_cons, List.all_nil, segment_0_0, segment_0_1, segment_0_2, segment_0_3, segment_0_4, segment_0_5, segment_0_6, segment_0_7, segment_0_8, Bool.true_and]
  have hp : segments0.all (fun s => s.piece.check) = true := by
    simp only [segments0, List.all_cons, List.all_nil, refinementPiece3_check, refinementPiece4_check, refinementPiece5_check, refinementPiece6_check, refinementPiece7_check, refinementPiece8_check, refinementPiece9_check, refinementPiece10_check, refinementPiece11_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_0, hall, hp]

theorem canonical_1 : compactRowCanonical row1 = true := by decide
theorem decode_1 : interpCompactRow catalog row1 = some (.direct macroPiece11) := by rfl
theorem canonical_2 : compactRowCanonical row2 = true := by decide
def segments2 : List SourceSegment := [
{lo := (1215/64), hi := (4748093/250000), piece := refinementPiece48},
{lo := (4748093/250000), hi := (19007997/1000000), piece := refinementPiece49},
{lo := (19007997/1000000), hi := (9511811/500000), piece := refinementPiece50},
{lo := (9511811/500000), hi := (19039247/1000000), piece := refinementPiece51},
{lo := (19039247/1000000), hi := (2381859/125000), piece := refinementPiece52},
{lo := (2381859/125000), hi := (19070497/1000000), piece := refinementPiece53},
{lo := (19070497/1000000), hi := (9543061/500000), piece := refinementPiece54},
{lo := (9543061/500000), hi := (19101747/1000000), piece := refinementPiece55},
{lo := (19101747/1000000), hi := (4779343/250000), piece := refinementPiece56},
{lo := (4779343/250000), hi := (19132997/1000000), piece := refinementPiece57},
{lo := (19132997/1000000), hi := (9574311/500000), piece := refinementPiece58},
{lo := (9574311/500000), hi := (19164247/1000000), piece := refinementPiece59},
{lo := (19164247/1000000), hi := (599371/31250), piece := refinementPiece60},
{lo := (599371/31250), hi := (19195497/1000000), piece := refinementPiece61},
{lo := (19195497/1000000), hi := (9605561/500000), piece := refinementPiece62},
{lo := (9605561/500000), hi := (19226747/1000000), piece := refinementPiece63},
{lo := (19226747/1000000), hi := (4810593/250000), piece := refinementPiece64},
{lo := (4810593/250000), hi := (19257997/1000000), piece := refinementPiece65},
{lo := (19257997/1000000), hi := (9636811/500000), piece := refinementPiece66},
{lo := (9636811/500000), hi := (19289247/1000000), piece := refinementPiece67},
{lo := (19289247/1000000), hi := (2413109/125000), piece := refinementPiece68},
{lo := (2413109/125000), hi := (19320497/1000000), piece := refinementPiece69},
{lo := (19320497/1000000), hi := (2475/128), piece := refinementPiece70}
]
theorem decode_2 : interpCompactRow catalog row2 = some (.floor (1755263779336959657910023102330969/7812500000000000000000000000000000000000) segments2) := by rfl
theorem segment_2_0 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (1215/64), hi := (4748093/250000), piece := refinementPiece48} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece48, MacroPiece.box]
theorem segment_2_1 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (4748093/250000), hi := (19007997/1000000), piece := refinementPiece49} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece49, MacroPiece.box]
theorem segment_2_2 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19007997/1000000), hi := (9511811/500000), piece := refinementPiece50} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece50, MacroPiece.box]
theorem segment_2_3 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9511811/500000), hi := (19039247/1000000), piece := refinementPiece51} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece51, MacroPiece.box]
theorem segment_2_4 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19039247/1000000), hi := (2381859/125000), piece := refinementPiece52} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece52, MacroPiece.box]
theorem segment_2_5 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (2381859/125000), hi := (19070497/1000000), piece := refinementPiece53} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece53, MacroPiece.box]
theorem segment_2_6 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19070497/1000000), hi := (9543061/500000), piece := refinementPiece54} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece54, MacroPiece.box]
theorem segment_2_7 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9543061/500000), hi := (19101747/1000000), piece := refinementPiece55} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]
theorem segment_2_8 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19101747/1000000), hi := (4779343/250000), piece := refinementPiece56} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]
theorem segment_2_9 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (4779343/250000), hi := (19132997/1000000), piece := refinementPiece57} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]
theorem segment_2_10 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19132997/1000000), hi := (9574311/500000), piece := refinementPiece58} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]
theorem segment_2_11 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9574311/500000), hi := (19164247/1000000), piece := refinementPiece59} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]
theorem segment_2_12 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19164247/1000000), hi := (599371/31250), piece := refinementPiece60} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]
theorem segment_2_13 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (599371/31250), hi := (19195497/1000000), piece := refinementPiece61} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]
theorem segment_2_14 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19195497/1000000), hi := (9605561/500000), piece := refinementPiece62} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]
theorem segment_2_15 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9605561/500000), hi := (19226747/1000000), piece := refinementPiece63} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]
theorem segment_2_16 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19226747/1000000), hi := (4810593/250000), piece := refinementPiece64} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]
theorem segment_2_17 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (4810593/250000), hi := (19257997/1000000), piece := refinementPiece65} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]
theorem segment_2_18 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19257997/1000000), hi := (9636811/500000), piece := refinementPiece66} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]
theorem segment_2_19 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9636811/500000), hi := (19289247/1000000), piece := refinementPiece67} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]
theorem segment_2_20 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19289247/1000000), hi := (2413109/125000), piece := refinementPiece68} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]
theorem segment_2_21 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (2413109/125000), hi := (19320497/1000000), piece := refinementPiece69} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]
theorem segment_2_22 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19320497/1000000), hi := (2475/128), piece := refinementPiece70} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]
theorem coverage_2 : sourceCoverFrom (1215/64) (2475/128) segments2 = true := by
  norm_num [sourceCoverFrom, segments2]
theorem piecewise_2 : certifiedPiecewiseCheck (1215/64) (2475/128) (1755263779336959657910023102330969/7812500000000000000000000000000000000000) segments2 = true := by
  have hlen : decide (0 < segments2.length) = true := by norm_num [segments2]
  have hall : segments2.all (sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000)) = true := by
    simp only [segments2, List.all_cons, List.all_nil, segment_2_0, segment_2_1, segment_2_2, segment_2_3, segment_2_4, segment_2_5, segment_2_6, segment_2_7, segment_2_8, segment_2_9, segment_2_10, segment_2_11, segment_2_12, segment_2_13, segment_2_14, segment_2_15, segment_2_16, segment_2_17, segment_2_18, segment_2_19, segment_2_20, segment_2_21, segment_2_22, Bool.true_and]
  have hp : segments2.all (fun s => s.piece.check) = true := by
    simp only [segments2, List.all_cons, List.all_nil, refinementPiece48_check, refinementPiece49_check, refinementPiece50_check, refinementPiece51_check, refinementPiece52_check, refinementPiece53_check, refinementPiece54_check, refinementPiece55_check, refinementPiece56_check, refinementPiece57_check, refinementPiece58_check, refinementPiece59_check, refinementPiece60_check, refinementPiece61_check, refinementPiece62_check, refinementPiece63_check, refinementPiece64_check, refinementPiece65_check, refinementPiece66_check, refinementPiece67_check, refinementPiece68_check, refinementPiece69_check, refinementPiece70_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_2, hall, hp]

theorem canonical_3 : compactRowCanonical row3 = true := by decide
def segments3 : List SourceSegment := [
{lo := (3255/128), hi := (5086319/200000), piece := refinementPiece84},
{lo := (5086319/200000), hi := (1272361/50000), piece := refinementPiece85},
{lo := (1272361/50000), hi := (5092569/200000), piece := refinementPiece86},
{lo := (5092569/200000), hi := (2547847/100000), piece := refinementPiece87},
{lo := (2547847/100000), hi := (5098819/200000), piece := refinementPiece88},
{lo := (5098819/200000), hi := (637743/25000), piece := refinementPiece89},
{lo := (637743/25000), hi := (5105069/200000), piece := refinementPiece90},
{lo := (5105069/200000), hi := (2554097/100000), piece := refinementPiece91},
{lo := (2554097/100000), hi := (5111319/200000), piece := refinementPiece92},
{lo := (5111319/200000), hi := (1278611/50000), piece := refinementPiece93},
{lo := (1278611/50000), hi := (5117569/200000), piece := refinementPiece94},
{lo := (5117569/200000), hi := (2560347/100000), piece := refinementPiece95},
{lo := (2560347/100000), hi := (5123819/200000), piece := macroPiece24},
{lo := (5123819/200000), hi := (160217/6250), piece := macroPiece24},
{lo := (160217/6250), hi := (5130069/200000), piece := refinementPiece98},
{lo := (5130069/200000), hi := (2566597/100000), piece := refinementPiece99},
{lo := (2566597/100000), hi := (5136319/200000), piece := refinementPiece100},
{lo := (5136319/200000), hi := (1284861/50000), piece := refinementPiece101},
{lo := (1284861/50000), hi := (5142569/200000), piece := refinementPiece102},
{lo := (5142569/200000), hi := (2572847/100000), piece := refinementPiece103},
{lo := (2572847/100000), hi := (5148819/200000), piece := refinementPiece104},
{lo := (5148819/200000), hi := (643993/25000), piece := refinementPiece105},
{lo := (643993/25000), hi := (5155069/200000), piece := refinementPiece106},
{lo := (5155069/200000), hi := (2579097/100000), piece := refinementPiece107},
{lo := (2579097/100000), hi := (5161319/200000), piece := refinementPiece108},
{lo := (5161319/200000), hi := (1291111/50000), piece := refinementPiece109},
{lo := (1291111/50000), hi := (5167569/200000), piece := refinementPiece110},
{lo := (5167569/200000), hi := (2585347/100000), piece := refinementPiece111},
{lo := (2585347/100000), hi := (5173819/200000), piece := refinementPiece112},
{lo := (5173819/200000), hi := (323559/12500), piece := refinementPiece113},
{lo := (323559/12500), hi := (3315/128), piece := refinementPiece114}
]
theorem decode_3 : interpCompactRow catalog row3 = some (.floor (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) segments3) := by rfl
theorem segment_3_0 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (3255/128), hi := (5086319/200000), piece := refinementPiece84} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece84, MacroPiece.box]
theorem segment_3_1 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5086319/200000), hi := (1272361/50000), piece := refinementPiece85} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece85, MacroPiece.box]
theorem segment_3_2 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1272361/50000), hi := (5092569/200000), piece := refinementPiece86} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece86, MacroPiece.box]
theorem segment_3_3 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5092569/200000), hi := (2547847/100000), piece := refinementPiece87} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece87, MacroPiece.box]
theorem segment_3_4 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2547847/100000), hi := (5098819/200000), piece := refinementPiece88} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece88, MacroPiece.box]
theorem segment_3_5 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5098819/200000), hi := (637743/25000), piece := refinementPiece89} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece89, MacroPiece.box]
theorem segment_3_6 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (637743/25000), hi := (5105069/200000), piece := refinementPiece90} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece90, MacroPiece.box]
theorem segment_3_7 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5105069/200000), hi := (2554097/100000), piece := refinementPiece91} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece91, MacroPiece.box]
theorem segment_3_8 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2554097/100000), hi := (5111319/200000), piece := refinementPiece92} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece92, MacroPiece.box]
theorem segment_3_9 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5111319/200000), hi := (1278611/50000), piece := refinementPiece93} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece93, MacroPiece.box]
theorem segment_3_10 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1278611/50000), hi := (5117569/200000), piece := refinementPiece94} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece94, MacroPiece.box]
theorem segment_3_11 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5117569/200000), hi := (2560347/100000), piece := refinementPiece95} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece95, MacroPiece.box]
theorem segment_3_12 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2560347/100000), hi := (5123819/200000), piece := macroPiece24} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]
theorem segment_3_13 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5123819/200000), hi := (160217/6250), piece := macroPiece24} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]
theorem segment_3_14 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (160217/6250), hi := (5130069/200000), piece := refinementPiece98} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece98, MacroPiece.box]
theorem segment_3_15 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5130069/200000), hi := (2566597/100000), piece := refinementPiece99} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece99, MacroPiece.box]
theorem segment_3_16 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2566597/100000), hi := (5136319/200000), piece := refinementPiece100} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece100, MacroPiece.box]
theorem segment_3_17 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5136319/200000), hi := (1284861/50000), piece := refinementPiece101} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece101, MacroPiece.box]
theorem segment_3_18 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1284861/50000), hi := (5142569/200000), piece := refinementPiece102} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece102, MacroPiece.box]
theorem segment_3_19 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5142569/200000), hi := (2572847/100000), piece := refinementPiece103} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece103, MacroPiece.box]
theorem segment_3_20 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2572847/100000), hi := (5148819/200000), piece := refinementPiece104} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece104, MacroPiece.box]
theorem segment_3_21 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5148819/200000), hi := (643993/25000), piece := refinementPiece105} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece105, MacroPiece.box]
theorem segment_3_22 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (643993/25000), hi := (5155069/200000), piece := refinementPiece106} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece106, MacroPiece.box]
theorem segment_3_23 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5155069/200000), hi := (2579097/100000), piece := refinementPiece107} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece107, MacroPiece.box]
theorem segment_3_24 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2579097/100000), hi := (5161319/200000), piece := refinementPiece108} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece108, MacroPiece.box]
theorem segment_3_25 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5161319/200000), hi := (1291111/50000), piece := refinementPiece109} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece109, MacroPiece.box]
theorem segment_3_26 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1291111/50000), hi := (5167569/200000), piece := refinementPiece110} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece110, MacroPiece.box]
theorem segment_3_27 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5167569/200000), hi := (2585347/100000), piece := refinementPiece111} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece111, MacroPiece.box]
theorem segment_3_28 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2585347/100000), hi := (5173819/200000), piece := refinementPiece112} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece112, MacroPiece.box]
theorem segment_3_29 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5173819/200000), hi := (323559/12500), piece := refinementPiece113} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece113, MacroPiece.box]
theorem segment_3_30 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (323559/12500), hi := (3315/128), piece := refinementPiece114} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece114, MacroPiece.box]
theorem coverage_3 : sourceCoverFrom (3255/128) (3315/128) segments3 = true := by
  norm_num [sourceCoverFrom, segments3]
theorem piecewise_3 : certifiedPiecewiseCheck (3255/128) (3315/128) (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) segments3 = true := by
  have hlen : decide (0 < segments3.length) = true := by norm_num [segments3]
  have hall : segments3.all (sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000)) = true := by
    simp only [segments3, List.all_cons, List.all_nil, segment_3_0, segment_3_1, segment_3_2, segment_3_3, segment_3_4, segment_3_5, segment_3_6, segment_3_7, segment_3_8, segment_3_9, segment_3_10, segment_3_11, segment_3_12, segment_3_13, segment_3_14, segment_3_15, segment_3_16, segment_3_17, segment_3_18, segment_3_19, segment_3_20, segment_3_21, segment_3_22, segment_3_23, segment_3_24, segment_3_25, segment_3_26, segment_3_27, segment_3_28, segment_3_29, segment_3_30, Bool.true_and]
  have hp : segments3.all (fun s => s.piece.check) = true := by
    simp only [segments3, List.all_cons, List.all_nil, refinementPiece84_check, refinementPiece85_check, refinementPiece86_check, refinementPiece87_check, refinementPiece88_check, refinementPiece89_check, refinementPiece90_check, refinementPiece91_check, refinementPiece92_check, refinementPiece93_check, refinementPiece94_check, refinementPiece95_check, macroPiece24_check, refinementPiece98_check, refinementPiece99_check, refinementPiece100_check, refinementPiece101_check, refinementPiece102_check, refinementPiece103_check, refinementPiece104_check, refinementPiece105_check, refinementPiece106_check, refinementPiece107_check, refinementPiece108_check, refinementPiece109_check, refinementPiece110_check, refinementPiece111_check, refinementPiece112_check, refinementPiece113_check, refinementPiece114_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_3, hall, hp]

theorem canonical_4 : compactRowCanonical row4 = true := by decide
def segments4 : List SourceSegment := [
{lo := (4065/128), hi := (1587913/50000), piece := refinementPiece160},
{lo := (1587913/50000), hi := (6354777/200000), piece := refinementPiece161},
{lo := (6354777/200000), hi := (3178951/100000), piece := refinementPiece162},
{lo := (3178951/100000), hi := (6361027/200000), piece := refinementPiece163},
{lo := (6361027/200000), hi := (795519/25000), piece := refinementPiece164},
{lo := (795519/25000), hi := (6367277/200000), piece := refinementPiece165},
{lo := (6367277/200000), hi := (3185201/100000), piece := refinementPiece166},
{lo := (3185201/100000), hi := (6373527/200000), piece := refinementPiece167},
{lo := (6373527/200000), hi := (6448527/200000), piece := macroPiece30},
{lo := (6448527/200000), hi := (4155/128), piece := macroPiece31}
]
theorem decode_4 : interpCompactRow catalog row4 = some (.floor (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) segments4) := by rfl
theorem segment_4_0 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (4065/128), hi := (1587913/50000), piece := refinementPiece160} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece160, MacroPiece.box]
theorem segment_4_1 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (1587913/50000), hi := (6354777/200000), piece := refinementPiece161} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece161, MacroPiece.box]
theorem segment_4_2 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (6354777/200000), hi := (3178951/100000), piece := refinementPiece162} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece162, MacroPiece.box]
theorem segment_4_3 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (3178951/100000), hi := (6361027/200000), piece := refinementPiece163} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece163, MacroPiece.box]
theorem segment_4_4 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (6361027/200000), hi := (795519/25000), piece := refinementPiece164} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece164, MacroPiece.box]
theorem segment_4_5 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (795519/25000), hi := (6367277/200000), piece := refinementPiece165} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece165, MacroPiece.box]
theorem segment_4_6 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (6367277/200000), hi := (3185201/100000), piece := refinementPiece166} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece166, MacroPiece.box]
theorem segment_4_7 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (3185201/100000), hi := (6373527/200000), piece := refinementPiece167} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece167, MacroPiece.box]
theorem segment_4_8 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (6373527/200000), hi := (6448527/200000), piece := macroPiece30} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece30, MacroPiece.box]
theorem segment_4_9 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) {lo := (6448527/200000), hi := (4155/128), piece := macroPiece31} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece31, MacroPiece.box]
theorem coverage_4 : sourceCoverFrom (4065/128) (4155/128) segments4 = true := by
  norm_num [sourceCoverFrom, segments4]
theorem piecewise_4 : certifiedPiecewiseCheck (4065/128) (4155/128) (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) segments4 = true := by
  have hlen : decide (0 < segments4.length) = true := by norm_num [segments4]
  have hall : segments4.all (sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000)) = true := by
    simp only [segments4, List.all_cons, List.all_nil, segment_4_0, segment_4_1, segment_4_2, segment_4_3, segment_4_4, segment_4_5, segment_4_6, segment_4_7, segment_4_8, segment_4_9, Bool.true_and]
  have hp : segments4.all (fun s => s.piece.check) = true := by
    simp only [segments4, List.all_cons, List.all_nil, refinementPiece160_check, refinementPiece161_check, refinementPiece162_check, refinementPiece163_check, refinementPiece164_check, refinementPiece165_check, refinementPiece166_check, refinementPiece167_check, macroPiece30_check, macroPiece31_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_4, hall, hp]

theorem canonical_5 : compactRowCanonical row5 = true := by decide
def segments5 : List SourceSegment := [
{lo := (825/128), hi := (258223/40000), piece := refinementPiece11},
{lo := (258223/40000), hi := (8089/1250), piece := refinementPiece12},
{lo := (8089/1250), hi := (259473/40000), piece := refinementPiece13},
{lo := (259473/40000), hi := (130049/20000), piece := refinementPiece14},
{lo := (130049/20000), hi := (260723/40000), piece := refinementPiece15},
{lo := (260723/40000), hi := (65337/10000), piece := refinementPiece16},
{lo := (65337/10000), hi := (261973/40000), piece := refinementPiece17},
{lo := (261973/40000), hi := (105/16), piece := refinementPiece18}
]
theorem decode_5 : interpCompactRow catalog row5 = some (.floor (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments5) := by rfl
theorem segment_5_0 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (825/128), hi := (258223/40000), piece := refinementPiece11} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]
theorem segment_5_1 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (258223/40000), hi := (8089/1250), piece := refinementPiece12} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]
theorem segment_5_2 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (8089/1250), hi := (259473/40000), piece := refinementPiece13} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]
theorem segment_5_3 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (259473/40000), hi := (130049/20000), piece := refinementPiece14} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]
theorem segment_5_4 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (130049/20000), hi := (260723/40000), piece := refinementPiece15} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]
theorem segment_5_5 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (260723/40000), hi := (65337/10000), piece := refinementPiece16} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]
theorem segment_5_6 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (65337/10000), hi := (261973/40000), piece := refinementPiece17} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]
theorem segment_5_7 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (261973/40000), hi := (105/16), piece := refinementPiece18} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]
theorem coverage_5 : sourceCoverFrom (825/128) (105/16) segments5 = true := by
  norm_num [sourceCoverFrom, segments5]
theorem piecewise_5 : certifiedPiecewiseCheck (825/128) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments5 = true := by
  have hlen : decide (0 < segments5.length) = true := by norm_num [segments5]
  have hall : segments5.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments5, List.all_cons, List.all_nil, segment_5_0, segment_5_1, segment_5_2, segment_5_3, segment_5_4, segment_5_5, segment_5_6, segment_5_7, Bool.true_and]
  have hp : segments5.all (fun s => s.piece.check) = true := by
    simp only [segments5, List.all_cons, List.all_nil, refinementPiece11_check, refinementPiece12_check, refinementPiece13_check, refinementPiece14_check, refinementPiece15_check, refinementPiece16_check, refinementPiece17_check, refinementPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_5, hall, hp]

theorem canonical_6 : compactRowCanonical row6 = true := by decide
def segments6 : List SourceSegment := [
{lo := (405/32), hi := (633077/50000), piece := refinementPiece41},
{lo := (633077/50000), hi := (2535433/200000), piece := refinementPiece42},
{lo := (2535433/200000), hi := (1269279/100000), piece := refinementPiece43},
{lo := (1269279/100000), hi := (2541683/200000), piece := refinementPiece44},
{lo := (2541683/200000), hi := (318101/25000), piece := refinementPiece45},
{lo := (318101/25000), hi := (2547933/200000), piece := refinementPiece46},
{lo := (2547933/200000), hi := (1275529/100000), piece := macroPiece9},
{lo := (1275529/100000), hi := (12755291/1000000), piece := macroPiece10},
{lo := (12755291/1000000), hi := (825/64), piece := macroPiece11}
]
theorem decode_6 : interpCompactRow catalog row6 = some (.floor (0) segments6) := by
  change some (ModelRow.floor (interpRat ⟨0,1⟩) segments6) = _
  norm_num [interpRat]
theorem segment_6_0 : sourceSegmentCheck (0) {lo := (405/32), hi := (633077/50000), piece := refinementPiece41} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece41, MacroPiece.box]
theorem segment_6_1 : sourceSegmentCheck (0) {lo := (633077/50000), hi := (2535433/200000), piece := refinementPiece42} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece42, MacroPiece.box]
theorem segment_6_2 : sourceSegmentCheck (0) {lo := (2535433/200000), hi := (1269279/100000), piece := refinementPiece43} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece43, MacroPiece.box]
theorem segment_6_3 : sourceSegmentCheck (0) {lo := (1269279/100000), hi := (2541683/200000), piece := refinementPiece44} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece44, MacroPiece.box]
theorem segment_6_4 : sourceSegmentCheck (0) {lo := (2541683/200000), hi := (318101/25000), piece := refinementPiece45} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece45, MacroPiece.box]
theorem segment_6_5 : sourceSegmentCheck (0) {lo := (318101/25000), hi := (2547933/200000), piece := refinementPiece46} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece46, MacroPiece.box]
theorem segment_6_6 : sourceSegmentCheck (0) {lo := (2547933/200000), hi := (1275529/100000), piece := macroPiece9} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece9, MacroPiece.box]
theorem segment_6_7 : sourceSegmentCheck (0) {lo := (1275529/100000), hi := (12755291/1000000), piece := macroPiece10} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece10, MacroPiece.box]
theorem segment_6_8 : sourceSegmentCheck (0) {lo := (12755291/1000000), hi := (825/64), piece := macroPiece11} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece11, MacroPiece.box]
theorem coverage_6 : sourceCoverFrom (405/32) (825/64) segments6 = true := by
  norm_num [sourceCoverFrom, segments6]
theorem piecewise_6 : certifiedPiecewiseCheck (405/32) (825/64) (0) segments6 = true := by
  have hlen : decide (0 < segments6.length) = true := by norm_num [segments6]
  have hall : segments6.all (sourceSegmentCheck (0)) = true := by
    simp only [segments6, List.all_cons, List.all_nil, segment_6_0, segment_6_1, segment_6_2, segment_6_3, segment_6_4, segment_6_5, segment_6_6, segment_6_7, segment_6_8, Bool.true_and]
  have hp : segments6.all (fun s => s.piece.check) = true := by
    simp only [segments6, List.all_cons, List.all_nil, refinementPiece41_check, refinementPiece42_check, refinementPiece43_check, refinementPiece44_check, refinementPiece45_check, refinementPiece46_check, macroPiece9_check, macroPiece10_check, macroPiece11_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_6, hall, hp]

theorem canonical_7 : compactRowCanonical row7 = true := by decide
def segments7 : List SourceSegment := [
{lo := (2445/128), hi := (19101747/1000000), piece := refinementPiece55},
{lo := (19101747/1000000), hi := (4779343/250000), piece := refinementPiece56},
{lo := (4779343/250000), hi := (19132997/1000000), piece := refinementPiece57},
{lo := (19132997/1000000), hi := (9574311/500000), piece := refinementPiece58},
{lo := (9574311/500000), hi := (19164247/1000000), piece := refinementPiece59},
{lo := (19164247/1000000), hi := (599371/31250), piece := refinementPiece60},
{lo := (599371/31250), hi := (19195497/1000000), piece := refinementPiece61},
{lo := (19195497/1000000), hi := (9605561/500000), piece := refinementPiece62},
{lo := (9605561/500000), hi := (19226747/1000000), piece := refinementPiece63},
{lo := (19226747/1000000), hi := (4810593/250000), piece := refinementPiece64},
{lo := (4810593/250000), hi := (19257997/1000000), piece := refinementPiece65},
{lo := (19257997/1000000), hi := (9636811/500000), piece := refinementPiece66},
{lo := (9636811/500000), hi := (19289247/1000000), piece := refinementPiece67},
{lo := (19289247/1000000), hi := (2413109/125000), piece := refinementPiece68},
{lo := (2413109/125000), hi := (19320497/1000000), piece := refinementPiece69},
{lo := (19320497/1000000), hi := (9668061/500000), piece := refinementPiece70},
{lo := (9668061/500000), hi := (19351747/1000000), piece := refinementPiece71},
{lo := (19351747/1000000), hi := (1245/64), piece := macroPiece18}
]
theorem decode_7 : interpCompactRow catalog row7 = some (.floor (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) segments7) := by rfl
theorem segment_7_0 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (2445/128), hi := (19101747/1000000), piece := refinementPiece55} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]
theorem segment_7_1 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19101747/1000000), hi := (4779343/250000), piece := refinementPiece56} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]
theorem segment_7_2 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (4779343/250000), hi := (19132997/1000000), piece := refinementPiece57} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]
theorem segment_7_3 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19132997/1000000), hi := (9574311/500000), piece := refinementPiece58} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]
theorem segment_7_4 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (9574311/500000), hi := (19164247/1000000), piece := refinementPiece59} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]
theorem segment_7_5 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19164247/1000000), hi := (599371/31250), piece := refinementPiece60} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]
theorem segment_7_6 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (599371/31250), hi := (19195497/1000000), piece := refinementPiece61} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]
theorem segment_7_7 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19195497/1000000), hi := (9605561/500000), piece := refinementPiece62} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]
theorem segment_7_8 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (9605561/500000), hi := (19226747/1000000), piece := refinementPiece63} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]
theorem segment_7_9 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19226747/1000000), hi := (4810593/250000), piece := refinementPiece64} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]
theorem segment_7_10 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (4810593/250000), hi := (19257997/1000000), piece := refinementPiece65} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]
theorem segment_7_11 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19257997/1000000), hi := (9636811/500000), piece := refinementPiece66} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]
theorem segment_7_12 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (9636811/500000), hi := (19289247/1000000), piece := refinementPiece67} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]
theorem segment_7_13 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19289247/1000000), hi := (2413109/125000), piece := refinementPiece68} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]
theorem segment_7_14 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (2413109/125000), hi := (19320497/1000000), piece := refinementPiece69} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]
theorem segment_7_15 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19320497/1000000), hi := (9668061/500000), piece := refinementPiece70} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]
theorem segment_7_16 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (9668061/500000), hi := (19351747/1000000), piece := refinementPiece71} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece71, MacroPiece.box]
theorem segment_7_17 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) {lo := (19351747/1000000), hi := (1245/64), piece := macroPiece18} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece18, MacroPiece.box]
theorem coverage_7 : sourceCoverFrom (2445/128) (1245/64) segments7 = true := by
  norm_num [sourceCoverFrom, segments7]
theorem piecewise_7 : certifiedPiecewiseCheck (2445/128) (1245/64) (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) segments7 = true := by
  have hlen : decide (0 < segments7.length) = true := by norm_num [segments7]
  have hall : segments7.all (sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000)) = true := by
    simp only [segments7, List.all_cons, List.all_nil, segment_7_0, segment_7_1, segment_7_2, segment_7_3, segment_7_4, segment_7_5, segment_7_6, segment_7_7, segment_7_8, segment_7_9, segment_7_10, segment_7_11, segment_7_12, segment_7_13, segment_7_14, segment_7_15, segment_7_16, segment_7_17, Bool.true_and]
  have hp : segments7.all (fun s => s.piece.check) = true := by
    simp only [segments7, List.all_cons, List.all_nil, refinementPiece55_check, refinementPiece56_check, refinementPiece57_check, refinementPiece58_check, refinementPiece59_check, refinementPiece60_check, refinementPiece61_check, refinementPiece62_check, refinementPiece63_check, refinementPiece64_check, refinementPiece65_check, refinementPiece66_check, refinementPiece67_check, refinementPiece68_check, refinementPiece69_check, refinementPiece70_check, refinementPiece71_check, macroPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_7, hall, hp]

theorem canonical_8 : compactRowCanonical row8 = true := by decide
def segments8 : List SourceSegment := [
{lo := (3255/128), hi := (5086319/200000), piece := refinementPiece84},
{lo := (5086319/200000), hi := (1272361/50000), piece := refinementPiece85},
{lo := (1272361/50000), hi := (5092569/200000), piece := refinementPiece86},
{lo := (5092569/200000), hi := (2547847/100000), piece := refinementPiece87},
{lo := (2547847/100000), hi := (5098819/200000), piece := refinementPiece88},
{lo := (5098819/200000), hi := (637743/25000), piece := refinementPiece89},
{lo := (637743/25000), hi := (5105069/200000), piece := refinementPiece90},
{lo := (5105069/200000), hi := (2554097/100000), piece := refinementPiece91},
{lo := (2554097/100000), hi := (5111319/200000), piece := refinementPiece92},
{lo := (5111319/200000), hi := (1278611/50000), piece := refinementPiece93},
{lo := (1278611/50000), hi := (5117569/200000), piece := refinementPiece94},
{lo := (5117569/200000), hi := (2560347/100000), piece := refinementPiece95},
{lo := (2560347/100000), hi := (5123819/200000), piece := macroPiece24},
{lo := (5123819/200000), hi := (160217/6250), piece := macroPiece24},
{lo := (160217/6250), hi := (5130069/200000), piece := refinementPiece98},
{lo := (5130069/200000), hi := (2566597/100000), piece := refinementPiece99},
{lo := (2566597/100000), hi := (5136319/200000), piece := refinementPiece100},
{lo := (5136319/200000), hi := (1284861/50000), piece := refinementPiece101},
{lo := (1284861/50000), hi := (5142569/200000), piece := refinementPiece102},
{lo := (5142569/200000), hi := (2572847/100000), piece := refinementPiece103},
{lo := (2572847/100000), hi := (5148819/200000), piece := refinementPiece104},
{lo := (5148819/200000), hi := (643993/25000), piece := refinementPiece105},
{lo := (643993/25000), hi := (5155069/200000), piece := refinementPiece106},
{lo := (5155069/200000), hi := (2579097/100000), piece := refinementPiece107},
{lo := (2579097/100000), hi := (5161319/200000), piece := refinementPiece108},
{lo := (5161319/200000), hi := (1291111/50000), piece := refinementPiece109},
{lo := (1291111/50000), hi := (5167569/200000), piece := refinementPiece110},
{lo := (5167569/200000), hi := (2585347/100000), piece := refinementPiece111},
{lo := (2585347/100000), hi := (5173819/200000), piece := refinementPiece112},
{lo := (5173819/200000), hi := (323559/12500), piece := refinementPiece113},
{lo := (323559/12500), hi := (5180069/200000), piece := refinementPiece114},
{lo := (5180069/200000), hi := (2591597/100000), piece := refinementPiece115},
{lo := (2591597/100000), hi := (5186319/200000), piece := refinementPiece116},
{lo := (5186319/200000), hi := (1297361/50000), piece := refinementPiece117},
{lo := (1297361/50000), hi := (5192569/200000), piece := refinementPiece118},
{lo := (5192569/200000), hi := (2597847/100000), piece := refinementPiece119},
{lo := (2597847/100000), hi := (1665/64), piece := macroPiece25}
]
theorem decode_8 : interpCompactRow catalog row8 = some (.floor (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) segments8) := by rfl
theorem segment_8_0 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (3255/128), hi := (5086319/200000), piece := refinementPiece84} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece84, MacroPiece.box]
theorem segment_8_1 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5086319/200000), hi := (1272361/50000), piece := refinementPiece85} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece85, MacroPiece.box]
theorem segment_8_2 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1272361/50000), hi := (5092569/200000), piece := refinementPiece86} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece86, MacroPiece.box]
theorem segment_8_3 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5092569/200000), hi := (2547847/100000), piece := refinementPiece87} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece87, MacroPiece.box]
theorem segment_8_4 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2547847/100000), hi := (5098819/200000), piece := refinementPiece88} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece88, MacroPiece.box]
theorem segment_8_5 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5098819/200000), hi := (637743/25000), piece := refinementPiece89} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece89, MacroPiece.box]
theorem segment_8_6 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (637743/25000), hi := (5105069/200000), piece := refinementPiece90} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece90, MacroPiece.box]
theorem segment_8_7 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5105069/200000), hi := (2554097/100000), piece := refinementPiece91} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece91, MacroPiece.box]
theorem segment_8_8 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2554097/100000), hi := (5111319/200000), piece := refinementPiece92} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece92, MacroPiece.box]
theorem segment_8_9 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5111319/200000), hi := (1278611/50000), piece := refinementPiece93} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece93, MacroPiece.box]
theorem segment_8_10 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1278611/50000), hi := (5117569/200000), piece := refinementPiece94} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece94, MacroPiece.box]
theorem segment_8_11 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5117569/200000), hi := (2560347/100000), piece := refinementPiece95} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece95, MacroPiece.box]
theorem segment_8_12 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2560347/100000), hi := (5123819/200000), piece := macroPiece24} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]
theorem segment_8_13 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5123819/200000), hi := (160217/6250), piece := macroPiece24} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]
theorem segment_8_14 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (160217/6250), hi := (5130069/200000), piece := refinementPiece98} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece98, MacroPiece.box]
theorem segment_8_15 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5130069/200000), hi := (2566597/100000), piece := refinementPiece99} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece99, MacroPiece.box]
theorem segment_8_16 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2566597/100000), hi := (5136319/200000), piece := refinementPiece100} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece100, MacroPiece.box]
theorem segment_8_17 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5136319/200000), hi := (1284861/50000), piece := refinementPiece101} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece101, MacroPiece.box]
theorem segment_8_18 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1284861/50000), hi := (5142569/200000), piece := refinementPiece102} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece102, MacroPiece.box]
theorem segment_8_19 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5142569/200000), hi := (2572847/100000), piece := refinementPiece103} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece103, MacroPiece.box]
theorem segment_8_20 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2572847/100000), hi := (5148819/200000), piece := refinementPiece104} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece104, MacroPiece.box]
theorem segment_8_21 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5148819/200000), hi := (643993/25000), piece := refinementPiece105} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece105, MacroPiece.box]
theorem segment_8_22 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (643993/25000), hi := (5155069/200000), piece := refinementPiece106} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece106, MacroPiece.box]
theorem segment_8_23 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5155069/200000), hi := (2579097/100000), piece := refinementPiece107} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece107, MacroPiece.box]
theorem segment_8_24 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2579097/100000), hi := (5161319/200000), piece := refinementPiece108} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece108, MacroPiece.box]
theorem segment_8_25 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5161319/200000), hi := (1291111/50000), piece := refinementPiece109} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece109, MacroPiece.box]
theorem segment_8_26 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1291111/50000), hi := (5167569/200000), piece := refinementPiece110} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece110, MacroPiece.box]
theorem segment_8_27 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5167569/200000), hi := (2585347/100000), piece := refinementPiece111} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece111, MacroPiece.box]
theorem segment_8_28 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2585347/100000), hi := (5173819/200000), piece := refinementPiece112} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece112, MacroPiece.box]
theorem segment_8_29 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5173819/200000), hi := (323559/12500), piece := refinementPiece113} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece113, MacroPiece.box]
theorem segment_8_30 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (323559/12500), hi := (5180069/200000), piece := refinementPiece114} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece114, MacroPiece.box]
theorem segment_8_31 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5180069/200000), hi := (2591597/100000), piece := refinementPiece115} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece115, MacroPiece.box]
theorem segment_8_32 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2591597/100000), hi := (5186319/200000), piece := refinementPiece116} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece116, MacroPiece.box]
theorem segment_8_33 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5186319/200000), hi := (1297361/50000), piece := refinementPiece117} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece117, MacroPiece.box]
theorem segment_8_34 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (1297361/50000), hi := (5192569/200000), piece := refinementPiece118} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece118, MacroPiece.box]
theorem segment_8_35 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (5192569/200000), hi := (2597847/100000), piece := refinementPiece119} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece119, MacroPiece.box]
theorem segment_8_36 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) {lo := (2597847/100000), hi := (1665/64), piece := macroPiece25} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece25, MacroPiece.box]
theorem coverage_8 : sourceCoverFrom (3255/128) (1665/64) segments8 = true := by
  norm_num [sourceCoverFrom, segments8]
theorem piecewise_8 : certifiedPiecewiseCheck (3255/128) (1665/64) (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) segments8 = true := by
  have hlen : decide (0 < segments8.length) = true := by norm_num [segments8]
  have hall : segments8.all (sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000)) = true := by
    simp only [segments8, List.all_cons, List.all_nil, segment_8_0, segment_8_1, segment_8_2, segment_8_3, segment_8_4, segment_8_5, segment_8_6, segment_8_7, segment_8_8, segment_8_9, segment_8_10, segment_8_11, segment_8_12, segment_8_13, segment_8_14, segment_8_15, segment_8_16, segment_8_17, segment_8_18, segment_8_19, segment_8_20, segment_8_21, segment_8_22, segment_8_23, segment_8_24, segment_8_25, segment_8_26, segment_8_27, segment_8_28, segment_8_29, segment_8_30, segment_8_31, segment_8_32, segment_8_33, segment_8_34, segment_8_35, segment_8_36, Bool.true_and]
  have hp : segments8.all (fun s => s.piece.check) = true := by
    simp only [segments8, List.all_cons, List.all_nil, refinementPiece84_check, refinementPiece85_check, refinementPiece86_check, refinementPiece87_check, refinementPiece88_check, refinementPiece89_check, refinementPiece90_check, refinementPiece91_check, refinementPiece92_check, refinementPiece93_check, refinementPiece94_check, refinementPiece95_check, macroPiece24_check, refinementPiece98_check, refinementPiece99_check, refinementPiece100_check, refinementPiece101_check, refinementPiece102_check, refinementPiece103_check, refinementPiece104_check, refinementPiece105_check, refinementPiece106_check, refinementPiece107_check, refinementPiece108_check, refinementPiece109_check, refinementPiece110_check, refinementPiece111_check, refinementPiece112_check, refinementPiece113_check, refinementPiece114_check, refinementPiece115_check, refinementPiece116_check, refinementPiece117_check, refinementPiece118_check, refinementPiece119_check, macroPiece25_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_8, hall, hp]

theorem canonical_9 : compactRowCanonical row9 = true := by decide
def segments9 : List SourceSegment := [
{lo := (795/128), hi := (250723/40000), piece := macroPiece2},
{lo := (250723/40000), hi := (62837/10000), piece := refinementPiece0},
{lo := (62837/10000), hi := (251973/40000), piece := refinementPiece1},
{lo := (251973/40000), hi := (126299/20000), piece := refinementPiece2},
{lo := (126299/20000), hi := (405/64), piece := refinementPiece3}
]
theorem decode_9 : interpCompactRow catalog row9 = some (.floor (21287960894909617826490440080249/5000000000000000000000000000000000) segments9) := by rfl
theorem segment_9_0 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) {lo := (795/128), hi := (250723/40000), piece := macroPiece2} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece2, MacroPiece.box]
theorem segment_9_1 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) {lo := (250723/40000), hi := (62837/10000), piece := refinementPiece0} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece0, MacroPiece.box]
theorem segment_9_2 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) {lo := (62837/10000), hi := (251973/40000), piece := refinementPiece1} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece1, MacroPiece.box]
theorem segment_9_3 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) {lo := (251973/40000), hi := (126299/20000), piece := refinementPiece2} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece2, MacroPiece.box]
theorem segment_9_4 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) {lo := (126299/20000), hi := (405/64), piece := refinementPiece3} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]
theorem coverage_9 : sourceCoverFrom (795/128) (405/64) segments9 = true := by
  norm_num [sourceCoverFrom, segments9]
theorem piecewise_9 : certifiedPiecewiseCheck (795/128) (405/64) (21287960894909617826490440080249/5000000000000000000000000000000000) segments9 = true := by
  have hlen : decide (0 < segments9.length) = true := by norm_num [segments9]
  have hall : segments9.all (sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000)) = true := by
    simp only [segments9, List.all_cons, List.all_nil, segment_9_0, segment_9_1, segment_9_2, segment_9_3, segment_9_4, Bool.true_and]
  have hp : segments9.all (fun s => s.piece.check) = true := by
    simp only [segments9, List.all_cons, List.all_nil, macroPiece2_check, refinementPiece0_check, refinementPiece1_check, refinementPiece2_check, refinementPiece3_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_9, hall, hp]

theorem canonical_10 : compactRowCanonical row10 = true := by decide
def segments10 : List SourceSegment := [
{lo := (405/32), hi := (633077/50000), piece := refinementPiece41},
{lo := (633077/50000), hi := (2535433/200000), piece := refinementPiece42},
{lo := (2535433/200000), hi := (1269279/100000), piece := refinementPiece43},
{lo := (1269279/100000), hi := (2541683/200000), piece := refinementPiece44},
{lo := (2541683/200000), hi := (318101/25000), piece := refinementPiece45},
{lo := (318101/25000), hi := (2547933/200000), piece := refinementPiece46},
{lo := (2547933/200000), hi := (1275529/100000), piece := macroPiece9},
{lo := (1275529/100000), hi := (12755291/1000000), piece := macroPiece10},
{lo := (12755291/1000000), hi := (825/64), piece := macroPiece11}
]
theorem decode_10 : interpCompactRow catalog row10 = some (.floor (0) segments10) := by
  change some (ModelRow.floor (interpRat ⟨0,1⟩) segments10) = _
  norm_num [interpRat]
theorem segment_10_0 : sourceSegmentCheck (0) {lo := (405/32), hi := (633077/50000), piece := refinementPiece41} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece41, MacroPiece.box]
theorem segment_10_1 : sourceSegmentCheck (0) {lo := (633077/50000), hi := (2535433/200000), piece := refinementPiece42} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece42, MacroPiece.box]
theorem segment_10_2 : sourceSegmentCheck (0) {lo := (2535433/200000), hi := (1269279/100000), piece := refinementPiece43} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece43, MacroPiece.box]
theorem segment_10_3 : sourceSegmentCheck (0) {lo := (1269279/100000), hi := (2541683/200000), piece := refinementPiece44} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece44, MacroPiece.box]
theorem segment_10_4 : sourceSegmentCheck (0) {lo := (2541683/200000), hi := (318101/25000), piece := refinementPiece45} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece45, MacroPiece.box]
theorem segment_10_5 : sourceSegmentCheck (0) {lo := (318101/25000), hi := (2547933/200000), piece := refinementPiece46} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece46, MacroPiece.box]
theorem segment_10_6 : sourceSegmentCheck (0) {lo := (2547933/200000), hi := (1275529/100000), piece := macroPiece9} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece9, MacroPiece.box]
theorem segment_10_7 : sourceSegmentCheck (0) {lo := (1275529/100000), hi := (12755291/1000000), piece := macroPiece10} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece10, MacroPiece.box]
theorem segment_10_8 : sourceSegmentCheck (0) {lo := (12755291/1000000), hi := (825/64), piece := macroPiece11} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece11, MacroPiece.box]
theorem coverage_10 : sourceCoverFrom (405/32) (825/64) segments10 = true := by
  norm_num [sourceCoverFrom, segments10]
theorem piecewise_10 : certifiedPiecewiseCheck (405/32) (825/64) (0) segments10 = true := by
  have hlen : decide (0 < segments10.length) = true := by norm_num [segments10]
  have hall : segments10.all (sourceSegmentCheck (0)) = true := by
    simp only [segments10, List.all_cons, List.all_nil, segment_10_0, segment_10_1, segment_10_2, segment_10_3, segment_10_4, segment_10_5, segment_10_6, segment_10_7, segment_10_8, Bool.true_and]
  have hp : segments10.all (fun s => s.piece.check) = true := by
    simp only [segments10, List.all_cons, List.all_nil, refinementPiece41_check, refinementPiece42_check, refinementPiece43_check, refinementPiece44_check, refinementPiece45_check, refinementPiece46_check, macroPiece9_check, macroPiece10_check, macroPiece11_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_10, hall, hp]

theorem canonical_11 : compactRowCanonical row11 = true := by decide
def segments11 : List SourceSegment := [
{lo := (1215/64), hi := (4748093/250000), piece := refinementPiece48},
{lo := (4748093/250000), hi := (19007997/1000000), piece := refinementPiece49},
{lo := (19007997/1000000), hi := (9511811/500000), piece := refinementPiece50},
{lo := (9511811/500000), hi := (19039247/1000000), piece := refinementPiece51},
{lo := (19039247/1000000), hi := (2381859/125000), piece := refinementPiece52},
{lo := (2381859/125000), hi := (19070497/1000000), piece := refinementPiece53},
{lo := (19070497/1000000), hi := (9543061/500000), piece := refinementPiece54},
{lo := (9543061/500000), hi := (19101747/1000000), piece := refinementPiece55},
{lo := (19101747/1000000), hi := (4779343/250000), piece := refinementPiece56},
{lo := (4779343/250000), hi := (19132997/1000000), piece := refinementPiece57},
{lo := (19132997/1000000), hi := (9574311/500000), piece := refinementPiece58},
{lo := (9574311/500000), hi := (19164247/1000000), piece := refinementPiece59},
{lo := (19164247/1000000), hi := (599371/31250), piece := refinementPiece60},
{lo := (599371/31250), hi := (19195497/1000000), piece := refinementPiece61},
{lo := (19195497/1000000), hi := (9605561/500000), piece := refinementPiece62},
{lo := (9605561/500000), hi := (19226747/1000000), piece := refinementPiece63},
{lo := (19226747/1000000), hi := (4810593/250000), piece := refinementPiece64},
{lo := (4810593/250000), hi := (19257997/1000000), piece := refinementPiece65},
{lo := (19257997/1000000), hi := (9636811/500000), piece := refinementPiece66},
{lo := (9636811/500000), hi := (19289247/1000000), piece := refinementPiece67},
{lo := (19289247/1000000), hi := (2413109/125000), piece := refinementPiece68},
{lo := (2413109/125000), hi := (19320497/1000000), piece := refinementPiece69},
{lo := (19320497/1000000), hi := (9668061/500000), piece := refinementPiece70},
{lo := (9668061/500000), hi := (19351747/1000000), piece := refinementPiece71},
{lo := (19351747/1000000), hi := (1245/64), piece := macroPiece18}
]
theorem decode_11 : interpCompactRow catalog row11 = some (.floor (1755263779336959657910023102330969/7812500000000000000000000000000000000000) segments11) := by rfl
theorem segment_11_0 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (1215/64), hi := (4748093/250000), piece := refinementPiece48} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece48, MacroPiece.box]
theorem segment_11_1 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (4748093/250000), hi := (19007997/1000000), piece := refinementPiece49} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece49, MacroPiece.box]
theorem segment_11_2 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19007997/1000000), hi := (9511811/500000), piece := refinementPiece50} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece50, MacroPiece.box]
theorem segment_11_3 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9511811/500000), hi := (19039247/1000000), piece := refinementPiece51} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece51, MacroPiece.box]
theorem segment_11_4 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19039247/1000000), hi := (2381859/125000), piece := refinementPiece52} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece52, MacroPiece.box]
theorem segment_11_5 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (2381859/125000), hi := (19070497/1000000), piece := refinementPiece53} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece53, MacroPiece.box]
theorem segment_11_6 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19070497/1000000), hi := (9543061/500000), piece := refinementPiece54} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece54, MacroPiece.box]
theorem segment_11_7 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9543061/500000), hi := (19101747/1000000), piece := refinementPiece55} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]
theorem segment_11_8 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19101747/1000000), hi := (4779343/250000), piece := refinementPiece56} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]
theorem segment_11_9 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (4779343/250000), hi := (19132997/1000000), piece := refinementPiece57} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]
theorem segment_11_10 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19132997/1000000), hi := (9574311/500000), piece := refinementPiece58} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]
theorem segment_11_11 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9574311/500000), hi := (19164247/1000000), piece := refinementPiece59} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]
theorem segment_11_12 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19164247/1000000), hi := (599371/31250), piece := refinementPiece60} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]
theorem segment_11_13 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (599371/31250), hi := (19195497/1000000), piece := refinementPiece61} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]
theorem segment_11_14 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19195497/1000000), hi := (9605561/500000), piece := refinementPiece62} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]
theorem segment_11_15 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9605561/500000), hi := (19226747/1000000), piece := refinementPiece63} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]
theorem segment_11_16 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19226747/1000000), hi := (4810593/250000), piece := refinementPiece64} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]
theorem segment_11_17 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (4810593/250000), hi := (19257997/1000000), piece := refinementPiece65} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]
theorem segment_11_18 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19257997/1000000), hi := (9636811/500000), piece := refinementPiece66} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]
theorem segment_11_19 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9636811/500000), hi := (19289247/1000000), piece := refinementPiece67} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]
theorem segment_11_20 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19289247/1000000), hi := (2413109/125000), piece := refinementPiece68} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]
theorem segment_11_21 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (2413109/125000), hi := (19320497/1000000), piece := refinementPiece69} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]
theorem segment_11_22 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19320497/1000000), hi := (9668061/500000), piece := refinementPiece70} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]
theorem segment_11_23 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (9668061/500000), hi := (19351747/1000000), piece := refinementPiece71} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece71, MacroPiece.box]
theorem segment_11_24 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) {lo := (19351747/1000000), hi := (1245/64), piece := macroPiece18} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece18, MacroPiece.box]
theorem coverage_11 : sourceCoverFrom (1215/64) (1245/64) segments11 = true := by
  norm_num [sourceCoverFrom, segments11]
theorem piecewise_11 : certifiedPiecewiseCheck (1215/64) (1245/64) (1755263779336959657910023102330969/7812500000000000000000000000000000000000) segments11 = true := by
  have hlen : decide (0 < segments11.length) = true := by norm_num [segments11]
  have hall : segments11.all (sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000)) = true := by
    simp only [segments11, List.all_cons, List.all_nil, segment_11_0, segment_11_1, segment_11_2, segment_11_3, segment_11_4, segment_11_5, segment_11_6, segment_11_7, segment_11_8, segment_11_9, segment_11_10, segment_11_11, segment_11_12, segment_11_13, segment_11_14, segment_11_15, segment_11_16, segment_11_17, segment_11_18, segment_11_19, segment_11_20, segment_11_21, segment_11_22, segment_11_23, segment_11_24, Bool.true_and]
  have hp : segments11.all (fun s => s.piece.check) = true := by
    simp only [segments11, List.all_cons, List.all_nil, refinementPiece48_check, refinementPiece49_check, refinementPiece50_check, refinementPiece51_check, refinementPiece52_check, refinementPiece53_check, refinementPiece54_check, refinementPiece55_check, refinementPiece56_check, refinementPiece57_check, refinementPiece58_check, refinementPiece59_check, refinementPiece60_check, refinementPiece61_check, refinementPiece62_check, refinementPiece63_check, refinementPiece64_check, refinementPiece65_check, refinementPiece66_check, refinementPiece67_check, refinementPiece68_check, refinementPiece69_check, refinementPiece70_check, refinementPiece71_check, macroPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_11, hall, hp]

theorem canonical_12 : compactRowCanonical row12 = true := by decide
def segments12 : List SourceSegment := [
{lo := (825/128), hi := (258223/40000), piece := refinementPiece11},
{lo := (258223/40000), hi := (8089/1250), piece := refinementPiece12},
{lo := (8089/1250), hi := (259473/40000), piece := refinementPiece13},
{lo := (259473/40000), hi := (130049/20000), piece := refinementPiece14},
{lo := (130049/20000), hi := (260723/40000), piece := refinementPiece15},
{lo := (260723/40000), hi := (65337/10000), piece := refinementPiece16},
{lo := (65337/10000), hi := (261973/40000), piece := refinementPiece17},
{lo := (261973/40000), hi := (105/16), piece := refinementPiece18}
]
theorem decode_12 : interpCompactRow catalog row12 = some (.floor (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments12) := by rfl
theorem segment_12_0 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (825/128), hi := (258223/40000), piece := refinementPiece11} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]
theorem segment_12_1 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (258223/40000), hi := (8089/1250), piece := refinementPiece12} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]
theorem segment_12_2 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (8089/1250), hi := (259473/40000), piece := refinementPiece13} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]
theorem segment_12_3 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (259473/40000), hi := (130049/20000), piece := refinementPiece14} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]
theorem segment_12_4 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (130049/20000), hi := (260723/40000), piece := refinementPiece15} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]
theorem segment_12_5 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (260723/40000), hi := (65337/10000), piece := refinementPiece16} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]
theorem segment_12_6 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (65337/10000), hi := (261973/40000), piece := refinementPiece17} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]
theorem segment_12_7 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (261973/40000), hi := (105/16), piece := refinementPiece18} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]
theorem coverage_12 : sourceCoverFrom (825/128) (105/16) segments12 = true := by
  norm_num [sourceCoverFrom, segments12]
theorem piecewise_12 : certifiedPiecewiseCheck (825/128) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments12 = true := by
  have hlen : decide (0 < segments12.length) = true := by norm_num [segments12]
  have hall : segments12.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments12, List.all_cons, List.all_nil, segment_12_0, segment_12_1, segment_12_2, segment_12_3, segment_12_4, segment_12_5, segment_12_6, segment_12_7, Bool.true_and]
  have hp : segments12.all (fun s => s.piece.check) = true := by
    simp only [segments12, List.all_cons, List.all_nil, refinementPiece11_check, refinementPiece12_check, refinementPiece13_check, refinementPiece14_check, refinementPiece15_check, refinementPiece16_check, refinementPiece17_check, refinementPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_12, hall, hp]

theorem canonical_13 : compactRowCanonical row13 = true := by decide
theorem decode_13 : interpCompactRow catalog row13 = some (.direct macroPiece11) := by rfl
theorem canonical_14 : compactRowCanonical row14 = true := by decide
def segments14 : List SourceSegment := [
{lo := (405/64), hi := (253223/40000), piece := refinementPiece3},
{lo := (253223/40000), hi := (31731/5000), piece := refinementPiece4},
{lo := (31731/5000), hi := (254473/40000), piece := refinementPiece5},
{lo := (254473/40000), hi := (127549/20000), piece := refinementPiece6},
{lo := (127549/20000), hi := (255723/40000), piece := refinementPiece7},
{lo := (255723/40000), hi := (64087/10000), piece := refinementPiece8},
{lo := (64087/10000), hi := (256973/40000), piece := refinementPiece9},
{lo := (256973/40000), hi := (128799/20000), piece := refinementPiece10},
{lo := (128799/20000), hi := (258223/40000), piece := refinementPiece11},
{lo := (258223/40000), hi := (8089/1250), piece := refinementPiece12},
{lo := (8089/1250), hi := (259473/40000), piece := refinementPiece13},
{lo := (259473/40000), hi := (130049/20000), piece := refinementPiece14},
{lo := (130049/20000), hi := (260723/40000), piece := refinementPiece15},
{lo := (260723/40000), hi := (65337/10000), piece := refinementPiece16},
{lo := (65337/10000), hi := (261973/40000), piece := refinementPiece17},
{lo := (261973/40000), hi := (105/16), piece := refinementPiece18}
]
theorem decode_14 : interpCompactRow catalog row14 = some (.floor (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments14) := by rfl
theorem segment_14_0 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (405/64), hi := (253223/40000), piece := refinementPiece3} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]
theorem segment_14_1 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (253223/40000), hi := (31731/5000), piece := refinementPiece4} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece4, MacroPiece.box]
theorem segment_14_2 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (31731/5000), hi := (254473/40000), piece := refinementPiece5} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece5, MacroPiece.box]
theorem segment_14_3 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (254473/40000), hi := (127549/20000), piece := refinementPiece6} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece6, MacroPiece.box]
theorem segment_14_4 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (127549/20000), hi := (255723/40000), piece := refinementPiece7} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece7, MacroPiece.box]
theorem segment_14_5 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (255723/40000), hi := (64087/10000), piece := refinementPiece8} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece8, MacroPiece.box]
theorem segment_14_6 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (64087/10000), hi := (256973/40000), piece := refinementPiece9} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece9, MacroPiece.box]
theorem segment_14_7 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (256973/40000), hi := (128799/20000), piece := refinementPiece10} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece10, MacroPiece.box]
theorem segment_14_8 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (128799/20000), hi := (258223/40000), piece := refinementPiece11} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]
theorem segment_14_9 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (258223/40000), hi := (8089/1250), piece := refinementPiece12} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]
theorem segment_14_10 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (8089/1250), hi := (259473/40000), piece := refinementPiece13} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]
theorem segment_14_11 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (259473/40000), hi := (130049/20000), piece := refinementPiece14} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]
theorem segment_14_12 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (130049/20000), hi := (260723/40000), piece := refinementPiece15} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]
theorem segment_14_13 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (260723/40000), hi := (65337/10000), piece := refinementPiece16} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]
theorem segment_14_14 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (65337/10000), hi := (261973/40000), piece := refinementPiece17} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]
theorem segment_14_15 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) {lo := (261973/40000), hi := (105/16), piece := refinementPiece18} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]
theorem coverage_14 : sourceCoverFrom (405/64) (105/16) segments14 = true := by
  norm_num [sourceCoverFrom, segments14]
theorem piecewise_14 : certifiedPiecewiseCheck (405/64) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments14 = true := by
  have hlen : decide (0 < segments14.length) = true := by norm_num [segments14]
  have hall : segments14.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments14, List.all_cons, List.all_nil, segment_14_0, segment_14_1, segment_14_2, segment_14_3, segment_14_4, segment_14_5, segment_14_6, segment_14_7, segment_14_8, segment_14_9, segment_14_10, segment_14_11, segment_14_12, segment_14_13, segment_14_14, segment_14_15, Bool.true_and]
  have hp : segments14.all (fun s => s.piece.check) = true := by
    simp only [segments14, List.all_cons, List.all_nil, refinementPiece3_check, refinementPiece4_check, refinementPiece5_check, refinementPiece6_check, refinementPiece7_check, refinementPiece8_check, refinementPiece9_check, refinementPiece10_check, refinementPiece11_check, refinementPiece12_check, refinementPiece13_check, refinementPiece14_check, refinementPiece15_check, refinementPiece16_check, refinementPiece17_check, refinementPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_14, hall, hp]

def distances (p : Fin 15) : RatInterval := match p.val with | 0 => ⟨(405/64), (825/128)⟩ | 1 => ⟨(1635/128), (1665/128)⟩ | 2 => ⟨(1215/64), (2475/128)⟩ | 3 => ⟨(3255/128), (3315/128)⟩ | 4 => ⟨(4065/128), (4155/128)⟩ | 5 => ⟨(825/128), (105/16)⟩ | 6 => ⟨(405/32), (825/64)⟩ | 7 => ⟨(2445/128), (1245/64)⟩ | 8 => ⟨(3255/128), (1665/64)⟩ | 9 => ⟨(795/128), (405/64)⟩ | 10 => ⟨(405/32), (825/64)⟩ | 11 => ⟨(1215/64), (1245/64)⟩ | 12 => ⟨(825/128), (105/16)⟩ | 13 => ⟨(1635/128), (105/8)⟩ | _ => ⟨(405/64), (105/16)⟩
theorem distances_exact : ∀ p, distanceInterval box p = distances p := by
  intro p
  fin_cases p <;> simp [distanceInterval, distances, gapSupport, pairLeft, pairRight, box, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num

theorem row_checked_0 : compactRowCheck catalog box (⟨0, by decide⟩ : Fin 15) row0 = true := by
  simp only [compactRowCheck, canonical_0, decode_0, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_0

theorem row_checked_1 : compactRowCheck catalog box (⟨1, by decide⟩ : Fin 15) row1 = true := by
  simp only [compactRowCheck, canonical_1, decode_1, Bool.true_and, modelCheck]
  rw [distances_exact]
  rw [macroPiece11_check]
  norm_num [distances, MacroPiece.box, macroPiece11]

theorem row_checked_2 : compactRowCheck catalog box (⟨2, by decide⟩ : Fin 15) row2 = true := by
  simp only [compactRowCheck, canonical_2, decode_2, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_2

theorem row_checked_3 : compactRowCheck catalog box (⟨3, by decide⟩ : Fin 15) row3 = true := by
  simp only [compactRowCheck, canonical_3, decode_3, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_3

theorem row_checked_4 : compactRowCheck catalog box (⟨4, by decide⟩ : Fin 15) row4 = true := by
  simp only [compactRowCheck, canonical_4, decode_4, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_4

theorem row_checked_5 : compactRowCheck catalog box (⟨5, by decide⟩ : Fin 15) row5 = true := by
  simp only [compactRowCheck, canonical_5, decode_5, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_5

theorem row_checked_6 : compactRowCheck catalog box (⟨6, by decide⟩ : Fin 15) row6 = true := by
  simp only [compactRowCheck, canonical_6, decode_6, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_6

theorem row_checked_7 : compactRowCheck catalog box (⟨7, by decide⟩ : Fin 15) row7 = true := by
  simp only [compactRowCheck, canonical_7, decode_7, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_7

theorem row_checked_8 : compactRowCheck catalog box (⟨8, by decide⟩ : Fin 15) row8 = true := by
  simp only [compactRowCheck, canonical_8, decode_8, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_8

theorem row_checked_9 : compactRowCheck catalog box (⟨9, by decide⟩ : Fin 15) row9 = true := by
  simp only [compactRowCheck, canonical_9, decode_9, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_9

theorem row_checked_10 : compactRowCheck catalog box (⟨10, by decide⟩ : Fin 15) row10 = true := by
  simp only [compactRowCheck, canonical_10, decode_10, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_10

theorem row_checked_11 : compactRowCheck catalog box (⟨11, by decide⟩ : Fin 15) row11 = true := by
  simp only [compactRowCheck, canonical_11, decode_11, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_11

theorem row_checked_12 : compactRowCheck catalog box (⟨12, by decide⟩ : Fin 15) row12 = true := by
  simp only [compactRowCheck, canonical_12, decode_12, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_12

theorem row_checked_13 : compactRowCheck catalog box (⟨13, by decide⟩ : Fin 15) row13 = true := by
  simp only [compactRowCheck, canonical_13, decode_13, Bool.true_and, modelCheck]
  rw [distances_exact]
  rw [macroPiece11_check]
  norm_num [distances, MacroPiece.box, macroPiece11]

theorem row_checked_14 : compactRowCheck catalog box (⟨14, by decide⟩ : Fin 15) row14 = true := by
  simp only [compactRowCheck, canonical_14, decode_14, Bool.true_and, modelCheck]
  rw [distances_exact]
  exact piecewise_14

def floors (p : Fin 15) : ℚ := match p.val with | 0 => (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) | 1 => (0) | 2 => (1755263779336959657910023102330969/7812500000000000000000000000000000000000) | 3 => (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) | 4 => (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) | 5 => (12892869620170946020955818564495929/50000000000000000000000000000000000000) | 6 => (0) | 7 => (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) | 8 => (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) | 9 => (21287960894909617826490440080249/5000000000000000000000000000000000) | 10 => (0) | 11 => (1755263779336959657910023102330969/7812500000000000000000000000000000000000) | 12 => (12892869620170946020955818564495929/50000000000000000000000000000000000000) | 13 => (0) | _ => (12892869620170946020955818564495929/50000000000000000000000000000000000000)
def terms (p : Fin 15) : RankOneModel :=
  if p.val = 1 then macroPieceRankModel (fun _ => macroPiece11) p
  else if p.val = 13 then macroPieceRankModel (fun _ => macroPiece11) p
  else {base := floors p, weight := 0, offset := 0, coeff := fun _ => 0}

theorem interpreted_terms : (fun p => interpModel (decodedRow catalog (rows p)) p) = terms := by
  funext p
  fin_cases p <;> simp [rows, decodedRow, decode_0, decode_1, decode_2, decode_3, decode_4, decode_5, decode_6, decode_7, decode_8, decode_9, decode_10, decode_11, decode_12, decode_13, decode_14, interpModel, terms, floors, interpRat]

theorem tangent_lower : rankTangentLower terms (1094977/5000000000) box anchor = (108853955129699356804065918948443215217/7812500000000000000000000000000000000000) := by
  norm_num [rankTangentLower, rankObjectiveRat, rankGradient, affineCoordinateLower, terms, floors, anchor, box, macroPiece11, MacroPiece.box, macroPieceRankModel, wellRankModel, wellSlope, wellOffset, consecutiveCoeff, gapSupport, RankOneModel.valueRat, RankOneModel.dotRat, pairLeft, pairRight, Finset.sum_filter, Fin.sum_univ_succ, Fin.sum_univ_five]
theorem tangent_checked : rankTangentCheck (647/50000) (1094977/5000000000) box anchor terms = true := by
  have ho : box.ordered = true := by
    rw [GapBox.ordered_iff]
    intro i
    fin_cases i <;> norm_num [box]
  have ha : ∀ i, box.lo i ≤ anchor i ∧ anchor i ≤ box.hi i := by
    intro i
    fin_cases i <;> norm_num [anchor, box]
  have hw : ∀ p, 0 ≤ (terms p).weight := by
    intro p
    fin_cases p <;> norm_num [terms, floors, macroPiece11, macroPieceRankModel, wellRankModel, wellSlope, wellOffset]
  have hm : (647/50000 : ℚ) ≤ rankTangentLower terms (1094977/5000000000) box anchor := by
    rw [tangent_lower]
    norm_num
  simp [rankTangentCheck, ho, ha, hw, hm]

theorem all_rows : ∀ p, compactRowCheck catalog box p (rows p) = true := by
  intro p
  fin_cases p
  · exact row_checked_0
  · exact row_checked_1
  · exact row_checked_2
  · exact row_checked_3
  · exact row_checked_4
  · exact row_checked_5
  · exact row_checked_6
  · exact row_checked_7
  · exact row_checked_8
  · exact row_checked_9
  · exact row_checked_10
  · exact row_checked_11
  · exact row_checked_12
  · exact row_checked_13
  · exact row_checked_14
theorem accepted : compactQuadraticLeafCheck catalog (647/50000) (1094977/5000000000) box anchor rows = true := by
  unfold compactQuadraticLeafCheck
  rw [interpreted_terms]
  simp [all_rows, tangent_checked]
theorem leaf_sound : ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=
  compactQuadraticLeafCheck_sound accepted
#print axioms all_rows
#print axioms tangent_checked
#print axioms decode_6
#print axioms decode_10
#print axioms accepted
#print axioms leaf_sound
end AuthenticCompactLeaf
