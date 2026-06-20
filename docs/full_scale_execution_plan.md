# Paper 28 Full-Scale Execution Plan

Date: 2026-06-15

This plan is the required pre-work gate for the v3 pass. No final PDF should be
placed in Downloads until the paper has been rebuilt as a genuinely final
25-page manuscript under the current batch standard.

## 2026-06-20 Visual-Hardening Addendum

The final v3 manuscript was rebuilt with the explicit VLA role-model hyperref
policy for boxed links.  The Downloads artifact remains 28 pages and is now:

- Path: `C:/Users/wangz/Downloads/28.pdf`
- Size: 324,221 bytes
- SHA256: `812D8C4A7C4DD1D105779F206D5D359A9C46CD22F647488DBE9A127B511562B1`
- Link-box inventory: green = 57, red = 12, cyan = 0, with one-point borders
  on all 69 link annotations.

## Current Thesis

Paper 28 argues that robotic common sense should be represented as executable
affordance tests rather than as static object-name or text priors. An
affordance predicate is valid for a robot only when the robot has an executable
witness, or an accepted cached witness, for the current object, action, task
demand, and embodiment.

## Current Evidence and State

- Current manuscript version: v2.
- Current scope: synthetic tabletop environment with ten object categories, six
  affordance tasks, four regimes, three methods, 1000 episodes, and 180000
  method-task rows.
- Current positive result: under label-preserving flips, EATL reduces unsafe
  false positives from 0.1335 for the text prior to 0.0218.
- Current negative boundary: under label-preserving flips, the break-even
  normalized test-harm weight is 1.176, and EATL loses at weight 1.25 on
  safety-plus-test-cost.
- Current readiness: workshop-only / strong-revise because the evidence is
  synthetic, tests are hand-written, the cost model is simplified, and there is
  no risk-aware test-selection policy.
- Current artifact gap: `Downloads/28.pdf` is absent in the current workspace
  check, so the v3 final must create the only canonical Downloads artifact.

## Harsh Reviewer Diagnosis

The present v2 paper is coherent but too small. A reviewer can still reject it
for at least these reasons:

1. The method may be a rebranding of active sensing unless the executable
   witness semantics, cache validity, abstention, and task-demand coupling are
   formalized much more sharply.
2. The baseline set is weak: text prior, passive geometry proxy, and oracle-like
   hand-written tests do not establish what happens against uncertainty-aware
   priors, risk-aware testing, cached evidence, active probing, or test-selection
   policies.
3. The main synthetic world has too few axes: hidden variables are useful, but
   task-demand sweeps, embodiment shifts, probe noise, sensor bias, destructive
   probes, occluded variables, cached witness staleness, and adversarial same-
   name artifacts are not explored.
4. The theorem is intentionally simple and should be supported by more precise
   propositions about cost-aware testing, value of information, abstention, and
   witness invalidation.
5. The manuscript is short and reads like a concept note. It needs full
   experimental sections, failure cases, sensitivity curves, ablations,
   appendix-level implementation details, and a more careful novelty boundary.

## V3 Claim Boundary

The final paper should not claim real-robot success. It may claim:

- EATL is a semantics for robot common-sense predicates as executable,
  task-demand-specific evidence.
- In controlled hidden-affordance-flip distributions, EATL-style witnesses
  reduce unsafe false positives relative to name priors and passive proxies.
- Test execution is not always beneficial; risk-aware selection is required
  when probes are costly, damaging, noisy, stale, or unnecessary.
- Cached witnesses are useful only under explicit validity conditions and
  degrade when object state, task demand, or embodiment changes.
- The contribution is mechanism-level and benchmark-level, with honest limits
  before real-robot deployment.

The final paper must explicitly reject:

- "Always run a test."
- "EATL replaces perception, VLMs, TAMP, active sensing, or learned affordance
  models."
- "Synthetic evidence is enough for real-robot deployment."
- "The executable tests are learned automatically."

## Full-Scale Experiment Program

Create a new RAM-light v3 runner rather than mutating the compact v2 runner
in-place. The runner should stream rows to disk and maintain only aggregate
statistics in memory.

