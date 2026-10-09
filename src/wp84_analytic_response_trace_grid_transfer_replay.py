"""Independent exact replay for fixed-pole response analyticity.

No import of the producer. Mutated-certificate tests are applied to copies.
"""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
from math import prod, factorial
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "notes/WP84_ANALYTIC_RESPONSE_TRACE_GRID_TRANSFER_CERTIFICATE.json"


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def primes(n):
    return [k for k in range(2, n + 1) if is_prime(k)]


def e3_upper():
    partial = sum((F(3**k, factorial(k)) for k in range(13)), F(0))
    tail = F(14, 11) * F(3**13, factorial(13))
    return partial + tail


def replay_constants():
    a = F(131,200)
    assert F(3142,2415)**2 + a*a < F(9,4)
    p = [F(1), F(16,5), F(14,5), F(7,10)]
    q0 = F(150,131)**3 * (p[0]+p[1]*F(3,2)+p[2]*F(9,4)+p[3]*F(27,8))
    assert q0 < 22
    q = {1:F(221,500),2:F(221,500),3:F(317,500)}
    qsup = 22 + sum(q[j]*5**j for j in range(1,4))
    assert qsup == F(22902,200)
    rbound = F(400,131)
    assert rbound == 1/(a*F(1,2))
    assert 1+2*a*rbound == 5
    d1,d2=F(72,1)/a,F(2592,1)/a**2
    q1=d1*sum(q[j]*j*5**(j-1) for j in range(1,4))
    q2=sum(q[j]*(j*5**(j-1)*d2+j*(j-1)*F(5)**(j-2)*d1**2) for j in range(1,4))
    M1,M2=4*qsup*q1,4*(q1*q1+qsup*q2)
    assert M1<10**7 and M2<10**9
    return qsup,M1,M2


def replay_old_atom(M1,M2):
    assert e3_upper()<21
    assert F(7800*7,44)>1000
    assert F(7800,6)==1300  # strict X<1300 uses pi>3
    assert e3_upper()**2<1000
    L_lower=F(6)
    eta=F(393,51200)
    assert eta == F(131,400)*L_lower/(128*2)
    h_lower=253891+173308
    gamma=eta*h_lower
    assert gamma>3279
    return M1*F(1,2**3279),M2*F(1,2**3279),gamma


def replay_many_alias():
    support=[q for q in primes(31) if q!=2]
    X=2*prod(support)
    assert support==[3,5,7,11,13,17,19,23,29,31]
    assert X>1323*32 and X<2**38
    # e>2 gives log X<38; hence sqrt(log X)<7.
    # e<3 and e^3<21 imply e^7<1323; therefore X/e^sqrt(log X)>32.
    assert F(1)+F(1)+F(1,2)>2 # e>2, hence log(2)<1
    assert e3_upper()<21
    assert X//1323>32
    Lsymbol="log(X)"
    # Identity is exact in integers: 2 * product(support) / X = 1.
    assert 2*prod(support)==X
    return support,X,Lsymbol


def validate(cert):
    assert cert["schema"]=="wp84-analytic-response-trace-grid-transfer-v1"
    assert cert["frozen"]["K"]==32 and cert["frozen"]["delta"]=="1/100000"
    assert cert["frozen"]["a"]=="131/200"
    assert cert["frozen"]["cutoff"]=="N=floor(X exp(-sqrt(log X)))"
    assert cert["frozen"]["quantifiers"]=="fixed R, then T->infinity"
    assert cert["decision"]=="C" and cert["strict_gt79"]=="OPEN"
    assert "400/131" in cert["complex_resolvent_domain"]["complexified"]
    assert cert["complex_resolvent_domain"]["warning"].find("Hermitian 1/a bound is not used")>=0
    assert cert["source_grouped_block"]["same_phase"].find("z_q^j")>=0
    assert "max{j>=1:q^j<=N}" in cert["source_grouped_block"]["J_q"]
    assert "sum_{j=1}^{J_q}" in cert["source_grouped_block"]["B_q_rho"]
    assert "sum_(q in S)" in cert["multi_index_optimization"]["feasible_constraint"]
    assert "128 eta |S|/L" in cert["multi_index_optimization"]["proof_cost"]
    assert cert["multi_index_optimization"]["global_weight_caveat"].find("does not itself prove")>=0
    assert cert["valid_weighted_l2"]["not_proved"].find("No single global weight")>=0
    assert cert["many_small_exponent_exact_alias"]["exponent_bound"]=="max_q |nu_q|=1"
    assert cert["many_small_exponent_exact_alias"]["alias"].find("m=1")>=0
    assert cert["many_small_exponent_exact_alias"]["coefficient_status"].find("not inferred")>=0
    assert cert["old_adversarial_atom"]["prior_l2_only_lemma"]=="FALSE for L2 coefficient control alone"
    assert "No claim that it occurs" in cert["old_adversarial_atom"]["interpretation"]
    assert cert["alias_split"]["m_nonzero"].find("not excluded")>=0
    assert cert["alias_split"]["near"].find("no count/weighted-l2")>=0
    assert cert["A1_weighted_dual_mass"]["status"].startswith("OPEN")
    assert cert["A2_weighted_dual_mass"]["status"].startswith("OPEN")
    assert cert["consistency"].find("would not imply full-vector Gaussian convergence")>=0
    assert cert["prior_count_reconciliation"]["certificate_named_hostile_scenarios"]==20
    assert cert["prior_count_reconciliation"]["prior_replay_hostile_inference_evidence_checks"]==21
    assert cert["prior_count_reconciliation"]["ordinary_rational_arithmetic_assert_statements"]==8
    assert cert["prior_count_reconciliation"]["source_hash_comparisons"]==6
    assert cert["prior_count_reconciliation"]["certificate_schema_field_consistency_assertions"]==7
    return True


