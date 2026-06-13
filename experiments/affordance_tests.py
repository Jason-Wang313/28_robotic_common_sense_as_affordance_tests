"""Executable affordance-test evidence for Paper 28.

The environment is intentionally small and transparent. It is not a real-robot
claim; it is a stress test for a specific assumption: object names remain
correlated with the physical variables that make robot actions safe.
"""

from __future__ import annotations

import csv
import json
import math
import random
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
FIGS = ROOT / "figures"
OUT.mkdir(exist_ok=True)
FIGS.mkdir(exist_ok=True)


TASKS = [
    "contain_liquid",
    "lift",
    "support_load",
    "cut_soft_food",
    "wipe_spill",
    "carry_hot",
]


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


TYPICAL: Dict[str, Obj] = {
    "mug": Obj("mug", True, False, False, 350, 320, 0.72, 900, 0.03, 0.30, 5, True, True, True, False),
    "bowl": Obj("bowl", True, False, False, 500, 420, 0.66, 1200, 0.02, 0.20, 10, True, False, True, False),
    "sieve": Obj("sieve", True, True, True, 450, 180, 0.61, 300, 0.02, 0.15, 20, True, False, True, False),
    "knife": Obj("knife", False, False, False, 0, 150, 0.58, 80, 0.94, 0.88, 0, True, True, False, False),
    "spoon": Obj("spoon", True, False, False, 20, 80, 0.55, 40, 0.07, 0.55, 0, True, True, False, False),
    "sponge": Obj("sponge", False, True, False, 40, 30, 0.80, 80, 0.01, 0.04, 160, False, False, True, False),
    "brick": Obj("brick", False, False, False, 0, 1800, 0.90, 6000, 0.01, 0.95, 5, True, False, True, True),
    "cardboard_box": Obj("cardboard_box", True, True, False, 800, 220, 0.70, 1500, 0.02, 0.35, 80, False, False, True, True),
    "plastic_tray": Obj("plastic_tray", True, False, False, 250, 160, 0.63, 700, 0.02, 0.50, 3, False, False, True, True),
    "glass": Obj("glass", True, False, False, 280, 260, 0.45, 600, 0.03, 0.40, 0, False, False, True, False),
}


TEXT_PRIOR: Dict[str, Dict[str, bool]] = {
    "mug": {"contain_liquid": True, "lift": True, "support_load": False, "cut_soft_food": False, "wipe_spill": False, "carry_hot": True},
    "bowl": {"contain_liquid": True, "lift": True, "support_load": False, "cut_soft_food": False, "wipe_spill": False, "carry_hot": False},
    "sieve": {"contain_liquid": False, "lift": True, "support_load": False, "cut_soft_food": False, "wipe_spill": False, "carry_hot": False},
    "knife": {"contain_liquid": False, "lift": True, "support_load": False, "cut_soft_food": True, "wipe_spill": False, "carry_hot": False},
    "spoon": {"contain_liquid": False, "lift": True, "support_load": False, "cut_soft_food": False, "wipe_spill": False, "carry_hot": False},
    "sponge": {"contain_liquid": False, "lift": True, "support_load": False, "cut_soft_food": False, "wipe_spill": True, "carry_hot": False},
    "brick": {"contain_liquid": False, "lift": False, "support_load": True, "cut_soft_food": False, "wipe_spill": False, "carry_hot": False},
    "cardboard_box": {"contain_liquid": False, "lift": True, "support_load": True, "cut_soft_food": False, "wipe_spill": False, "carry_hot": False},
    "plastic_tray": {"contain_liquid": True, "lift": True, "support_load": False, "cut_soft_food": False, "wipe_spill": False, "carry_hot": False},
    "glass": {"contain_liquid": True, "lift": True, "support_load": False, "cut_soft_food": False, "wipe_spill": False, "carry_hot": False},
}


DEMANDS = {
    "contain_liquid": {"volume_ml": 200},
    "lift": {"gripper_limit_g": 900},
    "support_load": {"load_g": 1000},
    "cut_soft_food": {"required_sharpness": 0.55, "required_stiffness": 0.45},
    "wipe_spill": {"spill_ml": 60},
    "carry_hot": {"temperature_c": 85},
}


def truth(obj: Obj, task: str) -> bool:
    if task == "contain_liquid":
        return obj.concave and not obj.porous and not obj.has_hole and obj.capacity_ml >= DEMANDS[task]["volume_ml"] and obj.stable_base
    if task == "lift":
        return obj.mass_g <= DEMANDS[task]["gripper_limit_g"] and obj.friction >= 0.50
    if task == "support_load":
        return obj.load_capacity_g >= DEMANDS[task]["load_g"] and obj.stable_base and obj.flat_top
    if task == "cut_soft_food":
        return obj.sharpness >= DEMANDS[task]["required_sharpness"] and obj.edge_stiffness >= DEMANDS[task]["required_stiffness"]
    if task == "wipe_spill":
        return obj.absorbency_ml >= DEMANDS[task]["spill_ml"] and obj.mass_g <= 600
    if task == "carry_hot":
        return obj.heat_resistant and obj.has_handle and obj.mass_g <= 900
    raise ValueError(task)


