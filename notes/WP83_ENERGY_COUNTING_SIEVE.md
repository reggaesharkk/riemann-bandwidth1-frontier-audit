# WP83 — Proposition-R energy-counting sieve\n\nDate: 2026-10-04\nStatus: **ALGEBRAIC ZERO-DENSITY MECHANISM CLOSED; ONE SMALL-CLUSTER RETENTION LEMMA + ONE LARGE-CLUSTER STAR LEMMA REMAIN**\n\nThe retraction says the valid forward work contains an energy-counting zero-density estimate, an unconditional <=4-cluster form, and one explicitly starred lemma. Those documents are not public. This note does **not** attribute the following reconstruction to the authors; it derives the natural energy-counting mechanism from our independently closed Gabor identities.\n\n## 1. Depth-band graph\n\nFor one representative from every off-line reflection pair define\n\n    delta_r=|beta_r-1/2|.\n\nFix a depth threshold delta>0 and a comparison band\n\n    delta_r >= delta - D*log L/L.\n\nOn these representatives build a graph by joining two ordinates when their separation is at most a chosen buffer R.\n\nThe buffer is selected large enough that distinct components are decoupled by `WP83_FAR_FIELD_DECOUPLING.md`. A typical asymptotic choice is a fixed power of L under the two-derivative decay route; a smoother/Gevrey profile may permit a smaller buffer.\n\nCall a connected component **small** if it contains at most four off-line pairs.\n\n## 2. Exact cluster-energy-to-fourth-moment inequality\n\nWork in the normalized matrix units used by the moment theorem. Suppose M selected small components survive in an orthogonal compression B of the full matrix and satisfy\n\n    rank(B) <= 8M\n\nand\n\n    tr(B^2)\n      >= c * M * X^(2 delta) / L^C.\n\nThe rank bound is structural: one reflection pair has rank at most two, hence a component with at most four pairs has rank at most eight.\n\nFor Hermitian B with nonzero eigenvalues lambda_i, Cauchy--Schwarz gives\n\n    (sum lambda_i^2)^2\n      <= rank(B) * sum lambda_i^4.\n\nTherefore\n\n    boxed:\n    tr(B^4)\n      >= [tr(B^2)]^2/rank(B)\n      >= (c^2/8) * M * X^(4 delta) / L^(2C).\n\nSchatten norms decrease under orthogonal compression, so\n\n    tr(Gtilde^4) >= tr(B^4).\n\nIf the fourth moment has any finite theorem-grade upper bound\n\n    tr(Gtilde^4) <= C4 * T * L^D\n\n(all exact normalizing powers of ell1 are absorbed into D), then\n\n    boxed:\n    M\n      <= C' * T * X^(-4 delta) * L^(D+2C).\n\nSince X=T^(lambda+o(1)),\n\n    M <= T^(1-4 lambda delta+o(1)).\n\nThis is the power-law energy-counting exponent.\n\n## 3. Proposition-R threshold falls out immediately\n\nIf\n\n    delta > 1/(4 lambda)+epsilon,\n\nthen\n\n    1-4 lambda delta < -4 lambda epsilon.\n\nHence the right side tends to zero. Since M is an integer, eventually there can be **no retained small component** at that depth.\n\nThus a finite fourth-moment bound forces the following dichotomy:\n\n    every zero deeper than 1/(4 lambda)+epsilon\n    must belong to a component that either\n      (a) has at least five off-line pairs, or\n      (b) violates the small-cluster retention lemma.\n\nThis is the exact location where the higher-moment theorem collides with Proposition R.\n\n## 4. The <=4 small-cluster retention lemma (SC4)\n\nThe missing analytic statement needed to make the previous section unconditional for small components is:\n\n**SC4.** For every fixed delta0>0 there exist c,C>0 such that every depth-band component C of size s<=4 with maximal depth delta_*>=delta0 has, in one of the two interior finite Gabor sections, a retained Hermitian compression B_C satisfying\n\n    rank(B_C)<=2s\n\nand\n\n    tr(B_C^2)\n      >= c * X^(2 delta_*) / L^C,\n\nafter the shallower and far background are included.\n\nOur completed pieces toward SC4 are:\n\n- exact complex Poisson continuation and pair spectrum;\n- finite-section capture for fixed depth;\n- full-lattice scalar Frobenius identity;\n- exact confluent Hilbert floors through size four;\n- far-field shell decoupling;\n- depth-gap suppression costs only powers of L when the band width is D log L/L.\n\nWhat remains is a uniform signed-cluster retention argument across the transition between separated and confluent configurations.\n\n## 5. Large components and the starred lemma\n\nThe graph itself gives a clean combinatorial reduction.\n\nEvery connected component of size s>=5 has at least s-1 edges, and\n\n    s <= (5/4)(s-1).\n\nTherefore\n\n    boxed:\n    # vertices in components of size >=5\n      <= (5/4) * (# edges in a spanning forest of those components)\n      <= (5/4) * (# close depth-band pairs).\n\nSo the exceptional large-cluster population is controlled once one controls close comparable-depth pairs.\n\nThis suggests the narrow starred input:\n\n**EC-star.** Obtain a power-saving upper bound for the number/energy of close comparable-depth off-line pairs at the resolution used by the component graph, strong enough that vertices in size>=5 components contribute only the allowed zero-density error.\n\nEC-star is deliberately stated as a separate interface. The current local zero count alone gives only O(R log T) possible neighbors per zero and does not supply the required power saving.\n\n## 6. Conditional zero-density form\n\nIf SC4 holds and EC-star gives an exceptional large-component count E_large(delta,T), then the number of off-line pairs at depth at least delta satisfies schematically\n\n    boxed:\n    N_off(delta;T)\n      <= T * X^(-4 delta) * L^C\n         + E_large(delta,T).\n\nThe first term is the unconditional small-cluster energy-counting contribution. The second is the single explicit obstruction.\n\nIf EC-star is strong enough that\n\n    E_large(delta,T)\n      <= T * X^(-4 delta) * L^C,\n\nthen\n\n    N_off(delta;T)\n      <= T^(1-4 lambda delta+o(1)),\n\nand for delta>1/(4lambda) this becomes a zero-free statement.\n\n## 7. Why this is a genuine kill-gate rather than another bookkeeping gate\n\nThe algebra from retained cluster energy to a power-law zero-density estimate is now exact and one line long. The unresolved work is no longer m4 combinatorics or G9 normalization.\n\nIt is precisely:\n\n1. prove SC4, the signed <=4 cluster retention inequality;\n2. prove or replace EC-star for large comparable-depth clusters.\n\nThose are the only two interfaces in this reconstruction where genuinely new zero-side information can enter.\n\nCompanion exact ledger: `src/wp83_energy_counting_ledger.py`.\n

