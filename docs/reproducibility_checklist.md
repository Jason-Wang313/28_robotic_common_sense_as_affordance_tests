# Reproducibility Checklist

- [x] Main experiment script is `experiments/affordance_tests.py`.
- [x] Table generator is `scripts/write_paper_assets.py`.
- [x] Build script is `scripts/build_pdf.ps1`.
- [x] Main outputs are `results/episode_results.csv`, `results/summary.csv`, and `results/README.md`.
- [x] V2 output is `results/test_cost_stress.csv`.
- [x] Paper tables are `paper/results_table.tex` and `paper/test_cost_stress_table.tex`.
- [x] Figure is `figures/accuracy_by_regime.svg`.
- [x] Paper source is `paper/main.tex`.
- [x] Canonical PDF path is `C:/Users/wangz/Downloads/28.pdf`.
- [x] Local `paper/main.pdf` is removed after canonical copy.
- [x] Visible Desktop PDF copies are absent.

Recommended verification commands:

```powershell
python experiments\affordance_tests.py
python scripts\write_paper_assets.py
powershell -ExecutionPolicy Bypass -File scripts\build_pdf.ps1
```
