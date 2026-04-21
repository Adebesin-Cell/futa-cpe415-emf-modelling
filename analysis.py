"""
CPE 415 — EMF Distribution Modelling
Fits candidate probability distributions to field measurements and ranks them
by goodness-of-fit. Produces CSV tables, markdown summary, and Q-Q + histogram
plots ready to paste into the Methods/Results sections.

Run:
    pip install numpy scipy pandas matplotlib
    python analysis.py
"""

from __future__ import annotations

import os
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

warnings.filterwarnings("ignore")

HERE = Path(__file__).parent
CSV_PATH = HERE / "field_measurements.csv"
OUT_DIR = HERE / "outputs"
PLOT_DIR = OUT_DIR / "plots"
OUT_DIR.mkdir(exist_ok=True)
PLOT_DIR.mkdir(exist_ok=True)

# --- Variables we model ------------------------------------------------------
# name -> (column, pretty label, unit)
VARIABLES = {
    "rf":               ("rf",               "RF Power Density",             "mW/m²"),
    "rf_peak":          ("rf_peak",          "RF Power Density (Peak)",      "mW/m²"),
    "std_magnetic":     ("std_magnetic",     "Standard Magnetic Field",      "mG"),
    "std_magnetic_peak":("std_magnetic_peak","Standard Magnetic Field (Pk)", "mG"),
    "wtd_magnetic":     ("wtd_magnetic",     "Weighted Magnetic Field",      "mG"),
    "wtd_magnetic_peak":("wtd_magnetic_peak","Weighted Magnetic Field (Pk)", "mG"),
    "wtd_electric_peak":("wtd_electric_peak","Weighted Electric Field (Pk)", "V/m"),
}

# Skip std_electric* — overwhelmingly zero (below meter detection threshold).
SKIP_REASON = {
    "std_electric": "All readings ~0.0 (below detection threshold) — no variation to model.",
    "std_electric_peak": "All readings ~0.0 except two outliers — insufficient variation to model.",
}

# --- Distributions to fit ----------------------------------------------------
# Each entry: scipy dist object, fit kwargs (floc=0 forces origin at 0 for
# distributions defined on x >= 0 — avoids phantom location parameters).
DISTRIBUTIONS = [
    ("Normal",      stats.norm,      {}),
    ("Lognormal",   stats.lognorm,   {"floc": 0}),
    ("Gamma",       stats.gamma,     {"floc": 0}),
    ("Weibull",     stats.weibull_min, {"floc": 0}),
    ("Rayleigh",    stats.rayleigh,  {"floc": 0}),
    ("Exponential", stats.expon,     {"floc": 0}),
    ("Nakagami",    stats.nakagami,  {"floc": 0}),
]

EPS = 1e-4  # small offset for log-based fits when data contains zeros


def load_data() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    return df[df["obstacle"] == False].reset_index(drop=True)  # noqa: E712


def extract_series(df: pd.DataFrame, col: str) -> np.ndarray:
    x = pd.to_numeric(df[col], errors="coerce").dropna().to_numpy()
    return x


def fit_and_test(x: np.ndarray, dist_name: str, dist, fit_kwargs: dict):
    """Fit a distribution and run KS + Anderson-Darling goodness-of-fit."""
    # Lognormal/Gamma/Rayleigh/Exp/Nakagami/Weibull need x > 0
    needs_positive = dist_name in {"Lognormal", "Gamma", "Rayleigh",
                                   "Exponential", "Nakagami", "Weibull"}
    data = x + EPS if needs_positive else x

    try:
        params = dist.fit(data, **fit_kwargs)
    except Exception as e:
        return {"dist": dist_name, "params": None, "ks_p": np.nan,
                "ad_stat": np.nan, "aic": np.nan, "error": str(e)}

    # KS test against fitted CDF
    try:
        ks_stat, ks_p = stats.kstest(data, dist.cdf, args=params)
    except Exception:
        ks_stat, ks_p = np.nan, np.nan

    # Anderson-Darling via transform (generic): A² = -n - (1/n) Σ (2i-1)[ln F + ln(1-F_rev)]
    try:
        sorted_data = np.sort(data)
        n = len(sorted_data)
        F = dist.cdf(sorted_data, *params)
        F = np.clip(F, 1e-10, 1 - 1e-10)
        i = np.arange(1, n + 1)
        ad_stat = -n - np.sum((2 * i - 1) * (np.log(F) + np.log(1 - F[::-1]))) / n
    except Exception:
        ad_stat = np.nan

    # AIC for comparative ranking
    try:
        log_lik = np.sum(dist.logpdf(data, *params))
        k = len(params)
        aic = 2 * k - 2 * log_lik
    except Exception:
        aic = np.nan

    return {"dist": dist_name, "params": params, "ks_stat": ks_stat,
            "ks_p": ks_p, "ad_stat": ad_stat, "aic": aic, "error": None}


