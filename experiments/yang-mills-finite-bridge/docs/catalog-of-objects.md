# Catalog of Objects

This catalog is the control surface for the finite Yang-Mills bridge. Each term is a mathematical object with scope boundaries. The catalog prevents semantic drift and blocks accidental promotion from finite fixture to continuum theorem.

## Template

```text
Term:
Mathematical object:
Definition:
Formula:
Allowed claims:
Forbidden claims:
Fixtures:
Failure modes:
Cross-references:
```

## GaugeGroup

Mathematical object: compact Lie group used for finite lattice gauge calculations.

Definition: the symmetry group whose elements decorate finite lattice links and whose irreducible representations index character expansions.

Initial scope: SU(2).

Allowed claims: finite representation and character identities for SU(2).

Forbidden claims: no continuum existence claim follows from finite group computations alone.

Fixtures: representation dimension, Casimir, character, tensor-product support.

Failure modes: conflating SU(2) fixtures with general compact semisimple group statements; forgetting normalization conventions.

Cross-references: `RepresentationLabel`, `Character`, `HeatKernelCoefficient`.

## RepresentationLabel

Mathematical object: non-negative integer `two_j = 2j` indexing an SU(2) irreducible representation.

Definition: doubled spin label that avoids half-integer storage and keeps tensor-product parity explicit.

Formula: dimension `d_j = two_j + 1`; Casimir `C2 = two_j * (two_j + 2) / 4`.

Allowed claims: finite-dimensional representation bookkeeping.

Forbidden claims: physical particle labels or continuum state labels without additional construction.

Fixtures: label range, dimension, Casimir, tensor-product support.

Failure modes: off-by-one dimension errors; mixing `j` and `2j`; parity mismatch.

Cross-references: `RepresentationCutoff`, `Character`, `FusionMatrix`.

## RepresentationCutoff

Mathematical object: finite truncation of representation labels.

Definition: an integer `Jmax2` defining the finite label set `{0, 1, ..., Jmax2}`.

Allowed claims: finite computations and convergence experiments.

Forbidden claims: exact continuum result unless a limiting theorem is supplied.

Fixtures: cutoff label enumeration; boundary-loss tests in truncated fusion.

Failure modes: treating cutoff artifacts as physics; failing to record discarded labels.

Cross-references: `FusionMatrix`, `TransferOperator`.

## Character

Mathematical object: trace of an SU(2) representation evaluated on a conjugacy class.

Definition: for class angle `theta`, `chi_two_j(theta) = sin((two_j + 1) theta) / sin(theta)` with removable singularities at `0` and `pi`.

Allowed claims: character identity and orthogonality fixtures.

Forbidden claims: numerical evaluation near singularities without limit handling.

Fixtures: identity limit equals dimension; minus-identity sign; Haar orthogonality.

Failure modes: unstable division near `sin(theta)=0`; wrong Haar measure.

Cross-references: `HaarClassMeasure`, `TensorProductSupport`.

## TensorProductSupport

Mathematical object: Clebsch-Gordan support for product of SU(2) irreducible representations.

Definition: labels appearing in tensor product of labels `a` and `b`.

Formula: `|a-b|, |a-b|+2, ..., a+b`.

Allowed claims: support and multiplicity-one decomposition for SU(2).

Forbidden claims: general compact-group tensor decomposition.

Fixtures: `1 x 1 -> 0 + 2`; `2 x 2 -> 0 + 2 + 4`; product-of-characters identity.

Failure modes: parity mistakes; boundary truncation hidden by cutoff.

Cross-references: `FusionMatrix`, `Character`.

## HaarClassMeasure

Mathematical object: class-function Haar measure for SU(2).

Definition: `(2/pi) sin(theta)^2 dtheta` on `[0, pi]`.

Allowed claims: numerical fixture integration for class functions.

Forbidden claims: production-grade quadrature or proof by floating-point integration.

Fixtures: character orthogonality.

Failure modes: using flat measure; insufficient integration resolution; endpoint instability.

Cross-references: `Character`, `Witness`.

## HeatKernelCoefficient

Mathematical object: finite coefficient in the SU(2) heat-kernel character expansion.

Definition: coefficient for label `two_j` at heat time `t`.

Formula: `dimension(two_j) * exp(-t * Casimir(two_j))`.

Allowed claims: finite smooth class-function approximation.

Forbidden claims: continuum Yang-Mills measure construction.

Fixtures: positivity for `t > 0`; monotone damping with Casimir.

