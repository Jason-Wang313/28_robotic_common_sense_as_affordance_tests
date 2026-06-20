# Paper28 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Make `C:/Users/wangz/Downloads/28.pdf` explicitly match the visible VLA-v4 role model's PDF link-box behavior while preserving the final 28-page executable-affordance paper:

- citation links use green one-point boxes;
- internal figure/table/section links use red one-point boxes;
- no cyan URL boxes appear;
- the final PDF is rebuilt, rendered, inspected, copied only to Downloads, and leaves no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/28.pdf`
- Pages: 28
- Size: 324,184 bytes
- SHA256: `5FDC2D0242E633A9DFFC0D6738E3CD4C48CA0985D1AB24CACCC8221C0C3ED03E`
- Local `paper/main.pdf`: absent
- Repository state: clean against `origin/master`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[(2, 29), (3, 28), (5, 2), (6, 1), (7, 1), (8, 1), (9, 2), (10, 2), (11, 2), (17, 1)]`
- Annotation colors: green = 57, red = 12, cyan = 0
- Border widths: `(0, 0, 1)` for all 69 link annotations

Source finding:

- `paper/main.tex` is the manuscript source.
- The preamble currently uses plain `\usepackage{hyperref}` with no explicit VLA-style `\hypersetup`.
- The active manuscript has both citation commands and internal references, so green citation boxes and red internal boxes should remain present after hardening.
- `paper/iclr2026_conference.tex` is a template/example file and is not the active manuscript build target.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the role-model `\hypersetup` immediately after `\usepackage{hyperref}` in `paper/main.tex`.
2. Rebuild with `scripts/build_pdf.ps1`, including BibTeX, so the final PDF is copied to Downloads and local `paper/main.pdf` is removed.
3. Recompute page count, SHA256, annotation colors, border widths, and link pages from the rebuilt PDF.
4. Render all affected link pages from the rebuilt Downloads PDF into `tmp/pdfs/paper28_after`.
5. Visually inspect the rendered affected pages:
   - green citation boxes remain crisp and aligned;
   - red internal reference boxes remain crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, line numbers, headers, tables, and page count remain stable.
6. Update README/status/audit/version/validation metadata with the new hash and visual-hardening result.
7. Scan LaTeX logs for fatal errors, undefined citations/references, rerun warnings, and overfull boxes.
8. Remove Paper28 temp renders, leaving only the shared role-model render directory.
9. Stage only Paper28 source and metadata files, commit, push, and verify a clean repository.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography content, or page count.
- Do not add or remove citations merely to change link counts.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

- Rebuilt Downloads artifact: `C:/Users/wangz/Downloads/28.pdf`
- Pages: 28
- Size: 324,221 bytes
- SHA256: `812D8C4A7C4DD1D105779F206D5D359A9C46CD22F647488DBE9A127B511562B1`
- Local `paper/main.pdf`: absent after export
- Link pages after rebuild:
  `[(2, 29), (3, 28), (5, 2), (6, 1), (7, 1), (8, 1), (9, 4), (11, 2), (17, 1)]`
- Annotation colors after rebuild: green = 57, red = 12, cyan = 0
- Border widths after rebuild: `(0, 0, 1)` for all 69 link annotations
- Rendered affected pages inspected from `tmp/pdfs/paper28_after`; green
  citation boxes and red internal-reference boxes are crisp and aligned, and
  no cyan boxes are present.
