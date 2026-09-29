# Results — full run outputs (committed)

Copied from the executed analysis run (`Documents/Best-2`, 30 Aug run).
Regenerate by running `notebooks/soil_heavy_metal_tabv4_analysis.ipynb` (Restart & Run All).

## Model comparison (identical held-out split, pre-tuning)
- `Model_Comparison_Before_Optimizer.csv` / `..._Formatted.csv` / `.png`

## Optimizer + architecture search (inner-validation only)
- `TabV4_Optimizer_Search.csv`, `TabV4_Optimizer_Search_Summary.csv`
- `TabV4_Optimizer_Comparison.csv` / `..._Formatted.csv`, `TabV4_Optimizer_Model_Comparison.png`
- `TabV4_Architecture_Search.csv`, `TabV4_MultiSeed_TieBreak.csv`

## Robustness — 5 runs, primary data
- `TabV4_5_Run_Results.csv` / `..._Formatted.csv` / `TabV4_5_Run_Summary.csv`

## External validation
- `TabV4_External_Validation_Runs.csv`, `TabV4_External_Validation_Summary.csv`, `TabV4_External_Validation_Accuracy.csv`
- `TabV4_Dataset_Comparison_Matrix.csv` / `..._Formatted.csv`, `TabV4_Dataset_Run_Summary.csv`, `TabV4_Dataset_Run_Tables.csv`
- `TabV4_All_Datasets_Metric_Comparison.csv` / `..._Formatted.csv`, `TabV4_Dataset_Accuracy_Comparison.png`

## Preprocessing audit
- `TabV4_Preprocessing_Gain.csv` / `..._Formatted.csv`, `TabV4_Preprocessing_Ablation_Runs.csv`, `TabV4_Preprocessing_Audit.csv`

## Research findings
- `Research_Finding_1_Heavy_Metal_Contribution.csv` — SHAP-ranked metal contribution
- `Research_Finding_2_Correlation_Matrix.csv`, `Research_Finding_2_Metal_CoContamination.csv`
- `Research_Finding_3_Contamination_Profile.csv`, `Research_Finding_3_Low_vs_High.csv`
- `Research_Finding_4_Cumulative_Metal_Burden.csv`, `Research_Finding_4_Sample_Metal_Burden.csv`
- `Research_Finding_5_Metal_Contamination_Association.csv`
- `Research_Finding_6_Final_Performance_Summary.csv`

## Regularized dataset + summary doc
- `soil_heavy_metal_regularized.csv` — 6 selected metals (Zn, Pb, Cr, Ni, Cu, As) + target, 1000×7
- `FINAL_DOCUMENTATION.md` — auto-generated summary from live kernel objects

## Trained model → see `models/FINAL_TABV4_PROPOSED_MODEL_BEST/`
- `configuration.json`, `final_metrics.csv`, `confusion_matrix.csv`
- `SHAP_original_feature_importance.csv`, `LIME_original_feature_importance.csv`
- `tabv4_best_optimizer_model.pt` (weights), `test_probabilities.npy`
