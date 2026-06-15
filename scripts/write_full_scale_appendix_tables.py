"""Write long appendix tables from Paper 28 v3 full-scale CSVs."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
PAPER = ROOT / "paper"


def rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def esc(x: object) -> str:
    return str(x).replace("_", " ").replace("&", "\\&").replace("%", "\\%")


def fmt(x: object, digits: int = 3) -> str:
    return f"{float(x):.{digits}f}"


def write(path: str, lines: list[str]) -> None:
    (PAPER / path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def longtable_start(spec: str, header: str) -> list[str]:
    return [
        f"\\begin{{longtable}}{{{spec}}}",
        "\\toprule",
        header + " \\\\",
        "\\midrule",
        "\\endfirsthead",
        "\\toprule",
        header + " \\\\",
        "\\midrule",
        "\\endhead",
    ]


def write_full_main() -> None:
    data = rows("main_summary.csv")
    order_regime = {
        "typical": 0,
        "label_preserving_flips": 1,
        "label_swap": 2,
        "mixed": 3,
        "adversarial_counterfeit": 4,
        "degraded_worn": 5,
        "task_demand_shift": 6,
        "embodiment_shift": 7,
    }
    order_method = {
        "text_prior": 0,
        "calibrated_text_prior": 1,
        "passive_vision_proxy": 2,
        "uncertainty_vision_proxy": 3,
        "conservative_prior": 4,
        "eager_eatl": 5,
        "risk_aware_eatl": 6,
        "cached_eatl": 7,
        "oracle_hidden_state": 8,
        "random_test_control": 9,
    }
    data.sort(key=lambda r: (order_regime[r["regime"]], order_method[r["method"]]))
    lines = longtable_start("llrrrrrr", "Regime & Method & Acc. & Unsafe FP & FN & Abstain & Test & Total")
    last = None
    for r in data:
        if last is not None and r["regime"] != last:
            lines.append("\\midrule")
        lines.append(
            f"{esc(r['regime'])} & {esc(r['method'])} & {fmt(r['accuracy'])} & "
            f"{fmt(r['unsafe_false_positive_rate'])} & {fmt(r['avoidable_false_negative_rate'])} & "
            f"{fmt(r['abstention_rate'])} & {fmt(r['mean_test_cost'])} & {fmt(r['mean_total_cost'])} \\\\"
        )
        last = r["regime"]
    lines.extend(["\\bottomrule", "\\end{longtable}"])
    write("full_main_appendix_table.tex", lines)


def write_task_breakdown() -> None:
    data = rows("main_task_summary.csv")
    regimes = {"label_preserving_flips", "adversarial_counterfeit", "task_demand_shift", "embodiment_shift"}
    methods = {"text_prior", "passive_vision_proxy", "conservative_prior", "eager_eatl", "risk_aware_eatl", "cached_eatl"}
    data = [r for r in data if r["regime"] in regimes and r["method"] in methods]
    data.sort(key=lambda r: (r["regime"], r["task"], r["method"]))
    lines = longtable_start("lllrrrrr", "Regime & Task & Method & Acc. & Unsafe FP & Abstain & Test & Total")
    last = None
    for r in data:
        key = (r["regime"], r["task"])
        if last is not None and key != last:
            lines.append("\\midrule")
        lines.append(
            f"{esc(r['regime'])} & {esc(r['task'])} & {esc(r['method'])} & {fmt(r['accuracy'])} & "
            f"{fmt(r['unsafe_false_positive_rate'])} & {fmt(r['abstention_rate'])} & "
            f"{fmt(r['mean_test_cost'])} & {fmt(r['mean_total_cost'])} \\\\"
        )
        last = key
    lines.extend(["\\bottomrule", "\\end{longtable}"])
    write("task_breakdown_appendix_table.tex", lines)


def write_phase_grid() -> None:
    data = rows("phase_boundary.csv")
    data = [r for r in data if float(r["failure_harm"]) in {5.0, 10.0}]
    data.sort(key=lambda r: (float(r["failure_harm"]), float(r["hidden_flip_rate"]), float(r["test_harm_weight"])))
    lines = longtable_start("rrrrlrrr", "Fail harm & Flip & Test harm & Text cost & Best & Risk-text & Eager-text & Best cost")
    for r in data:
        lines.append(
            f"{fmt(r['failure_harm'],1)} & {fmt(r['hidden_flip_rate'],2)} & {fmt(r['test_harm_weight'],2)} & "
            f"{fmt(r['text_total_cost'])} & {esc(r['best_method'])} & {fmt(r['risk_minus_text'])} & "
            f"{fmt(r['eager_minus_text'])} & {fmt(r['best_total_cost'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{longtable}"])
    write("phase_grid_appendix_table.tex", lines)


def write_demand_full() -> None:
    data = rows("demand_embodiment_summary.csv")
    keep_methods = {"text_prior", "passive_vision_proxy", "eager_eatl", "risk_aware_eatl"}
    data = [r for r in data if r["method"] in keep_methods]
    data.sort(key=lambda r: (r["task"], r["value"], r["method"]))
    lines = longtable_start("lllrrrrr", "Task & Value & Method & Acc. & Unsafe FP & Abstain & Test & Total")
    for r in data:
        lines.append(
            f"{esc(r['task'])} & {esc(r['value'])} & {esc(r['method'])} & {fmt(r['accuracy'])} & "
            f"{fmt(r['unsafe_false_positive_rate'])} & {fmt(r['abstention_rate'])} & "
            f"{fmt(r['mean_test_cost'])} & {fmt(r['mean_total_cost'])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{longtable}"])
    write("demand_full_appendix_table.tex", lines)


def write_failure_gallery() -> None:
    data = rows("failure_gallery.csv")[:60]
    lines = longtable_start(
        "@{}p{0.08\\linewidth}p{0.09\\linewidth}p{0.08\\linewidth}p{0.09\\linewidth}p{0.10\\linewidth}p{0.25\\linewidth}@{}",
        "Kind & Regime & Object & Task & Method & Witness",
    )
    for r in data:
        lines.append(
            f"{esc(r['kind'])} & {esc(r['regime'])} & {esc(r['label'])} & {esc(r['task'])} & "
            f"{esc(r['method'])} & {esc(r['witness'][:140])} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{longtable}"])
    write("failure_gallery_appendix_table.tex", lines)


def main() -> int:
    write_full_main()
    write_task_breakdown()
    write_phase_grid()
    write_demand_full()
    write_failure_gallery()
    print("wrote full-scale appendix tables")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
