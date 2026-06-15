# Hostile Reviewer Response

## Likely Rejection

The work still lacks real robot validation and could be seen as rebranding
active sensing, affordance learning, and feasibility checking.  The synthetic
environment uses hand-written tests and normalized costs, so the paper cannot
claim deployable robot safety.

## Honest Response

We agree that this is not a deployable robot system.  The contribution is a
semantics for embodied common-sense assertions: a predicate is licensed by a
current executable witness, failure certificate, abstention, or explicitly
tracked unsupported-risk status.

The v3 evaluation is much stronger than v2 because it attacks the mechanism
rather than only demonstrating it.  It includes 4,977,600 aggregate method
decisions, strong baselines, phase diagrams, selector ablations, cache validity,
noise, visibility, demand, embodiment, and failure-gallery analyses.

The paper also states when the mechanism loses.  If hidden flips are rare or
probes are expensive, text or conservative priors can be cheaper.  If passive
perception sees all deciding variables, tests are unnecessary.  If caches ignore
validity scope, they become unsafe.

## Required Upgrade For A Real-Robot Main-Track Submission

- Learn or synthesize executable tests.
- Evaluate on real robot manipulation tasks or high-fidelity physics.
- Calibrate probe costs, false-positive harms, and guard reliability.
- Compare against real VLM affordance systems, tactile probing systems, active
  sensing systems, and TAMP feasibility checkers.
