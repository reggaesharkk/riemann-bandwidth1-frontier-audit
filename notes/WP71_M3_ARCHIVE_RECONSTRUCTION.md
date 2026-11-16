# WP71 — independent reconstruction of the two archived \(m_3\) steps

Date: 2026-10-04  
Status: **ARCHIVED-DEPENDENCY RECONSTRUCTION — ANALYTIC INPUTS EXPLICIT**

## Purpose

The public proof of

\[
\mu_3\to2
\]

delegates two nonstandard steps to a non-public memo
\`V1_completion.md\`:

1. the \(k=3\) adaptation of the matrix tail estimate;
2. the locality-plus-calibration argument fixing each
   \(\mu P^2\) class at \(1/3\).

A search of the connected Drive corpus and the public GitHub package did not
locate that memo.  Rather than inherit an unavailable proof, we reconstruct
both steps from the displayed hypotheses.

This note does **not** re-prove Weil's explicit formula, the first-two-moment
theorem, or the standard prime-sum asymptotic.  Those remain explicit external
inputs.

## 1. The \(k=3\) matrix-tail step does not need a new tail theorem

Write the normalized compressed matrix as

\[
\widetilde G=A+E,
\]

where the public framework gives

\[
\|E\|_{\rm op}\le\theta_0,
\qquad
\theta_0\ll l\,T^{\lambda/2-1},
\]

and the \(A\)-part satisfies

\[
\|A\|_F^2=O(d\ell_1^2).
\]

Both \(A,E\) are Hermitian and

\[
d\asymp LT,\qquad
\ell_1\asymp l.
\]

By cyclicity of trace,

\[
\operatorname{tr}(A+E)^3-\operatorname{tr}A^3
=
3\operatorname{tr}(A^2E)
+
3\operatorname{tr}(AE^2)
+
\operatorname{tr}(E^3).
\]

The first term satisfies

\[
|\operatorname{tr}(A^2E)|
\le
\|E\|_{\rm op}\operatorname{tr}(A^2)
\le
\theta_0\|A\|_F^2.
\]

For the second,

\[
|\operatorname{tr}(AE^2)|
\le
\|A\|_F\|E^2\|_F
\le
\|A\|_F\,\sqrt d\,\theta_0^2,
\]

because every eigenvalue of \(E\) has magnitude at most \(\theta_0\).
Finally,

\[
|\operatorname{tr}(E^3)|
\le d\,\theta_0^3.
\]

After division by the third-moment normalization
\(d\ell_1^3\), these are respectively

\[
O\!\left(\frac{\theta_0}{\ell_1}\right),
\qquad
O\!\left(\frac{\theta_0^2}{\ell_1^2}\right),
\qquad
O\!\left(\frac{\theta_0^3}{\ell_1^3}\right).
\]

At the worst endpoint \(\lambda=1\),

\[
\frac{\theta_0}{\ell_1}=O(T^{-1/2}),
\quad
\frac{\theta_0^2}{\ell_1^2}=O(T^{-1}),
\quad
\frac{\theta_0^3}{\ell_1^3}=O(T^{-3/2}).
\]

Thus

\[
\boxed{
\operatorname{tr}(A+E)^3-\operatorname{tr}A^3
=
o(d\ell_1^3)
}
\]

uniformly for every fixed \(0<\lambda\le1\).

This reconstructs the first archived step using only the displayed
operator-tail estimate and the stated Frobenius scale.  The stronger public
trace-norm estimate for \(E\) is not needed.

## 2. Exact locality of the \(\mu P^2\) overlap

The potentially ambiguous constant is easier to see after freezing the
frequency pattern.

A \(\mu P^2\) diagonal has one zero-frequency slot and a cancelling prime pair

\[
(0,+u,-u)
\]

up to cyclic permutation.

For a hard unit window, a \(k\)-cycle overlap is

\[
O_k(v_1,\ldots,v_k)
=
\left(
1-
\bigl[\max_j s_j-\min_j s_j\bigr]
\right)_+,
\]

where \(s_j\) are the cumulative partial sums beginning at zero.

For the two-cycle prime diagonal,

\[
O_2(+u,-u)=(1-|u|)_+.
\]

For the three-cycle with a zero slot, the cumulative set contains only
\(0\) and \(u\) (with one repeated point), so **for every cyclic placement**

\[
\boxed{
O_3(0,+u,-u)=O_2(+u,-u)=(1-|u|)_+.
}
\]

This is the locality statement in exact geometric form.  It is not a
finite-height fit.

For the smooth taper, the public window calculus sandwiches the overlap
between the same hard-window profile with an \(O(w/L)\) edge loss, and the
endpoint limit sends

\[
w/L\to0.
\]

Hence the same diagonal weight is recovered asymptotically.

## 3. The \(\mu\)-slot has unit normalized weight

Stirling gives uniformly for \(\tau\in[T,2T]\)

\[
2\pi\mu(\tau)
=
\log(\tau/2\pi)+O(T^{-1})
=
l+O(1).
\]

Since

\[
\ell_1=l+2\log2-1,
\]

we have

\[
\boxed{
\frac{2\pi\mu(\tau)}{\ell_1}
=
1+O(l^{-1})
}
\]

uniformly over the consumed window.

Thus insertion of the single \(\mu\)-slot changes the normalized diagonal
coefficient only by \(1+o(1)\).

## 4. Calibration from the already established \(k=2\) diagonal

The first-two-moment theorem gives the prime diagonal with exactly the same
edge weight:

\[
\sum_{n\le X}
\frac{\Lambda(n)^2}{n}
g(\log n)
=
\frac{L^3}{6}(1+O(L^{-1})).
\]

Its normalized contribution at \(k=2\) is the established

\[
\frac13.
\]

Sections 2--3 show that a \(\mu P^2\) class has:

- the same cancelling \((+u,-u)\) prime diagonal;
- the same hard-window overlap in the endpoint limit;
- one normalized \(\mu\)-slot of weight \(1+o(1)\).

Therefore each cyclic class has the same endpoint coefficient,

\[
\boxed{
\mu P^2\text{ class}
=
\frac13+o(1).
}
\]

Trace cyclicity makes the three placements equal, so

\[
3\times\frac13=1.
\]

Together with the already standard

\[
\mu^3\to1,
\]

and the negligible \(\Pi\), single-\(P\), and exact-resonant \(P^3\) classes
listed in the public nine-class ledger, this reconstructs

\[
\boxed{\mu_3\to2}.
\]

## Evidence boundary

What is newly removed:

- dependence on the unavailable \(V1_completion.md\) for the matrix-tail
  adaptation;
- dependence on that memo for the **constant-identification mechanism** of
  the \(\mu P^2\) classes.

What remains external/analytic input:

1. the public operator-tail estimate itself;
2. the classical/Stirling estimates for \(\mu\);
3. the already established \(k=2\) prime diagonal / Montgomery evaluation;
4. the standard prime-power resonance/negligibility estimates for the other
   seven classes.

This is a much smaller and auditable dependency set.

## Portfolio-method transfer

The move mirrors the strongest lesson from the user's other exact audits:
identify the **local owner** of a coefficient before bounding the global sum.
Here the owner is the exact cycle overlap

\[
O_3(0,u,-u)=O_2(u,-u),
\]

so the coefficient is inherited from the independently established \(k=2\)
calibration instead of being inferred from a finite-height \(m_3\) fit.

No theorem from another research field is imported.
