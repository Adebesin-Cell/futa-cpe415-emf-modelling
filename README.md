# CPE 415 — Statistical Distribution Modelling of EMF Exposure Around a Cellular Base Station

> **Federal University of Technology Akure (FUTA) — Department of Electrical & Electronics Engineering**
> Mathematical Modelling Course Project, Session 2025/2026
> Submission deadline: **24 April 2026**

## What this project is (plain English)

We already recorded field measurements at the MTN LTE mast near Bisi Balogun Hostel last semester (EEE304): RF power density, standard & weighted magnetic fields, and electric fields at 8 distances × 8 compass bearings around the tower.

For CPE 415 we take those numbers and **figure out which probability distribution describes them best** — Normal, Lognormal, Gamma, Weibull, Rayleigh, Exponential, Nakagami. We fit each candidate with Maximum Likelihood, run standard goodness-of-fit tests (Kolmogorov–Smirnov, Anderson–Darling, Shapiro–Wilk), rank them by AIC, and pick a winner per variable. That winning distribution — with our fitted parameters plugged in — **is our mathematical model**.

In other words: *"given a position around the mast, predict (or validate) what the meter would show, using a probability distribution calibrated to our own data."*

## Repository layout

```
mts-415/
├── field_measurements.csv       ← the single source of truth (49 valid + 15 obstacle rows)
├── analysis.py                  ← runs the full modelling pipeline
├── md_to_docx.py                ← converts the Markdown deliverables into .docx
├── METHODS.md                   ← Section II of the report (ready to paste)
├── README.md                    ← this file
└── outputs/
    ├── report.md                ← Results + distance regression + excluded variables
    ├── fit_results.csv          ← master table: every variable × every distribution × every test
    ├── CPE415_Methods.docx      ← generated Word file
    ├── CPE415_Results.docx      ← generated Word file
    └── plots/
        ├── rf_pdfs.png, rf_qq_Lognormal.png   (and the rest per variable)
        └── ...
```

## How to run it

```bash
pip install numpy scipy pandas matplotlib python-docx
python3 analysis.py          # re-fits distributions, regenerates tables + plots
python3 md_to_docx.py         # converts METHODS.md, report.md, README.md → .docx
```

Everything regenerates from `field_measurements.csv` in ~2 seconds. If anyone spots a transcription error in the raw data, edit the CSV and re-run — no hand-editing of tables.

## The data (one-line summary)

- **Site:** Bisi Balogun Postgraduate Hostel, FUTA (7°17′52″N, 5°8′46″E), 23 Sept 2025, 12:10 PM
- **Mast:** Lattice tower, MTN Nigeria, LTE Band 7 (2600 MHz), FDD
- **Instrument:** Trifield TF2 (E-field V/m, B-field mG, RF mW/m²)
- **Grid:** 8 radial distances (0, 5, 10, 20, 30, 50, 75, 100 ft) × 8 directions (N, NE, E, SE, S, SW, W, NW)
- **Channels:** 5 quantities × 2 (instantaneous + peak) = 10 numbers per grid point
- **Valid readings:** 49 (15 obstacle points excluded — tank at 20 ft SE, buildings NE/NW/SE/SW beyond 30 ft)

## Headline results

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

**Secondary finding:** Mean RF *increases* with distance from the mast (empirical exponent ≈ −0.36, R² = 0.69). This is not an error — it reflects the radiation pattern of downtilted sector antennas, which project energy outward rather than straight down. The base of the mast sits in a partial "RF shadow" zone. Our own measurement report notes this: *"Standing directly under or near the mast still remains within compliance zones due to directional antennas focusing energy outward, not downward."*

**Safety:** Maximum RF reading (0.83 mW/m²) is **~12,000× below** the ICNIRP public reference level of 10 W/m² at 2–3 GHz. No public-health concern at the measurement zone.

## Who does what (group workflow)

| Section | Owner | Status |
|---|---|---|
| Data digitisation & CSV | Lope | ✅ done |
| Python analysis pipeline | Lope | ✅ done |
| Methods (Section II) | Lope | ✅ draft (`METHODS.md`) |
| Results & Discussion (Section V) | TBD | 🟡 outline ready in `outputs/report.md` |
| Introduction + Literature (Section I) | TBD | ⬜ |
| Regulatory Compliance (Section VI) | TBD | ⬜ |
| Conclusion (Section VII) | TBD | ⬜ |
| Formatting + references | TBD | ⬜ |

## Submission plan

1. **Early submission (Methods + Results only):** email `softcopyfiles001@gmail.com` with `CPE415_Methods.docx` + `CPE415_Results.docx` for lecturer feedback.
2. **Apply feedback**, finish Introduction + Conclusion, merge into a single report.
3. **Final submission** — hard copy via group rep, soft copy to the same email — **before 24 April 2026**.

## Credits

CPE Group 4 — FUTA Class of 2026:
Andre Clement Olanrewaju · Bodunde Boluwatife Michael · Olamiye Oluwagbeminiyi Emmanuel · Omoloju Champion Temilorun · Idoko Owoicho Louis · Ajayi David Ebenezer · Muhammed Sheriff Otaru · Yusuf Mariam Kanyinsola

Supervised by Engr. Charles Udekwe, Department of Electrical & Electronics Engineering, FUTA.
