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

theorem first_floor_canonical :
    (CompactRat.mk 5170581624709583018970186520240204081 3200000000000000000000000000000000000000).check = true := by
  decide

theorem first_catalog_ref : catalog[0]? = some refinementPiece3 := by rfl

theorem first_segment_decode :
    interpSegment catalog { lo := ⟨405,64⟩, hi := ⟨253223,40000⟩, pieceRef := 0 } =
      some { lo := 405/64, hi := 253223/40000, piece := refinementPiece3 } := by rfl

#print axioms first_floor_canonical
#print axioms first_catalog_ref
#print axioms first_segment_decode
end AuthenticCompactLeaf
