#!/usr/bin/env python3
import numpy as np

def build(alpha,beta,R):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(max(0,i-R),min(d,i+R+1)):
            if i!=j:
                H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def main():
    rng=np.random.default_rng(8414)
    for d in (63,127):
        for bw in (2,4,7):
            M=1.25
            alpha=np.clip(rng.normal(size=d)/2,-M,M)
            beta=3.0*rng.standard_t(df=3,size=d)
            H=build(alpha,beta,bw)
            R=np.linalg.inv(H-1j*np.eye(d))
            HR=sum(1.0/r for r in range(1,bw+1))
            J0=(4*M/np.pi)*HR
            theta=np.log(1+1/(2*J0))/bw
            worst=0.0
            for i in range(d):
                for j in range(d):
                    env=2*np.exp(-theta*abs(i-j))
                    worst=max(worst,abs(R[i,j])/env)
            assert worst<=1+2e-10,(d,bw,worst)
            print("d",d,"band",bw,"theta",theta,"worst_ratio",worst)
    print("RESULT: WP84_R2_FINITE_BAND_LOCALITY_PASS")

if __name__=="__main__":
    main()
