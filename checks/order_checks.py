from pathlib import Path
import pandas as pd


def validate_orders():

    latest_file = sorted(
        Path(
            "data/silver/orders"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    report = {

        "total_rows":
        len(df),

        "duplicate_orders":
        df["order_id"]
        .duplicated()
        .sum(),

        "invalid_quantity":
        len(
            df[
                df["quantity"] <= 0
            ]
        ),

        "invalid_amount":
        len(
            df[
                df["total_amount"] <= 0
            ]
        )
    }

    return report


if __name__ == "__main__":

    print(
        validate_orders()
    )