# Claims

## Supported by Formal Argument
1. For a label-only common-sense prior, if a deployment distribution contains
   label-preserving affordance flips with rate rho for a task predicate, the
   expected error for that label is at least min(rho, 1-rho), and reaches 1/2 on
   balanced same-label counterexamples.
2. If an executable affordance test observes sufficient causal variables for the
   predicate with independent sensor error epsilon, its predicate error is at
   most epsilon plus abstention-handling error for that test.

## Supported by Runnable Evidence
1. In the synthetic tabletop environment, name priors score well on typical
   objects but collapse under label-preserving physical mutations.
2. EATL maintains substantially lower unsafe false-positive rates because it
   tests containment, support, grasp, cutting, wiping, and thermal-transfer
   preconditions directly.
3. The benefit is largest when the visual/name taxonomy is held fixed while
   hidden variables such as holes, porosity, dullness, load capacity, heat
   resistance, and slipperiness change.
4. The v2 test-cost stress shows EATL is conditional on cheap/safe probes:
   under label-preserving flips the break-even test-harm weight is 1.176, and
   at weight 1.25 EATL loses to the text prior on safety-plus-test-cost.

## Honest Unsupported or Partially Supported Claims
1. Real-robot performance is not demonstrated in this run.
2. The test programs are hand-specified rather than learned from robot data.
3. The cost model is simplified and does not include wear caused by tests.
4. The theorem assumes a clean separation between label-only priors and tests
   that observe sufficient causal variables.
5. The literature sweep is broad and hostile, but most entries are abstract and
   metadata skims, not full PDF readings.
6. V2 does not solve test selection; it only quantifies when test harm can erase
   the safety advantage.
