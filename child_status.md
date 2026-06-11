Current stage: literature and experiment complete; paper assembly starting

Exact commands/actions so far:
- Created plan.md and child_status.md.
- Ran safe probes for repo/tool availability.
- Added and ran scripts/build_literature.py.
- Patched scripts/build_literature.py to recover from OpenAlex 429 using
  Crossref/arXiv and ignore fallback-expanded cache rows.
- Reran literature generation; produced required docs artifacts.
- Sanity checked related_work_matrix.csv: fallback_matches=0.
- Added and ran experiments/affordance_tests.py.
- Fixed experiment KeyError in witness construction and reran successfully.

Findings:
- Literature artifacts generated:
  - docs/related_work_matrix.csv: 1000 rows.
  - docs/literature_map.md: includes field box, 300 skim, 225 deep read,
    hidden assumptions, and directions.
  - docs/hostile_prior_work.md: 100 hostile prior works.
  - docs/novelty_boundary_map.md, docs/novelty_decision.md, docs/claims.md,
    docs/reviewer_attacks.md.
- OpenAlex returned HTTP 429 on all initial queries; Crossref/arXiv filled the
  real metadata sweep.
- Experiment generated 1000 episodes and 180000 method-task rows.
- Key result under label_preserving_flips:
  - EATL accuracy 0.9715; unsafe FP rate 0.0218.
  - text_prior accuracy 0.8337; unsafe FP rate 0.1335.
  - vision_proxy accuracy 0.7867; unsafe FP rate 0.2073.

Failures:
- OpenAlex rate limiting: recovered via Crossref/arXiv.
- Experiment first run failed with KeyError: recovered by patching witness code.

Recovery steps:
- Non-fatal wrappers recorded failures and allowed patch/rerun.

Next:
- Fetch official ICLR 2026 LaTeX template.
- Generate paper result tables and bibliography.
- Write and compile the anonymous ICLR-style paper.
