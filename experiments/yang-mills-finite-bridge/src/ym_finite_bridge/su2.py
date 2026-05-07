"""Finite SU(2) character and cutoff utilities for the Yang-Mills bridge.

The module intentionally stays inside finite representation cutoffs. It is a
fixture and transfer-operator workbench, not a continuum Yang-Mills proof.

Convention: irreducible representations are indexed by ``two_j = 2j`` so that
all labels are non-negative integers. The dimension is ``two_j + 1`` and the
quadratic Casimir is ``j(j+1) = two_j * (two_j + 2) / 4``.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, isclose, pi, sin
from typing import Callable, Dict, List, Mapping


@dataclass(frozen=True, order=True)
class SU2Rep:
    """SU(2) irreducible representation indexed by doubled spin."""

    two_j: int

    def __post_init__(self) -> None:
        if not isinstance(self.two_j, int):
            raise TypeError("two_j must be an integer")
        if self.two_j < 0:
            raise ValueError("two_j must be non-negative")

    @property
    def spin(self) -> float:
        return self.two_j / 2.0

    @property
    def dimension(self) -> int:
        return self.two_j + 1

    @property
    def casimir(self) -> float:
        return self.two_j * (self.two_j + 2) / 4.0

    def character(self, theta: float, *, tol: float = 1e-12) -> float:
        """Return the SU(2) character at conjugacy angle ``theta``.

        For eigenvalues exp(±i theta), χ_j(theta)=sin((2j+1)theta)/sin(theta).
        The removable singularities at 0 and π are handled by limiting values.
        """
        s = sin(theta)
        if abs(s) <= tol:
            k = round(theta / pi)
            sign = -1 if (k % 2 and self.two_j % 2) else 1
            return float(sign * self.dimension)
        return sin(self.dimension * theta) / s


def labels(cutoff_two_j: int) -> List[int]:
    """Return finite SU(2) representation labels 0..cutoff_two_j."""
    if not isinstance(cutoff_two_j, int):
        raise TypeError("cutoff_two_j must be an integer")
    if cutoff_two_j < 0:
        raise ValueError("cutoff_two_j must be non-negative")
    return list(range(cutoff_two_j + 1))


def tensor_product_labels(two_j_a: int, two_j_b: int) -> List[int]:
    """Clebsch-Gordan support for SU(2) labels.

    Spin j_a tensor spin j_b decomposes into labels
    |two_j_a-two_j_b|, |two_j_a-two_j_b|+2, ..., two_j_a+two_j_b.
    Multiplicities are all one.
    """
    SU2Rep(two_j_a)
    SU2Rep(two_j_b)
    low = abs(two_j_a - two_j_b)
    high = two_j_a + two_j_b
    return list(range(low, high + 1, 2))


def tensor_product_coefficients(two_j_a: int, two_j_b: int) -> Dict[int, int]:
    """Return multiplicities in the SU(2) tensor-product support."""
    return {label: 1 for label in tensor_product_labels(two_j_a, two_j_b)}


def heat_kernel_coefficients(cutoff_two_j: int, t: float) -> Dict[int, float]:
    """Return truncated SU(2) heat-kernel expansion coefficients.

    K_t(theta) = Σ_j dim(j) exp(-t C2(j)) χ_j(theta), truncated by label.
    Requires t > 0 for a smoothing heat kernel fixture.
    """
    if t <= 0:
        raise ValueError("t must be positive")
    return {
        two_j: SU2Rep(two_j).dimension * exp(-t * SU2Rep(two_j).casimir)
        for two_j in labels(cutoff_two_j)
    }


def evaluate_character_series(coefficients: Mapping[int, float], theta: float) -> float:
    """Evaluate Σ coeff[two_j] χ_two_j(theta)."""
    return sum(coeff * SU2Rep(two_j).character(theta) for two_j, coeff in coefficients.items())


def haar_integral_class_function(fn: Callable[[float], float], *, steps: int = 4000) -> float:
    """Midpoint integral over SU(2) class functions.

    Haar class measure is (2/pi) sin(theta)^2 dtheta on [0, pi]. The midpoint
    rule is deterministic and dependency-free; use this only for fixtures, not
    as production numerical analysis.
    """
    if steps <= 0:
        raise ValueError("steps must be positive")
    width = pi / steps
    acc = 0.0
    for k in range(steps):
        theta = (k + 0.5) * width
        acc += fn(theta) * (2.0 / pi) * sin(theta) ** 2 * width
    return acc


def character_inner_product(two_j_a: int, two_j_b: int, *, steps: int = 4000) -> float:
    """Numerical Haar inner product <χ_a, χ_b>."""
    rep_a = SU2Rep(two_j_a)
    rep_b = SU2Rep(two_j_b)
    return haar_integral_class_function(
        lambda theta: rep_a.character(theta) * rep_b.character(theta), steps=steps
    )


def fusion_matrix(cutoff_two_j: int, by_two_j: int) -> List[List[int]]:
    """Return a truncated fusion matrix for multiplication by a representation.

    Rows are output labels, columns are input labels. Entries outside the cutoff
    are dropped; this is a cutoff artifact and must be treated as such.
    """
    SU2Rep(by_two_j)
    labs = labels(cutoff_two_j)
    index = {label: i for i, label in enumerate(labs)}
    matrix = [[0 for _ in labs] for _ in labs]
    for col, input_label in enumerate(labs):
        for output_label in tensor_product_labels(by_two_j, input_label):
            if output_label in index:
                matrix[index[output_label]][col] += 1
    return matrix


def assert_close(actual: float, expected: float, *, tol: float = 1e-9) -> None:
    """Small assertion helper used by examples and tests."""
    if not isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"expected {expected}, got {actual}")
