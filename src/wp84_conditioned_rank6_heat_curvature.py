#!/usr/bin/env python3
"""Exact algebra certificate builder for the conditioned rank-six heat route.

The script derives the Cayley Fourier and resolvent coefficients with exact
Gaussian rationals, records the already-source-certified heat stencil, and
does not claim a zeta-side energy bound.
"""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "WP84_CONDITIONED_RANK6_HEAT_CURVATURE_CERTIFICATE.json"

def zadd(x, y): return x[0] + y[0], x[1] + y[1]
def zneg(x): return -x[0], -x[1]
def zscale(a, x): return a*x[0], a*x[1]
def zmul(x, y): return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]
def zconj(x): return x[0], -x[1]
def zstr(x): return {"re": str(x[0]), "im": str(x[1])}

Q = [
    (F(44,5000), F(2205,5000)),
    (F(-5695,5000), F(169,5000)),
    (F(-192,5000), F(-5495,5000)),
    (F(1936,5000), F(0)),
]

def derive():
    c = []
    c0 = sum((zmul(q,zconj(q))[0] for q in Q), F(0))
    c.append((c0,F(0)))
    for k in range(1,4):
        v=(F(0),F(0))
        for j in range(k,4): v=zadd(v,zmul(Q[j],zconj(Q[j-k])))
        c.append(v)
    C0=(c0,F(0))
    for ck in c[1:]: C0=zadd(C0,zscale(F(2),(ck[0],F(0))))
    A=zscale(F(2),zmul((F(0),F(1)),zadd(c[1],zadd(zscale(F(2),c[2]),zscale(F(3),c[3])))))
    B=zscale(F(-4),zadd(c[2],zscale(F(3),c[3])))
    C=zscale(F(-4),zmul((F(0),F(1)),c[3]))
    qone=(F(0),F(0))
    for q in Q: qone=zadd(qone,q)
    e_inf=zmul(qone,zconj(qone))
    return c,C0,A,B,C,qone,e_inf

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):h.update(block)
    return h.hexdigest()

