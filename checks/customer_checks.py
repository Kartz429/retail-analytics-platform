from pathlib import Path
import pandas as pd


def validate_customers():

    latest_file = sorted(
        Path(
            "data/silver/customers"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    report = {

        "total_rows":
        len(df),

        "null_customer_ids":
        df["customer_id"]
        .isna()
        .sum(),

        "duplicate_customer_ids":
        df["customer_id"]
        .duplicated()
        .sum(),

        "null_emails":
        df["email"]
        .isna()
        .sum()
    }

    return report


if __name__ == "__main__":

    print(
        validate_customers()
    )