# Robotic Common Sense as Executable Affordance Tests

This repository contains the artifacts for Paper 28 in the robotics batch.

## Hardening Status

This is the v2 submission-hardened version. The added test-cost stress shows
that EATL is justified only when diagnostic probes are cheap and safe enough:
under label-preserving flips, the break-even test-harm weight against the text
prior is 1.176, and at weight 1.25 EATL's safety-plus-test-cost is 0.141 versus
0.134 for the text prior.

## Reproduce the Evidence

```powershell
python experiments/affordance_tests.py
python scripts/write_paper_assets.py
```

Outputs:

- `results/episode_results.csv`
- `results/summary.csv`
- `results/test_cost_stress.csv`
- `results/README.md`
- `figures/accuracy_by_regime.svg`
- `paper/results_table.tex`
- `paper/test_cost_stress_table.tex`

## Reproduce the Literature Artifacts

```powershell
python scripts/build_literature.py
```

The run writes:

- `docs/related_work_matrix.csv`
- `docs/literature_map.md`
- `docs/hostile_prior_work.md`
- `docs/novelty_boundary_map.md`
- `docs/novelty_decision.md`
- `docs/claims.md`
- `docs/reviewer_attacks.md`

During the recorded run, OpenAlex returned HTTP 429 rate limits; the script
recovered with Crossref and arXiv metadata and produced a 1000-row matrix with
no fallback-expanded rows.

## Build the Paper

```powershell
python scripts/fetch_iclr_template.py
powershell -ExecutionPolicy Bypass -File scripts/build_pdf.ps1
```

The build script copies the final PDF to `C:/Users/wangz/Downloads/28.pdf` and
removes the transient local `paper/main.pdf`.

## Dependencies

The scripts use the Python standard library only. The paper build requires
`pdflatex` and `bibtex`.
