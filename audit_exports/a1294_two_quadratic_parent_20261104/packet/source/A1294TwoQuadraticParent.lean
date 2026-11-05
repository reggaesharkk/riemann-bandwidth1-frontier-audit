import Zeta23.ThmD.Sextuple.AffineTree
import Zeta23.ThmD.Sextuple.Macro.AffineAdapter
import Zeta23.ThmD.Sextuple.A1275.RefinementData

open Zeta23.ThmD.Sextuple
open Zeta23.ThmD.Sextuple.MacroPrototype

noncomputable section

namespace A1294TwoQuadraticParent

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

-- Generated by generate_lean_data.py from siblings_normal.json.
def segments_left_0 : List SourceSegment := [
  { lo := 405/64, hi := 253223/40000, piece := refinementPiece3 },
  { lo := 253223/40000, hi := 31731/5000, piece := refinementPiece4 },
  { lo := 31731/5000, hi := 254473/40000, piece := refinementPiece5 },
  { lo := 254473/40000, hi := 127549/20000, piece := refinementPiece6 },
  { lo := 127549/20000, hi := 255723/40000, piece := refinementPiece7 },
  { lo := 255723/40000, hi := 64087/10000, piece := refinementPiece8 },
  { lo := 64087/10000, hi := 256973/40000, piece := refinementPiece9 },
  { lo := 256973/40000, hi := 128799/20000, piece := refinementPiece10 },
  { lo := 128799/20000, hi := 825/128, piece := refinementPiece11 }
]
theorem segments_left_0_segment_0_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 405/64, hi := 253223/40000, piece := refinementPiece3 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]

theorem segments_left_0_segment_1_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 253223/40000, hi := 31731/5000, piece := refinementPiece4 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece4, MacroPiece.box]

theorem segments_left_0_segment_2_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 31731/5000, hi := 254473/40000, piece := refinementPiece5 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece5, MacroPiece.box]

theorem segments_left_0_segment_3_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 254473/40000, hi := 127549/20000, piece := refinementPiece6 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece6, MacroPiece.box]

theorem segments_left_0_segment_4_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 127549/20000, hi := 255723/40000, piece := refinementPiece7 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece7, MacroPiece.box]

theorem segments_left_0_segment_5_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 255723/40000, hi := 64087/10000, piece := refinementPiece8 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece8, MacroPiece.box]

theorem segments_left_0_segment_6_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 64087/10000, hi := 256973/40000, piece := refinementPiece9 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece9, MacroPiece.box]

theorem segments_left_0_segment_7_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 256973/40000, hi := 128799/20000, piece := refinementPiece10 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece10, MacroPiece.box]

theorem segments_left_0_segment_8_checked : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) { lo := 128799/20000, hi := 825/128, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_left_0_accepted : sourcePiecewiseCheck (405/64) (825/128) (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) segments_left_0 = true := by
  have hlen : decide (0 < segments_left_0.length) = true := by norm_num [segments_left_0]
  have hcover : sourceCoverFrom (405/64) (825/128) segments_left_0 = true := by
    norm_num [sourceCoverFrom, segments_left_0]
  have hall : segments_left_0.all (sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000)) = true := by
    simp only [segments_left_0, List.all_cons, List.all_nil, segments_left_0_segment_0_checked, segments_left_0_segment_1_checked, segments_left_0_segment_2_checked, segments_left_0_segment_3_checked, segments_left_0_segment_4_checked, segments_left_0_segment_5_checked, segments_left_0_segment_6_checked, segments_left_0_segment_7_checked, segments_left_0_segment_8_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_0_pieces_checked : ∀ s ∈ segments_left_0, s.piece.check = true := by
  intro s hs
  simp only [segments_left_0, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece3_check
  · cases h; exact refinementPiece4_check
  · cases h; exact refinementPiece5_check
  · cases h; exact refinementPiece6_check
  · cases h; exact refinementPiece7_check
  · cases h; exact refinementPiece8_check
  · cases h; exact refinementPiece9_check
  · cases h; exact refinementPiece10_check
  · cases h; exact refinementPiece11_check

def segments_left_2 : List SourceSegment := [
  { lo := 1215/64, hi := 4748093/250000, piece := refinementPiece48 },
  { lo := 4748093/250000, hi := 19007997/1000000, piece := refinementPiece49 },
  { lo := 19007997/1000000, hi := 9511811/500000, piece := refinementPiece50 },
  { lo := 9511811/500000, hi := 19039247/1000000, piece := refinementPiece51 },
  { lo := 19039247/1000000, hi := 2381859/125000, piece := refinementPiece52 },
  { lo := 2381859/125000, hi := 19070497/1000000, piece := refinementPiece53 },
  { lo := 19070497/1000000, hi := 9543061/500000, piece := refinementPiece54 },
  { lo := 9543061/500000, hi := 19101747/1000000, piece := refinementPiece55 },
  { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 },
  { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 },
  { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 },
  { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 },
  { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 },
  { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 },
  { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 },
  { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 },
  { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 },
  { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 },
  { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 },
  { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 },
  { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 },
  { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 },
  { lo := 19320497/1000000, hi := 2475/128, piece := refinementPiece70 }
]
theorem segments_left_2_segment_0_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 1215/64, hi := 4748093/250000, piece := refinementPiece48 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece48, MacroPiece.box]

theorem segments_left_2_segment_1_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4748093/250000, hi := 19007997/1000000, piece := refinementPiece49 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece49, MacroPiece.box]

theorem segments_left_2_segment_2_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19007997/1000000, hi := 9511811/500000, piece := refinementPiece50 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece50, MacroPiece.box]

theorem segments_left_2_segment_3_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9511811/500000, hi := 19039247/1000000, piece := refinementPiece51 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece51, MacroPiece.box]

theorem segments_left_2_segment_4_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19039247/1000000, hi := 2381859/125000, piece := refinementPiece52 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece52, MacroPiece.box]

theorem segments_left_2_segment_5_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 2381859/125000, hi := 19070497/1000000, piece := refinementPiece53 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece53, MacroPiece.box]

theorem segments_left_2_segment_6_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19070497/1000000, hi := 9543061/500000, piece := refinementPiece54 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece54, MacroPiece.box]

theorem segments_left_2_segment_7_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9543061/500000, hi := 19101747/1000000, piece := refinementPiece55 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]

theorem segments_left_2_segment_8_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]

theorem segments_left_2_segment_9_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]

theorem segments_left_2_segment_10_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]

theorem segments_left_2_segment_11_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]

theorem segments_left_2_segment_12_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]

theorem segments_left_2_segment_13_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]

theorem segments_left_2_segment_14_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]

theorem segments_left_2_segment_15_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]

theorem segments_left_2_segment_16_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]

theorem segments_left_2_segment_17_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]

theorem segments_left_2_segment_18_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]

theorem segments_left_2_segment_19_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]

theorem segments_left_2_segment_20_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]

theorem segments_left_2_segment_21_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]

theorem segments_left_2_segment_22_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19320497/1000000, hi := 2475/128, piece := refinementPiece70 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]

theorem segments_left_2_accepted : sourcePiecewiseCheck (1215/64) (2475/128) (1755263779336959657910023102330969/7812500000000000000000000000000000000000) segments_left_2 = true := by
  have hlen : decide (0 < segments_left_2.length) = true := by norm_num [segments_left_2]
  have hcover : sourceCoverFrom (1215/64) (2475/128) segments_left_2 = true := by
    norm_num [sourceCoverFrom, segments_left_2]
  have hall : segments_left_2.all (sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000)) = true := by
    simp only [segments_left_2, List.all_cons, List.all_nil, segments_left_2_segment_0_checked, segments_left_2_segment_1_checked, segments_left_2_segment_2_checked, segments_left_2_segment_3_checked, segments_left_2_segment_4_checked, segments_left_2_segment_5_checked, segments_left_2_segment_6_checked, segments_left_2_segment_7_checked, segments_left_2_segment_8_checked, segments_left_2_segment_9_checked, segments_left_2_segment_10_checked, segments_left_2_segment_11_checked, segments_left_2_segment_12_checked, segments_left_2_segment_13_checked, segments_left_2_segment_14_checked, segments_left_2_segment_15_checked, segments_left_2_segment_16_checked, segments_left_2_segment_17_checked, segments_left_2_segment_18_checked, segments_left_2_segment_19_checked, segments_left_2_segment_20_checked, segments_left_2_segment_21_checked, segments_left_2_segment_22_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_2_pieces_checked : ∀ s ∈ segments_left_2, s.piece.check = true := by
  intro s hs
  simp only [segments_left_2, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece48_check
  · cases h; exact refinementPiece49_check
  · cases h; exact refinementPiece50_check
  · cases h; exact refinementPiece51_check
  · cases h; exact refinementPiece52_check
  · cases h; exact refinementPiece53_check
  · cases h; exact refinementPiece54_check
  · cases h; exact refinementPiece55_check
  · cases h; exact refinementPiece56_check
  · cases h; exact refinementPiece57_check
  · cases h; exact refinementPiece58_check
  · cases h; exact refinementPiece59_check
  · cases h; exact refinementPiece60_check
  · cases h; exact refinementPiece61_check
  · cases h; exact refinementPiece62_check
  · cases h; exact refinementPiece63_check
  · cases h; exact refinementPiece64_check
  · cases h; exact refinementPiece65_check
  · cases h; exact refinementPiece66_check
  · cases h; exact refinementPiece67_check
  · cases h; exact refinementPiece68_check
  · cases h; exact refinementPiece69_check
  · cases h; exact refinementPiece70_check

def segments_left_3 : List SourceSegment := [
  { lo := 3255/128, hi := 5086319/200000, piece := refinementPiece84 },
  { lo := 5086319/200000, hi := 1272361/50000, piece := refinementPiece85 },
  { lo := 1272361/50000, hi := 5092569/200000, piece := refinementPiece86 },
  { lo := 5092569/200000, hi := 2547847/100000, piece := refinementPiece87 },
  { lo := 2547847/100000, hi := 5098819/200000, piece := refinementPiece88 },
  { lo := 5098819/200000, hi := 637743/25000, piece := refinementPiece89 },
  { lo := 637743/25000, hi := 5105069/200000, piece := refinementPiece90 },
  { lo := 5105069/200000, hi := 2554097/100000, piece := refinementPiece91 },
  { lo := 2554097/100000, hi := 5111319/200000, piece := refinementPiece92 },
  { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 },
  { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 },
  { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 },
  { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 },
  { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 },
  { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 },
  { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 },
  { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 },
  { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 },
  { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 },
  { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 },
  { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 },
  { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 },
  { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 },
  { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 },
  { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 },
  { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 },
  { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 },
  { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 },
  { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 },
  { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 },
  { lo := 323559/12500, hi := 3315/128, piece := refinementPiece114 }
]
theorem segments_left_3_segment_0_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 3255/128, hi := 5086319/200000, piece := refinementPiece84 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece84, MacroPiece.box]

theorem segments_left_3_segment_1_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5086319/200000, hi := 1272361/50000, piece := refinementPiece85 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece85, MacroPiece.box]

theorem segments_left_3_segment_2_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1272361/50000, hi := 5092569/200000, piece := refinementPiece86 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece86, MacroPiece.box]

theorem segments_left_3_segment_3_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5092569/200000, hi := 2547847/100000, piece := refinementPiece87 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece87, MacroPiece.box]

theorem segments_left_3_segment_4_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2547847/100000, hi := 5098819/200000, piece := refinementPiece88 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece88, MacroPiece.box]

theorem segments_left_3_segment_5_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5098819/200000, hi := 637743/25000, piece := refinementPiece89 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece89, MacroPiece.box]

theorem segments_left_3_segment_6_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 637743/25000, hi := 5105069/200000, piece := refinementPiece90 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece90, MacroPiece.box]

theorem segments_left_3_segment_7_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5105069/200000, hi := 2554097/100000, piece := refinementPiece91 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece91, MacroPiece.box]

theorem segments_left_3_segment_8_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2554097/100000, hi := 5111319/200000, piece := refinementPiece92 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece92, MacroPiece.box]

theorem segments_left_3_segment_9_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece93, MacroPiece.box]

theorem segments_left_3_segment_10_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece94, MacroPiece.box]

theorem segments_left_3_segment_11_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece95, MacroPiece.box]

theorem segments_left_3_segment_12_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_left_3_segment_13_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_left_3_segment_14_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece98, MacroPiece.box]

theorem segments_left_3_segment_15_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece99, MacroPiece.box]

theorem segments_left_3_segment_16_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece100, MacroPiece.box]

theorem segments_left_3_segment_17_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece101, MacroPiece.box]

theorem segments_left_3_segment_18_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece102, MacroPiece.box]

theorem segments_left_3_segment_19_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece103, MacroPiece.box]

theorem segments_left_3_segment_20_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece104, MacroPiece.box]

theorem segments_left_3_segment_21_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece105, MacroPiece.box]

theorem segments_left_3_segment_22_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece106, MacroPiece.box]

theorem segments_left_3_segment_23_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece107, MacroPiece.box]

theorem segments_left_3_segment_24_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece108, MacroPiece.box]

theorem segments_left_3_segment_25_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece109, MacroPiece.box]

theorem segments_left_3_segment_26_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece110, MacroPiece.box]

theorem segments_left_3_segment_27_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece111, MacroPiece.box]

theorem segments_left_3_segment_28_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece112, MacroPiece.box]

theorem segments_left_3_segment_29_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece113, MacroPiece.box]

theorem segments_left_3_segment_30_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 323559/12500, hi := 3315/128, piece := refinementPiece114 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece114, MacroPiece.box]

