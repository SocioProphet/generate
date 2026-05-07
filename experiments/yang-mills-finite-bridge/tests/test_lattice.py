import pytest

from ym_finite_bridge.lattice import (
    FiniteLattice,
    OrientedEdge,
    Path,
    Plaquette,
    gauge_transform_signature,
    square_lattice,
)


def test_oriented_edge_reversal_and_canonical_key():
    edge = OrientedEdge((0, 0), (1, 0))
    reverse = edge.reversed()
    assert reverse.source == (1, 0)
    assert reverse.target == (0, 0)
    assert reverse.reversed() == edge
    assert reverse.canonical_key == edge.canonical_key


def test_path_adjacency_and_closed_loop():
    _, plaquette = square_lattice()
    path = plaquette.boundary_path
    assert path.source == (0, 0)
    assert path.target == (0, 0)
    assert path.is_closed
    assert path.reversed().is_closed


def test_invalid_path_adjacency_rejected():
    with pytest.raises(ValueError, match="adjacency"):
        Path((OrientedEdge((0, 0), (1, 0)), OrientedEdge((0, 1), (0, 0))))


def test_plaquette_requires_closed_path():
    open_path = Path((OrientedEdge((0, 0), (1, 0)), OrientedEdge((1, 0), (1, 1))))
    with pytest.raises(ValueError, match="closed"):
        Plaquette(open_path)


def test_lattice_validates_edges_and_plaquettes():
    lattice, plaquette = square_lattice()
    lattice.require_plaquette(plaquette)
    assert lattice.has_edge(OrientedEdge((1, 0), (0, 0)))
    with pytest.raises(ValueError, match="not in lattice"):
        lattice.require_edge(OrientedEdge((0, 0), (2, 0)))


def test_lattice_serialization_round_trip():
    lattice, plaquette = square_lattice()
    restored_lattice = FiniteLattice.from_dict(lattice.to_dict())
    restored_plaquette = Plaquette.from_dict(plaquette.to_dict())
    assert restored_lattice.undirected_edges == lattice.undirected_edges
    assert restored_plaquette.vertices == plaquette.vertices
    restored_lattice.require_plaquette(restored_plaquette)


def test_gauge_transform_signature_shape():
    edge = OrientedEdge((0, 0), (1, 0))
    assert gauge_transform_signature(edge) == "g(0, 0) U(0, 0)->(1, 0) g(1, 0)^-1"
    assert gauge_transform_signature(edge.reversed()) == "g(1, 0) U(1, 0)->(0, 0) g(0, 0)^-1"
