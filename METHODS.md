# II. MEASUREMENT METHODOLOGY

## A. Study Area

The measurement campaign was conducted at a cellular base station located on the grounds of the Bisi Balogun Postgraduate Hostel, within the Federal University of Technology Akure (FUTA), Akure, Ondo State, Nigeria. FUTA is situated at approximately 7.298°N, 5.136°E in the south-western geopolitical zone of Nigeria. The study site presents a semi-urban propagation environment characterised by a mix of multi-storey residential buildings, a water tank enclosure, open green spaces, and pedestrian walkways — representative of the heterogeneous near-mast environments typical of West African campus installations.

The base of the measurement mast was geolocated at 7°17′52″N, 5°8′46″E, with a recorded elevation of approximately 1200 ft (365.8 m) above sea level. The tower is a **lattice-type structure** fitted with two multi-sector panel antennas and one microwave dish, serving the surrounding residential and academic zone. At the time of measurement, the serving cell was operated by **MTN Nigeria (MCC: 621, MNC: 30)** using **LTE Frequency-Division Duplex (FDD)** on **Band 7 (2600 MHz)**, with downlink centred at 2650.0 MHz and uplink at 2530.0 MHz. The recorded RSRP of −107 dBm and RSRQ of −18 dB at the test handset confirm a high-interference but low-absolute-power radiation environment at the measurement zone. Two additional neighbour cells were detected on Band 8 (900 MHz) and Band 3 (1800 MHz), but signal attribution for EMF measurement purposes was based on the serving cell.

The measurement campaign was performed on **23rd September 2025 at 12:10 PM local time**, under sunny weather at approximately 23 °C and with an estimated 56 active users on the serving cell — conditions broadly representative of daytime mid-load operation.

*[Figure 1 — Satellite map of the study site showing the base station (★) and the eight measurement distance rings (0, 5, 10, 20, 30, 50, 75, 100 ft). Insert captured Google Maps screenshot.]*

## B. Instrumentation

Electromagnetic field measurements were obtained using a calibrated **Trifield EMF Meter** (Model TF2), a broadband triple-axis instrument capable of simultaneously measuring the three principal components of the local electromagnetic environment. For each measurement point, the instrument provided both the **instantaneous (current) reading** and the **peak reading** observed over a short sampling interval (≈ 30 seconds), recorded separately. The quantities measured were:

| Symbol | Quantity | Unit | Meter Mode |
|---|---|---|---|
| **B_std** | Standard magnetic field | milliGauss (mG) | Flat frequency response |
| **E_std** | Standard electric field | Volts per metre (V/m) | Flat frequency response |
| **B_wtd** | Weighted magnetic field | milliGauss (mG) | Frequency-weighted |
| **E_wtd** | Weighted electric field | Volts per metre (V/m) | Frequency-weighted |
| **S_RF** | RF power density | milliWatts per square metre (mW/m²) | 20 MHz – 6 GHz |

For each of the above, both the *instantaneous* and *peak* values were retained, yielding **ten numerical observables per measurement point**. The peak channel captures the maximum field experienced during the sampling window and more conservatively represents short-term exposure, while the instantaneous channel represents the mean field during normal traffic activity. Both sets were carried through the analysis and modelled separately, consistent with the ICNIRP practice of distinguishing average and peak exposure in compliance assessment.

The GPS coordinates of every measurement point were logged using a smartphone GNSS receiver to enable spatial reproducibility. All readings were recorded by hand at the moment of acquisition and subsequently cross-verified during digitisation.

*[Figure 2 — Photograph of the Trifield TF2 meter and field measurement setup at the mast site. Insert photo.]*

## C. Spatial Sampling Design

A radial-grid sampling scheme was adopted, consistent with methodologies previously applied in Plets et al. (2021) and Abubakar et al. (2024). Eight radial distances were selected along the ground from the base of the mast:

> **0 ft, 5 ft, 10 ft, 20 ft, 30 ft, 50 ft, 75 ft, 100 ft**

corresponding to 0.00, 1.52, 3.05, 6.10, 9.14, 15.24, 22.86, and 30.48 metres respectively (using the standard conversion 1 ft = 0.3048 m). At each radial distance, readings were attempted along **eight cardinal and inter-cardinal bearings** (N, S, E, W, NE, NW, SE, SW), giving a theoretical grid of 8 × 8 = **64 measurement points**.

