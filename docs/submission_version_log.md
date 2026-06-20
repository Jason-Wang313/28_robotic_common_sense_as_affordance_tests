# Submission Version Log

## v4 visual link-box hardening - 2026-06-20

- Added explicit VLA role-model `hyperref` boxed-link policy to `paper/main.tex`.
- Rebuilt the final PDF and exported it to `C:/Users/wangz/Downloads/28.pdf`.
- Verified 28 pages, 324,221 bytes, and no local `paper/main.pdf`.
- Verified link annotation colors: green = 57, red = 12, cyan = 0, with
  one-point borders on all 69 link annotations.
- Final PDF SHA256:
  `812D8C4A7C4DD1D105779F206D5D359A9C46CD22F647488DBE9A127B511562B1`.

## v3 final full-scale - 2026-06-15

- Added `docs/full_scale_execution_plan.md` before substantive v3 work.
- Added `experiments/full_scale_affordance_tests.py`.
- Added `scripts/render_full_scale_figures.py`.
- Added `scripts/write_full_scale_appendix_tables.py`.
- Ran full-scale suite: 192,000 main cases, 1,920,000 main method decisions,
  4,977,600 aggregate method decisions, elapsed 437.075 seconds.
- Added full-scale CSVs in `results/full_scale/`.
- Added full-scale PDF figures in `figures/full_scale/`.
- Rewrote `paper/main.tex` as a 28-page v3 final full-scale manuscript.
- Added long appendix tables generated from CSV outputs.
- Final PDF exported to `C:/Users/wangz/Downloads/28.pdf`.
- Final v3 PDF SHA256 before the 2026-06-20 visual-hardening rebuild:
  `5FDC2D0242E633A9DFFC0D6738E3CD4C48CA0985D1AB24CACCC8221C0C3ED03E`.

## v2 - 2026-06-13

- Added test-cost stress generation to `experiments/affordance_tests.py`.
- Generated `results/test_cost_stress.csv`.
- Added `paper/test_cost_stress_table.tex`.
- Updated `results/README.md` with the v2 stress table.
- Updated the manuscript with a visible v2 note, test-cost stress table,
  narrowed abstract, and stronger limitations.
