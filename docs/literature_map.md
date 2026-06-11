# Literature Map

## Field Box
Embodied common sense for robotics: methods that decide whether a physical
action is possible, safe, or useful for a robot in a partially observed world.
The box includes affordance learning, robot manipulation, task-and-motion
planning, physical world models, interactive perception, robot foundation
models, and language-conditioned embodied agents. It excludes pure text-only
commonsense benchmarks unless they explicitly support embodied decisions.

## Sweep Protocol
- Landscape sweep target: at least 1000 papers.
- Serious skim: top 300 by relevance, citation signal, recency, and curated
  hostile importance.
- Deep read subset: top 225 using title, abstract, venue, concept tags, and
  known hostile seed papers.
- Hostile prior-work set: top 100 most likely to make the thesis non-novel.
- Metadata source: OpenAlex search over 12 robotics/embodied-AI
  queries plus curated hostile seed papers.
- Query failures: - robot affordance learning manipulation page 1: HTTPError: HTTP Error 429: Too Many Requests
- embodied common sense robotics page 1: HTTPError: HTTP Error 429: Too Many Requests
- robot physical reasoning manipulation planning page 1: HTTPError: HTTP Error 429: Too Many Requests
- language model robotics affordance planning page 1: HTTPError: HTTP Error 429: Too Many Requests
- robot foundation model manipulation affordance page 1: HTTPError: HTTP Error 429: Too Many Requests
- object affordances robotics page 1: HTTPError: HTTP Error 429: Too Many Requests
- task and motion planning affordance robotics page 1: HTTPError: HTTP Error 429: Too Many Requests
- robot commonsense reasoning manipulation page 1: HTTPError: HTTP Error 429: Too Many Requests
- vision language model robotic manipulation affordance page 1: HTTPError: HTTP Error 429: Too Many Requests
- causal affordance robot learning page 1: HTTPError: HTTP Error 429: Too Many Requests
- interactive perception robot affordances page 1: HTTPError: HTTP Error 429: Too Many Requests
- robot manipulation world model physical reasoning page 1: HTTPError: HTTP Error 429: Too Many Requests

## Landscape Counts
| Theme | Count in 1000-entry matrix |
| --- | ---: |
| manipulation skill learning | 293 |
| embodied commonsense knowledge | 254 |
| affordance learning | 181 |
| planning and feasibility | 149 |
| supporting embodied AI | 82 |
| language-conditioned robotics | 26 |
| physical world models | 14 |
| interactive sensing | 1 |

## Representative High-Pressure Papers
| Rank | Title | Year | Theme | Mechanism |
| ---: | --- | ---: | --- | --- |
| 1 | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022 | affordance learning | learned action-effect affordance predictor |
| 2 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models | 2023 | language-conditioned robotics | language-conditioned scoring or plan generation |
| 3 | Reasoning About Object Affordances in a Knowledge Base Representation | 2014 | affordance learning | learned action-effect affordance predictor |
| 4 | PaLM-E: An Embodied Multimodal Language Model | 2023 | language-conditioned robotics | language-conditioned scoring or plan generation |
| 5 | Inner Monologue: Embodied Reasoning Through Planning with Language Models | 2022 | language-conditioned robotics | language-conditioned scoring or plan generation |
| 6 | Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 2022 | language-conditioned robotics | language-conditioned scoring or plan generation |
| 7 | To Afford or Not to Afford: A New Formalization of Affordances Toward Affordance-Based Robot Control | 2007 | affordance learning | learned action-effect affordance predictor |
| 8 | Learning Object Affordances: From Sensory-Motor Coordination to Imitation | 2008 | affordance learning | learned action-effect affordance predictor |
| 9 | Behavior-Grounded Representation of Tool Affordances | 2005 | affordance learning | learned action-effect affordance predictor |
| 10 | Object-Action Complexes: Grounded Abstractions of Sensory-Motor Processes | 2011 | affordance learning | learned action-effect affordance predictor |
| 11 | Code as Policies: Language Model Programs for Embodied Control | 2023 | language-conditioned robotics | language-conditioned scoring or plan generation |
| 12 | RT-1: Robotics Transformer for Real-World Control at Scale | 2022 | manipulation skill learning | large transformer policy or multimodal representation |
| 13 | CLIPort: What and Where Pathways for Robotic Manipulation | 2022 | manipulation skill learning | language-conditioned scoring or plan generation |
| 14 | The Psychology of Everyday Things | 1988 | affordance learning | learned action-effect affordance predictor |
| 15 | Large Language Models Still Can't Plan | 2023 | language-conditioned robotics | language-conditioned scoring or plan generation |
| 16 | AffordanceNet: An End-to-End Deep Learning Approach for Object Affordance Detection | 2018 | affordance learning | learned action-effect affordance predictor |
| 17 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | language-conditioned robotics | language-conditioned scoring or plan generation |
| 18 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023 | supporting embodied AI | learned representation, dataset, or planner for embodied decision making |
| 19 | Learning to Poke by Poking: Experiential Learning of Intuitive Physics | 2016 | physical world models | physical simulation or intuitive-physics estimator |
| 20 | Supersizing Self-Supervision: Learning to Grasp from 50K Tries and 700 Robot Hours | 2016 | manipulation skill learning | grasp-quality model trained from trials |

