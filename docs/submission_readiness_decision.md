# Submission Readiness Decision

Decision: v3 final full-scale synthetic mechanism paper; strong-revise for a
robotics main track that requires hardware or high-fidelity simulation.

## Why This Is Now Much Stronger

- The paper is 28 pages with full formalism, expanded related-work boundary,
  main results, phase diagrams, ablations, cache studies, noise studies,
  visibility studies, demand/embodiment shifts, failure galleries, and long
  appendix tables.
- The evidence expanded from the compact v2 run to 4,977,600 aggregate method
  decisions.
- The strongest claim is now supported: executable witnesses reduce unsafe
  assertions under hidden same-name physical changes when selected with cost and
  validity conditions.
- The negative boundary is explicit rather than hidden.

## Why It Is Still Not A Real-Robot Submission

- No real robot validation is included.
- No high-fidelity physics simulation is included.
- Test policies and guards are hand-specified.
- Costs are normalized synthetic costs.
- Passive full-visibility baselines can solve the synthetic task, so the claim
  must remain about hidden, stale, or demand-specific variables.

## Final Honest Position

The paper is final under the current batch standard as a full-scale synthetic
mechanism paper.  It should be positioned as executable semantics and benchmark
evidence, not as a deployable robot system.
