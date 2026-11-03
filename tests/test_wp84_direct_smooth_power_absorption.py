import unittest
from fractions import Fraction

from src.wp84_direct_smooth_power_absorption import (
    PROPER_POWER_SQUARE_MASS_CONSTANT,
    branch_phase_exponents,
    circle_distance,
    flat_source_step_overlap_upper_bound,
    full_second_trace_constant,
    hard_band_operator_norm_constant,
    hard_band_second_trace_constant,
    normalized_large_sieve_factor,
    operator_norm_constant,
    smoothstep_overlap_ratio,
    source_entry_scalar_identity,
    zero_extension_overlap_length,
)


class DirectSmoothPowerAbsorptionTests(unittest.TestCase):
    def test_source_smooth_entry_normalization(self):
        source, compressed_shift = source_entry_scalar_identity()
        self.assertEqual(source, compressed_shift)

    def test_smooth_taper_is_not_sharp_box_overlap(self):
        ratio = smoothstep_overlap_ratio(Fraction(1, 10))
        self.assertGreater(ratio, 0)
        self.assertLess(ratio, Fraction(1, 100000))
        # A genuine C-infinity step allowed by the source gives a certified
        # smooth/sharp overlap ratio <= 10^-6 near the endpoint ramp.
        self.assertEqual(flat_source_step_overlap_upper_bound(), Fraction(1, 1_000_000))

    def test_full_cutoff_circular_spacing_including_endpoint_alias(self):
        # X=16: n=16 is the exact modulo-one endpoint; powers 4 and 8
        # give rational frequencies 1/2 and 3/4. No n=1 source point occurs.
        values = [Fraction(1, 2), Fraction(3, 4), Fraction(0)]
        circle_dists = [circle_distance(x, y)
                        for i, x in enumerate(values)
                        for y in values[i + 1:]]
        # log(16)<16, so 1/((16+1)log(16)) > 1/272.
        self.assertEqual(min(circle_dists), Fraction(1, 4))
        self.assertGreaterEqual(min(circle_dists), Fraction(1, 272))

    def test_start_row_changes_only_unit_phases_and_branches_stay_distinct(self):
        u = Fraction(7, 13)
        p0, n0 = branch_phase_exponents(0, 3, u)
        p37, n37 = branch_phase_exponents(37, 3, u)
        self.assertEqual(p37 - p0, 37 * u)
        self.assertEqual(n37 - n0, -37 * u)
        self.assertEqual(n0, -p0)

    def test_boundary_compression_has_no_circular_wrap(self):
        self.assertEqual(zero_extension_overlap_length(10.0, 10.0), 0.0)
        self.assertEqual(zero_extension_overlap_length(10.0, 9.5), 0.5)

    def test_all_diagonal_second_trace_factor_is_paid(self):
        # The full matrix proof sums every integer displacement through
        # Parseval; the MV and two-branch factors are explicit here.
        self.assertEqual(normalized_large_sieve_factor(0.5), 5.0)
        self.assertEqual(full_second_trace_constant(0.5, 0.5), 2560.0)
        self.assertEqual(hard_band_second_trace_constant(400, 0.5), 1_025_280.0)
        self.assertGreater(hard_band_operator_norm_constant(400), 19000.0)

    def test_prime_power_coefficient_square_mass_constant(self):
        # 16 from log(p)^2 <= 16 p^(1/2), 2 from p(p-1)>=p^2/2,
        # and 2 from sum_{n>=2} n^(-3/2) <= 2.
        self.assertEqual(PROPER_POWER_SQUARE_MASS_CONSTANT, 16 * 2 * 2)

    def test_operator_norm_constant_uses_source_absolute_mass(self):
        value = operator_norm_constant(0.5)
        self.assertGreater(value, 56.7)
        self.assertLess(value, 56.9)


if __name__ == "__main__":
    unittest.main()
