# Finite Yang-Mills Bridge Experiment

This experiment starts a bounded Yang-Mills research lane inside `SocioProphet/generate` because this repository already frames proof search, constraint assembly, sheaf-like gluing, and graph generation as one family of problems. The long-term target can still become a dedicated repository. The current seed is deliberately narrow: finite SU(2) representation fixtures, character identities, finite lattice orientation objects, cutoff discipline, and transfer-operator preparation.

This is not a proof of Yang-Mills existence or the mass gap. It is a finite-cutoff workbench for building verified objects that could later support a serious proof program.

## Program A boundary

Allowed claims:

- finite-volume and finite-cutoff identities;
- SU(2) representation-label fixtures;
- Clebsch-Gordan support checks;
- character-product identities;
- Haar-class orthogonality fixtures;
- finite lattice vertex, edge, path, and plaquette orientation fixtures;
- symbolic gauge-transformation shape fixtures;
- truncated fusion and transfer-operator scaffolding.

Forbidden claims without separate proof:

- continuum Yang-Mills existence;
- Clay mass-gap resolution;
- numerical gap evidence presented as proof;
- continuum extrapolation without a limiting theorem;
- gauge invariance proofs before group-valued links and vertex transforms are implemented.

## Operating discipline

The working pattern is dictionary-first. Every object must have a stable name, a definition, formulas, allowed claims, forbidden claims, fixtures, failure modes, and cross-references.

The validation pattern is triangulation. A claim is accepted only when we have at least three views: symbolic identity, numerical fixture, and symmetry or invariance check.

The proof architecture is tensegrity. Local calculations are compression members; global invariants are tension members. Local computations do not stand unless suspended inside the invariant network.

The acceptance pattern is witness and withoutness. Each result needs an internal witness plus an independent check from a limiting case, alternate implementation, known identity, brute-force enumeration, or symmetry orbit.

## Layout

```text
experiments/yang-mills-finite-bridge/
  docs/
    catalog-of-objects.md
    lattice-data-model.md
    proof-discipline.md
    roadmap.md
  src/ym_finite_bridge/
    __init__.py
    lattice.py
    su2.py
  tests/
    test_lattice.py
    test_su2.py
  pyproject.toml
```

## Run

From this directory:

```bash
python -m pytest -q
```

The tests are intentionally small and dependency-light. They prove only that the finite fixtures behave as expected.

## First mathematical object set

The first object set is SU(2) by doubled spin label `two_j = 2j`.

- dimension: `two_j + 1`;
- quadratic Casimir: `two_j * (two_j + 2) / 4`;
- character: `sin((two_j + 1) theta) / sin(theta)`;
- tensor-product support: `|a-b|, |a-b|+2, ..., a+b`.

This gives us deterministic, checkable pieces before any lattice action, transfer matrix, or continuum-limit language is introduced.

## Second mathematical object set

The second object set is the finite lattice orientation layer.

- vertex: tuple of integers;
- oriented edge: directed view of an undirected edge;
- path: adjacency-validated sequence of oriented edges;
- plaquette: closed finite boundary path;
- finite lattice: undirected finite graph with oriented edge views;
- symbolic gauge transform signature: `U[source,target] -> g[source] U[source,target] g[target]^-1`.

This gives us edge orientation, closed-loop, serialization, and rejection fixtures before any group-valued link variables are attached.
