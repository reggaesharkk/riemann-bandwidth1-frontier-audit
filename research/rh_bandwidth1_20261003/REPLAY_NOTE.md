# Baseline replay note

## Replayed from source formulas

Let x=1/√2. The paper states
R(ψ0)=4/3,
R(ψMT)=1/2+x cot(x),
C0=2−R(ψMT)=3/2−x cot(x),
C1=(3−R(ψMT))/2=(C0+1)/2.

The distinct-zero and simple-zero deductions are sourced from the same rank–trace/inertia chain. Therefore:
- indicator simple: 2−4/3=2/3;
- indicator distinct: (3−4/3)/2=5/6;
- MT simple: C0;
- MT distinct: C1.

For the 256-periodic PairCeiling law, the exact p0 rational is read from the source LawN256 declaration. The script evaluates that rational and verifies its relation to the displayed upward decimal 0.6818287. This is a conditional external-enclosure input, not an unconditional density lower bound.

## Numerical method and error control

The implementation uses Fraction throughout:
1. Bisection constructs a rational enclosure for x=sqrt(1/2).
2. Alternating Taylor sums for sin and cos use exact rational terms and the next alternating term as a rigorous remainder bound on [0,1].
3. Monotonicity of sin and cos propagates endpoint enclosures; positive interval division bounds cot(x).
4. Decimal output is outward-rounded from rational endpoints. No floating-point library is used in the computation.

The output contains lower/upper decimal endpoints, source display values, differences from those rounded displays, exact source formulas, input provenance, and per-value pass scope.

## Replay scope

The arithmetic replay checks all five requested numerical targets. The exact finite matrix pilot checks the algebraic identities and rank–trace inequality on synthetic rational matrices. It does not reconstruct zero-sum estimates, prime sums, asymptotic matrix compression, or re-prove the analytic input. The upstream formalization remains pinned but has not been cloned or built by this project.
