#!/usr/bin/env python3
"""Exact arithmetic checks for the endpoint-restricted WP84 audit.

This module checks finite logical implications and an abstract negative
control.  It contains no prime-source simulation and proves no asymptotic
ordinary-prime estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


DELTA_MAX = Fraction(3675673694911, 148250000000000)
EPSILON_ROUTE = Fraction(1, 8)
DELTA_OVER_EIGHT = DELTA_MAX / 8


def known_section_density_lower_bound(epsilon: Fraction) -> Fraction:
    """Markov/union lower bound for the known direct-consumer set."""
    epsilon = Fraction(epsilon)
    if not 0 < epsilon < Fraction(1, 4):
        raise ValueError("epsilon must lie strictly between 0 and 1/4")
    return Fraction(1, 4) - epsilon


def restricted_average_selects_section(values: tuple[Fraction, ...],
                                       threshold: Fraction) -> bool:
    """Whether a nonempty finite family has mean positive part < threshold.

    The conclusion is existential: at least one value is strictly below the
    threshold.  Inputs are the real connected contributions in this toy
    logical check; callers must supply a *complete* admissible section set.
    """
    if not values:
        raise ValueError("the section family must be nonempty")
    threshold = Fraction(threshold)
    positive_parts = tuple(max(value, Fraction(0)) for value in values)
    mean = sum(positive_parts, Fraction(0)) / len(positive_parts)
    return mean < threshold and min(positive_parts) < threshold


@dataclass(frozen=True)
class AbstractEndpointCountermodel:
    grid_size: int
    admissible_count: int
    density: Fraction
    lower_score_mean: Fraction
    upper_score_mean: Fraction
    signed_mean: Fraction
    global_positive_mean: Fraction
    admissible_positive_mean: Fraction


def abstract_endpoint_countermodel() -> AbstractEndpointCountermodel:
    """Exact 4x4 control showing marginal endpoint bounds do not control C+."""
    # Three of four endpoints are good at each side.  Each bad endpoint has
    # score 3B and threshold 2B; take B=1.  Boundary energy is identically 0.
    scores = (Fraction(0), Fraction(0), Fraction(0), Fraction(3))
    threshold = Fraction(2)
    good = tuple(index for index, score in enumerate(scores) if score <= threshold)
    cells = tuple((u, v) for u in range(4) for v in range(4))
    admissible = tuple((u, v) for u, v in cells if u in good and v in good)

    # Correlation is deliberately assigned after defining G.  This is an
    # abstract probability-space countermodel, not a legal prime source.
    contribution = {
        cell: (2 * DELTA_MAX if cell in admissible
               else -Fraction(18, 7) * DELTA_MAX)
        for cell in cells
    }
    signed_mean = sum(contribution.values(), Fraction(0)) / len(cells)
    positive_mean = sum((max(x, Fraction(0)) for x in contribution.values()),
                        Fraction(0)) / len(cells)
    admissible_positive_mean = sum(
        (max(contribution[cell], Fraction(0)) for cell in admissible),
        Fraction(0),
    ) / len(admissible)
    return AbstractEndpointCountermodel(
        grid_size=len(cells),
        admissible_count=len(admissible),
        density=Fraction(len(admissible), len(cells)),
        lower_score_mean=sum(scores, Fraction(0)) / 4,
        upper_score_mean=sum(scores, Fraction(0)) / 4,
        signed_mean=signed_mean,
        global_positive_mean=positive_mean,
        admissible_positive_mean=admissible_positive_mean,
    )


def exact_summary() -> dict[str, str]:
    model = abstract_endpoint_countermodel()
    return {
        "delta_max": str(DELTA_MAX),
        "delta_max_decimal_15dp": f"{float(DELTA_MAX):.15f}",
        "delta_max_over_8": str(DELTA_OVER_EIGHT),
        "delta_max_over_8_decimal_15dp": f"{float(DELTA_OVER_EIGHT):.15f}",
        "known_density_epsilon_1_over_8": str(known_section_density_lower_bound(EPSILON_ROUTE)),
        "abstract_admissible_density": str(model.density),
        "abstract_endpoint_score_means": str(model.lower_score_mean),
        "abstract_signed_mean": str(model.signed_mean),
        "abstract_global_positive_mean_over_delta": str(model.global_positive_mean / DELTA_MAX),
        "abstract_admissible_positive_mean_over_delta": str(model.admissible_positive_mean / DELTA_MAX),
    }


if __name__ == "__main__":
    for key, value in exact_summary().items():
        print(f"{key}={value}")