def dec_fraction(x: F, places=24):
    with localcontext() as ctx:
        ctx.prec=places+8
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def build():
    c,C0,A,B,C,qone,einf=derive()
    model=F(1272283602671916206561064875108101,12442212289373925054228673142500000)
    threshold=F(105,1000)
    cushion=threshold-model
    required_integral=C0[0]-threshold
    tail_allowance=cushion/2
    finite_required=required_integral+tail_allowance
    abs_A2=A[0]**2+A[1]**2
    abs_B2=B[0]**2+B[1]**2
    abs_C2=C[0]**2+C[1]**2
    norm_A=Decimal(abs_A2.numerator).__truediv__(Decimal(abs_A2.denominator)).sqrt()
    norm_B=Decimal(abs_B2.numerator).__truediv__(Decimal(abs_B2.denominator)).sqrt()
    norm_C=Decimal(abs_C2.numerator).__truediv__(Decimal(abs_C2.denominator)).sqrt()
    S0=F(15736,5000); S1=F(23046,5000); tail_K=4*S0*S1
    # Deterministic envelopes for normalized diagonal products and T_ab.
    M=(8/3)*float(norm_A)+8*float(norm_B)+32*float(norm_C)
    sources=[
        "notes/WP84_CONDITIONED_RANK6_79_CONSUMER.md",
        "notes/WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md",
        "notes/WP84_DIRECT_DEGREE2_HEAT_CURVATURE_STENCIL.md",
        "notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md",
        "notes/WP84_GAUSSIAN_DRIFT_ELIMINATION.md",
        "notes/WP84_CIRCULAR_GAUSSIAN_Q_FIELD.md",
        "notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md",
        "src/wp84_conditioned_rank6_79_consumer.py",
        "src/wp84_exact_frontier_one_point_heat_flow.py",
        "src/wp84_direct_heat_curvature_stencil.py",
        "src/wp84_gaussian_covariance_hadamard_gate.py",
        "src/wp84_resonant_d2_explicit_gate.py",
        "src/wp84_heat_s4_kernel_gate.py",
    ]
    return {
        "title":"WP84 conditioned rank-six heat-curvature audit certificate",
        "start_head":"97d52cfb784feb300197984a78e0d36ea4387dbb",
        "branch":"codex/c5-c6-attack-20261006",
        "consumer":"conditioned rank-six cubic at z=i; frozen q and threshold unchanged",
        "source_scope":"canonical source section and inherited Gaussian ensemble only; no selector is reconstructed or fabricated",
        "q_coefficients_ascending": [zstr(q) for q in Q],
        "unit_circle_energy_fourier": {
            "identity":"|q(u)|^2=c0+sum_{k=1}^3(c_k*u^k+conjugate(c_k)*u^(-k))",
            "c0":zstr(c[0]), "c1":zstr(c[1]), "c2":zstr(c[2]), "c3":zstr(c[3]),
        },
        "resolvent_trace_form": {
            "definition":"U=I+2iR, R=(H-iI)^(-1), m(z)=tau((H-zI)^(-1)); m_z=tau(R^2), m_zz=2*tau(R^3) at z=i",
            "C0":str(C0[0]), "A":zstr(A), "B":zstr(B), "C":zstr(C),
            "formula":"E(H)=tau(Q*Q)=C0+2*Re[A*m(i)+B*m_z(i)+C*m_zz(i)]",
            "q_at_one":zstr(qone), "E_infinity_abs_q1_squared":str(einf[0]),
            "exact_energy_identity":"C0=|q(1)|^2=2500529/2500000, not 1",
        },
        "heat_flow": {
            "bridge":"H_u=H_1+sqrt(u)*W; m_u(z)=E tau((H_u-zI)^(-1)); E_u=E tau(q(U_u)^*q(U_u))",
            "source_gaussian_ensemble":"At conditioned scale a=1, W=diag(h)+[diag(alpha),J], alpha=Im Z_L, h=2*Re Z_L-2*Im(Z_L'/L); Z_L(tau)=sum_{p<=X} gamma_p*(-log(p)/(L*sqrt(p)))*exp(i*tau*log(p)), independent standard circular complex gamma_p (E|gamma_p|^2=1, E gamma_p^2=0); grid covariance K_L(r)=L^(-2)*sum_{p<=X}(log p)^2/p*exp(i*2*pi*r*log(p)/L)",
            "derivative":"E_u'=2*Re[A*C_u(i)+B*partial_z C_u(i)+C*partial_z^2 C_u(i)]",
            "covariance_normalization":"C_u(z)=partial_u m_u(z)=(1/2)*E Xi_z(R_u(z))+o(1); partial_z C_u=(1/2)*E Xi_zz+o(1); partial_z^2 C_u=(1/2)*E Xi_zzz+o(1)",
            "conditioned_stencil":"E_u'=Re E[A*Xi_z+B*Xi_zz+C*Xi_zzz]+o(1), evaluated at z=i",
            "Xi_z":"<r1,r2>/(3d)-T12/pi^2+<h1,h2>/d-(<r2,q1>+<r1,q2>)/(2d)",
            "Xi_zz":"(<r2,r2>+2<r1,r3>)/(3d)-(T22+2*T13)/pi^2+(<h2,h2>+2<h1,h3>)/d-(<r3,q1>+<r2,q2>+<r1,q3>)/d",
            "Xi_zzz":"2*(<r2,r3>+<r1,r4>)/d-6*(T23+T14)/pi^2+6*(<h2,h3>+<h1,h4>)/d-3*(<r4,q1>+<r3,q2>+<r2,q3>+<r1,q4>)/d",
            "state_definitions":"r_k=diag(R^k), h_k=diag(JR^k), q_k=diag(JR^kJ), T_ab=d^(-1)*sum_(i!=j)(R^a)_ij(R^b)_ij/(i-j)^2",
        },
        "fourier_channel": {
            "grouped":"-(1/pi^2)*Re E[A*T12+B*partial_z(T12)+C*partial_z^2(T12)]",
            "derivatives":"partial_z T12=T22+2*T13; partial_z^2 T12=6*(T23+T14)",
            "kernel":"S4(t)=sum_(r!=0)e^(irt)/r^4=pi^4/45-pi^2*t^2/6+pi*t^3/6-t^4/24, 0<=t<=2*pi",
            "state_width":"base 2x4; differentiated representation through second derivative at most 2x8",
            "coefficient_kernel_audit":"actual A,B,C inserted into grouped linear channel; no PSD matrix completion derived",
            "S2_rejected":"using S2 after both commutators would lose two displacement powers; S4 is required",
        },
        "sign_audit": {
            "pointwise_curvature":"FALSIFIED even on exact rank-two sharp-Loewner 2x2 states; this is a statewise Xi functional, not a Gaussian expectation or zeta counterexample",
            "sharp_state_positive":{"a":[1,0],"h":[0,0],"H":"[[0,1/pi],[1/pi,0]]","curvature":"pi^2*(3+pi^2)*(46641783*pi^6-142650593*pi^4-135154723*pi^2+45959989)/(18750000*(1+pi^2)^5)","sign_proof":"with x=pi^2>9, P(9)=21276729256>0, P'(9)=8631087872>0 and P''(x)>0 for x>=9, hence P(x)>0"},
            "sharp_state_negative":{"a":[1,0],"h":[1,-1],"H":"[[1,1/pi],[1/pi,-1]]","curvature":"-pi^2*(-137879967+221624213*pi^2+1018618526*pi^4+183157196*pi^6+369045432*pi^8)/(18750000*(1+2*pi^2)^5)","sign_proof":"for x=pi^2>9, -137879967+221624213*x>0; all remaining terms are positive, and the denominator is positive"},
            "source_compatibility":"Neither 2x2 state is asserted to be a sampled zeta matrix or the conditioned Gaussian law; no actual-source counterexample is claimed",
            "F61_shortcut":"not used; the old F61 Hessian-kernel positivity shortcut remains rejected",
        },
        "finite_u_bound": {
            "hypotheses":"H Hermitian, ||R||<=1, J finite compression of the discrete Hilbert transform with ||J||<=1",
            "bounds":"|<r_a,r_b>/d|, |<h_a,h_b>/d|, |<r_a,q_b>/d|<=1; |T_ab|<=2*sum_(r>=1)r^(-2)=pi^2/3",
            "Xi_bounds":{"Xi_z":"8/3","Xi_zz":"8","Xi_zzz":"32"},
            "curvature_envelope":"|E_u'|<=M=(8/3)|A|+8|B|+32|C|",
            "coefficient_norm_squares":{"|A|^2":str(abs_A2),"|B|^2":str(abs_B2),"|C|^2":str(abs_C2)},
            "coefficient_norms_decimal":{"|A|":str(norm_A),"|B|":str(norm_B),"|C|":str(norm_C),"sum":"9.852290... (diagnostic)"},
            "M_decimal":format(M,".16g"),
            "U0":"1",
            "proved_integral_lower_bound":"integral_0^1 curvature du >= -M (deterministic bound only)",
            "required_finite_integral_with_tail_budget":str(finite_required),
            "tail_allowance":str(tail_allowance),
            "gap_from_current_bound_decimal":format(float(finite_required)+M,".16g"),
        },
        "large_u_tail": {
            "fixed_d":"E_u->|q(1)|^2 as u->infinity for each fixed finite d, per existing Gaussian invertibility argument",
            "uniform_d_status":"OPEN; no dimension-uniform tail theorem in the cited sources",
            "deterministic_reduction":f"|E_u-E_infinity|<=K*E[tau((I+H_u^2)^(-1/2))], K=4*S0*S1={tail_K}, S0={S0}, S1={S1}",
            "small_ball_form":"For H_u=sqrt(u)*(W+H_1/sqrt(u)), any delta>0: tail <= K*(omega_u(delta)+1/(sqrt(u)*delta)), omega_u(delta)=E tau(1_{|W+H_1/sqrt(u)|<=delta})",
            "missing_hypothesis":"a source-uniform, dimension-uniform expected empirical small-ball bound omega_u(delta)->0 with a quantitative rate for the actual sharp-Loewner Gaussian W and allowed deterministic H_1",
        },
        "theorem_target": {
            "threshold":"21/200=0.105",
            "model_energy":str(model), "model_energy_decimal":dec_fraction(model),
            "model_cushion":str(cushion), "model_cushion_decimal":dec_fraction(cushion),
            "required_total_integrated_curvature":"C0-21/200="+str(required_integral),
            "required_total_decimal":dec_fraction(required_integral),
            "U0":"1", "tail_allowance_exact":str(tail_allowance),
            "finite_interval_required":"integral_0^1 curvature du >= "+str(finite_required),
            "finite_interval_required_decimal":dec_fraction(finite_required),
            "rigorous_zeta_side_energy_upper_bound":"none",
            "distance_to_threshold":"unknown; model cushion is not a zeta-side bound",
            "raw_high_moment_expansion":"not used; retain bounded Cayley/resolvent consumer",
            "shifted_Bernoulli_warning":"no finite dilation-jet closure is invoked; its prior obstruction remains in force",
            "strict_gt79":"OPEN",
        },
        "conditioned_vs_frontier_diagnostic": {
            "conditioned_proxy":"|A|+|B|+|C| = sqrt(|A|^2)+sqrt(|B|^2)+sqrt(|C|^2) ~=9.85229",
            "frontier_exact_scale":"a_*^3=13891/9660; A_*=2*i*a_*(c1+2*c2+3*c3), B_*=(2*i*a_*)^2*(c2+3*c3), C_*=((2*i*a_*)^3/2)*c3 from the exact-frontier note",
            "frontier_proxy":"|A_*|+|B_*|+|C_*| ~=13.0088825022, inherited/replayed from WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md",
            "frontier_deterministic_envelope":"M_*=(8/3)|A_*|/a_*^3+8|B_*|/a_*^4+32|C_*|/a_*^5 ~=59.7168133840; strictly smaller than the conditioned M~=68.7587065028 but still far too large to prove the integrated target",
            "comparison_scope":"finite scalar envelopes compared; no exact finite kernel eigen-signature or positive completion established for either consumer",
        },
        "source_sha256":{rel:sha(ROOT/rel) for rel in sources},
        "hostile_mutations_required":[
            "alter_q", "alter_pole", "omit_conjugate_fourier", "alter_C0", "drop_mzz",
            "confuse_Xi_with_Xiz", "omit_Xizzz", "alter_T12_derivative_factor", "use_S2_instead_of_S4",
            "assert_F61_Hessian_positive", "energy_positive_implies_curvature_positive",
            "model_endpoint_as_zeta_endpoint", "omit_large_u_tail", "swap_limits_without_bound",
            "reopen_raw_H6", "use_shifted_Bernoulli_finite_closure", "alter_threshold",
            "alter_model_energy", "claim_79_5489_from_model", "fabricate_source_selector",
        ],
        "decision":"E",
    }

if __name__=="__main__":
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(build(),indent=2)+"\n",encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
