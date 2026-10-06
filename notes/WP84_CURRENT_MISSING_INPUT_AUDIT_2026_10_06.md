# WP84 — current analytic debt audit (2026-10-06)

Status: **SOURCE AUDIT; NO NEW ASYMPTOTIC THEOREM CLAIMED**

Audit basis: PR #5, branch `research/frontier-7962-hostile-audit-v0.1`,
head `2b1780e7acf428e91ef4bf38ab15e57449b59bee`.

## 1. Active consumer and exact reduction

The active theorem interface is the bounded Christoffel family
`F_delta=(delta+1)P^2/(P^2+delta)`, for each fixed `delta >= 61`.
Its six fixed nonreal poles reduce the zero-counting target to the weighted
resolvent inequality in
`notes/WP84_RESOLVENT_KILL_GATE_2026_10_05.md`.

The permutation/Lindeberg and common-state notes give, at each consumed pole,
the exact second-order flow up to the recorded uniform cubic `o(1)`
remainder:
```
d/dt E tau(R_t(z))
  = - E tau(R_t(z) P R_t(z))
    + (1-2t) E tau(R_t(z) V(R_t(z)) R_t(z))
    + o(1).
```
Here `R_t=(H_t-zI)^(-1)`, `P` is the deterministic retained prime
operator, and `V` is the current-block covariance map.

The current-block part has been reduced further:
- the resonant prime-square covariance is an explicit state functional
  `Psi_res(R_t,z)`, uniformly over the subset state;
- the fast carrier-`2T` current-prime covariance is `o(1)`;
- the exact sharp-state rank-two displacement law and rank-three
  `[D,B R]` formulas reduce the remaining traces to scalar/grid generator
  statistics.

See:
- `notes/WP84_BERNOULLI_COMMON_STATE_GENERATOR.md`
- `notes/WP84_D2_CURRENT_COVARIANCE_CLOSURE.md`
- `notes/WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md`
- `notes/WP84_D2_FAST_CHANNEL_VK_CLOSURE.md`
- `notes/WP84_BR_RANK3_SCALAR_D1.md`

Finite-dimensional identities have regression scripts, including
`src/wp84_br_rank3_scalar_d1_gate.py` and
`src/wp84_gaussian_covariance_hadamard_gate.py`. These verify algebraic
identities; they do not establish a large-`T` state limit.

## 2. The missing analytic input

For each fixed `delta`, it is sufficient to prove the one-sided,
six-pole-weighted endpoint bound after integrating the displayed state flow:
```
limsup_{T -> infinity}
  [ delta+1 + sum_{j=1}^6 c_j(delta) m_{H_T}(z_j(delta)) ]
  <= h_delta(1415/13891),
```
where `h_delta(w)=(delta+1)w/(delta+w)`, with the fixed-pole residues and
normalizations from the bounded-consumer note.

After the exact Lindeberg reduction, the open task is to bound the weighted
integral of the actual Bernoulli-state quantities
```
E tau(R_t P R_t)
and
E Psi_res(R_t,z_j(delta))
```
so their combined contribution fits the model ledger. The needed theorem is
a one-sided bound on this integrated aggregate. Separate limits for each
state statistic would suffice, but are stronger than logically necessary.

Thus the remaining theorem controls the arithmetic Bernoulli resolvent state
along `0 <= t <= 1` at the six fixed poles. The finite-population weights,
current-prime covariance, fixed-pole stability, and finite rank-three algebra
do not by themselves identify or bound that state average.

## 3. Distinction from the shifted heat-flow route

The uniform small-eigenvalue concentration and baseline-norm conditions in
`notes/WP84_SHIFTED_UNIFORM_HEAT_TAIL_CRITERION.md` belong to the separate
shifted-consumer additive-heat-flow route. They remain open for that route,
but are not premises of the active fixed six-pole Bernoulli/Lindeberg
inequality.

No unconditional zero-proportion theorem is claimed.
