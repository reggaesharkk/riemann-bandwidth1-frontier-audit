# WP84 source-matched signed residual: pair-sector audit

Decision **E**: the exact signed residual and its pair/distinct split survive
reconstruction, and a source-legal family already falsifies any universal
favorable-sign claim for the balanced-pair coefficient. No negative constant
saving is earned. One exact weighted full-source inequality remains open.
Strict >79% remains OPEN.

This is an additive audit from branch `codex/c5-c6-attack-20261006`, starting
at `78b056687dfaacf5493334125eaa3120811c1969`. It leaves the unrestricted
positive-part route frozen and does not use the 453 unmasked orbit count as a
mask or arithmetic bound. The full prime pool, original R=6000 factors and
paths, natural cutoff, prime-power bounded-gate equivalence, and unsplit root
sum are retained. `notebooklm_packet/` is untouched.

## Exact source object and signed split

Use `X=T/(2*pi)`, `L=log X`, `N=floor(exp(L-sqrt(L)))`,
`h=2*pi/L`, `d=floor(TL/(2*pi))`, `I0={0,...,d-1}`, and
`c_m=-Lambda(m)/(a_phi(T)*L*sqrt(m))`, with `a_phi(T)->1`. For an original
ordered closed path `ell`, `|ell_j|<=6000`, `sum ell_j=0`, set
`q_0=0`, `q_j=sum_{r<=j}ell_r`, `rho=d-max(q)+min(q)`, and
`i_min=-min(q)` on `I0`. The unaltered root kernel is

```text
K_ell(lambda) = exp(i*(T+h*i_min)*lambda)/d
                 * sum_{r=0}^{rho-1} exp(i*h*r*lambda).
```

In particular, after writing `lambda=mL+delta`, the factor
`exp(i*T*mL)` remains. No sharp-overlap kernel or alias-periodicity claim is
used. The original slot factors are `f_0^eps(s)=1-s` and, for nonzero `ell`,
`f_ell^+(s)=(1-exp(2*pi*i*ell*s))/(2*pi*i*ell)`,
`f_ell^-=conjugate(f_ell^+)`; the prefix phase is
`exp(2*pi*i*sum_j eps_j*q_(j-1)*log(p_j)/L)`.

For pair slots `a,b`, after the already-justified bounded-gate prime-square
PNT reduction, retain

```text
phi_ab(s) = 2 Re(f_(ell_a)^+(s) f_(ell_b)^-(s)
                    exp(2*pi*i*(q_(a-1)-q_(b-1))*s)),
k_ab      = integral_0^1 s*phi_ab(s) ds.
```

Let `D5,D6` denote the all-distinct ordinary-prime contributions on the
original degree-five/six paths, with all signs, root indices, windows and
carrier. Let `Q3,Q4` denote the same original degree-five/six path sums after
choosing respectively one of the ten/fifteen balanced slot pairs, replacing
that pair only by `k_ab`, and retaining the distinct visible 3-/4-prime
correlation, its exclusions, filters, phases, kernel and carrier. Then the
exact signed reduction is

```text
F_T       = - (11501/12500)*(D5+Q3)
            + (137641/250000)*(D6+Q4),
F_pair   = - (11501/12500)*Q3 + (137641/250000)*Q4,
F_dist   = - (11501/12500)*D5 + (137641/250000)*D6,
F_T      = F_pair + F_dist.
```

The last split is exact. In the inherited bounded signed gate,
`J_full=(137641/250000)*Pair6_6000 + Re F_T + o(1)`. This uses the already
proved global collision and complete balanced `2+2+1+1` removals; it does not
promote a per-alias or per-mask estimate. The retained raw census remains
degree five `192=32+160` and degree six `544=64+480`, where the summands are
all-distinct and balanced-one-pair orientation/sign/equality labels.

## Exact pair coefficient: formula, symmetry and a sign census

For all path geometries the exact finite-filter formula is the displayed
integral, and its value depends only on
`(ell_a,ell_b,q_(a-1)-q_(b-1))`. The following symmetries follow by complex
conjugation and commutativity:
`k(a,b,q)=k(b,a,-q)` and `k(-a,-b,-q)=k(a,b,q)`.
There is a finite closed form for every such triple, without enumerating
closed paths. Expand
`f_a^+ f_b^- exp(2*pi*i*q*s)=sum_n P_n(s) exp(2*pi*i*n*s)`, where each
`P_n` has degree at most two and the candidate frequencies are
`q,q+a,q-b,q+a-b` (with coincident frequencies combined). Define
`J_j(n)=integral_0^1 s^j exp(2*pi*i*n*s) ds`. Then
`J_0(0)=1`, `J_j(0)=1/(j+1)`, `J_0(n)=0` for nonzero integer `n`, and
integration by parts gives
`J_j(n)=1/(2*pi*i*n)-j*J_(j-1)(n)/(2*pi*i*n)` for `n!=0` and `j>=1`.
Consequently
`k_ab=2 Re sum_n sum_(j=0)^2 P_(n,j) J_(j+1)(n)`, an exact finite
rational/pi expression. The zero-lag factors are polynomials `1-s`, so the
same formula covers zero increments; coincident frequencies are added before
the real part. This is an evaluation formula, not an exhaustive sign census.
The certificate gives a complete exact sign census for the explicit
`ell_a=ell_b=0` subfamily (not a false claim to have exhausted all
`12001`-lag path geometries):

