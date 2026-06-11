# Robotic Common Sense as Executable Affordance Tests

This repository contains the artifacts for Paper 28 in the robotics batch.

## Reproduce the Evidence

```powershell
python experiments/affordance_tests.py
python scripts/write_paper_assets.py
```

Outputs:

- `results/episode_results.csv`
- `results/summary.csv`
- `results/README.md`
- `figures/accuracy_by_regime.svg`
- `paper/results_table.tex`

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
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The required final PDF path for the batch is `C:/Users/wangz/Downloads/28.pdf`.

## Dependencies

The scripts use the Python standard library only. The paper build requires
`pdflatex` and `bibtex`.
