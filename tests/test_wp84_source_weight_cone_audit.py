import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import wp84_source_weight_cone_audit as audit
import wp84_r400_filtered_sharp_repair as source_cumulant


class SourceWeightConeTests(unittest.TestCase):
    def test_partition_ledger_has_all_26_ordered_terms(self):
        terms = audit.ordered_partitions()
        self.assertEqual(len(terms), 26)
        self.assertEqual([sum(len(b) == k for _, b in terms) for k in range(1, 5)], [1, 7, 12, 6])
        self.assertEqual(sum(sign == 1 for sign, _ in terms), 13)
        self.assertEqual(sum(sign == -1 for sign, _ in terms), 13)

    def test_independent_partition_enumerator_matches_source_ledger(self):
        self.assertEqual(audit.ordered_partitions(), source_cumulant.terms())

    def test_actual_prime_power_atom_is_balanced_and_cutoff_legal(self):
        atom = audit.exact_source_atom_data()
        self.assertEqual(atom["n_exponents_of_p"], [1, 2, 3, 2])
        self.assertEqual(atom["epsilon"], [1, -1, 1, -1])
        self.assertEqual(atom["v"], ["1/5", "-2/5", "3/5", "-2/5"])
        self.assertEqual(atom["physical_closure_S"], "0")
        self.assertIn("p>=5", atom["admission_proof"])

    def test_source_cumulant_positive_for_all_selected_m_at_least_ten(self):
        for rows in (10, 11, 12, 13, 100, 1000000):
            lower, tail = audit.actual_weight_bound(rows)
            self.assertGreater(lower, Q(0))
            self.assertLessEqual(tail, Q(241, 625))
        self.assertEqual(audit.actual_weight_bound(10), (Q(384, 625), Q(241, 625)))
        self.assertEqual(Q(799, 4000) * Q(384, 625), Q(9588, 78125))

    def test_exact_denominator_five_vector_and_cone_violation(self):
        vector = audit.exact_grid_term_vector(audit.WITNESS, 10)
        self.assertEqual(vector[0], 1)
        self.assertEqual(sum(vector), 1)
        self.assertEqual(sum(value != 0 for value in vector), 1)
        self.assertGreater(sum(vector), 0)

    def test_all_six_balanced_orthants_24_orders_and_conjugates(self):
        vectors = audit.orientation_vectors()
        self.assertEqual(len(vectors), 24)
        self.assertEqual(len(set(vectors)), 12)
        self.assertEqual({tuple(i for i, x in enumerate(v) if x > 0) for v in vectors},
                         set(__import__("itertools").combinations(range(4), 2)))
        for vector in vectors:
            self.assertEqual(sum(vector, Q(0)), 0)
            self.assertEqual(sum(audit.exact_grid_term_vector(vector, 10)), 1)
            conjugate = tuple(-x for x in vector)
            self.assertEqual(sum(audit.exact_grid_term_vector(conjugate, 10)), 1)
        both_families = vectors + tuple(tuple(-x for x in vector) for vector in vectors)
        self.assertEqual(len(both_families), 48)
        self.assertEqual(len(set(both_families)), 24)
        ledgers = audit.build_evidence()["orientation_term_ledgers"]
        self.assertEqual(len(ledgers), 24)
        self.assertTrue(all(len(row["ordered_partition_terms"]) == 26 for row in ledgers))

    def test_zero_bracket_has_no_reweighting_margin(self):
        vector = audit.exact_grid_term_vector(audit.ZERO_WITNESS, 4)
        self.assertEqual(sum(vector), 0)
        nonzero = [i for i, value in enumerate(vector) if value]
        self.assertEqual(len(nonzero), 2)
        self.assertEqual([vector[i] for i in nonzero], [1, -1])
        for delta in (Q(1, 1000), -Q(1, 1000)):
            reweighted = vector[nonzero[0]] * (1 + delta) + vector[nonzero[1]]
            self.assertEqual(reweighted, delta)

    def test_supplied_abstract_positive_weight_countermodel(self):
        model = audit.abstract_countermodel()
        self.assertEqual(model["unweighted_bracket"], "-1/12")
        self.assertEqual(model["reweighted_bracket"], "1187/1200")
        self.assertEqual(model["classification"], "ABSTRACT_ONLY; not source-admissible WP84 evidence")

    def test_evidence_does_not_promote_aggregate_or_theorem(self):
        result = audit.build_evidence()
        self.assertEqual(result["decision"], "LEGAL_SOURCE_COUNTEREXAMPLE")
        self.assertIn("does not determine the complete signed sum", result["aggregate_gate"])
        self.assertEqual(result["theorem_claims"]["strict_gt_79_percent"], "OPEN")
        self.assertEqual(result["theorem_claims"]["unconditional_RH"], "OPEN")


if __name__ == "__main__":
    unittest.main()
