# Proof Discipline

The finite Yang-Mills bridge uses four controls: dictionary, triangulation, tensegrity, and witness/withoutness.

## 1. Dictionary control

Every term must be stable enough to test. If a term cannot be turned into a catalog entry, it is not yet allowed in theorem prose.

Required fields:

- definition;
- formula;
- allowed claims;
- forbidden claims;
- fixtures;
- failure modes;
- cross-references.

This prevents a finite computation from silently acquiring continuum meaning.

## 2. Triangulation control

Every accepted result needs three views:

1. symbolic or exact derivation;
2. numerical fixture;
3. symmetry, invariance, or independent implementation check.

For the initial SU(2) lane, the basic triangulation examples are:

- character product identity;
- Haar orthogonality numerical fixture;
- Clebsch-Gordan parity and endpoint checks.

## 3. Tensegrity control

Local compression members:

- representation labels;
- dimensions;
- Casimirs;
- character coefficients;
- plaquette factors;
- finite basis vectors;
- transfer-matrix entries.

Global tension members:

- gauge invariance;
- reflection or transfer positivity where applicable;
- symmetry orbit consistency;
- adjointness or self-adjointness checks;
- reproducible artifact manifests;
- cutoff-boundary accounting.

A result is accepted only when the local compression members are held by the global tension constraints.

## 4. Witness and withoutness

A witness is internal support: a derivation, fixture, proof sketch, test, generated manifest, or exact enumeration.

Withoutness is an independent check: a known identity, alternate implementation, limiting case, U(1) control, brute-force enumeration, or symmetry orbit.

No result enters the theorem namespace without both.

## 5. Claim levels

### Level 0: note

Unstructured observation or research note. Not accepted as a claim.

### Level 1: finite fixture

A finite identity or computation with tests. Allowed in this experiment.

### Level 2: finite theorem candidate

A general finite statement with proof sketch, tests, and independent checks.

### Level 3: limiting theorem candidate

A statement about convergence or uniform control across cutoffs. Requires a separate proof document and adversarial review.

### Level 4: continuum theorem

A continuum Yang-Mills statement. Not currently claimed.

### Level 5: mass-gap theorem

A Clay-level result. Explicitly forbidden in this repository unless independently proved and reviewed.

## 6. Immediate acceptance gate

A pull request touching this experiment must answer:

- What object did we define?
- What claim level is it?
- What is the witness?
- What is the withoutness check?
- What does it explicitly not prove?
- What validation command was run?

## 7. First slice completion criteria

The first slice is complete when:

- SU(2) representation labels are implemented;
- dimensions and Casimirs are tested;
- characters are evaluated with endpoint limits;
- tensor-product supports are tested;
- character product identity is tested;
- Haar orthogonality is tested;
- cutoff boundary behavior is exposed in fusion matrices;
- no continuum claims are present.
