# WP84 — Physical endpoint averaging and near-product closure

Base commit: `1139e81c5fdfc0ecfc054b892697c6f76f78db31`

Audit branch: `codex/wp84-physical-endpoint-averaging-20261103`

This is an additive local audit. Earlier source, commits, certificates,
counterexamples, and negative results are preserved. Nothing was pushed,
merged, or published.

| Decision | Result |
|---|---|
| `AVERAGED_FOURIER_KERNEL` | **EXACT** |
| `PHYSICAL_CUMULANT_AVERAGING` | **CORRECTION_REQUIRED** |
| `JOINT_ENDPOINT_SELECTION` | **CONDITIONAL** |
| `ORDINARY_CONNECTED_AGGREGATE` | **OPEN** |
| `R400_CONSUMER` | **CONDITIONAL** |

## 1. Parent replay and scope

The checked-out commit is exactly the requested base. The predecessor
endpoint/near-product manifest and sidecar verify, including its ten
artifacts and sixteen base inputs. Its fourteen tests pass under normal
Python, `python -O`, and `python -OO`. The Decision-D density replay and its
exact rational `build()` checks pass. The source interval replay was invoked
in memory and compared with the saved certificate: all 48 labeled source and
conjugate placements agree, and the 24 distinct outward-rounded R400 overlap
intervals are above `799/4000`; its exact row-cumulant lower bound is
`384/625` for every `m>=10`. The E2 safe-lobe script also replays, but that
public scalar-trace sign does not identify the physical filtered cumulant.

These replays confirm finite certificates and inherited source statements.
They do not verify an ordinary-prime aggregate estimate. In particular, the
older parent note's heuristic endpoint scale is corrected here without
rewriting it: Decision B uses

\[
X=T/(2\pi)=e^L,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,\quad
d=\lfloor TL/(2\pi)\rfloor,\quad
M_{end}=\lceil d e^{-\sqrt L/2}\rceil,
\]

and `I_uv=[b+u,b+d-1-v]`, `0<=u,v<=M_end`. Thus
`M_end/d=e^{-sqrt(L)/2}+o(1)` and the physical endpoint-window width is
`h M_end=(1+o(1))T e^{-sqrt(L)/2}`, with `h=2*pi/L`. This is not the wider
`T sqrt(L)` endpoint window or `T/sqrt(L)` Fourier span stated heuristically
in the predecessor near-product discussion. Any phase-cancellation threshold
must use the Decision-B width: endpoint phase oscillation requires
`T |Y| e^{-sqrt(L)/2}` large. The predecessor file remains unchanged.

The inherited source score theorem covers the direct bounded first-strike
endpoint-feature families: for `S_theta(t)=sum_{n<=N} a_n(theta)e^{it log n}`
with its stated integrated coefficient-square bound, both actual endpoint
means are `O_R(1+N/U_T)=O_R(1)`, where
`U_T=(1+o(1))T e^{-sqrt(L)/2}` and
`N/U_T=(1+o(1))e^{-sqrt(L)/2}/(2*pi)->0`. It retains the full prime-power
pool and the original carrier. Markov therefore gives endpoint-good sets
`G_-`, `G_+` of density at least `1/2` each in their actual uniform edge
windows. Their Cartesian pair set has density at least `1/4` in
`W_T={0,...,M_end}^2`. This statement does not transfer to the separate
hidden-prime `source_mask` determinant iterator.

The nonnegative boundary score is the actual crossing energy
`E(I)=||P_I V(1-P_I)||_HS^2`. Its source average on `W_T` is at most
`C_B log(d)`. For any fixed `0<epsilon<1/4`, Markov leaves boundary-good
density at least `1-epsilon` at threshold
`E(I)<=C_B log(d)/epsilon`. Intersecting with `G_- x G_+` gives at least
`1/4-epsilon` of all candidate pairs, without assuming any independence or
correlation between endpoint scores and boundary energy. The inherited
finite-section boundary estimate remains `o(1)` at every such fixed positive
density. Its source constants `C_R,C_B` are implicit, as in the parent.

