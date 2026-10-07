"""Complete small finite-band amplitude replay, numerical algebra only.
No natural-height or R6000 arithmetic bound is inferred.
"""
from pathlib import Path
import json
from math import log,pi,sqrt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def main():
    primes=(2,3,5);L=7.;I=tuple(range(2,6));R=1;T=13.;d=len(I)
    components=[]
    for k,p in enumerate(primes):
        alpha=log(p)/L;cp=-log(p)/(L*sqrt(p))
        for e in (-1,1):
            key=tuple(e if j==k else 0 for j in range(3));M=np.zeros((d,d),complex)
            for i,root in enumerate(I):
                for j,nextroot in enumerate(I):
                    l=nextroot-root
                    if abs(l)>R:continue
                    f=1-alpha if l==0 else (1-np.exp(2j*pi*l*alpha))/(2j*pi*l)
                    if e==-1:f=np.conjugate(f)
                    M[i,j]=cp*f*np.exp(2j*pi*e*root*alpha)
            components.append((key,M))
    for k in range(3):assert np.max(np.abs(components[2*k][1]-components[2*k+1][1].conj().T))<1e-14
    power={(0,0,0):np.eye(d,dtype=complex)};rows=[];bydegree={}
    source=sum((M*np.exp(1j*T*sum(v*log(p) for v,p in zip(key,primes))) for key,M in components),np.zeros((d,d),complex))
    for b in range(1,7):
        nxt={}
        for key,M in power.items():
            for e,N in components:
                target=tuple(a+c for a,c in zip(key,e))
                nxt[target]=nxt.get(target,np.zeros((d,d),complex))+M@N
        power=nxt
        if b not in (5,6):continue
        amplitudes={key:np.trace(M)/d for key,M in power.items()}
        assert all(sum(abs(v) for v in key)%2==b%2 for key in amplitudes)
        error=max(abs(amplitudes[tuple(-t for t in key)]-np.conjugate(A)) for key,A in amplitudes.items())
        assert error<2e-13
        resolved=sum(A*np.exp(1j*T*sum(v*log(p) for v,p in zip(key,primes))) for key,A in amplitudes.items())
        direct=np.trace(np.linalg.matrix_power(source,b))/d
        assert abs(resolved-direct)<2e-13
        bydegree[b]=amplitudes
        sample=sorted(amplitudes.items(),key=lambda item:-abs(item[1]))[:8]
        rows.append({'degree':b,'class_count':len(amplitudes),'TV':float(sum(abs(A) for A in amplitudes.values())),
             'counting_L2':float(np.sqrt(sum(abs(A)**2 for A in amplitudes.values()))),
             'conjugacy_error':float(error),'resolved_trace_error':float(abs(resolved-direct)),
             'complete_resolved_real_trace':float(resolved.real),
             'samples':[{'exponents':key,'lambda':sum(v*log(p) for v,p in zip(key,primes)),
                         'amplitude_real':float(A.real),'amplitude_imag':float(A.imag)} for key,A in sample]})
    assert not set(bydegree[5])&set(bydegree[6])
    c5=-11501/12500;c6=137641/250000
    TV=abs(c5)*rows[0]['TV']+c6*rows[1]['TV']
    L2=np.sqrt(c5**2*rows[0]['counting_L2']**2+c6**2*rows[1]['counting_L2']**2)
    out={'evidence':'NUMERICAL finite algebra replay only; no arithmetic theorem',
      'parameters':{'primes':primes,'L_toy':L,'T_phase':T,'I':I,'R_toy':R,'a_phi':1},
      'selected_section_certified_for_original_theorem':False,'all_lag_paths_and_roots_included':True,
      'common_degree5_degree6_carriers':[],'rows':rows,'frozen_joint_TV_toy':float(TV),
      'frozen_joint_counting_L2_toy':float(L2),'ratio_reconnaissance':'NO common carrier ratio exists',
      'strict_gt79':False}
    (ROOT/'notes/WP84_CARRIER_AWARE_AMPLITUDE_RECON.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
