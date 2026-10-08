"""Independent descriptor, jet-basis, and deliberate-corruption replay."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import json, math, copy
ROOT=Path(__file__).resolve().parents[1]
FUNCS=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
IDS=[[15,20,26,28,31,32],[10,12,16,17,21,22,25,29],[36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69],[34,37,39,43,53,56,60,63]]
HMAX={15:6,10:6,36:8,34:6}
EXPECTED={15:{31,32},10:{16,17,21,22,25,29},36:{47,49,50,62,65,69},34:{37,39,43,56,60,63}}

def decode(fid):
 f=FUNCS[fid]; pi=tuple(map(int,f['equality_partition'].split(','))); eps=tuple(1 if x=='+' else -1 for x in f['sign_word']);nu=tuple(pi.count(k) for k in range(max(pi)+1)); e=tuple(sum(eps[s] for s in range(5) if pi[s]==k) for k in range(len(nu)))
 ex=next(k for k in range(len(nu)) if nu[k]>abs(e[k]))
 return {'id':fid,'pi':pi,'eps':eps,'nu':nu,'e':e,'ex':ex,'hidden':e[ex]==0,'pair':tuple(s for s in range(5) if pi[s]==ex)}

def expected_basis():
 blocks=[]
 all_coords=set()
 for ids in IDS:
  hidden=[decode(i) for i in ids if decode(i)['hidden']]
  pairs=defaultdict(list)
  for d in hidden:pairs[d['pair']].append(d['id'])
  h=HMAX[ids[0]]; coords={(p,j) for p in pairs for j in range(2,3+h)};all_coords|=coords
  blocks.append({'ids':ids,'hidden':sorted(d['id'] for d in hidden),'visible':sorted(i for i in ids if not decode(i)['hidden']),'hmax':h,'pairs':{str(p):sorted(v) for p,v in pairs.items()},'coordinates':coords})
 return blocks,all_coords

def validate(cert):
 errors=[]
 if cert.get('R')!=6000:errors.append('R changed')
 if cert.get('prime_range')!='all source-admissible ordinary primes q<=N(T)':errors.append('full q-range replaced')
 if cert.get('section_dimension')!='source-selected dprime with dprime/d->1':errors.append('source section replaced')
 if cert.get('mask_signature_policy')!='preserve exact source chi; no unproved mask merging':errors.append('source mask signatures merged or changed')
 if cert.get('all_hidden_moments_zero'):errors.append('hidden moments forced to zero')
 if cert.get('first_possible_deficit')!='m-1':errors.append('first possible section deficit changed')
 if cert.get('delta_formula')!='sum_k a_k det(ones-row at k, first-subleading rows elsewhere)':errors.append('first section coefficient perturbed')
 blocks,coords=expected_basis(); got=set(tuple(x) for x in cert.get('moment_coordinates',[]))
 if got!=coords:errors.append('hidden q moment deleted, exponent altered, or coordinates misclassified')
 if cert.get('visible_as_hidden'):errors.append('visible repeated-prime layout misclassified as hidden')
 if cert.get('q_pool')=='[2,3,5,7,11,13]':errors.append('full q-range replaced by six-prime core')
 if cert.get('section_n')==2:errors.append('large section replaced by d=2')
 return errors

def main():
 blocks,coords=expected_basis()
 assert [len(b['hidden']) for b in blocks]==[2,6,6,6]
 assert [len(b['visible']) for b in blocks]==[4,2,10,2]
 assert len(coords)==73
 # Independently reconstruct coefficients of the q-local factor for simple exact cases.
 # For l_s=l_t=0 and A=0: only k=0,1,2 survive, with coefficients 1,-2,1.
 def local_coeff(h):
  out=Q(0)
  for a in range(h+1):
   for b in range(h-a+1):
    c=h-a-b
    ga=Q(1) if a==0 else (Q(-1) if a==1 else Q(0))
    gb=Q(1) if b==0 else (Q(-1) if b==1 else Q(0))
    out+=ga*gb*(Q(1) if c==0 else Q(0))
  return out
 assert [local_coeff(h) for h in range(5)]==[Q(1),Q(-2),Q(1),Q(0),Q(0)]
 base={'R':6000,'prime_range':'all source-admissible ordinary primes q<=N(T)','section_dimension':'source-selected dprime with dprime/d->1','mask_signature_policy':'preserve exact source chi; no unproved mask merging','all_hidden_moments_zero':False,'first_possible_deficit':'m-1','delta_formula':'sum_k a_k det(ones-row at k, first-subleading rows elsewhere)','moment_coordinates':[list(x) for x in sorted(coords)],'visible_as_hidden':False,'q_pool':'complete','section_n':'source-selected'}
 assert validate(base)==[]
 mutations=[]
 tests=[('misclass visible repeated prime',lambda x:x.update(visible_as_hidden=True)),('delete one hidden moment',lambda x:x['moment_coordinates'].pop()),('alter log exponent',lambda x:x['moment_coordinates'].__setitem__(0,[x['moment_coordinates'][0][0],x['moment_coordinates'][0][1]+1])),('force hidden moments zero',lambda x:x.update(all_hidden_moments_zero=True)),('six-prime q range',lambda x:x.update(q_pool='[2,3,5,7,11,13]')),('d=2 section',lambda x:x.update(section_n=2)),('change R',lambda x:x.update(R=5999)),('perturb Delta',lambda x:x.update(delta_formula='perturbed'))]
 for name,mut in tests:
  bad=copy.deepcopy(base);mut(bad);assert validate(bad),name;mutations.append(name)
 out={'decision':'F','hidden_layout_counts':[2,6,6,6],'visible_layout_counts':[4,2,10,2],'mask-merged_structural_moment_coordinates':len(coords),'coordinates':[list(x) for x in sorted(coords)],'q_local_coefficient_check':'PASS: l_s=l_t=A=0 gives kappa_0..4 = 1,-2,1,0,0','corruption_tests_rejected':mutations,'source_mask_merge_status':'not certified','correction_matrix_ranks':'unknown','first_nonzero_section_coefficient':'unknown; first possible deficit m-1 recorded separately','certified_rank_per_block':[1,1,1,1]}
 (ROOT/'notes/WP84_HIDDEN_PRIME_MOMENT_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS 20 hidden / 18 visible descriptors; 73 conditional moment coordinates; eight corruptions rejected')
if __name__=='__main__':main()
