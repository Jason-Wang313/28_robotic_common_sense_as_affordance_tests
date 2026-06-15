"""Full-scale v3 executable-affordance-test experiments for Paper 28.

The runner is deliberately RAM-light. It streams only bounded example rows and
keeps aggregate counters for the large sweeps. The goal is not a real-robot
claim; it is a controlled stress test of when executable affordance witnesses
beat, tie, or lose to name priors and passive perceptual proxies.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import statistics
import time
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
FIGS = ROOT / "figures" / "full_scale"
PAPER = ROOT / "paper"
for path in [RESULTS, FIGS, PAPER]:
    path.mkdir(parents=True, exist_ok=True)


TASKS = [
    "contain_liquid",
    "lift",
    "support_load",
    "cut_soft_food",
    "wipe_spill",
    "carry_hot",
    "pour_without_spill",
    "stack_safely",
    "push_without_sliding",
    "grasp_without_crushing",
]


REGIMES = [
    "typical",
    "label_preserving_flips",
    "label_swap",
    "mixed",
    "adversarial_counterfeit",
    "degraded_worn",
    "task_demand_shift",
    "embodiment_shift",
]


METHODS = [
    "text_prior",
    "calibrated_text_prior",
    "passive_vision_proxy",
    "uncertainty_vision_proxy",
    "conservative_prior",
    "eager_eatl",
    "risk_aware_eatl",
    "cached_eatl",
    "oracle_hidden_state",
    "random_test_control",
]

MAIN_SEEDS = list(range(28001, 28013))
MAIN_EPISODES = 10
PHASE_SEEDS = list(range(28101, 28105))
PHASE_EPISODES = 3
ABLATION_SEEDS = list(range(28201, 28209))
ABLATION_EPISODES = 8
CACHE_SEEDS = list(range(28301, 28309))
CACHE_STEPS = 30
NOISE_SEEDS = list(range(28401, 28407))
NOISE_EPISODES = 6
VISIBILITY_SEEDS = list(range(28501, 28507))
VISIBILITY_EPISODES = 8
DEMAND_SEEDS = list(range(28601, 28607))
DEMAND_EPISODES = 10


@dataclass(frozen=True)
class Obj:
    label: str
    concave: bool
    porous: bool
    has_hole: bool
    capacity_ml: int
    mass_g: int
    friction: float
    load_capacity_g: int
    sharpness: float
    edge_stiffness: float
    absorbency_ml: int
    heat_resistant: bool
    has_handle: bool
    stable_base: bool
    flat_top: bool
    pour_lip: bool
    crush_limit_n: float
    grippable: bool
    surface_fragility: float
    wet: bool = False


@dataclass(frozen=True)
class Robot:
    name: str
    gripper_limit_g: int
    min_friction: float
    max_contact_force_n: float
    heat_tolerance_c: int
    sensor_quality: float
    dexterity: float


@dataclass(frozen=True)
class Demand:
    volume_ml: int = 200
    gripper_limit_g: int = 900
    load_g: int = 1000
    required_sharpness: float = 0.55
    required_stiffness: float = 0.45
    spill_ml: int = 60
    temperature_c: int = 85
    stack_load_g: int = 600
    push_force_n: float = 8.0
    grip_force_n: float = 18.0


@dataclass
class Case:
    seed: int
    regime: str
    episode: int
    obj: Obj
    task: str
    demand: Demand
    robot: Robot
    hidden_flip_rate: float = 0.0
    failure_harm: float = 5.0
    test_harm_weight: float = 0.75
    sensor_noise: float = 0.03


@dataclass
class Decision:
    value: Optional[bool]
    test_cost: float = 0.0
    tests_used: int = 0
    witness: str = ""
    stale_reuse: bool = False
    dominated: bool = False


STANDARD_ROBOT = Robot("standard_parallel_jaw", 900, 0.50, 25.0, 90, 0.97, 0.75)
WEAK_ROBOT = Robot("weak_slippery_gripper", 650, 0.62, 16.0, 70, 0.93, 0.55)
PRECISE_ROBOT = Robot("precise_soft_gripper", 700, 0.48, 11.0, 80, 0.985, 0.90)
BASE_DEMAND = Demand()


CATALOG: Dict[str, Obj] = {
    "mug": Obj("mug", True, False, False, 350, 320, 0.72, 900, 0.03, 0.30, 5, True, True, True, False, True, 42, True, 0.10),
    "bowl": Obj("bowl", True, False, False, 500, 420, 0.66, 1200, 0.02, 0.20, 10, True, False, True, False, False, 50, True, 0.12),
    "sieve": Obj("sieve", True, True, True, 450, 180, 0.61, 300, 0.02, 0.15, 20, True, False, True, False, False, 32, True, 0.20),
    "knife": Obj("knife", False, False, False, 0, 150, 0.58, 80, 0.94, 0.88, 0, True, True, False, False, False, 70, True, 0.35),
    "spoon": Obj("spoon", True, False, False, 20, 80, 0.55, 40, 0.07, 0.55, 0, True, True, False, False, True, 40, True, 0.10),
    "sponge": Obj("sponge", False, True, False, 40, 30, 0.80, 80, 0.01, 0.04, 160, False, False, True, False, False, 9, True, 0.75),
    "brick": Obj("brick", False, False, False, 0, 1800, 0.90, 6000, 0.01, 0.95, 5, True, False, True, True, False, 250, True, 0.05),
    "cardboard_box": Obj("cardboard_box", True, True, False, 800, 220, 0.70, 1500, 0.02, 0.35, 80, False, False, True, True, False, 20, True, 0.55),
    "plastic_tray": Obj("plastic_tray", True, False, False, 250, 160, 0.63, 700, 0.02, 0.50, 3, False, False, True, True, True, 25, True, 0.45),
    "glass": Obj("glass", True, False, False, 280, 260, 0.45, 600, 0.03, 0.40, 0, False, False, True, False, True, 18, True, 0.90),
    "thermos": Obj("thermos", True, False, False, 600, 520, 0.68, 900, 0.02, 0.55, 0, True, True, True, False, True, 55, True, 0.20),
    "paper_cup": Obj("paper_cup", True, True, False, 250, 18, 0.50, 120, 0.01, 0.10, 40, False, False, True, False, True, 7, True, 0.85),
    "ceramic_plate": Obj("ceramic_plate", False, False, False, 30, 410, 0.48, 700, 0.02, 0.50, 0, True, False, True, True, False, 22, True, 0.80),
    "towel": Obj("towel", False, True, False, 60, 140, 0.75, 60, 0.01, 0.05, 220, False, False, False, False, False, 8, True, 0.60),
    "wooden_block": Obj("wooden_block", False, False, False, 0, 640, 0.82, 2800, 0.01, 0.70, 10, False, False, True, True, False, 80, True, 0.08),
    "foam_block": Obj("foam_block", False, True, False, 0, 90, 0.70, 260, 0.01, 0.08, 30, False, False, True, True, False, 6, True, 0.70),
    "metal_pan": Obj("metal_pan", True, False, False, 700, 780, 0.64, 1800, 0.02, 0.75, 0, True, True, True, False, True, 95, True, 0.25),
    "silicone_mat": Obj("silicone_mat", False, False, False, 0, 120, 0.95, 500, 0.01, 0.12, 5, True, False, False, True, False, 12, True, 0.30),
    "mesh_bag": Obj("mesh_bag", True, True, True, 300, 65, 0.56, 240, 0.01, 0.08, 45, False, True, False, False, False, 10, True, 0.65),
    "rubber_grip_pad": Obj("rubber_grip_pad", False, False, False, 0, 70, 0.98, 350, 0.01, 0.18, 0, True, False, True, True, False, 15, True, 0.35),
}


def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def stable_seed(*parts: object) -> int:
    payload = "|".join(str(p) for p in parts)
    return int(hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12], 16)


def jitter_int(x: int, rng: random.Random, frac: float, lo: int = 0) -> int:
    return max(lo, int(round(x * rng.uniform(1.0 - frac, 1.0 + frac))))


def truth(obj: Obj, task: str, demand: Demand, robot: Robot) -> bool:
    gripper_limit = min(demand.gripper_limit_g, robot.gripper_limit_g)
    if task == "contain_liquid":
        return obj.concave and not obj.porous and not obj.has_hole and obj.capacity_ml >= demand.volume_ml and obj.stable_base
    if task == "lift":
        return obj.mass_g <= gripper_limit and obj.friction >= robot.min_friction and obj.grippable
    if task == "support_load":
        return obj.load_capacity_g >= demand.load_g and obj.stable_base and obj.flat_top
    if task == "cut_soft_food":
        return obj.sharpness >= demand.required_sharpness and obj.edge_stiffness >= demand.required_stiffness
    if task == "wipe_spill":
        return obj.absorbency_ml >= demand.spill_ml and obj.mass_g <= 600 and not obj.has_hole
    if task == "carry_hot":
        return obj.heat_resistant and obj.has_handle and obj.mass_g <= gripper_limit and robot.heat_tolerance_c >= demand.temperature_c
    if task == "pour_without_spill":
        return (
            obj.concave
            and obj.pour_lip
            and not obj.porous
            and not obj.has_hole
            and obj.capacity_ml >= demand.volume_ml
            and obj.stable_base
            and obj.friction >= robot.min_friction
        )
    if task == "stack_safely":
        return obj.flat_top and obj.stable_base and obj.load_capacity_g >= demand.stack_load_g and obj.friction >= 0.55
    if task == "push_without_sliding":
        return obj.mass_g <= 1400 and obj.friction >= 0.60 and obj.surface_fragility < 0.65 and demand.push_force_n <= robot.max_contact_force_n
    if task == "grasp_without_crushing":
        return obj.grippable and obj.mass_g <= gripper_limit and obj.crush_limit_n >= demand.grip_force_n and obj.surface_fragility < 0.82
    raise ValueError(task)


TEXT_PRIOR: Dict[str, Dict[str, bool]] = {
    label: {task: truth(obj, task, BASE_DEMAND, STANDARD_ROBOT) for task in TASKS}
    for label, obj in CATALOG.items()
}


def label_score(label: str, task: str) -> float:
    return 0.88 if TEXT_PRIOR[label][task] else 0.12


def make_demand(regime: str, rng: random.Random, task: str) -> Demand:
    d = BASE_DEMAND
    if regime != "task_demand_shift":
        return d
    if task in {"contain_liquid", "pour_without_spill"}:
        return replace(d, volume_ml=rng.choice([100, 200, 350, 500, 750]))
    if task == "lift":
        return replace(d, gripper_limit_g=rng.choice([450, 650, 900, 1200]))
    if task == "support_load":
        return replace(d, load_g=rng.choice([300, 700, 1000, 1600, 2500]))
    if task == "cut_soft_food":
        return replace(d, required_sharpness=rng.choice([0.25, 0.45, 0.65, 0.85]))
    if task == "wipe_spill":
        return replace(d, spill_ml=rng.choice([20, 60, 120, 200]))
    if task == "carry_hot":
        return replace(d, temperature_c=rng.choice([50, 70, 85, 100, 120]))
    if task == "stack_safely":
        return replace(d, stack_load_g=rng.choice([200, 600, 1200, 2000]))
    if task == "push_without_sliding":
        return replace(d, push_force_n=rng.choice([4.0, 8.0, 14.0, 22.0]))
    if task == "grasp_without_crushing":
        return replace(d, grip_force_n=rng.choice([6.0, 12.0, 18.0, 28.0, 40.0]))
    return d


def make_robot(regime: str, rng: random.Random) -> Robot:
    if regime == "embodiment_shift":
        return rng.choice([WEAK_ROBOT, PRECISE_ROBOT, STANDARD_ROBOT])
    return STANDARD_ROBOT


def apply_hidden_flip(obj: Obj, rng: random.Random) -> Obj:
    choices: List[Callable[[Obj], Obj]] = [
        lambda o: replace(o, has_hole=True, capacity_ml=max(o.capacity_ml, 250), concave=True),
        lambda o: replace(o, porous=True),
        lambda o: replace(o, sharpness=min(o.sharpness, 0.10), edge_stiffness=min(o.edge_stiffness, 0.20)),
        lambda o: replace(o, mass_g=max(o.mass_g, 1250), friction=min(o.friction, 0.38)),
        lambda o: replace(o, load_capacity_g=min(o.load_capacity_g, 280), flat_top=False),
        lambda o: replace(o, heat_resistant=False, has_handle=False),
        lambda o: replace(o, absorbency_ml=0, porous=False),
        lambda o: replace(o, pour_lip=False, friction=min(o.friction, 0.44)),
        lambda o: replace(o, crush_limit_n=min(o.crush_limit_n, 6.0), surface_fragility=max(o.surface_fragility, 0.90)),
        lambda o: replace(o, stable_base=False, wet=True, friction=min(o.friction, 0.42)),
    ]
    for fn in rng.sample(choices, rng.randint(1, 4)):
        obj = fn(obj)
    return obj


def adversarial_counterfeit(obj: Obj, rng: random.Random) -> Obj:
    positive_tasks = [task for task, val in TEXT_PRIOR[obj.label].items() if val]
    if not positive_tasks:
        return apply_hidden_flip(obj, rng)
    task = rng.choice(positive_tasks)
    if task in {"contain_liquid", "pour_without_spill"}:
        return replace(obj, has_hole=True, porous=True, capacity_ml=max(obj.capacity_ml, 250), concave=True)
    if task == "lift":
        return replace(obj, mass_g=max(1300, obj.mass_g), friction=min(0.35, obj.friction))
    if task in {"support_load", "stack_safely"}:
        return replace(obj, load_capacity_g=min(250, obj.load_capacity_g), flat_top=False, stable_base=False)
    if task == "cut_soft_food":
        return replace(obj, sharpness=0.05, edge_stiffness=0.12)
    if task == "wipe_spill":
        return replace(obj, absorbency_ml=0, porous=False)
    if task == "carry_hot":
        return replace(obj, heat_resistant=False, has_handle=False)
    if task == "push_without_sliding":
        return replace(obj, friction=0.35, surface_fragility=0.90)
    if task == "grasp_without_crushing":
        return replace(obj, crush_limit_n=5.0, surface_fragility=0.95)
    return apply_hidden_flip(obj, rng)


def degrade(obj: Obj, rng: random.Random) -> Obj:
    return replace(
        obj,
        friction=clamp(obj.friction - rng.uniform(0.05, 0.30), 0.10, 1.0),
        load_capacity_g=max(20, int(obj.load_capacity_g * rng.uniform(0.20, 0.85))),
        sharpness=clamp(obj.sharpness * rng.uniform(0.10, 0.75), 0.0, 1.0),
        edge_stiffness=clamp(obj.edge_stiffness * rng.uniform(0.35, 0.95), 0.0, 1.0),
        absorbency_ml=max(0, int(obj.absorbency_ml * rng.uniform(0.0, 0.75))),
        heat_resistant=obj.heat_resistant and rng.random() > 0.35,
        stable_base=obj.stable_base and rng.random() > 0.18,
        crush_limit_n=max(2.0, obj.crush_limit_n * rng.uniform(0.35, 0.90)),
        wet=rng.random() < 0.35,
    )


def mutate(obj: Obj, rng: random.Random, regime: str, hidden_flip_rate: Optional[float] = None) -> Obj:
    obj = replace(
        obj,
        mass_g=jitter_int(obj.mass_g, rng, 0.08, 5),
        capacity_ml=jitter_int(obj.capacity_ml, rng, 0.08, 0),
        friction=clamp(obj.friction + rng.uniform(-0.035, 0.035), 0.10, 1.0),
    )
    if hidden_flip_rate is not None:
        return apply_hidden_flip(obj, rng) if rng.random() < hidden_flip_rate else obj
    if regime == "typical":
        return obj
    if regime == "label_preserving_flips":
        return apply_hidden_flip(obj, rng)
    if regime == "label_swap":
        donor = rng.choice(list(CATALOG.values()))
        return replace(donor, label=obj.label)
    if regime == "mixed":
        return mutate(obj, rng, rng.choice(["typical", "label_preserving_flips", "label_swap"]))
    if regime == "adversarial_counterfeit":
        return adversarial_counterfeit(obj, rng)
    if regime == "degraded_worn":
        return degrade(obj, rng)
    if regime == "task_demand_shift":
        return obj
    if regime == "embodiment_shift":
        return obj
    raise ValueError(regime)


def demand_signature(d: Demand) -> str:
    return ",".join(str(v) for v in asdict(d).values())


def state_signature(obj: Obj, demand: Demand, robot: Robot, strict: bool = True) -> str:
    if strict:
        payload = json.dumps({"obj": asdict(obj), "demand": asdict(demand), "robot": asdict(robot)}, sort_keys=True)
    else:
        payload = json.dumps({"label": obj.label, "demand": demand_signature(demand), "robot": robot.name}, sort_keys=True)
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


def base_test_cost(task: str, demand: Demand) -> float:
    costs = {
        "contain_liquid": 0.10,
        "lift": 0.08,
        "support_load": 0.13,
        "cut_soft_food": 0.12,
        "wipe_spill": 0.07,
        "carry_hot": 0.10,
        "pour_without_spill": 0.12,
        "stack_safely": 0.11,
        "push_without_sliding": 0.09,
        "grasp_without_crushing": 0.10,
    }
    scale = 1.0
    if task in {"contain_liquid", "pour_without_spill"}:
        scale += max(0, demand.volume_ml - 200) / 2000
    elif task in {"support_load", "stack_safely"}:
        scale += max(0, demand.load_g - 1000) / 6000
    elif task == "carry_hot":
        scale += max(0, demand.temperature_c - 85) / 500
    elif task == "grasp_without_crushing":
        scale += max(0, demand.grip_force_n - 18) / 200
    return costs[task] * scale


def witness_text(obj: Obj, task: str, demand: Demand, robot: Robot) -> str:
    if task == "contain_liquid":
        return f"pour_probe(volume={demand.volume_ml}, hole={obj.has_hole}, porous={obj.porous}, stable={obj.stable_base})"
    if task == "lift":
        return f"trial_lift(mass={obj.mass_g}, limit={min(demand.gripper_limit_g, robot.gripper_limit_g)}, friction={obj.friction:.2f})"
    if task == "support_load":
        return f"load_probe(load={demand.load_g}, capacity={obj.load_capacity_g}, flat={obj.flat_top})"
    if task == "cut_soft_food":
        return f"edge_probe(sharpness={obj.sharpness:.2f}, stiffness={obj.edge_stiffness:.2f})"
    if task == "wipe_spill":
        return f"absorb_probe(spill={demand.spill_ml}, absorbency={obj.absorbency_ml})"
    if task == "carry_hot":
        return f"thermal_probe(temp={demand.temperature_c}, resistant={obj.heat_resistant}, handle={obj.has_handle})"
    if task == "pour_without_spill":
        return f"pour_control_probe(lip={obj.pour_lip}, friction={obj.friction:.2f}, hole={obj.has_hole})"
    if task == "stack_safely":
        return f"stack_probe(load={demand.stack_load_g}, flat={obj.flat_top}, stable={obj.stable_base})"
    if task == "push_without_sliding":
        return f"push_probe(force={demand.push_force_n:.1f}, friction={obj.friction:.2f}, fragile={obj.surface_fragility:.2f})"
    if task == "grasp_without_crushing":
        return f"grip_probe(force={demand.grip_force_n:.1f}, crush_limit={obj.crush_limit_n:.1f})"
    return "unknown_probe"


def noisy_test(case: Case, rng: random.Random, noise: Optional[float] = None, repeats: int = 1) -> Decision:
    p = case.sensor_noise if noise is None else noise
    y = truth(case.obj, case.task, case.demand, case.robot)
    votes = 0
    for _ in range(repeats):
        obs = y
        effective_noise = clamp(p * (1.0 + (1.0 - case.robot.sensor_quality)), 0.0, 0.45)
        if rng.random() < effective_noise:
            obs = not obs
        votes += 1 if obs else -1
    pred = votes >= 0
    return Decision(pred, base_test_cost(case.task, case.demand) * repeats, repeats, witness_text(case.obj, case.task, case.demand, case.robot))


def visible_score(case: Case, visibility: str, rng: random.Random) -> float:
    obj, task, demand, robot = case.obj, case.task, case.demand, case.robot
    score = 0.5
    if task == "contain_liquid":
        score = 0.85 if obj.concave and obj.capacity_ml >= demand.volume_ml and obj.stable_base else 0.18
        if visibility in {"geometry_material", "geometry_damage", "full_noisy"} and obj.porous:
            score -= 0.35
        if visibility in {"geometry_damage", "full_noisy"} and obj.has_hole:
            score -= 0.40
    elif task == "lift":
        score = 0.82 if obj.mass_g <= min(demand.gripper_limit_g, robot.gripper_limit_g) and obj.grippable else 0.22
        if visibility in {"geometry_material", "full_noisy"} and obj.friction < robot.min_friction:
            score -= 0.30
    elif task == "support_load":
        score = 0.78 if obj.flat_top and obj.stable_base else 0.20
        if visibility in {"geometry_material", "full_noisy"} and obj.load_capacity_g < demand.load_g:
            score -= 0.35
    elif task == "cut_soft_food":
        score = 0.74 if obj.edge_stiffness >= demand.required_stiffness else 0.22
        if visibility in {"geometry_damage", "full_noisy"} and obj.sharpness < demand.required_sharpness:
            score -= 0.35
    elif task == "wipe_spill":
        score = 0.80 if obj.porous else 0.20
        if visibility in {"geometry_material", "full_noisy"} and obj.absorbency_ml < demand.spill_ml:
            score -= 0.35
    elif task == "carry_hot":
        score = 0.80 if obj.has_handle else 0.18
        if visibility in {"geometry_material", "full_noisy"} and not obj.heat_resistant:
            score -= 0.35
    elif task == "pour_without_spill":
        score = 0.82 if obj.concave and obj.pour_lip and obj.stable_base else 0.18
        if visibility in {"geometry_material", "geometry_damage", "full_noisy"} and (obj.porous or obj.has_hole):
            score -= 0.35
    elif task == "stack_safely":
        score = 0.80 if obj.flat_top and obj.stable_base else 0.18
        if visibility in {"geometry_material", "full_noisy"} and obj.load_capacity_g < demand.stack_load_g:
            score -= 0.30
    elif task == "push_without_sliding":
        score = 0.78 if obj.friction >= 0.60 and obj.surface_fragility < 0.65 else 0.24
    elif task == "grasp_without_crushing":
        score = 0.78 if obj.grippable and obj.mass_g <= min(demand.gripper_limit_g, robot.gripper_limit_g) else 0.20
        if visibility in {"geometry_damage", "full_noisy"} and obj.crush_limit_n < demand.grip_force_n:
            score -= 0.35
    if visibility == "label_only":
        score = label_score(obj.label, task)
    if visibility == "vlm_blend":
        score = 0.45 * label_score(obj.label, task) + 0.55 * visible_score(case, "geometry_material", rng)
    if visibility == "full_noisy":
        score = 0.88 if truth(obj, task, demand, robot) else 0.12
        score += rng.uniform(-0.12, 0.12)
    return clamp(score + rng.uniform(-0.04, 0.04), 0.01, 0.99)


def method_text_prior(case: Case, rng: random.Random, state: dict) -> Decision:
    return Decision(TEXT_PRIOR[case.obj.label][case.task], 0.0, 0, f"text_prior(label={case.obj.label})")


def method_calibrated_text_prior(case: Case, rng: random.Random, state: dict) -> Decision:
    p = label_score(case.obj.label, case.task)
    if case.regime in {"label_preserving_flips", "adversarial_counterfeit", "degraded_worn"}:
        p = 0.65 * p + 0.35 * 0.50
    if 0.42 <= p <= 0.58:
        return Decision(None, 0.0, 0, "calibrated_text_prior(abstain)")
    return Decision(p >= 0.5, 0.0, 0, f"calibrated_text_prior(p={p:.2f})")


def method_conservative_prior(case: Case, rng: random.Random, state: dict) -> Decision:
    p = label_score(case.obj.label, case.task)
    high_consequence = case.task in {"contain_liquid", "support_load", "carry_hot", "pour_without_spill", "grasp_without_crushing"}
    if p >= 0.84 and not high_consequence:
        return Decision(True, 0.0, 0, "conservative_prior(assert_low_consequence)")
    if p <= 0.20:
        return Decision(False, 0.0, 0, "conservative_prior(reject)")
    return Decision(None, 0.0, 0, "conservative_prior(abstain)")


def method_passive_vision(case: Case, rng: random.Random, state: dict) -> Decision:
    p = visible_score(case, "geometry_only", rng)
    return Decision(p >= 0.5, 0.0, 0, f"passive_vision_proxy(p={p:.2f})")


def method_uncertainty_vision(case: Case, rng: random.Random, state: dict) -> Decision:
    p = visible_score(case, "geometry_material", rng)
    if 0.38 <= p <= 0.62:
        return Decision(None, 0.0, 0, f"uncertainty_vision_proxy(abstain,p={p:.2f})")
    return Decision(p >= 0.5, 0.0, 0, f"uncertainty_vision_proxy(p={p:.2f})")


def method_eager_eatl(case: Case, rng: random.Random, state: dict) -> Decision:
    return noisy_test(case, rng)


def method_risk_aware_eatl(case: Case, rng: random.Random, state: dict) -> Decision:
    p_label = label_score(case.obj.label, case.task)
    p_vis = visible_score(case, "geometry_material", rng)
    p = 0.42 * p_label + 0.58 * p_vis
    if case.regime in {"label_preserving_flips", "adversarial_counterfeit", "degraded_worn"}:
        p = 0.75 * p + 0.25 * 0.50
    test_cost = base_test_cost(case.task, case.demand) * case.test_harm_weight
    expected_unsafe_if_assert = (1.0 - p) * case.failure_harm
    expected_loss_if_reject = p * 0.6
    value_of_test = max(expected_unsafe_if_assert, expected_loss_if_reject) * (0.75 + abs(p - 0.5))
    if p < 0.18:
        return Decision(False, 0.0, 0, f"risk_aware_eatl(reject,p={p:.2f})")
    if value_of_test > test_cost + 0.025:
        return noisy_test(case, rng)
    if 0.35 <= p <= 0.72:
        return Decision(None, 0.0, 0, f"risk_aware_eatl(abstain,p={p:.2f},test_cost={test_cost:.3f})")
    return Decision(p >= 0.72, 0.0, 0, f"risk_aware_eatl(prior_action,p={p:.2f})")


def method_cached_eatl(case: Case, rng: random.Random, state: dict) -> Decision:
    cache = state.setdefault("cached_eatl", {})
    key = (case.obj.label, case.task, state_signature(case.obj, case.demand, case.robot, strict=True))
    if key in cache:
        pred, witness = cache[key]
        return Decision(pred, 0.0, 0, "cache_hit:" + witness)
    decision = noisy_test(case, rng)
    cache[key] = (decision.value, decision.witness)
    return decision


def method_oracle(case: Case, rng: random.Random, state: dict) -> Decision:
    return Decision(truth(case.obj, case.task, case.demand, case.robot), 0.0, 0, "oracle_hidden_state")


def method_random_control(case: Case, rng: random.Random, state: dict) -> Decision:
    return Decision(rng.random() < 0.5, base_test_cost(case.task, case.demand) * 0.65, 1, "irrelevant_random_probe")


METHOD_FN: Dict[str, Callable[[Case, random.Random, dict], Decision]] = {
    "text_prior": method_text_prior,
    "calibrated_text_prior": method_calibrated_text_prior,
    "passive_vision_proxy": method_passive_vision,
    "uncertainty_vision_proxy": method_uncertainty_vision,
    "conservative_prior": method_conservative_prior,
    "eager_eatl": method_eager_eatl,
    "risk_aware_eatl": method_risk_aware_eatl,
    "cached_eatl": method_cached_eatl,
    "oracle_hidden_state": method_oracle,
    "random_test_control": method_random_control,
}


class Counter:
    def __init__(self) -> None:
        self.n = 0
        self.correct = 0
        self.nonabstain_correct = 0
        self.nonabstain = 0
        self.tp = 0
        self.fp = 0
        self.fn = 0
        self.tn = 0
        self.abstain = 0
        self.unsafe_fp = 0
        self.avoidable_fn = 0
        self.test_cost = 0.0
        self.tests_used = 0
        self.total_cost = 0.0
        self.stale_unsafe = 0
        self.dominated = 0

    def update(self, y: bool, d: Decision, failure_harm: float = 5.0, test_harm_weight: float = 1.0) -> None:
        self.n += 1
        test_cost = d.test_cost * test_harm_weight
        self.test_cost += d.test_cost
        self.tests_used += d.tests_used
        self.total_cost += test_cost
        if d.value is None:
            self.abstain += 1
            self.total_cost += 0.15
            return
        self.nonabstain += 1
        if d.value == y:
            self.correct += 1
            self.nonabstain_correct += 1
        if d.value and y:
            self.tp += 1
        elif d.value and not y:
            self.fp += 1
            self.unsafe_fp += 1
            self.total_cost += failure_harm
            if d.stale_reuse:
                self.stale_unsafe += 1
        elif (not d.value) and y:
            self.fn += 1
            self.avoidable_fn += 1
            self.total_cost += 0.6
        else:
            self.tn += 1
        if d.dominated:
            self.dominated += 1

    def row(self, extra: Dict[str, object]) -> Dict[str, object]:
        n = self.n or 1
        precision = self.tp / (self.tp + self.fp) if self.tp + self.fp else 0.0
        recall = self.tp / (self.tp + self.fn) if self.tp + self.fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        tpr = recall
        tnr = self.tn / (self.tn + self.fp) if self.tn + self.fp else 0.0
        out = {
            **extra,
            "n": self.n,
            "accuracy": self.correct / n,
            "nonabstain_accuracy": self.nonabstain_correct / self.nonabstain if self.nonabstain else 0.0,
            "balanced_accuracy": 0.5 * (tpr + tnr),
            "unsafe_false_positive_rate": self.unsafe_fp / n,
            "avoidable_false_negative_rate": self.avoidable_fn / n,
            "abstention_rate": self.abstain / n,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "mean_test_cost": self.test_cost / n,
            "mean_tests_used": self.tests_used / n,
            "mean_total_cost": self.total_cost / n,
            "stale_unsafe_rate": self.stale_unsafe / n,
            "dominated_rate": self.dominated / n,
        }
        return out


def write_csv(path: Path, rows: Iterable[Dict[str, object]]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def mean_se(values: List[float]) -> Tuple[float, float]:
    if not values:
        return 0.0, 0.0
    if len(values) == 1:
        return values[0], 0.0
    return statistics.mean(values), statistics.stdev(values) / math.sqrt(len(values))


def summarize_seed_rows(seed_rows: List[Dict[str, object]], keys: List[str]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[object, ...], List[Dict[str, object]]] = {}
    for row in seed_rows:
        grouped.setdefault(tuple(row[k] for k in keys), []).append(row)
    metrics = [
        "accuracy",
        "nonabstain_accuracy",
        "balanced_accuracy",
        "unsafe_false_positive_rate",
        "avoidable_false_negative_rate",
        "abstention_rate",
        "precision",
        "recall",
        "f1",
        "mean_test_cost",
        "mean_tests_used",
        "mean_total_cost",
        "stale_unsafe_rate",
        "dominated_rate",
    ]
    out: List[Dict[str, object]] = []
    for key, rows in sorted(grouped.items()):
        base = {keys[i]: key[i] for i in range(len(keys))}
        base["seeds"] = len(rows)
        base["n_total"] = sum(int(r["n"]) for r in rows)
        for metric in metrics:
            mean, se = mean_se([float(r[metric]) for r in rows])
            base[metric] = mean
            base[metric + "_se"] = se
        out.append(base)
    return out


def maybe_add_example(examples: List[Dict[str, object]], kind: str, case: Case, method: str, y: bool, d: Decision, limit: int = 160) -> None:
    if len(examples) >= limit:
        return
    counts: Dict[str, int] = {}
    for row in examples:
        counts[row["kind"]] = counts.get(row["kind"], 0) + 1
    if counts.get(kind, 0) >= 20:
        return
    examples.append(
        {
            "kind": kind,
            "regime": case.regime,
            "label": case.obj.label,
            "task": case.task,
            "method": method,
            "truth": int(y),
            "decision": "abstain" if d.value is None else int(d.value),
            "test_cost": f"{d.test_cost:.4f}",
            "witness": d.witness[:180],
            "object_state": json.dumps(asdict(case.obj), sort_keys=True),
            "demand": json.dumps(asdict(case.demand), sort_keys=True),
            "robot": case.robot.name,
        }
    )


def iter_main_cases(seed: int, regime: str, episodes: int) -> Iterable[Case]:
    rng = random.Random(seed * 101 + len(regime))
    for episode in range(episodes):
        robot = make_robot(regime, rng)
        for label, base in CATALOG.items():
            obj = mutate(base, rng, regime)
            for task in TASKS:
                demand = make_demand(regime, rng, task)
                sensor_noise = 0.025
                if regime in {"degraded_worn", "adversarial_counterfeit"}:
                    sensor_noise = 0.04
                if regime == "embodiment_shift":
                    sensor_noise = 0.045
                yield Case(seed, regime, episode, obj, task, demand, robot, sensor_noise=sensor_noise)


def run_family_a() -> Tuple[List[Dict[str, object]], List[Dict[str, object]], List[Dict[str, object]]]:
    seed_rows: List[Dict[str, object]] = []
    task_seed_rows: List[Dict[str, object]] = []
    examples: List[Dict[str, object]] = []
    for seed in MAIN_SEEDS:
        seed_counters: Dict[Tuple[str, str], Counter] = {}
        task_counters: Dict[Tuple[str, str, str], Counter] = {}
        method_state: Dict[str, dict] = {m: {} for m in METHODS}
        method_rngs = {m: random.Random(stable_seed("A", seed, m)) for m in METHODS}
        for regime in REGIMES:
            for case in iter_main_cases(seed, regime, MAIN_EPISODES):
                y = truth(case.obj, case.task, case.demand, case.robot)
                text_decision = method_text_prior(case, random.Random(seed + case.episode), {})
                for method in METHODS:
                    rng = method_rngs[method]
                    d = METHOD_FN[method](case, rng, method_state[method])
                    if d.value == text_decision.value and d.tests_used > 0 and d.test_cost > 0:
                        d.dominated = True
                    seed_counters.setdefault((case.regime, method), Counter()).update(y, d, case.failure_harm, 1.0)
                    task_counters.setdefault((case.regime, method, case.task), Counter()).update(y, d, case.failure_harm, 1.0)
                    if d.value is True and not y:
                        maybe_add_example(examples, "unsafe_false_positive", case, method, y, d)
                    elif d.value is False and y:
                        maybe_add_example(examples, "avoidable_false_negative", case, method, y, d)
                    elif d.value is None:
                        maybe_add_example(examples, "abstention", case, method, y, d)
                    elif method in {"risk_aware_eatl", "cached_eatl"} and d.tests_used == 0 and d.value == y:
                        maybe_add_example(examples, "saved_test_correct", case, method, y, d)
        for (regime, method), counter in seed_counters.items():
            seed_rows.append(counter.row({"family": "A_main", "seed": seed, "regime": regime, "method": method}))
        for (regime, method, task), counter in task_counters.items():
            task_seed_rows.append(counter.row({"family": "A_main_task", "seed": seed, "regime": regime, "method": method, "task": task}))
    summary = summarize_seed_rows(seed_rows, ["family", "regime", "method"])
    task_summary = summarize_seed_rows(task_seed_rows, ["family", "regime", "method", "task"])
    write_csv(RESULTS / "main_seed_summary.csv", seed_rows)
    write_csv(RESULTS / "main_summary.csv", summary)
    write_csv(RESULTS / "main_task_seed_summary.csv", task_seed_rows)
    write_csv(RESULTS / "main_task_summary.csv", task_summary)
    write_csv(RESULTS / "failure_gallery.csv", examples)
    return summary, task_summary, examples


def iter_phase_cases(seed: int, hidden_flip_rate: float, episodes: int, failure_harm: float, test_harm_weight: float) -> Iterable[Case]:
    rng = random.Random(seed * 991 + int(hidden_flip_rate * 1000) + int(test_harm_weight * 100))
    for episode in range(episodes):
        for label, base in CATALOG.items():
            obj = mutate(base, rng, "typical", hidden_flip_rate=hidden_flip_rate)
            for task in TASKS:
                yield Case(
                    seed=seed,
                    regime="phase_hidden_flip",
                    episode=episode,
                    obj=obj,
                    task=task,
                    demand=BASE_DEMAND,
                    robot=STANDARD_ROBOT,
                    hidden_flip_rate=hidden_flip_rate,
                    failure_harm=failure_harm,
                    test_harm_weight=test_harm_weight,
                    sensor_noise=0.03,
                )


def run_family_b() -> List[Dict[str, object]]:
    methods = ["text_prior", "passive_vision_proxy", "conservative_prior", "eager_eatl", "risk_aware_eatl"]
    hidden_rates = [0.0, 0.10, 0.25, 0.50, 0.75, 1.00]
    test_weights = [0.0, 0.25, 0.50, 1.00, 1.25, 2.00, 3.00]
    failure_harms = [1.0, 5.0, 10.0, 20.0]
    seed_rows: List[Dict[str, object]] = []
    for failure_harm in failure_harms:
        for hidden_rate in hidden_rates:
            for test_weight in test_weights:
                for seed in PHASE_SEEDS:
                    counters: Dict[str, Counter] = {m: Counter() for m in methods}
                    state = {m: {} for m in methods}
                    method_rngs = {m: random.Random(stable_seed("B", seed, hidden_rate, test_weight, failure_harm, m)) for m in methods}
                    for case in iter_phase_cases(seed, hidden_rate, PHASE_EPISODES, failure_harm, test_weight):
                        y = truth(case.obj, case.task, case.demand, case.robot)
                        for method in methods:
                            rng = method_rngs[method]
                            d = METHOD_FN[method](case, rng, state[method])
                            counters[method].update(y, d, failure_harm, test_weight)
                    for method, counter in counters.items():
                        seed_rows.append(
                            counter.row(
                                {
                                    "family": "B_phase",
                                    "seed": seed,
                                    "hidden_flip_rate": hidden_rate,
                                    "test_harm_weight": test_weight,
                                    "failure_harm": failure_harm,
                                    "method": method,
                                }
                            )
                        )
    summary = summarize_seed_rows(seed_rows, ["family", "hidden_flip_rate", "test_harm_weight", "failure_harm", "method"])
    write_csv(RESULTS / "phase_seed_summary.csv", seed_rows)
    write_csv(RESULTS / "phase_summary.csv", summary)
    boundary: List[Dict[str, object]] = []
    grouped: Dict[Tuple[float, float, float], List[Dict[str, object]]] = {}
    for row in summary:
        grouped.setdefault((float(row["hidden_flip_rate"]), float(row["test_harm_weight"]), float(row["failure_harm"])), []).append(row)
    for (hidden_rate, test_weight, failure_harm), rows in sorted(grouped.items()):
        winner = min(rows, key=lambda r: float(r["mean_total_cost"]))
        eager = next(r for r in rows if r["method"] == "eager_eatl")
        risk = next(r for r in rows if r["method"] == "risk_aware_eatl")
        text = next(r for r in rows if r["method"] == "text_prior")
        boundary.append(
            {
                "hidden_flip_rate": hidden_rate,
                "test_harm_weight": test_weight,
                "failure_harm": failure_harm,
                "best_method": winner["method"],
                "best_total_cost": winner["mean_total_cost"],
                "text_total_cost": text["mean_total_cost"],
                "eager_eatl_total_cost": eager["mean_total_cost"],
                "risk_aware_eatl_total_cost": risk["mean_total_cost"],
                "risk_minus_text": float(risk["mean_total_cost"]) - float(text["mean_total_cost"]),
                "eager_minus_text": float(eager["mean_total_cost"]) - float(text["mean_total_cost"]),
            }
        )
    write_csv(RESULTS / "phase_boundary.csv", boundary)
    return summary


def run_family_c() -> List[Dict[str, object]]:
    variants = [
        "risk_aware_eatl",
        "eager_eatl",
        "risk_no_failure_harm",
        "risk_no_test_harm",
        "risk_no_abstention",
        "cheapest_test_selector",
        "random_test_control",
    ]
    seed_rows: List[Dict[str, object]] = []
    for regime in ["label_preserving_flips", "mixed", "adversarial_counterfeit"]:
        for seed in ABLATION_SEEDS:
            counters = {v: Counter() for v in variants}
            variant_rngs = {v: random.Random(stable_seed("C", seed, regime, v)) for v in variants}
            for case in iter_main_cases(seed, regime, ABLATION_EPISODES):
                y = truth(case.obj, case.task, case.demand, case.robot)
                for variant in variants:
                    rng = variant_rngs[variant]
                    if variant == "risk_aware_eatl":
                        d = method_risk_aware_eatl(case, rng, {})
                    elif variant == "eager_eatl":
                        d = method_eager_eatl(case, rng, {})
                    elif variant == "risk_no_failure_harm":
                        d = method_risk_aware_eatl(replace_case(case, failure_harm=1.0), rng, {})
                    elif variant == "risk_no_test_harm":
                        d = method_risk_aware_eatl(replace_case(case, test_harm_weight=0.0), rng, {})
                    elif variant == "risk_no_abstention":
                        d = method_risk_aware_eatl(case, rng, {})
                        if d.value is None:
                            p = visible_score(case, "vlm_blend", rng)
                            d = Decision(p >= 0.5, 0.0, 0, "forced_no_abstention")
                    elif variant == "cheapest_test_selector":
                        p = label_score(case.obj.label, case.task)
                        d = noisy_test(case, rng) if base_test_cost(case.task, case.demand) <= 0.09 and 0.20 < p < 0.90 else Decision(p >= 0.5, 0.0, 0, "cheapest_or_prior")
                    else:
                        d = method_random_control(case, rng, {})
                    counters[variant].update(y, d, case.failure_harm, case.test_harm_weight)
            for variant, counter in counters.items():
                seed_rows.append(counter.row({"family": "C_selector_ablation", "seed": seed, "regime": regime, "method": variant}))
    summary = summarize_seed_rows(seed_rows, ["family", "regime", "method"])
    write_csv(RESULTS / "selector_ablation_seed_summary.csv", seed_rows)
    write_csv(RESULTS / "selector_ablation_summary.csv", summary)
    return summary


def replace_case(case: Case, **kwargs: object) -> Case:
    data = case.__dict__.copy()
    data.update(kwargs)
    return Case(**data)


def run_family_d() -> List[Dict[str, object]]:
    policies = ["no_cache", "strict_cache", "label_only_cache", "ttl_cache", "demand_compatible_cache"]
    seed_rows: List[Dict[str, object]] = []
    for seed in CACHE_SEEDS:
        rng = random.Random(seed)
        counters = {p: Counter() for p in policies}
        caches: Dict[str, Dict[Tuple[str, str], Tuple[bool, int, str, Demand, str]]] = {p: {} for p in policies}
        for obj_id, (label, base) in enumerate(CATALOG.items()):
            obj = base
            for step in range(CACHE_STEPS):
                if step > 0 and rng.random() < 0.35:
                    obj = rng.choice([apply_hidden_flip, degrade])(obj, rng)
                robot = rng.choice([STANDARD_ROBOT, WEAK_ROBOT]) if rng.random() < 0.20 else STANDARD_ROBOT
                for task in TASKS:
                    demand = make_demand("task_demand_shift" if rng.random() < 0.30 else "typical", rng, task)
                    case = Case(seed, "cache_drift", step + obj_id * 1000, obj, task, demand, robot, sensor_noise=0.025)
                    y = truth(obj, task, demand, robot)
                    for policy in policies:
                        d = cache_policy_decision(policy, case, rng, caches[policy], step)
                        counters[policy].update(y, d, case.failure_harm, 1.0)
        for policy, counter in counters.items():
            seed_rows.append(counter.row({"family": "D_cache_validity", "seed": seed, "method": policy}))
    summary = summarize_seed_rows(seed_rows, ["family", "method"])
    write_csv(RESULTS / "cache_validity_seed_summary.csv", seed_rows)
    write_csv(RESULTS / "cache_validity_summary.csv", summary)
    return summary


def cache_policy_decision(policy: str, case: Case, rng: random.Random, cache: Dict[Tuple[str, str], Tuple[bool, int, str, Demand, str]], step: int) -> Decision:
    if policy == "no_cache":
        return noisy_test(case, rng)
    strict_key = (case.obj.label, case.task, state_signature(case.obj, case.demand, case.robot, strict=True))
    label_key = (case.obj.label, case.task)
    key = strict_key if policy == "strict_cache" else label_key
    if key in cache:
        pred, saved_step, saved_state_sig, saved_demand, saved_robot = cache[key]
        valid = False
        if policy == "strict_cache":
            valid = saved_state_sig == state_signature(case.obj, case.demand, case.robot, strict=True)
        elif policy == "label_only_cache":
            valid = True
        elif policy == "ttl_cache":
            valid = (step - saved_step) <= 5
        elif policy == "demand_compatible_cache":
            valid = saved_robot == case.robot.name and demand_is_compatible(saved_demand, case.demand, case.task)
        if valid:
            y = truth(case.obj, case.task, case.demand, case.robot)
            return Decision(pred, 0.0, 0, f"{policy}_hit", stale_reuse=(pred != y))
    d = noisy_test(case, rng)
    cache[key] = (bool(d.value), step, state_signature(case.obj, case.demand, case.robot, strict=True), case.demand, case.robot.name)
    return d


def demand_is_compatible(old: Demand, new: Demand, task: str) -> bool:
    if task in {"contain_liquid", "pour_without_spill"}:
        return new.volume_ml <= old.volume_ml
    if task == "lift":
        return new.gripper_limit_g >= old.gripper_limit_g
    if task == "support_load":
        return new.load_g <= old.load_g
    if task == "cut_soft_food":
        return new.required_sharpness <= old.required_sharpness and new.required_stiffness <= old.required_stiffness
    if task == "wipe_spill":
        return new.spill_ml <= old.spill_ml
    if task == "carry_hot":
        return new.temperature_c <= old.temperature_c
    if task == "stack_safely":
        return new.stack_load_g <= old.stack_load_g
    if task == "push_without_sliding":
        return new.push_force_n <= old.push_force_n
    if task == "grasp_without_crushing":
        return new.grip_force_n <= old.grip_force_n
    return False


def run_family_e() -> List[Dict[str, object]]:
    guard_modes = ["crisp_guard", "margin_abstain_guard", "repeat3_guard", "bayes_guard"]
    noise_levels = [0.0, 0.01, 0.03, 0.05, 0.08, 0.12, 0.18, 0.25]
    seed_rows: List[Dict[str, object]] = []
    for noise in noise_levels:
        for guard in guard_modes:
            for seed in NOISE_SEEDS:
                counter = Counter()
                rng = random.Random(stable_seed("E", seed, noise, guard))
                for case in iter_main_cases(seed, "label_preserving_flips", NOISE_EPISODES):
                    case = replace_case(case, sensor_noise=noise)
                    y = truth(case.obj, case.task, case.demand, case.robot)
                    d = guard_decision(guard, case, rng, noise)
                    counter.update(y, d, case.failure_harm, 1.0)
                seed_rows.append(counter.row({"family": "E_noise_bias", "seed": seed, "noise": noise, "guard": guard}))
    summary = summarize_seed_rows(seed_rows, ["family", "noise", "guard"])
    write_csv(RESULTS / "noise_guard_seed_summary.csv", seed_rows)
    write_csv(RESULTS / "noise_guard_summary.csv", summary)
    return summary


def guard_decision(guard: str, case: Case, rng: random.Random, noise: float) -> Decision:
    if guard == "crisp_guard":
        return noisy_test(case, rng, noise=noise, repeats=1)
    if guard == "repeat3_guard":
        return noisy_test(case, rng, noise=noise, repeats=3)
    if guard == "margin_abstain_guard":
        y = truth(case.obj, case.task, case.demand, case.robot)
        if rng.random() < noise * 1.4:
            return Decision(None, base_test_cost(case.task, case.demand), 1, "margin_guard(abstain)")
        obs = y
        if rng.random() < noise * 0.45:
            obs = not obs
        return Decision(obs, base_test_cost(case.task, case.demand), 1, "margin_guard(pass/fail)")
    if guard == "bayes_guard":
        y = truth(case.obj, case.task, case.demand, case.robot)
        votes = []
        for _ in range(5):
            obs = y
            if rng.random() < noise:
                obs = not obs
            votes.append(obs)
        yes = sum(votes)
        if yes in {2, 3}:
            return Decision(None, base_test_cost(case.task, case.demand) * 5, 5, "bayes_guard(abstain)")
        return Decision(yes > 3, base_test_cost(case.task, case.demand) * 5, 5, "bayes_guard(decide)")
    raise ValueError(guard)


def run_family_f() -> List[Dict[str, object]]:
    visibilities = ["label_only", "geometry_only", "geometry_material", "geometry_damage", "vlm_blend", "full_noisy"]
    seed_rows: List[Dict[str, object]] = []
    for visibility in visibilities:
        for regime in ["label_preserving_flips", "mixed", "adversarial_counterfeit"]:
            for seed in VISIBILITY_SEEDS:
                counter = Counter()
                rng = random.Random(stable_seed("F", seed, visibility, regime))
                for case in iter_main_cases(seed, regime, VISIBILITY_EPISODES):
                    y = truth(case.obj, case.task, case.demand, case.robot)
                    p = visible_score(case, visibility, rng)
                    d = Decision(p >= 0.5, 0.0, 0, f"visibility={visibility},p={p:.2f}")
                    counter.update(y, d, case.failure_harm, 1.0)
                seed_rows.append(counter.row({"family": "F_visibility", "seed": seed, "regime": regime, "visibility": visibility}))
    summary = summarize_seed_rows(seed_rows, ["family", "regime", "visibility"])
    write_csv(RESULTS / "visibility_seed_summary.csv", seed_rows)
    write_csv(RESULTS / "visibility_summary.csv", summary)
    return summary


def run_family_g() -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    sweep_specs = {
        "contain_liquid": ("volume_ml", [50, 100, 200, 350, 500, 750]),
        "support_load": ("load_g", [100, 300, 700, 1000, 1600, 2500]),
        "carry_hot": ("temperature_c", [40, 60, 80, 95, 110, 130]),
        "grasp_without_crushing": ("grip_force_n", [4, 8, 14, 20, 30, 45]),
        "lift": ("robot", ["standard_parallel_jaw", "weak_slippery_gripper", "precise_soft_gripper"]),
    }
    methods = ["text_prior", "passive_vision_proxy", "eager_eatl", "risk_aware_eatl"]
    robots = {r.name: r for r in [STANDARD_ROBOT, WEAK_ROBOT, PRECISE_ROBOT]}
    for task, (axis, values) in sweep_specs.items():
        for value in values:
            for seed in DEMAND_SEEDS:
                counters = {m: Counter() for m in methods}
                rng = random.Random(stable_seed(seed, task, axis, value))
                for _episode in range(DEMAND_EPISODES):
                    for label, base in CATALOG.items():
                        obj = mutate(base, rng, rng.choice(["typical", "label_preserving_flips", "degraded_worn"]))
                        demand = BASE_DEMAND
                        robot = STANDARD_ROBOT
                        if axis == "volume_ml":
                            demand = replace(demand, volume_ml=int(value))
                        elif axis == "load_g":
                            demand = replace(demand, load_g=int(value), stack_load_g=int(value))
                        elif axis == "temperature_c":
                            demand = replace(demand, temperature_c=int(value))
                        elif axis == "grip_force_n":
                            demand = replace(demand, grip_force_n=float(value))
                        elif axis == "robot":
                            robot = robots[str(value)]
                        case = Case(seed, "demand_embodiment_sweep", _episode, obj, task, demand, robot, sensor_noise=0.035)
                        y = truth(obj, task, demand, robot)
                        for method in methods:
                            d = METHOD_FN[method](case, rng, {})
                            counters[method].update(y, d, case.failure_harm, 1.0)
                for method, counter in counters.items():
                    rows.append(counter.row({"family": "G_demand_embodiment", "seed": seed, "task": task, "axis": axis, "value": value, "method": method}))
    summary = summarize_seed_rows(rows, ["family", "task", "axis", "value", "method"])
    write_csv(RESULTS / "demand_embodiment_seed_summary.csv", rows)
    write_csv(RESULTS / "demand_embodiment_summary.csv", summary)
    return summary


def fmt(x: object, digits: int = 3) -> str:
    try:
        return f"{float(x):.{digits}f}"
    except (TypeError, ValueError):
        return str(x)


def tex_escape(s: object) -> str:
    return str(s).replace("_", "\\_").replace("%", "\\%").replace("&", "\\&")


def write_latex_tables(main: List[Dict[str, object]], phase: List[Dict[str, object]], ablation: List[Dict[str, object]], cache: List[Dict[str, object]], noise: List[Dict[str, object]], visibility: List[Dict[str, object]], demand: List[Dict[str, object]], examples: List[Dict[str, object]]) -> None:
    selected_regimes = ["typical", "label_preserving_flips", "adversarial_counterfeit", "task_demand_shift", "embodiment_shift"]
    selected_methods = ["text_prior", "passive_vision_proxy", "conservative_prior", "eager_eatl", "risk_aware_eatl", "cached_eatl", "oracle_hidden_state"]
    lookup = {(r["regime"], r["method"]): r for r in main}
    lines = ["\\begin{tabular}{llrrrrr}", "\\toprule", "Regime & Method & Acc. & Unsafe FP & Abstain & Test cost & Total cost \\\\", "\\midrule"]
    for regime in selected_regimes:
        first = True
        for method in selected_methods:
            r = lookup[(regime, method)]
            lines.append(
                f"{tex_escape(regime) if first else ''} & {tex_escape(method)} & {fmt(r['accuracy'])} & {fmt(r['unsafe_false_positive_rate'])} & {fmt(r['abstention_rate'])} & {fmt(r['mean_test_cost'])} & {fmt(r['mean_total_cost'])} \\\\"
            )
            first = False
        if regime != selected_regimes[-1]:
            lines.append("\\midrule")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (PAPER / "full_scale_main_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    boundary_path = RESULTS / "phase_boundary.csv"
    phase_rows = list(csv.DictReader(boundary_path.open("r", encoding="utf-8", newline="")))
    compact = [
        r
        for r in phase_rows
        if float(r["failure_harm"]) in {5.0, 10.0}
        and float(r["hidden_flip_rate"]) in {0.10, 0.25, 0.75}
        and float(r["test_harm_weight"]) in {0.25, 1.00, 2.00, 3.00}
    ]
    lines = ["\\begin{tabular}{rrrlrrr}", "\\toprule", "Flip rate & Test harm & Failure harm & Best & Risk-text & Eager-text & Text cost \\\\", "\\midrule"]
    for r in compact[:24]:
        lines.append(
            f"{fmt(r['hidden_flip_rate'],2)} & {fmt(r['test_harm_weight'],2)} & {fmt(r['failure_harm'],1)} & {tex_escape(r['best_method'])} & {fmt(r['risk_minus_text'])} & {fmt(r['eager_minus_text'])} & {fmt(r['text_total_cost'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (PAPER / "phase_boundary_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    write_simple_method_table(PAPER / "selector_ablation_table.tex", ablation, "method", "regime", ["label_preserving_flips", "adversarial_counterfeit"], "C_selector_ablation")
    write_simple_method_table(PAPER / "cache_validity_table.tex", cache, "method", None, [], "D_cache_validity")
    noise_rows = [r for r in noise if float(r["noise"]) in {0.0, 0.05, 0.12, 0.25}]
    lines = ["\\begin{tabular}{llrrrr}", "\\toprule", "Noise & Guard & Acc. & Unsafe FP & Abstain & Test cost \\\\", "\\midrule"]
    for r in noise_rows:
        lines.append(f"{fmt(r['noise'],2)} & {tex_escape(r['guard'])} & {fmt(r['accuracy'])} & {fmt(r['unsafe_false_positive_rate'])} & {fmt(r['abstention_rate'])} & {fmt(r['mean_test_cost'])} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (PAPER / "noise_guard_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    vis_rows = [r for r in visibility if r["regime"] in {"label_preserving_flips", "adversarial_counterfeit"}]
    lines = ["\\begin{tabular}{llrrrr}", "\\toprule", "Regime & Visibility & Acc. & Unsafe FP & F1 & Total cost \\\\", "\\midrule"]
    for r in vis_rows:
        lines.append(f"{tex_escape(r['regime'])} & {tex_escape(r['visibility'])} & {fmt(r['accuracy'])} & {fmt(r['unsafe_false_positive_rate'])} & {fmt(r['f1'])} & {fmt(r['mean_total_cost'])} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (PAPER / "visibility_ladder_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    demand_rows = [r for r in demand if r["method"] in {"text_prior", "passive_vision_proxy", "risk_aware_eatl"}]
    lines = ["\\begin{tabular}{lllrrrr}", "\\toprule", "Task & Value & Method & Acc. & Unsafe FP & Abstain & Total cost \\\\", "\\midrule"]
    for r in demand_rows[:54]:
        lines.append(f"{tex_escape(r['task'])} & {tex_escape(r['value'])} & {tex_escape(r['method'])} & {fmt(r['accuracy'])} & {fmt(r['unsafe_false_positive_rate'])} & {fmt(r['abstention_rate'])} & {fmt(r['mean_total_cost'])} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (PAPER / "demand_embodiment_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = ["\\begin{tabular}{lllllp{0.35\\linewidth}}", "\\toprule", "Kind & Regime & Object & Task & Method & Witness \\\\", "\\midrule"]
    for r in examples[:18]:
        lines.append(f"{tex_escape(r['kind'])} & {tex_escape(r['regime'])} & {tex_escape(r['label'])} & {tex_escape(r['task'])} & {tex_escape(r['method'])} & {tex_escape(r['witness'])} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (PAPER / "failure_gallery_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_simple_method_table(path: Path, rows: List[Dict[str, object]], method_key: str, split_key: Optional[str], splits: List[str], family: str) -> None:
    if split_key is None:
        use_rows = rows
        lines = ["\\begin{tabular}{lrrrrr}", "\\toprule", "Method & Acc. & Unsafe FP & Abstain & Test cost & Total cost \\\\", "\\midrule"]
        for r in use_rows:
            lines.append(f"{tex_escape(r[method_key])} & {fmt(r['accuracy'])} & {fmt(r['unsafe_false_positive_rate'])} & {fmt(r['abstention_rate'])} & {fmt(r['mean_test_cost'])} & {fmt(r['mean_total_cost'])} \\\\")
    else:
        use_rows = [r for r in rows if r[split_key] in splits]
        lines = ["\\begin{tabular}{llrrrrr}", "\\toprule", f"{tex_escape(split_key)} & Method & Acc. & Unsafe FP & Abstain & Test cost & Total cost \\\\", "\\midrule"]
        for r in use_rows:
            lines.append(f"{tex_escape(r[split_key])} & {tex_escape(r[method_key])} & {fmt(r['accuracy'])} & {fmt(r['unsafe_false_positive_rate'])} & {fmt(r['abstention_rate'])} & {fmt(r['mean_test_cost'])} & {fmt(r['mean_total_cost'])} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def svg_bar(path: Path, rows: List[Dict[str, object]], title: str, x_key: str, y_key: str, group_key: str, keep_groups: List[str]) -> None:
    xs = []
    for r in rows:
        if r[group_key] in keep_groups and r[x_key] not in xs:
            xs.append(str(r[x_key]))
    width, height = 980, 460
    left, right, top, bottom = 85, 30, 45, 90
    plot_w, plot_h = width - left - right, height - top - bottom
    colors = ["#275DAD", "#C4493D", "#27866E", "#7B4FA1", "#B47F17", "#555555", "#111111"]
    max_y = max(float(r[y_key]) for r in rows if r[group_key] in keep_groups) * 1.10
    max_y = max(max_y, 0.01)
    bar_w = plot_w / max(1, len(xs) * (len(keep_groups) + 1))
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="25" font-family="Arial" font-size="18" text-anchor="middle">{title}</text>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="#222"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="#222"/>',
    ]
    lookup = {(str(r[x_key]), r[group_key]): float(r[y_key]) for r in rows}
    for i, x in enumerate(xs):
        group_x = left + i * plot_w / len(xs) + 15
        for j, g in enumerate(keep_groups):
            value = lookup.get((x, g), 0.0)
            h = value / max_y * plot_h
            bx = group_x + j * (bar_w + 3)
            by = top + plot_h - h
            parts.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{colors[j % len(colors)]}"/>')
        parts.append(f'<text x="{group_x + (len(keep_groups)*bar_w)/2:.1f}" y="{height-55}" font-family="Arial" font-size="11" text-anchor="middle" transform="rotate(20 {group_x + (len(keep_groups)*bar_w)/2:.1f},{height-55})">{x.replace("_", " ")}</text>')
    ly = height - 23
    lx = left
    for j, g in enumerate(keep_groups):
        parts.append(f'<rect x="{lx + j*145}" y="{ly-12}" width="12" height="12" fill="{colors[j % len(colors)]}"/>')
        parts.append(f'<text x="{lx + j*145 + 17}" y="{ly-2}" font-family="Arial" font-size="11">{g}</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def svg_line(path: Path, rows: List[Dict[str, object]], title: str, x_key: str, y_key: str, group_key: str, keep_groups: List[str]) -> None:
    width, height = 900, 420
    left, right, top, bottom = 80, 40, 45, 65
    plot_w, plot_h = width - left - right, height - top - bottom
    xs = sorted({float(r[x_key]) for r in rows})
    max_y = max(float(r[y_key]) for r in rows if r[group_key] in keep_groups) * 1.1
    min_x, max_x = min(xs), max(xs)
    colors = ["#275DAD", "#C4493D", "#27866E", "#7B4FA1", "#B47F17"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="25" font-family="Arial" font-size="18" text-anchor="middle">{title}</text>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="#222"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="#222"/>',
    ]
    for j, g in enumerate(keep_groups):
        pts = []
        for x in xs:
            vals = [float(r[y_key]) for r in rows if r[group_key] == g and abs(float(r[x_key]) - x) < 1e-9]
            if not vals:
                continue
            y = statistics.mean(vals)
            px = left + (x - min_x) / max(1e-9, max_x - min_x) * plot_w
            py = top + (1 - y / max(max_y, 1e-9)) * plot_h
            pts.append((px, py))
        if len(pts) >= 2:
            point_str = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
            parts.append(f'<polyline fill="none" stroke="{colors[j % len(colors)]}" stroke-width="3" points="{point_str}"/>')
            for x, y in pts:
                parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{colors[j % len(colors)]}"/>')
        parts.append(f'<rect x="{left + j*160}" y="{height-24}" width="12" height="12" fill="{colors[j % len(colors)]}"/>')
        parts.append(f'<text x="{left + j*160 + 18}" y="{height-14}" font-family="Arial" font-size="12">{g}</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_figures(main: List[Dict[str, object]], phase: List[Dict[str, object]], noise: List[Dict[str, object]], visibility: List[Dict[str, object]]) -> None:
    main_subset = [r for r in main if r["regime"] in {"typical", "label_preserving_flips", "adversarial_counterfeit", "task_demand_shift"}]
    svg_bar(
        FIGS / "unsafe_fp_by_regime.svg",
        main_subset,
        "Unsafe false positives by regime",
        "regime",
        "unsafe_false_positive_rate",
        "method",
        ["text_prior", "passive_vision_proxy", "eager_eatl", "risk_aware_eatl", "cached_eatl"],
    )
    phase_slice = [r for r in phase if float(r["failure_harm"]) == 5.0 and float(r["test_harm_weight"]) == 1.0 and r["method"] in {"text_prior", "eager_eatl", "risk_aware_eatl"}]
    svg_line(FIGS / "phase_hidden_rate_cost.svg", phase_slice, "Cost as hidden-flip rate increases", "hidden_flip_rate", "mean_total_cost", "method", ["text_prior", "eager_eatl", "risk_aware_eatl"])
    noise_slice = [r for r in noise if r["guard"] in {"crisp_guard", "margin_abstain_guard", "repeat3_guard", "bayes_guard"}]
    svg_line(FIGS / "noise_guard_unsafe.svg", noise_slice, "Probe-noise stress", "noise", "unsafe_false_positive_rate", "guard", ["crisp_guard", "margin_abstain_guard", "repeat3_guard", "bayes_guard"])
    vis_slice = [r for r in visibility if r["regime"] == "adversarial_counterfeit"]
    svg_bar(FIGS / "visibility_ladder.svg", vis_slice, "Passive visibility ladder on counterfeits", "visibility", "unsafe_false_positive_rate", "regime", ["adversarial_counterfeit"])


def write_results_readme(metadata: Dict[str, object], main: List[Dict[str, object]]) -> None:
    lp = {r["method"]: r for r in main if r["regime"] == "label_preserving_flips"}
    adv = {r["method"]: r for r in main if r["regime"] == "adversarial_counterfeit"}
    text = lp["text_prior"]
    risk = lp["risk_aware_eatl"]
    eager = lp["eager_eatl"]
    body = f"""# Full-Scale v3 Affordance-Test Results