At each grid position, the Trifield meter was held at a height of 1.0–1.2 m above ground level — consistent with waist-height pedestrian exposure assessment — and oriented along the same axis throughout the campaign to avoid polarisation bias. A settling period was allowed before each reading, after which the displayed instantaneous and peak values were recorded.

## D. Obstacle Exclusion Protocol

Fifteen of the 64 grid positions were blocked by permanent structures (the hostel building wall and a large overhead water tank) and were therefore inaccessible to the meter. These positions were classified as **obstacle-excluded** and their GPS coordinates recorded for completeness but excluded from all distributional modelling:

| Distance | Excluded directions | Obstacle |
|---|---|---|
| 20 ft | SE | Overhead water tank |
| 30 ft | NE, NW | Building wall |
| 50 ft | NE, NW, SE, SW | Building wall |
| 75 ft | NE, NW, SE, SW | Building wall |
| 100 ft | NE, NW, SE, SW | Building wall |

After obstacle exclusion, **49 valid measurement positions** remained across the eight distances, yielding 49 × 10 = **490 numerical field observations** for subsequent statistical modelling. The per-distance sample count is summarised in Table 1.

**Table 1 — Valid sample size per radial distance (after obstacle exclusion)**

| Distance (ft) | Distance (m) | Valid n | Excluded |
|---|---|---|---|
| 0  | 0.00  | 8 | 0 |
| 5  | 1.52  | 8 | 0 |
| 10 | 3.05  | 8 | 0 |
| 20 | 6.10  | 7 | 1 |
| 30 | 9.14  | 6 | 2 |
| 50 | 15.24 | 4 | 4 |
| 75 | 22.86 | 4 | 4 |
| 100| 30.48 | 4 | 4 |
| **Total** | — | **49** | **15** |

## E. Data Preprocessing

Field readings were transcribed from the raw field-book into a structured CSV file (`field_measurements.csv`) with one row per grid position and twelve columns: `distance_ft`, `direction`, the ten measured observables, an `obstacle` boolean flag, and a free-text obstacle note. No imputation was performed for obstacle-excluded rows — these were carried as null values and filtered out prior to any statistical analysis.

Zero-valued observations, which predominate the standard-electric channel and several standard-magnetic rows, were **retained as valid data**. Unlike missing values, a zero reading encodes a meaningful physical observation — that the local field at the given position fell below the instrument's detection threshold — and its removal would introduce systematic upward bias in the estimated distribution parameters. For distributions defined strictly on the positive real line (Lognormal, Gamma, Weibull, Rayleigh, Exponential, Nakagami), a small numerical offset ε = 10⁻⁴ was added prior to parameter estimation to resolve the singularity at the origin; this offset is substantially smaller than the meter resolution (0.1 mG, 0.01 mW/m²) and has negligible effect on the fitted parameters.

Two measurement channels were subsequently excluded from distributional modelling:

- **Standard Electric (`E_std`)** — 47 of 49 readings equal zero; insufficient variation to support distribution fitting.
- **Standard Electric (peak) (`E_std_peak`)** — 46 of 49 readings equal zero, two outlier events (1.0 V/m at two positions).

Both channels are instead reported descriptively as being predominantly below the meter's detection floor, and this finding is itself discussed (Section VI) as evidence that electric-field exposure at the measurement zone is negligible.

## F. Candidate Probability Distributions

Seven continuous probability distributions were fitted to each of the seven retained measurement channels (RF instantaneous, RF peak, B_std, B_std peak, B_wtd, B_wtd peak, E_wtd peak). The candidate family was selected to span the modelling traditions found in EMF and propagation literature, covering symmetric, right-skewed, heavy-tailed, and fading-specific forms:

