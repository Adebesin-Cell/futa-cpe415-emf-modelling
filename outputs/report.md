# CPE 415 — Distribution Modelling Results

Data source: `field_measurements.csv`  

Valid readings (obstacle rows excluded): **49**


## RF Power Density (mW/m²)

- n = 49, mean = 0.1541, std = 0.1197, min = 0.0120, max = 0.6430, zeros = 0
- Shapiro-Wilk (Normal): W=0.7990, p=0.0000
- Shapiro-Wilk (Lognormal, on ln x): W=0.9799, p=0.5596

| Distribution | Parameters | KS stat | KS p | AD stat | AIC |
|---|---|---|---|---|---|
| Lognormal | s=0.7162, scale=0.1207 | 0.0652 | 0.9765 | 0.2542 | -94.90 |
| Gamma | a=2.1904, scale=0.0704 | 0.1032 | 0.6362 | 0.5649 | -93.24 |
| Weibull | c=1.4490, scale=0.1715 | 0.1212 | 0.4341 | 0.9245 | -89.66 |
| Nakagami | nu=0.6411, scale=0.1945 | 0.1606 | 0.1427 | 1.5037 | -85.33 |
| Normal | μ=0.1541, σ=0.1185 | 0.1951 | 0.0414 | 2.8707 | -65.98 |
| Exponential | scale=0.1542 | 0.2079 | 0.0246 | 3.0093 | -81.20 |
| Rayleigh | scale=0.1375 | 0.2179 | 0.0160 | 4.1331 | -79.63 |

**Best fit: Lognormal** — KS p = 0.9765 (strong fit).  Model parameters: s=0.7162, scale=0.1207

## RF Power Density (Peak) (mW/m²)

- n = 49, mean = 0.2126, std = 0.1509, min = 0.0260, max = 0.8310, zeros = 0
- Shapiro-Wilk (Normal): W=0.8260, p=0.0000
- Shapiro-Wilk (Lognormal, on ln x): W=0.9786, p=0.5070

| Distribution | Parameters | KS stat | KS p | AD stat | AIC |
|---|---|---|---|---|---|
| Gamma | a=2.4535, scale=0.0867 | 0.0906 | 0.7825 | 0.4690 | -65.34 |
| Lognormal | s=0.6780, scale=0.1711 | 0.1007 | 0.6662 | 0.3915 | -66.03 |
| Weibull | c=1.5573, scale=0.2383 | 0.1120 | 0.5334 | 0.7556 | -61.90 |
| Nakagami | nu=0.7202, scale=0.2599 | 0.1379 | 0.2826 | 1.0903 | -58.99 |
| Normal | μ=0.2126, σ=0.1494 | 0.1716 | 0.0990 | 2.1304 | -43.28 |
| Rayleigh | scale=0.1838 | 0.1920 | 0.0468 | 2.3825 | -57.03 |
| Exponential | scale=0.2127 | 0.2588 | 0.0022 | 3.5003 | -49.70 |

**Best fit: Gamma** — KS p = 0.7825 (strong fit).  Model parameters: a=2.4535, scale=0.0867

## Standard Magnetic Field (mG)

- n = 49, mean = 0.1002, std = 0.0296, min = 0.0000, max = 0.2100, zeros = 2
- Shapiro-Wilk (Normal): W=0.3872, p=0.0000
- Shapiro-Wilk (Lognormal, on ln x): W=0.2082, p=0.0000

| Distribution | Parameters | KS stat | KS p | AD stat | AIC |
|---|---|---|---|---|---|
| Normal | μ=0.1002, σ=0.0293 | 0.4620 | 0.0000 | 14.7257 | -202.86 |
| Lognormal | s=1.3803, scale=0.0777 | 0.5318 | 0.0000 | 16.6953 | -73.68 |
| Weibull | c=2.4825, scale=0.1063 | 0.5366 | 0.0000 | 16.3181 | -159.33 |
| Gamma | a=2.1142, scale=0.0474 | 0.5495 | 0.0000 | 16.5390 | -134.33 |
| Rayleigh | scale=0.0739 | 0.5597 | 0.0000 | 16.7668 | -158.29 |
| Nakagami | nu=0.9784, scale=0.1045 | 0.5615 | 0.0000 | 16.8123 | -156.30 |
| Exponential | scale=0.1003 | 0.5906 | 0.0000 | 17.8787 | -123.36 |

**Best fit: Normal** — KS p = 0.0000 (poor fit).  Model parameters: μ=0.1002, σ=0.0293

## Standard Magnetic Field (Pk) (mG)

- n = 49, mean = 0.2020, std = 0.0661, min = 0.1000, max = 0.4000, zeros = 0
- Shapiro-Wilk (Normal): W=0.7919, p=0.0000
- Shapiro-Wilk (Lognormal, on ln x): W=0.7665, p=0.0000

| Distribution | Parameters | KS stat | KS p | AD stat | AIC |
|---|---|---|---|---|---|
| Weibull | c=3.2969, scale=0.2250 | 0.3235 | 0.0000 | 5.0689 | -122.08 |
| Nakagami | nu=2.4931, scale=0.2125 | 0.3279 | 0.0000 | 5.2972 | -123.42 |
| Normal | μ=0.2020, σ=0.0654 | 0.3288 | 0.0000 | 5.2091 | -124.16 |
| Gamma | a=8.9267, scale=0.0226 | 0.3489 | 0.0000 | 5.5356 | -122.65 |
| Lognormal | s=0.3501, scale=0.1909 | 0.3696 | 0.0000 | 5.9237 | -120.09 |
| Rayleigh | scale=0.1502 | 0.4044 | 0.0000 | 6.7374 | -107.25 |
| Exponential | scale=0.2021 | 0.4447 | 0.0000 | 12.1890 | -54.68 |