## 2. Exact endpoint average

For a candidate section let `m_uv=d-u-v` and
`I_uv={b+u,...,b+d-1-v}`. Its normalized Fourier kernel is

\[
K_{uv}(Y)=e^{iTY}\frac1{m_{uv}}
\sum_{k=b+u}^{b+d-1-v}e^{2\pi i kY/L}.
\]

For any probability measure `rho_uv>=0`, `sum rho_uv=1` on any nonempty
source-selected set of candidate pairs, define

\[
w_k(\rho)=\sum_{(u,v)}\rho_{uv}
\frac{\mathbf 1_{b+u\le k\le b+d-1-v}}{d-u-v},
\qquad b\le k\le b+d-1.
\]

Reordering these finite sums proves the exact identity

\[
\mathbb E_\rho K_{uv}(Y)=e^{iTY}\sum_{k=b}^{b+d-1}
w_k(\rho)e^{2\pi i kY/L}.
\]

Every `w_k` is nonnegative, and
`sum_k w_k=sum_(u,v)rho_uv*m_uv/m_uv=1` exactly. For the original uniform
Decision-B measure, `rho_uv=1/(M_end+1)^2`; for a selected subset, `rho` is
its normalized conditional measure. The checker also evaluates an exact
nonuniform rational measure and an explicit finite uniform example.

The closed real form for one candidate row is

\[
\Re K_{uv}(Y)=
\frac{\sin(\pi m_{uv}Y/L)}
{m_{uv}\sin(\pi Y/L)}\cos(\omega_{uv}Y),\quad
\omega_{uv}=T+\frac{2\pi(b+u)}L+\frac{\pi(m_{uv}-1)}L,
\]

with removable singularities interpreted by continuity. Averaging this scalar
identity does not average the positive part: the exact two-section values
`(+1,-1)` have signed average zero and mean positive part `1/2`.

## 3. Physical source correction ledger

For an ordinary-prime tuple and balanced sign word, put

\[
Y=\sum_{j=0}^3\epsilon_j\log p_j=\log(A/B),\quad
v_j=\epsilon_j\log(p_j)/L,\quad
A=\prod_{\epsilon_j=+1}p_j,\quad
B=\prod_{\epsilon_j=-1}p_j.
\]

The original coefficient is `c_p=-log(p)/(a_phi(T)L sqrt(p))`. The parent
physical factor is
`Omega_(4,400)(v) kappa_m(v)`, where

\[
\kappa_m(v)=\sum_{\pi\text{ anchored, ordered}}
(-1)^{|\pi|-1}\prod_{B\in\pi}
D_m\!\left(\sum_{j\in B}v_j\right),\qquad
D_m(x)=m^{-1}\sum_{r=0}^{m-1}e^{2\pi i r x}.
\]

The exact term average over sections is therefore

\[
\Re\!\left[(\prod_jc_{p_j})\Omega_{4,400}(v)e^{iTY}
\sum_{u,v}\rho_{uv}e^{2\pi i(b+u)Y/L}
\kappa_{m_{uv}}(v)\right],
\]

before adding the finite-compression path-boundary correction below. The
same `m_uv` occurs in every block factor of each of the 26 partition terms.
Thus the row cumulant cannot be pulled outside the average, and
`E(prod_B D_m)` cannot be replaced by `prod_B E(D_m)`.

There is an exact comparison to any fixed reference row length `d`:

\[
\kappa_{m_{uv}}(v)=\kappa_d(v)+
\sum_{\pi}(-1)^{|\pi|-1}\left[
\prod_{B\in\pi}D_{m_{uv}}(v_B)-
\prod_{B\in\pi}D_d(v_B)\right].
\]

