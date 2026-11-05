from pathlib import Path
from fractions import Fraction as F
import json,hashlib
D=Path(__file__).resolve().parent
j=json.loads((D/'authentic_input.json').read_text())['children']['left']
if hashlib.sha256((D/'authentic_input.json').read_bytes()).hexdigest()!='9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072':raise RuntimeError('source ledger')
ref=(D/'GenericReference.lean').read_text(encoding='utf-8-sig')
generic_prefix=ref.split('def decodedRow')[0]
checked_decoder='def compactRowCheck ('+ref.split('def compactRowCheck (')[1].split('theorem compactRowCheck_sound')[0]
core=generic_prefix+checked_decoder
core+='''
end A1294FifteenBridge
namespace IndependentEngine
open A1294GenericChecker A1294Compact A1294FifteenBridge
theorem segmentCheck_mono {a b : ℚ} {s : SourceSegment}
    (hab : a ≤ b) (h : sourceSegmentCheck b s = true) : sourceSegmentCheck a s = true := by
  simp only [sourceSegmentCheck, decide_eq_true_eq] at h ⊢
  exact ⟨h.1, h.2.1, h.2.2.1, le_trans hab h.2.2.2⟩
structure SegmentRef where
  lo : Nat
  hi : Nat
  cat : Nat
inductive RowRef where
  | direct (cat : Nat)
  | floor (q : Nat) (segments : List Nat)
def decodeSegment (qs : Array CompactRat) (ss : Array SegmentRef)
    (catalog : Array MacroPiece) (i : Nat) : Option CompactSegment := do
  let s ← ss[i]?
  let lo ← qs[s.lo]?
  let hi ← qs[s.hi]?
  let _ ← catalog[s.cat]?
  return {lo := lo, hi := hi, pieceRef := s.cat}
def decodeRow (qs : Array CompactRat) (ss : Array SegmentRef)
    (catalog : Array MacroPiece) : RowRef → Option CompactRow
  | .direct i => do
      let _ ← catalog[i]?
      return .direct i
  | .floor q ids => do
      let v ← qs[q]?
      let segs ← ids.mapM (decodeSegment qs ss catalog)
      return .floor v segs
def explicitLeafCheck (catalog : Array MacroPiece) (A B : ℚ)
    (box : GapBox) (anchor : Fin 5 → ℚ)
    (rows : Fin 15 → CompactRow) (models : Fin 15 → ModelRow) : Bool :=
  decide (∀ p, compactRowCheck catalog box p (rows p) = true) &&
    rankTangentCheck A B box anchor (fun p => interpModel (models p) p)
theorem explicitLeafCheck_sound {catalog : Array MacroPiece} {A B : ℚ}
    {box : GapBox} {anchor : Fin 5 → ℚ} {rows : Fin 15 → CompactRow}
    {models : Fin 15 → ModelRow}
    (success : ∀ p, interpCompactRow catalog (rows p) = some (models p))
    (h : explicitLeafCheck catalog A B box anchor rows models = true) :
    ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →
      (A : ℝ) ≤ sextupleEnergy g + (B : ℝ) * sextupleSpan g := by
  simp only [explicitLeafCheck, Bool.and_eq_true, decide_eq_true_eq] at h
  apply rankTangentCheck_energy_sound h.2
  intro g hg p
  have hp := h.1 p
  simp only [compactRowCheck, success p, Bool.and_eq_true] at hp
  exact modelCheck_sound hp.2 hg
#print axioms explicitLeafCheck_sound
end IndependentEngine
'''
(D/'StandaloneCore.lean').write_text(core,encoding='utf-8')
rats=set();cats=[];segs={}
def q(x):
 f=F(x);rats.add(f);return f
for t in j['fifteen_models']:
 q(t['base'])
 if t['kind']=='direct_piece':
  n='macroPiece'+str(t['direct_catalog_index'])
  if n not in cats:cats.append(n)
 else:
  for x in t['segments']:
   key=(q(x['segment'][0]),q(x['segment'][1]),x['declaration'])
   segs[key]=max(segs.get(key,F(t['base'])),F(t['base']))
   if x['declaration'] not in cats:cats.append(x['declaration'])
