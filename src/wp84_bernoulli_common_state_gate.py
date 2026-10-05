#!/usr/bin/env python3
"""Regression gate for the common-state Bernoulli D1+D2 coefficient 1-2t."""
import numpy as np

def main():
    rng=np.random.default_rng(8412)
    for d in (7,13,21):
        X=rng.normal(size=(d,d))
        H=(X+X.T)/2
        Y=rng.normal(size=(d,d))
        G=(Y+Y.T)/2/80
        z=.13+1.5j
        Rm=np.linalg.inv(H-z*np.eye(d))
        Rp=np.linalg.inv(H+G-z*np.eye(d))

        d1=np.trace(Rm@G@Rm)/d
        d2=np.trace(Rm@G@Rm@G@Rm)/d

        for t in (.1,.37,.5,.82):
            common1=(1-t)*np.trace(Rm@G@Rm)/d+t*np.trace(Rp@G@Rp)/d
            common2=(1-t)*np.trace(Rm@G@Rm@G@Rm)/d+t*np.trace(Rp@G@Rp@G@Rp)/d

            lhs=-d1+d2
            rhs=-common1+(1-2*t)*common2

            # Error is cubic in G; verify cubic scaling below rather than
            # an absolute tiny threshold at one fixed G.
            err=abs(lhs-rhs)

            G2=G/2
            Rp2=np.linalg.inv(H+G2-z*np.eye(d))
            e1=np.trace(Rm@G2@Rm)/d
            e2=np.trace(Rm@G2@Rm@G2@Rm)/d
            c1=(1-t)*e1+t*np.trace(Rp2@G2@Rp2)/d
            c2=(1-t)*e2+t*np.trace(Rp2@G2@Rp2@G2@Rp2)/d
            err2=abs((-e1+e2)-(-c1+(1-2*t)*c2))

            # Halving G should reduce a cubic leading error by about 8.
            assert err2 <= .2*err + 1e-14,(d,t,err,err2)
            print("d",d,"t",t,"err",err,"half-ratio",err2/max(err,1e-30))

    print("RESULT: WP84_BERNOULLI_COMMON_STATE_GENERATOR_PASS")

if __name__=="__main__":
    main()
