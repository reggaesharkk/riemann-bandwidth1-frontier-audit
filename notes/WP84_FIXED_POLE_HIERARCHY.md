# WP84 — fixed-pole rational minorant hierarchy

Date: 2026-10-04

Status: **EXACT BOUNDED MINORANT FAMILY DERIVED; m=10 MODEL VALUE WITHIN 5.45e-8 OF THE 79.62709668% CHRISTOFFEL RUNG; PRIME-SIDE RESOLVENT LAW STILL OPEN**

The single observable `r3` from `WP84_R3_FIXED_POLE_CERTIFICATE.md` is only the first useful member of a whole fixed-pole hierarchy.

## 1. Universal minorant

For every integer `m>=1` define

[
r_m(x)=1-left(rac{(x-1)^2}{x^2+1}ight)^m.
]

Since

[
rac{(x-1)^2}{x^2+1}
=1-rac{2x}{x^2+1},
]

we have:

- if `x<=0`, the ratio is at least one, so `r_m(x)<=0`;
- if `x>0`, the ratio lies in `[0,1)`, so `0<r_m(x)<=1`.

Therefore, pointwise,

[
oxed{1_{{x>0}}ge r_m(x)}
]

for every fixed `m`.

Thus every Hermitian matrix `H` satisfies

[
oxed{n_+(H)ge operatorname{tr} r_m(H)}.
]

No spectral gap and no raw higher-moment bound are used.

## 2. Same two fixed poles for every m

The only poles of `r_m` are

[
z=+i,qquad z=-i,
]

each of order `m`.

Hence `d^{-1} tr r_m(H)` is determined by the normalized resolvent

[
m_H(z)=d^{-1}operatorname{tr}(H-zI)^{-1}
]

and its derivatives through order `m-1` at `z=i`; the `-i` contribution is the complex conjugate for Hermitian `H`.

So increasing `m` does **not** introduce new pole locations. It only asks for higher local analytic information around the same safe non-real point.

## 3. Rank robustness remains exact

Write

[
t(x)=rac{2x}{1+x^2}in[-1,1].
]

Then

[
r_m(x)=1-(1-t(x))^m.
]

As `x` moves from `-infty` to `+infty`, `t` runs

[
0	o -1	o 1	o0.
]

Since `1-(1-t)^m` is monotone in `t`, the total variation is exactly

[
oxed{operatorname{Var}(r_m)=2^{m+1}}.
]

Therefore a rank-`r` Hermitian perturbation changes the normalized statistic by at most

[
oxed{
left|rac1doperatorname{tr}r_m(A)-rac1doperatorname{tr}r_m(B)ight|
le 2^{m+1}rac rd.
}
]

For every fixed `m`, the deep-zero `o(d)` deletion from WP84 still costs only `o(1)`.

## 4. Trace-norm tail stability

Because

[
|t'(x)|le2
]

and

[
left|rac d{dt}igl(1-(1-t)^migr)ight|
le m2^{m-1},
]

we have the global Lipschitz bound

[
oxed{operatorname{Lip}(r_m)le m2^m}.
]

Hence for Hermitian `A,B`,

[
|operatorname{tr}r_m(A)-operatorname{tr}r_m(B)|
le m2^m|A-B|_1.
]

Thus the source-closed tail trace-norm estimate remains enough for every fixed member of the hierarchy.

## 5. Exact current-model ladder

Using the same extremal four-node quadrature behind the exact six-moment Christoffel certificate, `r_m` can be evaluated **exactly** without solving the cubic: reduce its rational function modulo the Christoffel cubic and then apply `m0,m1,m2`, subtracting the zero atom.

The resulting simple-zero model consumers `2 E[r_m]-1` are:

| m | model simple proportion |
|---:|---:|
| 3 | 0.790998651236532... |
| 4 | 0.795291373413557... |
| 5 | 0.796085641575181... |
| 6 | 0.796235413585635... |
| 7 | 0.796264057105291... |
| 8 | 0.796269607202403... |
| 9 | 0.796270696155902... |
| 10 | **0.796270912353962...** |

The exact Christoffel consumer is

[
rac{11061}{13891}
=0.796270966813044ldots
]

so `m=10` misses the full conditional/model rung by only

[
oxed{5.4459	imes10^{-8}}.
]

Companion exact checker:

`src/wp84_rm_model_hierarchy.py`.

This is still model reconnaissance: it does not turn the unproved six-moment premise into a zeta theorem.

## 6. Why m=10 is a better theorem target than m=3

To exceed 79 percent through

[
N_0^s/Nge2q-1-o(1),
]

we only need

[
q>0.895.
]

The `m=3` model gives

[
q_3approx0.8954993,
]

leaving only about `4.99e-4` of model margin.

The `m=10` model gives

[
q_{10}approx0.898135456,
]

leaving about

[
oxed{3.135	imes10^{-3}}
]

above the 79-percent threshold.

So the higher fixed-pole minorant buys roughly six times more error budget while remaining Proposition-R safe.

## 7. New analytic interface

It is unnecessary to prove the first nine derivatives independently.

Fix any `0<rho<1`. If a candidate limiting resolvent `m_*(z)` satisfies

[
sup_{|z-i|=ho}|m_H(z)-m_*(z)|	o0,
]

then Cauchy's formula gives, for every fixed `k`,

[
|m_H^{(k)}(i)-m_*^{(k)}(i)|
le k!ho^{-k}
sup_{|z-i|=ho}|m_H(z)-m_*(z)|.
]

Therefore one **uniform resolvent law on a fixed circle around `i`** automatically controls every fixed `r_m`, including `m=10`.

This is the preferred theorem interface going forward.

## 8. Current kill gate

The narrow target is now:

[
oxed{
sup_{|z-i|=ho}
|m_{widehat G}(z)-m_*(z)|=o(1)
}
]

for one fixed `rho<1`, with a model/limit for which

[
int r_{10}(x),dmu_*(x)>0.895+eta.
]

Closing that would yield an unconditional simple-zero proportion above 79 percent without any finite raw fourth/eighth moment theorem.
