# Experiment Rigor Checklist

- [x] Main synthetic environment is `experiments/affordance_tests.py`.
- [x] Main run uses 1000 episodes and 180000 method-task rows.
- [x] Regimes include typical, label-preserving flips, label swaps, and mixed cases.
- [x] Baselines include text prior, passive vision proxy, and EATL.
- [x] Primary safety metric includes unsafe false positives.
- [x] V2 test-cost stress attacks the cheap/safe-probe assumption.
- [x] Negative boundary is explicit: at test-harm weight 1.25, EATL loses to the text prior under label-preserving flips on safety-plus-test-cost.
- [ ] No real robot validation.
- [ ] No high-fidelity physics simulator.
- [ ] No learned or synthesized tests.
- [ ] No risk-aware active test-selection policy.

Decision: mechanism evidence only; terminal state is workshop-only / strong-revise.