def shapiro_tests(x: np.ndarray):
    """Shapiro-Wilk for Normal (on raw) and Lognormal (on log)."""
    out = {}
    if len(x) >= 3:
        try:
            w, p = stats.shapiro(x)
            out["sw_normal_W"] = w
            out["sw_normal_p"] = p
        except Exception:
            out["sw_normal_W"] = np.nan
            out["sw_normal_p"] = np.nan
        try:
            pos = x[x > 0]
            if len(pos) >= 3:
                w, p = stats.shapiro(np.log(pos + EPS))
                out["sw_lognormal_W"] = w
                out["sw_lognormal_p"] = p
        except Exception:
            out["sw_lognormal_W"] = np.nan
            out["sw_lognormal_p"] = np.nan
    return out


def plot_variable(x: np.ndarray, results: list, var_key: str, label: str, unit: str):
    """Histogram + fitted PDF overlays, and Q-Q plot for the best fit."""
    # --- Histogram + PDF overlays --
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(x, bins=min(12, max(5, len(x)//4)), density=True,
            alpha=0.45, edgecolor="black", label="Empirical")
    x_grid = np.linspace(max(x.min(), 0) + EPS, x.max() + EPS, 400)
    for r in results:
        if r["params"] is None:
            continue
        dist_obj = next(d for n, d, _ in DISTRIBUTIONS if n == r["dist"])
        try:
            pdf = dist_obj.pdf(x_grid, *r["params"])
            ax.plot(x_grid, pdf, lw=1.5, label=f"{r['dist']} (KS p={r['ks_p']:.3f})")
        except Exception:
            pass
    ax.set_title(f"{label} — Empirical vs Fitted Distributions")
    ax.set_xlabel(f"{label} ({unit})")
    ax.set_ylabel("Density")
    ax.legend(fontsize=8, loc="best")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / f"{var_key}_pdfs.png", dpi=150)
    plt.close(fig)

    # --- Q-Q plot for best fit by KS p-value --
    valid = [r for r in results if r["params"] is not None and not np.isnan(r["ks_p"])]
    if not valid:
        return
    best = max(valid, key=lambda r: r["ks_p"])
    dist_obj = next(d for n, d, _ in DISTRIBUTIONS if n == best["dist"])
    fig, ax = plt.subplots(figsize=(6, 6))
    needs_positive = best["dist"] in {"Lognormal", "Gamma", "Rayleigh",
                                      "Exponential", "Nakagami", "Weibull"}
    data = x + EPS if needs_positive else x
    stats.probplot(data, dist=dist_obj, sparams=best["params"], plot=ax)
    ax.set_title(f"{label} — Q-Q Plot ({best['dist']})")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / f"{var_key}_qq_{best['dist']}.png", dpi=150)
    plt.close(fig)


def summarise(x: np.ndarray) -> dict:
    return {
        "n":     len(x),
        "mean":  float(np.mean(x)),
        "std":   float(np.std(x, ddof=1)) if len(x) > 1 else np.nan,
        "min":   float(np.min(x)),
        "max":   float(np.max(x)),
        "median":float(np.median(x)),
        "zeros": int(np.sum(x == 0)),
    }


def format_params(dist_name, params):
    if params is None:
        return "—"
    if dist_name == "Normal":        return f"μ={params[0]:.4f}, σ={params[1]:.4f}"
    if dist_name == "Lognormal":     return f"s={params[0]:.4f}, scale={params[2]:.4f}"
    if dist_name == "Gamma":         return f"a={params[0]:.4f}, scale={params[2]:.4f}"
    if dist_name == "Weibull":       return f"c={params[0]:.4f}, scale={params[2]:.4f}"
    if dist_name == "Rayleigh":      return f"scale={params[1]:.4f}"
    if dist_name == "Exponential":   return f"scale={params[1]:.4f}"
    if dist_name == "Nakagami":      return f"nu={params[0]:.4f}, scale={params[2]:.4f}"
    return ", ".join(f"{p:.4f}" for p in params)


def distance_regression(df: pd.DataFrame, col: str):
    """Fit RF(d) ∝ d^-n using log-log OLS on distance-averaged data."""
    valid = df[df["obstacle"] == False].copy()  # noqa: E712
    valid[col] = pd.to_numeric(valid[col], errors="coerce")
    agg = valid.groupby("distance_ft")[col].mean().reset_index()
    # include only d > 0 and value > 0
    m = (agg["distance_ft"] > 0) & (agg[col] > 0)
    d = agg.loc[m, "distance_ft"].to_numpy(dtype=float)
    v = agg.loc[m, col].to_numpy(dtype=float)
    if len(d) < 3:
        return None
    slope, intercept, r, p, se = stats.linregress(np.log(d), np.log(v))
    return {
        "exponent_n":    -slope,
        "k_coefficient": float(np.exp(intercept)),
        "r_squared":     r ** 2,
        "p_value":       p,
        "n_points":      len(d),
        "mean_per_distance": agg.to_dict(orient="records"),
    }