For `m<=d`, `|D_m(x)-D_d(x)|<=2(d-m)/d`, since each is a normalized
average of unit-modulus terms and `D_d` is the convex combination of the
first `m` terms and the remaining `d-m` terms. Telescoping each product and
summing the 26 terms, with total block count
`1+7*2+12*3+6*4=75`, gives the rigorous bound

\[
|\kappa_m(v)-\kappa_d(v)|\le150(d-m)/d
\le300M_{end}/d=O(e^{-\sqrt L/2}).
\]

This is only a per-tuple pointwise kernel error. Multiplying it by the crude
absolute coefficient mass `(sum_p |c_p|)^4` does not give a useful aggregate
bound, so it does not close the source sum.

For the finite compressed lag trace, a closed hard-band path
`r_1+...+r_4=0`, `|r_j|<=400`, has prefix vertices
`q_0=0`, `q_j=sum_(a<=j)r_a`. If `ell=max(q)-min(q)`, its valid roots in
`I=[k_-,k_+]` are exactly
`[k_- - min(q), k_+ - max(q)]`, with count `m-ell`. Relative to the full
row average, the omitted-root correction is exactly

\[
-\frac1m\sum_{k\in I\setminus I_{r}}
e^{iTY}e^{2\pi i kY/L},
\]

whose absolute value is at most `ell/m<=4*400/m`. This exact identity keeps
the hard band, root interval, orientation, and section start. After summing
the actual path/source coefficients it still requires a source aggregate
estimate; the pathwise bound alone is not enough.

The inherited 26-term ledger has block-count multiplicities `1,7,12,6`
and signs `+,-,+,-`; all six balanced sign words occur once in the ordered
tuple sum. The original fourth-order source has all 16 sign words; the
balanced six-word aggregate below is the remaining target after the
predecessor's separately recorded unbalanced-sector reduction. The inherited
source interval replay checks 48 labeled source and
conjugate placements, with 24 distinct vectors/intervals. There is no extra
factor of six. `A=B` exact equalities are assigned to the pair contractions
by unique factorization. All `A!=B` terms, including near products and
aliases, remain. The preserved tuple `101*103=10403` versus
`97*107=10379` has exact product gap `24`; it is an ordinary-prime summand
when `N>=107`, not an asymptotic lower bound or a legality certificate for a
positive aggregate. Unequal product scales remain in the sum as well.

The public E2 lobe remains separate. Its relevant weighted frequencies are
on the `q=1` principal major arc, and the inherited oversampling pays
`H=M_prod/T`; on `M_prod=T^s`, `s>1`, this is `T^(s-1)`. Neither the public
minor-arc estimate nor the public nonpositive geometric `B4_nc` identity
controls the physical `Omega*kappa_m` source sum or its endpoint correction.
No principal-arc signed remainder or local `H^-1` saving was proved here.

## 4. Joint endpoint selection and exact budget

Let
`G_T(I)=max(0, Re C_T(I))`, where `C_T(I)` is the complete ordinary-prime
physical connected contribution after exact `A=B` pair contractions, with
all 26 terms, six balanced words, coefficients, carrier, and finite-section
correction retained. If the source were to establish

\[
\mathbb E_{(u,v)\ uniform\ on\ W_T}G_T(I_{uv})
<(1/4-\epsilon)\Delta_{max},\quad 0<\epsilon<1/4,
\]

then Markov makes the fraction with `Re C_T(I)>Delta_max` less than
`1/4-epsilon`. The endpoint-good and boundary-good intersection has density
at least `1/4-epsilon`, so strict inequality gives a common section that is
endpoint-admissible, has `E(I)<=C_B log(d)/epsilon`, and satisfies
`Re C_T(I)<=Delta_max`. For any fixed positive density the already-recorded
boundary/row-deletion costs remain `o(1)`.