rats=sorted(rats);qi={x:i for i,x in enumerate(rats)};keys=sorted(segs);si={x:i for i,x in enumerate(keys)}
def qr(x):return f'q{qi[F(x)]}'
S=['''import StandaloneCore
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
open A1294GenericChecker A1294Compact A1294FifteenBridge IndependentEngine
noncomputable section
namespace IndependentTerminal22
set_option maxRecDepth 6000
set_option maxHeartbeats 2000000
''']
for i,f in enumerate(rats):S+=[f'def q{i} : CompactRat := ⟨({f.numerator}),{f.denominator}⟩']
S+=['def qs : Array CompactRat := #['+','.join('q'+str(i) for i in range(len(rats)))+']','def catalog : Array MacroPiece := #['+','.join(cats)+']']
S+=['def segmentRefs : Array SegmentRef := #['+','.join(f'⟨{qi[a]},{qi[b]},{cats.index(c)}⟩' for a,b,c in keys)+']']
for k,(a,b,c) in enumerate(keys):
 S += [f'def c{k} : CompactSegment := {{lo := {qr(a)}, hi := {qr(b)}, pieceRef := {cats.index(c)}}}',f'def s{k} : SourceSegment := {{lo := interpRat {qr(a)}, hi := interpRat {qr(b)}, piece := {c}}}',f'''theorem maxcheck_{k} : sourceSegmentCheck ({segs[(a,b,c)]}) s{k} = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s{k}, {qr(a)}, {qr(b)}, interpRat, {c}, MacroPiece.box]
''']
for t in j['fifteen_models']:
 i=t['pair_index_zero_based'];floor=qr(t['base'])
 if t['kind']=='direct_piece':
  S += [f'def wire{i} : RowRef := .direct {cats.index("macroPiece11")}',f'def row{i} : CompactRow := .direct {cats.index("macroPiece11")}',f'def model{i} : ModelRow := .direct macroPiece11']
 else:
  ids=[si[(F(x['segment'][0]),F(x['segment'][1]),x['declaration'])] for x in t['segments']]
  S += [f'def wire{i} : RowRef := .floor {qi[F(t["base"])]} ['+','.join(map(str,ids))+']',f'def row{i} : CompactRow := .floor {floor} ['+','.join('c'+str(k) for k in ids)+']',f'def segments{i} : List SourceSegment := ['+','.join('s'+str(k) for k in ids)+']',f'def model{i} : ModelRow := .floor (interpRat {floor}) segments{i}']
  proofs=[]
  for k in dict.fromkeys(ids):
   n=f'rowseg_{i}_{k}';proofs.append(n)
   S += [f'theorem {n} : sourceSegmentCheck (interpRat {floor}) s{k} = true :=\n  segmentCheck_mono (by norm_num [interpRat, {floor}]) maxcheck_{k}']
  lo,hi=t['distance_interval']; defs=', '.join('s'+str(k) for k in dict.fromkeys(ids));qs=', '.join(dict.fromkeys(qr(v) for k in ids for v in keys[k][:2]));pieces=', '.join(dict.fromkeys(keys[k][2]+'_check' for k in ids))
  S += [f'''theorem coverage_{i} : sourceCoverFrom ({lo}) ({hi}) segments{i} = true := by
  norm_num [sourceCoverFrom, segments{i}, {defs}, {qs}, interpRat]
theorem piecewise_{i} : certifiedPiecewiseCheck ({lo}) ({hi}) (interpRat {floor}) segments{i} = true := by
  have hn : decide (0 < segments{i}.length) = true := by norm_num [segments{i}]
  have hs : segments{i}.all (sourceSegmentCheck (interpRat {floor})) = true := by
    simp only [segments{i}, List.all_cons, List.all_nil, {', '.join(proofs)}, Bool.true_and]
  have hp : segments{i}.all (fun s => s.piece.check) = true := by
    simp only [segments{i}, {defs}, List.all_cons, List.all_nil, {pieces}, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_{i}, hs, hp]
''']
 S += [f'theorem wire_success_{i} : decodeRow qs segmentRefs catalog wire{i} = some row{i} := by rfl',f'theorem model_success_{i} : interpCompactRow catalog row{i} = some model{i} := by rfl',f'theorem canonical_{i} : compactRowCanonical row{i} = true := by decide']
