# Child Status: Paper 28

Stage: v3 final full-scale complete; VLA link-box hardening exported and
verified; ready to commit/push

Current facts:

- Title: `Robotic Common Sense as Executable Affordance Tests`.
- v3 plan was written before substantive work in
  `docs/full_scale_execution_plan.md`.
- Full-scale runner: `experiments/full_scale_affordance_tests.py`.
- Figure renderer: `scripts/render_full_scale_figures.py`.
- Appendix table generator: `scripts/write_full_scale_appendix_tables.py`.
- Main benchmark: 192,000 robot-object-task cases and 1,920,000 method
  decisions.
- Full aggregate suite: 4,977,600 method decisions.
- Full-scale run elapsed time: 437.075 seconds.
- Label-preserving flips: text prior unsafe FP 0.188, eager EATL 0.022,
  risk-aware EATL 0.015.
- Adversarial counterfeits: text prior unsafe FP 0.197, passive vision 0.240,
  eager EATL 0.037, risk-aware EATL 0.025.
- Cache validity: label-only cache unsafe FP 0.270; strict cache unsafe FP
  0.025 while reducing test cost versus no cache.
- Noise stress: crisp one-shot guards degrade under noise; repeated and
  abstaining guards reduce unsafe assertions at higher cost or lower coverage.
- Visibility ladder: full noisy hidden-state visibility solves the synthetic
  task, honestly narrowing the EATL claim.
- Final manuscript: `paper/main.tex`, visible `v3 final full-scale` note.
- Final PDF: `C:/Users/wangz/Downloads/28.pdf`.
- Final PDF pages: 28.
- Final PDF size: 324,221 bytes.
- Final PDF SHA256:
  `812D8C4A7C4DD1D105779F206D5D359A9C46CD22F647488DBE9A127B511562B1`.
- Final PDF link boxes: green citation boxes and red internal-reference boxes
  match the VLA role-model policy; no cyan URL boxes were found.
- Local `paper/main.pdf` is absent after final export.
- Build status: `data/build_status.json` reports complete, copied true,
  removed local PDF true.

Commands run in v3:

- `python experiments/full_scale_affordance_tests.py`
- `python scripts/render_full_scale_figures.py`
- `python scripts/write_full_scale_appendix_tables.py`
- Local LaTeX compile checks with `pdflatex/bibtex/pdflatex/pdflatex`
- `powershell -ExecutionPolicy Bypass -File scripts/build_pdf.ps1`
- PDF verification with `pdfinfo`, `pdftotext`, `Get-FileHash`, and log scans
- VLA link-box verification with pypdf annotation inventory and rendered-page
  visual inspection

Final validation:

- `Downloads/28.pdf` exists.
- Page count is 28.
- PDF text contains `v3 final full-scale`, `192,000`, `4,977,600`, and
  `risk-aware EATL`.
- Link annotation inventory is green = 57, red = 12, cyan = 0, with one-point
  borders on all 69 link annotations.
- `paper/main.log` has no overfull boxes, undefined references, or undefined
  citations in the final build.
- `paper/main.pdf` was removed by the build script.

Next:

- Commit and push v3 full-scale hardening.