def mutate(obj: Obj, rng: random.Random, regime: str) -> Obj:
    if regime == "typical":
        # Mild wear only.
        return replace(
            obj,
            mass_g=max(10, int(obj.mass_g * rng.uniform(0.9, 1.1))),
            friction=min(1.0, max(0.1, obj.friction + rng.uniform(-0.05, 0.05))),
        )

    if regime == "label_preserving_flips":
        # Keep the name but flip one or more hidden physical variables.
        choices = [
            lambda o: replace(o, has_hole=True) if o.concave else replace(o, concave=True, capacity_ml=max(o.capacity_ml, 250), has_hole=True),
            lambda o: replace(o, porous=True),
            lambda o: replace(o, sharpness=min(o.sharpness, 0.12), edge_stiffness=min(o.edge_stiffness, 0.20)),
            lambda o: replace(o, mass_g=max(o.mass_g, 1200), friction=min(o.friction, 0.38)),
            lambda o: replace(o, load_capacity_g=min(o.load_capacity_g, 300), flat_top=False),
            lambda o: replace(o, heat_resistant=False, has_handle=False),
            lambda o: replace(o, absorbency_ml=0, porous=False),
        ]
        for fn in rng.sample(choices, rng.randint(1, 3)):
            obj = fn(obj)
        return obj

    if regime == "label_swap":
        donor = rng.choice(list(TYPICAL.values()))
        # Physical variables from donor, label from original.
        return replace(donor, label=obj.label)

    if regime == "mixed":
        return mutate(obj, rng, rng.choice(["typical", "label_preserving_flips", "label_swap"]))

    raise ValueError(regime)


def text_prior(obj: Obj, task: str, rng: random.Random, noise: float) -> Tuple[bool, str, float]:
    pred = TEXT_PRIOR[obj.label][task]
    if rng.random() < noise:
        pred = not pred
    return pred, f"text_prior(label={obj.label})", 0.0


def eatl_test(obj: Obj, task: str, rng: random.Random, noise: float) -> Tuple[bool, str, float]:
    # Each branch is a cheap micro-experiment. We simulate observation noise by
    # flipping the test result, not the underlying truth.
    y = truth(obj, task)
    cost = {
        "contain_liquid": 0.10,
        "lift": 0.08,
        "support_load": 0.12,
        "cut_soft_food": 0.11,
        "wipe_spill": 0.07,
        "carry_hot": 0.09,
    }[task]
    if rng.random() < noise:
        y = not y
    if task == "contain_liquid":
        witness = f"pour_probe(volume={DEMANDS[task]['volume_ml']}ml, leak={obj.porous or obj.has_hole}, stable={obj.stable_base})"
    elif task == "lift":
        witness = f"trial_lift(limit={DEMANDS[task]['gripper_limit_g']}g, mass={obj.mass_g}g, friction={obj.friction:.2f})"
    elif task == "support_load":
        witness = f"load_probe(load={DEMANDS[task]['load_g']}g, capacity={obj.load_capacity_g}g, flat_top={obj.flat_top})"
    elif task == "cut_soft_food":
        witness = f"edge_probe(sharpness={obj.sharpness:.2f}, stiffness={obj.edge_stiffness:.2f})"
    elif task == "wipe_spill":
        witness = f"absorb_probe(spill={DEMANDS[task]['spill_ml']}ml, absorbency={obj.absorbency_ml}ml)"
    elif task == "carry_hot":
        witness = f"thermal_handle_probe(temp={DEMANDS[task]['temperature_c']}C, heat_resistant={obj.heat_resistant}, handle={obj.has_handle})"
    else:
        raise ValueError(task)
    return y, witness, cost


def vision_proxy(obj: Obj, task: str, rng: random.Random, noise: float) -> Tuple[bool, str, float]:
    # A simple non-text baseline that sees geometry-like variables but misses
    # hidden material/damage state.
    if task == "contain_liquid":
        pred = obj.concave and obj.capacity_ml >= 200 and obj.stable_base
    elif task == "lift":
        pred = obj.mass_g <= 900
    elif task == "support_load":
        pred = obj.stable_base and obj.flat_top
    elif task == "cut_soft_food":
        pred = obj.edge_stiffness >= 0.45
    elif task == "wipe_spill":
        pred = obj.porous
    elif task == "carry_hot":
        pred = obj.has_handle
    else:
        raise ValueError(task)
    if rng.random() < noise:
        pred = not pred
    return pred, "vision_proxy(visible_geometry_only)", 0.0


