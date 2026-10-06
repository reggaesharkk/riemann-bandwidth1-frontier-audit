#!/usr/bin/env python3
"""Finite regression gate for Xi_z and Xi_zz formulas."""
import numpy as np

def stats(H,z):
    d=H.shape[0]
    R=np.linalg.inv(H-z*np.eye(d))
    J=np.zeros((d,d),dtype=complex)
    for i in range(d):
        for j in range(d):
            if i!=j:
                J[i,j]=1/(np.pi*(j-i))

    Rp=[None,R]
    Rp.append(R@R)
    Rp.append(R@R@R)

    r=[None]+[np.diag(Rp[k]) for k in (1,2,3)]
    h=[None]+[np.diag(J@Rp[k]) for k in (1,2,3)]
    q=[None]+[np.diag(J@Rp[k]@J) for k in (1,2,3)]

    def T(a,b):
        s=0j
        A=Rp[a]; B=Rp[b]
        for i in range(d):
            for j in range(d):
                if i!=j:
                    s += A[i,j]*B[i,j]/((i-j)**2)
        return s/d

    xi=(
        np.dot(r[1],r[1])/(6*d)
        -T(1,1)/(2*np.pi**2)
        +(np.dot(h[1],h[1])-np.dot(r[1],q[1]))/(2*d)
    )

    x1=(
        np.dot(r[1],r[2])/(3*d)
        -T(1,2)/(np.pi**2)
        +np.dot(h[1],h[2])/d
        -(np.dot(r[2],q[1])+np.dot(r[1],q[2]))/(2*d)
    )

    x2=(
        (np.dot(r[2],r[2])+2*np.dot(r[1],r[3]))/(3*d)
        -(T(2,2)+2*T(1,3))/(np.pi**2)
        +(np.dot(h[2],h[2])+2*np.dot(h[1],h[3]))/d
        -(np.dot(r[3],q[1])+np.dot(r[2],q[2])+np.dot(r[1],q[3]))/d
    )
    return xi,x1,x2

def main():
    rng=np.random.default_rng(8417)
    for d in (9,17,29):
        X=rng.normal(size=(d,d))
        H=(X+X.T)/2
        z=.13+1.4j

        xi,x1,x2=stats(H,z)

        h=1e-5
        xp=stats(H,z+h)[0]
        xm=stats(H,z-h)[0]
        fd1=(xp-xm)/(2*h)
        fd2=(xp-2*xi+xm)/(h*h)

        e1=abs(fd1-x1)
        e2=abs(fd2-x2)

        assert e1<2e-7,(d,e1)
        assert e2<2e-5,(d,e2)

        print("d",d,"Xi_z error",e1,"Xi_zz error",e2)

    print("RESULT: WP84_DIRECT_HEAT_CURVATURE_STENCIL_PASS")

if __name__=="__main__":
    main()
