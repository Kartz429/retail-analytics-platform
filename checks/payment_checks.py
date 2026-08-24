from pathlib import Path
import pandas as pd


def validate_payments():

    latest_file = sorted(
        Path(
            "data/silver/payments"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    report = {

        "total_rows":
        len(df),

        "duplicate_payments":
        df["payment_id"]
        .duplicated()
        .sum(),

        "invalid_amount":
        len(
            df[
                df["amount"] <= 0
            ]
        )
    }

    return report


if __name__ == "__main__":

    print(
        validate_payments()
    )