"""Fetch the official ICLR 2026 LaTeX template files."""

from __future__ import annotations

import io
import json
import shutil
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
PAPER.mkdir(exist_ok=True)
STATUS = ROOT / "data" / "template_fetch_status.json"
STATUS.parent.mkdir(exist_ok=True)


ZIP_URL = "https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip"
RAW_BASES = [
    "https://raw.githubusercontent.com/ICLR/Master-Template/master/iclr2026/",
    "https://raw.githubusercontent.com/ICLR/Master-Template/main/iclr2026/",
]
RAW_ROOTS = [
    "https://raw.githubusercontent.com/ICLR/Master-Template/master/",
    "https://raw.githubusercontent.com/ICLR/Master-Template/main/",
]

NEEDED = [
    "iclr2026_conference.sty",
    "iclr2026_conference.bst",
    "iclr2026_conference.tex",
]
OPTIONAL_ROOT = ["math_commands.tex", "fancyhdr.sty", "natbib.sty"]


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "paper28-template-fetch/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def copy_from_zip(blob: bytes) -> list[str]:
    copied = []
    with zipfile.ZipFile(io.BytesIO(blob)) as zf:
        for info in zf.infolist():
            name = Path(info.filename).name
            if name in NEEDED + OPTIONAL_ROOT:
                target = PAPER / name
                with zf.open(info) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
                copied.append(name)
    return copied


def copy_from_raw() -> list[str]:
    copied = []
    failures = []
    for name in NEEDED:
        ok = False
        for base in RAW_BASES:
            try:
                (PAPER / name).write_bytes(download(base + name))
                copied.append(name)
                ok = True
                break
            except Exception as exc:
                failures.append(f"{base}{name}: {type(exc).__name__}: {exc}")
        if not ok:
            raise RuntimeError("could not fetch " + name + "; " + " | ".join(failures[-2:]))
    for name in OPTIONAL_ROOT:
        for base in RAW_ROOTS:
            try:
                (PAPER / name).write_bytes(download(base + name))
                copied.append(name)
                break
            except Exception:
                continue
    return copied


def main() -> int:
    failures = []
    copied = []
    method = ""
    try:
        copied = copy_from_zip(download(ZIP_URL))
        method = ZIP_URL
    except Exception as exc:
        failures.append(f"zip fetch failed: {type(exc).__name__}: {exc}")
    missing = [name for name in NEEDED if not (PAPER / name).exists()]
    if missing:
        try:
            copied = copy_from_raw()
            method = "raw.githubusercontent.com fallback"
        except Exception as exc:
            failures.append(f"raw fetch failed: {type(exc).__name__}: {exc}")
    missing = [name for name in NEEDED if not (PAPER / name).exists()]
    status = {
        "method": method,
        "copied": sorted(set(copied)),
        "missing": missing,
        "failures": failures,
        "source": "ICLR/Master-Template official repository, iclr2026",
    }
    STATUS.write_text(json.dumps(status, indent=2), encoding="utf-8")
    print(json.dumps(status, indent=2))
    return 0 if not missing else 2


if __name__ == "__main__":
    raise SystemExit(main())