theorem segments_left_3_accepted : sourcePiecewiseCheck (3255/128) (3315/128) (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) segments_left_3 = true := by
  have hlen : decide (0 < segments_left_3.length) = true := by norm_num [segments_left_3]
  have hcover : sourceCoverFrom (3255/128) (3315/128) segments_left_3 = true := by
    norm_num [sourceCoverFrom, segments_left_3]
  have hall : segments_left_3.all (sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000)) = true := by
    simp only [segments_left_3, List.all_cons, List.all_nil, segments_left_3_segment_0_checked, segments_left_3_segment_1_checked, segments_left_3_segment_2_checked, segments_left_3_segment_3_checked, segments_left_3_segment_4_checked, segments_left_3_segment_5_checked, segments_left_3_segment_6_checked, segments_left_3_segment_7_checked, segments_left_3_segment_8_checked, segments_left_3_segment_9_checked, segments_left_3_segment_10_checked, segments_left_3_segment_11_checked, segments_left_3_segment_12_checked, segments_left_3_segment_13_checked, segments_left_3_segment_14_checked, segments_left_3_segment_15_checked, segments_left_3_segment_16_checked, segments_left_3_segment_17_checked, segments_left_3_segment_18_checked, segments_left_3_segment_19_checked, segments_left_3_segment_20_checked, segments_left_3_segment_21_checked, segments_left_3_segment_22_checked, segments_left_3_segment_23_checked, segments_left_3_segment_24_checked, segments_left_3_segment_25_checked, segments_left_3_segment_26_checked, segments_left_3_segment_27_checked, segments_left_3_segment_28_checked, segments_left_3_segment_29_checked, segments_left_3_segment_30_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_3_pieces_checked : ∀ s ∈ segments_left_3, s.piece.check = true := by
  intro s hs
  simp only [segments_left_3, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece84_check
  · cases h; exact refinementPiece85_check
  · cases h; exact refinementPiece86_check
  · cases h; exact refinementPiece87_check
  · cases h; exact refinementPiece88_check
  · cases h; exact refinementPiece89_check
  · cases h; exact refinementPiece90_check
  · cases h; exact refinementPiece91_check
  · cases h; exact refinementPiece92_check
  · cases h; exact refinementPiece93_check
  · cases h; exact refinementPiece94_check
  · cases h; exact refinementPiece95_check
  · cases h; exact macroPiece24_check
  · cases h; exact macroPiece24_check
  · cases h; exact refinementPiece98_check
  · cases h; exact refinementPiece99_check
  · cases h; exact refinementPiece100_check
  · cases h; exact refinementPiece101_check
  · cases h; exact refinementPiece102_check
  · cases h; exact refinementPiece103_check
  · cases h; exact refinementPiece104_check
  · cases h; exact refinementPiece105_check
  · cases h; exact refinementPiece106_check
  · cases h; exact refinementPiece107_check
  · cases h; exact refinementPiece108_check
  · cases h; exact refinementPiece109_check
  · cases h; exact refinementPiece110_check
  · cases h; exact refinementPiece111_check
  · cases h; exact refinementPiece112_check
  · cases h; exact refinementPiece113_check
  · cases h; exact refinementPiece114_check

def segments_left_4 : List SourceSegment := [
  { lo := 4065/128, hi := 1587913/50000, piece := refinementPiece160 },
  { lo := 1587913/50000, hi := 6354777/200000, piece := refinementPiece161 },
  { lo := 6354777/200000, hi := 3178951/100000, piece := refinementPiece162 },
  { lo := 3178951/100000, hi := 6361027/200000, piece := refinementPiece163 },
  { lo := 6361027/200000, hi := 795519/25000, piece := refinementPiece164 },
  { lo := 795519/25000, hi := 6367277/200000, piece := refinementPiece165 },
  { lo := 6367277/200000, hi := 3185201/100000, piece := refinementPiece166 },
  { lo := 3185201/100000, hi := 6373527/200000, piece := refinementPiece167 },
  { lo := 6373527/200000, hi := 6448527/200000, piece := macroPiece30 },
  { lo := 6448527/200000, hi := 4155/128, piece := macroPiece31 }
]
theorem segments_left_4_segment_0_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 4065/128, hi := 1587913/50000, piece := refinementPiece160 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece160, MacroPiece.box]

theorem segments_left_4_segment_1_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 1587913/50000, hi := 6354777/200000, piece := refinementPiece161 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece161, MacroPiece.box]

theorem segments_left_4_segment_2_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 6354777/200000, hi := 3178951/100000, piece := refinementPiece162 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece162, MacroPiece.box]

theorem segments_left_4_segment_3_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 3178951/100000, hi := 6361027/200000, piece := refinementPiece163 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece163, MacroPiece.box]

theorem segments_left_4_segment_4_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 6361027/200000, hi := 795519/25000, piece := refinementPiece164 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece164, MacroPiece.box]

theorem segments_left_4_segment_5_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 795519/25000, hi := 6367277/200000, piece := refinementPiece165 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece165, MacroPiece.box]

theorem segments_left_4_segment_6_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 6367277/200000, hi := 3185201/100000, piece := refinementPiece166 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece166, MacroPiece.box]

theorem segments_left_4_segment_7_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 3185201/100000, hi := 6373527/200000, piece := refinementPiece167 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece167, MacroPiece.box]

theorem segments_left_4_segment_8_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 6373527/200000, hi := 6448527/200000, piece := macroPiece30 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece30, MacroPiece.box]

theorem segments_left_4_segment_9_checked : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) { lo := 6448527/200000, hi := 4155/128, piece := macroPiece31 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece31, MacroPiece.box]

theorem segments_left_4_accepted : sourcePiecewiseCheck (4065/128) (4155/128) (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) segments_left_4 = true := by
  have hlen : decide (0 < segments_left_4.length) = true := by norm_num [segments_left_4]
  have hcover : sourceCoverFrom (4065/128) (4155/128) segments_left_4 = true := by
    norm_num [sourceCoverFrom, segments_left_4]
  have hall : segments_left_4.all (sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000)) = true := by
    simp only [segments_left_4, List.all_cons, List.all_nil, segments_left_4_segment_0_checked, segments_left_4_segment_1_checked, segments_left_4_segment_2_checked, segments_left_4_segment_3_checked, segments_left_4_segment_4_checked, segments_left_4_segment_5_checked, segments_left_4_segment_6_checked, segments_left_4_segment_7_checked, segments_left_4_segment_8_checked, segments_left_4_segment_9_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_4_pieces_checked : ∀ s ∈ segments_left_4, s.piece.check = true := by
  intro s hs
  simp only [segments_left_4, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece160_check
  · cases h; exact refinementPiece161_check
  · cases h; exact refinementPiece162_check
  · cases h; exact refinementPiece163_check
  · cases h; exact refinementPiece164_check
  · cases h; exact refinementPiece165_check
  · cases h; exact refinementPiece166_check
  · cases h; exact refinementPiece167_check
  · cases h; exact macroPiece30_check
  · cases h; exact macroPiece31_check

def segments_left_5 : List SourceSegment := [
  { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 },
  { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 },
  { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 },
  { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 },
  { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 },
  { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 },
  { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 },
  { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 }
]
theorem segments_left_5_segment_0_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_left_5_segment_1_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]

theorem segments_left_5_segment_2_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]

theorem segments_left_5_segment_3_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]

theorem segments_left_5_segment_4_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]

theorem segments_left_5_segment_5_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]

theorem segments_left_5_segment_6_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]

theorem segments_left_5_segment_7_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]

theorem segments_left_5_accepted : sourcePiecewiseCheck (825/128) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments_left_5 = true := by
  have hlen : decide (0 < segments_left_5.length) = true := by norm_num [segments_left_5]
  have hcover : sourceCoverFrom (825/128) (105/16) segments_left_5 = true := by
    norm_num [sourceCoverFrom, segments_left_5]
  have hall : segments_left_5.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments_left_5, List.all_cons, List.all_nil, segments_left_5_segment_0_checked, segments_left_5_segment_1_checked, segments_left_5_segment_2_checked, segments_left_5_segment_3_checked, segments_left_5_segment_4_checked, segments_left_5_segment_5_checked, segments_left_5_segment_6_checked, segments_left_5_segment_7_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_5_pieces_checked : ∀ s ∈ segments_left_5, s.piece.check = true := by
  intro s hs
  simp only [segments_left_5, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece11_check
  · cases h; exact refinementPiece12_check
  · cases h; exact refinementPiece13_check
  · cases h; exact refinementPiece14_check
  · cases h; exact refinementPiece15_check
  · cases h; exact refinementPiece16_check
  · cases h; exact refinementPiece17_check
  · cases h; exact refinementPiece18_check

def segments_left_7 : List SourceSegment := [
  { lo := 2445/128, hi := 19101747/1000000, piece := refinementPiece55 },
  { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 },
  { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 },
  { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 },
  { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 },
  { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 },
  { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 },
  { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 },
  { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 },
  { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 },
  { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 },
  { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 },
  { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 },
  { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 },
  { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 },
  { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 },
  { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 },
  { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 }
]
theorem segments_left_7_segment_0_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 2445/128, hi := 19101747/1000000, piece := refinementPiece55 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]

theorem segments_left_7_segment_1_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]

theorem segments_left_7_segment_2_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]

theorem segments_left_7_segment_3_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]

theorem segments_left_7_segment_4_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]

theorem segments_left_7_segment_5_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]

theorem segments_left_7_segment_6_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]

theorem segments_left_7_segment_7_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]

theorem segments_left_7_segment_8_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]

theorem segments_left_7_segment_9_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]

theorem segments_left_7_segment_10_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]

theorem segments_left_7_segment_11_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]

theorem segments_left_7_segment_12_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]

theorem segments_left_7_segment_13_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]

theorem segments_left_7_segment_14_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]

theorem segments_left_7_segment_15_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]

theorem segments_left_7_segment_16_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece71, MacroPiece.box]

theorem segments_left_7_segment_17_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece18, MacroPiece.box]

theorem segments_left_7_accepted : sourcePiecewiseCheck (2445/128) (1245/64) (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) segments_left_7 = true := by
  have hlen : decide (0 < segments_left_7.length) = true := by norm_num [segments_left_7]
  have hcover : sourceCoverFrom (2445/128) (1245/64) segments_left_7 = true := by
    norm_num [sourceCoverFrom, segments_left_7]
  have hall : segments_left_7.all (sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000)) = true := by
    simp only [segments_left_7, List.all_cons, List.all_nil, segments_left_7_segment_0_checked, segments_left_7_segment_1_checked, segments_left_7_segment_2_checked, segments_left_7_segment_3_checked, segments_left_7_segment_4_checked, segments_left_7_segment_5_checked, segments_left_7_segment_6_checked, segments_left_7_segment_7_checked, segments_left_7_segment_8_checked, segments_left_7_segment_9_checked, segments_left_7_segment_10_checked, segments_left_7_segment_11_checked, segments_left_7_segment_12_checked, segments_left_7_segment_13_checked, segments_left_7_segment_14_checked, segments_left_7_segment_15_checked, segments_left_7_segment_16_checked, segments_left_7_segment_17_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_7_pieces_checked : ∀ s ∈ segments_left_7, s.piece.check = true := by
  intro s hs
  simp only [segments_left_7, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece55_check
  · cases h; exact refinementPiece56_check
  · cases h; exact refinementPiece57_check
  · cases h; exact refinementPiece58_check
  · cases h; exact refinementPiece59_check
  · cases h; exact refinementPiece60_check
  · cases h; exact refinementPiece61_check
  · cases h; exact refinementPiece62_check
  · cases h; exact refinementPiece63_check
  · cases h; exact refinementPiece64_check
  · cases h; exact refinementPiece65_check
  · cases h; exact refinementPiece66_check
  · cases h; exact refinementPiece67_check
  · cases h; exact refinementPiece68_check
  · cases h; exact refinementPiece69_check
  · cases h; exact refinementPiece70_check
  · cases h; exact refinementPiece71_check
  · cases h; exact macroPiece18_check

def segments_left_8 : List SourceSegment := [
  { lo := 3255/128, hi := 5086319/200000, piece := refinementPiece84 },
  { lo := 5086319/200000, hi := 1272361/50000, piece := refinementPiece85 },
  { lo := 1272361/50000, hi := 5092569/200000, piece := refinementPiece86 },
  { lo := 5092569/200000, hi := 2547847/100000, piece := refinementPiece87 },
  { lo := 2547847/100000, hi := 5098819/200000, piece := refinementPiece88 },
  { lo := 5098819/200000, hi := 637743/25000, piece := refinementPiece89 },
  { lo := 637743/25000, hi := 5105069/200000, piece := refinementPiece90 },
  { lo := 5105069/200000, hi := 2554097/100000, piece := refinementPiece91 },
  { lo := 2554097/100000, hi := 5111319/200000, piece := refinementPiece92 },
  { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 },
  { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 },
  { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 },
  { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 },
  { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 },
  { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 },
  { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 },
  { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 },
  { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 },
  { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 },
  { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 },
  { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 },
  { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 },
  { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 },
  { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 },
  { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 },
  { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 },
  { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 },
  { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 },
  { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 },
  { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 },
  { lo := 323559/12500, hi := 5180069/200000, piece := refinementPiece114 },
  { lo := 5180069/200000, hi := 2591597/100000, piece := refinementPiece115 },
  { lo := 2591597/100000, hi := 5186319/200000, piece := refinementPiece116 },
  { lo := 5186319/200000, hi := 1297361/50000, piece := refinementPiece117 },
  { lo := 1297361/50000, hi := 5192569/200000, piece := refinementPiece118 },
  { lo := 5192569/200000, hi := 2597847/100000, piece := refinementPiece119 },
  { lo := 2597847/100000, hi := 1665/64, piece := macroPiece25 }
]
theorem segments_left_8_segment_0_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 3255/128, hi := 5086319/200000, piece := refinementPiece84 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece84, MacroPiece.box]

theorem segments_left_8_segment_1_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5086319/200000, hi := 1272361/50000, piece := refinementPiece85 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece85, MacroPiece.box]

theorem segments_left_8_segment_2_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1272361/50000, hi := 5092569/200000, piece := refinementPiece86 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece86, MacroPiece.box]

theorem segments_left_8_segment_3_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5092569/200000, hi := 2547847/100000, piece := refinementPiece87 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece87, MacroPiece.box]

theorem segments_left_8_segment_4_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2547847/100000, hi := 5098819/200000, piece := refinementPiece88 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece88, MacroPiece.box]

theorem segments_left_8_segment_5_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5098819/200000, hi := 637743/25000, piece := refinementPiece89 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece89, MacroPiece.box]

theorem segments_left_8_segment_6_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 637743/25000, hi := 5105069/200000, piece := refinementPiece90 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece90, MacroPiece.box]

theorem segments_left_8_segment_7_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5105069/200000, hi := 2554097/100000, piece := refinementPiece91 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece91, MacroPiece.box]

theorem segments_left_8_segment_8_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2554097/100000, hi := 5111319/200000, piece := refinementPiece92 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece92, MacroPiece.box]

theorem segments_left_8_segment_9_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece93, MacroPiece.box]

theorem segments_left_8_segment_10_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece94, MacroPiece.box]

theorem segments_left_8_segment_11_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece95, MacroPiece.box]

theorem segments_left_8_segment_12_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_left_8_segment_13_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_left_8_segment_14_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece98, MacroPiece.box]

theorem segments_left_8_segment_15_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece99, MacroPiece.box]

theorem segments_left_8_segment_16_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece100, MacroPiece.box]

theorem segments_left_8_segment_17_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece101, MacroPiece.box]

theorem segments_left_8_segment_18_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece102, MacroPiece.box]

theorem segments_left_8_segment_19_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece103, MacroPiece.box]

theorem segments_left_8_segment_20_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece104, MacroPiece.box]

theorem segments_left_8_segment_21_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece105, MacroPiece.box]

theorem segments_left_8_segment_22_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece106, MacroPiece.box]

theorem segments_left_8_segment_23_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece107, MacroPiece.box]

theorem segments_left_8_segment_24_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece108, MacroPiece.box]

theorem segments_left_8_segment_25_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece109, MacroPiece.box]

theorem segments_left_8_segment_26_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece110, MacroPiece.box]

theorem segments_left_8_segment_27_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece111, MacroPiece.box]

theorem segments_left_8_segment_28_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece112, MacroPiece.box]

theorem segments_left_8_segment_29_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece113, MacroPiece.box]

theorem segments_left_8_segment_30_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 323559/12500, hi := 5180069/200000, piece := refinementPiece114 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece114, MacroPiece.box]

theorem segments_left_8_segment_31_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5180069/200000, hi := 2591597/100000, piece := refinementPiece115 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece115, MacroPiece.box]

theorem segments_left_8_segment_32_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2591597/100000, hi := 5186319/200000, piece := refinementPiece116 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece116, MacroPiece.box]

theorem segments_left_8_segment_33_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5186319/200000, hi := 1297361/50000, piece := refinementPiece117 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece117, MacroPiece.box]

