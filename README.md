# Robotic Common Sense as Executable Affordance Tests

This repository contains the artifacts for Paper 28 in the robotics batch.

## Hardening Status

Status: v3 final full-scale.

The v3 pass expands the original compact synthetic note into a full-scale
mechanism paper.  It adds a RAM-light multi-family experiment suite with:

- 20 object categories.
- 10 affordance predicates.
- 8 deployment regimes.
- 10 mechanisms.
- 192,000 main robot-object-task cases.
- 1,920,000 main method decisions.
- 4,977,600 aggregate method decisions overall.
- Phase diagrams, selector ablations, cache validity tests, noise/guard
  sweeps, visibility ladders, demand/embodiment sweeps, and failure galleries.

Key result: under label-preserving flips, the text prior has 0.188 unsafe
false positives, eager EATL has 0.022, and risk-aware EATL has 0.015 with lower
test cost than eager testing.  Under adversarial counterfeits, the text prior
has 0.197 unsafe false positives and risk-aware EATL has 0.025.

The claim remains synthetic and mechanism-level.  The paper does not claim
real-robot validation.

## Reproduce the v3 Evidence

```powershell
python experiments/full_scale_affordance_tests.py
python scripts/render_full_scale_figures.py
python scripts/write_full_scale_appendix_tables.py
```

Primary v3 outputs:

- `results/full_scale/main_summary.csv`
- `results/full_scale/main_task_summary.csv`
- `results/full_scale/phase_summary.csv`
- `results/full_scale/phase_boundary.csv`
- `results/full_scale/selector_ablation_summary.csv`
- `results/full_scale/cache_validity_summary.csv`
- `results/full_scale/noise_guard_summary.csv`
- `results/full_scale/visibility_summary.csv`
- `results/full_scale/demand_embodiment_summary.csv`
- `results/full_scale/failure_gallery.csv`
- `figures/full_scale/*.pdf`
- `paper/full_scale_main_table.tex`
- `paper/*appendix_table.tex`

## Reproduce the v2 Evidence

The older compact experiment is retained:

```powershell
python experiments/affordance_tests.py
python scripts/write_paper_assets.py
```

## Build the Paper

```powershell
python scripts/render_full_scale_figures.py
python scripts/write_full_scale_appendix_tables.py
powershell -ExecutionPolicy Bypass -File scripts/build_pdf.ps1
```

The build script copies the final PDF to `C:/Users/wangz/Downloads/28.pdf` and
removes transient local `paper/main.pdf`.

Final verified artifact:

- Path: `C:/Users/wangz/Downloads/28.pdf`
- Pages: 28
- Size: 324,184 bytes
- SHA256: `5FDC2D0242E633A9DFFC0D6738E3CD4C48CA0985D1AB24CACCC8221C0C3ED03E`

## Dependencies

The full-scale runner uses the Python standard library.  Figure rendering uses
`matplotlib`.  The paper build requires `pdflatex` and `bibtex`.
