# WP84 — fixed-circle resolvent as a bounded-time unitary-flow problem

Date: 2026-10-05

Status: **EXACT REDUCTION CLOSED; NEW DYNAMIC STATE VARIABLES IDENTIFIED; ARITHMETIC FLOW CLOSURE OPEN**

The compressed-translation state space suggests a second formulation of the fixed-circle kill gate that avoids a Neumann expansion in powers of the full matrix.

## 1. Laplace representation

For Hermitian H and z=E+i eta with eta>0,

[
oxed{
(H-zI)^{-1}
=
iint_0^infty e^{itz}e^{-itH},dt
}
]

in operator norm.

Hence for the normalized trace

[
m_H(z)
=
iint_0^infty e^{itz},phi_H(t),dt,
qquad
phi_H(t)=	au_d(e^{-itH}).
]

On a fixed circle

[
|z-i|=ho<1,
qquad
etageeta_0:=1-ho,
]

the tail after time T_* is bounded uniformly by

[
oxed{
left|
iint_{T_*}^infty e^{itz}phi_H(t),dt
ight|
le
e^{-eta_0T_*}/eta_0.
}
]

Therefore a fixed-circle resolvent theorem is equivalent, up to an explicit exponentially small tail, to controlling the bounded unitary statistic (phi_H(t)) on one finite time interval.

## 2. Exact one-block Duhamel expansion

Let

[
U_A(t)=e^{-itA}.
]

For Hermitian A,B, iterated Duhamel gives

[
egin{aligned}
U_{A+B}(t)
={}&U_A(t)
-iint_0^t U_A(t-s)BU_A(s),ds\
&-int_{0<s_1<s_2<t}
U_A(t-s_2)B U_A(s_2-s_1)B U_A(s_1)
,ds_1ds_2
+mathcal R_3.
end{aligned}
]

Because every propagator is unitary, the normalized-trace remainder obeys

[
oxed{
|	au_d(mathcal R_3)|
le
t^3|B|_{m op}^3/6.
}
]

Thus, after summing the infinitesimal prime blocks,

[
sup_{0le tle T_*}
|mathcal R_{ge3}(t)|
le
T_*^3
sum_j|B_j|_{m op}^3/6
=
O(T_*^3L^{-3}).
]

For fixed (ho) and fixed target accuracy, (T_*) is an absolute constant, so the cubic debt is still o(1).

## 3. Trace cyclicity collapses the time integrals

The first-order trace simplifies exactly:

[
oxed{
-iint_0^t
	au_d(U_A(t-s)BU_A(s)),ds
=
-it,	au_d(BU_A(t)).
}
]

For the second-order term put (u=s_2-s_1).  Cyclicity gives

[
oxed{
-int_0^t
(t-u),
	au_d(
B U_A(u) B U_A(t-u)
),du.
}
]

These identities require no multiplication-algebra ansatz.

## 4. Correct translation-algebra state variables

For a sharp partial translation (U_s), the first-order term samples a translation coefficient of the unitary flow:

[
F_A(t;s)
:=
	au_d(U_s^*e^{-itA}).
]

The second-order term samples the two-time translation correlation

[
G_A(t,u;s_1,s_2)
:=
	au_d(
U_{s_1}e^{-iuA}
U_{s_2}e^{-i(t-u)A}
).
]

These are the natural dynamic variables of the compressed translation / Wiener--Hopf algebra.

They retain the boundary-overlap geometry automatically.  No scalar covariance closure is imposed.

## 5. Fourth-order fail-closed check

The small-time expansion is

[
phi_H(t)
=
1-it,m_1-rac{t^2}{2}m_2
+rac{it^3}{6}m_3+rac{t^4}{24}m_4+cdots.
]

With the exact model anchors,

[
m_1=1,quad
m_2=4/3,quad
m_3=2,quad
m_4=13/4.
]

Equivalently, after centering at one,

[
e^{it}phi_H(t)
=
1-rac{t^2}{6}
+rac{t^4}{96}
+O(t^5).
]

The rejected covariance-only closure gives centered (m_4=7/30), hence the wrong (t^4) coefficient.  Any proposed unitary-flow closure must reproduce the exact (1/60) fourth-moment repair before it can be transformed back into a resolvent law.

## 6. Why this formulation may be easier

The resolvent formulation carries repeated factors of ((Im z)^{-1}).  The unitary formulation instead keeps

[
|e^{-itA}|_{m op}=1
]

at every intermediate step and pays only an exponentially decaying Laplace tail.

The arithmetic problem is not eliminated, but it is recast as finite-time control of translation coefficients and two-time correlations in the exact state space already identified by the partial-shift overlap theorem.

## 7. Current theorem fork

We now have two equivalent analytic interfaces:

1. direct fixed-circle resolvent closure in the compressed translation algebra;
2. bounded-time unitary-flow closure for (F_A) and (G_A), followed by the explicit Laplace transform above.

Whichever route first reproduces the fourth-order overlap correction and reaches the consumer conditioning target should be preferred.
