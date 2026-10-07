"""Physical slot twists, finite character masks, and explicit unpaid extraction norm."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial
import json,subprocess
from wp84_full_pair_transfer_degree8 import carrier,offsets,admissible
ROOT=Path(__file__).resolve().parents[1]
def partitions(a):
    if not a:yield ();return
    head=a[0]
    for p in partitions(a[1:]):
        yield ((head,),)+p
        for i in range(len(p)):yield p[:i]+((head,)+p[i],)+p[i+1:]
def distinct_projector(labels):
    value=0;cost=0
    for pi in partitions(tuple(range(len(labels)))):
        mu=1
        for block in pi:mu*=(-1)**(len(block)-1)*factorial(len(block)-1)
        equal=all(len({labels[i] for i in block})==1 for block in pi)
        value+=mu*int(equal);cost+=abs(mu)
    return value,cost
def character_projection(value,target,q):
    # Exact roots-of-unity orthogonality, avoiding numerical complex roots.
    return int((value-target)%q==0)
def displacement_kernel(labels):
    return [(d,d%5) for d in labels]
def mask_lag_projection(lag,target,R):
    q=2*R+1
    return int(all((a-b)%q==0 for a,b in zip(lag[:-1],target[:-1])) and sum(lag)==0)
def exp_bounds(x,K=80):
    x=F(x);term=F(1);total=term
    for n in range(1,K+1):term*=x/n;total+=term
    next_term=term*x/(K+1);ratio=x/(K+2)
    assert ratio<1
    return total,total+next_term/(1-ratio)

def physical_prime_matrix(primes,L,T,I,R,phase=None):
    """Actual finite-band prime matrix; coefficient phase preserves Hermitian pairing."""
    import numpy as np
    from math import log,pi,sqrt
    phase=phase or {};A=np.zeros((len(I),len(I)),complex)
    for p in primes:
        alpha=log(p)/L;cp=-log(p)/(L*sqrt(p))
        for e in (-1,1):
            for i,r in enumerate(I):
                for j,v in enumerate(I):
                    lag=v-r
                    if abs(lag)>R:continue
                    f=1-alpha if lag==0 else (1-np.exp(e*2j*pi*lag*alpha))/(e*2j*pi*lag)
                    A[i,j]+=cp*f*np.exp(1j*e*((T+2*pi*r/L)*log(p)+phase.get(p,0)))
    return A

def main():
    for n in (2,3,4):
        for labels in product(range(3),repeat=n):
            v,c=distinct_projector(labels);assert v==int(len(set(labels))==n) and c==factorial(n)
    for R in (1,2):
        for a,b in product(range(-R,R+1),repeat=2):assert character_projection(a,b,2*R+1)==int(a==b)
    lower=((379,1,0),(401,1,0),(47,-1,0),(53,-1,0),(61,-1,0))
    M=((5,1,1),(5,-1,1),(379,1,-1),(401,1,0),(47,-1,-1),(53,-1,0),(61,-1,0))
    C=((5,1,1),(379,1,-1),(5,-1,1),(401,1,-1),(47,-1,0),(53,-1,0),(61,-1,0))
    assert carrier(M)==carrier(C) and admissible(M,5,(0,30),1) and admissible(C,5,(0,30),1)
    assert -M[0][2]-M[1][2]==-C[0][2]-C[2][2]==-2
    assert mask_lag_projection([x[2] for x in M],[x[2] for x in M],1)==1
    assert mask_lag_projection([x[2] for x in C],[x[2] for x in M],1)==0
    w=json.loads((ROOT/'notes/WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json').read_text())['SOS_witness']
    c7=F(w['p_coefficients'][7]);Craw=F(24);B=F(14157,2401);pairlo=F(343,8921088)
    Chard=Craw*2*B/pairlo/abs(c7)
    ideal=F(27704610381502,17886179119921875);relaxed=F(52897896569489,572357731837500000)
    assert exp_bounds(F(5,4))[1]<5<exp_bounds(F(5,3))[0]
    assert exp_bounds(F(11,2))[1]<379 and exp_bounds(F(13,2))[0]>401
    assert exp_bounds(F(7,2))[1]<47 and exp_bounds(F(9,2))[0]>61
    assert exp_bounds(6)[0]>401 and exp_bounds(10)[1]<22027
    assert F(44,7)*22027*F(28,151951)<32
    result={'physical_prime_atom':{'L':10,'T':'2*pi*exp(10)','primes':[5,379,401,47,53,61],'H':32,'central_window_certified':True,'all_leaves_below_natural_cutoff':True,'root_amplitude_nonzero':True,'scope':'realizable single auxiliary root/word correlation, not an untwisted full-block cancellation counterexample'},'decision':'F','Delta_only_counterexample':{'M':M,'competitor':C,'Delta':-2,'carrier_equal':True,'character_measurement_rank':1,'mask_augmented_rank':2},'slot_lag_projector':{'q':'2R+1','angles':'theta_j=2*pi*k_j/q','norm':1,'R6000_samples_per_order7_lag_mask':12001**6},'pair_equality_projector':{'physical_operation':'shared independent prime coefficient phases on the two selected slots','q':3,'norm':1,'finite_family_size':'3^(number of allowed pair primes), T dependent'},'distinctness_mobius_norms':{'2':2,'3':6,'4':24},'raw_order7_mask_norm_bound':str(Craw),'hard_trimmed_inverse_norm_bound_consumer_scaled':str(Chard),'degree6_ideal_slack_comparison_only':str(ideal),'degree6_relaxed_slack_comparison_only':str(relaxed),'uniform_aux_error_needed_for_ideal_comparison':str(ideal/Chard),'uniform_aux_error_needed_for_relaxed_comparison':str(relaxed/Chard),'paid_degree8_budget':'UNCERTIFIED','physical_natural_subspace_kernel':'UNCERTIFIED; actual family is nonlinear','physical_aux_linear_span':'finite character reconstruction exists at fixed T; arithmetic-only','full_cancellation_coefficient':'UNCERTIFIED','R6000_diagonal':'UNEVALUATED','mu7_mu8':'DEFERRED','strict_gt79':'OPEN'}
    result['parent']='876188d9f67cf8de5b3a15f6ed60b9ab3ea37596'
    files=['src/wp84_open_path_hardness_transfer.py','src/wp84_repaired_open_diagonal.py','notes/WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json']
    result['source_blobs']={p:subprocess.check_output(['git','rev-parse','876188d:'+p],cwd=ROOT,text=True).strip() for p in files}
    (ROOT/'notes/WP84_PHYSICAL_MASK_TWIST_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS finite character masks and exact Mobius norms');print('Hard extraction upper constant',float(Chard));print('Ideal comparison error ceiling',float(ideal/Chard));print('Relaxed comparison error ceiling',float(relaxed/Chard))
if __name__=='__main__':main()