def choose(name,typ,vals):return f'def {name} (p : Fin 15) : {typ} := match p.val with '+' '.join(f'| {i} => {v}' for i,v in enumerate(vals[:-1]))+' | _ => '+vals[-1]
S += [choose('rows','CompactRow',['row'+str(i) for i in range(15)]),choose('models','ModelRow',['model'+str(i) for i in range(15)]),choose('wireRows','RowRef',['wire'+str(i) for i in range(15)])]
b=j['box_exact'];S+=['def box : GapBox where\n  lo := fun i => match i.val with '+' '.join(f'| {i} => ({x[0]})' for i,x in enumerate(b[:-1]))+' | _ => ('+b[-1][0]+')\n  hi := fun i => match i.val with '+' '.join(f'| {i} => ({x[1]})' for i,x in enumerate(b[:-1]))+' | _ => ('+b[-1][1]+')','def anchor : Fin 5 → ℚ := box.lo']
S += [choose('distances','RatInterval',[f'⟨({t["distance_interval"][0]}),({t["distance_interval"][1]})⟩' for t in j['fifteen_models']]),'''theorem distances_exact : ∀ p, distanceInterval box p = distances p := by
  intro p
  fin_cases p <;> simp [distanceInterval, distances, gapSupport, pairLeft, pairRight, box, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num
''']
for t in j['fifteen_models']:
 i=t['pair_index_zero_based']
 S += [f'''theorem row_checked_{i} : compactRowCheck catalog box (⟨{i}, by decide⟩ : Fin 15) row{i} = true := by
  simp only [compactRowCheck, canonical_{i}, model_success_{i}, Bool.true_and, model{i}, modelCheck]
  rw [distances_exact]
'''+('  rw [macroPiece11_check]\n  norm_num [distances, MacroPiece.box, macroPiece11]' if t['kind']=='direct_piece' else f'  exact piecewise_{i}')]
S += [choose('floors','ℚ',['interpRat '+qr(t['base']) for t in j['fifteen_models']]),'''def terms (p : Fin 15) : RankOneModel :=
  if p.val = 1 then macroPieceRankModel (fun _ => macroPiece11) p
  else if p.val = 13 then macroPieceRankModel (fun _ => macroPiece11) p
  else {base := floors p, weight := 0, offset := 0, coeff := fun _ => 0}
theorem interpreted_terms : (fun p => interpModel (models p) p) = terms := by
  funext p
  fin_cases p <;> rfl
''']
old=(D/'baseline/Zeta23/ThmD/Sextuple/CompositionalLeaf.lean').read_text(encoding='utf-8-sig')
tangent='theorem tangent_lower'+old.split('theorem tangent_lower')[1].split('theorem all_rows')[0]
tangent=tangent.replace('floors,','floors, interpRat, '+', '.join(dict.fromkeys(qr(t['base']) for t in j['fifteen_models']))+',')
S += [tangent]
for name,typ,expr,prefix in [('wire_success','decodeRow qs segmentRefs catalog (wireRows p) = some (rows p)','', 'wire_success_'),('model_success','interpCompactRow catalog (rows p) = some (models p)','','model_success_'),('all_rows','compactRowCheck catalog box p (rows p) = true','','row_checked_')]:
 S += [f'theorem {name} : ∀ p, {typ} := by\n  intro p\n  fin_cases p\n'+'\n'.join('  · exact '+prefix+str(i) for i in range(15))]
S += ['''theorem accepted : explicitLeafCheck catalog (647/50000) (1094977/5000000000) box anchor rows models = true := by
  unfold explicitLeafCheck
  rw [interpreted_terms]
  simp [all_rows, tangent_checked]
theorem leaf_sound : ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=
  explicitLeafCheck_sound model_success accepted
#print axioms wire_success
#print axioms model_success
#print axioms all_rows
#print axioms tangent_checked
#print axioms accepted
#print axioms leaf_sound
#print leaf_sound
end IndependentTerminal22
''']
(D/'StandaloneTerminal22.lean').write_text('\n'.join(S),encoding='utf-8')
summary={'rational_records':len(rats),'unique_segments':len(keys),'segment_occurrences':sum(len(t['segments']) for t in j['fifteen_models']),'catalog_records':len(cats),'row_records':15,'unique_checks':len(keys),'max_floor_source':'maximum of unchanged source row floors sharing each exact segment; monotonicity proved generically'}
(D/'data_summary.json').write_text(json.dumps(summary,indent=2));print(summary)
payload={'version':'A1294Independent/1','terminal':22,'node':66,'q':[[f.numerator,f.denominator] for f in rats],'catalog':cats,'segments':[[qi[a],qi[b],cats.index(c)] for a,b,c in keys],'rows':[],'box':j['box_exact'],'anchor':j['anchor_coordinates_exact'],'A':j['A'],'B':j['B']}
for t in j['fifteen_models']:
 if t['kind']=='direct_piece':payload['rows'].append([0,cats.index('macroPiece'+str(t['direct_catalog_index']))])
 else:payload['rows'].append([1,qi[F(t['base'])],[si[(F(x['segment'][0]),F(x['segment'][1]),x['declaration'])] for x in t['segments']]])
(D/'data_certificate.json').write_text(json.dumps(payload,sort_keys=True,separators=(',',':')))