theorem segments_left_8_segment_34_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1297361/50000, hi := 5192569/200000, piece := refinementPiece118 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece118, MacroPiece.box]

theorem segments_left_8_segment_35_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5192569/200000, hi := 2597847/100000, piece := refinementPiece119 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece119, MacroPiece.box]

theorem segments_left_8_segment_36_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2597847/100000, hi := 1665/64, piece := macroPiece25 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece25, MacroPiece.box]

theorem segments_left_8_accepted : sourcePiecewiseCheck (3255/128) (1665/64) (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) segments_left_8 = true := by
  have hlen : decide (0 < segments_left_8.length) = true := by norm_num [segments_left_8]
  have hcover : sourceCoverFrom (3255/128) (1665/64) segments_left_8 = true := by
    norm_num [sourceCoverFrom, segments_left_8]
  have hall : segments_left_8.all (sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000)) = true := by
    simp only [segments_left_8, List.all_cons, List.all_nil, segments_left_8_segment_0_checked, segments_left_8_segment_1_checked, segments_left_8_segment_2_checked, segments_left_8_segment_3_checked, segments_left_8_segment_4_checked, segments_left_8_segment_5_checked, segments_left_8_segment_6_checked, segments_left_8_segment_7_checked, segments_left_8_segment_8_checked, segments_left_8_segment_9_checked, segments_left_8_segment_10_checked, segments_left_8_segment_11_checked, segments_left_8_segment_12_checked, segments_left_8_segment_13_checked, segments_left_8_segment_14_checked, segments_left_8_segment_15_checked, segments_left_8_segment_16_checked, segments_left_8_segment_17_checked, segments_left_8_segment_18_checked, segments_left_8_segment_19_checked, segments_left_8_segment_20_checked, segments_left_8_segment_21_checked, segments_left_8_segment_22_checked, segments_left_8_segment_23_checked, segments_left_8_segment_24_checked, segments_left_8_segment_25_checked, segments_left_8_segment_26_checked, segments_left_8_segment_27_checked, segments_left_8_segment_28_checked, segments_left_8_segment_29_checked, segments_left_8_segment_30_checked, segments_left_8_segment_31_checked, segments_left_8_segment_32_checked, segments_left_8_segment_33_checked, segments_left_8_segment_34_checked, segments_left_8_segment_35_checked, segments_left_8_segment_36_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_8_pieces_checked : ∀ s ∈ segments_left_8, s.piece.check = true := by
  intro s hs
  simp only [segments_left_8, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece84_check
  · cases h; exact refinementPiece85_check
  · cases h; exact refinementPiece86_check
  · cases h; exact refinementPiece87_check
  · cases h; exact refinementPiece88_check
  · cases h; exact refinementPiece89_check
  · cases h; exact refinementPiece90_check
  · cases h; exact refinementPiece91_check
  · cases h; exact refinementPiece92_check
  · cases h; exact refinementPiece93_check
  · cases h; exact refinementPiece94_check
  · cases h; exact refinementPiece95_check
  · cases h; exact macroPiece24_check
  · cases h; exact macroPiece24_check
  · cases h; exact refinementPiece98_check
  · cases h; exact refinementPiece99_check
  · cases h; exact refinementPiece100_check
  · cases h; exact refinementPiece101_check
  · cases h; exact refinementPiece102_check
  · cases h; exact refinementPiece103_check
  · cases h; exact refinementPiece104_check
  · cases h; exact refinementPiece105_check
  · cases h; exact refinementPiece106_check
  · cases h; exact refinementPiece107_check
  · cases h; exact refinementPiece108_check
  · cases h; exact refinementPiece109_check
  · cases h; exact refinementPiece110_check
  · cases h; exact refinementPiece111_check
  · cases h; exact refinementPiece112_check
  · cases h; exact refinementPiece113_check
  · cases h; exact refinementPiece114_check
  · cases h; exact refinementPiece115_check
  · cases h; exact refinementPiece116_check
  · cases h; exact refinementPiece117_check
  · cases h; exact refinementPiece118_check
  · cases h; exact refinementPiece119_check
  · cases h; exact macroPiece25_check

def segments_left_9 : List SourceSegment := [
  { lo := 795/128, hi := 250723/40000, piece := macroPiece2 },
  { lo := 250723/40000, hi := 62837/10000, piece := refinementPiece0 },
  { lo := 62837/10000, hi := 251973/40000, piece := refinementPiece1 },
  { lo := 251973/40000, hi := 126299/20000, piece := refinementPiece2 },
  { lo := 126299/20000, hi := 405/64, piece := refinementPiece3 }
]
theorem segments_left_9_segment_0_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 795/128, hi := 250723/40000, piece := macroPiece2 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece2, MacroPiece.box]

theorem segments_left_9_segment_1_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 250723/40000, hi := 62837/10000, piece := refinementPiece0 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece0, MacroPiece.box]

theorem segments_left_9_segment_2_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 62837/10000, hi := 251973/40000, piece := refinementPiece1 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece1, MacroPiece.box]

theorem segments_left_9_segment_3_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 251973/40000, hi := 126299/20000, piece := refinementPiece2 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece2, MacroPiece.box]

theorem segments_left_9_segment_4_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 126299/20000, hi := 405/64, piece := refinementPiece3 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]

theorem segments_left_9_accepted : sourcePiecewiseCheck (795/128) (405/64) (21287960894909617826490440080249/5000000000000000000000000000000000) segments_left_9 = true := by
  have hlen : decide (0 < segments_left_9.length) = true := by norm_num [segments_left_9]
  have hcover : sourceCoverFrom (795/128) (405/64) segments_left_9 = true := by
    norm_num [sourceCoverFrom, segments_left_9]
  have hall : segments_left_9.all (sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000)) = true := by
    simp only [segments_left_9, List.all_cons, List.all_nil, segments_left_9_segment_0_checked, segments_left_9_segment_1_checked, segments_left_9_segment_2_checked, segments_left_9_segment_3_checked, segments_left_9_segment_4_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_9_pieces_checked : ∀ s ∈ segments_left_9, s.piece.check = true := by
  intro s hs
  simp only [segments_left_9, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h
  · cases h; exact macroPiece2_check
  · cases h; exact refinementPiece0_check
  · cases h; exact refinementPiece1_check
  · cases h; exact refinementPiece2_check
  · cases h; exact refinementPiece3_check

def segments_left_11 : List SourceSegment := [
  { lo := 1215/64, hi := 4748093/250000, piece := refinementPiece48 },
  { lo := 4748093/250000, hi := 19007997/1000000, piece := refinementPiece49 },
  { lo := 19007997/1000000, hi := 9511811/500000, piece := refinementPiece50 },
  { lo := 9511811/500000, hi := 19039247/1000000, piece := refinementPiece51 },
  { lo := 19039247/1000000, hi := 2381859/125000, piece := refinementPiece52 },
  { lo := 2381859/125000, hi := 19070497/1000000, piece := refinementPiece53 },
  { lo := 19070497/1000000, hi := 9543061/500000, piece := refinementPiece54 },
  { lo := 9543061/500000, hi := 19101747/1000000, piece := refinementPiece55 },
  { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 },
  { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 },
  { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 },
  { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 },
  { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 },
  { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 },
  { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 },
  { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 },
  { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 },
  { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 },
  { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 },
  { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 },
  { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 },
  { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 },
  { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 },
  { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 },
  { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 }
]
theorem segments_left_11_segment_0_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 1215/64, hi := 4748093/250000, piece := refinementPiece48 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece48, MacroPiece.box]

theorem segments_left_11_segment_1_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4748093/250000, hi := 19007997/1000000, piece := refinementPiece49 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece49, MacroPiece.box]

theorem segments_left_11_segment_2_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19007997/1000000, hi := 9511811/500000, piece := refinementPiece50 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece50, MacroPiece.box]

theorem segments_left_11_segment_3_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9511811/500000, hi := 19039247/1000000, piece := refinementPiece51 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece51, MacroPiece.box]

theorem segments_left_11_segment_4_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19039247/1000000, hi := 2381859/125000, piece := refinementPiece52 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece52, MacroPiece.box]

theorem segments_left_11_segment_5_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 2381859/125000, hi := 19070497/1000000, piece := refinementPiece53 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece53, MacroPiece.box]

theorem segments_left_11_segment_6_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19070497/1000000, hi := 9543061/500000, piece := refinementPiece54 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece54, MacroPiece.box]

theorem segments_left_11_segment_7_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9543061/500000, hi := 19101747/1000000, piece := refinementPiece55 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]

theorem segments_left_11_segment_8_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]

theorem segments_left_11_segment_9_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]

theorem segments_left_11_segment_10_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]

theorem segments_left_11_segment_11_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]

theorem segments_left_11_segment_12_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]

theorem segments_left_11_segment_13_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]

theorem segments_left_11_segment_14_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]

theorem segments_left_11_segment_15_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]

theorem segments_left_11_segment_16_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]

theorem segments_left_11_segment_17_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]

theorem segments_left_11_segment_18_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]

theorem segments_left_11_segment_19_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]

theorem segments_left_11_segment_20_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]

theorem segments_left_11_segment_21_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]

theorem segments_left_11_segment_22_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]

theorem segments_left_11_segment_23_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece71, MacroPiece.box]

theorem segments_left_11_segment_24_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece18, MacroPiece.box]

theorem segments_left_11_accepted : sourcePiecewiseCheck (1215/64) (1245/64) (1755263779336959657910023102330969/7812500000000000000000000000000000000000) segments_left_11 = true := by
  have hlen : decide (0 < segments_left_11.length) = true := by norm_num [segments_left_11]
  have hcover : sourceCoverFrom (1215/64) (1245/64) segments_left_11 = true := by
    norm_num [sourceCoverFrom, segments_left_11]
  have hall : segments_left_11.all (sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000)) = true := by
    simp only [segments_left_11, List.all_cons, List.all_nil, segments_left_11_segment_0_checked, segments_left_11_segment_1_checked, segments_left_11_segment_2_checked, segments_left_11_segment_3_checked, segments_left_11_segment_4_checked, segments_left_11_segment_5_checked, segments_left_11_segment_6_checked, segments_left_11_segment_7_checked, segments_left_11_segment_8_checked, segments_left_11_segment_9_checked, segments_left_11_segment_10_checked, segments_left_11_segment_11_checked, segments_left_11_segment_12_checked, segments_left_11_segment_13_checked, segments_left_11_segment_14_checked, segments_left_11_segment_15_checked, segments_left_11_segment_16_checked, segments_left_11_segment_17_checked, segments_left_11_segment_18_checked, segments_left_11_segment_19_checked, segments_left_11_segment_20_checked, segments_left_11_segment_21_checked, segments_left_11_segment_22_checked, segments_left_11_segment_23_checked, segments_left_11_segment_24_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_11_pieces_checked : ∀ s ∈ segments_left_11, s.piece.check = true := by
  intro s hs
  simp only [segments_left_11, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece48_check
  · cases h; exact refinementPiece49_check
  · cases h; exact refinementPiece50_check
  · cases h; exact refinementPiece51_check
  · cases h; exact refinementPiece52_check
  · cases h; exact refinementPiece53_check
  · cases h; exact refinementPiece54_check
  · cases h; exact refinementPiece55_check
  · cases h; exact refinementPiece56_check
  · cases h; exact refinementPiece57_check
  · cases h; exact refinementPiece58_check
  · cases h; exact refinementPiece59_check
  · cases h; exact refinementPiece60_check
  · cases h; exact refinementPiece61_check
  · cases h; exact refinementPiece62_check
  · cases h; exact refinementPiece63_check
  · cases h; exact refinementPiece64_check
  · cases h; exact refinementPiece65_check
  · cases h; exact refinementPiece66_check
  · cases h; exact refinementPiece67_check
  · cases h; exact refinementPiece68_check
  · cases h; exact refinementPiece69_check
  · cases h; exact refinementPiece70_check
  · cases h; exact refinementPiece71_check
  · cases h; exact macroPiece18_check

def segments_left_12 : List SourceSegment := [
  { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 },
  { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 },
  { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 },
  { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 },
  { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 },
  { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 },
  { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 },
  { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 }
]
theorem segments_left_12_segment_0_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_left_12_segment_1_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]

theorem segments_left_12_segment_2_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]

theorem segments_left_12_segment_3_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]

theorem segments_left_12_segment_4_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]

theorem segments_left_12_segment_5_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]

theorem segments_left_12_segment_6_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]

theorem segments_left_12_segment_7_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]

theorem segments_left_12_accepted : sourcePiecewiseCheck (825/128) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments_left_12 = true := by
  have hlen : decide (0 < segments_left_12.length) = true := by norm_num [segments_left_12]
  have hcover : sourceCoverFrom (825/128) (105/16) segments_left_12 = true := by
    norm_num [sourceCoverFrom, segments_left_12]
  have hall : segments_left_12.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments_left_12, List.all_cons, List.all_nil, segments_left_12_segment_0_checked, segments_left_12_segment_1_checked, segments_left_12_segment_2_checked, segments_left_12_segment_3_checked, segments_left_12_segment_4_checked, segments_left_12_segment_5_checked, segments_left_12_segment_6_checked, segments_left_12_segment_7_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_12_pieces_checked : ∀ s ∈ segments_left_12, s.piece.check = true := by
  intro s hs
  simp only [segments_left_12, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece11_check
  · cases h; exact refinementPiece12_check
  · cases h; exact refinementPiece13_check
  · cases h; exact refinementPiece14_check
  · cases h; exact refinementPiece15_check
  · cases h; exact refinementPiece16_check
  · cases h; exact refinementPiece17_check
  · cases h; exact refinementPiece18_check

def segments_left_14 : List SourceSegment := [
  { lo := 405/64, hi := 253223/40000, piece := refinementPiece3 },
  { lo := 253223/40000, hi := 31731/5000, piece := refinementPiece4 },
  { lo := 31731/5000, hi := 254473/40000, piece := refinementPiece5 },
  { lo := 254473/40000, hi := 127549/20000, piece := refinementPiece6 },
  { lo := 127549/20000, hi := 255723/40000, piece := refinementPiece7 },
  { lo := 255723/40000, hi := 64087/10000, piece := refinementPiece8 },
  { lo := 64087/10000, hi := 256973/40000, piece := refinementPiece9 },
  { lo := 256973/40000, hi := 128799/20000, piece := refinementPiece10 },
  { lo := 128799/20000, hi := 258223/40000, piece := refinementPiece11 },
  { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 },
  { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 },
  { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 },
  { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 },
  { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 },
  { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 },
  { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 }
]
theorem segments_left_14_segment_0_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 405/64, hi := 253223/40000, piece := refinementPiece3 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]

theorem segments_left_14_segment_1_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 253223/40000, hi := 31731/5000, piece := refinementPiece4 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece4, MacroPiece.box]

theorem segments_left_14_segment_2_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 31731/5000, hi := 254473/40000, piece := refinementPiece5 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece5, MacroPiece.box]

theorem segments_left_14_segment_3_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 254473/40000, hi := 127549/20000, piece := refinementPiece6 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece6, MacroPiece.box]

theorem segments_left_14_segment_4_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 127549/20000, hi := 255723/40000, piece := refinementPiece7 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece7, MacroPiece.box]

