# Hostile Prior Work

These are the 100 papers most likely to make the proposed thesis look non-novel. The extraction is abstract/metadata based for the large sweep; curated entries use known paper-level context.

## 1. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (2022)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the robot does not need to spend action budget on diagnostic tests
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions

## 2. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips

## 3. Reasoning About Object Affordances in a Knowledge Base Representation (2014)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: material parameters
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: cost-aware selection among micro-experiments

## 4. PaLM-E: An Embodied Multimodal Language Model (2023)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: training labels encode the same affordance boundary needed at deployment
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips

## 5. Inner Monologue: Embodied Reasoning Through Planning with Language Models (2022)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: auditable failure certificates for rejected actions

## 6. Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents (2022)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: training labels encode the same affordance boundary needed at deployment
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: auditable failure certificates for rejected actions

## 7. To Afford or Not to Afford: A New Formalization of Affordances Toward Affordance-Based Robot Control (2007)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: failure costs are low enough to learn from direct task execution
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties

## 8. Learning Object Affordances: From Sensory-Motor Coordination to Imitation (2008)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: material parameters
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense

## 9. Behavior-Grounded Representation of Tool Affordances (2005)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips

## 10. Object-Action Complexes: Grounded Abstractions of Sensory-Motor Processes (2011)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the robot does not need to spend action budget on diagnostic tests
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties

## 11. Code as Policies: Language Model Programs for Embodied Control (2023)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips

## 12. RT-1: Robotics Transformer for Real-World Control at Scale (2022)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: large transformer policy or multimodal representation
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: operational tests that define the predicate before task execution

## 13. CLIPort: What and Where Pathways for Robotic Manipulation (2022)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: cost-aware selection among micro-experiments

## 14. The Psychology of Everyday Things (1988)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the robot does not need to spend action budget on diagnostic tests
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution

## 15. Large Language Models Still Can't Plan (2023)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: failure costs are low enough to learn from direct task execution
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips

## 16. AffordanceNet: An End-to-End Deep Learning Approach for Object Affordance Detection (2018)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: failure costs are low enough to learn from direct task execution
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions

## 17. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (2023)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: failure costs are low enough to learn from direct task execution
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: cost-aware selection among micro-experiments

## 18. Open X-Embodiment: Robotic Learning Datasets and RT-X Models (2023)
- Problem claimed: improve embodied-agent behavior under partial physical information
- Actual mechanism introduced: learned representation, dataset, or planner for embodied decision making
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes broad embodied AI benchmarking or representation learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties

## 19. Learning to Poke by Poking: Experiential Learning of Intuitive Physics (2016)
- Problem claimed: reason about object dynamics and material constraints
- Actual mechanism introduced: physical simulation or intuitive-physics estimator
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes predictive physical simulation or learned dynamics non-novel
- What it leaves open: operational tests that define the predicate before task execution

## 20. Supersizing Self-Supervision: Learning to Grasp from 50K Tries and 700 Robot Hours (2016)
- Problem claimed: choose reliable contact and grasp actions under partial perception
- Actual mechanism introduced: grasp-quality model trained from trials
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense

## 21. The Ecological Approach to Visual Perception (1979)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties

## 22. Learning Human Activities and Object Affordances from RGB-D Videos (2013)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties

## 23. Affordance Detection of Tool Parts from Geometric Features (2015)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions

## 24. PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning (2020)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: cost-aware selection among micro-experiments

## 25. Learning About Objects Through Action: Initial Steps Towards Artificial Cognition (2003)
- Problem claimed: improve embodied-agent behavior under partial physical information
- Actual mechanism introduced: learned representation, dataset, or planner for embodied decision making
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes broad embodied AI benchmarking or representation learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties

## 26. World Models (2018)
- Problem claimed: predict physical consequences before acting
- Actual mechanism introduced: predictive latent dynamics model
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes predictive physical simulation or learned dynamics non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips

## 27. Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning (2015)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: material parameters
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: cost-aware selection among micro-experiments

## 28. Developing Intelligent Robots that Grasp Affordance (2022)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.3389/frobt.2022.951293

## 29. Task-Oriented Robot Cognitive Manipulation Planning Using Affordance Segmentation and Logic Reasoning (2024)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1109/tnnls.2023.3252578

## 30. PLATO: Planning with LLMs and Affordances for Tool Manipulation (2026)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the robot does not need to spend action budget on diagnostic tests
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1007/s10846-026-02392-y

## 31. Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1007/978-3-031-72940-9_13