### Family A: Large Replicated Main Benchmark

Purpose: replace the 1000-episode single-seed result with a larger multi-seed
benchmark.

Design:

- Regimes: typical, label-preserving flips, label swaps, mixed, adversarial
  counterfeit, degraded/worn objects, task-demand shift, and embodiment shift.
- Tasks: contain liquid, lift, support load, cut soft food, wipe spill, carry
  hot, pour without spill, stack safely, push without sliding, and grasp without
  crushing.
- Objects: extend from 10 to at least 20 named categories with physically
  distinct hidden states.
- Methods:
  - text prior
  - calibrated text prior
  - passive vision proxy
  - uncertainty-aware vision proxy
  - conservative prior
  - risk-aware EATL selector
  - eager EATL
  - cached EATL
  - oracle hidden-state upper bound
  - random-test negative control
- Seeds: at least 20 seeds if runtime remains reasonable.
- Metrics: accuracy, unsafe false positives, avoidable false negatives,
  precision, recall, F1, balanced accuracy, abstention rate, mean test cost,
  safety-plus-test cost, and dominated-decision rate.

Expected role in paper: main results table and Figure 1/2.

### Family B: Probe-Cost and Failure-Harm Phase Diagram

Purpose: make the v2 test-cost boundary a full phase diagram instead of one
lambda point.

Design:

- Sweep test-harm weights from 0 to 3.
- Sweep failure-harm weights from 1 to 20.
- Sweep hidden-flip rates from 0 to 1.
- Compare eager EATL, risk-aware EATL, conservative prior, text prior, passive
  vision, and cached EATL.
- Report break-even surfaces and regions where testing is dominated.

Expected role in paper: phase diagram, break-even table, and negative boundary
section.

### Family C: Test-Selection Ablations

Purpose: show that "execute tests" needs a policy.

Design:

- Risk-aware selector with value-of-information threshold.
- Eager all-tests.
- No-test text prior.
- Random test selector.
- Cheapest-test selector.
- Highest-uncertainty selector.
- Conservative abstain-first policy.
- Ablate components: no failure harm, no test harm, no prior uncertainty, no
  abstention, no cache invalidation.

Expected role in paper: ablation table and selector analysis.

### Family D: Witness Cache Validity

Purpose: turn cached executable evidence into a first-class semantic object.

Design:

- Cache witness traces across episodes when label, embodiment, object state
  hash, and task demand remain valid.
- Introduce drift: wear, damage, cleaning, wetness, heating, load changes, and
  gripper changes.
- Compare strict invalidation, label-only reuse, time-to-live reuse, demand-
  compatible reuse, and no cache.
- Measure unsafe stale-witness reuse and avoided test cost.

Expected role in paper: stale witness failure table and cache trade-off figure.

### Family E: Sensor Noise, Bias, and Abstention

Purpose: attack the oracle-like test assumption.

Design:

- Sweep independent probe noise from 0 to 0.25.
- Add biased sensors for leakage, mass, heat resistance, sharpness, and
  friction.
- Add abstention when readings fall inside guard margins.
- Compare crisp guards, margin guards, repeated tests, and Bayesian guard
  aggregation.

Expected role in paper: robustness curves and guard-design section.

### Family F: Hidden-Variable Visibility and VLM-Like Baselines

Purpose: avoid a strawman passive baseline.

Design:

- Give passive proxy progressively more hidden variables: geometry only,
  geometry plus material, geometry plus damage, and full but noisy visible
  state.
- Add a VLM-like prior that blends label and visible variables with calibrated
  confidence.
- Report when passive systems close the gap and when tests are still needed.

Expected role in paper: novelty boundary against visual affordance prediction.

### Family G: Demand and Embodiment Shift

Purpose: show that affordance truth is relative to demand and robot body.

Design:

- Sweep liquid volume, load, temperature, required sharpness, gripper limit,
  gripper friction, allowed contact force, and end-effector heat tolerance.
- Evaluate whether label priors, passive proxies, and cached tests transfer
  across demand or robot changes.

Expected role in paper: task-demand heatmaps and embodiment-shift failure cases.

### Family H: Failure Case Gallery and Negative Controls

