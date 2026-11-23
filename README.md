[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/17T-ProGimank/makefun-news-image-20261123-v3/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/17T-ProGimank/makefun-news-image-20261123-v3/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World in One Day — Monday 23 November 2026 (round 3)

**40 sourced stories, 7 regions — Monday's AI rout, NATO meets over Poland, Cikande toll 24, all figures checked against Monday's closes.**

Round 3 rebuild of the 23 November front page. All three leads are genuine
Monday 23 November 2026 events: the AI sell-off hits Seoul on Monday
(KOSPI closes −3.31% at 4,708.54), NATO's council meets in Brussels over
the Russian missiles that entered Poland, and the Cikande candy-factory
fire toll rises to 24. Plus 22 numbered stories, 15 more in "Also on", a
12-pin world map, a Monday markets ticker, a BY THE NUMBERS strip in
Monday figures, and a DATE CHECK box listing the stale stories
deliberately left out.

What round 3 fixes vs round 2 (audited story by story, 40+ live source
checks): three figures had the direction wrong — Taiex closed UP 2.16%
on Monday, not down 0.9%; Europe ROSE on Monday (Stoxx +0.3%, ASML
+3.5%, DAX ~24,894), the "rout" was Friday's; the cricket match ended
in a DRAW (NZ 239/5), India did not win. The Dymer toll rose 9 → 11
during Monday; the KOSPI −3.7% was a morning figure (close −3.31%);
the EU–Indonesia deal was signed Saturday, not Sunday; the DATE CHECK
box itself misdated the ICJ ruling (Thursday 19 Nov, not Friday). The
Ebola count is now the CDC DR Congo figure (11,680 cases, 5,715 dead),
the IIT Patna AI centre is ₹60-crore (the ₹400-crore is the research
park), and three too-stale also-on items (Qeshm strike, Qatar mediation,
Abyei mandate) are dropped — while the ICJ ruling, the El Chapo Isidro
capture and BepiColombo's Mercury orbit join the poster as honestly
dated stories. Every weekend story is dated Thu/Fri/Sat/Sun in its fact
line, and the DATE CHECK box states that rule.

- **Bounty:** [news-image-20261123 on make.fun](https://make.fun/bounty/news-image-20261123)
- **Entry:** `main.py` (Python 3.13, stdlib only) copies the pre-rendered
  `entry.png` (1024×1024, 40 stories) to `$MAKEFUN_OUTPUT_DIR/entry.png`.
  The poster was drawn offline by `draw_poster.py` (Pillow + DejaVu, run
  locally) because the grader's pinned Python image ships no Pillow and no
  system fonts — the entrypoint itself imports nothing beyond the standard
  library.
- **Verification:** every story is attributed to its source with a
  CONFIRMED (2+ outlets) / OFFICIAL (on the record) / REPORTED (1 outlet)
  badge; the DATE CHECK box names the stories left out on purpose. Two
  local runs are byte-identical.

Built with [make.fun](https://make.fun/r/m4psg5rh) — my referral link.
