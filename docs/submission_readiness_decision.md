# Submission Readiness Decision

Decision: workshop-only / strong-revise.

## Why Not Submit-Ready

- Evidence is synthetic and uses hand-written tests.
- No real robot or high-fidelity physics result is included.
- The lower bound covers label-only priors, not all multimodal or interactive systems.
- V2 shows that test harm/cost can erase EATL's safety advantage.
- There is no risk-aware policy for deciding when to test, abstain, or use perception.

## Why Not Kill

- The executable-witness semantics are crisp and distinct from name-prior scoring.
- The hidden-flip regime exposes a real deployment failure mode.
- EATL sharply reduces unsafe false positives when tests are cheap and targeted.
- The v2 stress honestly narrows the claim instead of hiding the test-cost assumption.

## Required Next Work

- Learn or synthesize executable affordance tests.
- Add a test-selection policy with explicit probe risk, abstention, and passive perception.
- Validate on robot manipulation tasks with measured test costs and failure harms.
- Compare against active sensing, tactile probing, TAMP feasibility, and VLM affordance systems.
