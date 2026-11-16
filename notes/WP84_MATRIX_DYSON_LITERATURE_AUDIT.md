# WP84 — matrix-Dyson literature audit for the artificial Gaussian bridge

Date: 2026-10-05

Status: **USEFUL ROADMAP, NOT A BLACK-BOX THEOREM; STANDARD FLATNESS/DECAY HYPOTHESES DO NOT MATCH THE WP84 COVARIANCE**

The exact Gaussian quadrature bridge naturally suggests a matrix Dyson
equation (MDE).  This note records what may and may not be imported from the
standard correlated-Gaussian literature.

## 1. Relevant published framework

Ajanki--Erdos--Kruger, *Stability of the matrix Dyson equation and random
matrices with correlations*, Probab. Theory Relat. Fields 173 (2019),
293--373, studies correlated Hermitian random matrices with self-energy map

    S[R]
      = E[(H-A) R (H-A)]

and deterministic MDE

    1 + (z I - A + S[M]) M = 0.

DOI:

    10.1007/s00440-018-0835-z

Their framework is conceptually close to the artificial WP84 Gaussian bridge
because our mixed-sign covariance is also an explicit linear self-energy map.

A related translation-invariant Gaussian paper is
Ajanki--Erdos--Kruger, *Local Spectral Statistics of Gaussian Matrices with
Correlated Entries*, J. Stat. Phys. 163 (2016), 280--302,
DOI 10.1007/s10955-016-1479-y.

## 2. Why the main AEK theorem is not directly applicable

The 2019 MDE framework assumes, among other structural conditions, a
**flatness** lower/upper bound of the schematic form

    p <R> I
      <= S[R]
      <= P <R> I

for positive semidefinite R.

Our mixed sharp covariance does not have such a uniform lower bound.

Already on multiplication symbols its continuum action is

    (K r)(x)
      = a^(-2)
        int_0^1 |x-u| r(u) du.

If r is concentrated near one point x0, then (K r)(x0) can be arbitrarily
small compared with the average of r.

Thus a positive flatness constant p cannot be read off from the WP84 kernel.

## 3. Decay mismatch

The 2016 translation-invariant local-law paper assumes power-law or
exponential summability/decay of the correlation kernel, together with a
non-resonance condition.

The circular scalar Gaussian field produced by our quadrature bridge has
fixed-lag covariance

    K_infty(r)
      = 1/(2*pi*i*r*a^2),
      r!=0.

So its natural Fourier-grid correlation decays only like

    1/|r|.

That is long-range Cauchy decay, not the summable fast-decay regime required
by those local-law theorems.

Therefore the published local laws may not be cited as if they already prove
our bridge resolvent limit.

## 4. Why the MDE idea is still useful

The published work confirms the correct conceptual object:

    deterministic mean A
      + covariance/self-energy map S
      -> nonlinear resolvent equation.

WP84 is easier in one important respect:

    the F9 poles stay a fixed distance
    Im z >= about 1.46

from the real axis.

We do **not** need a local law down to eigenvalue spacing.

At fixed imaginary part all resolvents have a deterministic operator bound,
and our random matrices have the additional exact structure

    rank[D,H] <= 2,
    rank[D,R] <= 2.

So a bespoke fixed-eta Dyson comparison may be substantially simpler than
the general AEK local-law problem.

## 5. Correct next use of the literature

Use the MDE papers as a proof-design guide:

1. derive an approximate/self-consistent equation for the small displacement
   generators rather than for all d^2 entries;
2. prove stability only at the four fixed F9 poles;
3. exploit the explicit circular covariance symbol s/a^2;
4. never invoke flatness or fast-decay conclusions that fail for the
   Cauchy/Loewner kernel.

This is a candidate analytic route, not a closed input.

See:

    notes/WP84_GAUSSIAN_QUADRATURE_BRIDGE.md
    notes/WP84_CIRCULAR_GAUSSIAN_Q_FIELD.md
    notes/WP84_BR_RANK3_SCALAR_D1.md