**Best fit: Weibull** — KS p = 0.0000 (poor fit).  Model parameters: c=3.2969, scale=0.2250

## Weighted Magnetic Field (mG)

- n = 49, mean = 0.1245, std = 0.0925, min = 0.0000, max = 0.7000, zeros = 1
- Shapiro-Wilk (Normal): W=0.3602, p=0.0000
- Shapiro-Wilk (Lognormal, on ln x): W=0.4381, p=0.0000

| Distribution | Parameters | KS stat | KS p | AD stat | AIC |
|---|---|---|---|---|---|
| Nakagami | nu=0.6924, scale=0.1546 | 0.4195 | 0.0000 | 11.0374 | -109.12 |
| Gamma | a=2.4139, scale=0.0516 | 0.4365 | 0.0000 | 10.8494 | -117.22 |
| Weibull | c=1.5281, scale=0.1376 | 0.4388 | 0.0000 | 10.9027 | -115.31 |
| Normal | μ=0.1245, σ=0.0915 | 0.4422 | 0.0000 | 11.4665 | -91.26 |
| Lognormal | s=1.0582, scale=0.0999 | 0.4805 | 0.0000 | 12.5856 | -75.18 |
| Rayleigh | scale=0.1093 | 0.4943 | 0.0000 | 12.4157 | -106.05 |
| Exponential | scale=0.1246 | 0.5318 | 0.0000 | 13.2699 | -102.11 |

**Best fit: Nakagami** — KS p = 0.0000 (poor fit).  Model parameters: nu=0.6924, scale=0.1546

## Weighted Magnetic Field (Pk) (mG)

- n = 49, mean = 0.1265, std = 0.0491, min = 0.1000, max = 0.3000, zeros = 0
- Shapiro-Wilk (Normal): W=0.5647, p=0.0000
- Shapiro-Wilk (Lognormal, on ln x): W=0.5638, p=0.0000

| Distribution | Parameters | KS stat | KS p | AD stat | AIC |
|---|---|---|---|---|---|
| Rayleigh | scale=0.0959 | 0.4200 | 0.0000 | 9.0924 | -149.40 |
| Weibull | c=2.6813, scale=0.1426 | 0.4339 | 0.0000 | 9.6349 | -154.62 |
| Normal | μ=0.1265, σ=0.0486 | 0.4627 | 0.0000 | 10.7197 | -153.40 |
| Lognormal | s=0.3173, scale=0.1196 | 0.4676 | 0.0000 | 11.2071 | -175.57 |
| Gamma | a=8.9039, scale=0.0142 | 0.4677 | 0.0000 | 11.0851 | -168.37 |
| Nakagami | nu=2.1392, scale=0.1356 | 0.4699 | 0.0000 | 10.9553 | -160.72 |
| Exponential | scale=0.1266 | 0.5464 | 0.0000 | 13.5527 | -100.52 |

**Best fit: Rayleigh** — KS p = 0.0000 (poor fit).  Model parameters: scale=0.0959

## Weighted Electric Field (Pk) (V/m)

- n = 49, mean = 0.4694, std = 0.7933, min = 0.0000, max = 2.0000, zeros = 35
- Shapiro-Wilk (Normal): W=0.5956, p=0.0000
- Shapiro-Wilk (Lognormal, on ln x): W=0.6160, p=0.0001

| Distribution | Parameters | KS stat | KS p | AD stat | AIC |
|---|---|---|---|---|---|
| Weibull | c=0.2159, scale=0.0167 | 0.4324 | 0.0000 | 9.6097 | -328.14 |
| Normal | μ=0.4694, σ=0.7851 | 0.4393 | 0.0000 | 9.6836 | 119.35 |
| Lognormal | s=4.3657, scale=0.0016 | 0.4506 | 0.0000 | 10.6788 | -342.76 |
| Gamma | a=0.1367, scale=3.4332 | 0.4586 | 0.0000 | 9.8396 | -321.19 |
| Nakagami | nu=0.0669, scale=0.9148 | 0.4590 | 0.0000 | 9.9387 | -324.85 |
| Exponential | scale=0.4695 | 0.7141 | 0.0000 | 175.6102 | 27.90 |
| Rayleigh | scale=0.6468 | 0.7143 | 0.0000 | 420.6674 | 648.86 |

**Best fit: Weibull** — KS p = 0.0000 (poor fit).  Model parameters: c=0.2159, scale=0.0167

## Distance-decay regression — RF Power Density

Log-log OLS fit of mean RF vs. distance: **RF(d) ≈ 0.0517 · d^(--0.363)**  
R² = 0.6904, p = 0.0206, points = 7

| Distance (ft) | Mean RF (mW/m²) |
|---|---|
| 0 | 0.0820 |
| 5 | 0.1015 |
| 10 | 0.1368 |
| 20 | 0.0961 |
| 30 | 0.1863 |
| 50 | 0.2755 |
| 75 | 0.1908 |
| 100 | 0.3335 |

## Variables not modelled

- **std_electric**: All readings ~0.0 (below detection threshold) — no variation to model.
- **std_electric_peak**: All readings ~0.0 except two outliers — insufficient variation to model.