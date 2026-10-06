# WP84 — exact coefficient audit for the shifted Hankel wedge

Date: 2026-10-06

Status: **EXACT RATIONAL-COMPLEX COEFFICIENTS AND MATRIX INVARIANTS; NOT A LARGE-T ENERGY BOUND**

This supplements `WP84_SHIFTED_RESOLVENT_SIX_VECTOR_WEDGE.md`. The coefficient matrix is fixed by the consumer and pole; it does not vary with displacement length.

Let (z=\frac45(1+i)), (P(x)=1-Ax+Bx^2-Cx^3), and
[
A=\frac{43428}{13891},\quad B=\frac{37704}{13891},\quad C=\frac{9660}{13891}.
]
The resolvent-polynomial coefficients
[
b_1= B-3Cz,\quad b_2=-A+2Bz-3Cz^2,\quad b_3=P(z)
]
are exactly
[
b_1=\frac{14520-23184i}{13891},\qquad
b_2=\frac{84492}{69455}+\frac{23232}{13891}i,qquad
b_3=\frac{-273989+90672i}{347275}.
]
Thus
[
M=\begin{pmatrix}b_1&b_2&b_3\\b_2&b_3&0\\b_3&0&0\end{pmatrix}.
]

Its characteristic polynomial is
[
\chi_M(\lambda)=\lambda^3-(b_1+b_3)\lambda^2+
(b_1b_3-b_2^2-b_3^2)\lambda+b_3^3.
]
The exact invariants are
[
\operatorname{tr}M=\frac{89011-488928i}{347275},
]
[
b_1b_3-b_2^2-b_3^2=
\frac{45103112063-249325314384i}{120599925625},
]
[
\det M=-b_3^3=
\frac{13810617575994941-19674781705321488i}{41881339171421875}.
]
In particular, (M) is invertible because (b_3\ne0).

This coefficient audit is useful for exact implementation and for detecting accidental coefficient or sign changes. It does **not** establish a positive-energy bound: (M) is complex symmetric, not Hermitian, and its eigenvalues do not by themselves control
[
\frac1d\sum_{i\ne j}\frac{|(UMV^T-VMU^T)_{ij}|^2}{(i-j)^2}.
]
There is also no displacement-indexed family of (M)'s whose spectral distribution could be studied. The live analytic object is the coupled (K_2)-weighted wedge, including the joint large-(T) behavior of (U) and (V).

The companion finite-matrix gate now checks these rational-complex coefficients and invariants before its floating-point commutator and positive-energy replay. Exact coefficient checks and floating-point matrix checks have distinct evidence grades.

No large-(T) estimate or zero-proportion theorem is claimed.
