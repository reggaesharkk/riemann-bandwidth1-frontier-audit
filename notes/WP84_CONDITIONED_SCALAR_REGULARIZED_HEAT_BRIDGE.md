# Conditioned scalar-regularized heat bridge

**Decision B — tail closed, generic scalar-curvature payment exceeds the frozen model cushion.** The scalar shift gives a dimension-uniform endpoint tail for the *conditioned* consumer, with no small-ball assumption on the source matrix. But the certified generic scalar-curvature payment has infimum 9, versus the frozen model-relative cushion approximately 0.00274458. No signed scalar saving or theorem-side endpoint estimate is obtained. Strict >79 remains **OPEN**.

This audit starts from `fb16bc83a6b26c51faec17b99ac2555e869ff033` on `codex/c5-c6-attack-20261006`. The consumer and threshold are unchanged. The pre-existing `notebooklm_packet/` was not touched.

## Exact conditioned consumer

For (u=(x+i)/(x-i)), let

```text
q(u) = [1936u^3+(-192-5495i)u^2+(-5695+169i)u+(44+2205i)]/5000,
p(x) = |q((x+i)/(x-i))|^2,
C0 = |q(1)|^2 = 2500529/2500000.
```

Direct rational substitution and cancellation give

```text
p(x) = (12502645x^6-82863712x^5+221347891x^4-303496416x^3
        +224073135x^2-84028544x+12502001)
       /(12500000(x^2+1)^3).

g(x)=p(x)-C0
    =(-20715928x^5+45959989x^4-75874104x^3+46641300x^2
      -21007136x-161)/(3125000(x^2+1)^3).
```

The numerator of (g) has exact degree five: the (x^6) terms cancel, while its leading coefficient is nonzero. Its first nonzero Laurent term at both ends is

```text
g(x) = -(20715928/3125000)/x + O(x^-2).
```

Thus the coefficient is (-20715928/3125000) at (+infty), and the value of the leading term changes sign at (-infty) through (1/x).

### Rational global bounds certified by Sturm

Write (N_g) for the displayed numerator and (D_g=3125000(x^2+1)^3>0). Exact Sturm sequences give:

```text
81 D_g^2 - N_g^2 > 0                       for every real x,
144 D_g^2 - x^2 N_g^2 > 0                  for |x|>=2.
```

The first polynomial has degree 12, no real roots, and is positive at zero. For the second, the Sturm root counts are zero on each of ((-∞,-2)) and ((2,+∞)); it is positive at both endpoints (x=\pm2) and at both infinities. Hence the theorem-grade choices

```text
B_g = 9 >= sup_R |g(x)|,
C_g = 12, with |g(x)| <= C_g/|x| for |x|>=2.
```

The certificate records the exact Sturm variation counts and the replay recomputes them; these constants are not numerical-fit bounds.

## Exact covariance addition and the source normalization

Set (F(H)=\tau p(H)), let (W) be the original centered source Gaussian Hermitian matrix, and let ξ be an independent standard real Gaussian. For rational σ>0,

```text
H_(u,sigma)=H_1+sqrt(u)W+sigma*sqrt(u)*xi*I,
E_(u,sigma)=E F(H_(u,sigma)).
```

At (u=0), (H_{(0,σ)}=H_1), so (E_{(0,σ)}=E_0) exactly. Price's identity for the sum of independent Gaussian directions gives, at every fixed finite dimension,

```text
d/du E_(u,sigma)
  = (1/2) E D^2F_H[W,W] + (sigma^2/2) E tau p''(H)
  = G_source^exact(u,sigma) + G_scalar(u,sigma).
```

Here `G_source^exact = (1/2) E D^2F_H[W,W]` and `G_scalar = (sigma^2/2) E tau p''(H)`. The mixed Hessian term has coefficient `sigma*xi` and expectation zero; equivalently the covariance tensor is the source covariance plus `sigma^2 I tensor I`, with no cross covariance. Since `D^2F_H[I,I]=tau p''(H)`, the factor `1/2` and variance factor `sigma^2` are exact.

The inherited WP84 source calculation identifies

```text
G_source^exact(u,sigma)
 = Re E[A Xi_z + B Xi_zz + C Xi_zzz] + o_T(1)
```

