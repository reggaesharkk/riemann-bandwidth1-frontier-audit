# Conditioned rank-six heat curvature: sign failure and integrated target

**Decision E:** universal pointwise curvature positivity is false even on
exact rank-two sharp-Loewner 2x2 states. The bounded positive-energy route
therefore reduces to one explicit finite-u state-average estimate plus a
dimension-uniform large-u tail bound. Neither is proved here; the conditioned
79% energy gate remains open, and strict >79% remains OPEN.

This audit starts from local commit
`97d52cfb784feb300197984a78e0d36ea4387dbb` on
`codex/c5-c6-attack-20261006`. It freezes the conditioned cubic, energy
consumer and threshold. It does not alter the direct signed-residual result,
use the discarded F61 positivity shortcut, or touch `notebooklm_packet/`.

## Exact Fourier and resolvent coefficients

Use

```text
q(u) = (1936 u^3 + (-192-5495i)u^2 + (-5695+169i)u + (44+2205i))/5000,
U=(H+iI)(H-iI)^(-1)=I+2iR, R=(H-iI)^(-1).
```

The exact unit-circle coefficients, recomputed by Gaussian-rational
convolution of the four coefficients of `q`, are

```text
c0 = 17826383/6250000
c1 = -42431/12500000 + (6816213/3125000)i
c2 = -23150443/25000000 - (36401/6250000)i
c3 = 1331/390625 - (53361/312500)i.
```

Expanding `U^2=I+4iR-4R^2` and
`U^3=I+6iR-12R^2-8iR^3` gives

```text
E(H)=tau(Q*Q)=C0+2 Re[A m(i)+B m_z(i)+C m_zz(i)],
m_z(i)=tau(R^2), m_zz(i)=2 tau(R^3),
C0=2500529/2500000,
A=-2589491/781250 -(11532549/3125000)i,
B=22894891/6250000 +(3238061/1562500)i,
C=-53361/78125 -(5324/390625)i.
```

In particular `q(1)=(-3907-3121i)/5000`, so
`|q(1)|^2=C0=2500529/2500000=1.0002116`, not 1. The independent replay
checks these coefficients exactly and compares the trace identity against
direct Cayley evaluation on seeded arbitrary finite Hermitian matrices.

## Heat-flow stencil and the Fourier channel

For the inherited co-moving bridge `H_u=H_1+sqrt(u)W`, define
`C_u(z)=partial_u m_u(z)`. Exact differentiation gives

```text
E_u'=2 Re[A C_u(i)+B partial_z C_u(i)+C partial_z^2 C_u(i)].
```

Using the already-certified resonant normalization
`C_u=(1/2) E Xi_z+o(1)` and its z derivatives yields

```text
E_u'=Re E[A Xi_z+B Xi_zz+C Xi_zzz]+o(1), at z=i.
```

The source Gaussian is the one fixed by the circular prime field:
`W=diag(h)+[diag(alpha),J]`, `alpha=Im Z_L`,
`h=2 Re Z_L-2 Im(Z_L'/L)`, and
`Z_L(tau)=sum_(p<=X) gamma_p*(-log(p)/(L*sqrt(p)))*exp(i*tau*log(p))`.
The `gamma_p` are independent standard circular complex Gaussians with
`E|gamma_p|^2=1`, `E gamma_p^2=0`; the scale-one grid covariance is
`K_L(r)=L^-2 sum_(p<=X)(log p)^2/p*exp(i*2*pi*r*log(p)/L)`. This inherited
ensemble is retained; it is not replaced by GUE or an independent-entry
matrix model.

Here the existing finite-d formulas are retained verbatim:

```text
Xi_z = <r1,r2>/(3d)-T12/pi^2+<h1,h2>/d-(<r2,q1>+<r1,q2>)/(2d)
Xi_zz = (<r2,r2>+2<r1,r3>)/(3d)-(T22+2T13)/pi^2
        +(<h2,h2>+2<h1,h3>)/d-(<r3,q1>+<r2,q2>+<r1,q3>)/d
Xi_zzz = 2(<r2,r3>+<r1,r4>)/d-6(T23+T14)/pi^2
         +6(<h2,h3>+<h1,h4>)/d
         -3(<r4,q1>+<r3,q2>+<r2,q3>+<r1,q4>)/d.
```

The Fourier leakage remains one signed channel:

```text
-(1/pi^2) Re E[A*T12+B*partial_z(T12)+C*partial_z^2(T12)],
partial_z(T12)=T22+2T13,
partial_z^2(T12)=6(T23+T14).
```

Both displacement commutators require the corrected `S4` kernel
`sum_(r!=0)e^(irt)/r^4`; replacing it by `S2` loses two powers. The source
notes bound the base channel width by 2x4 and its twice-differentiated state
by at most 2x8. With the conditioned `A,B,C` inserted, I found no exact PSD
coefficient matrix or positive-energy completion. The exact sign counterexample
below already rules out a universal PSD representation of the entire
pointwise curvature, though it does not classify every possible indefinite
channel matrix.

## Hostile pointwise sign test

For a sharp-Loewner state in dimension two, set
`J=[[0,1/pi],[-1/pi,0]]`, `a=(1,0)`, and
`H=diag(h)+[diag(a),J]`. Then `[D,H]` has exact rank two and the resolvent
inherits the rank-two displacement identity. Substitution into the exact
`Xi_z,Xi_zz,Xi_zzz` formulas gives two exact opposite signs:

