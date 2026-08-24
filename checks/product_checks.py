from pathlib import Path

import pandas as pd


def validate_products():

    latest_file = sorted(
        Path(
            "data/silver/products"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    report = {

        "total_rows":
        len(df),

        "duplicate_products":
        df["product_id"]
        .duplicated()
        .sum(),

        "invalid_cost_price":
        len(
            df[
                df["cost_price"] <= 0
            ]
        ),

        "invalid_selling_price":
        len(
            df[
                df["selling_price"] <= 0
            ]
        )
    }

    return report


if __name__ == "__main__":

    print(
        validate_products()
    )