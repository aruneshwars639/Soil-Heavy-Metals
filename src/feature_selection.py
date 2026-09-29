"""L1 feature selection (LinearSVC, train-only)."""
import numpy as np
from sklearn.svm import LinearSVC

RESEARCH_METALS = ["Zn", "Pb", "Cr", "Ni", "Cu", "As"]

def l1_ranking(X_processed, y_train, feature_names, C: float = 0.01):
    model = LinearSVC(C=C, penalty="l1", dual=False, random_state=42, max_iter=10000)
    model.fit(X_processed, y_train)
    importance = np.abs(model.coef_).max(axis=0)
    order = np.argsort(importance)[::-1]
    return model, [(feature_names[i], float(importance[i])) for i in order]
