# Roadmap

## Slice 0: repository seed

Status: started.

Deliverables:

- bounded README;
- object catalog;
- proof discipline;
- SU(2) finite fixtures;
- tests.

Exit condition: tests pass and PR states that no continuum claim is made.

## Slice 1: finite lattice data model

Deliverables:

- finite lattice object;
- oriented edge convention;
- plaquette convention;
- boundary-state convention;
- serialization fixtures.

Validation:

- orientation reversal tests;
- closed-loop validation;
- invalid-path rejection;
- gauge-transformation shape checks.

## Slice 2: plaquette action separation

Deliverables:

- heat-kernel action lane;
- Wilson-action lane;
- explicit normalization metadata;
- coefficient comparison fixtures.

Validation:

- positivity where expected;
- character coefficient sanity checks;
- small-coupling and large-coupling diagnostics clearly marked as numerical, not proof.

## Slice 3: Wilson loop fixtures

Deliverables:

- loop path object;
- trace convention;
- trivial-loop fixtures;
- small lattice exact cases.

Validation:

- gauge invariance under vertex transformations;
- orientation behavior;
- representation normalization tests.

## Slice 4: transfer operator prototype

Deliverables:

- finite basis construction;
- transfer matrix assembly;
- self-adjointness or adjointness checks where applicable;
- positivity checks;
- cutoff boundary report.

Validation:

- exact small case;
- numerical finite spectrum;
- independent assembly path.

## Slice 5: finite spectral-gap proxies

Deliverables:

- finite spectral-gap computation;
- artifact manifest;
- cutoff sweep;
- strict warning labels.

Validation:

- small exact case;
- convergence diagnostics;
- no continuum language in result names.

## Slice 6: theorem-candidate lane

Deliverables:

- finite theorem statements;
- proof sketches;
- formalizable assumptions;
- adversarial review checklist.

Validation:

- proof-notebook to test parity;
- independent reviewer pass;
- claim-level register.

## Open risks

- Cutoff artifacts can masquerade as structure.
- Floating-point fixtures can hide convention bugs.
- Tensor-product support is easy to implement correctly for SU(2) and much harder in broader scope.
- Transfer positivity must be handled with care; finite positive-looking matrices are not enough.
- The continuum problem remains untouched until a separate limiting argument exists.