Failure modes: using `t <= 0`; confusing heat time with lattice coupling without convention.

Cross-references: `PlaquetteWeight`, `TransferOperator`.

## PlaquetteWeight

Mathematical object: finite lattice action factor attached to a plaquette.

Definition: class function on the gauge group used as a local Boltzmann weight.

Initial implementation: deferred until heat-kernel and Wilson-action conventions are explicitly separated.

Allowed claims: finite class-function evaluation.

Forbidden claims: continuum action limit without renormalization statement.

Fixtures: positivity, normalization convention, character coefficient comparison.

Failure modes: mixing Wilson and heat-kernel actions; unrecorded normalization choices.

Cross-references: `HeatKernelCoefficient`, `TransferOperator`.

## WilsonLoop

Mathematical object: gauge-invariant trace around a closed lattice loop.

Definition: product of link variables around a closed path, traced in a representation.

Initial implementation: deferred until lattice path and orientation conventions are introduced.

Allowed claims: finite loop observable construction.

Forbidden claims: area-law or mass-gap conclusion without proof.

Fixtures: orientation reversal in SU(2), trivial loop value, small-lattice exact cases.

Failure modes: non-closed path; gauge-variant implementation; representation normalization drift.

Cross-references: `GaugeInvariance`, `Witness`.

## TransferOperator

Mathematical object: finite operator encoding propagation between boundary states.

Definition: cutoff-dependent matrix or linear map generated from finite lattice slices.

Allowed claims: finite spectral data and consistency checks.

Forbidden claims: physical mass gap without continuum construction.

Fixtures: self-adjointness where applicable; positivity; finite spectrum; cutoff boundary report.

Failure modes: non-positive operator from broken convention; treating finite gap as continuum gap.

Cross-references: `FiniteSpectralGap`, `RepresentationCutoff`.

## FiniteSpectralGap

Mathematical object: separation between the leading spectral level and the next level of a finite transfer operator.

Definition: finite matrix spectral proxy used as a diagnostic.

Allowed claims: finite numerical or exact eigenvalue separation.

Forbidden claims: Clay mass gap or continuum mass gap.

Fixtures: exact small matrices; perturbation checks; monotonicity experiments when justified.

Failure modes: discretization artifact; cutoff artifact; normalization mismatch.

Cross-references: `TransferOperator`, `ContinuumClaim`.

## ContinuumClaim

Mathematical object: theorem-level statement about limiting Yang-Mills theory.

Definition: any statement that survives infinite volume, continuum limit, and required renormalization controls.

Allowed claims: none in this experiment until proved separately.

Forbidden claims: all unproved continuum existence or mass-gap statements.

Fixtures: not applicable yet.

Failure modes: upgrading finite data into theorem language.

Cross-references: all objects.

## Witness

Mathematical object: internal derivation, fixture, or certificate supporting a claim.

Definition: explicit evidence generated inside the repository.

Allowed claims: the claim is internally supported to the stated level.

Forbidden claims: independent confirmation.

Fixtures: tests, generated manifests, exact derivations.

Failure modes: unstated assumptions; stale generated artifact.

Cross-references: `Withoutness`, `Triangulation`.

## Withoutness

Mathematical object: independent external check.

Definition: an alternate implementation, limiting case, known identity, brute-force enumeration, or symmetry orbit check.

Allowed claims: independent confirmation of a finite result.

Forbidden claims: proof of a stronger theorem than the check supports.

Fixtures: character orthogonality; tensor-product identity; U(1) null-control later.

Failure modes: not actually independent; same bug replicated in both checks.

Cross-references: `Witness`, `Triangulation`.

## Triangulation

Mathematical object: three-way validation discipline.

Definition: a result must pass symbolic, numerical, and symmetry/invariance tests.

Allowed claims: result has passed the finite acceptance gate.

Forbidden claims: final proof.

Fixtures: identity + numerical integration + symmetry orbit.

Failure modes: accepting one successful computation.

Cross-references: `Tensegrity`, `Witness`, `Withoutness`.

## Tensegrity

Mathematical object: proof architecture where local computations are constrained by global invariants.

Definition: local compression members include coefficients and finite matrices; global tension members include gauge invariance, positivity, transfer consistency, and symmetry.

Allowed claims: a finite result is structurally supported by multiple constraints.

Forbidden claims: a local computation is valid without global checks.

Fixtures: invariant-check matrix around each result.

Failure modes: local numerical success floating free from proof constraints.

Cross-references: all objects.
