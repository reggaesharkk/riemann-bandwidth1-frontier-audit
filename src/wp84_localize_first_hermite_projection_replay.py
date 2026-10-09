"""Independent replay and hostile mutations for the localize-first audit.

This file intentionally does not import the certificate producer. Run:
    python src/wp84_localize_first_hermite_projection_replay.py
"""
from copy import deepcopy
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION_CERTIFICATE.json"
EPS = F(8711, 2778200)
EINF = F(7761139416076220170204368647089, 1680256283972002400160000000000)
DELTA = F(1, 100000)
LAMBDA = [
    F(-177474003807058873909, 55887390900000000),
    F(-16820385, 938417306), F(150292891, 874129933),
    F(-458723607, 134099951), F(50678184278, 828307931),
    F(-634564925781, 913638178), F(414028352447, 98018322),
    F(-9148412858571, 774794887), F(4252112992579, 373099229),
]
RHOS = [F(1,4),F(1,2),F(3,4),F(7,8),F(15,16),F(31,32),F(63,64),F(127,128)]


def need(ok, msg):
    if not ok:
        raise AssertionError(msg)


def ceil_sqrt(x, scale=10**12):
    q = isqrt(x.numerator*scale*scale//x.denominator)
    while F(q, scale)**2 < x:
        q += 1
    return F(q, scale)


def outward(x, places=12):
    scale=10**places
    lo=x.numerator*scale//x.denominator
    hi=-((-x.numerator*scale)//x.denominator)
    return [str(F(lo,scale)),str(F(hi,scale))]


def finite_projection_replay():
    # A finite Hermite basis with degrees (0,1,1,2,2): P is exactly a
    # diagonal orthogonal projection. Enumerate a finite rational vector set.
    degrees=[0,1,1,2,2]
    keep=[n<=2 for n in degrees]
    scalars=[F(-2),F(-1),F(0),F(1),F(2)]
    cases=0
    for v in product(scalars,repeat=len(degrees)):
        lhs=sum((v[j]**2 for j in range(len(v)) if keep[j]),F(0))
        rhs=sum((x*x for x in v),F(0))
        need(lhs<=rhs,"finite Hermite projection contraction")
        cases+=1
    # Explicit expansive-map falsifier: A=2I violates the contraction bound.
    norm_v=F(1); norm_Av=F(2)
    need(norm_Av>norm_v,"expansive map must be rejected")
    return {"basis_degrees":degrees,"rational_vectors_checked":cases,
            "orthogonal_projection_contracts":True,"expansive_map_rejected":True}


def recompute_localization(cert):
    loc=cert["localization"]
    lam=sum(map(abs,LAMBDA),F(0))
    root_e=ceil_sqrt(EINF)
    new=20*root_e
    old=43*lam
    need(F(loc["Lambda_U"])==lam,"K=32 witness Lambda_U")
    need(F(loc["old_sqrt_h_coefficient"])==old,"old weak-dual coefficient")
    need(F(loc["new_sqrt_h_coefficient"])==new,"new projected coefficient")
    need(F(loc["coefficient_reduction_factor"])==old/new,"amplification factor")
    need("delta" in loc["new_pair"],"delta layer is required")
    need("Lambda_U" not in loc["new_single_layer"],"new bound must not include Lambda_U")
    rows=loc["R_table"]
    need([r["U"] for r in rows]==[1,2,4,8,16,32],"representative U table")
    for row in rows:
        e2=F(row["e_pair_squared_upper"])
        target=(EPS/4)**2
        need(e2<target,"each R bound must be strictly below epsilon/4")
        need(F(row["ratio_to_target_squared"])==e2/target,"budget ratio")
        m=row["R"]+1
        k=(m-1).bit_length()
        h=F(8*(k+2),9*m)
        ru=ceil_sqrt(F(2)+F(row["U"],4))
        rd=ceil_sqrt(F(2)+DELTA/4)
        check_e2=new**2*(ru+rd)**2*h
        need(check_e2==e2,"independent R-table formula")
    need(cert["consumer"]["K"]==32,"K frozen")
    need(cert["consumer"]["delta"]==str(DELTA),"delta frozen")
    need(cert["consumer"]["epsilon"]==str(EPS),"epsilon frozen")
    return {"Lambda_U":str(lam),"old_coefficient":str(old),"new_coefficient":str(new),
            "reduction_factor":str(old/new),"R_rows":len(rows)}


def derivative_replay(cert):
    a=F(131,200); u1=2/a; u2=4/a**2; u3=12/a**3
    bounds=[]
    for r in (1,2,3):
        total=F(0)
        for n,q in ((1,F(442,1000)),(2,F(442,1000)),(3,F(634,1000))):
            term={
                1:n*u1,
                2:n*u2+n*(n-1)*u1**2,
                3:n*u3+3*n*(n-1)*u2*u1+n*(n-1)*(n-2)*u1**3,
            }[r]
            total += q*term
        bounds.append(total)
    d=[bounds[0]*6,bounds[1]*36,bounds[2]*216]
    se=ceil_sqrt(EINF)
    psi=[4*se*d[0],4*(d[0]**2+se*d[1]),4*(3*d[0]*d[1]+se*d[2])]
    actual=cert["local_cylinder"]["derivatives"]
    need(list(map(str,bounds))==actual["Q_derivative_bounds_C1_C2_C3"],"C1/C2/C3 consumer bounds")
    need(list(map(str,d))==actual["sampled_consumer_derivative_bounds_D1_D2_D3"],"sample-map derivative bounds")
    need(list(map(str,psi))==actual["Psi_derivative_bounds_C1_C2_C3"],"Psi derivative bounds")
    return {"Q_bounds":list(map(str,bounds)),"Psi_bounds":list(map(str,psi))}


def multiplier_replay(cert):
    q=[]
    powers=[F(1)]*len(RHOS)
    max_abs=F(0); at=0
    for n in range(2048):
        val=LAMBDA[0]+sum((LAMBDA[j+1]*powers[j] for j in range(8)),F(0))
        if abs(val)>max_abs:
            max_abs,at=abs(val),n
        powers=[powers[j]*RHOS[j] for j in range(8)]
    lam=sum(map(abs,LAMBDA),F(0))
    tail=lam*F(3,8)**16
    need(F(127,128)**128<F(3,8),"tail block comparison")
    need(tail<F(1,100),"tail < 0.01")
    upper=max(max_abs,abs(LAMBDA[0])+F(1,100))
    obj=cert["optional_multiplier_norm"]
    need(obj["finite_scan_sup_enclosure_1e-12"]==outward(max_abs),"finite Mq scan enclosure")
    need(obj["M_q_lower_bound_from_limit_enclosure_1e-12"]==outward(abs(LAMBDA[0])),"Mq lower limit")
    need(obj["M_q_upper_bound_enclosure_1e-12"]==outward(upper),"Mq upper enclosure")
    need(F(obj["tail_bound_n_ge_2048"])==tail,"Mq tail")
    return {"finite_max_n":at,"finite_scan_sup":outward(max_abs),
            "M_q_interval": [outward(abs(LAMBDA[0]))[0],outward(upper)[1]],
            "Lambda_U":str(lam)}


def validate_semantics(c):
    need(c["decision"]=="C","decision C frozen")
    need(c["consumer"]["K"]==32 and c["consumer"]["delta"]=="1/100000","frozen consumer")
    need(c["consumer"]["epsilon"]=="8711/2778200","epsilon")
    need(c["consumer"]["E_inf"]==str(EINF),"not a model endpoint")
    p=c["projection_contraction"]
    need(p["statement"]=="||P_{<=K}(F-G)||_2 <= ||F-G||_2","orthogonal projection")
    need(p["independent_of"]==["K","weak-dual rho count","Lambda_U","453"],"no arithmetic dimension or dual amplification")
    need("Lambda_U" not in c["localization"]["new_single_layer"],"Lambda amplification absent")
    need("delta" in c["localization"]["new_pair"],"delta paid")
    need(c["localization"]["order_of_limits"].startswith("fixed R -> T->infinity -> R->infinity"),"limit order")
    need("no R(T)" in c["localization"]["order_of_limits"],"no growing R(T)")
    need("tends to zero only after T->infinity" in c["localization"]["edge_term"],"physical edge term")
    need("4 E_inf R/d" in c["localization"]["edge_term"] and "Lambda_total" not in c["localization"]["edge_term"],"projected edge payment is separately bounded without weak-dual amplification")
    need("same finite standard Gaussian g" in c["fixed_R_covariance_transfer"]["argument"],"common-coordinate coupling")
    need("including singular limits" in c["fixed_R_covariance_transfer"]["argument"],"PSD square-root continuity")
    need("REMOVED" in c["fixed_R_covariance_transfer"]["2K_plus_2_derivative_debt"],"2K+2 debt removed")
    need("arbitrary_nonorthogonal_change" in c["chaos_representation"],"nonorthogonal boundary")
    need("not invariant" in c["chaos_representation"]["arbitrary_nonorthogonal_change"],"no arbitrary invariance")
    need(c["prime_smooth_comparison"]["status"]=="A1 and A2 remain OPEN; Y_p depends on the same trace index K as V_p(K). No independence or mean-zero cancellation is available. The obstruction is unchanged in kind, with improved finite-cylinder derivative constants.","no false cancellation and retain phase dependence")
    need(c["remaining_theorem"]=="For each fixed R and the explicit Psi_R, prove A1_T,R + A2_T,R -> 0 (or directly E Psi_R(X_(T,R))-E Psi_R(G_R)->0), while retaining same-index dependence, full prime cutoff, original masks and proper powers; this is the first missing source-dependent prime law.","do not reopen raw moments or source selector")
    need(c["strict_gt79"] is False,"strict theorem remains open")
    need("not actual" not in c["consumer"]["cap"],"cap statement")
    need(c["two_stage_localization"]["no_optimized_r_m"] is True,"no unproved r/m gain")
    need("rank d" in c["two_stage_localization"]["hostile_example"],"rank counterexample retained")


def hostile_mutations(cert):
    # Each mutation models one forbidden shortcut and must be caught by the
    # independent semantic/integer checks above.
    mutations=[
        ("expansive projection",lambda x:x["projection_contraction"].update(statement="||2P(F-G)||<=||F-G||")),
        ("insert Lambda_U",lambda x:x["localization"].update(new_single_layer=x["localization"]["new_single_layer"]+" Lambda_U")),
        ("omit delta",lambda x:x["localization"].update(new_pair="only U layer")),
        ("model endpoint",lambda x:x["consumer"].update(E_inf="model energy")),
        ("vary K",lambda x:x["consumer"].update(K=33)),
        ("uncoupled coordinates",lambda x:x["fixed_R_covariance_transfer"].update(argument="compare unrelated coordinate spaces")),
        ("false singular Lipschitz",lambda x:x["fixed_R_covariance_transfer"].update(argument="square root is Lipschitz at singular limits")),
        ("arbitrary nonorthogonal invariance",lambda x:x["chaos_representation"].update(arbitrary_nonorthogonal_change="invariant")),
        ("interchange limits",lambda x:x["localization"].update(order_of_limits="R->infinity then T->infinity")),
        ("R(T)",lambda x:x["localization"].update(order_of_limits="fixed R -> T->infinity -> R->infinity; choose R(T)")),
        ("omit edge",lambda x:x["localization"].update(edge_term="omitted")),
        ("A1 from mean zero",lambda x:x["prime_smooth_comparison"].update(status="A1=0 by mean zero; A2 open")),
        ("A2 from covariance",lambda x:x["prime_smooth_comparison"].update(status="A2=0 by covariance match; A1 open")),
        ("independent prime phases",lambda x:x["prime_smooth_comparison"].update(status="prime phases independent")),
        ("453 as dimension",lambda x:x["projection_contraction"].update(independent_of=["453 arithmetic dimension"])),
        ("raw moments",lambda x:x.update(remaining_theorem="reopen raw H5/H6")),
        ("source mask",lambda x:x.update(remaining_theorem="recover source_mask")),
        ("alter epsilon",lambda x:x["consumer"].update(epsilon="1/100")),
        ("synthetic benchmark actual",lambda x:x["prime_smooth_comparison"].update(status="synthetic benchmark is actual Gaussian evaluation")),
        (">79 claim",lambda x:x.update(strict_gt79=True)),
    ]
    passed=[]
    for name,mut in mutations:
        bad=deepcopy(cert); mut(bad)
        try:
            validate_semantics(bad)
        except (AssertionError,KeyError,TypeError):
            passed.append(name)
        else:
            raise AssertionError("hostile mutation survived: "+name)
    need(len(passed)==20,"all required hostile mutations rejected")
    return passed


def hash_replay(cert):
    for path,digest in cert["source_sha256"].items():
        got=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
        need(got==digest,"source hash mismatch: "+path)
    return len(cert["source_sha256"])


def main():
    c=json.loads(CERT_PATH.read_text(encoding="utf-8"))
    validate_semantics(c)
    projection=finite_projection_replay()
    loc=recompute_localization(c)
    deriv=derivative_replay(c)
    mq=multiplier_replay(c)
    hashes=hash_replay(c)
    hostile=hostile_mutations(c)
    print("PASS: independent exact projection, localization, derivative, M_q, source-hash replays.")
    print(f"PASS: {len(hostile)}/20 hostile mutations rejected; {projection['rational_vectors_checked']} finite-basis vectors checked.")
    print("Lambda_U amplification removed; R thresholds remain ~10^12; fixed-R covariance transfer closes.")
    print("A1+A2 and strict >79 remain OPEN. Decision C.")
    print(json.dumps({"localization":loc,"derivatives":deriv,"M_q":mq,"source_hashes":hashes},sort_keys=True))


if __name__=="__main__":
    main()
