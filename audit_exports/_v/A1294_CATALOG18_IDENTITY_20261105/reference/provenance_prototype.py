from pathlib import Path
import json,hashlib,re
from vrk.canonical import digest_object,sha256_file
from vrk.evidence import evidence_root
D=Path(__file__).resolve().parent
records=json.loads((D/'leaf_data_summary.json').read_text())['catalog_declarations']
if len(records)!=171:raise ValueError('catalog cardinality')
source_text=(D/'Catalog18Lookup.lean').read_text(encoding='utf-8')
def entries(name):
 m=re.search(r'def '+name+r' : Array MacroPiece := #\[([^\n]*)\]',source_text)
 if not m: raise ValueError('missing array '+name)
 return m.group(1).split(', ')
if entries('original')!=records or sum((entries('block'+str(i)) for i in range(3)),[])!=records:raise ValueError('source catalog order mismatch')
pred='09de5506c416dfded56a5bc979f7cb776d05df2285d1f98f9565e071bccfea23'
claim={'schema':'a1294-vrk-style-contract-v1','proposition':'For the newly blocked 171-element catalog, catalog[0]? = some refinementPiece3','status':'KERNEL_PROVED','theorem':'Catalog18.lookup0','axioms':['propext','Classical.choice','Quot.sound'],'source_authentication':'EXTERNALLY_CHECKED','original_catalog_correspondence':'INCOMPLETE','root_predicate':'INCOMPLETE','predecessor_sha256':pred,'v2_sha256':'3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5','vrk_release_sha256':'c18c4c697d8188490e96530cfb5ddcb2e63f7c65aa560415401b1541e575cd79','lean_commit':'d8b18978322de05a8f3dba51ef03cf5461676c17','upstream_commit':'fba91d214655aaa1fd0504bb893c8859c20c79f9','mathlib_commit':'51e6992efd06126df61a496bebf8f49482a4e129','source_sha256':sha256_file(D/'Catalog18Lookup.lean'),'object_sha256':sha256_file(D/'Catalog18Lookup.olean'),'catalog_sequence_digest':digest_object(records),'evidence_root':evidence_root([{'role':'proof','path':'Catalog18Lookup.lean','sha256':sha256_file(D/'Catalog18Lookup.lean')},{'role':'object','path':'Catalog18Lookup.olean','sha256':sha256_file(D/'Catalog18Lookup.olean')}]),'boundary':'VRK evidence roots bind metadata; no native VRK Lean verifier or signed external trust anchor is asserted.'}
source_ledger=json.loads((D/'authentic_input.json').read_text(encoding='utf-8'))
claim['source_stream_sha256']=source_ledger['source_stream_sha256']
claim['source_catalog_sha256']=source_ledger['source_input_sha256']
expected=claim['catalog_sequence_digest'];tests={'entry_mutation':records.copy(),'index_shift':records[1:]+records[:1],'reorder':records.copy(),'duplicate':records.copy(),'truncation':records[:-1]};tests['entry_mutation'][0]+='_changed';tests['reorder'][0],tests['reorder'][1]=tests['reorder'][1],tests['reorder'][0];tests['duplicate'][1]=tests['duplicate'][0]
results={k:('REJECTED' if digest_object(v)!=expected else 'UNEXPECTED_MATCH') for k,v in tests.items()};source=D/'reference/predecessor.zip'
if sha256_file(source)!=pred:raise RuntimeError('predecessor bytes do not match frozen digest')
def source_hash_accepted(payload): return hashlib.sha256(payload).hexdigest() == pred
real=source.read_bytes()
if not source_hash_accepted(real):raise RuntimeError('original source rejected')
mutated=bytes([real[0]^1])+real[1:]
results['mismatched_source_hash']='REJECTED' if not source_hash_accepted(mutated) else 'UNEXPECTED_MATCH'
if any(v!='REJECTED' for v in results.values()):raise RuntimeError(results)
(D/'claim_evidence.json').write_text(json.dumps(claim,indent=2));(D/'mutation_results.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
