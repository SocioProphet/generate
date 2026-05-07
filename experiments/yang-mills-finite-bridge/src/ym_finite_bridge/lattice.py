"""Finite lattice orientation fixtures for the Yang-Mills bridge.

This module defines graph-level objects only: vertices, oriented edges, paths,
and plaquettes. It does not attach group elements or make continuum claims.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

Vertex = Tuple[int, ...]


@dataclass(frozen=True, order=True)
class OrientedEdge:
    """Directed view of an undirected finite lattice edge."""

    source: Vertex
    target: Vertex

    def __post_init__(self) -> None:
        if self.source == self.target:
            raise ValueError("edge source and target must differ")

    @property
    def boundary(self) -> Tuple[Vertex, Vertex]:
        return (self.source, self.target)

    @property
    def canonical_key(self) -> Tuple[Vertex, Vertex]:
        return tuple(sorted((self.source, self.target)))  # type: ignore[return-value]

    def reversed(self) -> "OrientedEdge":
        return OrientedEdge(self.target, self.source)

    def to_dict(self) -> dict:
        return {"source": list(self.source), "target": list(self.target)}

    @staticmethod
    def from_dict(data: dict) -> "OrientedEdge":
        return OrientedEdge(tuple(data["source"]), tuple(data["target"]))


@dataclass(frozen=True)
class Path:
    """Sequence of oriented edges with adjacency validation."""

    edges: Tuple[OrientedEdge, ...]

    def __post_init__(self) -> None:
        if not self.edges:
            raise ValueError("path must contain at least one edge")
        for left, right in zip(self.edges, self.edges[1:]):
            if left.target != right.source:
                raise ValueError(
                    f"path adjacency failure: {left.target} does not match {right.source}"
                )

    @property
    def source(self) -> Vertex:
        return self.edges[0].source

    @property
    def target(self) -> Vertex:
        return self.edges[-1].target

    @property
    def is_closed(self) -> bool:
        return self.source == self.target

    @property
    def vertices(self) -> Tuple[Vertex, ...]:
        return (self.source,) + tuple(edge.target for edge in self.edges)

    def reversed(self) -> "Path":
        return Path(tuple(edge.reversed() for edge in reversed(self.edges)))

    def to_dict(self) -> dict:
        return {"edges": [edge.to_dict() for edge in self.edges]}

    @staticmethod
    def from_dict(data: dict) -> "Path":
        return Path(tuple(OrientedEdge.from_dict(edge) for edge in data["edges"]))


@dataclass(frozen=True)
class Plaquette:
    """Closed finite lattice face represented by an oriented boundary path."""

    boundary_path: Path

    def __post_init__(self) -> None:
        if not self.boundary_path.is_closed:
            raise ValueError("plaquette boundary must be closed")
        if len(self.boundary_path.edges) < 3:
            raise ValueError("plaquette boundary must have at least three edges")

    @property
    def vertices(self) -> Tuple[Vertex, ...]:
        return self.boundary_path.vertices[:-1]

    def reversed(self) -> "Plaquette":
        return Plaquette(self.boundary_path.reversed())

    def to_dict(self) -> dict:
        return {"boundary_path": self.boundary_path.to_dict()}

    @staticmethod
    def from_dict(data: dict) -> "Plaquette":
        return Plaquette(Path.from_dict(data["boundary_path"]))


class FiniteLattice:
    """Finite undirected lattice with oriented edge views."""

    def __init__(self, vertices: Iterable[Vertex], edges: Iterable[OrientedEdge]) -> None:
        self.vertices = frozenset(vertices)
        edge_list = tuple(edges)
        self._edges = frozenset(edge.canonical_key for edge in edge_list)
        missing = [vertex for edge in edge_list for vertex in edge.boundary if vertex not in self.vertices]
        if missing:
            raise ValueError(f"edge references vertices outside lattice: {missing}")

    @property
    def undirected_edges(self) -> frozenset[Tuple[Vertex, Vertex]]:
        return self._edges

    def has_edge(self, edge: OrientedEdge) -> bool:
        return edge.source in self.vertices and edge.target in self.vertices and edge.canonical_key in self._edges

    def require_edge(self, edge: OrientedEdge) -> OrientedEdge:
        if not self.has_edge(edge):
            raise ValueError(f"edge is not in lattice: {edge}")
        return edge

    def require_path(self, path: Path) -> Path:
        for edge in path.edges:
            self.require_edge(edge)
        return path

    def require_plaquette(self, plaquette: Plaquette) -> Plaquette:
        self.require_path(plaquette.boundary_path)
        return plaquette

    def to_dict(self) -> dict:
        return {
            "vertices": [list(vertex) for vertex in sorted(self.vertices)],
            "edges": [
                {"source": list(source), "target": list(target)}
                for source, target in sorted(self._edges)
            ],
        }

    @staticmethod
    def from_dict(data: dict) -> "FiniteLattice":
        vertices = [tuple(vertex) for vertex in data["vertices"]]
        edges = [OrientedEdge(tuple(edge["source"]), tuple(edge["target"])) for edge in data["edges"]]
        return FiniteLattice(vertices, edges)


def gauge_transform_signature(edge: OrientedEdge) -> str:
    """Return the symbolic gauge transformation shape for a link variable.

    Convention: U[source,target] -> g[source] U[source,target] g[target]^-1.
    This is only a shape fixture; no group operations are performed here.
    """
    return f"g{edge.source} U{edge.source}->{edge.target} g{edge.target}^-1"


def square_lattice() -> tuple[FiniteLattice, Plaquette]:
    """Return a minimal square lattice and its oriented plaquette fixture."""
    v00 = (0, 0)
    v10 = (1, 0)
    v11 = (1, 1)
    v01 = (0, 1)
    edges = (
        OrientedEdge(v00, v10),
        OrientedEdge(v10, v11),
        OrientedEdge(v11, v01),
        OrientedEdge(v01, v00),
    )
    lattice = FiniteLattice((v00, v10, v11, v01), edges)
    plaquette = Plaquette(Path(edges))
    return lattice, plaquette
