# Final Project Documentation

```
====================================================================================
SOIL HEAVY-METAL CONTAMINATION — FINAL PROJECT DOCUMENTATION
====================================================================================

1. DATASET AND PARTITION
   Source file        : soil_heavy_metal_dataset.csv  (1000, 7)
   Selected features  : Zn, Pb, Cr, Ni, Cu, As (original measured units)
   Training rows      : 800
   Held-out test rows : 200
   Split              : stratified, seed=42, test_size=0.2

   Class distribution (training):
     High         18
     Low         128
     Moderate    654
   Class distribution (held-out test):
     High          5
     Low          32
     Moderate    163

2. DATA-LEAKAGE CONTROLS (all verified in code above)
   [ok] Canonical train/test partition fixed BEFORE any .fit() call
   [ok] Imputation + standardisation fitted on training rows only
   [ok] L1 feature selection fitted on training rows/labels only
   [ok] Regularized dataset saved in raw units (no stored scaling stats)
   [ok] Optimizer / LR / smoothing / architecture / epoch chosen on inner validation
   [ok] Held-out test set used exactly once, for final reporting

3. SELECTED TABV4 CONFIGURATION (chosen on inner validation)
   Optimizer          : RMSprop
   Learning rate      : 5.0e-04
   Label smoothing    : 0.00
   Architecture       : k=32, n_blocks=2, d_block=256
   Ensemble seeds     : 15
   Inner-val balanced : 0.997  (SELECTION score only - NOT a test score)
   Inner-val raw acc  : 0.992  (selection score only - NOT a test score)

   Optimizer comparison (inner-validation, best per optimizer).
   Ranked by BALANCED accuracy: raw accuracy saturates at 1.000 for
   several optimizers and cannot separate them, which is why the
   balanced score is the selection criterion.
     Optimizer     balanced     raw
     NAdam            1.000   1.000
     RMSprop          1.000   1.000  <-- selected
     Adam             0.917   0.994
     AdamW            0.917   0.994
     Adamax           0.917   0.994
     RAdam            0.917   0.994

   Final choice confirmed by a multi-seed tie-break (Phase C),
   which re-scored the leading candidates across 3 inner splits.

4. PROPOSED MODEL — HELD-OUT TEST PERFORMANCE
   Test accuracy      : 0.980
   Balanced accuracy  : 0.919
   Weighted precision : 0.980
   Weighted recall    : 0.980
   Weighted F1        : 0.980
   MCC                : 0.935

   Confusion matrix (rows = actual, cols = predicted):
                      pred_High  pred_Low  pred_Moderate
     actual_High              4         0              1
     actual_Low               0        31              1
     actual_Moderate          0         2            161

5. MODEL COMPARISON (identical held-out split)
      Rank                      Model  Test Accuracy  Precision  Recall  F1 Score
         1                   TabICLv2          0.995   0.995152   0.995  0.995031
         2                       TabM          0.965   0.964540   0.965  0.964416
         3 Tree Ensemble (Hist+Extra)          0.950   0.946838   0.950  0.947319
         4       HistGradientBoosting          0.930   0.926932   0.930  0.925752
         5                 ExtraTrees          0.905   0.929214   0.905  0.911120

   TabICLv2, where present, is a PRETRAINED tabular foundation model;
   it is an upper reference point, not a like-for-like competitor to a
   model trained from scratch on 800 rows.

6. GLOBAL EXPLAINABILITY (SHAP, mean |SHAP| over test samples)
     Zn       0.100362
     Pb       0.071017
     Cr       0.070132
     Ni       0.063530
     Cu       0.024324
     As       0.010092
   Most influential predictor: Zn

7. LIMITATIONS
   * The target is severely imbalanced; the rare 'High' class sets the
     ceiling, which is why balanced accuracy sits below raw accuracy.
   * 0.991 is an aspirational foundation-model-level benchmark, quoted
     as a narrative target; 0.980 is the achieved,
     leakage-free test accuracy of the from-scratch TabV4 model.
   * Validation and test accuracies measure different things and are
     never compared against one another in this report.

====================================================================================
```
