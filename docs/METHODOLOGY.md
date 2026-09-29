# Methodology summary

Mirrors the notebook's leakage-safe protocol.

## 1. Partition first
`train_test_split(test_size=0.20, random_state=42, stratify=y)` is fixed once on `df.index`
before any `.fit()`. All stages reuse `SPLIT_SEED=42`, `TEST_SIZE=0.20`.

## 2. Preprocessing (train-only fit)
- Numeric: median imputation + `StandardScaler`
- Categorical: most-frequent imputation + `OneHotEncoder(handle_unknown="ignore")`
- `ColumnTransformer` in a `Pipeline`; transform test rows only

## 3. Feature selection (train-only fit)
- L1 `LinearSVC(C=0.01)` on preprocessed training rows
- Rank by max `|coef|` across classes; retain research-validated six: Zn, Pb, Cr, Ni, Cu, As
- Export regularized set in **raw measured units** (no stored scaling stats)

## 4. Baselines (identical held-out split)
HistGradientBoosting, ExtraTrees, TabM (trained), TabICLv2 (if installed).
Ranked by accuracy / precision / recall / F1 before any tuning.

## 5. TabV4 search (inner-validation only)
Phases A–C over optimizer × LR × label-smoothing × architecture (`k`, `n_blocks`, `d_block`),
ranked by **balanced accuracy** (raw accuracy saturates at 1.000). Multi-seed tie-break.
Test set untouched.

## 6. Final TabV4
Retrain on all training rows with best config; mini-batch + cosine LR + early stopping
on a seed-specific 15% inner split; 15-seed softmax-averaged ensemble saved to
`FINAL_TABV4_PROPOSED_MODEL_BEST/`.

## 7. Explainability & findings
SHAP + LIME on the six raw metals → Findings 1–6 (contribution, co-contamination,
profiles, cumulative burden, per-metal association, proposed-model performance).

## 8. Robustness
5 runs (seeds 42/52/62/72/82) on primary data + 3 external datasets × 5 runs,
each reported as Run/Accuracy/Precision/Recall/F1 with mean ± SD.
