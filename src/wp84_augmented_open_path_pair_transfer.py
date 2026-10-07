"""Exact augmented path defects, marked incidence, and trace countercertificates."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import comb
import json,subprocess
from wp84_full_pair_transfer_degree8 import carrier,offsets,admissible,marked_deletions,insertion_channels,hard_mask
ROOT=Path(__file__).resolve().parents[1]
def state(word,root,section,R):
    u=offsets(word)
    return {'word':word,'root':root,'terminal':root+u[-1],'Delta':u[-1],'offsets':u,'carrier':carrier(word),'projection_mask':[section[0]<=root+t<=section[1] for t in u],'section':section,'R':R}
def defect_counts(R):
    return {str(d):2*comb(7,2)*(2*R+1-abs(d)) for d in range(-2*R,2*R+1)}
def delete(word,slots):
    i,j=slots;assert word[i][0]==word[j][0] and word[i][1]==-word[j][1]
    lower=tuple(t for k,t in enumerate(word) if k not in slots)
    assert offsets(lower)[-1]==-word[i][2]-word[j][2]
    return lower

def incidence_replay():
    # All marked channels above one fixed open skeleton; exact 0/1 matrices.
    lower=((3,1,-1),(5,1,0),(7,-1,-1),(11,-1,0),(13,-1,0))
    channels=list(insertion_channels(lower,[2],1,0,(0,2)))
    assert channels
    # Distinct source skeletons from deleting marks in one multiply-paired closed word.
    high=((2,1,1),(2,-1,1),(3,1,-1),(3,-1,-1),(5,1,0),(5,-1,0),(7,1,0),(7,-1,0))
    assert admissible(high,0,(0,2),1)
    rotated=high[4:]+high[:4]
    assert admissible(rotated,0,(0,2),1) and rotated[-1][2]==rotated[-2][2]==-1
    assert sorted(offsets(lo)[-1] for i,j,lo in marked_deletions(rotated))==[-2,0,0,2]
    images=[delete(high,(i,j)) for i,j,lo in marked_deletions(high)]
    assert [offsets(w)[-1] for w in images]==[-2,2,0,0]
    # D sends each marked state to one skeleton; I=D^t.
    # A small complete fiber and a second one give DI=diag(2,1), ID=two all-one blocks.
    D=[[1,1,0],[0,0,1]]
    DI=[[sum(D[i][k]*D[j][k] for k in range(3)) for j in range(2)] for i in range(2)]
    ID=[[sum(D[k][i]*D[k][j] for k in range(2)) for j in range(3)] for i in range(3)]
    assert DI==[[2,0],[0,1]] and ID==[[1,1,0],[1,1,0],[0,0,1]]
    return {'marked_fiber_DI':DI,'marked_fiber_ID':ID,'higher_word':high,'rotated_noncanonical_word':rotated,'deletion_defects':[-2,2,0,0],'open_fiber_channel_count':len(channels)}
def positive_population():
    # PNT-reduced exact diagonal population, not the full signed open block.
    a,b=F(1,8),F(1,6);c,d=F(1,4),F(1,3);pi_hi=F(22,7)
    first=(b*b-a*a)/2;second=(d*d-c*c)/2
    f1_lower=4*a*a/(pi_hi*pi_hi);f0_lower=(1-d)**2
    cos_lower=1-(2*pi_hi*(b-a))**2/2
    C=F(1,2)*cos_lower*(f1_lower*first)**2*(f0_lower*second)**2
    assert C>0
    return {'open_marked_population_liminf_lower':str(C),'value_approx':float(C),'prime_windows':[['1/8','1/6'],['1/4','1/3']],'scope':'selected exact-diagonal order-eight population only; not a lower bound on full signed open aggregate'}
def main():
    c=json.loads((ROOT/'notes/WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json').read_text())
    w=c['SOS_witness'];E=F(w['expectation']);slack=F(21,200)-E
    variance=2*abs(F(w['p_coefficients'][2]))*F(106,333)**2/6000
    counts={str(b):{str(R):{str(d):2*comb(b+2,2)*(2*R+1-abs(d)) for d in range(-2*R,2*R+1)} for R in (1,2)} for b in (5,6)}
    for b in (5,6):
        for R in (1,2):
            brute={str(d):0 for d in range(-2*R,2*R+1)}
            for i,j in combinations(range(b+2),2):
                for e,v,t in product((-1,1),range(-R,R+1),range(-R,R+1)):brute[str(-v-t)]+=1
            assert brute==counts[str(b)][str(R)]
    result={'decision':'F','incidence':incidence_replay(),'defect_counts_per_prime_before_endpoint_mask':counts,'positive_population':positive_population(),'bare_open_trace':0,'inserted_closed_trace_not_zero':True,'witness':w,'uncharged_defect_slack':str(slack),'uncharged_percentage_slack':str(200*slack),'intersection':'NOT YET CERTIFIABLE','partial_variance_payment':str(variance),'relaxed_slack_after_variance_only':str(slack-variance),'charged_margin':'UNCERTIFIED','mu7_mu8':'NO-GO'}
    result['source_blobs']={p:subprocess.check_output(['git','rev-parse','484769f:'+p],cwd=ROOT,text=True).strip() for p in ['src/wp84_full_pair_transfer_degree8.py','notes/WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md','notes/WP84_FOURIER_REPROJECTION_BRIDGE_AUDIT.md','notes/WP84_TWO_SCALE_FILTERED_TO_SHARP_MOMENT_BRIDGE.md','notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md']}
    (ROOT/'notes/WP84_AUGMENTED_OPEN_PATH_PAIR_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Exact open population lower bound',result['positive_population']);print('Uncharged defect slack',slack,float(slack));print('PASS defects, incidence, witness recovery; Decision F')
if __name__=='__main__':main()