theorem segments_left_14_segment_5_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 255723/40000, hi := 64087/10000, piece := refinementPiece8 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece8, MacroPiece.box]

theorem segments_left_14_segment_6_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 64087/10000, hi := 256973/40000, piece := refinementPiece9 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece9, MacroPiece.box]

theorem segments_left_14_segment_7_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 256973/40000, hi := 128799/20000, piece := refinementPiece10 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece10, MacroPiece.box]

theorem segments_left_14_segment_8_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 128799/20000, hi := 258223/40000, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_left_14_segment_9_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]

theorem segments_left_14_segment_10_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]

theorem segments_left_14_segment_11_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]

theorem segments_left_14_segment_12_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]

theorem segments_left_14_segment_13_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]

theorem segments_left_14_segment_14_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]

theorem segments_left_14_segment_15_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]

theorem segments_left_14_accepted : sourcePiecewiseCheck (405/64) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments_left_14 = true := by
  have hlen : decide (0 < segments_left_14.length) = true := by norm_num [segments_left_14]
  have hcover : sourceCoverFrom (405/64) (105/16) segments_left_14 = true := by
    norm_num [sourceCoverFrom, segments_left_14]
  have hall : segments_left_14.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments_left_14, List.all_cons, List.all_nil, segments_left_14_segment_0_checked, segments_left_14_segment_1_checked, segments_left_14_segment_2_checked, segments_left_14_segment_3_checked, segments_left_14_segment_4_checked, segments_left_14_segment_5_checked, segments_left_14_segment_6_checked, segments_left_14_segment_7_checked, segments_left_14_segment_8_checked, segments_left_14_segment_9_checked, segments_left_14_segment_10_checked, segments_left_14_segment_11_checked, segments_left_14_segment_12_checked, segments_left_14_segment_13_checked, segments_left_14_segment_14_checked, segments_left_14_segment_15_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_left_14_pieces_checked : ∀ s ∈ segments_left_14, s.piece.check = true := by
  intro s hs
  simp only [segments_left_14, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece3_check
  · cases h; exact refinementPiece4_check
  · cases h; exact refinementPiece5_check
  · cases h; exact refinementPiece6_check
  · cases h; exact refinementPiece7_check
  · cases h; exact refinementPiece8_check
  · cases h; exact refinementPiece9_check
  · cases h; exact refinementPiece10_check
  · cases h; exact refinementPiece11_check
  · cases h; exact refinementPiece12_check
  · cases h; exact refinementPiece13_check
  · cases h; exact refinementPiece14_check
  · cases h; exact refinementPiece15_check
  · cases h; exact refinementPiece16_check
  · cases h; exact refinementPiece17_check
  · cases h; exact refinementPiece18_check

def segments_right_0 : List SourceSegment := [
  { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 },
  { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 },
  { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 },
  { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 },
  { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 },
  { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 },
  { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 },
  { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 }
]
theorem segments_right_0_segment_0_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_right_0_segment_1_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]

theorem segments_right_0_segment_2_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]

theorem segments_right_0_segment_3_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]

theorem segments_right_0_segment_4_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]

theorem segments_right_0_segment_5_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]

theorem segments_right_0_segment_6_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]

theorem segments_right_0_segment_7_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]

theorem segments_right_0_accepted : sourcePiecewiseCheck (825/128) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments_right_0 = true := by
  have hlen : decide (0 < segments_right_0.length) = true := by norm_num [segments_right_0]
  have hcover : sourceCoverFrom (825/128) (105/16) segments_right_0 = true := by
    norm_num [sourceCoverFrom, segments_right_0]
  have hall : segments_right_0.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments_right_0, List.all_cons, List.all_nil, segments_right_0_segment_0_checked, segments_right_0_segment_1_checked, segments_right_0_segment_2_checked, segments_right_0_segment_3_checked, segments_right_0_segment_4_checked, segments_right_0_segment_5_checked, segments_right_0_segment_6_checked, segments_right_0_segment_7_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_0_pieces_checked : ∀ s ∈ segments_right_0, s.piece.check = true := by
  intro s hs
  simp only [segments_right_0, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece11_check
  · cases h; exact refinementPiece12_check
  · cases h; exact refinementPiece13_check
  · cases h; exact refinementPiece14_check
  · cases h; exact refinementPiece15_check
  · cases h; exact refinementPiece16_check
  · cases h; exact refinementPiece17_check
  · cases h; exact refinementPiece18_check

def segments_right_2 : List SourceSegment := [
  { lo := 2445/128, hi := 19101747/1000000, piece := refinementPiece55 },
  { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 },
  { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 },
  { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 },
  { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 },
  { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 },
  { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 },
  { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 },
  { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 },
  { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 },
  { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 },
  { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 },
  { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 },
  { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 },
  { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 },
  { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 },
  { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 },
  { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 }
]
theorem segments_right_2_segment_0_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 2445/128, hi := 19101747/1000000, piece := refinementPiece55 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]

theorem segments_right_2_segment_1_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]

theorem segments_right_2_segment_2_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]

theorem segments_right_2_segment_3_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]

theorem segments_right_2_segment_4_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]

theorem segments_right_2_segment_5_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]

theorem segments_right_2_segment_6_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]

theorem segments_right_2_segment_7_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]

theorem segments_right_2_segment_8_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]

theorem segments_right_2_segment_9_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]

theorem segments_right_2_segment_10_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]

theorem segments_right_2_segment_11_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]

theorem segments_right_2_segment_12_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]

theorem segments_right_2_segment_13_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]

theorem segments_right_2_segment_14_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]

theorem segments_right_2_segment_15_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]

theorem segments_right_2_segment_16_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece71, MacroPiece.box]

theorem segments_right_2_segment_17_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece18, MacroPiece.box]

theorem segments_right_2_accepted : sourcePiecewiseCheck (2445/128) (1245/64) (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) segments_right_2 = true := by
  have hlen : decide (0 < segments_right_2.length) = true := by norm_num [segments_right_2]
  have hcover : sourceCoverFrom (2445/128) (1245/64) segments_right_2 = true := by
    norm_num [sourceCoverFrom, segments_right_2]
  have hall : segments_right_2.all (sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000)) = true := by
    simp only [segments_right_2, List.all_cons, List.all_nil, segments_right_2_segment_0_checked, segments_right_2_segment_1_checked, segments_right_2_segment_2_checked, segments_right_2_segment_3_checked, segments_right_2_segment_4_checked, segments_right_2_segment_5_checked, segments_right_2_segment_6_checked, segments_right_2_segment_7_checked, segments_right_2_segment_8_checked, segments_right_2_segment_9_checked, segments_right_2_segment_10_checked, segments_right_2_segment_11_checked, segments_right_2_segment_12_checked, segments_right_2_segment_13_checked, segments_right_2_segment_14_checked, segments_right_2_segment_15_checked, segments_right_2_segment_16_checked, segments_right_2_segment_17_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_2_pieces_checked : ∀ s ∈ segments_right_2, s.piece.check = true := by
  intro s hs
  simp only [segments_right_2, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece55_check
  · cases h; exact refinementPiece56_check
  · cases h; exact refinementPiece57_check
  · cases h; exact refinementPiece58_check
  · cases h; exact refinementPiece59_check
  · cases h; exact refinementPiece60_check
  · cases h; exact refinementPiece61_check
  · cases h; exact refinementPiece62_check
  · cases h; exact refinementPiece63_check
  · cases h; exact refinementPiece64_check
  · cases h; exact refinementPiece65_check
  · cases h; exact refinementPiece66_check
  · cases h; exact refinementPiece67_check
  · cases h; exact refinementPiece68_check
  · cases h; exact refinementPiece69_check
  · cases h; exact refinementPiece70_check
  · cases h; exact refinementPiece71_check
  · cases h; exact macroPiece18_check

def segments_right_3 : List SourceSegment := [
  { lo := 1635/64, hi := 5111319/200000, piece := refinementPiece92 },
  { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 },
  { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 },
  { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 },
  { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 },
  { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 },
  { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 },
  { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 },
  { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 },
  { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 },
  { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 },
  { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 },
  { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 },
  { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 },
  { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 },
  { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 },
  { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 },
  { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 },
  { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 },
  { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 },
  { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 },
  { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 },
  { lo := 323559/12500, hi := 5180069/200000, piece := refinementPiece114 },
  { lo := 5180069/200000, hi := 2591597/100000, piece := refinementPiece115 },
  { lo := 2591597/100000, hi := 5186319/200000, piece := refinementPiece116 },
  { lo := 5186319/200000, hi := 1297361/50000, piece := refinementPiece117 },
  { lo := 1297361/50000, hi := 5192569/200000, piece := refinementPiece118 },
  { lo := 5192569/200000, hi := 2597847/100000, piece := refinementPiece119 },
  { lo := 2597847/100000, hi := 1665/64, piece := macroPiece25 }
]
theorem segments_right_3_segment_0_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 1635/64, hi := 5111319/200000, piece := refinementPiece92 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece92, MacroPiece.box]

theorem segments_right_3_segment_1_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece93, MacroPiece.box]

theorem segments_right_3_segment_2_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece94, MacroPiece.box]

theorem segments_right_3_segment_3_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece95, MacroPiece.box]

theorem segments_right_3_segment_4_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_right_3_segment_5_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_right_3_segment_6_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece98, MacroPiece.box]

theorem segments_right_3_segment_7_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece99, MacroPiece.box]

theorem segments_right_3_segment_8_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece100, MacroPiece.box]

theorem segments_right_3_segment_9_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece101, MacroPiece.box]

theorem segments_right_3_segment_10_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece102, MacroPiece.box]

theorem segments_right_3_segment_11_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece103, MacroPiece.box]

theorem segments_right_3_segment_12_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece104, MacroPiece.box]

theorem segments_right_3_segment_13_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece105, MacroPiece.box]

theorem segments_right_3_segment_14_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece106, MacroPiece.box]

theorem segments_right_3_segment_15_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece107, MacroPiece.box]

theorem segments_right_3_segment_16_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece108, MacroPiece.box]

theorem segments_right_3_segment_17_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece109, MacroPiece.box]

theorem segments_right_3_segment_18_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece110, MacroPiece.box]

theorem segments_right_3_segment_19_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece111, MacroPiece.box]

theorem segments_right_3_segment_20_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece112, MacroPiece.box]

theorem segments_right_3_segment_21_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece113, MacroPiece.box]

theorem segments_right_3_segment_22_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 323559/12500, hi := 5180069/200000, piece := refinementPiece114 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece114, MacroPiece.box]

theorem segments_right_3_segment_23_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5180069/200000, hi := 2591597/100000, piece := refinementPiece115 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece115, MacroPiece.box]

theorem segments_right_3_segment_24_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 2591597/100000, hi := 5186319/200000, piece := refinementPiece116 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece116, MacroPiece.box]

theorem segments_right_3_segment_25_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5186319/200000, hi := 1297361/50000, piece := refinementPiece117 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece117, MacroPiece.box]

theorem segments_right_3_segment_26_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 1297361/50000, hi := 5192569/200000, piece := refinementPiece118 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece118, MacroPiece.box]

theorem segments_right_3_segment_27_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 5192569/200000, hi := 2597847/100000, piece := refinementPiece119 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece119, MacroPiece.box]

theorem segments_right_3_segment_28_checked : sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) { lo := 2597847/100000, hi := 1665/64, piece := macroPiece25 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece25, MacroPiece.box]

theorem segments_right_3_accepted : sourcePiecewiseCheck (1635/64) (1665/64) (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) segments_right_3 = true := by
  have hlen : decide (0 < segments_right_3.length) = true := by norm_num [segments_right_3]
  have hcover : sourceCoverFrom (1635/64) (1665/64) segments_right_3 = true := by
    norm_num [sourceCoverFrom, segments_right_3]
  have hall : segments_right_3.all (sourceSegmentCheck (1060756076606974029304872234228987649/5000000000000000000000000000000000000000)) = true := by
    simp only [segments_right_3, List.all_cons, List.all_nil, segments_right_3_segment_0_checked, segments_right_3_segment_1_checked, segments_right_3_segment_2_checked, segments_right_3_segment_3_checked, segments_right_3_segment_4_checked, segments_right_3_segment_5_checked, segments_right_3_segment_6_checked, segments_right_3_segment_7_checked, segments_right_3_segment_8_checked, segments_right_3_segment_9_checked, segments_right_3_segment_10_checked, segments_right_3_segment_11_checked, segments_right_3_segment_12_checked, segments_right_3_segment_13_checked, segments_right_3_segment_14_checked, segments_right_3_segment_15_checked, segments_right_3_segment_16_checked, segments_right_3_segment_17_checked, segments_right_3_segment_18_checked, segments_right_3_segment_19_checked, segments_right_3_segment_20_checked, segments_right_3_segment_21_checked, segments_right_3_segment_22_checked, segments_right_3_segment_23_checked, segments_right_3_segment_24_checked, segments_right_3_segment_25_checked, segments_right_3_segment_26_checked, segments_right_3_segment_27_checked, segments_right_3_segment_28_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_3_pieces_checked : ∀ s ∈ segments_right_3, s.piece.check = true := by
  intro s hs
  simp only [segments_right_3, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece92_check
  · cases h; exact refinementPiece93_check
  · cases h; exact refinementPiece94_check
  · cases h; exact refinementPiece95_check
  · cases h; exact macroPiece24_check
  · cases h; exact macroPiece24_check
  · cases h; exact refinementPiece98_check
  · cases h; exact refinementPiece99_check
  · cases h; exact refinementPiece100_check
  · cases h; exact refinementPiece101_check
  · cases h; exact refinementPiece102_check
  · cases h; exact refinementPiece103_check
  · cases h; exact refinementPiece104_check
  · cases h; exact refinementPiece105_check
  · cases h; exact refinementPiece106_check
  · cases h; exact refinementPiece107_check
  · cases h; exact refinementPiece108_check
  · cases h; exact refinementPiece109_check
  · cases h; exact refinementPiece110_check
  · cases h; exact refinementPiece111_check
  · cases h; exact refinementPiece112_check
  · cases h; exact refinementPiece113_check
  · cases h; exact refinementPiece114_check
  · cases h; exact refinementPiece115_check
  · cases h; exact refinementPiece116_check
  · cases h; exact refinementPiece117_check
  · cases h; exact refinementPiece118_check
  · cases h; exact refinementPiece119_check
  · cases h; exact macroPiece25_check

def segments_right_4 : List SourceSegment := [
  { lo := 255/8, hi := 6448527/200000, piece := macroPiece30 },
  { lo := 6448527/200000, hi := 2085/64, piece := macroPiece31 }
]
theorem segments_right_4_segment_0_checked : sourceSegmentCheck (245028537159250067459167806169/1250000000000000000000000000000000) { lo := 255/8, hi := 6448527/200000, piece := macroPiece30 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece30, MacroPiece.box]

theorem segments_right_4_segment_1_checked : sourceSegmentCheck (245028537159250067459167806169/1250000000000000000000000000000000) { lo := 6448527/200000, hi := 2085/64, piece := macroPiece31 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece31, MacroPiece.box]

theorem segments_right_4_accepted : sourcePiecewiseCheck (255/8) (2085/64) (245028537159250067459167806169/1250000000000000000000000000000000) segments_right_4 = true := by
  have hlen : decide (0 < segments_right_4.length) = true := by norm_num [segments_right_4]
  have hcover : sourceCoverFrom (255/8) (2085/64) segments_right_4 = true := by
    norm_num [sourceCoverFrom, segments_right_4]
  have hall : segments_right_4.all (sourceSegmentCheck (245028537159250067459167806169/1250000000000000000000000000000000)) = true := by
    simp only [segments_right_4, List.all_cons, List.all_nil, segments_right_4_segment_0_checked, segments_right_4_segment_1_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_4_pieces_checked : ∀ s ∈ segments_right_4, s.piece.check = true := by
  intro s hs
  simp only [segments_right_4, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h
  · cases h; exact macroPiece30_check
  · cases h; exact macroPiece31_check

def segments_right_5 : List SourceSegment := [
  { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 },
  { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 },
  { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 },
  { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 },
  { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 },
  { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 },
  { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 },
  { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 }
]
theorem segments_right_5_segment_0_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_right_5_segment_1_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]

theorem segments_right_5_segment_2_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]

theorem segments_right_5_segment_3_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]

theorem segments_right_5_segment_4_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]

