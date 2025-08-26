from pathlib import Path
import sys
import pandas as pd

# Ensure we can import from python/src regardless of where pytest is run
THIS_FILE = Path(__file__).resolve()
SRC_DIR = THIS_FILE.parents[1] / "src"
sys.path.append(str(SRC_DIR))

from data_utils import clean_data  # noqa: E402


def test_clean_data_removes_nas_and_out_of_range_ages():
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "age": [17, 25, 80],  # two out-of-range
            "gender": ["Female", "Male", None],  # one missing
            "education": ["Bachelor's", "Master's", "PhD"],
            "mental_health": [3, 4, 2],
        }
    )

    cleaned = clean_data(df)

    # expect only the row with age 25 and non-missing fields remains
    assert len(cleaned) == 1
    assert cleaned.iloc[0]["age"] == 25
    assert cleaned.isna().sum().sum() == 0

    # Age bounds hold for all rows
    assert (cleaned["age"] >= 18).all() and (cleaned["age"] <= 70).all()