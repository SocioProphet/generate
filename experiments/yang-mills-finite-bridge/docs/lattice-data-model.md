# Finite Lattice Data Model

This slice adds graph-level lattice fixtures only. It does not attach SU(2) group elements to links and does not construct a lattice action.

## Objects

## Vertex

A vertex is a tuple of integers. Initial fixtures use two-dimensional coordinates such as `(0, 0)`.

Allowed claims: finite coordinate identity and graph adjacency.

Forbidden claims: manifold, continuum, or smooth geometric structure.

## OrientedEdge

An oriented edge is a directed view of an undirected lattice edge.

Fields:

- `source`;
- `target`.

Rules:

- source and target must differ;
- reversing twice returns the original oriented edge;
- opposite orientations share the same canonical undirected key.

Witness: `test_oriented_edge_reversal_and_canonical_key`.

Withoutness: canonical key equality between reversed orientations.

## Path

A path is a sequence of oriented edges with adjacency validation.

Rules:

- a path must contain at least one edge;
- each edge target must equal the next edge source;
- a path is closed when its source equals its target.

Witness: `test_path_adjacency_and_closed_loop`.

Withoutness: `test_invalid_path_adjacency_rejected`.

## Plaquette

A plaquette is a closed finite face represented by an oriented boundary path.

Rules:

- boundary path must be closed;
- boundary path must contain at least three edges;
- reversing a plaquette reverses its boundary orientation.

Witness: `test_plaquette_requires_closed_path`.

Withoutness: invalid open paths are rejected before any gauge-field interpretation is possible.

## FiniteLattice

A finite lattice is an undirected finite graph with oriented edge views.

Rules:

- all edge endpoints must be vertices in the lattice;
- either orientation of a known edge is valid;
- unknown edges are rejected;
- paths and plaquettes must use lattice edges.

Witness: `test_lattice_validates_edges_and_plaquettes`.

Withoutness: serialization round-trip checks that the finite object is not only an in-memory construction.

## Gauge transform signature

The symbolic gauge transformation shape for a link is:

```text
U[source,target] -> g[source] U[source,target] g[target]^-1
```

The implementation returns this shape as text only. It does not perform group multiplication.

Witness: `test_gauge_transform_signature_shape`.

Forbidden claims: no gauge invariance is proved yet; only the transformation signature is stabilized.

## Minimal fixture

`square_lattice()` returns one square plaquette with four vertices and four edges.

This fixture is intentionally small enough to support brute-force and alternate-implementation checks in later slices.

## Claim level

Level 1: finite fixture.

## Next required objects

- group-valued link assignment;
- vertex gauge transformation map;
- plaquette holonomy path;
- trivial-loop observable;
- small-lattice Wilson loop fixture.