## Hidden Assumptions That May Be False
- A noun phrase is a stable proxy for the object's causal affordance variables.
- Visual form is sufficient to infer material, damage, contents, and blocked openings.
- Common sense is a prior over likely facts, not an obligation to test action preconditions.
- A failed manipulation attempt has acceptable cost.
- The same affordance predicate means the same thing for all robot hands and tools.
- Semantic plausibility and executable feasibility fail on the same examples.
- Rare counterexamples can be averaged away without changing safety conclusions.
- A planner can reuse learned skill success probabilities outside their calibration range.
- The benchmark object taxonomy contains the affordance boundary.
- Task demands such as volume, load, temperature, and required precision are fixed.
- Hidden states such as wetness, sharpness, charge, and blockage are either observable or irrelevant.
- Diagnostic actions are unnecessary overhead rather than part of rational embodied cognition.
- Language supervision captures negative physical evidence.
- A simulator's object label corresponds to a real object's functional state.
- Robot common sense can be evaluated by answer correctness without measuring intervention cost.
- The world will not contain counterfeit, damaged, or intentionally misleading objects.
- A single scalar uncertainty estimate is enough to decide when to act.
- Offline datasets contain the causal interventions needed to distinguish lookalikes.
- Human commonsense categories transfer to robot-specific sensors and actuators.
- Affordances are static object properties rather than relations among object, action, agent, and demand.
- Checking a precondition after executing the task is equivalent to checking it before risk is incurred.
- False negatives and false positives are symmetric errors.
- Physical tests must be expensive full-task rollouts rather than cheap micro-experiments.
- A learned verifier is novel even if it only rescoring the same textual or visual prior.

## Candidate Directions That Break Assumptions
### Executable affordance-test semantics
- Broken assumption: Common sense is a text prior.
- Central mechanism: Define each commonsense predicate by a cheap action-sensor test program that produces a witness, a failure certificate, and a task-demand-specific bound.
- Assessment: Changes the central object from a fact predictor to a precondition-testing program and directly attacks label-preserving physical counterexamples.

### Affordance type system for robot skills
- Broken assumption: Skill APIs can accept semantically named objects.
- Central mechanism: Attach typed executable contracts to skill arguments and reject plans whose arguments lack test witnesses.
- Assessment: Useful, but it risks sounding like an interface layer unless backed by new test semantics.

### Counterfeit-object stress distributions
- Broken assumption: Benchmarks can preserve normal object-name correlations.
- Central mechanism: Generate label-preserving physical mutations and score planners under safety-weighted error.
- Assessment: Important evidence, but benchmark-only is forbidden unless paired with a new mechanism.

### Minimal diagnostic action selection
- Broken assumption: Diagnostic actions are overhead.
- Central mechanism: Select the cheapest micro-experiment that separates remaining affordance hypotheses.
- Assessment: Attractive extension, but alone resembles active learning unless the predicate semantics are redefined.

### Failure-certificate world models
- Broken assumption: World models should predict trajectories.
- Central mechanism: Learn structured impossibility certificates for skill preconditions.
- Assessment: Novel-ish, but too close to verification unless tests are executable and relational.


## Preliminary Conclusion
The strongest direction is **Executable affordance-test semantics**. Existing
work makes generic affordance prediction, language-conditioned planning,
task-and-motion feasibility checking, active sensing, and foundation-model
control non-novel. The remaining boundary is to define robot common sense itself
as an executable relation: an affordance predicate is not a text fact or a
static classifier output, but a small robot-test program whose witness is
conditioned on the robot, object, action, and task demand.