## 8. Large-component replacement route

The literature and input audit shows that EC-star is not currently supplied by
the declared local-zero-count or bandwidth-one pair-ceiling inputs.

There is, however, an exact positive-multiplicity mechanism that may remove
close-pair counting entirely.

For an equal-depth layer

    q(v)=sum_j m_j exp(i omega_j v),   m_j in positive integers,

the Fejer triangle gives the spacing-free identity

    integral W_H(v)|q(v)|^2 dv
      = H sum_{i,j} m_i m_j sinc^2((omega_i-omega_j)H/2)
      >= H sum_j m_j^2.

See `WP83_POSITIVE_FEJER_CLUSTER_ENERGY.md`.

The remaining large-cluster problem can therefore be stated as PT-star:

> propagate a polynomial-in-L amount of this positive energy to the
> exponentially amplified endpoint region when the positive amplitudes vary
> by exp(-eps_j v), 0<=eps_j<=D log L/L.

If PT-star is proved, the large-component branch receives its own scalar
energy floor and EC-star is unnecessary.

Thus the current theorem frontier has exactly two possible star closures:

1. **EC-star:** an external/de novo close-pair power saving for the deep
   comparable-depth set;
2. **PT-star:** a spacing-free positive-amplitude endpoint-transfer theorem.

No other unresolved G9 or finite-model calculation is hidden in this step.
