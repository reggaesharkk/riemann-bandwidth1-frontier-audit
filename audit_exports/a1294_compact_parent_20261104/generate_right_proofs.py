import json
from pathlib import Path
D=Path(__file__).resolve().parent
j=json.loads((D/'authentic_input.json').read_text())['children']['right']
s=(D/'AuthenticCompactRight.lean').read_text(encoding='utf-8-sig').split('set_option maxRecDepth 4000 in')[0]
s+='\nopen A1294GenericChecker\n'
out=[]
for t in j['fifteen_models']:
 i=t['pair_index_zero_based']; p=f'(⟨{i}, by decide⟩ : Fin 15)'
 out += [f'theorem canonical_{i} : compactRowCanonical row{i} = true := by decide']
 if t['kind']=='direct_piece':
  out += [f'theorem decode_{i} : interpCompactRow catalog row{i} = some (.direct macroPiece11) := by rfl']
  continue
 ss=t['segments'];floor=t['base'];lo,hi=t['distance_interval'];nm=f'segments{i}'
 out += [f'def {nm} : List SourceSegment := [\n'+',\n'.join(f'{{lo := ({x["segment"][0]}), hi := ({x["segment"][1]}), piece := {x["declaration"]}}}' for x in ss)+'\n]']
 out += [f'theorem decode_{i} : interpCompactRow catalog row{i} = some (.floor ({floor}) {nm}) := by' + (f'\n  change some (ModelRow.floor (interpRat ⟨0,1⟩) {nm}) = _\n  norm_num [interpRat]' if floor == '0' else ' rfl')]
 checks=[]
 for k,x in enumerate(ss):
  n=f'segment_{i}_{k}';checks.append(n)
  out += [f'theorem {n} : sourceSegmentCheck ({floor}) {{lo := ({x["segment"][0]}), hi := ({x["segment"][1]}), piece := {x["declaration"]}}} = true := by\n  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, {x["declaration"]}, MacroPiece.box]']
 out += [f'''theorem coverage_{i} : sourceCoverFrom ({lo}) ({hi}) {nm} = true := by
  norm_num [sourceCoverFrom, {nm}]
theorem piecewise_{i} : certifiedPiecewiseCheck ({lo}) ({hi}) ({floor}) {nm} = true := by
  have hlen : decide (0 < {nm}.length) = true := by norm_num [{nm}]
  have hall : {nm}.all (sourceSegmentCheck ({floor})) = true := by
    simp only [{nm}, List.all_cons, List.all_nil, {', '.join(checks)}, Bool.true_and]
  have hp : {nm}.all (fun s => s.piece.check) = true := by
    simp only [{nm}, List.all_cons, List.all_nil, {', '.join(dict.fromkeys(x['declaration']+'_check' for x in ss))}, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_{i}, hall, hp]
''']
# Exact source distance intervals
clauses=' '.join(f'| {i} => ⟨({t["distance_interval"][0]}), ({t["distance_interval"][1]})⟩' for i,t in enumerate(j['fifteen_models'][:-1]))
t=j['fifteen_models'][-1];clauses+=f' | _ => ⟨({t["distance_interval"][0]}), ({t["distance_interval"][1]})⟩'
out += [f'''def distances (p : Fin 15) : RatInterval := match p.val with {clauses}
theorem distances_exact : ∀ p, distanceInterval box p = distances p := by
  intro p
  fin_cases p <;> simp [distanceInterval, distances, gapSupport, pairLeft, pairRight, box, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num
''']
for t in j['fifteen_models']:
 i=t['pair_index_zero_based'];p=f'(⟨{i}, by decide⟩ : Fin 15)'
 out += [f'''theorem row_checked_{i} : compactRowCheck catalog box {p} row{i} = true := by
  simp only [compactRowCheck, canonical_{i}, decode_{i}, Bool.true_and, modelCheck]
  rw [distances_exact]
'''+('  rw [macroPiece11_check]\n  norm_num [distances, MacroPiece.box, macroPiece11]\n' if t['kind']=='direct_piece' else f'  exact piecewise_{i}\n')]
# tangent on the interpreted rows, after finite model normalization
floors=' '.join(f'| {i} => ({t["base"]})' for i,t in enumerate(j['fifteen_models'][:-1]))+f' | _ => ({j["fifteen_models"][-1]["base"]})'
out += [f'def floors (p : Fin 15) : ℚ := match p.val with {floors}', '''def terms (p : Fin 15) : RankOneModel :=
  if p.val = 1 then macroPieceRankModel (fun _ => macroPiece11) p
  else if p.val = 13 then macroPieceRankModel (fun _ => macroPiece11) p
  else {base := floors p, weight := 0, offset := 0, coeff := fun _ => 0}
''', 'theorem interpreted_terms : (fun p => interpModel (decodedRow catalog (rows p)) p) = terms := by\n  funext p\n  fin_cases p <;> simp [rows, decodedRow, '+', '.join(f'decode_{i}' for i in range(15))+', interpModel, terms, floors, interpRat]\n']
out += [f'''theorem tangent_lower : rankTangentLower terms (1094977/5000000000) box anchor = ({j['rank_tangent_lower']}) := by
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
''']
out += ['theorem all_rows : ∀ p, compactRowCheck catalog box p (rows p) = true := by\n  intro p\n  fin_cases p\n'+'\n'.join(f'  · exact row_checked_{i}' for i in range(15)), '''theorem accepted : compactQuadraticLeafCheck catalog (647/50000) (1094977/5000000000) box anchor rows = true := by
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
end AuthenticCompactRight
''']
(D/'CompositionalRight.lean').write_text(s+'\n'.join(out),encoding='utf-8')
print('source segments',sum(len(t['segments']) for t in j['fifteen_models']))



