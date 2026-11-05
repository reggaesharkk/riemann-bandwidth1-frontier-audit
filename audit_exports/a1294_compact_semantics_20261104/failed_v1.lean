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
    refine ⟨t, he, ?_⟩
    have hc : certifiedPiecewiseCheck t.lo t.hi (interpRat floor) [t] = true := by
      simp only [he, Bool.and_eq_true] at h
      exact h.2
    intro x hlo hhi
    exact certifiedPiecewiseCheck_sound hc hlo hhi

#print axioms compactSegmentCheck_sound
end A1294Compact