Generated by `python experiments/full_scale_affordance_tests.py`.

Run metadata:

- Seed families: 28001-28612 depending on experiment family.
- Main benchmark cases: {metadata['main_cases']} robot-object-task cases.
- Main benchmark method decisions: {metadata['main_method_decisions']}.
- Total aggregate experiment families: A through G plus failure-gallery examples.
- Elapsed seconds: {metadata['elapsed_seconds']:.3f}.
- RAM-light design: raw main decisions are not retained; aggregate counters and bounded examples are written.

Key label-preserving flip result:

- Text prior unsafe false-positive rate: {float(text['unsafe_false_positive_rate']):.4f}.
- Eager EATL unsafe false-positive rate: {float(eager['unsafe_false_positive_rate']):.4f}.
- Risk-aware EATL unsafe false-positive rate: {float(risk['unsafe_false_positive_rate']):.4f}.
- Risk-aware EATL abstention rate: {float(risk['abstention_rate']):.4f}.
- Risk-aware EATL mean test cost: {float(risk['mean_test_cost']):.4f}.

Adversarial counterfeit result:

- Text prior unsafe false-positive rate: {float(adv['text_prior']['unsafe_false_positive_rate']):.4f}.
- Risk-aware EATL unsafe false-positive rate: {float(adv['risk_aware_eatl']['unsafe_false_positive_rate']):.4f}.
- Risk-aware EATL abstention rate: {float(adv['risk_aware_eatl']['abstention_rate']):.4f}.

