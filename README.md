# Soil Heavy-Metal Contamination Analysis with TabV4 (Tuned TabM)

End-to-end machine-learning workflow for **soil heavy-metal contamination classification** using classical baselines and a tuned tabular deep-learning model (**TabV4**, built on TabM).

## Highlights

- **Dataset:** 1,000 soil samples × 14 columns (`soil_heavy_metal_dataset.csv`, user-provided, not committed)
- **Target:** `Contamination_Level` — Low (160) / Moderate (817) / High (23)
- **Leakage-safe protocol:** canonical 80/20 stratified split (seed 42) fixed **before any `.fit()`**; imputation, scaling, and L1 selection fitted on training rows only
- **Feature selection:** L1-regularized `LinearSVC` (C=0.01) → 6 research-validated metals retained: **Zn, Pb, Cr, Ni, Cu, As** (saved as `soil_heavy_metal_regularized.csv` on run)
- **Candidate models (same held-out split):** HistGradientBoosting, ExtraTrees, TabM, TabICLv2 (optional)
- **Proposed model:** TabV4 (tuned TabM ensemble) + validation-selected optimizer (AdamW / Lion / RMSprop / SGD-Momentum search) with mini-batch training, cosine LR, early stopping, and multi-seed softmax averaging
- **Explainability:** SHAP + LIME in original measured units
- **Robustness:** 5 independent runs (seeds 42, 52, 62, 72, 82) + external validation on 3 independent soil datasets

## Project structure

```
soil-heavy-metal-contamination/
├── README.md
├── LICENSE
├── requirements.txt
├── environment.yml
├── .gitignore
├── notebooks/
│   └── soil_heavy_metal_tabv4_analysis.ipynb   # main analysis (96 cells)
├── data/
│   ├── README.md                               # where to place input CSVs
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_selection.py
│   ├── models.py
│   ├── train_tabv4.py
│   └── explain.py
├── results/
│   └── .gitkeep                                # run outputs (CSVs, figures, FINAL_DOCUMENTATION.md)
└── docs/
    └── METHODOLOGY.md
```

## Quickstart

### 1. Prerequisites

- Python 3.10+
- pip or conda

### 2. Install

```bash
git clone <your-repo-url>.git
cd soil-heavy-metal-contamination
pip install -r requirements.txt
```

Or with conda:

```bash
conda env create -f environment.yml
conda activate soil-tabv4
```

### 3. Add the dataset

Place your dataset here (not tracked by git):

```
data/soil_heavy_metal_dataset.csv
```

Expected shape: **(1000, 14)** with a `Contamination_Level` column (`Low`/`Moderate`/`High`) and heavy-metal columns including `Zn, Pb, Cr, Ni, Cu, As` plus additional soil covariates.

See [`data/README.md`](data/README.md) for the full column contract.

### 4. Run the notebook

```bash
jupyter lab notebooks/soil_heavy_metal_tabv4_analysis.ipynb
```

Then **Restart & Run All** in a fresh kernel. The notebook will:

1. Print environment versions + set global seed 42
2. Load `data/soil_heavy_metal_dataset.csv` (update the `read_csv` path if running from `notebooks/`, e.g. `../data/soil_heavy_metal_dataset.csv`)
3. Fix the canonical 80/20 stratified split
4. Run preprocessing → L1 selection → save `soil_heavy_metal_regularized.csv`
5. Train/compare HistGradientBoosting, ExtraTrees, TabM (+ TabICLv2 if installed)
6. Run the 4-optimizer study + TabV4 architecture search (inner-validation only)
7. Train final TabV4 ensemble → SHAP/LIME → Findings 1–6 → 5-run robustness + 3-dataset external validation
8. Write `FINAL_DOCUMENTATION.md` + ~25 CSVs + figures into the run directory

> **Note:** the notebook currently uses relative paths like `"soil_heavy_metal_dataset.csv"`. Either launch Jupyter from the folder containing the CSV, or edit the first `read_csv` cell to `"../data/soil_heavy_metal_dataset.csv"`.

### 5. Minimal `src` usage (optional)

```bash
python -m src.train_tabv4 --data data/soil_heavy_metal_dataset.csv --out results/
```

See `src/` module docstrings — they mirror the notebook stages for reuse/scripting.

## Reproducibility

- Global seed `42`; five-run seeds `42, 52, 62, 72, 82`
- Canonical split: `train_test_split(test_size=0.20, random_state=42, stratify=y)` fixed once
- Validation vs test: optimizer/LR/smoothing/architecture/epochs are chosen on an **inner 15% validation split**; headline metrics are **held-out test only**
- Weighted vs macro: classes are imbalanced (Moderate ≈ 82%), so both weighted and macro precision/recall/F1 are reported; weighted recall = accuracy by definition
- Section 1b of the notebook prints exact `numpy, pandas, sklearn, torch, tabm, matplotlib, shap, lime` versions; Section 38 indexes all artifacts

## Results (from a full run)

After a full run, `FINAL_DOCUMENTATION.md` (auto-generated from live kernel objects) contains:

- Test accuracy / balanced accuracy / weighted precision-recall-F1 / MCC
- Confusion matrix
- Model-comparison table (identical split, pre-tuning)
- Optimizer comparison (inner-validation, ranked by balanced accuracy)
- SHAP/LIME top metals, Findings 1–6, 5-run mean ± SD, external 3×5 table

Because outputs depend on the installed library versions, they are **not committed** — re-run to regenerate.

## Data & privacy

- `data/*.csv`, `data/*.xlsx` are git-ignored. Only `data/README.md` is tracked.
- External validation references (optional): `SOIL DATA GR.xlsx`, `soil_pollution_diseases.csv`, Kaggle `jocelyndumlao/soil-data-grevena` (downloaded via `kagglehub` if absent).

## License

MIT — see [LICENSE](LICENSE).
