# Hostile Reviewer Response

## Likely Rejection

The work rebrands active sensing and affordance learning, then evaluates only a synthetic tabletop world with hand-written tests. Worse, some tests can be costly or destructive, so "execute a test" is not always safer than a cautious prior.

## Honest Response

We agree that EATL is not a deployable robot system by itself. The contribution is a semantics for embodied common-sense claims: a predicate is supported only by current executable evidence for the robot-object-demand tuple.

The v2 stress quantifies the objection. In label-preserving flips, EATL lowers unsafe false positives from 0.134 to 0.022 at mean test cost 0.095. That advantage breaks even at normalized test-harm weight 1.176, and EATL loses at weight 1.25. The paper should claim only cheap, safe, task-justified probes.

## Required Upgrade For Main-Track Submission

- Evaluate on real or high-fidelity robot manipulation tasks.
- Learn or synthesize test programs instead of hand-writing them.
- Add a risk-aware test-selection policy that can abstain or use passive perception.
- Compare against active perception, tactile probing, TAMP feasibility checks, and VLM affordance baselines.
