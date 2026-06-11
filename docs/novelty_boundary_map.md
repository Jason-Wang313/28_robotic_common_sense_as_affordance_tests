# Novelty Boundary Map

| Boundary | Closest hostile work | What is already covered | Remaining claim boundary |
| --- | --- | --- | --- |
| Classical affordance theory and robot affordance learning | Gibson, Sahin et al., Montesano et al., Stoytchev, Kruger et al. | Affordances are relations among actors, actions, and environments; robots can learn action-effect models. | They usually learn or represent affordance predicates. This paper makes the predicate definition itself an executable test with a witness and safety-weighted semantics. |
| Visual affordance detection | AffordanceNet, tool-part affordance detection, RGB-D activity-affordance models | Perception can predict functional regions and likely object uses. | A visual affordance label is not accepted as common sense unless a task-demand-specific test program can certify it. |
| Task-and-motion planning feasibility | PDDLStream, logic-geometric programming, TAMP surveys | Symbolic actions need continuous feasibility checks and samplers. | TAMP checks action feasibility for planning; the proposed mechanism defines commonsense predicates as cheap pre-task affordance experiments, including failures induced by names and hidden physical state. |
| LLM robotics and language-affordance grounding | SayCan, Inner Monologue, Code as Policies, VoxPoser, PaLM-E, RT-2 | Text/world knowledge can guide robot action choice when grounded by skill scores or perception. | The paper's hostile distribution breaks name-affordance correlations. Text priors become the object of critique, not the mechanism. |
| Interactive perception and active sensing | Learning through action, tactile probing, poking, self-supervised grasp learning | Robots can learn hidden properties by acting. | The novelty is not merely acting to reduce uncertainty; it is using executable tests as the semantics of common-sense claims, with theorem and safety-cost evaluation for label-preserving affordance flips. |
| World models and physical prediction | World Models, intuitive physics, robot dynamics models | Predict future observations or trajectories from latent state. | The mechanism is predicate-level test certification, not full trajectory prediction. |

## Non-Novel Moves Rejected
- Bigger model: rejected because the failure mode is invariant to model size when
  the input variable is only a label with flipped hidden affordance.
- Better data: rejected because the proposed distribution intentionally creates
  same-label counterexamples after training.
- New benchmark only: rejected unless paired with the executable-test mechanism.
- Add uncertainty: rejected because scalar uncertainty does not define what
  physical evidence would make a commonsense predicate true.
- Add active learning: rejected because the selected mechanism is not generic
  information gathering; it is operational predicate semantics.
- Add verifier: rejected because the tests produce physical witnesses before
  task execution, rather than rescoring a pre-existing plan.
- Combine modules or use an LLM planner: rejected as central mechanisms.
- Reinforcement learning: not used.
