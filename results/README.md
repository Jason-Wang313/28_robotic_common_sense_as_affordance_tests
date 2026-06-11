# Affordance-Test Experiment Results

The experiment compares three mechanisms:

- `text_prior`: predicts affordances from the object label.
- `vision_proxy`: sees geometry-like variables but not hidden material/damage.
- `eatl`: runs executable affordance tests that probe task-specific causal variables.

| Regime | Method | Accuracy | Unsafe FP Rate | Avoidable FN Rate | F1 | Mean Test Cost |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| label_preserving_flips | eatl | 0.972 | 0.022 | 0.007 | 0.934 | 0.095 |
| label_preserving_flips | text_prior | 0.834 | 0.134 | 0.033 | 0.680 | 0.000 |
| label_preserving_flips | vision_proxy | 0.787 | 0.207 | 0.006 | 0.656 | 0.000 |
| label_swap | eatl | 0.971 | 0.020 | 0.009 | 0.956 | 0.095 |
| label_swap | text_prior | 0.679 | 0.152 | 0.169 | 0.500 | 0.000 |
| label_swap | vision_proxy | 0.840 | 0.150 | 0.010 | 0.800 | 0.000 |
| mixed | eatl | 0.956 | 0.031 | 0.013 | 0.928 | 0.095 |
| mixed | text_prior | 0.797 | 0.113 | 0.089 | 0.668 | 0.000 |
| mixed | vision_proxy | 0.819 | 0.170 | 0.011 | 0.758 | 0.000 |
| typical | eatl | 0.980 | 0.014 | 0.006 | 0.971 | 0.095 |
| typical | text_prior | 0.917 | 0.029 | 0.054 | 0.871 | 0.000 |
| typical | vision_proxy | 0.850 | 0.142 | 0.007 | 0.813 | 0.000 |

The important stress regime is `label_preserving_flips`: the object name is
unchanged, but hidden properties such as holes, porosity, dullness, load
capacity, heat resistance, and slipperiness are changed. A name-only prior has
no input channel for those variables, while EATL obtains them through tests.
