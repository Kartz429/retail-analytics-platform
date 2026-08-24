from pathlib import Path
import pandas as pd


def validate_returns():

    latest_file = sorted(
        Path(
            "data/silver/returns"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    report = {

        "total_rows":
        len(df),

        "duplicate_returns":
        df["return_id"]
        .duplicated()
        .sum(),

        "invalid_refund_amount":
        len(
            df[
                df["refund_amount"] <= 0
            ]
        )
    }

    return report


if __name__ == "__main__":

    print(
        validate_returns()
    )