Primary outputs:

- `main_summary.csv`
- `main_task_summary.csv`
- `phase_summary.csv`
- `phase_boundary.csv`
- `selector_ablation_summary.csv`
- `cache_validity_summary.csv`
- `noise_guard_summary.csv`
- `visibility_summary.csv`
- `demand_embodiment_summary.csv`
- `failure_gallery.csv`
"""
    (RESULTS / "README.md").write_text(body, encoding="utf-8")


def main() -> int:
    start = time.time()
    main_summary, task_summary, examples = run_family_a()
    phase_summary = run_family_b()
    ablation_summary = run_family_c()
    cache_summary = run_family_d()
    noise_summary = run_family_e()
    visibility_summary = run_family_f()
    demand_summary = run_family_g()
    write_latex_tables(main_summary, phase_summary, ablation_summary, cache_summary, noise_summary, visibility_summary, demand_summary, examples)
    write_figures(main_summary, phase_summary, noise_summary, visibility_summary)
    elapsed = time.time() - start
    main_cases = len(MAIN_SEEDS) * len(REGIMES) * MAIN_EPISODES * len(CATALOG) * len(TASKS)
    metadata = {
        "status": "complete",
        "version": "v3_full_scale",
        "elapsed_seconds": elapsed,
        "main_cases": main_cases,
        "main_method_decisions": main_cases * len(METHODS),
        "families": ["A_main", "B_phase", "C_selector_ablation", "D_cache_validity", "E_noise_bias", "F_visibility", "G_demand_embodiment", "H_failure_gallery"],
        "regimes": REGIMES,
        "tasks": TASKS,
        "methods": METHODS,
        "object_count": len(CATALOG),
        "ram_light": True,
    }
    (RESULTS / "run_metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    write_results_readme(metadata, main_summary)
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
