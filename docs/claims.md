# Claims

## Supported by Formal Argument

1. For a label-only common-sense prior, if a deployment distribution contains
   same-label affordance flips, the best label-only conditional error is bounded
   below by `min(p, 1-p)` for the fixed label and reaches 1/2 on balanced
   counterexamples.
2. A test improves safety-plus-test cost when the expected reduction in unsafe
   false-positive harm exceeds the cost of running the test.
3. Abstention is an honest non-assertion when both assertion and rejection have
   higher expected cost than escalation.
4. Cached witnesses require validity conditions over object state, robot
   embodiment, task demand, and time; label-only witness reuse is unsafe when
   hidden variables can change.

## Supported by Runnable v3 Evidence

1. In the 192,000-case main benchmark, text/name priors are excellent on typical
   objects but fail under hidden same-name physical changes.
2. Under label-preserving flips, risk-aware EATL reduces unsafe false positives
   from 0.188 for the text prior to 0.015, while eager EATL reaches 0.022.
3. Under adversarial counterfeits, risk-aware EATL reduces unsafe false
   positives from 0.197 for the text prior and 0.240 for passive vision to
   0.025.
4. Risk-aware EATL uses less mean test cost and lower mean total cost than eager
   testing in the hostile regimes.
5. The phase diagram shows the boundary: when hidden flips are rare or probes
   are expensive, text or conservative priors can dominate.
6. Strict witness caches reduce test cost without the large unsafe failure of
   label-only cache reuse.
7. Probe-noise sweeps show that guard design matters; repeated and abstaining
   guards reduce unsafe false positives at higher cost or lower coverage.
8. The visibility ladder shows that passive systems can close the gap when they
   directly observe the deciding hidden variables.

## Honest Unsupported or Partially Supported Claims

1. Real-robot performance is not demonstrated.
2. High-fidelity physics simulation is not included.
3. Test programs are hand-specified rather than learned or synthesized.
4. The cost model is normalized and synthetic.
5. The formal analysis is intentionally narrow and does not cover every
   multimodal or interactive system.
6. The paper supports a synthetic mechanism claim, not a deployable robot system
   claim.
