# Final Audit

1. **Chosen thesis**
   Robotic common sense should be defined as executable affordance tests: an
   affordance predicate is supported only when the robot can run, or cite, a
   task-demand-specific micro-experiment that returns a witness for the current
   robot-object-action tuple.

2. **Field assumption broken**
   The broken assumption is that object names, passive visual categories, or
   text priors remain reliably correlated with physical affordances at
   deployment. The paper targets label-preserving affordance flips such as a mug
   with a hole, a dull knife, a wet cardboard box, or a hot object without a
   usable handle.

3. **New central mechanism**
   Executable Affordance Test Logic (EATL). Each predicate has a typed
   micro-policy, observation trace, guard, normalized cost, and pass/fail/abstain
   output. A pass trace is a witness; a fail trace is a failure certificate.

4. **Genuine novelty**
   The novelty is semantic rather than architectural: the paper changes what a
   robot common-sense claim is. It is not a larger model, better data, generic
   uncertainty, active learning, an LLM planner, reinforcement learning, or a
   verifier bolted onto a plan. Existing affordance predictors and planners can
   implement tests, but they do not define common-sense predicates as executable
   witnesses.

5. **Closest hostile prior work**
   The closest hostile areas are classical robot affordance learning
   (Sahin et al.; Montesano et al.; Stoytchev), task-and-motion feasibility
   checking (Kaelbling and Lozano-Perez; Toussaint; PDDLStream), and
   language-grounded affordance robotics (SayCan, Inner Monologue, Code as
   Policies, VoxPoser, PaLM-E, RT-1/RT-2). These make prediction, planning
   feasibility, and language-affordance scoring non-novel, but leave open an
   executable semantics for embodied common-sense predicates under hidden
   physical state changes.

6. **Literature coverage**
   Required artifacts exist. `docs/related_work_matrix.csv` has 1000 rows.
   `docs/literature_map.md` documents the 1000-paper landscape sweep, 300-paper
   serious skim, 225-paper deep-read subset, 100-paper hostile set, field box,
   hidden assumptions, and candidate directions. OpenAlex returned HTTP 429
   during this run; the script recovered with Crossref and arXiv metadata.
   A sanity check found `fallback_matches=0` in the final matrix.

7. **Proof/formal-claim status**
   The paper contains one narrow proposition. For any label-only classifier, if
   a fixed label has positive affordance probability `p`, the best possible
   conditional error is at least `min(p, 1-p)`, reaching 1/2 on balanced
   same-label counterexamples. If a test observes sufficient evidence with
   guard error at most epsilon, its non-abstaining predicate error is at most
   epsilon. This is a simple lower-bound argument, not a broad theorem about all
   perception or planning systems.

8. **Strongest evidence**
   The runnable synthetic tabletop experiment generated 1000 episodes and
   180000 method-task rows. Under `label_preserving_flips`, EATL reached 0.9715
   accuracy and 0.0218 unsafe false-positive rate, compared with 0.8337
   accuracy and 0.1335 unsafe false-positive rate for the text prior. The
   experiment is reproducible with `python experiments/affordance_tests.py`.

9. **Biggest weaknesses**
   No real-robot or high-fidelity physics result is included. Test programs are
   hand-specified. The cost model is simplified. The theorem assumes sufficient
   test observations and independent guard noise. The literature sweep is broad
   and hostile, but most entries are metadata/abstract skims rather than full
   PDF readings.

10. **Paper-readiness judgment**
    Workshop. The mechanism and stress test are coherent, but an ICLR main-track
    submission would need real-robot or stronger simulator evidence, learned or
    synthesized tests, and more manual verification of the most hostile prior
    work.

11. **Exact Downloads PDF path**
    `C:/Users/wangz/Downloads/28.pdf`

12. **GitHub URL**
    `https://github.com/Jason-Wang313/28_robotic_common_sense_as_affordance_tests`

13. **Visible Desktop PDF copy status**
    pending orchestrator copy

## Build and Push Status

- Official ICLR 2026 template fetched from the ICLR/Master-Template
  `iclr2026.zip`.
- Paper compiled successfully with direct `pdflatex`, `bibtex`, and final
  sequential `pdflatex` passes.
- Final PDF copied to `C:/Users/wangz/Downloads/28.pdf`.
- GitHub repository created as public and pushed successfully to `master`.
- GitHub emitted a non-fatal warning that `results/episode_results.csv` is
  74.23 MB, above the recommended 50 MB size but below the hard 100 MB limit.
