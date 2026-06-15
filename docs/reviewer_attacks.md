# Reviewer Attacks

## Attack: This Is Just Affordance Learning

Response: affordance learning predicts action possibilities.  EATL defines when
a robot may assert an embodied common-sense predicate.  A learned affordance
model can implement tests or priors, but it is not the same as a witness,
failure certificate, abstention, and validity scope.

## Attack: This Is Just Active Sensing

Response: active sensing chooses measurements.  EATL can use active sensing, but
the paper's main object is the semantic license for an assertion.  The v3 phase
diagram and selector ablation explicitly treat measurement selection as a
cost-aware policy problem.

## Attack: The Evaluation Is Synthetic

Response: correct.  The paper does not claim real-robot deployment.  The
synthetic environment isolates same-label hidden physical changes and makes the
failure mechanism inspectable.  The readiness decision remains strong-revise
for venues that require hardware.

## Attack: A Strong VLM Could Infer The Hidden Variable

Response: sometimes.  The visibility ladder shows that full noisy hidden-state
visibility solves the synthetic task.  EATL is most useful when the deciding
variable is hidden, stale, demand-specific, or too consequential to trust as a
category prior.

## Attack: Tests Can Be Dangerous

Response: agreed.  The cost-aware proposition and phase diagram make this a
central boundary.  EATL is not "always test"; it is "do not assert without
licensed evidence or explicit unsupported-risk status."

## Attack: Cached Tests Become Stale

Response: agreed.  The cache experiment shows label-only reuse has 0.270 unsafe
false positives, while strict validity reuse preserves accuracy and reduces
test cost.

## Attack: The Paper Is Too Long For A Simple Idea

Response: the length is now driven by real stress evidence: main benchmark,
phase diagram, ablations, cache validity, noise, visibility, demand/embodiment,
failure cases, and full appendix tables.  The extra pages document scope and
failure boundaries rather than padding.
