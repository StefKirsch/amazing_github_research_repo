from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from src.data_utils import clean_data

LIKERT_OR_NUMERIC_COLS = [
    "job_satisfaction",
    "stress_at_job",
    "salary",
    "years_experience",
]

essential_cols = ["education", "gender", "mental_health"]

if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "survey_data.csv"
    out_dir = project_root / "python" / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    # load & clean
    df = pd.read_csv(data_path)
    df_clean = clean_data(df)

    # correlations (mental_health vs selected variables)
    available = [c for c in LIKERT_OR_NUMERIC_COLS if c in df_clean.columns]
    corrs = []
    for col in available:
        corr_val = df_clean["mental_health"].corr(df_clean[col])  # pairwise complete
        corrs.append({"variable": col, "correlation_with_mental_health": corr_val})
    corrs_df = pd.DataFrame(corrs)
    corrs_path = out_dir / "mental_health_correlations.csv"
    corrs_df.to_csv(corrs_path, index=False)

    # plot: mean mental_health by education (two bars per gender)
    grouped = (
        df_clean.groupby(["education", "gender"])["mental_health"]
        .mean()
        .unstack("gender")
    )
    ax = grouped.plot(kind="bar")
    ax.set_xlabel("Education")
    ax.set_ylabel("Mean mental health")
    ax.set_title("Mental health by education and gender")
    plt.tight_layout()
    plot_path = out_dir / "mental_health_by_education_gender.png"
    plt.savefig(plot_path)
    plt.close()

    print("Saved:", corrs_path)
    print("Saved:", plot_path)
