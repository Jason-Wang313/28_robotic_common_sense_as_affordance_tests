Current stage: complete

Exact commands/actions so far:
- Created plan.md with apply_patch as the first folder action.
- Created and maintained child_status.md.
- Ran safe probes for repo/tool availability.
- Added scripts/build_literature.py and experiments/affordance_tests.py.
- Ran python scripts/build_literature.py with 300000 ms timeout.
- Patched literature collector after OpenAlex HTTP 429 to add Crossref/arXiv
  source adapters and ignore fallback-expanded cache rows.
- Reran python scripts/build_literature.py with 300000 ms timeout.
- Checked docs/related_work_matrix.csv for fallback-expanded rows:
  fallback_matches=0.
- Ran python experiments/affordance_tests.py with 300000 ms timeout.
- Patched experiment witness construction after KeyError and reran.
- Added scripts/fetch_iclr_template.py.
- Ran python scripts/fetch_iclr_template.py; fetched official ICLR 2026 files
  from https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip.
- Added scripts/write_paper_assets.py and ran it.
- Wrote README.md, paper/main.tex, paper/references.bib, and docs/final_audit.md.
- Built paper with:
  - pdflatex -interaction=nonstopmode -halt-on-error main.tex
  - bibtex main
  - pdflatex -interaction=nonstopmode -halt-on-error main.tex
  - pdflatex -interaction=nonstopmode -halt-on-error main.tex
  - one extra final sequential pdflatex pass after noticing two passes had
    overlapped.
- Copied paper/main.pdf to C:/Users/wangz/Downloads/28.pdf.
- Ran gh auth status.
- Ran gh repo create 28_robotic_common_sense_as_affordance_tests --public
  --source=. --remote=origin.
- Ran git add ., git commit -m "Produce paper 28 affordance-test artifacts",
  and git push -u origin master.

Findings:
- Literature artifacts generated:
  - docs/related_work_matrix.csv: 1000 rows.
  - docs/literature_map.md: includes field box, 300 skim, 225 deep read,
    hidden assumptions, and directions.
  - docs/hostile_prior_work.md: 100 hostile prior works.
  - docs/novelty_boundary_map.md, docs/novelty_decision.md, docs/claims.md,
    docs/reviewer_attacks.md, docs/final_audit.md.
- OpenAlex returned HTTP 429 on all initial queries; Crossref/arXiv filled the
  real metadata sweep.
- Experiment generated 1000 episodes and 180000 method-task rows.
- Key result under label_preserving_flips:
  - EATL accuracy 0.9715; unsafe FP rate 0.0218.
  - text_prior accuracy 0.8337; unsafe FP rate 0.1335.
  - vision_proxy accuracy 0.7867; unsafe FP rate 0.2073.
- Final PDF exists at C:/Users/wangz/Downloads/28.pdf.
- Public GitHub URL:
  https://github.com/Jason-Wang313/28_robotic_common_sense_as_affordance_tests

Failures:
- OpenAlex rate limiting: recovered via Crossref/arXiv.
- Experiment first run failed with KeyError: recovered by patching witness code.
- Two pdflatex passes were accidentally launched in parallel; recovered by
  running one final sequential pass.
- GitHub push emitted a non-fatal large-file warning for
  results/episode_results.csv: 74.23 MB exceeds recommended 50 MB but is below
  hard 100 MB limit.

Recovery steps:
- Non-fatal wrappers recorded failures and allowed patch/rerun.
- Final audit records the synthetic-evidence limitation and GitHub warning.

Next:
- No required child-agent work remains. Orchestrator desktop copy status is
  pending orchestrator copy.
