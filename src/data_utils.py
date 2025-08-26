from __future__ import annotations
import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataset by:
    1) removing rows with any missing values
    2) keeping participants with 18 <= age <= 70
    """
    cleaned = df.dropna()
    # keep only ages within [18, 70]
    cleaned = cleaned.query("age >= 18 and age <= 70")
    return cleaned