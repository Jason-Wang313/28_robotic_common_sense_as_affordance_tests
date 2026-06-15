# Submission Attack Log

Updated: 2026-06-15

## v3 Attack Rounds

1. Scale attack: v2 used only 1000 episodes and a compact result table.
   Response: added v3 full-scale suite with 4,977,600 aggregate method
   decisions.
2. Baseline attack: v2 compared against only text prior, passive proxy, and
   EATL.  Response: added calibrated prior, uncertainty vision, conservative
   prior, eager EATL, risk-aware EATL, cached EATL, oracle, and random-test
   negative control.
3. Cost attack: tests may be too expensive.  Response: added phase diagram over
   hidden-flip rate, test harm, and failure harm.
4. Policy attack: "run tests" is not enough.  Response: added risk-aware
   selector and ablations.
5. Cache attack: witnesses become stale.  Response: added strict, label-only,
   TTL, demand-compatible, and no-cache comparisons.
6. Noise attack: executable tests are not oracles.  Response: added probe-noise
   and guard-design sweep.
7. Strong perception attack: a VLM may see the deciding variable.  Response:
   added passive visibility ladder and explicitly narrowed the claim.
8. Demand attack: affordances are relative to task demand.  Response: added
   demand and embodiment sweeps.
9. Artifact attack: PDFs must be final-only in Downloads.  Response: final
   export is `C:/Users/wangz/Downloads/28.pdf`; local `paper/main.pdf` removed.
10. Page-depth attack: v2 was too short.  Response: final manuscript is 28 pages
    with real experiment content and appendices.

## v3 Outcome

Paper 28 is final under the current batch standard as a full-scale synthetic
mechanism paper.  It is still not a real-robot validation paper.
