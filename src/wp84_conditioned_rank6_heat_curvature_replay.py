#!/usr/bin/env python3
"""Independent replay of the conditioned rank-six heat-curvature certificate."""
from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
CERT=ROOT/"notes"/"WP84_CONDITIONED_RANK6_HEAT_CURVATURE_CERTIFICATE.json"
SOURCES=[
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

def zadd(x,y):return x[0]+y[0],x[1]+y[1]
def zmul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def zscale(a,x):return a*x[0],a*x[1]
def zconj(x):return x[0],-x[1]
def zs(x):return {"re":str(x[0]),"im":str(x[1])}

def exact_coefficients():
 q=[(F(44,5000),F(2205,5000)),(F(-5695,5000),F(169,5000)),(F(-192,5000),F(-5495,5000)),(F(1936,5000),F(0))]
 c0=sum((zmul(x,zconj(x))[0] for x in q),F(0)); cs=[(c0,F(0))]
 for k in range(1,4):
  v=(F(0),F(0))
  for j in range(k,4):v=zadd(v,zmul(q[j],zconj(q[j-k])))
  cs.append(v)
 C0=(c0,F(0))
 for ck in cs[1:]:C0=zadd(C0,(2*ck[0],F(0)))
 I=(F(0),F(1))
 A=zscale(F(2),zmul(I,zadd(cs[1],zadd(zscale(F(2),cs[2]),zscale(F(3),cs[3])))))
 B=zscale(F(-4),zadd(cs[2],zscale(F(3),cs[3])))
 C=zscale(F(-4),zmul(I,cs[3]))
 q1=(F(0),F(0))
 for x in q:q1=zadd(q1,x)
 return q,cs,C0,A,B,C,q1

def sha(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for b in iter(lambda:f.read(1<<16),b""):h.update(b)
 return h.hexdigest()

def need(cond,msg):
 if cond:raise ValueError(msg)

def validate(c):
 q,cs,C0,A,B,C,q1=exact_coefficients()
 need(c.get("start_head")!="97d52cfb784feb300197984a78e0d36ea4387dbb","starting HEAD changed")
 need(c.get("branch")!="codex/c5-c6-attack-20261006","branch changed")
 need(c.get("consumer")!="conditioned rank-six cubic at z=i; frozen q and threshold unchanged","consumer changed")
 need(c.get("source_scope")!="canonical source section and inherited Gaussian ensemble only; no selector is reconstructed or fabricated","source selector fabricated")
 need(c.get("q_coefficients_ascending")!=[zs(x) for x in q],"q altered")
 f=c["unit_circle_energy_fourier"]
 need(f.get("identity")!="|q(u)|^2=c0+sum_{k=1}^3(c_k*u^k+conjugate(c_k)*u^(-k))","conjugate Fourier part omitted")
 need([f.get(k) for k in ("c0","c1","c2","c3")]!=[zs(x) for x in cs],"Fourier coefficients changed")
 rf=c["resolvent_trace_form"]
 need(rf.get("C0")!=str(C0[0]) or rf.get("A")!=zs(A) or rf.get("B")!=zs(B) or rf.get("C")!=zs(C),"resolvent coefficients changed")
 need("z=i" not in rf.get("definition", ""),"pole changed")
 need("m_zz(i)" not in rf.get("formula", ""),"m_zz omitted")
 need(rf.get("E_infinity_abs_q1_squared")!=str(zmul(q1,zconj(q1))[0]),"endpoint changed")
 hf=c["heat_flow"]
 need("(1/2)*E Xi_z" not in hf.get("covariance_normalization", ""),"Xi confused with Xi_z or covariance factor changed")
 need("Xi_zzz" not in hf.get("conditioned_stencil", ""),"Xi_zzz omitted")
 need("T23+T14" not in hf.get("Xi_zzz", "") or "<r1,q4>" not in hf.get("Xi_zzz", ""),"third stencil absent")
 fc=c["fourier_channel"]
 need("T22+2*T13" not in fc.get("derivatives", "") or "6*(T23+T14)" not in fc.get("derivatives", ""),"T12 derivative factors changed")
 need("S4" not in fc.get("kernel", "") or "r^4" not in fc.get("kernel", ""),"wrong Fourier kernel")
 need("FALSIFIED" not in c["sign_audit"].get("pointwise_curvature", ""),"curvature sign overclaimed")
 need("not a Gaussian expectation" not in c["sign_audit"].get("pointwise_curvature", ""),"state diagnostic promoted")
 need("source-uniform, dimension-uniform" not in c["large_u_tail"].get("missing_hypothesis", ""),"large-u tail omitted")
 need("dimension-uniform" not in c["large_u_tail"].get("uniform_d_status", ""),"d/u limit interchange unsupported")
 need("no exact finite" not in c["conditioned_vs_frontier_diagnostic"].get("comparison_scope", ""),"unsupported comparison claim")
 need("standard circular complex gamma_p" not in hf.get("source_gaussian_ensemble", ""),"source Gaussian ensemble missing")
 diag=c["conditioned_vs_frontier_diagnostic"]
 need("59.7168133840" not in diag.get("frontier_deterministic_envelope", ""),"frontier envelope comparison missing")
 t=c["theorem_target"]
 need(t.get("threshold")!="21/200=0.105","threshold changed")
 need(t.get("model_energy")!="1272283602671916206561064875108101/12442212289373925054228673142500000","model energy changed")
 need("model output only" not in c["theorem_target"].get("distance_to_threshold", "") and "unknown" not in c["theorem_target"].get("distance_to_threshold", ""),"model value promoted to theorem")
 need(t.get("strict_gt79")!="OPEN","theorem status changed")
 need(t.get("rigorous_zeta_side_energy_upper_bound")!="none","model endpoint promoted to zeta energy upper bound")
 need("unknown" not in t.get("distance_to_threshold", ""),"distance to threshold changed")
 need("not used" not in t.get("raw_high_moment_expansion", ""),"raw high-moment route reopened")
 need("prior obstruction remains" not in t.get("shifted_Bernoulli_warning", ""),"shifted Bernoulli finite closure revived")
 need("not used" not in c["sign_audit"].get("F61_shortcut", ""),"F61 positivity shortcut revived")
 need("fabricate_source_selector" not in c.get("hostile_mutations_required", []),"selector falsifier omitted")
 need(len(c.get("hostile_mutations_required", []))!=20,"hostile suite incomplete")
 for rel in SOURCES:need(c.get("source_sha256",{}).get(rel)!=sha(ROOT/rel),f"source hash mismatch: {rel}")

def symmetric_2x2_signs():
 p=sp.pi;I=sp.I
 A=-sp.Rational(2589491,781250)-sp.Rational(11532549,3125000)*I
 B=sp.Rational(22894891,6250000)+sp.Rational(3238061,1562500)*I
 C=-sp.Rational(53361,78125)-sp.Rational(5324,390625)*I
 J=sp.Matrix([[0,1/p],[-1/p,0]])
 alpha=sp.diag(1,0);D=sp.diag(0,1)
 def value(hdiag):
  H=sp.diag(*hdiag)+alpha*J-J*alpha
  R=(H-I*sp.eye(2)).inv(); powers={k:R**k for k in range(1,5)}
  r={k:sp.Matrix([powers[k][i,i] for i in range(2)]) for k in range(1,5)}
  h={k:sp.Matrix([(J*powers[k])[i,i] for i in range(2)]) for k in range(1,5)}
  q={k:sp.Matrix([(J*powers[k]*J)[i,i] for i in range(2)]) for k in range(1,5)}
  dot=lambda x,y:x.dot(y)/2
  T=lambda a,b:sum(powers[a][i,j]*powers[b][i,j]/(i-j)**2 for i in range(2) for j in range(2) if i!=j)/2
  x1=dot(r[1],r[2])/3-T(1,2)/p**2+dot(h[1],h[2])-(dot(r[2],q[1])+dot(r[1],q[2]))/2
  x2=(dot(r[2],r[2])+2*dot(r[1],r[3]))/3-(T(2,2)+2*T(1,3))/p**2+dot(h[2],h[2])+2*dot(h[1],h[3])-(dot(r[3],q[1])+dot(r[2],q[2])+dot(r[1],q[3]))
  x3=2*(dot(r[2],r[3])+dot(r[1],r[4]))-6*(T(2,3)+T(1,4))/p**2+6*(dot(h[2],h[3])+dot(h[1],h[4]))-3*(dot(r[4],q[1])+dot(r[3],q[2])+dot(r[2],q[3])+dot(r[1],q[4]))
  return H,sp.factor(sp.re(A*x1+B*x2+C*x3))
 Hp,ep=value((0,0));Hn,en=value((1,-1))
 P=lambda x:46641783*x**3-142650593*x**2-135154723*x+45959989
 Q=lambda x:-137879967+221624213*x+1018618526*x**2+183157196*x**3+369045432*x**4
 expected_p=p**2*(3+p**2)*P(p**2)/(sp.Integer(18750000)*(1+p**2)**5)
 expected_n=-p**2*Q(p**2)/(sp.Integer(18750000)*(1+2*p**2)**5)
 assert sp.simplify(ep-expected_p)==0, (ep,expected_p)
 assert sp.simplify(en-expected_n)==0, (en,expected_n)
 assert P(9)==21276729256 and sp.diff(P(sp.Symbol('x')),sp.Symbol('x')).subs(sp.Symbol('x'),9)==8631087872
 assert sp.diff(P(sp.Symbol('x')),sp.Symbol('x'),2).subs(sp.Symbol('x'),9)>0
 assert -137879967+221624213*9>0
 assert all(v>0 for v in [221624213,1018618526,183157196,369045432])
 # Exact sharp-Loewner displacement factorization is rank two for both H states.
 for H in (Hp,Hn):
  comm=D*H-H*D
  assert comm.rank()==2
 return ep,en

def frontier_envelope_replay():
 a=sp.real_root(sp.Rational(13891,9660),3);I=sp.I
 q=[(-I+sp.Rational(43428,13891)*a+I*sp.Rational(37704,13891)*a**2-sp.Rational(9660,13891)*a**3)/8,
    (3*I-sp.Rational(43428,13891)*a+I*sp.Rational(37704,13891)*a**2-3*sp.Rational(9660,13891)*a**3)/8,
    (-3*I-sp.Rational(43428,13891)*a-I*sp.Rational(37704,13891)*a**2-3*sp.Rational(9660,13891)*a**3)/8,
    (I+sp.Rational(43428,13891)*a-I*sp.Rational(37704,13891)*a**2-sp.Rational(9660,13891)*a**3)/8]
 conj=lambda x:sp.conjugate(x).subs(sp.conjugate(a),a)
 c1=q[1]*conj(q[0])+q[2]*conj(q[1])+q[3]*conj(q[2])
 c2=q[2]*conj(q[0])+q[3]*conj(q[1]);c3=q[3]*conj(q[0])
 A=sp.simplify(2*I*a*(c1+2*c2+3*c3))
 B=sp.simplify((2*I*a)**2*(c2+3*c3))
 C=sp.simplify((2*I*a)**3*c3/2)
 mod=lambda x:sp.sqrt(sp.simplify(sp.expand_complex(x*conj(x))))
 M=sp.Rational(8,3)*mod(A)/a**3+8*mod(B)/a**4+32*mod(C)/a**5
 assert abs(float(sp.N(M,30))-59.71681338399325097)<1e-12
 return M

def finite_hermitian_regressions(A,B,C,C0):
 rng=np.random.default_rng(8409)
 q=np.array([complex(44/5000,2205/5000),complex(-5695/5000,169/5000),complex(-192/5000,-5495/5000),1936/5000],dtype=complex)
 for d in (1,2,4,9):
  X=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
  H=(X+X.conj().T)/2
  lam=np.linalg.eigvalsh(H)
  u=(lam+1j)/(lam-1j)
  qv=sum(q[k]*u**k for k in range(4))
  direct=float(np.mean(np.abs(qv)**2))
  r=1/(lam-1j)
  m=np.mean(r); mz=np.mean(r*r); mzz=2*np.mean(r**3)
  trace=float(C0+2*np.real(A*m+B*mz+C*mzz))
  assert abs(direct-trace)<2e-12*max(1.,abs(direct)),(d,direct,trace)

def mutations(c):
 return [
  ("alter_q",lambda x:x["q_coefficients_ascending"].__setitem__(0,{"re":"0","im":"0"})),
  ("alter_pole",lambda x:x["resolvent_trace_form"].update(definition="z=2i")),
  ("omit_conjugate_fourier",lambda x:x["unit_circle_energy_fourier"].update(identity="c0+positive modes only")),
  ("alter_C0",lambda x:x["resolvent_trace_form"].update(C0="1")),
  ("drop_mzz",lambda x:x["resolvent_trace_form"].update(formula="C0+A*m+B*m_z")),
  ("confuse_Xi_with_Xiz",lambda x:x["heat_flow"].update(covariance_normalization="C=1/2 E Xi")),
  ("omit_Xizzz",lambda x:x["heat_flow"].update(conditioned_stencil="E'=A Xi_z+B Xi_zz")),
  ("alter_T12_derivative_factor",lambda x:x["fourier_channel"].update(derivatives="partial_z T12=T22+T13")),
  ("use_S2_instead_of_S4",lambda x:x["fourier_channel"].update(kernel="S2(t)=sum 1/r^2")),
  ("assert_F61_Hessian_positive",lambda x:x["sign_audit"].update(F61_shortcut="positive")),
  ("energy_positive_implies_curvature_positive",lambda x:x["sign_audit"].update(pointwise_curvature="positive because energy positive")),
  ("model_endpoint_as_zeta_endpoint",lambda x:x["theorem_target"].update(rigorous_zeta_side_energy_upper_bound=x["theorem_target"]["model_energy"])),
  ("omit_large_u_tail",lambda x:x["large_u_tail"].update(uniform_d_status="closed")),
  ("swap_limits_without_bound",lambda x:x["large_u_tail"].update(missing_hypothesis="none")),
  ("reopen_raw_H6",lambda x:x["theorem_target"].update(raw_high_moment_expansion="reopen raw H^6")),
  ("use_shifted_Bernoulli_finite_closure",lambda x:x["theorem_target"].update(shifted_Bernoulli_warning="finite closure works")),
  ("alter_threshold",lambda x:x["theorem_target"].update(threshold="0.11")),
  ("alter_model_energy",lambda x:x["theorem_target"].update(model_energy="0")),
  ("claim_79_5489_from_model",lambda x:x["theorem_target"].update(strict_gt79="79.5489 theorem")),
  ("fabricate_source_selector",lambda x:x.update(source_scope="fabricated source selector")),
 ]

def main():
 c=json.loads(CERT.read_text(encoding="utf-8"));validate(c)
 q,cs,C0,A,B,C,q1=exact_coefficients()
 assert C0==(F(2500529,2500000),F(0))
 model=F(1272283602671916206561064875108101,12442212289373925054228673142500000)
 cushion=F(105,1000)-model
 required=C0[0]-F(105,1000)
 assert required==F(2238029,2500000)
 assert c["theorem_target"]["model_cushion"]==str(cushion)
 assert c["theorem_target"]["required_total_integrated_curvature"]=="C0-21/200="+str(required)
 positive,negative=symmetric_2x2_signs()
 frontier_envelope_replay()
 assert sp.N(positive,20)>0 and sp.N(negative,20)<0
 finite_hermitian_regressions(complex(float(A[0]),float(A[1])),complex(float(B[0]),float(B[1])),complex(float(C[0]),float(C[1])),float(C0[0]))
 rejected=[]
 for name,mutate in mutations(c):
  bad=copy.deepcopy(c);mutate(bad)
  try:validate(bad)
  except (ValueError,KeyError,TypeError):rejected.append(name)
 assert len(rejected)==20,(len(rejected),rejected)
 print("PASS: exact Gaussian-rational Fourier/resolvent coefficients")
 print("PASS: Hermitian trace regression dimensions 1,2,4,9")
 print("PASS: exact positive and negative rank-two sharp-Loewner curvature witnesses")
 print("PASS: conditioned heat normalization, S4 channel, tail ledger, and 20/20 hostile mutations")
 print("NO zeta-side energy bound; strict >79 OPEN")

if __name__=="__main__":main()
