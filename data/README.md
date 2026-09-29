# Data directory

Place input files here. All `*.csv` / `*.xlsx` under `data/` are git-ignored.

## Required

```
data/soil_heavy_metal_dataset.csv
```

- Shape: ~(1000, 14)
- Must contain target column `Contamination_Level` with values `Low`, `Moderate`, `High`
- Must contain heavy-metal columns `Zn`, `Pb`, `Cr`, `Ni`, `Cu`, `As` (numeric, original measured units)
- Remaining columns: additional soil covariates (numeric or categorical)
- Class balance is roughly Moderate 817 / Low 160 / High 23 — keep `stratify=y` in splits

## Generated on run (do not commit)

- `soil_heavy_metal_regularized.csv` — 6 selected metals + target (1000, 7)
- `FINAL_TABV4_PROPOSED_MODEL_BEST/` — model dir, SHAP/LIME CSVs, `FINAL_DOCUMENTATION.md`
- `results/` — comparison tables, robustness and external-validation CSVs

## Optional external validation files

- `SOIL DATA GR.xlsx`
- `soil_pollution_diseases.csv`
- Kaggle `jocelyndumlao/soil-data-grevena` (auto-downloaded via `kagglehub` if missing)
