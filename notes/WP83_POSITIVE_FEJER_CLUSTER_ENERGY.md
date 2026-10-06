# WP83 — positive-multiplicity Fejer energy and the remaining endpoint-transfer star\n\nDate: 2026-10-04\nStatus: **SPACING-FREE POSITIVE ENERGY AT THE CENTRAL SCALE CLOSED; ENDPOINT AMPLIFICATION FOR LARGE COMPARABLE-DEPTH CLUSTERS STILL OPEN**\n\nThe <=4 branch is now controlled by the spacing-free Turan--Nazarov argument. The remaining EC-star concerns components with at least five comparable-depth off-line pairs.\n\nThis note isolates one exact positivity mechanism that survives arbitrary ordinate collisions and clarifies why it is not yet the full kill shot.\n\n## 1. Fejer triangle identity\n\nFor H>0 put\n\n    W_H(t)=(1-|t|/H)_+.\n\nIts Fourier transform in the convention e^{i xi t} is\n\n    integral_{-H}^H W_H(t)e^{i xi t}dt\n      = H * sinc^2(xi H/2)\n      >= 0.\n\nLet\n\n    q(t)=sum_{j=1}^M m_j e^{i omega_j t},\n\nwith multiplicities m_j positive integers. Expanding and using the nonnegative transform gives\n\n    boxed:\n    integral_{-H}^H W_H(t)|q(t)|^2 dt\n      = H sum_{i,j} m_i m_j sinc^2((omega_i-omega_j)H/2)\n      >= H sum_j m_j^2\n      >= H sum_j m_j.\n\nNo spacing between the omega_j is assumed.\n\nThis is an exact positive-energy floor for any equal-depth positive-multiplicity layer.\n\n## 2. Why this matters for large clusters\n\nThe arbitrary-coefficient near-collision obstruction does not apply to an equal-depth zero layer: the coefficients are positive multiplicities. Even a component containing many nearly coincident ordinates carries at least diagonal Fejer energy.\n\nThus large cluster size by itself is not enough to create total scalar cancellation.\n\n## 3. Why this does NOT yet close EC-star\n\nThe Proposition-R scalar is\n\n    F(v)=2 sum_j m_j e^{i omega_j v} cosh(delta_j v).\n\nor, after removing the maximal growth e^{delta_* v},\n\n    q_*(v)=sum_j m_j e^{-(delta_*-delta_j)v}e^{i omega_j v}.\n\nFor a comparable-depth band the coefficients now vary with v. The exact Fejer positivity above applies only when the depth weights are constant (for example an exact equal-depth layer).\n\nThe high-moment contradiction needs energy near the positive endpoint v~L, where the factor X^{delta_*} is present. A central Fejer floor near v=0 does not by itself transport that energy to the endpoint.\n\nTherefore the genuine remaining statement is an **endpoint-transfer inequality for positive exponential sums with slowly varying positive amplitudes**.\n\n## 4. PT-star interface\n\nA sufficient replacement for EC-star is:\n\n**PT-star.** Let\n\n    q_*(v)=sum_j m_j exp(-eps_j v+i omega_j v),\n\nwhere m_j are positive integers and\n\n    0<=eps_j<=D log L/L.\n\nFor some fixed theta in (0,1/4), prove uniformly that\n\n    integral_{(1-2theta)L}^{(1-theta)L} |q_*(v)|^2 dv\n      >= L^{-C} * sum_j m_j\n\nwith C depending only on D and theta, not on the number or spacing of frequencies.\n\nCombined with the maximal factor exp(delta_* v), the g(v) plateau, and the exact Frobenius identity, PT-star would give the required large-component energy floor and eliminate EC-star as a separate zero-pair-counting assumption.\n\n## 5. Current evidence\n\n- Exact equal-depth Fejer floor: CLOSED.\n- Size<=4 endpoint transfer by Turan--Nazarov: CLOSED in analytic write-up.\n- Arbitrary-size slowly varying positive-amplitude endpoint transfer: OPEN.\n- Local zero count alone does not prove it.\n- Dimension counting / two-window row excess does not prove it.\n\n## 6. Strategic meaning\n\nThis converts the large-cluster obstruction from an opaque zero-spacing problem into one scalar harmonic-analysis question. A proof of PT-star would close the large-component branch without any new zero-pair density theorem.\n\nCompanion finite Fourier positivity gate: `src/wp83_positive_fejer_energy.py`.\n

## 7. PT-star falsified

The endpoint-transfer target proposed above is **false** under positivity and the local-count scale alone.

Take the equal-depth family

    omega_j=j/L,  m_j=1,  j=0,...,M-1.

Then on the endpoint interval J=[(1-2theta)L,(1-theta)L],

    q(v)=sum_j exp(i j v/L)

is a Dirichlet kernel evaluated at x=v/L, and x stays a fixed distance away from 0 mod 2pi. Hence

    |q(v)| <= c_theta

uniformly in M, so

    integral_J |q|^2 = O_theta(L).

Choosing M~T L while keeping spacing 1/L respects the O(L) unit-interval local-count scale, but then

    [endpoint energy]/M << 1/T=o(L^{-C})

for every fixed C.

Thus the Fejer floor is genuinely a **central-energy** theorem and cannot be transported uniformly to the amplified endpoint.

See `WP83_PT_STAR_COUNTEREXAMPLE.md`.

The raw-moment large-component branch is therefore left with EC-star or another genuinely stronger zero-distribution input.
