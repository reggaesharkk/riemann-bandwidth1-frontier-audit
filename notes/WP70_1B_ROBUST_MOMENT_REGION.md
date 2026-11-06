# WP70-1B — exact robust moment region for 70%

Date: 2026-10-04  
Status: **DERIVED REDUCTION — NOT YET AN UNCONDITIONAL MOMENT THEOREM**

## Result

The full conjectural statement

\[
(\mu_1,\mu_2,\mu_3,\mu_4)
=
\left(1,\frac43,2,\frac{13}{4}\right)
\]

is stronger than necessary to cross 70%.

Let

\[
\mu_0=1,\qquad
\mu_1=1,\qquad
\mu_2=\frac43,\qquad
\mu_3=r,\qquad
\mu_4=q.
\]

For the degree-two Christoffel bound at zero, the Hankel moment matrix is

\[
M=
\begin{pmatrix}
1&1&4/3\\
1&4/3&r\\
4/3&r&q
\end{pmatrix}.
\]

Exact inversion gives

\[
\Lambda_2(0)
=
\frac{9q-27r^2+72r-64}
     {9(4q-3r^2)}.
\]

The simple-zero transfer is

\[
B(r,q)=1-2\Lambda_2(0)
=
\frac{18q+27r^2-144r+128}
     {9(4q-3r^2)}.
\]

Assuming the moment matrix is positive definite, the exact condition

\[
B(r,q)>\frac7{10}
\]

is equivalent to

\[
\boxed{
q<
\frac{459r^2-1440r+1280}{72}.
}
\]

This is the first useful kill-shot reduction: **we do not need the exact
fourth-moment asymptotic.  One-sided moment bounds are enough.**

## Error budget around the sine-kernel target

Write

\[
r=2-\delta_3,\qquad
q=\frac{13}{4}+\delta_4.
\]

Then \(B>0.70\) is guaranteed by the exact inequality

\[
\boxed{
\delta_4
+\frac{11}{2}\delta_3
-\frac{51}{8}\delta_3^2
<
\frac1{36}.
}
\]

This gives a quantitative research budget.

### If the third moment is exact

If \(r=2\), it is enough to prove merely

\[
\boxed{q<\frac{59}{18}=3.277777\ldots}
\]

rather than \(q=13/4=3.25\).

So the fourth moment may exceed its sine-kernel target by almost

\[
\frac1{36}=0.027777\ldots
\]

and still clear 70%.

### If the fourth moment is at the sine-kernel value

If \(q\le13/4\), the third moment only needs to be slightly below 2.

Numerically the exact critical lower value is approximately

\[
\boxed{r>1.994919578\ldots}.
\]

A clean safe target is therefore

\[
\boxed{\mu_3\ge1.995,\qquad \mu_4\le3.25}
\]

which has substantial strict margin for 70%.

### Mixed errors

The exact budget lets us trade a weaker third-moment estimate against a weaker
fourth-moment estimate.  This is valuable because the two prime-side trace
problems need not be solved to the same precision.

## Why this changes the analytic target

The paper phrases the conditional rung as \(HL^*(4)\), i.e. convergence of the
first four normalized moments to their sine-process values.

For 70%, that is overkill.

It is sufficient to establish **one-sided inequalities** of the form

\[
\liminf \mu_3(T)\ge 2-\delta_3,
\qquad
\limsup \mu_4(T)\le \frac{13}{4}+\delta_4
\]

for any explicit \((\delta_3,\delta_4)\) satisfying the budget above.

That may be materially easier than identifying the complete asymptotic main
term for every shifted correlation.

## Prime-side consequence

WP70-1A identified the fourth-trace obstruction as weighted correlations of

\[
(\Lambda*\Lambda)(m)(\Lambda*\Lambda)(m+h).
\]

WP70-1B now tells us exactly how accurate the resulting trace estimate must be.

The preferred first theorem target is therefore no longer

> prove \(\mu_4\to13/4\) exactly.

It is

> prove \(\mu_3\ge1.995-o(1)\) and \(\mu_4\le3.25+o(1)\),

or another point inside the exact two-parameter region.

If that target is too strong, use the full error budget rather than abandoning
the route.

## Independent exact checker

\`src/wp70_moment_region_exact.py\` verifies the exact rational algebra and
tests explicit safe/unsafe budget points.

Expected final line:

\`RESULT: ROBUST_70_PERCENT_MOMENT_REGION_DERIVED\`

## Claim boundary

This note derives a **sufficient moment region** for a 70% theorem.

It does not prove that zeta's prime-side traces satisfy that region.
That is the remaining analytic problem.