theorem segments_right_5_segment_5_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]

theorem segments_right_5_segment_6_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]

theorem segments_right_5_segment_7_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]

theorem segments_right_5_accepted : sourcePiecewiseCheck (825/128) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments_right_5 = true := by
  have hlen : decide (0 < segments_right_5.length) = true := by norm_num [segments_right_5]
  have hcover : sourceCoverFrom (825/128) (105/16) segments_right_5 = true := by
    norm_num [sourceCoverFrom, segments_right_5]
  have hall : segments_right_5.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments_right_5, List.all_cons, List.all_nil, segments_right_5_segment_0_checked, segments_right_5_segment_1_checked, segments_right_5_segment_2_checked, segments_right_5_segment_3_checked, segments_right_5_segment_4_checked, segments_right_5_segment_5_checked, segments_right_5_segment_6_checked, segments_right_5_segment_7_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_5_pieces_checked : ∀ s ∈ segments_right_5, s.piece.check = true := by
  intro s hs
  simp only [segments_right_5, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece11_check
  · cases h; exact refinementPiece12_check
  · cases h; exact refinementPiece13_check
  · cases h; exact refinementPiece14_check
  · cases h; exact refinementPiece15_check
  · cases h; exact refinementPiece16_check
  · cases h; exact refinementPiece17_check
  · cases h; exact refinementPiece18_check

def segments_right_7 : List SourceSegment := [
  { lo := 2445/128, hi := 19101747/1000000, piece := refinementPiece55 },
  { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 },
  { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 },
  { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 },
  { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 },
  { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 },
  { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 },
  { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 },
  { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 },
  { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 },
  { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 },
  { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 },
  { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 },
  { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 },
  { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 },
  { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 },
  { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 },
  { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 }
]
theorem segments_right_7_segment_0_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 2445/128, hi := 19101747/1000000, piece := refinementPiece55 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]

theorem segments_right_7_segment_1_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]

theorem segments_right_7_segment_2_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]

theorem segments_right_7_segment_3_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]

theorem segments_right_7_segment_4_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]

theorem segments_right_7_segment_5_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]

theorem segments_right_7_segment_6_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]

theorem segments_right_7_segment_7_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]

theorem segments_right_7_segment_8_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]

theorem segments_right_7_segment_9_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]

theorem segments_right_7_segment_10_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]

theorem segments_right_7_segment_11_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]

theorem segments_right_7_segment_12_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]

theorem segments_right_7_segment_13_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]

theorem segments_right_7_segment_14_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]

theorem segments_right_7_segment_15_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]

theorem segments_right_7_segment_16_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece71, MacroPiece.box]

theorem segments_right_7_segment_17_checked : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece18, MacroPiece.box]

theorem segments_right_7_accepted : sourcePiecewiseCheck (2445/128) (1245/64) (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) segments_right_7 = true := by
  have hlen : decide (0 < segments_right_7.length) = true := by norm_num [segments_right_7]
  have hcover : sourceCoverFrom (2445/128) (1245/64) segments_right_7 = true := by
    norm_num [sourceCoverFrom, segments_right_7]
  have hall : segments_right_7.all (sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000)) = true := by
    simp only [segments_right_7, List.all_cons, List.all_nil, segments_right_7_segment_0_checked, segments_right_7_segment_1_checked, segments_right_7_segment_2_checked, segments_right_7_segment_3_checked, segments_right_7_segment_4_checked, segments_right_7_segment_5_checked, segments_right_7_segment_6_checked, segments_right_7_segment_7_checked, segments_right_7_segment_8_checked, segments_right_7_segment_9_checked, segments_right_7_segment_10_checked, segments_right_7_segment_11_checked, segments_right_7_segment_12_checked, segments_right_7_segment_13_checked, segments_right_7_segment_14_checked, segments_right_7_segment_15_checked, segments_right_7_segment_16_checked, segments_right_7_segment_17_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_7_pieces_checked : ∀ s ∈ segments_right_7, s.piece.check = true := by
  intro s hs
  simp only [segments_right_7, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece55_check
  · cases h; exact refinementPiece56_check
  · cases h; exact refinementPiece57_check
  · cases h; exact refinementPiece58_check
  · cases h; exact refinementPiece59_check
  · cases h; exact refinementPiece60_check
  · cases h; exact refinementPiece61_check
  · cases h; exact refinementPiece62_check
  · cases h; exact refinementPiece63_check
  · cases h; exact refinementPiece64_check
  · cases h; exact refinementPiece65_check
  · cases h; exact refinementPiece66_check
  · cases h; exact refinementPiece67_check
  · cases h; exact refinementPiece68_check
  · cases h; exact refinementPiece69_check
  · cases h; exact refinementPiece70_check
  · cases h; exact refinementPiece71_check
  · cases h; exact macroPiece18_check

def segments_right_8 : List SourceSegment := [
  { lo := 3255/128, hi := 5086319/200000, piece := refinementPiece84 },
  { lo := 5086319/200000, hi := 1272361/50000, piece := refinementPiece85 },
  { lo := 1272361/50000, hi := 5092569/200000, piece := refinementPiece86 },
  { lo := 5092569/200000, hi := 2547847/100000, piece := refinementPiece87 },
  { lo := 2547847/100000, hi := 5098819/200000, piece := refinementPiece88 },
  { lo := 5098819/200000, hi := 637743/25000, piece := refinementPiece89 },
  { lo := 637743/25000, hi := 5105069/200000, piece := refinementPiece90 },
  { lo := 5105069/200000, hi := 2554097/100000, piece := refinementPiece91 },
  { lo := 2554097/100000, hi := 5111319/200000, piece := refinementPiece92 },
  { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 },
  { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 },
  { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 },
  { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 },
  { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 },
  { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 },
  { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 },
  { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 },
  { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 },
  { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 },
  { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 },
  { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 },
  { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 },
  { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 },
  { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 },
  { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 },
  { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 },
  { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 },
  { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 },
  { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 },
  { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 },
  { lo := 323559/12500, hi := 5180069/200000, piece := refinementPiece114 },
  { lo := 5180069/200000, hi := 2591597/100000, piece := refinementPiece115 },
  { lo := 2591597/100000, hi := 5186319/200000, piece := refinementPiece116 },
  { lo := 5186319/200000, hi := 1297361/50000, piece := refinementPiece117 },
  { lo := 1297361/50000, hi := 5192569/200000, piece := refinementPiece118 },
  { lo := 5192569/200000, hi := 2597847/100000, piece := refinementPiece119 },
  { lo := 2597847/100000, hi := 1665/64, piece := macroPiece25 }
]
theorem segments_right_8_segment_0_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 3255/128, hi := 5086319/200000, piece := refinementPiece84 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece84, MacroPiece.box]

theorem segments_right_8_segment_1_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5086319/200000, hi := 1272361/50000, piece := refinementPiece85 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece85, MacroPiece.box]

theorem segments_right_8_segment_2_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1272361/50000, hi := 5092569/200000, piece := refinementPiece86 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece86, MacroPiece.box]

theorem segments_right_8_segment_3_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5092569/200000, hi := 2547847/100000, piece := refinementPiece87 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece87, MacroPiece.box]

theorem segments_right_8_segment_4_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2547847/100000, hi := 5098819/200000, piece := refinementPiece88 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece88, MacroPiece.box]

theorem segments_right_8_segment_5_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5098819/200000, hi := 637743/25000, piece := refinementPiece89 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece89, MacroPiece.box]

theorem segments_right_8_segment_6_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 637743/25000, hi := 5105069/200000, piece := refinementPiece90 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece90, MacroPiece.box]

theorem segments_right_8_segment_7_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5105069/200000, hi := 2554097/100000, piece := refinementPiece91 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece91, MacroPiece.box]

theorem segments_right_8_segment_8_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2554097/100000, hi := 5111319/200000, piece := refinementPiece92 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece92, MacroPiece.box]

theorem segments_right_8_segment_9_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5111319/200000, hi := 1278611/50000, piece := refinementPiece93 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece93, MacroPiece.box]

theorem segments_right_8_segment_10_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1278611/50000, hi := 5117569/200000, piece := refinementPiece94 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece94, MacroPiece.box]

theorem segments_right_8_segment_11_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5117569/200000, hi := 2560347/100000, piece := refinementPiece95 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece95, MacroPiece.box]

theorem segments_right_8_segment_12_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2560347/100000, hi := 5123819/200000, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_right_8_segment_13_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5123819/200000, hi := 160217/6250, piece := macroPiece24 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece24, MacroPiece.box]

theorem segments_right_8_segment_14_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 160217/6250, hi := 5130069/200000, piece := refinementPiece98 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece98, MacroPiece.box]

theorem segments_right_8_segment_15_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5130069/200000, hi := 2566597/100000, piece := refinementPiece99 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece99, MacroPiece.box]

theorem segments_right_8_segment_16_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2566597/100000, hi := 5136319/200000, piece := refinementPiece100 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece100, MacroPiece.box]

theorem segments_right_8_segment_17_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5136319/200000, hi := 1284861/50000, piece := refinementPiece101 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece101, MacroPiece.box]

theorem segments_right_8_segment_18_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1284861/50000, hi := 5142569/200000, piece := refinementPiece102 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece102, MacroPiece.box]

theorem segments_right_8_segment_19_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5142569/200000, hi := 2572847/100000, piece := refinementPiece103 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece103, MacroPiece.box]

theorem segments_right_8_segment_20_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2572847/100000, hi := 5148819/200000, piece := refinementPiece104 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece104, MacroPiece.box]

theorem segments_right_8_segment_21_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5148819/200000, hi := 643993/25000, piece := refinementPiece105 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece105, MacroPiece.box]

theorem segments_right_8_segment_22_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 643993/25000, hi := 5155069/200000, piece := refinementPiece106 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece106, MacroPiece.box]

theorem segments_right_8_segment_23_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5155069/200000, hi := 2579097/100000, piece := refinementPiece107 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece107, MacroPiece.box]

theorem segments_right_8_segment_24_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2579097/100000, hi := 5161319/200000, piece := refinementPiece108 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece108, MacroPiece.box]

theorem segments_right_8_segment_25_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5161319/200000, hi := 1291111/50000, piece := refinementPiece109 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece109, MacroPiece.box]

theorem segments_right_8_segment_26_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1291111/50000, hi := 5167569/200000, piece := refinementPiece110 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece110, MacroPiece.box]

theorem segments_right_8_segment_27_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5167569/200000, hi := 2585347/100000, piece := refinementPiece111 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece111, MacroPiece.box]

theorem segments_right_8_segment_28_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2585347/100000, hi := 5173819/200000, piece := refinementPiece112 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece112, MacroPiece.box]

theorem segments_right_8_segment_29_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5173819/200000, hi := 323559/12500, piece := refinementPiece113 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece113, MacroPiece.box]

theorem segments_right_8_segment_30_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 323559/12500, hi := 5180069/200000, piece := refinementPiece114 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece114, MacroPiece.box]

theorem segments_right_8_segment_31_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5180069/200000, hi := 2591597/100000, piece := refinementPiece115 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece115, MacroPiece.box]

theorem segments_right_8_segment_32_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2591597/100000, hi := 5186319/200000, piece := refinementPiece116 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece116, MacroPiece.box]

theorem segments_right_8_segment_33_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5186319/200000, hi := 1297361/50000, piece := refinementPiece117 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece117, MacroPiece.box]

theorem segments_right_8_segment_34_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 1297361/50000, hi := 5192569/200000, piece := refinementPiece118 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece118, MacroPiece.box]

theorem segments_right_8_segment_35_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 5192569/200000, hi := 2597847/100000, piece := refinementPiece119 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece119, MacroPiece.box]

theorem segments_right_8_segment_36_checked : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) { lo := 2597847/100000, hi := 1665/64, piece := macroPiece25 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece25, MacroPiece.box]

theorem segments_right_8_accepted : sourcePiecewiseCheck (3255/128) (1665/64) (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) segments_right_8 = true := by
  have hlen : decide (0 < segments_right_8.length) = true := by norm_num [segments_right_8]
  have hcover : sourceCoverFrom (3255/128) (1665/64) segments_right_8 = true := by
    norm_num [sourceCoverFrom, segments_right_8]
  have hall : segments_right_8.all (sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000)) = true := by
    simp only [segments_right_8, List.all_cons, List.all_nil, segments_right_8_segment_0_checked, segments_right_8_segment_1_checked, segments_right_8_segment_2_checked, segments_right_8_segment_3_checked, segments_right_8_segment_4_checked, segments_right_8_segment_5_checked, segments_right_8_segment_6_checked, segments_right_8_segment_7_checked, segments_right_8_segment_8_checked, segments_right_8_segment_9_checked, segments_right_8_segment_10_checked, segments_right_8_segment_11_checked, segments_right_8_segment_12_checked, segments_right_8_segment_13_checked, segments_right_8_segment_14_checked, segments_right_8_segment_15_checked, segments_right_8_segment_16_checked, segments_right_8_segment_17_checked, segments_right_8_segment_18_checked, segments_right_8_segment_19_checked, segments_right_8_segment_20_checked, segments_right_8_segment_21_checked, segments_right_8_segment_22_checked, segments_right_8_segment_23_checked, segments_right_8_segment_24_checked, segments_right_8_segment_25_checked, segments_right_8_segment_26_checked, segments_right_8_segment_27_checked, segments_right_8_segment_28_checked, segments_right_8_segment_29_checked, segments_right_8_segment_30_checked, segments_right_8_segment_31_checked, segments_right_8_segment_32_checked, segments_right_8_segment_33_checked, segments_right_8_segment_34_checked, segments_right_8_segment_35_checked, segments_right_8_segment_36_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_8_pieces_checked : ∀ s ∈ segments_right_8, s.piece.check = true := by
  intro s hs
  simp only [segments_right_8, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece84_check
  · cases h; exact refinementPiece85_check
  · cases h; exact refinementPiece86_check
  · cases h; exact refinementPiece87_check
  · cases h; exact refinementPiece88_check
  · cases h; exact refinementPiece89_check
  · cases h; exact refinementPiece90_check
  · cases h; exact refinementPiece91_check
  · cases h; exact refinementPiece92_check
  · cases h; exact refinementPiece93_check
  · cases h; exact refinementPiece94_check
  · cases h; exact refinementPiece95_check
  · cases h; exact macroPiece24_check
  · cases h; exact macroPiece24_check
  · cases h; exact refinementPiece98_check
  · cases h; exact refinementPiece99_check
  · cases h; exact refinementPiece100_check
  · cases h; exact refinementPiece101_check
  · cases h; exact refinementPiece102_check
  · cases h; exact refinementPiece103_check
  · cases h; exact refinementPiece104_check
  · cases h; exact refinementPiece105_check
  · cases h; exact refinementPiece106_check
  · cases h; exact refinementPiece107_check
  · cases h; exact refinementPiece108_check
  · cases h; exact refinementPiece109_check
  · cases h; exact refinementPiece110_check
  · cases h; exact refinementPiece111_check
  · cases h; exact refinementPiece112_check
  · cases h; exact refinementPiece113_check
  · cases h; exact refinementPiece114_check
  · cases h; exact refinementPiece115_check
  · cases h; exact refinementPiece116_check
  · cases h; exact refinementPiece117_check
  · cases h; exact refinementPiece118_check
  · cases h; exact refinementPiece119_check
  · cases h; exact macroPiece25_check

def segments_right_9 : List SourceSegment := [
  { lo := 795/128, hi := 250723/40000, piece := macroPiece2 },
  { lo := 250723/40000, hi := 62837/10000, piece := refinementPiece0 },
  { lo := 62837/10000, hi := 251973/40000, piece := refinementPiece1 },
  { lo := 251973/40000, hi := 126299/20000, piece := refinementPiece2 },
  { lo := 126299/20000, hi := 405/64, piece := refinementPiece3 }
]
theorem segments_right_9_segment_0_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 795/128, hi := 250723/40000, piece := macroPiece2 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece2, MacroPiece.box]

theorem segments_right_9_segment_1_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 250723/40000, hi := 62837/10000, piece := refinementPiece0 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece0, MacroPiece.box]

