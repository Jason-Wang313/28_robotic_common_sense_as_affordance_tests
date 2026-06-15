"""Render PDF figures for the Paper 28 v3 manuscript from aggregate CSVs."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
FIGS = ROOT / "figures" / "full_scale"
FIGS.mkdir(parents=True, exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def savefig(name: str) -> None:
    plt.tight_layout()
    plt.savefig(FIGS / name, bbox_inches="tight")
    plt.close()


def plot_main_unsafe() -> None:
    rows = read_csv("main_summary.csv")
    regimes = ["typical", "label_preserving_flips", "adversarial_counterfeit", "task_demand_shift", "embodiment_shift"]
    methods = ["text_prior", "passive_vision_proxy", "eager_eatl", "risk_aware_eatl", "cached_eatl"]
    lookup = {(r["regime"], r["method"]): float(r["unsafe_false_positive_rate"]) for r in rows}
    x = range(len(regimes))
    width = 0.15
    colors = ["#8C3B2E", "#426F62", "#355C9A", "#B47F17", "#6B5B95"]
    plt.figure(figsize=(9.6, 4.2))
    for j, method in enumerate(methods):
        vals = [lookup[(regime, method)] for regime in regimes]
        pos = [i + (j - 2) * width for i in x]
        plt.bar(pos, vals, width=width, label=method.replace("_", " "), color=colors[j])
    plt.ylabel("Unsafe false-positive rate")
    plt.xticks(list(x), [r.replace("_", " ") for r in regimes], rotation=18, ha="right")
    plt.ylim(0, 0.28)
    plt.legend(ncol=3, fontsize=8, frameon=False)
    plt.title("Executable tests reduce unsafe assertions in hidden-affordance regimes")
    savefig("unsafe_fp_by_regime.pdf")


def plot_phase() -> None:
    rows = [
        r
        for r in read_csv("phase_summary.csv")
        if float(r["failure_harm"]) == 5.0
        and float(r["test_harm_weight"]) == 1.0
        and r["method"] in {"text_prior", "eager_eatl", "risk_aware_eatl", "conservative_prior"}
    ]
    methods = ["text_prior", "conservative_prior", "eager_eatl", "risk_aware_eatl"]
    colors = ["#8C3B2E", "#555555", "#355C9A", "#B47F17"]
    plt.figure(figsize=(7.2, 4.1))
    for method, color in zip(methods, colors):
        sub = sorted([r for r in rows if r["method"] == method], key=lambda r: float(r["hidden_flip_rate"]))
        plt.plot(
            [float(r["hidden_flip_rate"]) for r in sub],
            [float(r["mean_total_cost"]) for r in sub],
            marker="o",
            label=method.replace("_", " "),
            color=color,
        )
    plt.xlabel("Hidden affordance flip rate")
    plt.ylabel("Mean safety-plus-test cost")
    plt.title("Cost boundary at failure harm 5 and test-harm weight 1")
    plt.legend(frameon=False, fontsize=8)
    savefig("phase_hidden_rate_cost.pdf")


def plot_noise() -> None:
    rows = read_csv("noise_guard_summary.csv")
    guards = ["crisp_guard", "margin_abstain_guard", "repeat3_guard", "bayes_guard"]
    colors = ["#8C3B2E", "#426F62", "#355C9A", "#B47F17"]
    plt.figure(figsize=(7.2, 4.1))
    for guard, color in zip(guards, colors):
        sub = sorted([r for r in rows if r["guard"] == guard], key=lambda r: float(r["noise"]))
        plt.plot(
            [float(r["noise"]) for r in sub],
            [float(r["unsafe_false_positive_rate"]) for r in sub],
            marker="o",
            label=guard.replace("_", " "),
            color=color,
        )
    plt.xlabel("Probe observation noise")
    plt.ylabel("Unsafe false-positive rate")
    plt.title("Guard design under noisy executable tests")
    plt.legend(frameon=False, fontsize=8)
    savefig("noise_guard_unsafe.pdf")


def plot_visibility() -> None:
    rows = [r for r in read_csv("visibility_summary.csv") if r["regime"] == "adversarial_counterfeit"]
    order = ["label_only", "geometry_only", "geometry_material", "geometry_damage", "vlm_blend", "full_noisy"]
    lookup = {r["visibility"]: float(r["unsafe_false_positive_rate"]) for r in rows}
    plt.figure(figsize=(7.2, 4.0))
    plt.bar(range(len(order)), [lookup[v] for v in order], color="#426F62")
    plt.ylabel("Unsafe false-positive rate")
    plt.xticks(range(len(order)), [v.replace("_", " ") for v in order], rotation=20, ha="right")
    plt.title("Passive visibility ladder on adversarial counterfeits")
    savefig("visibility_ladder.pdf")


def main() -> int:
    plot_main_unsafe()
    plot_phase()
    plot_noise()
    plot_visibility()
    print("rendered full-scale PDF figures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
