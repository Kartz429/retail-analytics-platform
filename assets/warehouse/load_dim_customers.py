from pathlib import Path
import pandas as pd
import duckdb


DB_PATH = "warehouse/retail.duckdb"


def load_dim_customers():

    latest_file = sorted(
        Path(
            "data/silver/customers"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    conn = duckdb.connect(
        DB_PATH
    )

    conn.execute("""
    CREATE TABLE IF NOT EXISTS dim_customers AS
    SELECT * FROM df LIMIT 0
    """)

    conn.execute(
        "DELETE FROM dim_customers"
    )

    conn.register(
        "customer_df",
        df
    )

    conn.execute("""
    INSERT INTO dim_customers
    SELECT * FROM customer_df
    """)

    count = conn.execute("""
    SELECT COUNT(*)
    FROM dim_customers
    """).fetchone()[0]

    conn.close()

    print(
        f"Loaded {count} customers"
    )


if __name__ == "__main__":
    load_dim_customers()