theorem segments_right_9_segment_2_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 62837/10000, hi := 251973/40000, piece := refinementPiece1 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece1, MacroPiece.box]

theorem segments_right_9_segment_3_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 251973/40000, hi := 126299/20000, piece := refinementPiece2 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece2, MacroPiece.box]

theorem segments_right_9_segment_4_checked : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) { lo := 126299/20000, hi := 405/64, piece := refinementPiece3 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]

theorem segments_right_9_accepted : sourcePiecewiseCheck (795/128) (405/64) (21287960894909617826490440080249/5000000000000000000000000000000000) segments_right_9 = true := by
  have hlen : decide (0 < segments_right_9.length) = true := by norm_num [segments_right_9]
  have hcover : sourceCoverFrom (795/128) (405/64) segments_right_9 = true := by
    norm_num [sourceCoverFrom, segments_right_9]
  have hall : segments_right_9.all (sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000)) = true := by
    simp only [segments_right_9, List.all_cons, List.all_nil, segments_right_9_segment_0_checked, segments_right_9_segment_1_checked, segments_right_9_segment_2_checked, segments_right_9_segment_3_checked, segments_right_9_segment_4_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_9_pieces_checked : ∀ s ∈ segments_right_9, s.piece.check = true := by
  intro s hs
  simp only [segments_right_9, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h
  · cases h; exact macroPiece2_check
  · cases h; exact refinementPiece0_check
  · cases h; exact refinementPiece1_check
  · cases h; exact refinementPiece2_check
  · cases h; exact refinementPiece3_check

def segments_right_11 : List SourceSegment := [
  { lo := 1215/64, hi := 4748093/250000, piece := refinementPiece48 },
  { lo := 4748093/250000, hi := 19007997/1000000, piece := refinementPiece49 },
  { lo := 19007997/1000000, hi := 9511811/500000, piece := refinementPiece50 },
  { lo := 9511811/500000, hi := 19039247/1000000, piece := refinementPiece51 },
  { lo := 19039247/1000000, hi := 2381859/125000, piece := refinementPiece52 },
  { lo := 2381859/125000, hi := 19070497/1000000, piece := refinementPiece53 },
  { lo := 19070497/1000000, hi := 9543061/500000, piece := refinementPiece54 },
  { lo := 9543061/500000, hi := 19101747/1000000, piece := refinementPiece55 },
  { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 },
  { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 },
  { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 },
  { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 },
  { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 },
  { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 },
  { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 },
  { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 },
  { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 },
  { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 },
  { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 },
  { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 },
  { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 },
  { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 },
  { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 },
  { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 },
  { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 }
]
theorem segments_right_11_segment_0_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 1215/64, hi := 4748093/250000, piece := refinementPiece48 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece48, MacroPiece.box]

theorem segments_right_11_segment_1_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4748093/250000, hi := 19007997/1000000, piece := refinementPiece49 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece49, MacroPiece.box]

theorem segments_right_11_segment_2_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19007997/1000000, hi := 9511811/500000, piece := refinementPiece50 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece50, MacroPiece.box]

theorem segments_right_11_segment_3_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9511811/500000, hi := 19039247/1000000, piece := refinementPiece51 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece51, MacroPiece.box]

theorem segments_right_11_segment_4_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19039247/1000000, hi := 2381859/125000, piece := refinementPiece52 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece52, MacroPiece.box]

theorem segments_right_11_segment_5_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 2381859/125000, hi := 19070497/1000000, piece := refinementPiece53 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece53, MacroPiece.box]

theorem segments_right_11_segment_6_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19070497/1000000, hi := 9543061/500000, piece := refinementPiece54 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece54, MacroPiece.box]

theorem segments_right_11_segment_7_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9543061/500000, hi := 19101747/1000000, piece := refinementPiece55 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece55, MacroPiece.box]

theorem segments_right_11_segment_8_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19101747/1000000, hi := 4779343/250000, piece := refinementPiece56 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece56, MacroPiece.box]

theorem segments_right_11_segment_9_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4779343/250000, hi := 19132997/1000000, piece := refinementPiece57 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece57, MacroPiece.box]

theorem segments_right_11_segment_10_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19132997/1000000, hi := 9574311/500000, piece := refinementPiece58 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece58, MacroPiece.box]

theorem segments_right_11_segment_11_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9574311/500000, hi := 19164247/1000000, piece := refinementPiece59 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece59, MacroPiece.box]

theorem segments_right_11_segment_12_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19164247/1000000, hi := 599371/31250, piece := refinementPiece60 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece60, MacroPiece.box]

theorem segments_right_11_segment_13_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 599371/31250, hi := 19195497/1000000, piece := refinementPiece61 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece61, MacroPiece.box]

theorem segments_right_11_segment_14_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19195497/1000000, hi := 9605561/500000, piece := refinementPiece62 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece62, MacroPiece.box]

theorem segments_right_11_segment_15_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9605561/500000, hi := 19226747/1000000, piece := refinementPiece63 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece63, MacroPiece.box]

theorem segments_right_11_segment_16_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19226747/1000000, hi := 4810593/250000, piece := refinementPiece64 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece64, MacroPiece.box]

theorem segments_right_11_segment_17_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 4810593/250000, hi := 19257997/1000000, piece := refinementPiece65 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece65, MacroPiece.box]

theorem segments_right_11_segment_18_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19257997/1000000, hi := 9636811/500000, piece := refinementPiece66 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece66, MacroPiece.box]

theorem segments_right_11_segment_19_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9636811/500000, hi := 19289247/1000000, piece := refinementPiece67 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece67, MacroPiece.box]

theorem segments_right_11_segment_20_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19289247/1000000, hi := 2413109/125000, piece := refinementPiece68 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece68, MacroPiece.box]

theorem segments_right_11_segment_21_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 2413109/125000, hi := 19320497/1000000, piece := refinementPiece69 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece69, MacroPiece.box]

theorem segments_right_11_segment_22_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19320497/1000000, hi := 9668061/500000, piece := refinementPiece70 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece70, MacroPiece.box]

theorem segments_right_11_segment_23_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 9668061/500000, hi := 19351747/1000000, piece := refinementPiece71 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece71, MacroPiece.box]

theorem segments_right_11_segment_24_checked : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) { lo := 19351747/1000000, hi := 1245/64, piece := macroPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, macroPiece18, MacroPiece.box]

theorem segments_right_11_accepted : sourcePiecewiseCheck (1215/64) (1245/64) (1755263779336959657910023102330969/7812500000000000000000000000000000000000) segments_right_11 = true := by
  have hlen : decide (0 < segments_right_11.length) = true := by norm_num [segments_right_11]
  have hcover : sourceCoverFrom (1215/64) (1245/64) segments_right_11 = true := by
    norm_num [sourceCoverFrom, segments_right_11]
  have hall : segments_right_11.all (sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000)) = true := by
    simp only [segments_right_11, List.all_cons, List.all_nil, segments_right_11_segment_0_checked, segments_right_11_segment_1_checked, segments_right_11_segment_2_checked, segments_right_11_segment_3_checked, segments_right_11_segment_4_checked, segments_right_11_segment_5_checked, segments_right_11_segment_6_checked, segments_right_11_segment_7_checked, segments_right_11_segment_8_checked, segments_right_11_segment_9_checked, segments_right_11_segment_10_checked, segments_right_11_segment_11_checked, segments_right_11_segment_12_checked, segments_right_11_segment_13_checked, segments_right_11_segment_14_checked, segments_right_11_segment_15_checked, segments_right_11_segment_16_checked, segments_right_11_segment_17_checked, segments_right_11_segment_18_checked, segments_right_11_segment_19_checked, segments_right_11_segment_20_checked, segments_right_11_segment_21_checked, segments_right_11_segment_22_checked, segments_right_11_segment_23_checked, segments_right_11_segment_24_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_11_pieces_checked : ∀ s ∈ segments_right_11, s.piece.check = true := by
  intro s hs
  simp only [segments_right_11, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece48_check
  · cases h; exact refinementPiece49_check
  · cases h; exact refinementPiece50_check
  · cases h; exact refinementPiece51_check
  · cases h; exact refinementPiece52_check
  · cases h; exact refinementPiece53_check
  · cases h; exact refinementPiece54_check
  · cases h; exact refinementPiece55_check
  · cases h; exact refinementPiece56_check
  · cases h; exact refinementPiece57_check
  · cases h; exact refinementPiece58_check
  · cases h; exact refinementPiece59_check
  · cases h; exact refinementPiece60_check
  · cases h; exact refinementPiece61_check
  · cases h; exact refinementPiece62_check
  · cases h; exact refinementPiece63_check
  · cases h; exact refinementPiece64_check
  · cases h; exact refinementPiece65_check
  · cases h; exact refinementPiece66_check
  · cases h; exact refinementPiece67_check
  · cases h; exact refinementPiece68_check
  · cases h; exact refinementPiece69_check
  · cases h; exact refinementPiece70_check
  · cases h; exact refinementPiece71_check
  · cases h; exact macroPiece18_check

def segments_right_12 : List SourceSegment := [
  { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 },
  { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 },
  { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 },
  { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 },
  { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 },
  { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 },
  { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 },
  { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 }
]
theorem segments_right_12_segment_0_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 825/128, hi := 258223/40000, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_right_12_segment_1_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]

theorem segments_right_12_segment_2_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]

theorem segments_right_12_segment_3_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]

theorem segments_right_12_segment_4_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]

theorem segments_right_12_segment_5_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]

theorem segments_right_12_segment_6_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]

theorem segments_right_12_segment_7_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]

theorem segments_right_12_accepted : sourcePiecewiseCheck (825/128) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments_right_12 = true := by
  have hlen : decide (0 < segments_right_12.length) = true := by norm_num [segments_right_12]
  have hcover : sourceCoverFrom (825/128) (105/16) segments_right_12 = true := by
    norm_num [sourceCoverFrom, segments_right_12]
  have hall : segments_right_12.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments_right_12, List.all_cons, List.all_nil, segments_right_12_segment_0_checked, segments_right_12_segment_1_checked, segments_right_12_segment_2_checked, segments_right_12_segment_3_checked, segments_right_12_segment_4_checked, segments_right_12_segment_5_checked, segments_right_12_segment_6_checked, segments_right_12_segment_7_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_12_pieces_checked : ∀ s ∈ segments_right_12, s.piece.check = true := by
  intro s hs
  simp only [segments_right_12, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece11_check
  · cases h; exact refinementPiece12_check
  · cases h; exact refinementPiece13_check
  · cases h; exact refinementPiece14_check
  · cases h; exact refinementPiece15_check
  · cases h; exact refinementPiece16_check
  · cases h; exact refinementPiece17_check
  · cases h; exact refinementPiece18_check

def segments_right_14 : List SourceSegment := [
  { lo := 405/64, hi := 253223/40000, piece := refinementPiece3 },
  { lo := 253223/40000, hi := 31731/5000, piece := refinementPiece4 },
  { lo := 31731/5000, hi := 254473/40000, piece := refinementPiece5 },
  { lo := 254473/40000, hi := 127549/20000, piece := refinementPiece6 },
  { lo := 127549/20000, hi := 255723/40000, piece := refinementPiece7 },
  { lo := 255723/40000, hi := 64087/10000, piece := refinementPiece8 },
  { lo := 64087/10000, hi := 256973/40000, piece := refinementPiece9 },
  { lo := 256973/40000, hi := 128799/20000, piece := refinementPiece10 },
  { lo := 128799/20000, hi := 258223/40000, piece := refinementPiece11 },
  { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 },
  { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 },
  { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 },
  { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 },
  { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 },
  { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 },
  { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 }
]
theorem segments_right_14_segment_0_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 405/64, hi := 253223/40000, piece := refinementPiece3 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece3, MacroPiece.box]

theorem segments_right_14_segment_1_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 253223/40000, hi := 31731/5000, piece := refinementPiece4 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece4, MacroPiece.box]

theorem segments_right_14_segment_2_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 31731/5000, hi := 254473/40000, piece := refinementPiece5 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece5, MacroPiece.box]

theorem segments_right_14_segment_3_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 254473/40000, hi := 127549/20000, piece := refinementPiece6 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece6, MacroPiece.box]

theorem segments_right_14_segment_4_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 127549/20000, hi := 255723/40000, piece := refinementPiece7 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece7, MacroPiece.box]

theorem segments_right_14_segment_5_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 255723/40000, hi := 64087/10000, piece := refinementPiece8 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece8, MacroPiece.box]

theorem segments_right_14_segment_6_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 64087/10000, hi := 256973/40000, piece := refinementPiece9 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece9, MacroPiece.box]

theorem segments_right_14_segment_7_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 256973/40000, hi := 128799/20000, piece := refinementPiece10 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece10, MacroPiece.box]

theorem segments_right_14_segment_8_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 128799/20000, hi := 258223/40000, piece := refinementPiece11 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece11, MacroPiece.box]

theorem segments_right_14_segment_9_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 258223/40000, hi := 8089/1250, piece := refinementPiece12 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece12, MacroPiece.box]

theorem segments_right_14_segment_10_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 8089/1250, hi := 259473/40000, piece := refinementPiece13 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece13, MacroPiece.box]

theorem segments_right_14_segment_11_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 259473/40000, hi := 130049/20000, piece := refinementPiece14 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece14, MacroPiece.box]

theorem segments_right_14_segment_12_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 130049/20000, hi := 260723/40000, piece := refinementPiece15 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece15, MacroPiece.box]

