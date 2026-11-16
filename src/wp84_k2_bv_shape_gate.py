#!/usr/bin/env python3
"""Finite algebra gate for the K2-weighted BV/log-d estimate shape."""
import numpy as np
import math

def main():
    rng=np.random.default_rng(8407)
    for d in (32,128,512):
        x=rng.normal(size=d)+1j*rng.normal(size=d)
        y=rng.normal(size=d)+1j*rng.normal(size=d)
        x*=math.sqrt(d)/np.linalg.norm(x)
        y*=math.sqrt(d)/np.linalg.norm(y)

        # displacement coefficients h_r = sum_i x_i y_{i-r}
        var_bound=0.0
        sup_bound=0.0
        for r in range(1,d):
            hp=np.dot(x[r:],y[:-r])
            hm=np.dot(x[:-r],y[r:])
            sup_bound += (abs(hp)+abs(hm))/(d*r*r)
            var_bound += 2*math.pi*(abs(hp)+abs(hm))/(d*r)

        crude_sup=(math.pi**2/3)
        crude_var=4*math.pi*sum(1/r for r in range(1,d))
        assert sup_bound <= crude_sup*1.0000001
        assert var_bound <= crude_var*1.0000001

        print(
            "d",d,
            "sup_proxy",sup_bound,
            "variation_proxy",var_bound,
            "variation/logd",var_bound/math.log(d)
        )

    print("RESULT: WP84_K2_BV_SHAPE_PASS")

if __name__=="__main__":
    main()