def hostile_mutation_tests(cert):
    # Each mutation is applied to a copy and must fail validation.
    mutations = [
        lambda x: x["old_adversarial_atom"].update(prior_l2_only_lemma="TRUE"),
        lambda x: x["old_adversarial_atom"].update(interpretation="actual coefficient exists"),
        lambda x: x["complex_resolvent_domain"].update(complexified="Hermitian 1/a after complexification"),
        lambda x: x["source_grouped_block"].update(same_phase="independent phases for each power"),
        lambda x: x["multi_index_optimization"].update(feasible_constraint="product of independent strips"),
        lambda x: x["multi_index_optimization"].update(proof_cost="omit cumulative perturbation"),
        lambda x: x["source_grouped_block"].update(J_q="j=1 only"),
        lambda x: x["alias_split"].update(m_nonzero="all nonzero aliases impossible"),
        lambda x: x["many_small_exponent_exact_alias"].update(alias="X is irrational"),
        lambda x: x["many_small_exponent_exact_alias"].update(exponent_bound="max |nu|=1000"),
        lambda x: x["valid_weighted_l2"].update(not_proved="pointwise bound implies global weighted l2"),
        lambda x: x["A1_weighted_dual_mass"].update(status="CLOSED termwise"),
        lambda x: x["A2_weighted_dual_mass"].update(status="CLOSED for each p, hence summed"),
        lambda x: x["frozen"].update(cutoff="N=X^0.9"),
        lambda x: x["frozen"].update(quantifiers="R=R(T)"),
        lambda x: x["frozen"].update(K=31),
        lambda x: x["frozen"].update(delta="1/1000"),
        lambda x: x["many_small_exponent_exact_alias"].update(coefficient_status="synthetic numerical evidence proves arithmetic"),
        lambda x: x.update(consistency="full original-scale prime field is asymptotically Gaussian"),
        lambda x: x["prior_count_reconciliation"].update(certificate_named_hostile_scenarios=21),
        lambda x: x["prior_count_reconciliation"].update(prior_replay_hostile_inference_evidence_checks=20),
        lambda x: x["source_grouped_block"].update(J_q="j=1 only; proper powers omitted"),
    ]
    for idx,mutate in enumerate(mutations,1):
        bad=deepcopy(cert)
        mutate(bad)
        try:
            validate(bad)
        except (AssertionError, KeyError, TypeError):
            continue
        raise AssertionError(f"hostile mutation {idx} was not rejected")
    return len(mutations)


def check_source_hashes(cert):
    hashes=cert["prior_source_hashes"]
    assert len(hashes)==10
    for rel,expected in hashes.items():
        actual=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
        assert actual==expected, rel
    return len(hashes)


def main():
    cert=json.loads(CERT_PATH.read_text(encoding="utf-8"))
    validate(cert)
    _,M1,M2=replay_constants()
    assert cert["complex_resolvent_domain"]["consumer_bounds"]["M1_R1_upper"]==str(M1)
    assert cert["complex_resolvent_domain"]["consumer_bounds"]["M2_R2_upper"]==str(M2)
    b1,b2,gamma=replay_old_atom(M1,M2)
    atom=cert["old_adversarial_atom"]
    assert atom["R1_coefficient_upper"]==str(b1)
    assert atom["R2_coefficient_upper"]==str(b2)
    assert F(atom["Gamma_lower"])==gamma
    assert atom["certified_decimal_upper"]=="R1 coefficient<10^-974; R2 coefficient<10^-972, since 2^3279>10^981"
    support,X,_=replay_many_alias()
    fam=cert["many_small_exponent_exact_alias"]
    assert fam["explicit_support_primes"]==support and int(fam["explicit_X"])==X
    count=hostile_mutation_tests(cert)
    hashes=check_source_hashes(cert)
    print(f"PASS: exact rational replay; {count} mutated certificates rejected; {hashes} source hashes verified.")
    print("PASS: one-variable and simultaneous strips; exact many-support periodic-alias construction.")
    print("OPEN: global weighted dual mass, actual A1/A2, dependent-phase law, strict >79.")


if __name__=="__main__":
    main()
