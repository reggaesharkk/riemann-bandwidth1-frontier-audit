"""Certificate verifier with independent replay and literal mutation rejection."""
from pathlib import Path
import json,copy
import wp84_fifth_shared_block_replay as replay
ROOT=Path(__file__).resolve().parents[1]
def validate(c):
 assert c['old_fifth_lower']==20 and c['new_dimensions']==9
 assert c['new_fifth_lower']==len(set(c['witness_ids']))==29
 assert len(c['remaining_blocks'])==7
 pairs={tuple(p['ids']):p for p in c['pair_coefficients']}
 assert pairs[(5,7)]['order']==11 and pairs[(5,7)]['coefficient']=='parent exact coefficient'
 for p in c['pair_coefficients']:assert p['coefficient']!='0'
 assert c['global_kernel_vectors']==[] and c['mixed_intersection'] is None
 for p,h in c['source_sha256'].items():
  import hashlib
  assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h

def main():
 c=json.loads((ROOT/'notes/WP84_FIFTH_SHARED_RANK_WITNESS.json').read_text());validate(c)
 bad=copy.deepcopy(c);next(p for p in bad['pair_coefficients'] if p['ids']==[5,7])['coefficient']='0'
 try:validate(bad)
 except AssertionError:pass
 else:raise AssertionError('forced zero was accepted')
 replay.main();print('PASS certificate and independent replay')
if __name__=='__main__':main()