## 32. RLAfford: End-to-End Affordance Learning for Robotic Manipulation (2023)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the robot does not need to spend action budget on diagnostic tests
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1109/icra48891.2023.10161571

## 33. TARS: Tactile Affordance in Robot Synesthesia for Dexterous Manipulation (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1109/lra.2024.3505783

## 34. Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks* (2024)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the robot does not need to spend action budget on diagnostic tests
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1109/icarm62033.2024.10715821

## 35. An Affordance Keypoint Detection Network for Robot Manipulation (2021)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/lra.2021.3062560

## 36. Learning Affordance Space in Physical World for Vision-based Robotic Object Manipulation (2020)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: friction and contact conditions
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/icra40945.2020.9196783

## 37. Learning garment manipulation policies toward robot-assisted dressing (2022)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: physical simulation or intuitive-physics estimator
- Hidden assumptions: failure costs are low enough to learn from direct task execution
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes predictive physical simulation or learned dynamics non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1126/scirobotics.abm6010

## 38. Learning Affordance Segmentation for Real-World Robotic Manipulation via Synthetic Images (2019)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1109/lra.2019.2894439

## 39. Real-Time Kinematically Synchronous Planning for Cooperative Manipulation of Multi-Arms Robot Using the Self-Organizing Competitive Neural Network (2023)
- Problem claimed: supply commonsense knowledge for embodied decision making
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: material parameters
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.3390/s23115120

## 40. Interactive Open-Ended Object, Affordance and Grasp Learning for Robotic Manipulation (2019)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/icra.2019.8794184

## 41. Learning 2D Invariant Affordance Knowledge for 3D Affordance Grounding (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1609/aaai.v39i3.32318

## 42. Embodied AI with Foundation Models for Mobile Service Robots: A Systematic Review (2026)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.3390/robotics15030055

## 43. Object affordance detection with boundary-preserving network for robotic manipulation tasks (2022)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1007/s00521-022-07446-4

## 44. Critical Review: Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning (2025)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: training labels encode the same affordance boundary needed at deployment
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.70777/si.v2i4.15315

## 45. Intent-driven LLM ensemble planning for flexible multi-robot manipulation (2026)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: material parameters
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.3389/frobt.2026.1727433

## 46. Toward Affordance Detection and Ranking on Novel Objects for Real-World Robotic Manipulation (2019)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1109/lra.2019.2930364

## 47. Learning relational affordance models for robots in multi-object manipulation tasks (2012)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/icra.2012.6225042

## 48. Object Pose Estimation From RGB-D Images With Affordance-Instance Segmentation Constraint for Semantic Robot Manipulation (2024)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1109/lra.2023.3333693

## 49. Sense-Making Reconsidered: Large Language Models and the Blind Spot of Embodied Cognition (2025)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.31234/osf.io/w7hg4_v1

## 50. Towards affordance detection for robot manipulation using affordance for parts and parts for affordance (2019)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.1007/s10514-018-9787-5

## 51. Variation-Robust Few-Shot 3D Affordance Segmentation for Robotic Manipulation (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the robot does not need to spend action budget on diagnostic tests
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/lra.2024.3524904

## 52. Can I Pour Into It? Robot Imagining Open Containability Affordance of Previously Unseen Objects via Physical Simulations (2021)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: material parameters
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/lra.2020.3039943

## 53. RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1109/icra55743.2025.11127525

## 54. AffPose: An Integrated RGB-Based Framework for Simultaneous Pose Estimation and Affordance Detection in Robotic Tool Manipulation (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/lra.2025.3598984

## 55. Towards zero-shot robot tool manipulation in industrial context: A modular VLM framework enhanced by multimodal affordance representation (2026)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1016/j.rcim.2025.103161

## 56. Semantic labeling of 3D point clouds with object affordance for robot manipulation (2014)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.1109/icra.2014.6907679

## 57. Me and My Robot Smiled at One Another: The Process of Socially Enacted Communicative Affordance in Human-Machine Communication (2020)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.30658/hmc.1.4

## 58. Deep learning-based robotic cloth manipulation applications: systematic review, challenges and opportunities for physical AI (2026)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: training labels encode the same affordance boundary needed at deployment
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.3389/frobt.2026.1752914

## 59. Versatile multicontact planning and control for legged loco-manipulation (2023)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: training labels encode the same affordance boundary needed at deployment
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1126/scirobotics.adg5014

## 60. UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: training labels encode the same affordance boundary needed at deployment
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1109/icra55743.2025.11128868

