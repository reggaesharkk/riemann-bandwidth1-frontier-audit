"""Independent replay and adversarial mutation tests for the mask ladder.

This file deliberately does not import the certificate builder. It reparses
the frozen CSV, rebuilds subgroup components, checks the callback source
contract, and rejects 18 false promotions/corruptions.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes/WP84_MASK_EQUIVARIANCE_LADDER_CERTIFICATE.json"
PATTERNS = ROOT / "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv"
FUNCTIONALS = ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"
CONTRACT = ROOT / "notes/WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json"
AMPLITUDE = ROOT / "src/wp84_fifth_full_pool_amplitude.py"
EXPECTED_PROFILES = None


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def canonical_partition(s):
    labels = [int(x) for x in s.split(",")]
    table, out = {}, []
    for x in labels:
        if x not in table:
            table[x] = len(table)
        out.append(table[x])
    return ",".join(str(x) for x in out)


def actions():
    def r(x):
        d, s, p = x
        q = [int(v) for v in p.split(",")]
        return d, s[1:] + s[:1], canonical_partition(",".join(map(str, q[1:] + q[:1])))

    def v(x):
        d, s, p = x
        return d, s[::-1], canonical_partition(",".join(map(str, reversed([int(t) for t in p.split(",")]))))

    def c(x):
        d, s, p = x
        return d, "".join("-" if z == "+" else "+" for z in s), p

    return r, v, c


def alias_actions():
    r, v, c = actions()
    return (
        lambda x: (*r(x[:3]), x[3]),
        lambda x: (*v(x[:3]), x[3]),
        lambda x: (*c(x[:3]), -x[3]),
    )


def orbit_profile(nodes, generators):
    left = set(nodes)
    sizes = []
    while left:
        stack = [next(iter(left))]
        seen = {stack[0]}
        while stack:
            item = stack.pop()
            for generator in generators:
                target = generator(item)
                if target not in nodes:
                    raise AssertionError("generator maps outside the frozen survivor set")
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
        left.difference_update(seen)
        sizes.append(len(seen))
    return len(sizes), {str(k): v for k, v in sorted(Counter(sizes).items())}


def source_records():
    with PATTERNS.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    raw = {(int(z["degree"]), z["sign_word"], z["equality_labels"]) for z in rows}
    return rows, raw


def validate(cert):
    global EXPECTED_PROFILES
    rows, raw = source_records()
    rot, rev, conj = actions()
    arot, arev, aconj = alias_actions()
    alias_nodes = {(int(x["degree"]), x["sign_word"], x["equality_labels"], int(x["m"])) for x in rows}
    functions = json.loads(FUNCTIONALS.read_text(encoding="utf-8"))
    raw_to_fid = {}
    for fun in functions:
        for d, s, p in fun["raw_orbit_members"]:
            raw_to_fid[(int(d), s, p)] = int(fun["id"])
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    api = contract["contract"]
    if len(raw) != cert["origin_census"]["raw_survivor_classes"]:
        raise AssertionError("raw origin census mismatch")
    degrees = Counter(x[0] for x in raw)
    pair_counts = Counter(int(x["degree"]) for x in rows)
    if dict(degrees) != {5: 1132, 6: 7608}:
        raise AssertionError("degree census mismatch")
    census = cert["origin_census"]
    if census["fifth"] != degrees[5] or census["sixth"] != degrees[6]:
        raise AssertionError("per-degree origin census mismatch")
    if len(rows) != 21588 or dict(pair_counts) != {5: 1956, 6: 19632}:
        raise AssertionError("class/alias census mismatch")
    if not all(int(x["m"]) != 0 for x in rows):
        raise AssertionError("zero alias introduced")
    if len(functions) != 453:
        raise AssertionError("formal full-covariant reference changed")
    if set(raw_to_fid) != raw or any(raw_to_fid[g(x)] != raw_to_fid[x] for x in raw for g in (rot, rev, conj)):
        raise AssertionError("formal generator-to-canonical-fid mapping changed")
    if api["callback_call_arguments"] != ["fid", "slots", "lag", "T", "section", "m"]:
        raise AssertionError("callback key contract changed")
    if api["project_python_source_mask_definitions"] != []:
        raise AssertionError("source implementation is present; this audit must be rerun")
    if "source_mask(fid,slots,lag,T,section,m)" not in AMPLITUDE.read_text(encoding="utf-8"):
        raise AssertionError("iterator callback invocation changed")
    expected_hashes = {
        "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv": digest(PATTERNS),
        "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json": digest(FUNCTIONALS),
        "notes/WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json": digest(CONTRACT),
        "src/wp84_fifth_full_pool_amplitude.py": digest(AMPLITUDE),
    }
    if cert["source_hashes"] != expected_hashes:
        raise AssertionError("pinned source hashes mismatch")
    if cert["proved_equality_constraints"] != [
        {"relation": "chi(k)=chi(k') iff k==k' as full six-field callback tuple", "kind": "variable identity", "nontrivial_cross_key_edge": False},
        {"relation": "dummy equality-block or prime-variable renaming", "kind": "representation gauge", "nontrivial_semantic_edge": False},
    ]:
        raise AssertionError("unproved equality edge or split identity")

    cc = cert["component_counts"]
    if EXPECTED_PROFILES is None:
        EXPECTED_PROFILES = (
            orbit_profile(raw, []),
            orbit_profile(raw, [conj]),
            orbit_profile(raw, [conj, rev]),
            orbit_profile(raw, [conj, rot, rev]),
            orbit_profile(alias_nodes, []),
            orbit_profile(alias_nodes, [aconj]),
            orbit_profile(alias_nodes, [aconj, arev]),
            orbit_profile(alias_nodes, [aconj, arot, arev]),
        )
    expected0, expectedc, expectedcr, expectedfull, alias0, alias_conj, alias_conj_rev, alias_full = EXPECTED_PROFILES
    if expected0 != (8740, {"1": 8740}) or expectedc != (4370, {"2": 4370}):
        raise AssertionError("identity/conjugation component recomputation failed")
    if expectedcr[0] != 2237 or expectedfull[0] != 453:
        raise AssertionError("conditional component recomputation failed")
    if alias0 != (21588, {"1": 21588}) or alias_conj != (10794, {"2": 10794}):
        raise AssertionError("alias-expanded identity/conjugation count mismatch")
    if alias_conj_rev != (5530, {"2": 266, "4": 5264}):
        raise AssertionError("alias-expanded conjugation/reversal count mismatch")
    if alias_full != (1148, {"2": 7, "4": 10, "6": 44, "10": 79, "12": 290, "20": 58, "24": 660}):
        raise AssertionError("alias-expanded full-covariant count mismatch")
    if cc["proved_origin_refinement"] != expected0[0] or cc["proved_origin_histogram"] != expected0[1]:
        raise AssertionError("proved component count was compressed or split")
    if cc["proved_origin_alias_refinement"] != alias0[0] or cc["proved_origin_alias_histogram"] != alias0[1]:
        raise AssertionError("alias bit index was merged or split")
    if cc["full_covariant_origin_reference"] != expectedfull[0] or cc["full_covariant_origin_histogram"] != expectedfull[1]:
        raise AssertionError("full-covariant reference is incorrect")
    if cc["full_covariant_origin_alias_components"] != alias_full[0] or cc["full_covariant_origin_alias_histogram"] != alias_full[1]:
        raise AssertionError("full-covariant alias-expanded components are incorrect")
    ladder = cert["conditional_covariance_ladder"]
    expected_ladder = [21588, 21588, 10794, 5530, 1148]
    if [x["components"] for x in ladder] != expected_ladder:
        raise AssertionError("conditional ladder counts changed")
    if [x["origin_only_components"] for x in ladder] != [8740, 8740, 4370, 2237, 453]:
        raise AssertionError("origin-only reference ladder changed")
    if [x["proved"] for x in ladder] != [True, True, False, False, False]:
        raise AssertionError("conditional property was promoted to theorem")
    byname = {x["name"]: x for x in cert["group_generators"]}
    for name in ("cyclic_slot_rotation", "path_reversal_with_negative_reversed_lags", "simultaneous_conjugation_sign_reversal_and_alias_inversion"):
        if byname[name]["classification"] != "D" or byname[name]["proved_callback_equality"] is not False:
            raise AssertionError(f"false unconditional covariance: {name}")
    if byname["cyclic_slot_rotation"]["action"]["slots"] != "cyclic left rotation" or byname["cyclic_slot_rotation"]["action"]["lag"] != "cyclic left rotation":
        raise AssertionError("cyclic slot/path action corrupted")
    if byname["path_reversal_with_negative_reversed_lags"]["action"]["lag"] != "reverse order and negate each entry":
        raise AssertionError("reversal lag action corrupted")
    if byname["simultaneous_conjugation_sign_reversal_and_alias_inversion"]["action"]["alias"] != "m -> -m":
        raise AssertionError("conjugation alias action corrupted")
    for name in ("dummy_equality_block_label_renaming", "dummy_prime_block_relabeling", "root_summation_index_translation", "identical_key_atom_aggregation"):
        if byname[name]["classification"] != "A" or byname[name]["proved_callback_equality"] is not True:
            raise AssertionError(f"lost identity/gauge relation: {name}")
    if byname["real_part_conjugate_pairing"]["classification"] != "C":
        raise AssertionError("real-part algebra mislabeled as mask covariance")
    if next(x for x in cert["group_generators"] if x["name"] == "slot_window_swap_under_explicit_identical_window_hypothesis")["classification"] != "B":
        raise AssertionError("conditional window property missing")
    if next(x for x in cert["group_generators"] if x["name"] == "unspecified_slot_window_intersection_symmetry")["classification"] != "E":
        raise AssertionError("missing-source window status concealed")
    for witness in cert["callback_distinguishing_witnesses"].values():
        if witness["callback_values"] != [1, 0]:
            raise AssertionError("hostile callback no longer distinguishes transformed keys")
    if cert["origin_census"]["class_alias_pair_nodes"] != 21588:
        raise AssertionError("callback alias coordinate omitted from node census")
    if cert["component_counts"]["453_requires_alias_mask_aggregation"] is not True:
        raise AssertionError("453 alias aggregation defect concealed")
    if cert["support_function"]["full_covariant_alias_form"] != "1148 components after P_conj, P_rev, and P_cyc on (raw origin,m)":
        raise AssertionError("full-covariant alias support count changed")
    if cert["decision"] != "F. PRIOR 453 MASK-COMPONENT COLLAPSE OMITS THE CALLBACK ALIAS INDEX":
        raise AssertionError("prior 453 alias-index defect not reported")
    alias = cert["alias_separation"]
    if "2H/T < |m-m'|L" not in alias["disjointness"] or "nearest-residual condition admits at most one alias" not in alias["disjointness"]:
        raise AssertionError("alias-window disjointness argument omitted")
    if "H/T<L/2" not in alias["source_statement"]:
        raise AssertionError("alias uniqueness hypothesis omitted")
    if cert["source_conditions"]["R"] != 6000 or cert["source_conditions"]["complete_prime_pool"] is not True:
        raise AssertionError("source scale or full prime pool changed")
    if cert["source_conditions"]["diagnostic_core"] is not False or cert["source_conditions"]["selector_reconstructed"] is not False:
        raise AssertionError("diagnostic pool or invented selector detected")
    if not cert["source_conditions"]["long_tail_retained"] or not cert["source_conditions"]["long_tail_transforms"]:
        raise AssertionError("long-tail compatibility omitted")
    if cert["budget_and_theorem_state"]["relaxed_allowance"] != "52897896569489/572357731837500000":
        raise AssertionError("relaxed budget altered")
    if cert["consumer_coefficients"] != {"omega5": "-11501/12500", "omega6": "137641/250000", "sign_convention": "raw degree-5 coefficient is negative; raw degree-6 coefficient is positive"}:
        raise AssertionError("fifth/sixth consumer coefficient or sign altered")
    if cert["budget_and_theorem_state"]["fifth_analytic_rank"] != "38-72" or cert["budget_and_theorem_state"]["strict_gt_79"] != "OPEN":
        raise AssertionError("theorem status or rank changed")
    if not all(isinstance(cert["budget_and_theorem_state"][x], str) for x in ("relaxed_allowance", "relaxed_H400_scale")):
        raise AssertionError("exact rational serialized as a floating number")
    if Fraction(cert["budget_and_theorem_state"]["relaxed_allowance"]) != Fraction(52897896569489, 572357731837500000):
        raise AssertionError("rational budget parse failed")
    return True


def mutations(cert):
    cases = []
    def add(label, fn):
        c = copy.deepcopy(cert)
        fn(c)
        cases.append((label, c))

    add("promote cyclic rotation", lambda c: next(g for g in c["group_generators"] if g["name"] == "cyclic_slot_rotation").update(classification="A", proved_callback_equality=True))
    add("promote reversal", lambda c: next(g for g in c["group_generators"] if g["name"] == "path_reversal_with_negative_reversed_lags").update(classification="A", proved_callback_equality=True))
    add("promote conjugation", lambda c: next(g for g in c["group_generators"] if g["name"] == "simultaneous_conjugation_sign_reversal_and_alias_inversion").update(classification="A", proved_callback_equality=True))
    add("change equality partition", lambda c: c["origin_census"].update(fifth=1133))
    add("change slot ordering", lambda c: next(g for g in c["group_generators"] if g["name"] == "cyclic_slot_rotation")["action"].update(slots="fixed"))
    add("change alias", lambda c: next(g for g in c["group_generators"] if g["name"] == "simultaneous_conjugation_sign_reversal_and_alias_inversion")["action"].update(alias="fixed"))
    add("change R=6000", lambda c: c["source_conditions"].update(R=1))
    add("delete raw origin", lambda c: c["origin_census"].update(raw_survivor_classes=8739))
    add("finite core replaces full pool", lambda c: c["source_conditions"].update(complete_prime_pool=False))
    add("merge independent bits", lambda c: c["component_counts"].update(proved_origin_alias_refinement=1, proved_origin_alias_histogram={"21588": 1}))
    add("split proved-identical bit", lambda c: c["proved_equality_constraints"].pop(0))
    add("float coefficient comparison", lambda c: c["budget_and_theorem_state"].update(relaxed_allowance=0.09243))
    add("diagnostic rows", lambda c: c["source_conditions"].update(diagnostic_core=True))
    add("invent historical selector", lambda c: c["source_conditions"].update(selector_reconstructed=True))
    add("claim 453 unconditional", lambda c: c["component_counts"].update(proved_origin_alias_refinement=453))
    add("alter component count", lambda c: c["conditional_covariance_ladder"][2].update(components=10793))
    add("alter fifth/sixth consumer sign", lambda c: c["consumer_coefficients"].update(omega5="11501/12500"))
    add("omit long-tail compatibility", lambda c: c["source_conditions"].update(long_tail_transforms=""))
    return cases


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    validate(cert)
    rejected = []
    for label, altered in mutations(cert):
        try:
            validate(altered)
        except (AssertionError, KeyError, TypeError, ValueError):
            rejected.append(label)
        else:
            raise AssertionError("hostile mutation passed: " + label)
    if len(rejected) != 18:
        raise AssertionError(f"only rejected {len(rejected)}/18 hostile mutations")
    print("PASS independent origin census and subgroup orbit reconstruction")
    print("PASS callback API: only literal-key identity and dummy-label gauge are unconditional")
    print("PASS exact support formula and 18/18 hostile mutation rejections")
    print("F decision; 453 origin count is not alias-expanded mask component count (1148 under full formal covariance)")
    print("No source selector reconstructed; alias windows remain separate Boolean inputs")
    print("Strict >79 OPEN; relaxed budget UNPAID")


if __name__ == "__main__":
    main()
