import itertools
import unittest
from fractions import Fraction as F

from src.wp84_physical_kernel_proper_power_reconciliation import (
    V,
    build_ledger,
    ordered_anchored_partitions,
    public_nested_overlap,
    rational_grid_term_vector,
    source_prefix_overlap,
)


class PhysicalKernelReconciliationTests(unittest.TestCase):
    def test_exact_public_and_physical_kernels(self):
        ledger = build_ledger()
        self.assertEqual(ledger["partition_counts"], {"1": 1, "2": 7, "3": 12, "4": 6})
        self.assertEqual(ledger["common_first_overlap_OA"], "2/5")
        self.assertEqual(ledger["public_geometric_B4"], "0")
        self.assertEqual(ledger["physical_kappa_m10"], "1")
        self.assertEqual(ledger["physical_term_vector_m10"], ["1"] + ["0"] * 25)

    def test_all_six_balanced_sign_orthants_and_labeled_orientations(self):
        signs = set()
        source_labeled = list(itertools.permutations(V))
        conjugate_labeled = [tuple(-x for x in point) for point in source_labeled]
        labeled = source_labeled + conjugate_labeled
        self.assertEqual(len(source_labeled), 24)
        self.assertEqual(len(labeled), 48)
        for point in labeled:
            signs.add(tuple(i for i, x in enumerate(point) if x > 0))
            self.assertEqual(sum(point), 0)
            self.assertEqual(sum(1 for x in point if x > 0), 2)
            self.assertEqual(rational_grid_term_vector(point, 10)[0], 1)
            self.assertEqual(sum(rational_grid_term_vector(point, 10)), 1)
        self.assertEqual(len(signs), 6)
        # Conjugation supplies the other 24 labeled source entries; duplicate
        # magnitudes explain why the two families have 24 unique points total.
        self.assertEqual(len(set(labeled)), 24)
        self.assertEqual(1 - 7 * F(2, 10) ** 2 - 12 * F(2, 10) ** 3 - 6 * F(2, 10) ** 4, F(384, 625))

    def test_zero_margin_and_positive_weight_abstract_counterexample(self):
        ledger = build_ledger()
        self.assertEqual(
            ledger["zero_margin_diagnostic"]["nonzero_term_vector_entries_one_based"],
            [[1, 1], [8, -1]],
        )
        self.assertEqual(ledger["zero_margin_diagnostic"]["unweighted_bracket"], "0")
        self.assertEqual(ledger["abstract_positive_weight_counterexample"]["unweighted_public_bracket"], "-1/12")
        self.assertEqual(ledger["abstract_positive_weight_counterexample"]["positively_reweighted_bracket"], "1187/1200")

    def test_source_atom_mass_classification_and_consumer_scope(self):
        ledger = build_ledger()
        entry = ledger["proper_power_ledger_entry"]
        self.assertEqual(entry["prime_exponents"], [1, 2, 3, 2])
        self.assertEqual(entry["signed_exponent_sum"], 0)
        self.assertEqual(entry["family_aggregate_bound"], "O_R(L^-4); this controls this complete one-base resonance family only")
        self.assertEqual(ledger["global_proper_power_sector"]["uniform_bound"], "<=64/(|a_phi|^2 L^2) <=256/L^2 once |a_phi|>=1/2")
        self.assertIn("not bounded here", ledger["r400_consumer"]["status"])
        self.assertEqual(ledger["decision"], "PROPER_POWER_EXCEPTION_CONTROLLED")

    def test_public_prefix_overlap(self):
        oa, prefix = source_prefix_overlap()
        self.assertEqual(oa, F(2, 5))
        self.assertEqual(prefix, (F(0), F(1, 5), F(-1, 5), F(2, 5), F(0)))
        self.assertEqual(sum(public_nested_overlap(blocks) * sign for sign, blocks in ordered_anchored_partitions()), 0)


if __name__ == "__main__":
    unittest.main()
