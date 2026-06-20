# Reproducibility Checklist

- [x] v3 full-scale runner: `experiments/full_scale_affordance_tests.py`.
- [x] v3 figure renderer: `scripts/render_full_scale_figures.py`.
- [x] v3 appendix table writer: `scripts/write_full_scale_appendix_tables.py`.
- [x] Run metadata: `results/full_scale/run_metadata.json`.
- [x] Aggregate results: `results/full_scale/*.csv`.
- [x] Full-scale results README: `results/full_scale/README.md`.
- [x] Main manuscript tables: `paper/full_scale_main_table.tex`,
  `paper/phase_boundary_table.tex`, `paper/selector_ablation_table.tex`,
  `paper/cache_validity_table.tex`, `paper/noise_guard_table.tex`,
  `paper/visibility_ladder_table.tex`, `paper/demand_embodiment_table.tex`,
  and appendix tables.
- [x] Figure PDFs: `figures/full_scale/*.pdf`.
- [x] Final build script: `scripts/build_pdf.ps1`.
- [x] Final PDF copied to `C:/Users/wangz/Downloads/28.pdf`.
- [x] Local `paper/main.pdf` removed after final build.
- [x] Final PDF page count verified with `pdfinfo`: 28.
- [x] Final PDF hash recorded.
- [x] VLA-style link boxes verified with pypdf inventory and rendered-page
  visual inspection.

Exact final artifact:

- Path: `C:/Users/wangz/Downloads/28.pdf`
- Size: 324,221 bytes
- SHA256: `812D8C4A7C4DD1D105779F206D5D359A9C46CD22F647488DBE9A127B511562B1`
- Link boxes: green citations, red internal links, no cyan boxes.
