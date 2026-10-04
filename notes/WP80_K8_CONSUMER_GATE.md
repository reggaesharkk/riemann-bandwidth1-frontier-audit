# WP80 — exact k=8 consumer gate beyond 79.627%

Date: 2026-10-04  
Status: **EXACT CONSUMER-SIDE ALGEBRA; k=8 analytic transport remains open**

## 1. Why this gate matters

The exact k<=6 Christoffel consumer is

\[
w_0\le\lambda_3(0)=\frac{1415}{13891},
\qquad
1-2w_0\ge\frac{11061}{13891}
=0.796270966813\ldots .
\]

The post-79 question is therefore not "can a numerical LP print a larger
number?"  The right question is:

> what exact \((m_7,m_8)\) information is sufficient to force a strict
> improvement, and what is sufficient to cross 80%?

This note answers that algebraically.

## 2. Exact m7 floor

From the shifted Stieltjes moment matrix, the companion gate
`WP80_EXACT_M7_MOMENT_CONE.md` gives

\[
\boxed{
m_7\ge L_7:=
\frac{25866469}{1352400}
=19.126345016267\ldots
}.
\]

This is stronger than the public reconnaissance floor 19.123.

## 3. Exact order-4 Christoffel bound

Let

\[
M_4=(m_{i+j})_{0\le i,j\le4}.
\]

For any polynomial \(p\) of degree at most four with \(p(0)=1\),

\[
\nu(\{0\})\le\int p(x)^2\,d\nu(x).
\]

Minimizing the right-hand side gives

\[
\lambda_4(0)=\frac{1}{(M_4^{-1})_{00}}
=\frac{\det M_4}{\det B_4},
\]

where \(B_4\) is the principal block with indices \(1,\ldots,4\).

After substituting the exact moments through \(m_6\), exact elimination gives

\[
\boxed{
\lambda_4(0)
=
\frac{N(m_7,m_8)}{4D(m_7,m_8)}
}
\]

with

\[
N=
748818000m_8
-13335840000m_7^2
+504286322400m_7
-4794396454037,
\]

\[
D=
1837779300m_8
-24004512000m_7^2
+903891063600m_7
-8574904106497.
\]

In the positive-definite feasible region \(D>0\).

## 4. Strict improvement over 79.627% is automatic once m7 moves

The key identity is

\[
\boxed{
\lambda_4-\frac{1415}{13891}
=
-\frac{
27(1352400m_7-25866469)^2
}{
55564\,D
}.
}
\]

Therefore, whenever \(D>0\),

\[
m_7>L_7
\quad\Longrightarrow\quad
\lambda_4<\frac{1415}{13891}.
\]

So a theorem-grade exact k=8 transport with any \(m_7\) strictly above its
flat Stieltjes floor gives a **strictly larger** simple-zero coefficient than

\[
\frac{11061}{13891}=79.6270966813\ldots\%.
\]

The amount of improvement still depends on \(m_8\), but the direction does
not.

This is important strategically: the k=8 rung does not need to rediscover the
79.627% gain.  It needs to certify that the transported moment pair is a
non-flat extension and then control \(m_8\) tightly enough for the desired
headline.

## 5. Exact 80% gate

The condition

\[
1-2\lambda_4>\frac45
\]

is equivalent, in the feasible region, to

\[
\boxed{
m_8
<
T_{80}(m_7):=
\frac{
18670176000m_7^2
-713649484800m_7
+6822174057191
}{
68531400
}.
}
\]

There is also an exact feasibility floor coming from \(M_4\succeq0\):

\[
\boxed{
m_8\ge
F_8(m_7):=
\frac{
13335840000m_7^2
-504286322400m_7
+4794396454037
}{
748818000
}.
}
\]

At the flat point \(m_7=L_7\), these two curves touch:

\[
F_8(L_7)=T_{80}(L_7)
=
\frac{90678451343}{2449534500}
=37.018646335865\ldots .
\]

For comparison, at the public reconnaissance upper endpoint
\(m_7=19.136\),

\[
F_8(19.136)=37.095675327302\ldots,
\]

while

\[
T_{80}(19.136)=37.119410977975\ldots .
\]

So an 80% result is not a vague aspiration: once \(m_7\) is pinned, there is
an explicit exact corridor for \(m_8\).

## 6. Research consequence

The >79 programme now has a sharper order of attack:

1. exactify the seven-cycle / \(m_7\) model assembly;
2. transport the mixed \(\{5,2\}\) contribution analytically;
3. assemble and transport the \(m_8\) classes
   \(\{2^4\},\{4,2,2\},\{4,4\},\{6,2\}\);
4. compare the resulting exact \(m_8\) directly with \(T_{80}(m_7)\);
5. only if that fails, re-optimize the consumer rather than moving the
   goalposts numerically.

The companion checker
`src/wp80_k8_christoffel_gate.py` verifies the determinant identities with
exact rational arithmetic and no numerical optimizer.

## Evidence boundary

Nothing in this note proves the zeta-side \(m_7\) or \(m_8\) transport.
It upgrades the **consumer**: it tells us exactly what the arithmetic/model
side must deliver to beat 79.627% and to cross 80%.
