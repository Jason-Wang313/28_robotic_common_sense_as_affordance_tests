# Child Status: Paper 28

Stage: complete; v2 submission hardening ready to commit and push

Current facts:
- Literature sweep completed with `docs/related_work_matrix.csv` containing 1000 rows and `docs/hostile_prior_work.md` containing 100 hostile priors.
- Main experiment generated 1000 episodes and 180000 method-task rows.
- Main label-preserving flip result: EATL accuracy 0.9715 and unsafe false-positive rate 0.0218 versus text-prior accuracy 0.8337 and unsafe false-positive rate 0.1335.
- V2 test-cost stress generated `results/test_cost_stress.csv` and `paper/test_cost_stress_table.tex`.
- V2 stress result: under label-preserving flips, EATL breaks even with the text prior at normalized test-harm weight 1.176 and loses at weight 1.25 on safety-plus-test-cost.
- Paper generated at `paper/main.tex` with visible v2 note, stress table, narrowed abstract, and narrowed limitations.
- LaTeX build completed with `scripts/build_pdf.ps1`.
- Final PDF copied to `C:/Users/wangz/Downloads/28.pdf`.
- Transient `paper/main.pdf` removed so the final PDF exists only at the required Downloads path.
- Checked Desktop paths contain no `28.pdf`.
- Public GitHub repo exists: `https://github.com/Jason-Wang313/28_robotic_common_sense_as_affordance_tests`.
- `docs/final_audit.md` exists and reports build status, v2 stress evidence, Downloads-only artifact status, Desktop absence, and local PDF absence.

Commands run:
- `python experiments\affordance_tests.py`
- `python scripts\write_paper_assets.py`
- `powershell -ExecutionPolicy Bypass -File scripts\build_pdf.ps1`
- Safe probes for build status, Downloads PDF, Desktop absence, local PDF absence, LaTeX log status, and generated stress outputs.

Historical failures:
- OpenAlex returned HTTP 429 during the original literature run; Crossref/arXiv fallback recovered the matrix.
- Original experiment first run failed with `KeyError`; witness construction was patched before v1.
- Original build had overlapping pdflatex passes; recovered with a final sequential pass.
- Initial GitHub push emitted a non-fatal large-file warning for `results/episode_results.csv` because it is 74.23 MB.

Recovery / hardening steps:
- Added v2 test-cost stress and narrowed the EATL claim to cheap/safe, task-justified probes.
- Added standard hardening docs: attack log, version log, hostile reviewer response, rigor checklist, reproducibility checklist, and readiness decision.
- Added `scripts/build_pdf.ps1` and `.gitignore` rule for `paper/main.pdf`.
- Rebuilt the canonical PDF and removed the tracked local PDF.

Next:
- Commit and push the v2 hardening update.