```text
h=(0,0), H=[[0,1/pi],[1/pi,0]]:
  curvature = pi^2(3+pi^2)P(pi^2)/(18750000(1+pi^2)^5),
  P(x)=46641783x^3-142650593x^2-135154723x+45959989 > 0 for x=pi^2.

h=(1,-1), H=[[1,1/pi],[1/pi,-1]]:
  curvature = -pi^2 Q(pi^2)/(18750000(1+2pi^2)^5) < 0,
  Q(x)=-137879967+221624213x+1018618526x^2
       +183157196x^3+369045432x^4 > 0 for x>9.
```

For the first sign, `pi^2>9`, `P(9)=21276729256`, `P'(9)=8631087872`,
and `P''(x)>0` for `x>=9`, hence `P(pi^2)>0`. The second sign follows
since `-137879967+221624213*9>0` and the remaining terms are positive. The two matrices meet the exact rank-two
sharp-Loewner structural test. They are deterministic states of the
covariance primitive, **not** samples from the conditioned Gaussian
expectation and not arithmetic counterexamples. Thus pointwise positivity is
falsified; positivity of `E_u` does not imply positivity of `E_u'`.

The actual integrated Gaussian expectation could still be positive enough.
No argument here turns the statewise examples into a claim about that
expectation.

## Finite-u deterministic bound

For Hermitian `H`, `||R||<=1`. The finite compression `J` of the discrete
Hilbert transform has `||J||<=1`; therefore each normalized diagonal
bilinear among `r_a,h_a,q_a` has modulus at most 1. Also

```text
|T_ab| <= (2/d) sum_(r=1)^(d-1) (d-r)/r^2 <= 2*zeta(2)=pi^2/3.
```

Consequently
`|Xi_z|<=8/3`, `|Xi_zz|<=8`, and `|Xi_zzz|<=32`. Keeping the Fourier
contribution grouped until this deterministic envelope is applied gives

```text
|E_u'| <= M=(8/3)|A|+8|B|+32|C| ~= 68.7587065028,
integral_0^U0 E_u' du >= -M*U0.
```

The coefficient norm squares are exact:
`|A|^2=240287104662697/9765625000000`,
`|B|^2=691936658537417/39062500000000`, and
`|C|^2=71213253001/152587890625`. This finite bound is dimension-uniform
but has the wrong scale and gives no positive curvature lower bound.

## Large-u tail and the exact next integrated target

For every fixed finite dimension the inherited invertibility argument gives
`E_u -> C0`. It does not provide a bound uniform in dimension. A deterministic
reduction makes the missing input explicit. Let
`S0=15736/5000` and `S1=23046/5000`, obtained by rational upper bounds for
`sum |q_j|` and `sum j|q_j|`. On the unit circle,

```text
||q(u)|^2-|q(1)|^2| <= K/sqrt(1+lambda^2),
K=4*S0*S1.
```

Writing `H_u=sqrt(u)*(W+H_1/sqrt(u))`, any `delta>0` gives

```text
|E_u-C0| <= K*(omega_u(delta)+1/(sqrt(u)*delta)),
omega_u(delta)=E tau(1_{|W+H_1/sqrt(u)|<=delta}).
```

There is no source-uniform, dimension-uniform small-ball estimate for this
actual sharp-Loewner Gaussian ensemble among the cited closed results. This
is the precise missing tail hypothesis; fixed pole distance alone does not
bound the fraction of eigenvalues near zero after rescaling.

The theorem target is `E_0<21/200=0.105`. The exact total curvature required
is
`C0-21/200=2238029/2500000=0.8952116`. The frozen model energy is
`1272283602671916206561064875108101/12442212289373925054228673142500000`
(`0.1022554167283008...`), leaving model cushion
`34148687712345924132945804854399/12442212289373925054228673142500000`
(`0.0027445832716992...`). This is only a model cushion.

For a concrete split, take `U0=1` and reserve half the model cushion as an
absolute endpoint tail allowance:

```text
epsilon_tail = 34148687712345924132945804854399
               /24884424578747850108457346285000000,
|E_1-C0| <= epsilon_tail,
integral_0^1 E_u' du >=
  4462194845986506963257044060880661/4976884915749570021691469257000000
  = 0.8965838916358496....
```

Together these would imply the required total integral. Current deterministic
lower bound on this finite interval is only `-M`, missing the target by
approximately `69.6552903944`; the tail allowance is unproved. No finite
zeta-side energy upper bound `U_bound` has been established, so the distance
to `0.105` is unknown. The value `79.5489...%` remains a model output only.

For comparison only, the inherited frontier consumer has
`a_*^3=13891/9660` and coefficient proxy about `13.00888`, versus `9.85229`
for the conditioned cubic. Pole scaling improves its crude envelope to
`M_*=(8/3)|A_*|/a_*^3+8|B_*|/a_*^4+32|C_*|/a_*^5 ~=59.7168133840`,
smaller than conditioned `M~=68.7587065028`. Both are far too large to prove
the required integrated bound; no PSD channel or theorem advantage follows.
The active consumer remains the conditioned cubic.

## Verification

```powershell
python src/wp84_conditioned_rank6_heat_curvature.py
python src/wp84_conditioned_rank6_heat_curvature_replay.py
```

The producer uses exact rational complex arithmetic. The independent replay
recomputes the Fourier/resolvent coefficients, checks Hermitian regression
matrices, verifies both structural sign witnesses and their exact signs,
checks the covariance factors, S4 grouping, finite-u envelope, threshold and
tail split, and rejects 20 hostile mutations. The exact S4 kernel and
conditioned rank-six consumer retain their existing independent project
replays; none of these checks proves the missing expected integrated law.
