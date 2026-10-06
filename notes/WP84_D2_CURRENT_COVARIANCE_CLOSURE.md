# WP84 — D2 resonant sector closes at current-prime covariance level

Date: 2026-10-05

Status: **NO HIGHER CURRENT-PRIME CORRELATIONS ENTER D2; RESONANT D2 IS A DETERMINISTIC QUADRATIC FUNCTIONAL OF THE TWO alpha/beta COVARIANCE KERNELS**

No percentage theorem is claimed here.

This note combines four previously separate reductions:

1. D2 current/state leave-one-out decoupling;
2. removal of proper prime powers from D2;
3. rank-three BR displacement closure;
4. exact resonant alpha/beta covariance kernels.

The consequence is stronger than the individual statements:

> once the state resolvent R is fixed independently of the current prime p,
> the complete second-order primitive tr((B_p R)^2) is quadratic in the
> current scalar fields alpha_p,beta_p.  Therefore D2 uses **only second
> current-prime covariance**.  No E2/four-prime theorem is needed to average
> the current block.

Higher arithmetic memory survives only through the evolving state R.

## 1. Fixed state and current scalar fields

Fix a subset/Bernoulli state and a nonreal z.

Write

    R=(H-zI)^(-1),

    a=Im Q_state,

    u=R1,
    v=Ra,

and for the current ordinary prime p,

    alpha=alpha_p,
    beta=beta_p.

The current block is

    B
      = M_beta
        + [M_alpha,J].

Everything below is exact at finite d.

## 2. diag(BR) is linear in alpha,beta

The rank-three scalar formula gives

    x:=diag(BR)

      =
      beta odot r
      + pi^(-2)[
          u odot L_alpha v
          - v odot L_alpha u
        ],

where

    r=diag R,

    L_alpha
      = M_alpha K2-K2 M_alpha.

Since L_alpha is linear in alpha,

    boxed:
    x
      = A_alpha alpha
        + A_beta beta

for two deterministic d by d matrices A_alpha,A_beta depending only on the
state R,a.

Explicitly,

    A_beta=diag(r),

and A_alpha is read directly from the displayed L_alpha formula.

## 3. [D,BR] is linear in alpha,beta

The exact rank-three factorization is

    [D,BR]
      =
      pi^(-1)[
        1 w^T
        + (s-alpha)u^T
        - t v^T
      ],

with

    w=R alpha,

    s=Bv,

    t=Bu.

But

    Bf
      =
      beta odot f
      + alpha odot (Jf)
      - J(alpha odot f),

so w,s,t are each linear in alpha,beta.

Therefore

    boxed:
    C:=[D,BR]
      =
      C_alpha[alpha]
      + C_beta[beta],

where C_alpha and C_beta are deterministic linear maps once the state is
fixed.

## 4. The whole D2 primitive is quadratic

The exact trace-square identity is

    tr((BR)^2)

      =
      sum_i x_i^2
      - sum_{i!=j}
          C_ij C_ji/(i-j)^2.

Because both x and C are linear in alpha,beta, this is a quadratic form:

    boxed:
    tr((BR)^2)
      =
      Q_aa(alpha,alpha)
      + Q_ab(alpha,beta)
      + Q_ba(beta,alpha)
      + Q_bb(beta,beta),

for four deterministic bilinear forms Q_* depending only on the fixed state.

Thus averaging over the current prime requires only

    E alpha alpha^T,
    E alpha beta^T,
    E beta alpha^T,
    E beta beta^T.

No higher current-prime moment appears.

## 5. Resonant covariance substitution

The resonant prime-square calculation gives

    boxed:
    C_aa
      = (1/(4a_phi^2)) I,

    C_ab=C_ba=0,

    C_bb
      =
      (1/(6a_phi^2)) I
      - (1/(2a_phi^2 pi^2)) K2,

in the continuum lattice limit, with the PNT/K2 note supplying o(1)
growing-section error for K2-weighted bilinears once the remaining J terms
are arranged in l2-bounded form.

Therefore the resonant D2 primitive becomes the deterministic state
functional

    boxed:
    Psi_res(R,a)

      :=
      Q_aa contracted with C_aa
      + Q_bb contracted with C_bb.

The alpha-beta terms disappear identically.

This is the exact object to differentiate in z for the D2 Lindeberg
coefficient.

## 6. What carries the connected memory

This does **not** reduce the theorem to a scalar covariance-only spectral
law.

The state R is the full nonlinear resolvent of the previously inserted
prime field.

All order-four crossing and connected memory can survive through the
state-dependence of the deterministic bilinear forms Q_aa,Q_bb.

What has disappeared is only the need for a **new arithmetic theorem about
the current prime** beyond its second square-prime covariance.

This resolves the apparent tension with the -1/60 connected calibration.

## 7. Consequence for the earlier E2/product-collision route

The E2 / Lambda*Lambda correlation route remains a valid way to understand
the fixed-degree four-word expansion.

But the bounded Lindeberg theorem no longer needs to expand the state R into
those words in order to average the current D2 block.

For D2, the preferred route is now:

    current prime
      -> exact second covariance
      -> deterministic Psi_res(R,a)
      -> average only over the Bernoulli state.

E2 machinery should be reserved for a place where a state expansion is
actually unavoidable, not inserted automatically.

## 8. Remaining D2 debt after this note

The second-order sector is now split into:

1. **resonant current covariance**
       -> explicit C_aa,C_bb;
       -> algebraic J-to-K2 rearrangement still to finish;

2. **fast / carrier-2T current covariance**
       -> one Hankel-type second covariance;
       -> theorem estimate or nonzero limit still open;

3. **state average**
       -> Bernoulli t-flow of Psi_res/Psi_fast evaluated on R_t.

There is no current-prime four-point theorem left inside D2.

See:

    notes/WP84_D2_LEAVE_ONE_OUT_DECOUPLING.md
    notes/WP84_RESONANT_SCALAR_COVARIANCE.md
    notes/WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md
    notes/WP84_BR_RANK3_SCALAR_D1.md