## 61. CORPP: Commonsense Reasoning and Probabilistic Planning, as Applied to Dialog with a Mobile Robot (2015)
- Problem claimed: supply commonsense knowledge for embodied decision making
- Actual mechanism introduced: symbolic or graph-based knowledge representation
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.1609/aaai.v29i1.9385

## 62. Affordance RAG: Hierarchical Multimodal Retrieval With Affordance-Aware Embodied Memory for Mobile Manipulation (2026)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: failure costs are low enough to learn from direct task execution
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.1109/lra.2026.3653281

## 63. Affordance-Based Grasping and Manipulation in Real World Applications (2020)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/iros45743.2020.9341482

## 64. Continuous control actions learning and adaptation for robotic manipulation through reinforcement learning (2022)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: grasp-quality model trained from trials
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: material parameters
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.1007/s10514-022-10034-z

## 65. Information-driven Affordance Discovery for Efficient Robotic Manipulation (2024)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/icra57147.2024.10611170

## 66. Robot adaptation to human physical fatigue in human–robot co-manipulation (2018)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: learned representation, dataset, or planner for embodied decision making
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1007/s10514-017-9678-1

## 67. kPAM-SC: Generalizable Manipulation Planning using KeyPoint Affordance and Shape Completion (2021)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/icra48506.2021.9561428

## 68. RoboAfford: A Dataset and Benchmark for Enhancing Object and Spatial Affordance Learning in Robot Manipulation (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1145/3746027.3758209

## 69. Safe robot affordance-based grasping and handover for Human-Robot assistive applications (2024)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: the set of available diagnostic actions
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.1109/iecon55916.2024.10905268

## 70. Modeling, learning, perception, and control methods for deformable object manipulation (2021)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: learned representation, dataset, or planner for embodied decision making
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1126/scirobotics.abd8803

## 71. From Nano Robotic Manipulation to Nano Manipulation Robot (2025)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: visual detector or segmentation model
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1002/smb2.12021

## 72. A4T: Hierarchical Affordance Detection for Transparent Objects Depth Reconstruction and Manipulation (2022)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/lra.2022.3191231

## 73. Sim-to-Real Surgical Robot Learning and Autonomous Planning for Internal Tissue Points Manipulation Using Reinforcement Learning (2023)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1109/lra.2023.3254860

## 74. Robject: Embodied Robotics for Enhanced Domestic Interaction (2025)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.20944/preprints202506.1042.v1

## 75. Implicit instruction reasoning by fine-tuning VLM for robotic manipulation (2026)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes text-conditioned planning and language-affordance scoring non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1108/ir-05-2025-0175

## 76. Human-robot collaborative manipulation planning using early prediction of human motion (2013)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/iros.2013.6696368

## 77. Real-time Grasp Affordance Detection of Unknown Object for Robot-Human Interaction (2019)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1109/smc.2019.8914202

## 78. Tool use and affordance: Manipulation-based versus reasoning-based approaches. (2016)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1037/rev0000027

## 79. TacGNN: Learning Tactile-Based In-Hand Manipulation With a Blind Robot Using Hierarchical Graph Neural Network (2023)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: interactive contact probe and sensor classifier
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: planner accepts a semantically plausible but physically impossible step
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/lra.2023.3264759

## 80. AdaAfford: Learning to Adapt Manipulation Affordance for 3D Articulated Objects via Few-Shot Interactions (2022)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: task demand outside the training range
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1007/978-3-031-19818-2_6

## 81. Affordance Reasoning-based Sequence Planning Manner for Human-robot Collaborative Disassembly (2024)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.3901/jme.2024.17.297

## 82. On deformable object handling: Model-based motion planning for human-robot co-manipulation (2022)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: friction and contact conditions
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1016/j.cirp.2022.04.048

## 83. Affordance-Based Human–Robot Interaction With Reinforcement Learning (2023)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: friction and contact conditions
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1109/access.2023.3262450

## 84. CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks (2022)
- Problem claimed: ground linguistic or text-derived priors in robot actions
- Actual mechanism introduced: language-conditioned scoring or plan generation
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: friction and contact conditions
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/lra.2022.3180108

## 85. One-shot 3D Affordance Learning for Multi-stage Robotic Manipulation (2026)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/access.2026.3681732

## 86. Embodied Spatial Affordance: Spatial-Aware Affordance Learning for Embodied Navigation and Manipulation (2026)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: a static dataset contains the relevant rare counterexamples
- Variables treated as fixed: material parameters
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/tip.2026.3698366

## 87. Hierarchical Generation of Robot Programs Based on the Integration of Visual Affordance Recognition and Language Model (2026)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: failure costs are low enough to learn from direct task execution
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.5220/0014291700004084