Purpose: provide reviewer-resistant qualitative evidence from the synthetic
world without pretending it is hardware.

Design:

- Write compact representative rows for false positives, false negatives,
  abstentions, stale witnesses, dominated tests, and passive-perception wins.
- Include random-test and irrelevant-test negative controls.
- Include cases where EATL should abstain or lose.

Expected role in paper: failure taxonomy and appendix table.

## Figures and Tables

Generate dependency-light SVG/LaTeX assets:

- Main benchmark table by regime and method.
- Family A safety table for unsafe false positives and abstention.
- Probe-cost phase diagram or compact heatmap.
- Test-selection ablation table.
- Cache validity table/figure.
- Noise robustness figure.
- Visibility ladder table.
- Demand/embodiment shift heatmap.
- Failure gallery table.
- Runtime and row-count reproducibility table.

## Manuscript Expansion Plan

Target final length: at least 25 compiled pages. The added length must come
from real content, not padding.

Main paper structure:

1. Abstract with v3 scope and honest boundaries.
2. Introduction focused on same-name changed-physics deployment failures.
3. Related work and novelty boundary against affordance learning, active
   sensing, TAMP, VLM robotics, interactive perception, common-sense reasoning,
   and robot foundation models.
4. EATL formalism: predicates, witnesses, guards, costs, abstention, cached
   evidence, invalidation, and task-demand dependence.
5. Formal analysis:
   - label-only lower bound
   - cost-aware testing inequality
   - value-of-information threshold
   - stale-witness invalidation failure
   - abstention as honest non-assertion
6. Experimental setup:
   - object families
   - hidden variables
   - task demands
   - regimes
   - methods
   - metrics
   - seeds
   - RAM-light implementation
7. Main results.
8. Probe-cost and failure-harm phase diagram.
9. Test-selection ablations.
10. Cache validity and stale witnesses.
11. Noise, bias, visibility, demand, and embodiment stress tests.
12. Failure cases and negative controls.
13. Discussion.
14. Limitations.
15. Reproducibility statement.
16. Appendices with full tables, algorithm boxes, environment details, and
    extra stress results.

## RAM-Light Execution Strategy

- Use one Python process per major run; no multiprocessing unless a single
  family is too slow and can be safely chunked.
- Stream raw rows to CSV files incrementally.
- Maintain aggregate counters keyed by compact tuples instead of retaining all
  rows in memory.
- Store detailed examples only for bounded failure galleries.
- Use deterministic seeds and write progress JSON after each family.
- Generate figures/tables from aggregate CSVs, not from full raw logs.
- Avoid large object-state JSON in full-scale raw rows except in bounded
  example files.
- Keep intermediate PDFs local and remove `paper/main.pdf` after final export.

## Documentation Updates Required

Update all of these before final commit:

- README.md
- child_status.md
- docs/claims.md
- docs/final_audit.md
- docs/hostile_reviewer_response.md
- docs/experiment_rigor_checklist.md
- docs/reproducibility_checklist.md
- docs/reviewer_attacks.md
- docs/submission_attack_log.md
- docs/submission_readiness_decision.md
- docs/submission_version_log.md
- data/build_status.json
- results/README.md

## Final Acceptance Checklist

Paper 28 is not complete until all checks pass:

- Detailed v3 experiment runner exists and is reproducible.
- Full-scale run completes with deterministic seed metadata.
- Results include strong baselines, ablations, stress tests, negative controls,
  uncertainty or multi-seed variation, and failure cases.
- Manuscript visibly says submission-hardening version v3 final full-scale.
- Manuscript compiles without undefined references/citations.
- Compiled paper is at least 25 pages.
- Final canonical PDF exists only as `C:/Users/wangz/Downloads/28.pdf` after
  export; local `paper/main.pdf` is removed.
- Downloads PDF is verified to be the real Paper 28 final manuscript.
- Claims are narrowed to synthetic mechanism evidence and risk-aware testing.
- Docs report exact row counts, page count, hash, and limitations.
- Git status is clean after commit.
- Commit is pushed.
- Local HEAD equals upstream HEAD before Paper 29 begins.