```text
k(0,0,q) = 2 integral_0^1 s(1-s)^2 cos(2*pi*q*s) ds
          = 1/6                         if q=0,
          = -1/(2*pi^2*q^2)             if q is a nonzero integer.
```

For `q!=0`, two integrations by parts, or direct integration of
`s-2s^2+s^3`, give `integral s cos=0`, `integral s^2 cos=2/(2*pi*q)^2`,
and `integral s^3 cos=3/(2*pi*q)^2`; hence the negative value above. Both
signs occur on actual closed R=6000 paths: the all-zero path gives `q=0`;
`ell=(0,1,0,-1,0)` with pair `(a,b)=(1,3)` gives `q=-1`. Appending a
zero gives the degree-six example.

There is also an exact parameter-tuple count within this subfamily. If `t`
increments lie strictly between the two pair slots in a degree `b` path,
there are `b-1-t` slot-pair placements. Feasible relative prefix differences
are every integer `q` with
`|q|<=M_t=6000*min(t,b-2-t)`: the internal increments sum to `-q`, and the
remaining non-pair increments sum to `q`. Thus, counting `(slot-pair,q)`
tuples only:

| Degree | `t : placements, M_t` | Positive | Negative | Zero |
|---|---|---:|---:|---:|
| 5 | `0:4,0; 1:3,6000; 2:2,6000; 3:1,0` | 10 | 60,000 | 0 |
| 6 | `0:5,0; 1:4,6000; 2:3,12000; 3:2,6000; 4:1,0` | 15 | 144,000 | 0 |

These are **parameter-tuple multiplicities**, not counts of complete closed
paths, prime tuples, or distinct coefficient values. They show decisively that
the pair coefficient has no uniform favorable sign; they do not give the sign
of `Q3` or `Q4`, because the remaining visible correlation is not known to be
nonnegative.

## Operator/cumulant attack and obstruction

No exact full finite-R identity for all of `F_T` as a finite combination of
the proposed `tau(DY^3)`, `tau(V(Y)Y^2)`, `tau(DY^4)`, `tau(V(Y)Y^3)`, or
`tau(V2(Y,Y)Y^2)` terms was established. The prior conditional cubic identity
for `Q3`,
`Q3=5*tau(D*Y^3)+5*tau(V(Y)*Y^2)+o(1)`, applies only under its inherited
bounded-gate/source reductions and does not represent `Q4` or the whole
residual. It gives no sign. The prime-partition inclusion/exclusion is an
exact distinctness identity; no cumulant/Möbius rearrangement with a
source-derived PSD remainder and a saving was obtained. No Gaussian law for
`Y` is assumed. The auxiliary Gaussian covariance object encodes only the
certified prime-square contraction.

A scalar sign shortcut is already falsified exactly: for
`P(x)=(137641/250000)x^6-(11501/12500)x^5`, `P(1)<0` while `P(-1)>0`.
This is an algebraic falsifier, not an arithmetic counterexample. Together
with the source-legal positive and negative `k_ab` examples, it rules out
inferring a favorable sign from the consumer coefficients or covariance
alone. No source-compatible counterexample to the target inequality is
claimed.

## Numerical gate and the single remaining theorem

The exact threshold remains

```text
limsup Re F_T <= Jstar - (137641/250000)*Pair6_6000 - eta,
Jstar = 64788151489666079/572357731837500000, eta>0.
```

The inherited pair-main lower certificate makes the required saving at least

```text
g9 = 43770221409581023769108432686241
     /21264421581420459982848000000000000
   = 0.0020583781807554428... .
```

The newly audited signed saving is exactly **0 proved**; its ratio to `g9` is
0 and the remaining positive requirement is at least `g9`, plus `eta`. The
existing complete collision removals and central one-prime-side estimates
pay only `o(1)`. They cannot pay a positive constant. Therefore the one
remaining analytic target is the source-weighted estimate for the exact
`F_T` displayed above, with all original ordinary-prime tuples through `N`,
path filters, closed paths, root sums, carrier and tails, and an upper bound
strictly below the pair-main cap by a positive constant. Existing estimates
prove no such signed saving. This is an unresolved mathematical estimate,
not a proof that the inequality is false.

## Verification

Run from the repository root:

```powershell
python src/wp84_source_matched_signed_residual.py
python src/wp84_source_matched_signed_residual_replay.py
```

Both programs use only the Python standard library. The independent replay
reconstructs the rational budget, lag-zero census, feasible-difference
counts, input hashes and scope limitations without importing the producer;
it also tries all 20 required hostile mutations and requires each to fail.
Neither script numerically samples primes or purports to prove the missing
asymptotic inequality.
