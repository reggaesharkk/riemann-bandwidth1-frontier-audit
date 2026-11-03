from fractions import Fraction
import unittest

from src.wp84_r400_endpoint_restricted_attack import (
    DELTA_MAX,
    DELTA_OVER_EIGHT,
    abstract_endpoint_countermodel,
    known_section_density_lower_bound,
    restricted_average_selects_section,
)


class EndpointRestrictedAttackTests(unittest.TestCase):
    def test_exact_budget_and_density(self):
        self.assertEqual(DELTA_OVER_EIGHT,
                         Fraction(3675673694911, 1186000000000000))
        self.assertEqual(known_section_density_lower_bound(Fraction(1, 8)),
                         Fraction(1, 8))

    def test_markov_intersection_bound_is_exact_union_bound(self):
        # Product of the two endpoint good densities is at least 1/4;
        # boundary-bad mass is at most epsilon in the full candidate measure.
        for epsilon in (Fraction(1, 16), Fraction(1, 8), Fraction(1, 5)):
            self.assertEqual(known_section_density_lower_bound(epsilon),
                             Fraction(1, 4) - epsilon)

    def test_finite_conditional_average_implies_a_common_section(self):
        self.assertTrue(restricted_average_selects_section(
            (Fraction(-9, 1), DELTA_MAX / 2, DELTA_MAX), DELTA_MAX))
        self.assertFalse(restricted_average_selects_section(
            (2 * DELTA_MAX, 2 * DELTA_MAX), DELTA_MAX))
        with self.assertRaises(ValueError):
            restricted_average_selects_section((), DELTA_MAX)

    def test_abstract_negative_control(self):
        model = abstract_endpoint_countermodel()
        self.assertEqual(model.admissible_count, 9)
        self.assertEqual(model.density, Fraction(9, 16))
        self.assertEqual(model.lower_score_mean, Fraction(3, 4))
        self.assertEqual(model.upper_score_mean, Fraction(3, 4))
        self.assertEqual(model.signed_mean, Fraction(0))
        self.assertEqual(model.global_positive_mean, Fraction(9, 8) * DELTA_MAX)
        self.assertEqual(model.admissible_positive_mean, 2 * DELTA_MAX)

    def test_positive_part_is_not_controlled_by_signed_mean(self):
        model = abstract_endpoint_countermodel()
        self.assertGreater(model.admissible_positive_mean, DELTA_MAX)
        self.assertGreater(model.global_positive_mean, DELTA_MAX)


if __name__ == "__main__":
    unittest.main()
