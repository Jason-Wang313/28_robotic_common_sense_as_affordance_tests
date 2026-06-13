# Submission Attack Log

Updated: 2026-06-13

## Attack Rounds

1. Closest-prior attack: affordance learning, interactive perception, active sensing, TAMP feasibility checks, and language-grounded robotics all cover adjacent mechanisms. Response: keep novelty to executable witness semantics for embodied common-sense predicates.
2. Formality attack: the lower bound is simple and label-only. Response: present it as a narrow impossibility for same-label affordance flips, not a broad theorem about all perception systems.
3. Evidence attack: the main results are synthetic with hand-written tests. Response: keep the claim mechanism-level and workshop-only.
4. Test-harm attack: executable tests may be costly, damaging, or unsafe. Response: add v2 test-cost stress.
5. Artifact attack: v1 kept `paper/main.pdf` locally and recorded stale Desktop-copy status. Response: add a build script that copies only to Downloads and removes the local PDF.

## V2 Outcome

The paper remains workshop-only / strong-revise. EATL sharply reduces unsafe false positives under hidden affordance flips, but v2 shows the mechanism is justified only when diagnostic tests are cheap and safe enough. At normalized test-harm weight 1.25, EATL loses to the text prior in the label-preserving flip regime on safety-plus-test-cost.
