# Final Audit

1. Chosen thesis: Robotic common sense should be defined as executable
   affordance tests.  An affordance predicate is supported only when the robot
   has current executable evidence, or a valid cached witness, for the current
   robot-object-action-demand tuple.

2. Final hardening version: v3 final full-scale.

3. Field assumption broken: Object names, passive categories, and text priors
   often remain stable while hidden physical variables, task demands, or robot
   embodiment change.

4. New central mechanism: Executable Affordance Test Logic (EATL), with typed
   micro-policies, observation traces, pass/fail/abstain guards, test costs, and
   witness validity scopes.

5. Genuine novelty: The novelty is semantic and evidential.  The paper is not
   claiming generic affordance learning, active sensing, TAMP feasibility, or a
   new VLM policy.  It changes when a robot may assert an embodied
   common-sense predicate.

6. Literature boundary: Affordance learning, interactive perception, active
   sensing, TAMP, language-conditioned robotics, and robot foundation models are
   acknowledged as close prior work.  They can implement or propose EATL tests,
   but they do not by themselves define the witness semantics.

7. Formal status: The manuscript includes a label-only lower bound,
   cost-aware test threshold, abstention condition, and invalid-cache argument.
   These are intentionally narrow and used to justify the mechanism boundary.

8. Strongest v3 evidence: Full-scale synthetic suite with 4,977,600 aggregate
   method decisions.  The main benchmark has 192,000 robot-object-task cases and
   1,920,000 method decisions.

9. Key positive result: Under label-preserving flips, risk-aware EATL reduces
   unsafe false positives from 0.188 for text priors to 0.015.  Under
   adversarial counterfeits, risk-aware EATL reduces unsafe false positives
   from 0.197 for text priors to 0.025.

10. Key negative boundary: Text or conservative priors can dominate when hidden
   flips are rare or probe costs are high.  Passive full-visibility systems can
   solve the synthetic task when they observe the deciding variables.

11. Biggest weaknesses: No real robot, no high-fidelity physics simulator, no
   learned tests, and normalized synthetic costs.

12. Paper-readiness judgment: final full-scale synthetic mechanism paper;
   strong-revise for hardware-focused robotics venues.

13. Final Downloads PDF path: `C:/Users/wangz/Downloads/28.pdf`.

14. Final PDF page count: 28.

15. Final PDF size: 324,221 bytes.

16. Final PDF SHA256:
   `812D8C4A7C4DD1D105779F206D5D359A9C46CD22F647488DBE9A127B511562B1`.

17. Build status: `data/build_status.json` reports `complete`, copied true, and
   removed local PDF true.

18. Local repo PDF copy: absent after final export.

19. PDF text markers verified: `v3 final full-scale`, `192,000`, `4,977,600`,
   and `risk-aware EATL`.

20. LaTeX final-log check: no overfull boxes, undefined references, or
   undefined citations were found by log scan.

21. Public GitHub repo:
   `https://github.com/Jason-Wang313/28_robotic_common_sense_as_affordance_tests`.

22. VLA-style link-box audit: all 69 link annotations use one-point borders;
    citation boxes are green, internal-reference boxes are red, no cyan boxes
    are present, and rendered affected pages were visually inspected.
