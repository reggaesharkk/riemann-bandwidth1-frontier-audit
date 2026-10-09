"""Exact finite audit of WP84 callback-mask equivariance.

This is an origin-level structural census, not a source selector and not a
prime-sum evaluation.  It treats the 8,740 frozen raw survivor labels as the
nodes of the support-function model and only adds equality edges proved by
the executable callback contract.  The full per-(T,section) callback-key set
is not enumerable from the checked-in source because the source mask and its
selected section are not implemented.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURVIVORS = ROOT / "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv"
FUNCTIONALS = ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"
MASK_CONTRACT = ROOT / "notes/WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json"
AMPLITUDE = ROOT / "src/wp84_fifth_full_pool_amplitude.py"
OUT = ROOT / "notes/WP84_MASK_EQUIVARIANCE_LADDER_CERTIFICATE.json"
R = 6000
OMEGA = {5: "-11501/12500", 6: "137641/250000"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_rows():
    with SURVIVORS.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    origins = {
        (int(r["degree"]), r["sign_word"], r["equality_labels"])
        for r in rows
    }
    if len(origins) != 8740:
        raise AssertionError(f"raw-origin count {len(origins)} != 8740")
    return rows, origins


def norm(labels):
    remap = {}
    out = []
    for label in labels:
        if label not in remap:
            remap[label] = len(remap)
        out.append(remap[label])
    return ",".join(map(str, out))


def rotate(origin):
    b, signs, part = origin
    labels = list(map(int, part.split(",")))
    return b, signs[1:] + signs[:1], norm(labels[1:] + labels[:1])


def reverse(origin):
    b, signs, part = origin
    return b, signs[::-1], norm(list(map(int, part.split(",")))[::-1])


def conjugate(origin):
    b, signs, part = origin
    return b, "".join("-" if c == "+" else "+" for c in signs), part


def component_census(origins, generators):
    remaining = set(origins)
    components = []
    while remaining:
        seed = next(iter(remaining))
        todo = [seed]
        component = {seed}
        while todo:
            x = todo.pop()
            for gen in generators:
                y = gen(x)
                if y not in origins:
                    raise AssertionError(f"generator left frozen origin set: {gen.__name__} {x} -> {y}")
                if y not in component:
                    component.add(y)
                    todo.append(y)
        remaining.difference_update(component)
        components.append(component)
    return len(components), dict(sorted(Counter(map(len, components)).items()))


def alias_census(rows, generators):
    """Orbit census on (degree, sign, partition, alias m), hence m is a node key."""
    nodes = {
        (int(r["degree"]), r["sign_word"], r["equality_labels"], int(r["m"]))
        for r in rows
    }
    remaining = set(nodes)
    components = []
    while remaining:
        todo = [next(iter(remaining))]
        component = {todo[0]}
        while todo:
            x = todo.pop()
            for gen in generators:
                y = gen(x)
                if y not in nodes:
                    raise AssertionError(f"alias generator left frozen table: {x} -> {y}")
                if y not in component:
                    component.add(y)
                    todo.append(y)
        remaining.difference_update(component)
        components.append(component)
    return len(nodes), len(components), dict(sorted(Counter(map(len, components)).items()))


def alias_rotate(node):
    b, signs, part, m = node
    return (*rotate((b, signs, part)), m)


def alias_reverse(node):
    b, signs, part, m = node
    return (*reverse((b, signs, part)), m)


def alias_conjugate(node):
    b, signs, part, m = node
    return (*conjugate((b, signs, part)), -m)


def canonical_fid_map(functionals):
    result = {}
    for fun in functionals:
        fid = int(fun["id"])
        for b, signs, part in fun["raw_orbit_members"]:
            key = (int(b), signs, part)
            if key in result:
                raise AssertionError("raw origin belongs to multiple canonical fids")
            result[key] = fid
    return result


def build() -> dict:
    rows, origins = parse_rows()
    functions = json.loads(FUNCTIONALS.read_text(encoding="utf-8"))
    mask_contract = json.loads(MASK_CONTRACT.read_text(encoding="utf-8"))
    amplitude_text = AMPLITUDE.read_text(encoding="utf-8")
    fid_of = canonical_fid_map(functions)
    if set(fid_of) != origins or len(functions) != 453:
        raise AssertionError("canonical functional/origin map does not match frozen census")
    for origin in origins:
        if any(fid_of[g(origin)] != fid_of[origin] for g in (rotate, reverse, conjugate)):
            raise AssertionError("certified generator leaves its canonical fid orbit")

    by_degree = Counter(b for b, _, _ in origins)
    pair_rows = Counter(int(row["degree"]) for row in rows)
    raw_total, raw_hist = component_census(origins, [])
    c_total, c_hist = component_census(origins, [conjugate])
    r_total, r_hist = component_census(origins, [reverse])
    rot_total, rot_hist = component_census(origins, [rotate])
    cr_total, cr_hist = component_census(origins, [conjugate, reverse])
    cc_total, cc_hist = component_census(origins, [conjugate, rotate])
    d_total, d_hist = component_census(origins, [rotate, reverse])
    full_total, full_hist = component_census(origins, [conjugate, rotate, reverse])
    alias_nodes, alias_identity, alias_identity_hist = alias_census(rows, [])
    _, alias_conj, alias_conj_hist = alias_census(rows, [alias_conjugate])
    _, alias_conj_rev, alias_conj_rev_hist = alias_census(rows, [alias_conjugate, alias_reverse])
    _, alias_full, alias_full_hist = alias_census(rows, [alias_conjugate, alias_rotate, alias_reverse])
    _, alias_cyc, alias_cyc_hist = alias_census(rows, [alias_rotate])
    _, alias_rev, alias_rev_hist = alias_census(rows, [alias_reverse])
    _, alias_conj_cyc, alias_conj_cyc_hist = alias_census(rows, [alias_conjugate, alias_rotate])
    _, alias_dihedral, alias_dihedral_hist = alias_census(rows, [alias_rotate, alias_reverse])
    if (raw_total, c_total, cr_total, full_total) != (8740, 4370, 2237, 453):
        raise AssertionError("exact subgroup orbit census changed")
    if (alias_nodes, alias_identity, alias_conj, alias_conj_rev, alias_full) != (21588, 21588, 10794, 5530, 1148):
        raise AssertionError("exact class-alias subgroup census changed")

    # The only forced equality on callback bits is literal equality of the
    # complete six-field callback argument.  Dummy block names normalize away.
    callback_contract = mask_contract["contract"]
    expected_args = ["fid", "slots", "lag", "T", "section", "m"]
    if callback_contract["callback_call_arguments"] != expected_args:
        raise AssertionError("callback signature changed")
    if callback_contract["callback_result_consumed_as_boolean_filter"] is not True:
        raise AssertionError("callback truthiness semantics changed")
    if callback_contract["project_python_source_mask_definitions"] != []:
        raise AssertionError("a source-mask implementation is now recorded; re-audit required")
    if "source_mask(fid,slots,lag,T,section,m)" not in amplitude_text:
        raise AssertionError("callback call site changed")

    generators = [
        {
            "name": "literal_same_callback_key",
            "classification": "A",
            "mask_claim": "Equal complete tuples (fid,slots,lag,T,section,m) are one bit by definition.",
            "functional_status": "identity",
            "action": {"degree": "fixed", "sign_word": "fixed", "partition": "fixed", "alias": "fixed", "slots": "fixed", "lag": "fixed", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed", "W": "fixed", "K": "fixed", "Real": "fixed", "callback_key": "fixed"},
            "proved_callback_equality": True,
            "component_effect_on_8740_origin_refinement": "identity only; does not identify distinct raw origins",
            "hostile_distinguishing_callback": None,
        },
        {
            "name": "dummy_equality_block_label_renaming",
            "classification": "A",
            "mask_claim": "A pure renaming of temporary equality-block variables, followed by consistent renaming of their assigned primes, leaves the physical slot tuple unchanged; canonical restricted-growth partition labels normalize to the same partition.",
            "functional_status": "coordinate gauge; no physical slot permutation",
            "action": {"degree": "fixed", "sign_word": "fixed", "partition": "same set partition after canonical normalization", "alias": "fixed", "slots": "identical after reindexing dummy assignment variables", "lag": "fixed", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed", "W": "fixed", "K": "fixed", "Real": "fixed", "callback_key": "identical after canonicalization"},
            "proved_callback_equality": True,
            "component_effect_on_8740_origin_refinement": "none; this bookkeeping quotient is already applied in equality_labels",
            "hostile_distinguishing_callback": "not applicable: semantic callback tuple is identical",
        },
        {
            "name": "dummy_prime_block_relabeling",
            "classification": "A",
            "mask_claim": "A simultaneous renaming of block variables and their prime assignment is dummy-variable renaming only; it leaves each physical slot prime unchanged.",
            "functional_status": "coordinate gauge when all block data are relabeled together",
            "action": {"degree": "fixed", "sign_word": "fixed", "partition": "same set partition", "alias": "fixed", "slots": "identical", "lag": "fixed", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed", "W": "fixed", "K": "fixed", "Real": "fixed", "callback_key": "identical"},
            "proved_callback_equality": True,
            "component_effect_on_8740_origin_refinement": "none; no distinct node is identified",
            "hostile_distinguishing_callback": "not applicable: it is not a physical reassignment of primes among slots",
        },
        {
            "name": "cyclic_slot_rotation",
            "classification": "D",
            "mask_claim": "Mask covariance is not forced; the arbitrary callback can distinguish the rotated fid/slots/lag key.",
            "functional_status": "C: complete unmasked path sum is invariant after rotating signs, partition, physical slots, and closed lag path together; root-start phase is compensated by K.",
            "action": {"degree": "fixed", "sign_word": "cyclic left rotation", "partition": "same rotation then canonicalize labels", "alias": "fixed", "slots": "cyclic left rotation", "lag": "cyclic left rotation", "T": "fixed", "section": "fixed endpoints", "carrier_lambda": "fixed", "W": "multiplied by exp(-2*pi*i*u_s*lambda/L)", "K": "compensating root phase; M unchanged", "Real": "unchanged after W*K compensation", "callback_key": "raw fid/origin mapping is not specified; under the canonical 453 interface the fid is fixed while slots/lag generally change"},
            "proved_callback_equality": False,
            "conditional_property": "For every source admission factor, rotating its indexed slot-window family and all slot data must preserve the Boolean conjunction exactly.",
            "hostile_distinguishing_callback": "indicator of the first transformed six-tuple; 1 on k and 0 on rotate(k), whenever the tuples differ",
        },
        {
            "name": "path_reversal_with_negative_reversed_lags",
            "classification": "D",
            "mask_claim": "Mask covariance is not forced; reversed slots/lag give a distinguishable key.",
            "functional_status": "C: complete unmasked path sum is invariant; f_{-l}^epsilon phase is canceled by the reversed slot-start phase and the root extrema are unchanged.",
            "action": {"degree": "fixed", "sign_word": "reverse", "partition": "reverse then canonicalize labels", "alias": "fixed", "slots": "reverse", "lag": "reverse order and negate each entry", "T": "fixed", "section": "fixed endpoints", "carrier_lambda": "fixed", "W": "same after slotwise phase cancellation", "K": "same", "Real": "same", "callback_key": "raw fid/origin mapping is not specified; under the canonical 453 interface fid is fixed while slots/lag generally change"},
            "proved_callback_equality": False,
            "conditional_property": "The source admission/window predicate must be invariant under reversing the physical slot-window list together with the slots and reversing-negating the lag vector.",
            "hostile_distinguishing_callback": "indicator of the first transformed six-tuple; 1 on k and 0 on reverse(k), whenever the tuples differ",
        },
        {
            "name": "simultaneous_conjugation_sign_reversal_and_alias_inversion",
            "classification": "D",
            "mask_claim": "Mask covariance is not forced; fid and m change, while a callback may distinguish them.",
            "functional_status": "C: sign word and lambda change sign, m maps to -m, W and K conjugate, and the complete real functional is unchanged.",
            "action": {"degree": "fixed", "sign_word": "flip every +/− within the full-covariant origin orbit", "partition": "fixed", "alias": "m -> -m", "slots": "fixed", "lag": "fixed", "T": "fixed", "section": "fixed", "carrier_lambda": "lambda -> -lambda", "W": "conjugate", "K": "conjugate", "Real": "unchanged", "callback_key": "raw fid/origin mapping is not specified; canonical 453 interface keeps fid fixed and m changes sign"},
            "proved_callback_equality": False,
            "conditional_property": "The complete original source admission predicate, including slot-window membership and orientation/section conditions, must be invariant under (fid,slots,lag,T,I,m) -> (conj(fid),slots,lag,T,I,-m).",
            "hostile_distinguishing_callback": "indicator of m=m0 for a nonzero alias pair; it is truthy on one key and false on its conjugate key",
        },
        {
            "name": "alias_sign_exchange_alone",
            "classification": "D",
            "mask_claim": "Changing only m changes a callback argument and no contract equality links the two bits.",
            "functional_status": "not a complete correlation symmetry by itself; delta window is centered on a different alias",
            "action": {"degree": "fixed", "sign_word": "fixed", "partition": "fixed", "alias": "m -> -m", "slots": "fixed", "lag": "fixed", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed", "W": "fixed", "K": "fixed", "Real": "fixed", "callback_key": "m changes"},
            "proved_callback_equality": False,
            "hostile_distinguishing_callback": "indicator of the original alias value m0",
        },
        {
            "name": "physical_slot_permutation_not_generated_by_D_b",
            "classification": "D",
            "mask_claim": "An arbitrary physical permutation changes slots and generally the path order; no general source-window equality is in the API.",
            "functional_status": "not a general symmetry; only the certified cyclic/reversal transformations are justified for the complete path sum",
            "action": {"degree": "fixed", "sign_word": "same permutation only if explicitly applied", "partition": "same permutation only if explicitly applied", "alias": "not generally fixed", "slots": "permuted", "lag": "not generally a symmetry unless cyclic/reversal rule", "T": "fixed", "section": "fixed", "carrier_lambda": "may change if signs not permuted with slots", "W": "not generally fixed", "K": "not generally fixed", "Real": "not generally fixed", "callback_key": "slots and possibly fid/lag change"},
            "proved_callback_equality": False,
            "conditional_property": "All permuted physical slot-window functions must be identical after the same permutation, with every path and root factor transformed by an independently proved symmetry.",
            "hostile_distinguishing_callback": "indicator of a selected ordered slots tuple",
        },
        {
            "name": "Fourier_displacement_negation_alone",
            "classification": "D",
            "mask_claim": "Negating lag alone changes a callback argument; the original root/path weights do not supply a mask identity.",
            "functional_status": "not invariant alone; reversal requires simultaneous slot/sign/partition transformation",
            "action": {"degree": "fixed", "sign_word": "fixed", "partition": "fixed", "alias": "fixed", "slots": "fixed", "lag": "-lag", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed", "W": "generally changed", "K": "generally changed", "Real": "not known invariant", "callback_key": "lag changes"},
            "proved_callback_equality": False,
            "hostile_distinguishing_callback": "indicator of the original lag tuple",
        },
        {
            "name": "root_summation_index_translation",
            "classification": "A",
            "mask_claim": "A change of dummy root summation index is not a distinct callback key: root indices are computed after callback and are not callback arguments.",
            "functional_status": "reindexing only when the endpoints and phase compensation are preserved",
            "action": {"degree": "fixed", "sign_word": "fixed", "partition": "fixed", "alias": "fixed", "slots": "fixed", "lag": "fixed", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed", "W": "fixed", "K": "same sum after valid dummy reindexing", "Real": "fixed", "callback_key": "identical"},
            "proved_callback_equality": True,
            "component_effect_on_8740_origin_refinement": "none; root summation indices do not label origin bits",
            "hostile_distinguishing_callback": None,
        },
        {
            "name": "repeated_equal_prime_slot_swap_with_lag_swap",
            "classification": "D",
            "mask_claim": "Even when the swapped slot-prime entries are numerically equal, swapping lag coordinates changes the lag tuple; no source equality of the callback bits is defined.",
            "functional_status": "depends on the exact pair of window functions and path transformation; not a universal physical permutation theorem",
            "action": {"degree": "fixed", "sign_word": "permuted", "partition": "permuted", "alias": "not necessarily changed", "slots": "may be numerically unchanged at equal-prime positions", "lag": "coordinates swap", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed only under simultaneous sign/slot permutation", "W": "not generally fixed", "K": "not generally fixed", "Real": "not generally fixed", "callback_key": "fid and/or lag generally change"},
            "proved_callback_equality": False,
            "conditional_property": "The two physical slot-window tests must be identical functions and the full trace/path expression must be invariant under their swap.",
            "hostile_distinguishing_callback": "indicator of the original lag coordinate order",
        },
        {
            "name": "slot_window_swap_under_explicit_identical_window_hypothesis",
            "classification": "B",
            "mask_claim": "Conditional only: if the two complete indexed source-window/admission functions are identical after the physical slot swap, the corresponding callback values agree.",
            "functional_status": "the full path-weighted functional still needs its own permitted slot/path symmetry; identical windows alone do not establish a functional identity",
            "action": {"degree": "fixed", "sign_word": "swap the two designated positions", "partition": "swap positions and normalize", "alias": "fixed only if carrier and detuning are preserved", "slots": "swap designated entries", "lag": "swap according to an independently valid path symmetry", "T": "fixed", "section": "fixed", "carrier_lambda": "fixed only under simultaneous sign permutation", "W": "not asserted without a functional symmetry", "K": "not asserted without a functional symmetry", "Real": "not asserted", "callback_key": "changes unless the swapped data happen to coincide"},
            "proved_callback_equality": False,
            "conditional_property": "P_swap: the entire original admission predicate satisfies chi(swap(k))=chi(k) for every admissible input; a sufficient window-level version requires identical window functions plus invariance of the remaining alias/orientation/section gates.",
            "hostile_distinguishing_callback": "indicator of the ordered slots tuple when P_swap is not assumed",
        },
        {
            "name": "unspecified_slot_window_intersection_symmetry",
            "classification": "E",
            "mask_claim": "The actual source-window relation is undecidable from the checked-in source because its predicate is an absent caller-supplied implementation.",
            "functional_status": "no particular intersection symmetry is certified",
            "action": {"degree": "unspecified", "sign_word": "unspecified", "partition": "unspecified", "alias": "unspecified", "slots": "depends on the missing window rule", "lag": "depends on the missing window rule", "T": "fixed", "section": "fixed", "carrier_lambda": "not enough data", "W": "not enough data", "K": "not enough data", "Real": "not enough data", "callback_key": "not enough data"},
            "proved_callback_equality": False,
            "evidence_boundary": "The task does not reconstruct or guess this missing predicate; the callback API itself allows distinguishing values, while whether the intended source mask has this symmetry is not decidable here.",
            "hostile_distinguishing_callback": "interface-level table separates any two distinct keys; it does not decide the absent authentic source predicate",
        },
        {
            "name": "real_part_conjugate_pairing",
            "classification": "C",
            "mask_claim": "Real-part linearity gives coefficient identities but does not equate independent mask bits.",
            "functional_status": "For z and conjugate(z), Re(x*z+y*conjugate(z))=(x+y)*Re(z) for x,y in {0,1}.",
            "action": {"degree": "fixed", "sign_word": "conjugate pair within one canonical fid orbit", "partition": "same", "alias": "m -> -m", "slots": "same", "lag": "same", "T": "fixed", "section": "fixed", "carrier_lambda": "sign reversed", "W": "conjugate", "K": "conjugate", "Real": "equal scalar coefficients", "callback_key": "same fid/slots/lag/T/section; m generally changes"},
            "proved_callback_equality": False,
            "exact_algebra": "independent bits x,y remain: x*a+y*a; sup over x,y is 2*[a]_+, equal to [2a]_+ but not because x=y",
            "hostile_distinguishing_callback": "x=1,y=0 is allowed by the product Boolean interface",
        },
        {
            "name": "identical_key_atom_aggregation",
            "classification": "A",
            "mask_claim": "Contributions with exactly the same six callback arguments multiply the same Boolean bit; they are already summed into a_k before support maximization.",
            "functional_status": "exact linear coefficient aggregation",
            "action": {"degree": "fixed", "sign_word": "may differ outside key; key identity controls", "partition": "may differ outside key", "alias": "same", "slots": "same", "lag": "same", "T": "same", "section": "same", "carrier_lambda": "may vary inside summed coefficient", "W": "summed", "K": "summed", "Real": "linearity", "callback_key": "identical"},
            "proved_callback_equality": True,
            "component_effect_on_8740_origin_refinement": "already represented by coefficient a_k; not a new cross-key relation",
            "hostile_distinguishing_callback": None,
        },
    ]

    # Full-covariant orbits from the historical formal quotient are reproduced
    # as a conditional reference, never imported as proved mask edges.
    subgroup = [
        {"level": 0, "name": "executable_callback_product_class", "added_properties": [], "proved": True, "components": alias_identity, "histogram": alias_identity_hist, "origin_only_components": raw_total},
        {"level": 1, "name": "dummy_label_gauge_only", "added_properties": ["consistent renaming of nonphysical equality-block variables"], "proved": True, "components": alias_identity, "histogram": alias_identity_hist, "origin_only_components": raw_total},
        {"level": 2, "name": "conditional_conjugation", "added_properties": ["C: exact source-admission invariance under simultaneous sign-word conjugation and m -> -m"], "proved": False, "components": alias_conj, "histogram": alias_conj_hist, "origin_only_components": c_total},
        {"level": 3, "name": "conditional_conjugation_plus_reversal", "added_properties": ["level 2", "R: exact source-admission invariance under reversed slots and negative reversed lag"], "proved": False, "components": alias_conj_rev, "histogram": alias_conj_rev_hist, "origin_only_components": cr_total},
        {"level": 4, "name": "conditional_full_dihedral_conjugation", "added_properties": ["level 3", "Cyc: exact source-admission invariance under cyclic slot/lag rotation"], "proved": False, "components": alias_full, "histogram": alias_full_hist, "origin_only_components": full_total},
    ]

    # Construct key-schema witnesses rather than fabricated prime rows. They
    # show that the callback API itself has no equality axiom for distinct
    # tuples; they do not assert the absent iterator generates each pair.
    conj_fun = next(f for f in functions if any(-int(m) in {int(x) for x in f["aliases"]} for m in f["aliases"]))
    sample_fid = int(conj_fun["id"])
    sample_m = next(int(m) for m in conj_fun["aliases"] if -int(m) in {int(x) for x in conj_fun["aliases"]})
    b = int(conj_fun["degree"])
    slots = tuple(f"p_{i}" for i in range(b))
    lag = tuple(f"ell_{i}" for i in range(b))
    base_key = (sample_fid, slots, lag, "T", "I", sample_m)
    conjugate_key = (sample_fid, slots, lag, "T", "I", -sample_m)
    rotate_key = (sample_fid, slots[1:] + slots[:1], lag[1:] + lag[:1], "T", "I", sample_m)
    reverse_key = (sample_fid, slots[::-1], tuple(f"-{x}" for x in lag[::-1]), "T", "I", sample_m)
    hostile = {}
    for name, other in (("conjugation", conjugate_key), ("rotation", rotate_key), ("reversal", reverse_key)):
        if other == base_key:
            raise AssertionError(f"sample key is fixed under {name}; select another origin")
        callback = lambda key, chosen=base_key: int(key == chosen)
        hostile[name] = {"base_key_schema": repr(base_key), "transformed_key_schema": repr(other), "callback_values": [callback(base_key), callback(other)], "scope": "truthiness callback distinguishes distinct API tuples; this schema witness does not claim the missing iterator generates both keys or is a source-authentic window implementation"}

    cert = {
        "schema": "wp84-mask-equivariance-ladder-v1",
        "decision": "F. PRIOR 453 MASK-COMPONENT COLLAPSE OMITS THE CALLBACK ALIAS INDEX",
        "starting_commit": "0a4aade6900d2e4ed11cb534508461d0aeab0fad",
        "branch": "codex/c5-c6-attack-20261006",
        "source_hashes": {p.relative_to(ROOT).as_posix(): sha(p) for p in (SURVIVORS, FUNCTIONALS, MASK_CONTRACT, AMPLITUDE)},
        "source_semantics": {
            "callback_key": ["fid", "slots", "lag", "T", "section", "m"],
            "callback_return_use": "truthiness filter; not a weight or rewritten atom",
            "source_mask_implementation": "absent from the iterator source; required caller input",
            "selected_section_and_window_rule": "not executable here; this audit does not reconstruct it",
            "origin_model_limit": "The callback key includes alias m. Therefore the 21588 (raw origin,m) rows, not just the 8740 raw origins, are the smallest finite symbolic Boolean-node census. The actual per-(T,I) key set K_T also ranges over prime assignments, lags, and supplied sections and is not enumerated; with no proved cross-key equalities its component count is exactly |K_T|.",
            "canonical_fid_mapping_limit": "The callback receives one of 453 canonical functional IDs, but the raw 8740 origin table has no executable mapping from each transformed origin to a separate source-mask argument. The formal origin/alias action is certified; its embedding into actual source callback keys is not.",
            "unconditional_equality_relation": "only literal equality of the complete callback tuple; dummy labels are canonicalized before the tuple is formed",
        },
        "origin_census": {
            "raw_survivor_classes": raw_total,
            "fifth": by_degree[5],
            "sixth": by_degree[6],
            "class_alias_pairs": len(rows),
            "class_alias_pair_nodes": alias_nodes,
            "fifth_class_alias_pairs": pair_rows[5],
            "sixth_class_alias_pairs": pair_rows[6],
            "full_covariant_reference": 453,
            "alias_values_nonzero": all(int(r["m"]) != 0 for r in rows),
        },
        "group_generators": generators,
        "proved_equality_constraints": [
            {"relation": "chi(k)=chi(k') iff k==k' as full six-field callback tuple", "kind": "variable identity", "nontrivial_cross_key_edge": False},
            {"relation": "dummy equality-block or prime-variable renaming", "kind": "representation gauge", "nontrivial_semantic_edge": False},
        ],
        "mask_constraint_graph": {"origin_refinement_nodes": raw_total, "origin_alias_refinement_nodes": alias_nodes, "proved_nontrivial_edges": [], "identity_loops_omitted": True, "origin_components": raw_total, "origin_component_histogram": raw_hist, "origin_alias_components": alias_identity, "origin_alias_component_histogram": alias_identity_hist, "actual_callback_key_graph": "not enumerated; nodes are exact six-tuples arising from all admitted prime assignments, paths, aliases and supplied (T,section)"},
        "component_counts": {
            "proved_origin_refinement": raw_total,
            "proved_origin_histogram": raw_hist,
            "proved_origin_alias_refinement": alias_identity,
            "proved_origin_alias_histogram": alias_identity_hist,
            "actual_callback_key_components": "|K_T|; exact key set not enumerated in current source",
            "actual_mask_component_warning": "m is an explicit callback-key coordinate, so a class-alias pair cannot be treated as one Boolean bit; 21588 is the finite raw (origin,m) lower-level node set before the unenumerated slot/path/T/section expansion.",
            "full_covariant_origin_reference": full_total,
            "full_covariant_origin_histogram": full_hist,
            "full_covariant_origin_alias_components": alias_full,
            "full_covariant_origin_alias_histogram": alias_full_hist,
            "453_requires_alias_mask_aggregation": True,
            "why_453_is_not_a_mask_component_count": "The 453 functionals sum each representative's aliases inside one C_j, but source_mask is called with m and can return a different bit for each alias. Full D_b x C2 covariance on (raw origin,m) yields 1148 components, not 453.",
        },
        "conditional_covariance_ladder": subgroup,
        "alternative_subgroup_counts": {
            "cyclic_rotation_only": {"origin_components": rot_total, "origin_histogram": rot_hist, "origin_alias_components": alias_cyc, "origin_alias_histogram": alias_cyc_hist},
            "reversal_only": {"origin_components": r_total, "origin_histogram": r_hist, "origin_alias_components": alias_rev, "origin_alias_histogram": alias_rev_hist},
            "conjugation_plus_cyclic_rotation": {"origin_components": cc_total, "origin_histogram": cc_hist, "origin_alias_components": alias_conj_cyc, "origin_alias_histogram": alias_conj_cyc_hist},
            "dihedral_without_conjugation": {"origin_components": d_total, "origin_histogram": d_hist, "origin_alias_components": alias_dihedral, "origin_alias_histogram": alias_dihedral_hist},
        },
        "minimal_missing_source_properties": [
            {"name": "P_conj", "statement": "On raw class-alias nodes, simultaneous sign conjugation and m -> -m preserves the complete source admission bit.", "window_identity_needed": "The complete sign/orientation-specific window and admission predicate is invariant under conjugation. This only gives 21588 -> 10794 pair components.", "proved": False, "leverage": "alias-expanded components 21588 -> 10794"},
            {"name": "P_rev", "statement": "Reversing signs/partition/slots and negative-reversing lag preserves the complete source admission bit at fixed m.", "window_identity_needed": "The physical slot-window family and every endpoint/section admission factor are invariant under reversal. This gives 10794 -> 5530 pair components after P_conj.", "proved": False, "leverage": "alias-expanded components 10794 -> 5530"},
            {"name": "P_cyc", "statement": "Cyclically rotating signs/partition/slots and lag preserves the complete source admission bit at fixed m.", "window_identity_needed": "The source slot-window list is cyclically covariant and source-section/root eligibility is unchanged. This gives 5530 -> 1148 pair components, not 453.", "proved": False, "leverage": "alias-expanded components 5530 -> 1148"},
            {"name": "P_alias_merge", "statement": "To recover 453 support components one would also have to identify different m values aggregated in each canonical functional.", "window_identity_needed": "No such property is compatible in general with the exact per-alias condition 0<|lambda-mL|<=H/T: for distinct m,m', the alias windows are disjoint once 2H/T < |m-m'|L. A tuple admitted at m is rejected at m'.", "proved": False, "leverage": "would formally merge 1148 alias-expanded orbits into 453 origin functionals, but is not source-legal and is false whenever a nonzero alias is admitted"},
        ],
        "alias_separation": {
            "source_statement": "Each callback is called separately for a listed alias m, and the exact source condition includes 0<|lambda-mL|<=H/T with H/T<L/2 eventually.",
            "disjointness": "For m != m', the intervals |lambda-mL|<=H/T and |lambda-m'L|<=H/T are disjoint whenever 2H/T < |m-m'|L; in particular the nearest-residual condition admits at most one alias for fixed lambda.",
            "consequence": "Different alias values cannot be silently summed into one callback bit. An alias-constant mask would be incompatible with a key admitted at one alias and rejected at another.",
            "frozen_source": "notes/WP84_NEAR_ALIAS_SURVIVOR_LEMMA.md states H fixed positive (or explicitly declared H=X^o(1)), H/T<L/2, and uniqueness of the nearest alias.",
            "proof_scope": "exact interval geometry; it does not assert existence of an admitted prime tuple for a given alias",
        },
        "callback_distinguishing_witnesses": hostile,
        "real_part_and_coefficient_algebra": {
            "conjugate_pair_identity": "Re(x*z+y*conj(z))=(x+y)*Re(z), x,y in {0,1}.",
            "coefficient_relation": "conjugate raw terms have equal real scalar coefficients after full-sum reindexing, not opposite coefficients",
            "support_relation": "[a]_+ + [a]_+ = [2a]_+ exactly; the independent bits remain independent, and this identity earns no reduction in the positive-part support bound",
            "same_bit_same_coefficient": "all atoms with the same exact six-field key are already combined in a_k",
            "same_bit_opposite_coefficient": "possible only after exact same-key signed atom summation; no additional pair census is defined by current source",
            "independent_bits_same_coefficient": "the conjugation identity gives this at the formal complete-origin level, conditional on the origin-to-key map; the map is not executable",
            "independent_bits_opposite_coefficient": "no such relation is proved for the listed full symmetries",
            "exact_key_pair_enumeration": "not available: source callback membership and finite key set K_T are absent",
        },
        "support_function": {
            "actual_executable_key_form": "sup_{chi in {0,1}^{K_T}} sum_k chi_k a_k = sum_k [a_k]_+; only identical full callback tuples are pre-summed",
            "origin_refinement_form": "sum_{(r,m) in 21588 raw class-alias pairs} chi_(r,m) a_(r,m); with no proved off-diagonal equality its support is sum_(r,m) [a_(r,m)]_+",
            "conditional_components_form": "if a source property proves chi constant on components C, sup = sum_C [sum_(r,m in C) a_(r,m)]_+",
            "full_covariant_alias_form": "1148 components after P_conj, P_rev, and P_cyc on (raw origin,m)",
            "historical_453_form": "453 sums alias lists inside each functional; it additionally assumes away the callback m-index and is not the support function for the stated callback key",
        },
        "consumer_coefficients": {"omega5": OMEGA[5], "omega6": OMEGA[6], "sign_convention": "raw degree-5 coefficient is negative; raw degree-6 coefficient is positive"},
        "budget_and_theorem_state": {
            "relaxed_allowance": "52897896569489/572357731837500000",
            "relaxed_H400_scale": "52897896569489/115043904099337500000",
            "relaxed_budget": "UNPAID; this audit does not estimate coefficients",
            "fifth_analytic_rank": "38-72",
            "strict_gt_79": "OPEN",
        },
        "source_conditions": {"R": R, "prime_cutoff": "N(T)=floor(exp(L-sqrt(L)))", "complete_prime_pool": True, "diagnostic_core": False, "long_tail_retained": True, "long_tail_transforms": "|delta| and nearest residual cell are preserved by conjugation; lambda and |delta| are preserved by the simultaneous path reindexings; R and complete prime pool are unchanged", "selector_reconstructed": False},
        "hostile_mutation_rejection_cases": [
            "promote cyclic rotation", "promote reversal", "promote conjugation", "change equality partition", "change slot order", "change alias", "change R", "delete a raw origin", "replace complete prime pool by finite core", "merge independent bits", "split proved-equal bit", "use floating coefficient equality", "use diagnostic rows", "invent historical selector", "claim unconditional 453", "alter component count", "alter fifth/sixth signs", "omit long-tail compatibility"
        ],
    }
    return cert


def main() -> None:
    cert = build()
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS source-checked mask equivariance ladder")
    print("raw origins=8740; class-alias nodes=21588; no proved merge; full-covariant alias components=1148")
    print("453 counts origin functionals only and omits the callback alias coordinate")
    print("real-part identity gives equal coefficients, not equal callback bits")
    print("strict >79 OPEN; relaxed budget UNPAID")


if __name__ == "__main__":
    main()