at the *regularized state* (H_{(u,σ)}), with the same existing source covariance/resonance error. This audit retains that (o_T(1)); it does not upgrade the inherited source stencil to an exact finite-(T) identity. The scalar addition does not change the source covariance tensor. Resolvent bounds remain uniform under a real scalar shift, so the already established uniform source-reduction error is unchanged.

The exact augmented asymptotic stencil is consequently

```text
E_(u,sigma)' = Re E[A Xi_z+B Xi_zz+C Xi_zzz]
                +(sigma^2/2) E tau p''(H_(u,sigma)) + o_T(1).
```

The Fourier part of the source stencil remains the one grouped (S_4) channel:

```text
-(1/pi^2) Re E[A T12+B(T22+2T13)+6C(T23+T14)],
```

now evaluated at (H_{(u,σ)}). The scalar Gaussian adds no Fourier covariance term.

The independent replay checks the Gaussian Hessian identity symbolically in dimension one and by direct divided-difference Hessian contraction on finite Hermitian matrices. For diagonal (H=\operatorname{diag}(\lambda_j)), the replay uses

```text
D^2 tr p(H)[V,V]
 = sum_(i,j) p'^[1](lambda_i,lambda_j) V_ij V_ji,
```

where (p'^{[1]}(a,b)=(p'(a)-p'(b))/(a-b)) off the diagonal and (p''(a)) on it. Expansion at (V=W+\sigma\xi I), followed by (E\xi=0,E\xi^2=1), reproduces the exact split and (D^2F[I,I]=\tau p'').

## Exact (p'') certificate and sign

```text
p''(x) = (-20715928x^7+137879967x^6-185937560x^5-222986835x^4
         +615845240x^3-330580347x^2-38558088x+46641783)
        /(1562500(x^2+1)^5).
```

For numerator (N_2) and positive denominator (D_2), the degree-20 polynomial

```text
31^2 D_2^2 - N_2^2
```

has no real roots by its exact Sturm sequence and is positive at zero. Therefore (M_2=31\ge\sup_{x\in\mathbb R}|p''(x)|).

The numerator (N_2) has exactly seven real roots, isolated one apiece in the rational intervals recorded in the certificate:

```text
(-397/250,-793/500), (-329/1000,-41/125), (3/5,601/1000),
(109/125,873/1000), (627/500,251/200), (379/250,1517/1000),
(4327/1000,541/125).
```

They are simple, and the signs of (p'') on the eight complementary intervals are (+,-,+,-,+,-,+,-), since the leading coefficient of (N_2) is negative. Exact rational witnesses also give

```text
p''(0) = 46641783/1562500 > 0,
p''(-2/3) = -15547254589917/580145312500 < 0.
```

Thus scalar smoothing is not monotone for this consumer; no claim (G_{scalar}\ge0) is valid in general.

## Dimension-uniform scalar tail

Condition on (A=H_1+\sqrt u W) and diagonalize it. For each eigenvalue λ, the translated scalar λ+σ\sqrt u,ξ has density bounded by (1/(\sqrt{2\pi}\sigma\sqrt u)). For any (K\ge2),

```text
P(|lambda+sigma*sqrt(u)*xi|<=K)
 <= min(1, sqrt(2/pi)*K/(sigma*sqrt(u))).
```

On this event use |g|≤9; off it use |g(x)|≤12/K. Average over eigenvalues, (W), and (H_1). This proves

```text
|E_(u,sigma)-C0|
 <= TailBound(sigma,u,K)
 := 9*min(1,sqrt(2/pi)*K/(sigma*sqrt(u))) + 12/K.
```

This bound is uniform in dimension, deterministic (H_1), every realization of (W), and (T). In particular, it closes the earlier structured-(W) small-ball dependency for the *augmented endpoint*; it proves no bound on the source curvature integral.

Put (y=\sigma\sqrt u), (c=\sqrt{2/\pi}), and (h=y/c). The infimum over (K\ge2) is explicit. If (h<2), the infimum is (9). If (h\ge2), set

```text
K0 = sqrt(12*y/(9*c)),
K* = clamp(K0,2,h),
Tail_sigma(u) = min(9, 9*c*K*/y + 12/K*).
```

The other branch (K\ge h) decreases to the infimum (9), which explains the outer minimum. When (y\ge16c/3), the unconstrained minimizer lies in ([2,h]) and the value is below 9, so

```text
Tail_sigma(u) = 2*sqrt(108*c/y)
              = 2*sqrt(108*sqrt(2/pi)/sigma)*u^(-1/4).
```

Thus (E_{(u,σ)}\to C_0) uniformly in dimension for each fixed σ>0. For each finite dimension the endpoint identity is

```text
E_0 = C0 - integral_0^infinity [G_source^exact(u,sigma)+G_scalar(u,sigma)] du.
```

The uniform endpoint estimate justifies the (u\to\infty) endpoint uniformly; the source curvature integral itself remains unestimated.

## Quantitative kill gate

The generic scalar payment on ([0,U]), with (y=\sigma\sqrt U), is

```text
Overhead = 9*min(1,c*K/y) + 12/K + (31/2)*y^2,  K>=2.
```

Its global infimum is exactly (9). Indeed, if (y\le cK), the first term is 9. If (y>cK\ge2c), then

```text
(31/2)*y^2 > (31/2)*(2c)^2 = 124/pi > 31 > 9,
```

using only π<4. Conversely, (K=n,y=n^{-2}) gives overhead (9+12/n+31/(2n^4)\to9). This is an analytic infimum proof, not a grid search.

The exact frozen model cushion is

```text
epsilon_model = 34148687712345924132945804854399
                /12442212289373925054228673142500000
              = 0.0027445832716992... .
```

The generic overhead is (9/\epsilon_{model}=3279.186349637698\ldots) times this cushion. Therefore this prescribed generic payment is **quantitatively killed** for the frozen cushion. The tail theorem remains valid and reusable.

## One signed scalar check; no Fourier contraction

At fixed source variance (u), integrating the scalar heat derivative with respect to a separate scalar variance (v) gives the exact endpoint difference

```text
integral_0^(sigma^2*U) (1/2) E tau p''(H_1+sqrt(U)W+sqrt(v)xi I) dv
 = E tau p(H_1+sqrt(U)W+sigma*sqrt(U)xi I)
   - E tau p(H_1+sqrt(U)W).
```

But the required integral has source variance (u) changing simultaneously with scalar variance (v=\sigma^2u). The chain rule adds the source derivative; the fixed-source endpoint identity therefore only redistributes the joint budget and supplies no one-sided saving. The exact (p'') sign witnesses above forbid a general monotonicity shortcut. **Signed scalar improvement: none.**

Conditioning on ξ gives the exact Gaussian heat semigroup in the scalar-translation variable (s): (e^{(\sigma^2u/2)\partial_s^2}) applied to each resolvent statistic as a function of (H+sI). This is not a Poisson-kernel identity and yields no strict multiplicative contraction for the grouped (T_{12}), its derivatives, or the (S_4) channel; the only general sup-norm contraction factor is 1. This branch stops here.

## Remaining theorem-side law

The threshold is (21/200=0.105), so the total curvature required is exactly

```text
C0-21/200 = 2238029/2500000 = 0.8952116.
```

Using the scalar tail at a finite (U), a sufficient remaining source-side theorem would be

```text
integral_0^U [G_source(u,sigma)+G_scalar(u,sigma)] du
 > 2238029/2500000 + Tail_sigma(U) + eta
```

for an explicit η>0, including the inherited (o_T(1)) payment. No such lower bound is proved. The model energy (0.1022554167283008\ldots) and its cushion do not supply an actual zeta-side endpoint bound. Strict (>79) remains **OPEN**.

## Reproducibility

```powershell
python src/wp84_conditioned_scalar_regularized_heat_bridge.py
python src/wp84_conditioned_scalar_regularized_heat_bridge_replay.py
```

The producer derives the rational functions and writes exact Sturm data to the JSON certificate. The independent replay re-derives the consumer, checks all Sturm root counts and signs, the uniform tail and overhead proofs, the augmented Hessian identity, and rejects the 20 listed hostile mutations. The replay imports no producer calculations. Dependency SHA-256 values are embedded in the certificate.
