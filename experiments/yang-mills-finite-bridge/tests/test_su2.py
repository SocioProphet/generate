from math import pi

from ym_finite_bridge.su2 import (
    SU2Rep,
    character_inner_product,
    fusion_matrix,
    labels,
    tensor_product_labels,
)


def test_labels_and_rep_invariants():
    assert labels(4) == [0, 1, 2, 3, 4]
    rep = SU2Rep(3)
    assert rep.spin == 1.5
    assert rep.dimension == 4
    assert rep.casimir == 15 / 4


def test_su2_clebsch_gordan_support():
    assert tensor_product_labels(1, 1) == [0, 2]
    assert tensor_product_labels(2, 2) == [0, 2, 4]
    assert tensor_product_labels(1, 4) == [3, 5]


def test_character_product_identity_at_sample_angles():
    for a, b in [(1, 1), (1, 2), (2, 3), (4, 4)]:
        for theta in [0.17, 0.71, 1.23, 2.41]:
            lhs = SU2Rep(a).character(theta) * SU2Rep(b).character(theta)
            rhs = sum(SU2Rep(c).character(theta) for c in tensor_product_labels(a, b))
            assert abs(lhs - rhs) < 1e-9


def test_character_limits_at_identity_and_minus_identity():
    assert SU2Rep(4).character(0.0) == 5.0
    assert SU2Rep(4).character(pi) == 5.0
    assert SU2Rep(3).character(pi) == -4.0


def test_haar_character_orthogonality_fixture():
    for a in range(5):
        for b in range(5):
            expected = 1.0 if a == b else 0.0
            actual = character_inner_product(a, b, steps=3000)
            assert abs(actual - expected) < 2e-6


def test_truncated_fusion_matrix_for_fundamental_rep():
    matrix = fusion_matrix(4, by_two_j=1)
    # Multiplication by spin-1/2 maps label 0 -> label 1.
    assert matrix[1][0] == 1
    # Label 1 -> labels 0 and 2.
    assert matrix[0][1] == 1
    assert matrix[2][1] == 1
    # Label 4 would map to 3 and 5, but 5 is outside cutoff.
    assert matrix[3][4] == 1
    assert sum(row[4] for row in matrix) == 1
