# CPE 415 — Statistical Distribution Modelling of EMF Exposure Around a Cellular Base Station

> **FUTA — Department of Electrical & Electronics Engineering · Mathematical Modelling Project · 2025/2026 Session**
> Submission deadline: **24 April 2026**

---

## 📌 Hey group — start here

Below is a section-by-section table with **exactly what to download for your assigned part**. Click the file, hit the download button on GitHub, open it in Word, and you're good. Everything has been pre-computed — the tables, the plots, the Methods section — you just need to write the surrounding narrative for your section and cite what's already here.

### 📥 Where to download what

| Your section | Click to download | What's inside you can paste straight in |
|---|---|---|
| **Introduction & Literature Review** | [`README.md`](README.md) + [`outputs/report.md`](outputs/report.md) | Problem statement, context, headline results summary. Use the Background/Motivation prompts in *What this project is* below, plus the citations listed in `METHODS.md`. |
| **Methods (Section II)** | [`METHODS.md`](METHODS.md) · [`outputs/CPE415_Methods.docx`](outputs/CPE415_Methods.docx) | ✅ **Already written.** Open the .docx in Word, touch up formatting/figures, done. |
| **Results & Discussion (Section V)** | [`outputs/report.md`](outputs/report.md) · [`outputs/CPE415_Results.docx`](outputs/CPE415_Results.docx) · [`outputs/fit_results.csv`](outputs/fit_results.csv) · [`outputs/plots/`](outputs/plots) | Every fitted distribution, every KS/AD/SW/AIC value, every best-fit verdict, the distance-regression output. Plots are in `outputs/plots/`. |
| **Regulatory Compliance (Section VI)** | Key numbers below ⬇ | Our max RF = **0.83 mW/m²**. ICNIRP public limit at 2–3 GHz = **10 000 mW/m²**. Ratio = **~12 000× below limit**. Cite ICNIRP 2020 Guidelines. |
| **Conclusion (Section VII)** | [`outputs/report.md`](outputs/report.md) | Summarise: Lognormal wins for RF (KS p = 0.977), magnetic-field quantisation issue, E-field below detection floor, safety compliant. |
| **References / formatting** | [`METHODS.md`](METHODS.md) | Numbered citations [1]–[10] already used in Methods — extend the same list. |

### 🟢 Start here if you're new to the repo
1. Open [`METHODS.md`](METHODS.md) — read it top to bottom. That's the spine of the report.
2. Open [`outputs/report.md`](outputs/report.md) — that's what every fitted distribution looks like.
3. Browse [`outputs/plots/`](outputs/plots) — those are the figures for the Results section.

---

## What this project is (plain English)

We already recorded field measurements at the MTN LTE mast near Bisi Balogun Hostel last semester (EEE304): RF power density, standard & weighted magnetic fields, and electric fields at 8 distances × 8 compass bearings around the tower.

For CPE 415 we took those numbers and **figured out which probability distribution describes them best** — Normal, Lognormal, Gamma, Weibull, Rayleigh, Exponential, Nakagami. We fitted each candidate with Maximum Likelihood, ran standard goodness-of-fit tests (Kolmogorov–Smirnov, Anderson–Darling, Shapiro–Wilk), ranked them by AIC, and picked a winner per variable. That winning distribution — with our fitted parameters plugged in — **is our mathematical model**.

In other words: *"given a position around the mast, predict (or validate) what the meter would show, using a probability distribution calibrated to our own data."*

---

## 🎯 Headline results

| Variable | n | Best-fit distribution | KS p-value | Verdict |
|---|---|---|---|---|
| **RF Power Density** | 49 | **Lognormal** (s = 0.72, scale = 0.12) | **0.977** | Strong fit ✓ |
| **RF Power Density (Peak)** | 49 | **Gamma** (a = 2.45, scale = 0.087) | **0.783** | Strong fit ✓ |
| Standard Magnetic | 49 | Normal | 0.000 | Meter resolution (0.1 mG) limits fit |
| Standard Magnetic (Peak) | 49 | Weibull | 0.000 | Same quantisation issue |
| Weighted Magnetic | 49 | Nakagami | 0.000 | Same |
| Weighted Magnetic (Peak) | 49 | Rayleigh | 0.000 | Same |
| Weighted Electric (Peak) | 49 | — | — | 35/49 zeros; below meter detection floor |

