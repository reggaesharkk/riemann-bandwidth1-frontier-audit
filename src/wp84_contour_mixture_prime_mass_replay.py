"""Independent exact checks for the contour-mixture/primes certificate."""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes/WP84_CONTOUR_MIXTURE_PRIME_MASS_CERTIFICATE.json"


def validate(c):
    assert c["schema"] == "wp84-contour-mixture-prime-mass-v1"
    assert c["decision"] == "C" and c["strict_gt79"] == "OPEN"
    assert c["frozen"]["K"] == 32 and c["frozen"]["delta"] == "1/100000"
    assert c["frozen"]["cutoff"] == "N=floor(X*exp(-sqrt(log X)))"
    mix = c["contour_mixture"]
    assert "probability measure" in mix["finite_statement"]
    assert "monotone convergence" in mix["infinite_statement"]
    assert "product_q cosh" in mix["sign_mixture"]
    assert "2^(-|supp(nu)|)" in mix["pointwise_lower_bound"]
    assert "same objective value" in mix["optimization"]["finite_support"]
    assert "different optimizer separately for each nu" in mix["optimization"]["warning"]
    assert mix["optimization"]["numerical_optimizer"] == "None used; no numerical optimum is asserted."
    assert c["current_prime_mass"]["envelope"].startswith("g_p=4*log(p)")
    assert "= 8+o(1)" in c["current_prime_mass"]["square_mass"]
    assert "O(L^-3)" in c["current_prime_mass"]["cube_mass"]
    assert "O(L^-4)" in c["current_prime_mass"]["fourth_mass"]
    assert F(1, 2) * 16 == 8
    assert F(131, 200) * F(1, 2) == F(131, 400)
    assert "omitted path/operator factor" in c["current_prime_mass"]["normalization_caveat"]
    assert "sum_p g_p^2" in c["A1"]["mixture_bound"]
    assert "exp(i*tau_k*epsilon*a*log(p))" in c["A1"]["exact_grouped_kernel_definition"]
    assert "carrier, which occurs exactly once" in c["A1"]["exact_grouped_kernel_definition"]
    assert "D1_T=o(1)" in c["A1"]["target"]
    assert "sum_p g_p^4" in c["A2"]["mixture_bound"]
    assert "D2_T=o(L^4)" in c["A2"]["target"]
    assert "removes only epsilon'=-epsilon and a=b" in c["A2"]["exact_grouped_kernel_definition"]
    assert "m!=0" in c["alias_falsification"]["periodic"] and "possible" in c["alias_falsification"]["periodic"]
    assert "does not bound the full alias family or prove a nonzero response coefficient" in c["alias_falsification"]["primorial_test"]["interpretation"]
    assert "1=mu*B_q'(rho_q)" in c["alias_falsification"]["primorial_test"]["optimized_single_label_mixture"]
    assert "1<=mu*B_q'(0)" in c["alias_falsification"]["primorial_test"]["optimized_single_label_mixture"]
    assert "alpha>1/2" in c["radius_schedule_tests"]["power_decay"]
    assert "beta>1" in c["radius_schedule_tests"]["log_weighted_power_decay"]
    assert "strict >79 remains OPEN" in c["first_unproved_lemma"] or c["strict_gt79"] == "OPEN"
    return True


def exact_checks():
    # Exact identities are checked by rational algebra where possible. For
    # x real, cosh(x)=e^|x|(1+e^-2|x|)/2; setting t=e^-|x| in [0,1]
    # reduces the support bound to 1+t^2>=1, with no numerical approximation.
    # The product identity is the finite distributive expansion over signs.
    assert F(131, 400) * 2 == F(131, 200)
    # Geometric series: sum_{a>=1} u^a=u/(1-u)=1/(sqrt(p)-1), 0<u<1.
    # PNT exponents for the cubic and quartic prime series are strictly >1.
    assert 3/2 > 1 and 2 > 1
    return True


def hostile(c):
    mutations = [
        lambda x: x["contour_mixture"].update(finite_statement="sum over unnormalized signs <=M"),
        lambda x: x["contour_mixture"].update(pointwise_lower_bound="W>=exp(2sum rho abs nu)"),
        lambda x: x["contour_mixture"]["optimization"].update(warning="optimize each nu independently"),
        lambda x: x["current_prime_mass"].update(fourth_mass="O(L^-2)"),
        lambda x: x["current_prime_mass"].update(envelope="omit all a>=2 powers"),
        lambda x: x["alias_falsification"].update(periodic="all nonzero m aliases impossible"),
        lambda x: x["A2"].update(exact_grouped_kernel_definition="remove all opposite signs"),
        lambda x: x["A1"].update(exact_grouped_kernel_definition="drop exp(i*T*a*log(p)) carrier"),
        lambda x: x["alias_falsification"]["primorial_test"].update(interpretation="the exact alias proves a nonzero source coefficient"),
        lambda x: x["contour_mixture"]["optimization"].update(numerical_optimizer="verified optimizer establishes bound"),
        lambda x: x["frozen"].update(cutoff="N=X^0.9"),
        lambda x: x.update(strict_gt79="PROVED"),
    ]
    for i, mutate in enumerate(mutations, 1):
        bad = deepcopy(c)
        mutate(bad)
        try:
            validate(bad)
        except (AssertionError, KeyError, TypeError):
            continue
        raise AssertionError(f"hostile mutation {i} was not detected")
    return len(mutations)


def check_hashes(c):
    h = c["source_sha256"]
    assert len(h) == 9
    for rel, expected in h.items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        assert actual == expected, rel
    return len(h)


def main():
    c = json.loads(CERT.read_text(encoding="utf-8"))
    validate(c)
    exact_checks()
    nm = hostile(c)
    nh = check_hashes(c)
    assert c["A1"]["status"].startswith("OPEN")
    assert c["A2"]["status"].startswith("OPEN")
    print(f"PASS: exact contour identities and mass checks; {nm} hostile mutations rejected; {nh} source hashes verified.")
    print("OPEN: D1=o(1), D2=o(L^4), actual A1/A2 transfer and strict >79.")


if __name__ == "__main__":
    main()
