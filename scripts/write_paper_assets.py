"""Generate small LaTeX assets from experiment outputs."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
PAPER.mkdir(exist_ok=True)


def fmt(x: str) -> str:
    return f"{float(x):.3f}"


def main() -> int:
    rows = []
    with (ROOT / "results" / "summary.csv").open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row["regime"] in {"typical", "label_preserving_flips", "label_swap", "mixed"}:
                rows.append(row)
    order_regime = {
        "typical": 0,
        "label_preserving_flips": 1,
        "label_swap": 2,
        "mixed": 3,
    }
    order_method = {"text_prior": 0, "vision_proxy": 1, "eatl": 2}
    rows.sort(key=lambda r: (order_regime[r["regime"]], order_method[r["method"]]))

    lines = [
        "\\begin{tabular}{llrrrr}",
        "\\toprule",
        "Regime & Method & Acc. & Unsafe FP & Avoidable FN & F1 \\\\",
        "\\midrule",
    ]
    last = None
    for row in rows:
        regime = row["regime"].replace("_", " ")
        if last is not None and row["regime"] != last:
            lines.append("\\midrule")
        method = row["method"].replace("_", "\\_")
        lines.append(
            f"{regime} & {method} & {fmt(row['accuracy'])} & {fmt(row['unsafe_false_positive_rate'])} & {fmt(row['avoidable_false_negative_rate'])} & {fmt(row['f1'])} \\\\"
        )
        last = row["regime"]
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (PAPER / "results_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote paper/results_table.tex")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
