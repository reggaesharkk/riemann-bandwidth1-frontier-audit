import unittest
from fractions import Fraction

from src.wp84_r400_theorem_feasibility import DELTA_MAX, build_checks, diagonal_spike


class TheoremFeasibilityTests(unittest.TestCase):
    def test_exact_record_budget(self):
        self.assertEqual(DELTA_MAX, Fraction(3675673694911, 148250000000000))
        checks = build_checks()["record_budget"]
        self.assertEqual(checks["epsilon_one_eighth_positive_part_budget_exact"], "3675673694911/1186000000000000")
        self.assertTrue(checks["strict_inequality_required"])

    def test_second_mass_does_not_bound_fourth_moment(self):
        row = diagonal_spike(10)
        self.assertEqual(row["dimension"], 10**8)
        self.assertEqual(row["normalized_tau_Q2"], "1/100")
        self.assertEqual(row["normalized_tau_Q4"], "10000")

    def test_signed_mean_is_not_mean_positive_part(self):
        checks = build_checks()["signed_mean_vs_positive_part"]
        self.assertEqual(checks["mean_signed_exact"], "0")
        self.assertEqual(checks["mean_positive_part_exact"], "1/2")

    def test_major_arc_insertion_has_unpaid_H_loss(self):
        row = build_checks()["evans_direct_major_arc_insertion"]
        self.assertIn("T^(s-1)", row["asymptotic_form"])
        self.assertIn("diverges", row["conclusion"])

    def test_final_gate_is_open_not_a_prime_counterexample(self):
        decisions = build_checks()["decisions"]
        self.assertEqual(decisions["ORDINARY_CONNECTED_AGGREGATE"], "OPEN")
        self.assertEqual(decisions["NEXT_ACTION"], "NEW_ANALYTIC_THEOREM_REQUIRED")


if __name__ == "__main__":
    unittest.main()