METHODS = {
    "text_prior": text_prior,
    "vision_proxy": vision_proxy,
    "eatl": eatl_test,
}


def run_episode(rng: random.Random, regime: str, noise: float, episode_id: int) -> List[dict]:
    rows = []
    for label, base in TYPICAL.items():
        obj = mutate(base, rng, regime)
        for task in TASKS:
            y = truth(obj, task)
            for method, fn in METHODS.items():
                pred, witness, cost = fn(obj, task, rng, noise)
                rows.append(
                    {
                        "episode": episode_id,
                        "regime": regime,
                        "label": label,
                        "task": task,
                        "method": method,
                        "truth": int(y),
                        "prediction": int(pred),
                        "correct": int(pred == y),
                        "unsafe_false_positive": int(pred and not y),
                        "avoidable_false_negative": int((not pred) and y),
                        "test_cost": cost,
                        "witness": witness,
                        "object_state": json.dumps(obj.__dict__, sort_keys=True),
                    }
                )
    return rows


def summarize(rows: List[dict]) -> List[dict]:
    groups: Dict[Tuple[str, str], List[dict]] = {}
    for row in rows:
        groups.setdefault((row["regime"], row["method"]), []).append(row)
    out = []
    for (regime, method), items in sorted(groups.items()):
        n = len(items)
        tp = sum(1 for r in items if r["truth"] == 1 and r["prediction"] == 1)
        fp = sum(1 for r in items if r["truth"] == 0 and r["prediction"] == 1)
        fn = sum(1 for r in items if r["truth"] == 1 and r["prediction"] == 0)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        out.append(
            {
                "regime": regime,
                "method": method,
                "n": n,
                "accuracy": sum(r["correct"] for r in items) / n,
                "unsafe_false_positive_rate": sum(r["unsafe_false_positive"] for r in items) / n,
                "avoidable_false_negative_rate": sum(r["avoidable_false_negative"] for r in items) / n,
                "precision": precision,
                "recall": recall,
                "f1": f1,
                "mean_test_cost": sum(float(r["test_cost"]) for r in items) / n,
            }
        )
    return out


def write_csv(path: Path, rows: List[dict]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def test_cost_stress(summary: List[dict]) -> List[dict]:
    """Measure when diagnostic testing stops being the safer default."""
    lookup = {(row["regime"], row["method"]): row for row in summary}
    regimes = ["typical", "label_preserving_flips", "label_swap", "mixed"]
    rows = []
    for regime in regimes:
        text = lookup[(regime, "text_prior")]
        eatl = lookup[(regime, "eatl")]
        text_unsafe = float(text["unsafe_false_positive_rate"])
        eatl_unsafe = float(eatl["unsafe_false_positive_rate"])
        eatl_cost = float(eatl["mean_test_cost"])
        if eatl_cost > 0:
            break_even = (text_unsafe - eatl_unsafe) / eatl_cost
        else:
            break_even = math.inf
        stress_weight = 1.25
        rows.append(
            {
                "regime": regime,
                "text_unsafe_false_positive_rate": text_unsafe,
                "eatl_unsafe_false_positive_rate": eatl_unsafe,
                "eatl_mean_test_cost": eatl_cost,
                "break_even_test_harm_weight": break_even,
                "stress_test_harm_weight": stress_weight,
                "text_safety_cost_at_stress": text_unsafe,
                "eatl_safety_cost_at_stress": eatl_unsafe + stress_weight * eatl_cost,
                "eatl_wins_at_stress": int(eatl_unsafe + stress_weight * eatl_cost < text_unsafe),
            }
        )
    return rows


def write_svg(summary: List[dict]) -> None:
    # Minimal dependency-free grouped bar chart.
    regimes = ["typical", "label_preserving_flips", "label_swap", "mixed"]
    methods = ["text_prior", "vision_proxy", "eatl"]
    lookup = {(r["regime"], r["method"]): r for r in summary}
    width, height = 900, 420
    margin_l, margin_b, top = 70, 70, 35
    plot_w, plot_h = width - margin_l - 30, height - margin_b - top
    colors = {"text_prior": "#9C4D2F", "vision_proxy": "#447C69", "eatl": "#355C9A"}
    bar_w = plot_w / (len(regimes) * 5)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<line x1="{margin_l}" y1="{top}" x2="{margin_l}" y2="{height-margin_b}" stroke="#222"/>',
        f'<line x1="{margin_l}" y1="{height-margin_b}" x2="{width-30}" y2="{height-margin_b}" stroke="#222"/>',
        f'<text x="{width/2}" y="24" font-family="Arial" font-size="18" text-anchor="middle">Accuracy under label-preserving affordance flips</text>',
        f'<text x="18" y="{height/2}" font-family="Arial" font-size="13" transform="rotate(-90 18,{height/2})" text-anchor="middle">Accuracy</text>',
    ]
    for tick in [0, 0.25, 0.5, 0.75, 1.0]:
        y = top + (1 - tick) * plot_h
        parts.append(f'<line x1="{margin_l-4}" y1="{y:.1f}" x2="{margin_l}" y2="{y:.1f}" stroke="#222"/>')
        parts.append(f'<text x="{margin_l-8}" y="{y+4:.1f}" font-family="Arial" font-size="11" text-anchor="end">{tick:.2f}</text>')
        parts.append(f'<line x1="{margin_l}" y1="{y:.1f}" x2="{width-30}" y2="{y:.1f}" stroke="#e8e8e8"/>')
    for i, regime in enumerate(regimes):
        group_x = margin_l + i * plot_w / len(regimes) + 35
        for j, method in enumerate(methods):
            acc = lookup[(regime, method)]["accuracy"]
            h = acc * plot_h
            x = group_x + j * (bar_w + 5)
            y = top + plot_h - h
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{colors[method]}"/>')
        label = regime.replace("_", " ")
        parts.append(f'<text x="{group_x + bar_w*1.5:.1f}" y="{height-45}" font-family="Arial" font-size="12" text-anchor="middle">{label}</text>')
    lx = margin_l + 10
    for j, method in enumerate(methods):
        parts.append(f'<rect x="{lx + j*180}" y="{height-24}" width="14" height="14" fill="{colors[method]}"/>')
        parts.append(f'<text x="{lx + j*180 + 20}" y="{height-13}" font-family="Arial" font-size="12">{method}</text>')
    parts.append("</svg>")
    (FIGS / "accuracy_by_regime.svg").write_text("\n".join(parts), encoding="utf-8")


