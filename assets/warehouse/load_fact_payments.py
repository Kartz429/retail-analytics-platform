from pathlib import Path
import pandas as pd
import duckdb


DB_PATH = "warehouse/retail.duckdb"


def load_fact_payments():

    latest_file = sorted(
        Path(
            "data/silver/payments"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    conn = duckdb.connect(
        DB_PATH
    )

    conn.execute("""
    CREATE TABLE IF NOT EXISTS fact_payments AS
    SELECT * FROM df LIMIT 0
    """)

    conn.execute(
        "DELETE FROM fact_payments"
    )

    conn.register(
        "payments_df",
        df
    )

    conn.execute("""
    INSERT INTO fact_payments
    SELECT * FROM payments_df
    """)

    count = conn.execute("""
    SELECT COUNT(*)
    FROM fact_payments
    """).fetchone()[0]

    conn.close()

    print(
        f"Loaded {count} payments"
    )


if __name__ == "__main__":
    load_fact_payments()