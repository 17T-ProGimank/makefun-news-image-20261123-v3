#!/usr/bin/env python3
"""Entrypoint for the news-image-20261123 bounty, round 3.

Copies the pre-rendered front page for Monday 23 November 2026
(entry.png, 1024x1024, 40 sourced stories across 7 regions) into
$MAKEFUN_OUTPUT_DIR/entry.png.

Round 3 rebuild: a story-by-story audit of round 2 (40+ live source
checks) found three figures with the direction wrong -- Taiex closed
UP 2.16% on Monday, not down 0.9%; Europe ROSE on Monday (Stoxx +0.3%,
ASML +3.5%, DAX ~24,894), the "rout" was Friday's; the cricket match
ended in a DRAW, India did not win -- plus superseded tolls (Dymer
9 -> 11), a stale KOSPI close (-3.7% was the morning figure; the close
was -3.31%), a wrong day on the EU-Indonesia deal (signed Saturday,
not Sunday), a misdated ICJ ruling in the DATE CHECK box itself, and
three also-on items too stale to keep (Qeshm, Qatar mediation, Abyei).
Every figure on this page is now a verified Monday close or an
honestly dated weekend story; the ICJ ruling, the El Chapo Isidro
capture and BepiColombo's Mercury orbit join the poster as dated
stories, and the DATE CHECK box lists the stale stories left out.

Stdlib only, on purpose: the grader runs this in the pinned python
image, which ships no Pillow and no system fonts, so the program
itself must not import anything beyond the standard library. The
poster was drawn offline by draw_poster.py (Pillow + DejaVu Sans,
run locally) and the rendered bytes are committed here as entry.png;
copying them keeps the graded run byte-identical and deterministic.

Run locally:  python3 main.py
"""
import hashlib
import os
import sys

SOURCE_NAME = "entry.png"


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(repo_root, SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, SOURCE_NAME)
    with open(source, "rb") as f:
        data = f.read()
    with open(path, "wb") as f:
        f.write(data)
    print(f"entry written to {path}")
    print(f"bytes {len(data)}")
    print(f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
