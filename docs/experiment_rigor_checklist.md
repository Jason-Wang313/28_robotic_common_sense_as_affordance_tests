# Experiment Rigor Checklist

- [x] Detailed v3 execution plan written before substantive work.
- [x] New RAM-light full-scale runner added.
- [x] Main benchmark uses 20 objects, 10 predicates, 8 regimes, 10 mechanisms,
  12 seeds, and 192,000 robot-object-task cases.
- [x] Full aggregate suite contains 4,977,600 method decisions.
- [x] Baselines include text prior, calibrated prior, passive vision,
  uncertainty-aware vision, conservative prior, eager EATL, risk-aware EATL,
  cached EATL, oracle hidden state, and random-test control.
- [x] Stress tests include hidden flips, adversarial counterfeits,
  task-demand shift, embodiment shift, probe cost/failure harm phase diagrams,
  selector ablations, cache validity, probe noise, visibility ladders, and
  failure galleries.
- [x] Results report unsafe false positives, accuracy, abstention, test cost,
  total cost, and failure modes.
- [x] Negative boundaries are explicit: text/conservative priors can dominate
  when hidden flips are rare or probes are expensive; passive full visibility
  solves the synthetic task.
- [x] Final PDF is 28 pages and exported only to Downloads.
- [ ] No real robot validation.
- [ ] No high-fidelity physics simulator.
- [ ] No learned or synthesized tests.

Decision: final full-scale synthetic mechanism paper; strong-revise for any
venue that requires real-robot validation.
