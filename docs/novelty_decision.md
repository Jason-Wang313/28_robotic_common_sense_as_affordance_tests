# Novelty Decision

## Chosen Thesis
Robotic common sense should be defined as **executable affordance tests**:
an embodied agent knows that an object affords an action for a task demand only
when it can run, or cite, a cheap robot-specific test program whose observations
certify the required causal variables before the risky task action is attempted.

## Why This Is Stronger Than the Seed
The seed opposed executable affordance tests to text priors. The literature sweep
shows the sharper contribution is semantic: the paper changes what a
commonsense predicate *is*. It is not a text prior, a static affordance label, a
planner precondition, or a learned verifier. It is an executable relation among
object, robot, action, demand, and observation.

## Selected Central Mechanism
Executable Affordance Test Logic (EATL):
- Each affordance predicate has a typed micro-experiment.
- The micro-experiment returns pass, fail, or abstain with a witness trace.
- Plans may use an affordance predicate only when a witness exists for the
  current robot-object-demand tuple.
- Tests are cheap compared with task failure and are selected before the
  irreversible task action.

## Why Hostile Prior Work Does Not Already Cover It
Affordance learning predicts action effects; task-and-motion planning checks
geometric feasibility; LLM robotics scores language-conditioned skills; active
sensing estimates hidden state. EATL makes the executable test the *meaning* of
robot common sense and evaluates the point on label-preserving affordance flips,
where any name-only prior has a formal error lower bound.
