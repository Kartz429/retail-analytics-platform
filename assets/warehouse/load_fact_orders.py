from pathlib import Path
import pandas as pd
import duckdb


DB_PATH = "warehouse/retail.duckdb"


def load_fact_orders():

    latest_file = sorted(
        Path(
            "data/silver/orders"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    conn = duckdb.connect(
        DB_PATH
    )

    conn.execute("""
    CREATE TABLE IF NOT EXISTS fact_orders AS
    SELECT * FROM df LIMIT 0
    """)

    conn.execute(
        "DELETE FROM fact_orders"
    )

    conn.register(
        "orders_df",
        df
    )

    conn.execute("""
    INSERT INTO fact_orders
    SELECT * FROM orders_df
    """)

    count = conn.execute("""
    SELECT COUNT(*)
    FROM fact_orders
    """).fetchone()[0]

    conn.close()

    print(
        f"Loaded {count} orders"
    )


if __name__ == "__main__":
    load_fact_orders()