**Headline finding:** RF power density follows a **Lognormal distribution** — consistent with shadow-fading propagation theory and matching independent results from comparable Nigerian (Olatunde 2022) and Rwandan (Nshizirungu 2021) studies.

**Secondary finding:** Mean RF *increases* with distance from the mast (empirical exponent ≈ −0.36, R² = 0.69). Not an error — reflects the radiation pattern of downtilted sector antennas, which project energy outward rather than straight down. The base of the mast sits in a partial "RF shadow" zone.

**Safety:** Maximum RF reading (0.83 mW/m²) is **~12 000× below** the ICNIRP public reference level of 10 W/m² at 2–3 GHz. No public-health concern at the measurement zone.

---

## 📁 Repository layout

```
mts-415/
├── README.md                   ← this file (project overview, download guide)
├── METHODS.md                  ← Section II — Methodology (done)
├── analysis.py                 ← the Python pipeline (fits all distributions)
├── md_to_docx.py               ← converts .md → .docx for easy Word editing
├── field_measurements.csv      ← source of truth: 49 valid + 15 obstacle rows
└── outputs/
    ├── report.md               ← Results draft (all tables + verdicts)
    ├── fit_results.csv         ← master table: every (variable × distribution) × test stats
    ├── CPE415_Methods.docx     ← Methods in Word, ready to drop into the report
    ├── CPE415_Results.docx     ← Results in Word
    ├── CPE415_README.docx      ← this README in Word
    └── plots/
        ├── rf_pdfs.png, rf_qq_Lognormal.png
        ├── rf_peak_pdfs.png, rf_peak_qq_Gamma.png
        ├── std_magnetic_*.png, wtd_magnetic_*.png, wtd_electric_peak_*.png
        └── (14 figures in total)
```

---

## The data (one-line summary)

- **Site:** Bisi Balogun Postgraduate Hostel, FUTA (7°17′52″N, 5°8′46″E), 23 Sept 2025, 12:10 PM
- **Mast:** Lattice tower, MTN Nigeria, LTE Band 7 (2600 MHz), FDD
- **Instrument:** Trifield TF2 (E-field V/m, B-field mG, RF mW/m²)
- **Grid:** 8 radial distances (0, 5, 10, 20, 30, 50, 75, 100 ft) × 8 directions (N, NE, E, SE, S, SW, W, NW)
- **Channels:** 5 quantities × 2 (instantaneous + peak) = 10 numbers per grid point
- **Valid readings:** 49 (15 obstacle points excluded — tank at 20 ft SE, buildings NE/NW/SE/SW beyond 30 ft)

---

## 👥 Who does what

| Section | Owner | Status |
|---|---|---|
| Data digitisation & CSV | Lope | ✅ done |
| Python analysis pipeline | Lope | ✅ done |
| **Methods (Section II)** | Lope | ✅ done — `METHODS.md` + `outputs/CPE415_Methods.docx` |
| Results & Discussion (Section V) | TBD | 🟡 draft ready in `outputs/report.md` |
| Introduction + Literature (Section I) | TBD | ⬜ |
| Regulatory Compliance (Section VI) | TBD | ⬜ |
| Conclusion (Section VII) | TBD | ⬜ |
| Formatting + references | TBD | ⬜ |

**Claim a section in the group chat and update this table when you start.**

---

## 🔧 Reproducing the analysis locally (optional)

Only needed if you want to re-run the pipeline, change the CSV, or regenerate plots. If you're just writing — you don't need to run anything; the outputs are already in `outputs/`.

```bash
pip install numpy scipy pandas matplotlib python-docx
python3 analysis.py       # fits distributions, regenerates outputs/report.md + plots
python3 md_to_docx.py     # converts .md → .docx
```

Everything regenerates from `field_measurements.csv` in ~2 seconds.
---

## 🙌 Credits

**CPE Group 4 — FUTA Class of 2026**
Andre Clement Olanrewaju · Bodunde Boluwatife Michael · Olamiye Oluwagbeminiyi Emmanuel · Omoloju Champion Temilorun · Idoko Owoicho Louis · Ajayi David Ebenezer · Muhammed Sheriff Otaru · Yusuf Mariam Kanyinsola

Supervised by **Engr. Charles Udekwe**, Department of Electrical & Electronics Engineering, FUTA.