## 88. Enabling Affordance-Guided Grasp Synthesis for Robotic Manipulation (2020)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: load, volume, temperature, and other task demands
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: cost-aware selection among micro-experiments
- URL: https://doi.org/10.1007/978-981-15-2414-1_35

## 89. Survey of learning-based approaches for robotic in-hand manipulation (2024)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: grasp-quality model trained from trials
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: false positive that causes spill, drop, breakage, or collision
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.3389/frobt.2024.1455431

## 90. RobotGPT: Robot Manipulation Learning From ChatGPT (2024)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: learned representation, dataset, or planner for embodied decision making
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: distribution of counterfeit or unusual objects
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/lra.2024.3357432

## 91. Global Manipulation Planning in Robot Joint Space With Task Constraints (2010)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: object damage such as holes, cracks, dull edges, and blocked openings
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/tro.2010.2044949

## 92. Affordance-based altruistic robotic architecture for human–robot collaboration (2019)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: visual appearance exposes the variables needed for safe action
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: diagnostic action changes the object state or consumes scarce resources
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1177/1059712318824697

## 93. Embodied Intelligence in Soft Robotics Through Hardware Multifunctionality (2021)
- Problem claimed: choose reliable contact and grasp actions under partial perception
- Actual mechanism introduced: grasp-quality model trained from trials
- Hidden assumptions: the environment will not include adversarially relabeled or modified artifacts
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.3389/frobt.2021.724056

## 94. Force manipulability-oriented manipulation planning for collaborative robot (2024)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: a plan-level success score is enough to expose local physical impossibility
- Variables treated as fixed: embodiment and end-effector geometry
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: formal error bounds under label-preserving affordance flips
- URL: https://doi.org/10.1108/ir-01-2024-0037

## 95. Collision-Inclusive Manipulation Planning for Occluded Object Grasping via Compliant Robot Motions (2025)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: skill preconditions are stable across materials, wear, and hidden state
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: novel object whose visible geometry is misleading
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: operational tests that define the predicate before task execution
- URL: https://doi.org/10.1109/lra.2025.3592060

## 96. Development of a Multifunctional Mobile Manipulation Robot Based on Hierarchical Motion Planning Strategy and Hybrid Grasping (2025)
- Problem claimed: connect high-level task choices to feasible robot executions
- Actual mechanism introduced: task-and-motion planner with feasibility models
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes feasibility checking inside task-and-motion planning non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.3390/robotics14070096

## 97. Learning Grasping Points for Garment Manipulation in Robot-Assisted Dressing (2020)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: grasp-quality model trained from trials
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: the mapping from words to object instances
- Failure modes ignored: rare material state dominates success but is not represented in labels
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: benchmarks where names and visual priors are decoupled from causal properties
- URL: https://doi.org/10.1109/icra40945.2020.9196994

## 98. Affordance-Based Mobile Robot Navigation Among Movable Obstacles (2020)
- Problem claimed: predict which actions an object or scene physically affords to an embodied agent
- Actual mechanism introduced: learned action-effect affordance predictor
- Hidden assumptions: training labels encode the same affordance boundary needed at deployment
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes generic affordance prediction and action-effect learning non-novel
- What it leaves open: explicit treatment of hidden physical variables as part of common sense
- URL: https://doi.org/10.1109/iros45743.2020.9341337

## 99. IMITATION LEARNING OF DUAL-ARM MANIPULATION TASKS IN HUMANOID ROBOTS (2008)
- Problem claimed: supply commonsense knowledge for embodied decision making
- Actual mechanism introduced: learned representation, dataset, or planner for embodied decision making
- Hidden assumptions: object names remain correlated with their physical affordances
- Variables treated as fixed: sensor noise and latency
- Failure modes ignored: same-named object with opposite affordance
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1142/s0219843608001431

## 100. FOTS: A Fast Optical Tactile Simulator for Sim2Real Learning of Tactile-Motor Robot Manipulation Skills (2024)
- Problem claimed: make robot manipulation robust to object and scene variation
- Actual mechanism introduced: interactive contact probe and sensor classifier
- Hidden assumptions: semantic categories can be mapped to robot-specific capabilities without recalibration
- Variables treated as fixed: cost of unsafe false positives
- Failure modes ignored: sensor probe is noisy or unavailable
- What it makes less novel: makes skill-conditioned manipulation policies non-novel
- What it leaves open: auditable failure certificates for rejected actions
- URL: https://doi.org/10.1109/lra.2024.3396665