def write_readme(summary: List[dict], stress: List[dict]) -> None:
    rows = "\n".join(
        f"| {r['regime']} | {r['method']} | {r['accuracy']:.3f} | {r['unsafe_false_positive_rate']:.3f} | {r['avoidable_false_negative_rate']:.3f} | {r['f1']:.3f} | {r['mean_test_cost']:.3f} |"
        for r in summary
    )
    stress_rows = "\n".join(
        f"| {r['regime']} | {r['text_unsafe_false_positive_rate']:.3f} | {r['eatl_unsafe_false_positive_rate']:.3f} | {r['eatl_mean_test_cost']:.3f} | {r['break_even_test_harm_weight']:.3f} | {r['eatl_safety_cost_at_stress']:.3f} |"
        for r in stress
    )
    (OUT / "README.md").write_text(
        f"""# Affordance-Test Experiment Results

The experiment compares three mechanisms:

- `text_prior`: predicts affordances from the object label.
- `vision_proxy`: sees geometry-like variables but not hidden material/damage.
- `eatl`: runs executable affordance tests that probe task-specific causal variables.

| Regime | Method | Accuracy | Unsafe FP Rate | Avoidable FN Rate | F1 | Mean Test Cost |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
{rows}

The important stress regime is `label_preserving_flips`: the object name is
unchanged, but hidden properties such as holes, porosity, dullness, load
capacity, heat resistance, and slipperiness are changed. A name-only prior has
no input channel for those variables, while EATL obtains them through tests.

## V2 Test-Cost Stress

The v2 stress computes `unsafe_false_positive_rate + lambda * mean_test_cost`.
The break-even lambda is the normalized test-harm weight where EATL and the text
prior have the same safety-plus-test-cost.

| Regime | Text Unsafe FP | EATL Unsafe FP | EATL Test Cost | Break-even Lambda | EATL Cost at Lambda 1.25 |
| --- | ---: | ---: | ---: | ---: | ---: |
{stress_rows}
""",
        encoding="utf-8",
    )


def main() -> int:
    rng = random.Random(28)
    rows: List[dict] = []
    regimes = ["typical", "label_preserving_flips", "label_swap", "mixed"]
    noise_by_regime = {
        "typical": 0.02,
        "label_preserving_flips": 0.03,
        "label_swap": 0.03,
        "mixed": 0.04,
    }
    episode = 0
    for regime in regimes:
        for _ in range(250):
            rows.extend(run_episode(rng, regime, noise_by_regime[regime], episode))
            episode += 1
    summary = summarize(rows)
    stress = test_cost_stress(summary)
    write_csv(OUT / "episode_results.csv", rows)
    write_csv(OUT / "summary.csv", summary)
    write_csv(OUT / "test_cost_stress.csv", stress)
    write_svg(summary)
    write_readme(summary, stress)
    print(json.dumps({"episodes": episode, "rows": len(rows), "summary": summary, "test_cost_stress": stress}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
