"""Dataset loading contract. See data/README.md."""
import pandas as pd

TARGET = "Contamination_Level"
REQUIRED_METALS = ["Zn", "Pb", "Cr", "Ni", "Cu", "As"]

def load_dataset(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = [c for c in [TARGET, *REQUIRED_METALS] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns {missing}; got {list(df.columns)}")
    return df
