Paper 28 Plan
=============

Objective
---------
Produce a complete anonymous ICLR-style robotics/embodied-intelligence paper for
``Robotic Common Sense as Affordance Tests``, with runnable evidence, literature
coverage artifacts, final audit, compiled PDF at ``C:/Users/wangz/Downloads/28.pdf``,
and a public GitHub push when credentials permit.

Execution Stages
----------------
1. Initialize run bookkeeping.
   - Create and maintain ``child_status.md``.
   - Inspect the existing repo without deleting or reverting user artifacts.
   - Record tool availability and recovery paths.

2. Landscape sweep before choosing a thesis.
   - Collect at least 1000 relevant robotics/embodied-common-sense prior works
     using public scholarly metadata APIs and cached files.
   - Save ``docs/related_work_matrix.csv`` with problem, mechanism, assumptions,
     fixed variables, ignored failures, novelty pressure, and open gaps.
   - Produce a 300-paper serious skim, 200-250-paper deep read subset, and
     100-paper hostile prior-work set from the same cache.

3. Novelty search and decision.
   - Define the field box and at least 20 fragile hidden assumptions.
   - Generate directions that break those assumptions.
   - Select the strongest thesis only after hostile comparison.
   - Save ``docs/literature_map.md``, ``docs/hostile_prior_work.md``,
     ``docs/novelty_boundary_map.md``, ``docs/novelty_decision.md``,
     ``docs/claims.md``, and ``docs/reviewer_attacks.md``.

4. Runnable evidence.
   - Implement a small reproducible embodied affordance-test environment.
   - Compare text-prior scoring against executable affordance tests under
     controlled assumption breaks.
   - Save scripts, configs, data, figures, and command documentation.

5. Paper writing and build.
   - Use the latest official ICLR LaTeX template available at runtime.
   - Sanitize BibTeX/LaTeX for pdfLaTeX.
   - Write an anonymous complete paper with honest claims and limitations.
   - Compile with direct ``pdflatex``/``bibtex`` passes and copy the final PDF
     only to ``C:/Users/wangz/Downloads/28.pdf``.

6. Publication packaging.
   - Ensure repo is runnable from a clean checkout.
   - Create or update public GitHub repo
     ``28_robotic_common_sense_as_affordance_tests`` and push if authenticated.
   - Write ``docs/final_audit.md`` answering the required twelve audit points
     plus desktop-copy status.

Safety Notes
------------
- Avoid bare nonzero diagnostic commands; wrap expected failures and record them.
- Use explicit long timeouts for experiments and LaTeX builds.
- Do not delete or revert unrelated existing files.
- Reuse existing artifacts if this folder already contains useful progress.
