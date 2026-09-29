"""Baseline model constructors (same 80/20 split, seed 42)."""
from sklearn.ensemble import ExtraTreesClassifier, HistGradientBoostingClassifier

def hist_model():
    return HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05,
                                          max_leaf_nodes=31, l2_regularization=1.0,
                                          random_state=42)

def extra_trees():
    return ExtraTreesClassifier(n_estimators=500, max_features="sqrt",
                                class_weight="balanced", random_state=42, n_jobs=-1)
# TabM / TabICLv2 are constructed in the notebook (torch-dependent).