| Distribution | PDF *f(x; θ)* (x ≥ 0 where applicable) | Rationale for inclusion |
|---|---|---|
| **Normal** | (1/σ√2π) exp(−(x − μ)² / 2σ²) | Baseline symmetric model; expected for log-scaled RF [3] |
| **Lognormal** | (1/xσ√2π) exp(−(ln x − μ)² / 2σ²) | Theoretical model for shadow-faded received power [3][4] |
| **Gamma** | x^(k−1) e^(−x/θ) / (θ^k Γ(k)) | Flexible right-skewed alternative to Lognormal [7] |
| **Weibull** | (c/λ)(x/λ)^(c−1) exp(−(x/λ)^c) | Common for reliability and built-environment RF data [6] |
| **Rayleigh** | (x/σ²) exp(−x²/2σ²) | Classical flat-fading channel amplitude model |
| **Exponential** | (1/λ) exp(−x/λ) | Memoryless baseline; Gamma with k = 1 |
| **Nakagami** | (2m^m / Γ(m) Ω^m) x^(2m−1) exp(−m x²/Ω) | Multipath-dominated fading; m > 1 indicates mild fading [6][9] |

Parameters for each candidate were estimated by **Maximum Likelihood Estimation (MLE)** using the SciPy `scipy.stats` implementation (v1.13, Python 3.9). For distributions defined on x ≥ 0, the location parameter was fixed at zero (`floc = 0`) to prevent spurious negative shifts that would otherwise allow unconstrained fits to produce non-physical parameter values.

## G. Goodness-of-Fit Assessment

Four complementary goodness-of-fit procedures were applied to each (variable, distribution) pair:

1. **Kolmogorov–Smirnov (KS) test.** The supremum distance between the empirical CDF F_n(x) and the fitted theoretical CDF F̂(x) is computed:

    D_n = sup_x |F_n(x) − F̂(x)|

    The associated p-value (under the null hypothesis that the data follow the fitted distribution) is reported. A p-value > 0.05 is interpreted as failure to reject the hypothesis at the 5% level.

2. **Anderson–Darling (AD) test.** The AD statistic weights the tails of the distribution more heavily than KS, making it sensitive to misfit in the extremes:

    A² = −n − (1/n) Σᵢ (2i − 1)[ln F̂(xᵢ) + ln(1 − F̂(xₙ₊₁₋ᵢ))]

    The statistic is reported directly; lower values indicate a better fit.

3. **Shapiro–Wilk (SW) test.** Applied to the raw data (as a test for Normality) and to ln(x + ε) (as a test for Lognormality). A W statistic close to unity with p > 0.05 indicates consistency with the hypothesised form.

4. **Akaike Information Criterion (AIC).** For comparative ranking between non-nested candidates, AIC = 2k − 2·ln L̂ is computed, where *k* is the number of fitted parameters and L̂ is the maximised likelihood. Lower AIC indicates a better balance between fit and parsimony.

5. **Q–Q analysis.** For each variable, a quantile–quantile plot was generated against the best-fitting candidate (by KS p-value) to provide a visual verdict on tail behaviour and linearity of alignment.

The final best-fit designation for each variable was assigned to the distribution achieving the **highest KS p-value**, with AD and AIC used as secondary tie-breakers when KS p-values fell within ~0.1 of one another. Where the best KS p-value nonetheless fell below 0.05, the variable was declared to have **no acceptable fit** within the candidate family, and the failure mode was diagnosed (e.g., meter-resolution-induced quantisation).

## H. Distance-Decay Model

In addition to the purely distributional modelling, an empirical path-loss model was fitted to the directionally-averaged RF power density as a function of radial distance. A log-log ordinary least squares regression was performed on the mean RF at each valid distance:

    ln S̄_RF(d) = ln k − n · ln d     ⟹     S̄_RF(d) ≈ k · d^(−n)

where *n* is the empirical path-loss exponent and *k* is the near-field scaling constant. The coefficient of determination (R²) and the regression p-value quantify goodness-of-fit for the decay law. This second model, together with the winning distribution fitted to the direction-level residuals, constitutes the complete mathematical model of the EMF environment: the regression captures the **mean behaviour with distance**, and the distribution captures the **spatial variability at a given distance**.

## I. Computational Implementation

All analyses were implemented in a single reproducible Python script (`analysis.py`) using the following libraries: **NumPy 1.26** (numerical primitives), **SciPy 1.13** (distribution fitting, KS, Anderson–Darling, Shapiro–Wilk), **Pandas 2.2** (tabular I/O), and **Matplotlib 3.8** (plotting). The full source code and generated outputs are archived with this report and may be re-executed from the single command `python3 analysis.py` operating on the provided CSV, producing all tables and figures presented in Section V.
