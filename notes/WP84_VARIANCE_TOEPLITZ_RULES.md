# WP84 — exact modulated-Toeplitz multiplication rules for the variance map

Date: 2026-10-04

Status: **FOUR-BRANCH ALGEBRA CLOSED; THE CLAIM THAT MERTENS AUTOMATICALLY ISOLATES tr(R) IS NOT YET JUSTIFIED**

## 1. Prime block factorization

For y=log n write

    Cplus(y)=cL D_y T_y D_y,    cL=2*pi/L,

where

    (D_y)_{kk}=exp(i*tau_k*y/2),
    (T_y)_{kl}=A_{k-l}(y).

Because f_y(x)=phi(x-y/2)phi(x+y/2) is unchanged by y -> -y,

    T_{-y}=T_y,
    Cminus(y)=Cplus(-y)=cL D_y^* T_y D_y^*.

The real cosine block is exactly

    C(y)=(Cplus(y)+Cminus(y))/2.

The normalized prime block is

    B_n= - Lambda(n)/(pi*sqrt(n)*a*L) * C(log n).

## 2. Exact four-branch identity

For arbitrary A, with no commutation assumption,

    C(y) A C(y)
      = cL^2/4 * (Splus + Dplus + Dminus + Sminus),

where

    Splus  = D T D A D  T D,
    Dplus  = D T D A D* T D*,
    Dminus = D* T D* A D T D,
    Sminus = D* T D* A D* T D*.

The S branches are same-sign / sum-frequency branches. The D branches are mixed-sign / difference-frequency branches.

Companion exact algebra gate: `src/wp84_variance_branch_algebra.py`.

## 3. Phase content

Using tau_k=T+k h with h=2*pi/L, a same-sign summand carries phase

    exp(i*(tau_k+tau_p+tau_q+tau_l)*y/2),

whose carrier contains 2T.

A mixed-sign summand carries

    exp(i*(tau_k+tau_p-tau_q-tau_l)*y/2)
      = exp(i*pi*(k+p-q-l)*y/L),

so the height T cancels exactly.

That is the fundamental algebraic split.

## 4. Exact prime-square variance map

Put

    kappa_n = Lambda(n)^2/(pi^2*n*a^2*L^2).

Then

    V(A)=sum_{n<=X} kappa_n C(log n) A C(log n).

So V splits exactly into difference-frequency and sum-frequency parts.

## 5. What Chebyshev--Mertens really supplies

The public formal source proves

    sum_{n<=x} Lambda(n)^2/n
      = (log x)^2/2 + O(log x),

with an explicit error constant.

Hence the total square mass is source-closed:

    sum_{n<=X} kappa_n
      = 1/(2*pi^2*a^2) + O(1/L).

For slowly varying scalar weights, Abel summation likewise turns this measure into the y dy density.

But that fact alone does not evaluate the operator-valued V(A), because the four branches carry nontrivial modulations.

## 6. Why scalarization is not automatic

For the mixed-sign branch the residual phase is a low lattice frequency exp(i*pi*m*y/L), and T_y still sandwiches the full matrix A.

For the same-sign branch the carrier is of size 2T. A sum of the form

    sum Lambda(n)^2/n * exp(i*(2T+O(T))*log n) * matrix_amplitude(n)

is not controlled by ordinary Chebyshev--Mertens.

The public P_X P_X theorem does control an O2 sum-frequency branch, but only after inserting the special translation kernel Phi(tau-sigma)^2 and integrating over the full square. An arbitrary intermediate resolvent R_S(z) is not known to have that translation-invariant kernel.

So `prop_PP` cannot currently be imported as a black-box theorem for V_S(R_S).

## 7. A sufficient scalarization theorem

A strong sufficient result would be

    V_S(A)=alpha_S*tau_d(A) I + beta_S*A + o_op(1)

uniformly for the actual intermediate resolvents.

But full operator convergence is stronger than needed.

The actual Lindeberg scalar is only

    sum_n kappa_n tau_d(R C(y_n) R C(y_n) R).

So the minimal target is a trace-only limit

    sum_n kappa_n tau_d(R C(y_n) R C(y_n) R)
       = Vfun[m_R](z) + o(1),

uniformly along the permutation process.

## 8. Two concrete subgates

V-diff: control the mixed-sign low-frequency branches using exact carrier cancellation and Toeplitz overlap geometry.

V-sum: prove the same-sign carrier-2T branches are negligible, or identify their nonzero limit, with the resolvent inserted.

The source second-moment theorem suggests V-sum should be small in a translation-invariant setting, but the resolvent-weighted extension is a new theorem obligation.

## 9. Current consequence

The multiplication rules are now explicit, but they do not yet collapse the variance to tr(R). This removes one tempting unjustified shortcut and gives the next attack concrete harmonic-analysis targets.