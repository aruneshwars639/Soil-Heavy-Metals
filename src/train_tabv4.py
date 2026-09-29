"""Entry point stub — full TabV4 training lives in the notebook.
Run: python -m src.train_tabv4 --data data/soil_heavy_metal_dataset.csv --out results/
"""
import argparse
from .data_loader import load_dataset

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="results")
    args = ap.parse_args()
    df = load_dataset(args.data)
    print(f"Loaded {df.shape}. See notebooks/soil_heavy_metal_tabv4_analysis.ipynb for full training.")

if __name__ == "__main__":
    main()