theorem segments_right_14_segment_13_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 260723/40000, hi := 65337/10000, piece := refinementPiece16 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece16, MacroPiece.box]

theorem segments_right_14_segment_14_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 65337/10000, hi := 261973/40000, piece := refinementPiece17 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece17, MacroPiece.box]

theorem segments_right_14_segment_15_checked : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) { lo := 261973/40000, hi := 105/16, piece := refinementPiece18 } = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, refinementPiece18, MacroPiece.box]

theorem segments_right_14_accepted : sourcePiecewiseCheck (405/64) (105/16) (12892869620170946020955818564495929/50000000000000000000000000000000000000) segments_right_14 = true := by
  have hlen : decide (0 < segments_right_14.length) = true := by norm_num [segments_right_14]
  have hcover : sourceCoverFrom (405/64) (105/16) segments_right_14 = true := by
    norm_num [sourceCoverFrom, segments_right_14]
  have hall : segments_right_14.all (sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000)) = true := by
    simp only [segments_right_14, List.all_cons, List.all_nil, segments_right_14_segment_0_checked, segments_right_14_segment_1_checked, segments_right_14_segment_2_checked, segments_right_14_segment_3_checked, segments_right_14_segment_4_checked, segments_right_14_segment_5_checked, segments_right_14_segment_6_checked, segments_right_14_segment_7_checked, segments_right_14_segment_8_checked, segments_right_14_segment_9_checked, segments_right_14_segment_10_checked, segments_right_14_segment_11_checked, segments_right_14_segment_12_checked, segments_right_14_segment_13_checked, segments_right_14_segment_14_checked, segments_right_14_segment_15_checked, Bool.true_and]
  simp [sourcePiecewiseCheck, hlen, hcover, hall]
theorem segments_right_14_pieces_checked : ∀ s ∈ segments_right_14, s.piece.check = true := by
  intro s hs
  simp only [segments_right_14, List.mem_cons, List.mem_nil_iff, or_false] at hs
  rcases hs with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · cases h; exact refinementPiece3_check
  · cases h; exact refinementPiece4_check
  · cases h; exact refinementPiece5_check
  · cases h; exact refinementPiece6_check
  · cases h; exact refinementPiece7_check
  · cases h; exact refinementPiece8_check
  · cases h; exact refinementPiece9_check
  · cases h; exact refinementPiece10_check
  · cases h; exact refinementPiece11_check
  · cases h; exact refinementPiece12_check
  · cases h; exact refinementPiece13_check
  · cases h; exact refinementPiece14_check
  · cases h; exact refinementPiece15_check
  · cases h; exact refinementPiece16_check
  · cases h; exact refinementPiece17_check
  · cases h; exact refinementPiece18_check


-- Exact boxes, paths, anchors, segment certificates, tangent checks, and midpoint parent.

def targetA : ℚ := 647 / 50000
def targetB : ℚ := 1094977 / 5000000000

def sourceParentBox : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (825/128) | 2 => (795/128) | 3 => (825/128) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)

def sourceLeftBox : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (825/128) | 2 => (795/128) | 3 => (825/128) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (825/128) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)

def sourceRightBox : GapBox where
  lo := fun i => match i.val with | 0 => (825/128) | 1 => (825/128) | 2 => (795/128) | 3 => (825/128) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)

def sourceParentPath : List (Fin 5 × Bool) := [
  (⟨2, by decide⟩, false),
  (⟨1, by decide⟩, false),
  (⟨3, by decide⟩, false),
  (⟨0, by decide⟩, false),
  (⟨4, by decide⟩, false),
  (⟨2, by decide⟩, false),
  (⟨1, by decide⟩, false),
  (⟨3, by decide⟩, false),
  (⟨0, by decide⟩, false),
  (⟨4, by decide⟩, false),
  (⟨2, by decide⟩, false),
  (⟨1, by decide⟩, false),
  (⟨3, by decide⟩, false),
  (⟨0, by decide⟩, false),
  (⟨4, by decide⟩, false),
  (⟨2, by decide⟩, true),
  (⟨1, by decide⟩, true),
  (⟨3, by decide⟩, true),
  (⟨0, by decide⟩, true),
  (⟨4, by decide⟩, true),
  (⟨2, by decide⟩, true),
  (⟨1, by decide⟩, true),
  (⟨3, by decide⟩, true),
  (⟨0, by decide⟩, true),
  (⟨4, by decide⟩, true),
  (⟨2, by decide⟩, false),
  (⟨1, by decide⟩, false),
  (⟨3, by decide⟩, false),
  (⟨0, by decide⟩, false),
  (⟨4, by decide⟩, false),
  (⟨2, by decide⟩, true),
  (⟨1, by decide⟩, true),
  (⟨3, by decide⟩, true),
  (⟨0, by decide⟩, true),
  (⟨4, by decide⟩, true),
  (⟨2, by decide⟩, false),
  (⟨1, by decide⟩, true),
  (⟨3, by decide⟩, true),
  (⟨0, by decide⟩, true),
  (⟨4, by decide⟩, true),
  (⟨2, by decide⟩, true),
  (⟨1, by decide⟩, true),
  (⟨3, by decide⟩, true)
]


def descend (box : GapBox) (step : Fin 5 × Bool) : GapBox :=
  if step.2 then box.upperHalf step.1 else box.lowerHalf step.1

def sourceLeftPath : List (Fin 5 × Bool) :=
  sourceParentPath ++ [(⟨0, by decide⟩, false)]
def sourceRightPath : List (Fin 5 × Bool) :=
  sourceParentPath ++ [(⟨0, by decide⟩, true)]

theorem gapBox_ext_exact {a b : GapBox}
    (hlo : ∀ i, a.lo i = b.lo i) (hhi : ∀ i, a.hi i = b.hi i) : a = b := by
  cases a with
  | mk alo ahi =>
    cases b with
    | mk blo bhi =>
      simp only [GapBox.mk.injEq]
      constructor
      · funext i
        exact hlo i
      · funext i
        exact hhi i

