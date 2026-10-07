"""Numerical discovery only. Exact certificates live in the separate verifier.
Centered variable X; physical support x<=0 is X<=-1.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement
import json
import numpy as np
from scipy.optimize import minimize

ROOT=Path(__file__).resolve().parents[1]
mu=np.array([1,0,1/3,0,1/4,1/36,157/630])
indices={n:list(combinations_with_replacement(range(n),2)) for n in (3,4)}
def unpack(t,n):
    m=np.zeros((n,n))
    for a,(i,j) in zip(t,indices[n]):m[i,j]=m[j,i]=a
    return m
def pack(m):return np.array([m[i,j] for i,j in indices[len(m)]])
def coeff(m):
    out=np.zeros(2*len(m)-1)
    for i in range(len(m)):
        for j in range(len(m)):out[i+j]+=m[i,j]
    return out
def translate(c):
    # c(X) at X=-1-y, exact algebra evaluated in float for discovery only.
    from math import comb
    return np.array([sum(c[j]*(-1)**j*comb(j,k) for j in range(k,7)) for k in range(7)])
def split(t):return unpack(t[:10],4),unpack(t[10:20],4),unpack(t[20:],3)
def initial():
    q=np.array([-19101/185500,961/3710,31/50,-371/500])
    g=np.outer(q,q);cs=translate(coeff(g));cs[0]-=1
    h=np.diag(cs[::2]);r=np.diag(cs[1::2])
    return np.r_[pack(g),pack(h),pack(r)]
def discover(c5zero=False):
    def equal(t):
        g,h,r=split(t);c=coeff(g);target=translate(c);target[0]-=1
        proof=coeff(h);proof[1:6]+=coeff(r)
        extra=[c[4]]+([c[5]] if c5zero else [])
        return np.r_[target-proof,extra]
    def psd(t):return np.r_[*[np.linalg.eigvalsh(m) for m in split(t)]]
    res=minimize(lambda t:coeff(split(t)[0])@mu,initial(),method='SLSQP',
                 constraints=[{'type':'eq','fun':equal},{'type':'ineq','fun':psd}],
                 options={'maxiter':350,'ftol':1e-11})
    G=split(res.x)[0];c=coeff(G)
    return {'c5_zero':c5zero,'success':bool(res.success),'message':res.message,
            'objective_model_only':float(res.fun),'percentage_model_only':float(100*(1-2*res.fun)),
            'max_equation_residual':float(np.max(np.abs(equal(res.x)))),
            'min_Gram_eigenvalue':float(np.min(psd(res.x))),
            'G_float':G.tolist(),'G_rational_approximants_UNCERTIFIED':
              [[str(F(float(x)).limit_denominator(1000000)) for x in row] for row in G],
            'coefficients_float':c.tolist(),'theorem_certified':False}
def main():
    out={'parent':'195928861e6227d6b7cd824fd35b7eccda7d139c',
         'evidence':'DISCOVERY ONLY; no optimizer values enter a theorem',
         'support_SOS':'p(-1-y)-1=z3^T H z3+y z2^T Q z2, H,Q PSD',
         'safe_kernel_optimization':'not well-defined for actual arithmetic; disjoint proxy forced quadratic analytically',
         'runs':[discover(False),discover(True)]}
    path=ROOT/'notes/WP84_DEGREE6_CONSUMER_NUMERICAL_DISCOVERY.json'
    path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