def main():
    df = load_data()
    print(f"Loaded {len(df)} valid readings across "
          f"{df['distance_ft'].nunique()} distances.\n")

    all_summary_rows = []
    md = ["# CPE 415 — Distribution Modelling Results\n"]
    md.append(f"Data source: `{CSV_PATH.name}`  \n")
    md.append(f"Valid readings (obstacle rows excluded): **{len(df)}**\n")

    for key, (col, label, unit) in VARIABLES.items():
        x = extract_series(df, col)
        if len(x) == 0:
            continue

        summ = summarise(x)
        sw = shapiro_tests(x)

        print(f"=== {label} ({unit}) — n={summ['n']}, "
              f"mean={summ['mean']:.4f}, std={summ['std']:.4f}, "
              f"zeros={summ['zeros']} ===")

        results = []
        for dist_name, dist, kwargs in DISTRIBUTIONS:
            r = fit_and_test(x, dist_name, dist, kwargs)
            results.append(r)

        # Rank by KS p-value descending (higher p = better fit)
        ranked = sorted(
            [r for r in results if not np.isnan(r.get("ks_p", np.nan))],
            key=lambda r: r["ks_p"], reverse=True
        )
        best = ranked[0] if ranked else None

        # Plots
        plot_variable(x, results, key, label, unit)

        # CSV row per distribution
        for r in results:
            all_summary_rows.append({
                "variable": label,
                "unit": unit,
                "n": summ["n"],
                "mean": summ["mean"],
                "std": summ["std"],
                "distribution": r["dist"],
                "parameters": format_params(r["dist"], r["params"]),
                "ks_stat": r.get("ks_stat"),
                "ks_p_value": r.get("ks_p"),
                "ad_stat": r.get("ad_stat"),
                "aic": r.get("aic"),
                "sw_normal_W": sw.get("sw_normal_W"),
                "sw_normal_p": sw.get("sw_normal_p"),
                "sw_lognormal_W": sw.get("sw_lognormal_W"),
                "sw_lognormal_p": sw.get("sw_lognormal_p"),
            })

        # Markdown section
        md.append(f"\n## {label} ({unit})\n")
        md.append(f"- n = {summ['n']}, mean = {summ['mean']:.4f}, "
                  f"std = {summ['std']:.4f}, "
                  f"min = {summ['min']:.4f}, max = {summ['max']:.4f}, "
                  f"zeros = {summ['zeros']}")
        md.append(f"- Shapiro-Wilk (Normal): W={sw.get('sw_normal_W', float('nan')):.4f}, "
                  f"p={sw.get('sw_normal_p', float('nan')):.4f}")
        if "sw_lognormal_W" in sw:
            md.append(f"- Shapiro-Wilk (Lognormal, on ln x): "
                      f"W={sw['sw_lognormal_W']:.4f}, p={sw['sw_lognormal_p']:.4f}")

        md.append("\n| Distribution | Parameters | KS stat | KS p | AD stat | AIC |")
        md.append("|---|---|---|---|---|---|")
        for r in sorted(results, key=lambda r: (-r["ks_p"]
                                                if not np.isnan(r.get("ks_p", np.nan))
                                                else 1)):
            md.append(
                f"| {r['dist']} | {format_params(r['dist'], r['params'])} | "
                f"{r.get('ks_stat', float('nan')):.4f} | "
                f"{r.get('ks_p', float('nan')):.4f} | "
                f"{r.get('ad_stat', float('nan')):.4f} | "
                f"{r.get('aic', float('nan')):.2f} |"
            )

        if best:
            verdict = ("strong fit" if best["ks_p"] > 0.10 else
                       "acceptable fit" if best["ks_p"] > 0.05 else
                       "borderline fit" if best["ks_p"] > 0.01 else
                       "poor fit")
            md.append(f"\n**Best fit: {best['dist']}** — KS p = {best['ks_p']:.4f} "
                      f"({verdict}).  Model parameters: {format_params(best['dist'], best['params'])}")

        print()

    # Distance regression for RF
    md.append("\n## Distance-decay regression — RF Power Density\n")
    reg = distance_regression(df, "rf")
    if reg:
        md.append(f"Log-log OLS fit of mean RF vs. distance: "
                  f"**RF(d) ≈ {reg['k_coefficient']:.4f} · d^(-{reg['exponent_n']:.3f})**  ")
        md.append(f"R² = {reg['r_squared']:.4f}, p = {reg['p_value']:.4f}, "
                  f"points = {reg['n_points']}\n")
        md.append("| Distance (ft) | Mean RF (mW/m²) |")
        md.append("|---|---|")
        for row in reg["mean_per_distance"]:
            md.append(f"| {int(row['distance_ft'])} | {row['rf']:.4f} |")

    # Skipped variables
    if SKIP_REASON:
        md.append("\n## Variables not modelled\n")
        for k, why in SKIP_REASON.items():
            md.append(f"- **{k}**: {why}")

    pd.DataFrame(all_summary_rows).to_csv(OUT_DIR / "fit_results.csv", index=False)
    (OUT_DIR / "report.md").write_text("\n".join(md))
    print(f"Wrote {OUT_DIR/'fit_results.csv'}")
    print(f"Wrote {OUT_DIR/'report.md'}")
    print(f"Plots in {PLOT_DIR}")


if __name__ == "__main__":
    main()
