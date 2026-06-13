# Final Audit

1. Chosen thesis: Robotic common sense should be defined as executable affordance tests: an affordance predicate is supported only when the robot can run, or cite, a task-demand-specific micro-experiment that returns a witness for the current robot-object-action tuple.

2. Field assumption broken: The run challenges the assumption that object names, passive visual categories, or text priors remain reliably correlated with physical affordances at deployment.

3. New central mechanism: Executable Affordance Test Logic (EATL). Each predicate has a typed micro-policy, observation trace, guard, normalized cost, and pass/fail/abstain output. A pass trace is a witness; a fail trace is a failure certificate.

4. Genuine novelty: The novelty is semantic rather than architectural. The paper changes what a robot common-sense claim is; it is not a larger model, better data, generic uncertainty, active learning, an LLM planner, reinforcement learning, or a verifier bolted onto a plan.

5. Closest hostile prior work: Classical robot affordance learning, interactive perception, active sensing, task-and-motion feasibility checking, and language-grounded affordance robotics. These make prediction, planning feasibility, and language-affordance scoring non-novel, but leave open an executable-witness semantics for hidden same-label physical changes.

6. Literature coverage: `docs/related_work_matrix.csv` has 1000 rows. `docs/literature_map.md` documents the 1000-paper landscape sweep, 300-paper serious skim, 225-paper deep-read subset, and 100-paper hostile set. OpenAlex returned HTTP 429 during the original run; the script recovered with Crossref and arXiv metadata.

7. Proof/formal-claim status: The paper contains a narrow label-only lower bound. For any label-only classifier, if a fixed label has positive affordance probability `p`, the best possible conditional error is at least `min(p, 1-p)`, reaching 1/2 on balanced same-label counterexamples. If a test observes sufficient evidence with guard error at most epsilon, its non-abstaining predicate error is at most epsilon.

8. Strongest evidence: The synthetic tabletop experiment generated 1000 episodes and 180000 method-task rows. Under `label_preserving_flips`, EATL reached 0.9715 accuracy and 0.0218 unsafe false-positive rate, compared with 0.8337 accuracy and 0.1335 unsafe false-positive rate for the text prior.

9. V2 stress evidence: The test-cost stress computes unsafe false positives plus `lambda * mean_test_cost`. Under label-preserving flips, EATL's break-even test-harm weight against the text prior is 1.176. At `lambda=1.25`, EATL's safety-plus-test-cost is 0.141 versus 0.134 for the text prior, so the mechanism depends on cheap, safe, task-justified probes.

10. Biggest weaknesses: No real-robot or high-fidelity physics result is included. Test programs are hand-specified. The cost model is simplified. The theorem is label-only. The v2 stress does not solve risk-aware test selection; it only exposes when test harm can erase EATL's safety advantage.

11. Paper-readiness judgment: workshop-only / strong-revise. The mechanism and stress test are coherent, but an ICLR main-track submission would need real-robot or stronger simulator evidence, learned or synthesized tests, and risk-aware test selection.

12. Exact Downloads PDF path: `C:/Users/wangz/Downloads/28.pdf` (exists, size=171742 bytes). Build status: `complete`; copied flag: `True`.

13. GitHub URL: `https://github.com/Jason-Wang313/28_robotic_common_sense_as_affordance_tests`.

14. Visible Desktop PDF copy: absent at checked Desktop paths (expected; canonical PDF is Downloads only).

15. Local repo PDF copy: absent (expected after Downloads copy).

Additional audit notes:
- Official ICLR 2026 template fetched from the ICLR/Master-Template `iclr2026.zip`.
- The build used `scripts/build_pdf.ps1` and removed transient `paper/main.pdf`.
- GitHub previously emitted a non-fatal warning that `results/episode_results.csv` is above the recommended 50 MB size but below the hard 100 MB limit.
