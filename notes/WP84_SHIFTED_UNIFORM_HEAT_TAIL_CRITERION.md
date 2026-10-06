# WP84 — uniform large-u tail criterion for the shifted consumer

Date: 2026-10-06

Status: **EXACT CONSUMER TAIL POLYNOMIAL AND CONDITIONAL UNIFORM TAIL LEMMA; REQUIRED GAUSSIAN SMALL-BALL INPUT NOT YET PROVED**

This audits the large-noise step for the shifted consumer
[
p_s(x)=\frac{r^6P(x)^2}{((x-4/5)^2+(4/5)^2)^3},
\qquad r^2=\frac{32}{25},
]
whose boundary value is
[
E_\infty=\frac{122310623232}{120599925625}.
]
For each fixed finite (d), the existing Gaussian invertibility argument gives (\mathbb E\tau p_s(H_{1,d}+\sqrt u W_d)\to E_\infty). That pointwise-in-(d) fact alone does not control the large-(d) limit of the integrated heat flow.

## 1. Exact scalar tail

The rational function
[
g(x)=p_s(x)-E_\infty
=\frac{F(x)}{((x-4/5)^2+(4/5)^2)^3}
]
has exact numerator coefficients in ascending powers of (x):
[
\begin{array}{c|r}
k&[x^k]F\\\hline
0&-56056139186176/1884373837890625\\
1&-1935986510266368/376874767578125\\
2&43996384591872/2599136328125\\
3&-330024542797824/15074990703125\\
4&1339674329088/103965453125\\
5&-367691563008/120599925625
\end{array}
]
and the degree-six coefficient is zero. The sum of the absolute numerator coefficients is
[
S_F=\frac{112913213256073216}{1884373837890625}.
]
For (|x|\ge2),
[
((x-4/5)^2+(4/5)^2)^3
\ge (|x|-4/5)^6
\ge (3|x|/5)^6,
]
so
[
\boxed{|g(x)|\le \frac{C_F}{|x|},\qquad
C_F=\left(\frac53\right)^6S_F
=\frac{112913213256073216}{87917345780625}.}
]
Also (B_F=\sup_{x\in\mathbb R}|g(x)|<\infty), since (g) is continuous on the real line and has a finite limit at infinity.

## 2. Conditional uniform-tail inequality

Let (A_d) be deterministic Hermitian, (W_d) random Hermitian, and put (X_{d,u}=A_d+\sqrt u W_d), (t=\sqrt u), and (M_d=\|A_d\|_{op}). Define
[
\rho_d(\epsilon)=\mathbb E\,\mu_{W_d}([-\epsilon,\epsilon]).
]
For every (K\ge2), Weyl's eigenvalue inequality and the scalar tail above imply
[
\boxed{
\left|\mathbb E\tau_d g(X_{d,u})\right|
\le B_F\,\rho_d\!\left(\frac{K+M_d}{\sqrt u}\right)
+\frac{C_F}{K}.
}
]
Indeed, eigenvalues of (X_{d,u}) inside ([-K,K]) can only arise from eigenvalues of (W_d) inside ([-(K+M_d)/\sqrt u,(K+M_d)/\sqrt u]); outside ([-K,K]), (|g|\le C_F/K).

Consequently, a sufficient uniform input is:
[
\sup_d M_d<\infty,
\qquad
\sup_d\rho_d(\epsilon)\le C_0\epsilon^\beta
\quad(0<\epsilon\le\epsilon_0)
]
for some (C_0,\beta>0). Choosing (K=u^{\beta/(2(\beta+1))}) for sufficiently large (u) then yields
[
\sup_d\left|\mathbb E\tau_d p_s(X_{d,u})-E_\infty\right|
=O\!\left(u^{-\beta/(2(\beta+1))}\right).
]
The implied constant depends on (B_F,C_F,C_0,\beta), and the uniform baseline norm. This is a conditional rate, not a proved estimate for the WP84 Gaussian Loewner field.

For the exact heat-flow identity,
[
\int_U^\infty \mathbb E E'_u\,du
=E_\infty-\mathbb E E_U
=-\mathbb E\tau g(X_{d,U})
]
at finite (d). The conditional uniform bound above would therefore justify making the signed tail uniformly small. It does not bound the absolute variation \(\int_U^\infty|\mathbb E E'_u|du\).

## 3. Why finite-d invertibility is insufficient

Pointwise invertibility for every finite (d) supplies no uniform small-ball estimate. For example, take the illustrative family (A_d=0), (W_d=\epsilon_d I), with (\epsilon_d>0) and (\epsilon_d\to0). Every (W_d) is invertible, and for each fixed (d),
[
p_s(\sqrt u W_d)\to E_\infty
\quad\text{as }u\to\infty.
]
But for every fixed (u), (p_s(\sqrt u\epsilon_d)\to p_s(0)=1) as (d\to\infty). Thus the limits do not commute. This example is not the WP84 noise; it shows why the existing fixed-d invertibility statement cannot by itself establish a uniform tail.

## 4. Exact status

Closed:
- exact rational numerator and (O(1/|x|)) scalar tail for the shifted consumer;
- a Weyl-based uniform-tail inequality conditional on spectral small-ball control;
- explicit identification of the interchange condition needed for the integrated heat flow.

Open:
- a uniform small-eigenvalue concentration bound for the actual growing-dimensional Gaussian Loewner noise (W_d) near zero;
- uniform control of the baseline (\|H_{1,d}\|_{op}), or a replacement argument that handles its growth;
- numerical constants strong enough to put the tail below the (0.00313548) model cushion;
- the remaining heat-curvature and zero-count/taper transfers.

No (>79\%\) unconditional zero theorem is claimed.
