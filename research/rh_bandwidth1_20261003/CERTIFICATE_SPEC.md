# Bandwidth-one certificate class: source definition and finite adversary

Source: Alpöge–Furman arXiv:2608.13637v2, §7.2; formal instance: PairCeiling files in formal-math at commit 2bafb8c88f177284a2123b5fefa2ff84e2365eb6. This specification records the broad class described by the paper and the finite law used to bound it. It does not claim that the external enclosure input has been reproduced.

## 1. Limiting primal certificate problem

Let Ω be the class of locally finite zero configurations, symmetric under ρ↦1−conjugate(ρ). Let z(ω)=N0s(ω)/N(ω) be the simple-critical-zero fraction.

For each bandwidth-one test function f (Fourier support in [-1,1]), let M1(ω;f) and M2(ω;f) denote the first and second trace moments of the associated finite Weil-form compression. Let σ(ω) record the partition of zeros into on-line points and off-line conjugate pairs.

A broad certificate is a configuration functional p satisfying:
1. information restriction: p(ω)=F({M1(ω;f), M2(ω;f): support(f)⊂[-1,1]}, σ(ω)) for some functional F;
2. configuration-wise validity: p(ω)≤z(ω) for every admissible ω;
3. the finite/asymptotic moment relations used to bound these statistics are unconditional and retain their stated error terms.

The best universal density value expressible in this class is the primal supremum
C_BW1 = sup_F inf_{ω∈Ω} F(M1(ω),M2(ω),σ(ω))
subject to F(M1(ω),M2(ω),σ(ω))≤z(ω) for every ω∈Ω.

This is a limiting semi-infinite optimization over functionals of the first two bandwidth-one trace moments and zero partition. The definition is deliberately broad; it is not itself a finite numerical program. The AF rank–trace certificate supplies one admissible F and gives a lower bound. A finite adversarial law supplies an upper bound on every admissible F.

## 2. Matrix certificate constraints and normalization

For an interval (T,2T), normalize N=N(T,2T), d=N+o(N), and use the paper's smoothed Gabor family with L≈log T, X=e^L≤T, modulation spacing 2π/L, and Fourier support of each product in [-L,L].

The compressed real symmetric matrix G̃ admits, up to negligible trace-norm tails, a decomposition G̃=P+Q:
- P is positive semidefinite and comes from on-line zeros;
- off-line conjugate pairs contribute signature (1,1) blocks to Q;
- n₊(Q)≤number of off-line pairs;
- tr(G̃)=(1+o(1))N;
- tr(G̃²)=||G̃||HS²=(R(ψ)+o(1))N;
- tr(P)≤N0 and rank of the simple-on-line part P1 is at most N0s;
- multiplicity bookkeeping: N≥s1+2s2+2p, where s1 counts simple on-line zeros, s2 multiple on-line points, and p off-line pairs.

The finite matrix inequality for P1≥0 and Hermitian Q′ with n₊(Q′)≤b is:
rank(P1) ≥ 2 tr(P1)+4 tr(Q′)−4b−||P1+Q′||HS².

The output functionals are:
- simple and on-line: 2−R(ψ);
- distinct zeros: (3−R(ψ))/2.

For the indicator window R=4/3. For the Montgomery–Taylor window ψ(s)=cos(√2 s) on [-1/2,1/2], R=1/2+(1/√2)cot(1/√2).

## 3. Exact adversarial problem represented by the N=256 law

The source ceiling uses a finite 256-periodic law of marked configurations:
- law weights w_c≥0 with sum_c w_c=1;
- rational positions x_{c,i} in [0,256);
- marks m_{c,i} in {1,2};
- each configuration has sum_i m_{c,i}=256.

The sampled form factor is
S(j)=(1/256) sum_c w_c |sum_i m_{c,i} exp(2π i j x_{c,i}/256)|²,
with grid masses s_j=S(j)/256 at j/256.

For the selected law, define:
C_m=sum_{1≤j≤m}s_j,
C(x)=sum_{j/256≤x}s_j,
D(x)=C(x)−x²/2,
E(x)=integral_0^x D(t)dt.

For a certificate pair (c0,r), with r∈C1[0,1], g=r′ continuous, and r″ integrable (with the stated piecewise regularity), validity at the law is:
c0 + sum_{j=1}^{256} s_j r(j/256) ≤ p,
where p is the configuration functional's value. Its objective is
v=c0+integral_0^1 r(x)x dx.

The source's stability bound is
v ≤ p + |r(1)| |D(1)| + |r′(1)| |E(1)| + (sup_[0,1]|E|) integral_0^1 |r″(x)|dx.
The near-CUE row assumptions and the edge discrepancy bound make the constant small. For band-limited windows with r(±1)=0, the paper's displayed 0.824|r(1)| term vanishes; the remaining error is 2.55×10^-6 times |r′(1)|+integral|r″|.

The law's simple-point fraction is the exact p0 rational stored in LawN256.lean, about 0.68182868746. The source says its law is an optimum of a corresponding exact-rational finite program over marked periodic configurations. As an LP, its explicit finite-support mixture has decision variables w_c and constraints from row form-factor bounds; the configuration catalogue (positions and marks) is fixed by the supplied certificate. That certificate is cited by digest cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8 but is not included in the inspected repository. Thus an independent implementation of the finite LP is blocked by missing input data.

## 4. Conditional status

The analytic stability inequality is formalized. The law's EnclOK hypothesis says the true form-factor values lie within externally computed interval enclosures. The Lean theorem assumes EnclOK; it proves the downstream row inequalities and ceiling implication conditionally. Since the exact law data and interval producer are not in the source tree, the ceiling is not fully replayed here.

## 5. Optimization type

- The broad primal is a semi-infinite function/moment optimization constrained by universal configuration-wise inequalities.
- The adversarial finite law is a rational LP over mixture weights for a specified finite catalogue.
- The AF base lower certificate is a finite matrix inequality with asymptotic analytic moment inputs.
- No finite SDP encoding of the whole broad class is provided by these sources; calling the existing ceiling an SDP would be inaccurate.
- Higher-moment extensions could be formulated as moment/SDP relaxations, but unconditional availability beyond the second moment at bandwidth one is not established by AF. Such an input would be conditional unless independently proved.

## 6. Primal and dual directions

Primal direction: exhibit a functional F of the permitted moment and partition data, prove F(ω)≤z(ω) for every admissible configuration, then use the unconditional explicit-formula estimates to prove F(ω)≥c−o(1).

Adversarial/dual direction: exhibit a probability law μ on admissible configurations whose expected permitted moment data match the allowed constraints. For every valid F,
c ≤ E_μ[F] ≤ E_μ[z].
The N=256 law is such a finite adversarial object and yields the p0 upper benchmark. The source's conditional EnclOK proof is needed to make its stated row constraints rigorous.

No strong-duality theorem between these abstract spaces is asserted here.