The supremal sufficient global mean threshold from the guaranteed endpoint
density is `Delta_max/4`; it is approached as epsilon decreases to zero,
but equality at the limiting threshold is not enough for this strict Markov
argument. Numerically exact budgets are:

* `epsilon=1/8`: common necessary-condition density at least `1/8` and mean
  budget `Delta_max/8 = 3675673694911/1186000000000000` (the predecessor
  lemma);
* `epsilon=1/16`: density at least `3/16` and mean budget
  `3 Delta_max/16 = 11027021084733/2372000000000000`;
* as `epsilon -> 0+`: density tends to `1/4` and the strict mean threshold
  tends to `Delta_max/4 = 3675673694911/593000000000000`.

This proves a sharper conditional selection lemma, not its hypothesis. If
the true endpoint-good density is known as `gamma_T>=1/4`, the exact general
condition is mean positive excess `<(gamma_T-epsilon)Delta_max` while the
boundary-good threshold is `C_B log(d)/epsilon`. No source estimate for that
mean positive excess was found. Averaging `C_T` and then taking positive
part cannot be interchanged, so a signed averaged Fourier kernel does not
establish this premise.

## 5. Ordinary-prime aggregate and final gate

The source group is indexed by the exact integer pair `(A,B)`, but the
coefficient of a pair retains every labeled prime split, the original
`prod c_p`, physical filtered overlap, 26-term physical row cumulant,
section carrier, and finite root corrections. Unique factorization removes
only exact `A=B` pair contractions. It gives no cancellation for `A!=B`.
The cutoff gives `N/T->0` but
`N^2/T~T e^{-2 sqrt(L)}/(2*pi)->infinity`; for products up to `N^2`, the
integer-grid lower separation permits
`T|log(A/B)|` as small as order `T/N^2->0`. That observation does not assert
prime products realize every close integer pair.

The old one-atom positive physical certificate and the physical/geometric
kernel mismatch remain intact. The former includes proper prime powers and
is not an ordinary-prime aggregate counterexample. The latter prevents
importing the geometric Gram sign; it does not prove an arithmetic lower
bound. In particular, the exact tuple `(p,p^2,p^3,p^2)` and its finite
permutation/conjugation family with coefficient mass `O_R(L^-4)` remain a
proper-power atom, not an ordinary-prime lower bound. Finite exact examples, near-alias intervals, and tests below do not
replace asymptotic prime-correlation estimates.

**Smallest missing source-valid estimate:** prove either the direct
common-section inequality `Re C_T(I_T)<=Delta_max+o(1)` on a section also
satisfying the endpoint and boundary requirements, or the sufficient uniform
pair-average statement

\[
\limsup_{T\to\infty}\mathbb E_{(u,v)\ uniform\ on\ W_T}
\max(0,\Re C_T(I_{uv}))<\Delta_{max}/4.
\]

It must control the physical ordinary-prime near-product and q=1 principal
arc contributions with the actual source weights and finite-section terms.
No such estimate or source-admissible counterexample was established.
Therefore the ordinary aggregate is **OPEN** and the R400 consumer remains
**CONDITIONAL** on this inequality and the previously listed pair/zero-side
obligations. The conditional `68.820273%` route, strict greater-than-79%
claim, and RH all remain open.

## 6. Reproduction and evidence

The exact checker is `src/wp84_r400_physical_endpoint_averaging.py`; its
rational ledger is `evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_LEDGER.json`.
Independent tests are in `tests/test_wp84_r400_physical_endpoint_averaging.py`.
Parent and current test logs, the source inventory, and the complete SHA-256
manifest are listed in `evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SHA256_MANIFEST.json`
and its `.sha256` sidecar. Tests replay in normal, `-O`, and `-OO` Python.
The initial ledger producer's Fraction-serialization failure and its repair
are preserved in `evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_INITIAL_SERIALIZATION_FAILURE.log`.
Their passing status verifies finite identities and certificates only; it
does not prove the unresolved source-weighted aggregate estimate.