set_option maxRecDepth 10000 in
set_option maxHeartbeats 2000000 in
theorem source_children_match_parent_split :
    sourceLeftBox = sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5) ∧
    sourceRightBox = sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5) := by
  constructor
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [sourceLeftBox, sourceParentBox,
        GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [sourceLeftBox, sourceParentBox,
        GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [sourceRightBox, sourceParentBox,
        GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [sourceRightBox, sourceParentBox,
        GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def sourceAnchorCodes : Fin 5 → ℕ := fun _ => 0
def sourceAnchorLeft : Fin 5 → ℚ := fun i =>
  sourceLeftBox.lo i + (sourceAnchorCodes i : ℚ) / 16384 *
    (sourceLeftBox.hi i - sourceLeftBox.lo i)
def sourceAnchorRight : Fin 5 → ℚ := fun i =>
  sourceRightBox.lo i + (sourceAnchorCodes i : ℚ) / 16384 *
    (sourceRightBox.hi i - sourceRightBox.lo i)

theorem source_left_anchor_exact : sourceAnchorLeft = sourceLeftBox.lo := by
  funext i
  simp [sourceAnchorLeft, sourceAnchorCodes]
theorem source_right_anchor_exact : sourceAnchorRight = sourceRightBox.lo := by
  funext i
  simp [sourceAnchorRight, sourceAnchorCodes]

def sourceDistanceLeft (p : Fin 15) : RatInterval := match p.val with | 0 => ⟨(405/64), (825/128)⟩ | 1 => ⟨(1635/128), (1665/128)⟩ | 2 => ⟨(1215/64), (2475/128)⟩ | 3 => ⟨(3255/128), (3315/128)⟩ | 4 => ⟨(4065/128), (4155/128)⟩ | 5 => ⟨(825/128), (105/16)⟩ | 6 => ⟨(405/32), (825/64)⟩ | 7 => ⟨(2445/128), (1245/64)⟩ | 8 => ⟨(3255/128), (1665/64)⟩ | 9 => ⟨(795/128), (405/64)⟩ | 10 => ⟨(405/32), (825/64)⟩ | 11 => ⟨(1215/64), (1245/64)⟩ | 12 => ⟨(825/128), (105/16)⟩ | 13 => ⟨(1635/128), (105/8)⟩ | _ => ⟨(405/64), (105/16)⟩

def sourceFloorLeft (p : Fin 15) : ℚ := match p.val with | 0 => (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) | 1 => (0) | 2 => (1755263779336959657910023102330969/7812500000000000000000000000000000000000) | 3 => (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) | 4 => (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) | 5 => (12892869620170946020955818564495929/50000000000000000000000000000000000000) | 6 => (0) | 7 => (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) | 8 => (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) | 9 => (21287960894909617826490440080249/5000000000000000000000000000000000) | 10 => (0) | 11 => (1755263779336959657910023102330969/7812500000000000000000000000000000000000) | 12 => (12892869620170946020955818564495929/50000000000000000000000000000000000000) | 13 => (0) | _ => (12892869620170946020955818564495929/50000000000000000000000000000000000000)


def sourceRankTermsLeft (p : Fin 15) : RankOneModel :=
  if p.val = 1 then macroPieceRankModel (fun _ => MacroPrototype.macroPiece11) p
  else if p.val = 13 then macroPieceRankModel (fun _ => MacroPrototype.macroPiece11) p
  else { base := sourceFloorLeft p, weight := 0, offset := 0, coeff := fun _ => 0 }

theorem source_distance_intervals_left_exact :
    ∀ p, distanceInterval sourceLeftBox p = sourceDistanceLeft p := by
  intro p
  fin_cases p <;> simp [distanceInterval, sourceDistanceLeft, gapSupport,
    pairLeft, pairRight, sourceLeftBox, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num



theorem source_model_left_0_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨0, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨0, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨0, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_0_accepted
    segments_left_0_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_1_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨1, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨1, by decide⟩ : Fin 15)) ^ 2 := by
  have hfit : MacroPrototype.macroPiece11.box.lo ≤
      (distanceInterval sourceLeftBox (⟨1, by decide⟩ : Fin 15)).lo ∧
      (distanceInterval sourceLeftBox (⟨1, by decide⟩ : Fin 15)).hi ≤ MacroPrototype.macroPiece11.box.hi := by
    rw [source_distance_intervals_left_exact (⟨1, by decide⟩ : Fin 15)]
    norm_num [sourceDistanceLeft, MacroPrototype.macroPiece11, MacroPiece.box]
  have hd := distanceInterval_holds hg (⟨1, by decide⟩ : Fin 15)
  have hpiece : RatInterval.Holds MacroPrototype.macroPiece11.box
      (gapDistance g (⟨1, by decide⟩ : Fin 15)) := by
    constructor
    · have hlo : MacroPrototype.macroPiece11.box.lo ≤
        (distanceInterval sourceLeftBox (⟨1, by decide⟩ : Fin 15)).lo := hfit.1
      have hloR : (MacroPrototype.macroPiece11.box.lo : ℝ) ≤
          ((distanceInterval sourceLeftBox (⟨(⟨1, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).lo : ℝ) := by
        exact_mod_cast hlo
      exact hloR.trans hd.1
    · have hhi : (distanceInterval sourceLeftBox (⟨1, by decide⟩ : Fin 15)).hi ≤
        MacroPrototype.macroPiece11.box.hi := hfit.2
      have hhiR : ((distanceInterval sourceLeftBox (⟨(⟨1, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).hi : ℝ) ≤
          (MacroPrototype.macroPiece11.box.hi : ℝ) := by
        exact_mod_cast hhi
      exact hd.2.trans hhiR
  have hbound := MacroPiece.check_sound MacroPrototype.macroPiece11_check hpiece
  simpa [sourceRankTermsLeft] using hbound


theorem source_model_left_2_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨2, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨2, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨2, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_2_accepted
    segments_left_2_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_3_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨3, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨3, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨3, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_3_accepted
    segments_left_3_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_4_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨4, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨4, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨4, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_4_accepted
    segments_left_4_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_5_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨5, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨5, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨5, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_5_accepted
    segments_left_5_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_6_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨6, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨6, by decide⟩ : Fin 15)) ^ 2 := by
  have hnonneg : (0 : ℝ) ≤ 2 * mtKernel (gapDistance g (⟨6, by decide⟩ : Fin 15)) ^ 2 := by positivity
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hnonneg


theorem source_model_left_7_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨7, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨7, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨7, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_7_accepted
    segments_left_7_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_8_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨8, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨8, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨8, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_8_accepted
    segments_left_8_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_9_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨9, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨9, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨9, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_9_accepted
    segments_left_9_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_10_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨10, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨10, by decide⟩ : Fin 15)) ^ 2 := by
  have hnonneg : (0 : ℝ) ≤ 2 * mtKernel (gapDistance g (⟨10, by decide⟩ : Fin 15)) ^ 2 := by positivity
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hnonneg


theorem source_model_left_11_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨11, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨11, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨11, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_11_accepted
    segments_left_11_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_12_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨12, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨12, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨12, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_12_accepted
    segments_left_12_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_left_13_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨13, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨13, by decide⟩ : Fin 15)) ^ 2 := by
  have hfit : MacroPrototype.macroPiece11.box.lo ≤
      (distanceInterval sourceLeftBox (⟨13, by decide⟩ : Fin 15)).lo ∧
      (distanceInterval sourceLeftBox (⟨13, by decide⟩ : Fin 15)).hi ≤ MacroPrototype.macroPiece11.box.hi := by
    rw [source_distance_intervals_left_exact (⟨13, by decide⟩ : Fin 15)]
    norm_num [sourceDistanceLeft, MacroPrototype.macroPiece11, MacroPiece.box]
  have hd := distanceInterval_holds hg (⟨13, by decide⟩ : Fin 15)
  have hpiece : RatInterval.Holds MacroPrototype.macroPiece11.box
      (gapDistance g (⟨13, by decide⟩ : Fin 15)) := by
    constructor
    · have hlo : MacroPrototype.macroPiece11.box.lo ≤
        (distanceInterval sourceLeftBox (⟨13, by decide⟩ : Fin 15)).lo := hfit.1
      have hloR : (MacroPrototype.macroPiece11.box.lo : ℝ) ≤
          ((distanceInterval sourceLeftBox (⟨(⟨13, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).lo : ℝ) := by
        exact_mod_cast hlo
      exact hloR.trans hd.1
    · have hhi : (distanceInterval sourceLeftBox (⟨13, by decide⟩ : Fin 15)).hi ≤
        MacroPrototype.macroPiece11.box.hi := hfit.2
      have hhiR : ((distanceInterval sourceLeftBox (⟨(⟨13, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).hi : ℝ) ≤
          (MacroPrototype.macroPiece11.box.hi : ℝ) := by
        exact_mod_cast hhi
      exact hd.2.trans hhiR
  have hbound := MacroPiece.check_sound MacroPrototype.macroPiece11_check hpiece
  simpa [sourceRankTermsLeft] using hbound


theorem source_model_left_14_valid {g : Fin 5 → ℝ} (hg : sourceLeftBox.Holds g) :
    (sourceRankTermsLeft (⟨14, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨14, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨14, by decide⟩ : Fin 15)
  rw [source_distance_intervals_left_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_left_14_accepted
    segments_left_14_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsLeft, sourceFloorLeft, RankOneModel.value,
    RankOneModel.dot] using hbound

theorem source_models_left_pairwise_valid {g : Fin 5 → ℝ}
    (hg : sourceLeftBox.Holds g) : ∀ p,
      (sourceRankTermsLeft p).value g ≤ 2 * mtKernel (gapDistance g p) ^ 2 := by
  intro p
  fin_cases p

  · exact source_model_left_0_valid hg

  · exact source_model_left_1_valid hg

  · exact source_model_left_2_valid hg

  · exact source_model_left_3_valid hg

  · exact source_model_left_4_valid hg

  · exact source_model_left_5_valid hg

  · exact source_model_left_6_valid hg

  · exact source_model_left_7_valid hg

  · exact source_model_left_8_valid hg

  · exact source_model_left_9_valid hg

  · exact source_model_left_10_valid hg

  · exact source_model_left_11_valid hg

  · exact source_model_left_12_valid hg

  · exact source_model_left_13_valid hg

  · exact source_model_left_14_valid hg


theorem source_rank_tangent_left :
    rankTangentLower sourceRankTermsLeft targetB sourceLeftBox
      sourceAnchorLeft = (108853955129699356804065918948443215217/7812500000000000000000000000000000000000) := by
  norm_num [rankTangentLower, rankObjectiveRat, rankGradient,
    affineCoordinateLower, sourceRankTermsLeft, sourceFloorLeft,
    sourceAnchorLeft, sourceAnchorCodes, targetB, sourceLeftBox,
    MacroPrototype.macroPiece11, MacroPiece.box, macroPieceRankModel,
    wellRankModel, wellSlope, wellOffset, consecutiveCoeff, gapSupport,
    RankOneModel.valueRat, RankOneModel.dotRat,
    pairLeft, pairRight, Finset.sum_filter, Fin.sum_univ_succ,
    Fin.sum_univ_five]

theorem source_rank_tangent_check_left :
    rankTangentCheck targetA targetB sourceLeftBox sourceAnchorLeft
      sourceRankTermsLeft = true := by
  have hordered : sourceLeftBox.ordered = true := by
    rw [GapBox.ordered_iff]
    intro i
    fin_cases i <;> norm_num [sourceLeftBox]
  have hanchor : ∀ i, sourceLeftBox.lo i ≤ sourceAnchorLeft i ∧
      sourceAnchorLeft i ≤ sourceLeftBox.hi i := by
    intro i
    fin_cases i <;> norm_num [sourceAnchorLeft, sourceAnchorCodes, sourceLeftBox]
  have hweights : ∀ p, 0 ≤ (sourceRankTermsLeft p).weight := by
    intro p
    fin_cases p <;> norm_num [sourceRankTermsLeft, sourceFloorLeft,
      MacroPrototype.macroPiece11, macroPieceRankModel, wellRankModel, wellSlope, wellOffset]
  have hmargin : targetA ≤ rankTangentLower sourceRankTermsLeft targetB
      sourceLeftBox sourceAnchorLeft := by
    rw [source_rank_tangent_left]
    norm_num [targetA]
  simp [rankTangentCheck, hordered, hanchor, hweights, hmargin]

theorem source_left_box_predicate :
    ∀ ⦃g : Fin 5 → ℝ⦄, sourceLeftBox.Holds g →
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  exact rankTangentCheck_energy_sound source_rank_tangent_check_left
    (by
      intro g hg p
      exact source_models_left_pairwise_valid hg p)

def sourceDistanceRight (p : Fin 15) : RatInterval := match p.val with | 0 => ⟨(825/128), (105/16)⟩ | 1 => ⟨(825/64), (105/8)⟩ | 2 => ⟨(2445/128), (1245/64)⟩ | 3 => ⟨(1635/64), (1665/64)⟩ | 4 => ⟨(255/8), (2085/64)⟩ | 5 => ⟨(825/128), (105/16)⟩ | 6 => ⟨(405/32), (825/64)⟩ | 7 => ⟨(2445/128), (1245/64)⟩ | 8 => ⟨(3255/128), (1665/64)⟩ | 9 => ⟨(795/128), (405/64)⟩ | 10 => ⟨(405/32), (825/64)⟩ | 11 => ⟨(1215/64), (1245/64)⟩ | 12 => ⟨(825/128), (105/16)⟩ | 13 => ⟨(1635/128), (105/8)⟩ | _ => ⟨(405/64), (105/16)⟩

def sourceFloorRight (p : Fin 15) : ℚ := match p.val with | 0 => (12892869620170946020955818564495929/50000000000000000000000000000000000000) | 1 => (0) | 2 => (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) | 3 => (1060756076606974029304872234228987649/5000000000000000000000000000000000000000) | 4 => (245028537159250067459167806169/1250000000000000000000000000000000) | 5 => (12892869620170946020955818564495929/50000000000000000000000000000000000000) | 6 => (0) | 7 => (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) | 8 => (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) | 9 => (21287960894909617826490440080249/5000000000000000000000000000000000) | 10 => (0) | 11 => (1755263779336959657910023102330969/7812500000000000000000000000000000000000) | 12 => (12892869620170946020955818564495929/50000000000000000000000000000000000000) | 13 => (0) | _ => (12892869620170946020955818564495929/50000000000000000000000000000000000000)


def sourceRankTermsRight (p : Fin 15) : RankOneModel :=
  if p.val = 1 then macroPieceRankModel (fun _ => MacroPrototype.macroPiece11) p
  else if p.val = 13 then macroPieceRankModel (fun _ => MacroPrototype.macroPiece11) p
  else { base := sourceFloorRight p, weight := 0, offset := 0, coeff := fun _ => 0 }

theorem source_distance_intervals_right_exact :
    ∀ p, distanceInterval sourceRightBox p = sourceDistanceRight p := by
  intro p
  fin_cases p <;> simp [distanceInterval, sourceDistanceRight, gapSupport,
    pairLeft, pairRight, sourceRightBox, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num



theorem source_model_right_0_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨0, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨0, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨0, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_0_accepted
    segments_right_0_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_1_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨1, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨1, by decide⟩ : Fin 15)) ^ 2 := by
  have hfit : MacroPrototype.macroPiece11.box.lo ≤
      (distanceInterval sourceRightBox (⟨1, by decide⟩ : Fin 15)).lo ∧
      (distanceInterval sourceRightBox (⟨1, by decide⟩ : Fin 15)).hi ≤ MacroPrototype.macroPiece11.box.hi := by
    rw [source_distance_intervals_right_exact (⟨1, by decide⟩ : Fin 15)]
    norm_num [sourceDistanceRight, MacroPrototype.macroPiece11, MacroPiece.box]
  have hd := distanceInterval_holds hg (⟨1, by decide⟩ : Fin 15)
  have hpiece : RatInterval.Holds MacroPrototype.macroPiece11.box
      (gapDistance g (⟨1, by decide⟩ : Fin 15)) := by
    constructor
    · have hlo : MacroPrototype.macroPiece11.box.lo ≤
        (distanceInterval sourceRightBox (⟨1, by decide⟩ : Fin 15)).lo := hfit.1
      have hloR : (MacroPrototype.macroPiece11.box.lo : ℝ) ≤
          ((distanceInterval sourceRightBox (⟨(⟨1, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).lo : ℝ) := by
        exact_mod_cast hlo
      exact hloR.trans hd.1
    · have hhi : (distanceInterval sourceRightBox (⟨1, by decide⟩ : Fin 15)).hi ≤
        MacroPrototype.macroPiece11.box.hi := hfit.2
      have hhiR : ((distanceInterval sourceRightBox (⟨(⟨1, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).hi : ℝ) ≤
          (MacroPrototype.macroPiece11.box.hi : ℝ) := by
        exact_mod_cast hhi
      exact hd.2.trans hhiR
  have hbound := MacroPiece.check_sound MacroPrototype.macroPiece11_check hpiece
  simpa [sourceRankTermsRight] using hbound


theorem source_model_right_2_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨2, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨2, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨2, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_2_accepted
    segments_right_2_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_3_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨3, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨3, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨3, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_3_accepted
    segments_right_3_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_4_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨4, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨4, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨4, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_4_accepted
    segments_right_4_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_5_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨5, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨5, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨5, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_5_accepted
    segments_right_5_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_6_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨6, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨6, by decide⟩ : Fin 15)) ^ 2 := by
  have hnonneg : (0 : ℝ) ≤ 2 * mtKernel (gapDistance g (⟨6, by decide⟩ : Fin 15)) ^ 2 := by positivity
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hnonneg


theorem source_model_right_7_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨7, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨7, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨7, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_7_accepted
    segments_right_7_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_8_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨8, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨8, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨8, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_8_accepted
    segments_right_8_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_9_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨9, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨9, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨9, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_9_accepted
    segments_right_9_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_10_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨10, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨10, by decide⟩ : Fin 15)) ^ 2 := by
  have hnonneg : (0 : ℝ) ≤ 2 * mtKernel (gapDistance g (⟨10, by decide⟩ : Fin 15)) ^ 2 := by positivity
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hnonneg


theorem source_model_right_11_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨11, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨11, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨11, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_11_accepted
    segments_right_11_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_12_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨12, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨12, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨12, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_12_accepted
    segments_right_12_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound


theorem source_model_right_13_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨13, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨13, by decide⟩ : Fin 15)) ^ 2 := by
  have hfit : MacroPrototype.macroPiece11.box.lo ≤
      (distanceInterval sourceRightBox (⟨13, by decide⟩ : Fin 15)).lo ∧
      (distanceInterval sourceRightBox (⟨13, by decide⟩ : Fin 15)).hi ≤ MacroPrototype.macroPiece11.box.hi := by
    rw [source_distance_intervals_right_exact (⟨13, by decide⟩ : Fin 15)]
    norm_num [sourceDistanceRight, MacroPrototype.macroPiece11, MacroPiece.box]
  have hd := distanceInterval_holds hg (⟨13, by decide⟩ : Fin 15)
  have hpiece : RatInterval.Holds MacroPrototype.macroPiece11.box
      (gapDistance g (⟨13, by decide⟩ : Fin 15)) := by
    constructor
    · have hlo : MacroPrototype.macroPiece11.box.lo ≤
        (distanceInterval sourceRightBox (⟨13, by decide⟩ : Fin 15)).lo := hfit.1
      have hloR : (MacroPrototype.macroPiece11.box.lo : ℝ) ≤
          ((distanceInterval sourceRightBox (⟨(⟨13, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).lo : ℝ) := by
        exact_mod_cast hlo
      exact hloR.trans hd.1
    · have hhi : (distanceInterval sourceRightBox (⟨13, by decide⟩ : Fin 15)).hi ≤
        MacroPrototype.macroPiece11.box.hi := hfit.2
      have hhiR : ((distanceInterval sourceRightBox (⟨(⟨13, by decide⟩ : Fin 15), by decide⟩ : Fin 15)).hi : ℝ) ≤
          (MacroPrototype.macroPiece11.box.hi : ℝ) := by
        exact_mod_cast hhi
      exact hd.2.trans hhiR
  have hbound := MacroPiece.check_sound MacroPrototype.macroPiece11_check hpiece
  simpa [sourceRankTermsRight] using hbound


theorem source_model_right_14_valid {g : Fin 5 → ℝ} (hg : sourceRightBox.Holds g) :
    (sourceRankTermsRight (⟨14, by decide⟩ : Fin 15)).value g ≤ 2 * mtKernel (gapDistance g (⟨14, by decide⟩ : Fin 15)) ^ 2 := by
  have hdist := distanceInterval_holds hg (⟨14, by decide⟩ : Fin 15)
  rw [source_distance_intervals_right_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_right_14_accepted
    segments_right_14_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTermsRight, sourceFloorRight, RankOneModel.value,
    RankOneModel.dot] using hbound

theorem source_models_right_pairwise_valid {g : Fin 5 → ℝ}
    (hg : sourceRightBox.Holds g) : ∀ p,
      (sourceRankTermsRight p).value g ≤ 2 * mtKernel (gapDistance g p) ^ 2 := by
  intro p
  fin_cases p

  · exact source_model_right_0_valid hg

  · exact source_model_right_1_valid hg

  · exact source_model_right_2_valid hg

  · exact source_model_right_3_valid hg

  · exact source_model_right_4_valid hg

  · exact source_model_right_5_valid hg

  · exact source_model_right_6_valid hg

  · exact source_model_right_7_valid hg

  · exact source_model_right_8_valid hg

  · exact source_model_right_9_valid hg

  · exact source_model_right_10_valid hg

  · exact source_model_right_11_valid hg

  · exact source_model_right_12_valid hg

  · exact source_model_right_13_valid hg

  · exact source_model_right_14_valid hg


theorem source_rank_tangent_right :
    rankTangentLower sourceRankTermsRight targetB sourceRightBox
      sourceAnchorRight = (26036215021254826261948480423241409791537/2000000000000000000000000000000000000000000) := by
  norm_num [rankTangentLower, rankObjectiveRat, rankGradient,
    affineCoordinateLower, sourceRankTermsRight, sourceFloorRight,
    sourceAnchorRight, sourceAnchorCodes, targetB, sourceRightBox,
    MacroPrototype.macroPiece11, MacroPiece.box, macroPieceRankModel,
    wellRankModel, wellSlope, wellOffset, consecutiveCoeff, gapSupport,
    RankOneModel.valueRat, RankOneModel.dotRat,
    pairLeft, pairRight, Finset.sum_filter, Fin.sum_univ_succ,
    Fin.sum_univ_five]

theorem source_rank_tangent_check_right :
    rankTangentCheck targetA targetB sourceRightBox sourceAnchorRight
      sourceRankTermsRight = true := by
  have hordered : sourceRightBox.ordered = true := by
    rw [GapBox.ordered_iff]
    intro i
    fin_cases i <;> norm_num [sourceRightBox]
  have hanchor : ∀ i, sourceRightBox.lo i ≤ sourceAnchorRight i ∧
      sourceAnchorRight i ≤ sourceRightBox.hi i := by
    intro i
    fin_cases i <;> norm_num [sourceAnchorRight, sourceAnchorCodes, sourceRightBox]
  have hweights : ∀ p, 0 ≤ (sourceRankTermsRight p).weight := by
    intro p
    fin_cases p <;> norm_num [sourceRankTermsRight, sourceFloorRight,
      MacroPrototype.macroPiece11, macroPieceRankModel, wellRankModel, wellSlope, wellOffset]
  have hmargin : targetA ≤ rankTangentLower sourceRankTermsRight targetB
      sourceRightBox sourceAnchorRight := by
    rw [source_rank_tangent_right]
    norm_num [targetA]
  simp [rankTangentCheck, hordered, hanchor, hweights, hmargin]

theorem source_right_box_predicate :
    ∀ ⦃g : Fin 5 → ℝ⦄, sourceRightBox.Holds g →
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  exact rankTangentCheck_energy_sound source_rank_tangent_check_right
    (by
      intro g hg p
      exact source_models_right_pairwise_valid hg p)


theorem source_parent_box_predicate :
    ∀ ⦃g : Fin 5 → ℝ⦄, sourceParentBox.Holds g →
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  have hleft : BoxPredicate (fun g =>
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g)
      (sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← source_children_match_parent_split.1]
    exact source_left_box_predicate
  have hright : BoxPredicate (fun g =>
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g)
      (sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← source_children_match_parent_split.2]
    exact source_right_box_predicate
  exact boxPredicate_of_midpoint_children hleft hright

#print axioms source_children_match_parent_split
#print axioms source_left_box_predicate
#print axioms source_right_box_predicate
#print axioms source_parent_box_predicate

end A1294TwoQuadraticParent
