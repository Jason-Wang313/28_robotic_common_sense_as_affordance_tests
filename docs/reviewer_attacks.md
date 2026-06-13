# Reviewer Attacks

## Attack 1: This is just affordance learning.
Response: affordance learning predicts labels or effects. EATL defines the
truth condition of a commonsense predicate by an executable micro-experiment and
requires a witness for the current robot-object-demand tuple.

## Attack 2: This is just a verifier.
Response: a verifier usually checks a proposed plan state or rescores a model
output. EATL is pre-action predicate semantics: the robot obtains physical
evidence before the dangerous task action, and failure certificates are first
class outputs.

## Attack 3: This is active sensing with a new name.
Response: active sensing chooses measurements to reduce uncertainty. EATL can
use active sensing, but the contribution is the operational definition of
common-sense predicates and the lower-bound argument against label-only priors.

## Attack 4: The experiments are synthetic.
Response: correct. The evidence is an executable stress test that isolates the
assumption break. The claim should be revised before main-conference submission
unless a real robot or high-fidelity simulator evaluation is added.

## Attack 5: A large VLM could inspect the hole, dull edge, or wetness.
Response: if the variable is visually available, perception can help. The claim
targets hidden or causally ambiguous state and same-label counterexamples where
the deciding variable is only exposed by action-sensor tests.

## Attack 6: TAMP already has preconditions and feasibility checks.
Response: TAMP preconditions are planner machinery. EATL is a semantics for
embodied commonsense assertions and includes object-name adversaries,
task-demand parameters, witness traces, and safety-weighted predicate errors.

## Attack 7: Hand-written tests do not scale.
Response: true as a limitation. The paper argues for the semantic object and
demonstrates why it matters; learning or synthesizing test programs is future
work.

## Attack 8: The theorem is too simple.
Response: it is deliberately simple: the goal is to make the broken assumption
unavoidable. If the only input is a label and labels are decoupled from
affordance, no amount of text prior can recover hidden causal state.

## Attack 9: The tests themselves can be costly or damaging.
Response: agreed. The v2 stress computes unsafe false positives plus normalized
test harm. Under label-preserving flips, EATL breaks even with the text prior at
test-harm weight 1.176 and loses at weight 1.25. The paper now claims EATL only
for probes that are cheap/safe relative to the prevented task failure.
