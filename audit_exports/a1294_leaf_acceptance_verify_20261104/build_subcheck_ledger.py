import json,re
from pathlib import Path
D=Path(__file__).resolve().parent
s=(D/'CompositionalLeaf_failed_v1.lean').read_text(encoding='utf-8-sig')
records=[]
failed={'decode_6','decode_10','row_checked_1','row_checked_13'}
dependent={'interpreted_terms','all_rows','accepted','row_checked_6','row_checked_10'}
for m in re.finditer(r'theorem (\w+) :([\s\S]*?) := by',s):
 name,expr=m.groups()
 if not name.startswith(('canonical_','decode_','segment_','coverage_','piecewise_','row_checked_','distances_exact','interpreted_terms','tangent_','all_rows','accepted')):continue
 records.append({'name':name,'exact_expression':expr.strip(),'compiler_status': 'FAILED_LOCAL_PROOF' if name in failed else 'DEPENDS_ON_FAILED_DECLARATION' if name in dependent else 'NO_ERROR_REPORTED_IN_FAILED_MODULE','clean_module_verified':False,'boolean_false_established':False,'corrected_build_status':'NO_LEAN_RESULT_WSL_SERVICE_TIMEOUT'})
for name,expr in [('first_floor_canonical','(CompactRat.mk 5170581624709583018970186520240204081 3200000000000000000000000000000000000000).check = true'),('first_catalog_ref','catalog[0]? = some refinementPiece3'),('first_segment_decode','interpSegment catalog {lo := ⟨405,64⟩, hi := ⟨253223,40000⟩, pieceRef := 0} = some {lo := 405/64, hi := 253223/40000, piece := refinementPiece3}')]:
 records.append({'name':name,'exact_expression':expr,'compiler_status':'KERNEL_CHECKED_IN_CLEAN_CHECKPOINT_MODULE','clean_module_verified':True,'equality_obtained':True,'support':'checkpoints.log'})
(D/'subcheck_ledger.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(len(records),'subcheck records')
