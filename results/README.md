# Affordance-Test Experiment Results

This directory contains both the historical v2 compact outputs and the v3
full-scale outputs.

## v3 Full-Scale Results

The final manuscript uses `results/full_scale/`.

Reproduce:

```powershell
python experiments/full_scale_affordance_tests.py
python scripts/render_full_scale_figures.py
python scripts/write_full_scale_appendix_tables.py
```

Summary:

- Main benchmark: 192,000 robot-object-task cases.
- Main method decisions: 1,920,000.
- Aggregate method decisions across all families: 4,977,600.
- Main label-preserving flips: text prior unsafe FP 0.188, eager EATL 0.022,
  risk-aware EATL 0.015.
- Main adversarial counterfeits: text prior unsafe FP 0.197, passive vision
  0.240, risk-aware EATL 0.025.

Primary files:

- `full_scale/main_summary.csv`
- `full_scale/main_task_summary.csv`
- `full_scale/phase_summary.csv`
- `full_scale/phase_boundary.csv`
- `full_scale/selector_ablation_summary.csv`
- `full_scale/cache_validity_summary.csv`
- `full_scale/noise_guard_summary.csv`
- `full_scale/visibility_summary.csv`
- `full_scale/demand_embodiment_summary.csv`
- `full_scale/failure_gallery.csv`
- `full_scale/run_metadata.json`

## Historical v2 Results

The v2 compact experiment compared:

- `text_prior`: predicts affordances from the object label.
- `vision_proxy`: sees geometry-like variables but not hidden material/damage.
- `eatl`: runs executable affordance tests that probe task-specific causal
  variables.

Historical files:

- `episode_results.csv`
- `summary.csv`
- `test_cost_stress.csv`

The v2 stress computed `unsafe_false_positive_rate + lambda * mean_test_cost`.
Under label-preserving flips, the v2 break-even test-harm weight was 1.176.
