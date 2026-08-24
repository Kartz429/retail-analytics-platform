from pathlib import Path
import pandas as pd
import duckdb


DB_PATH = "warehouse/retail.duckdb"


def load_fact_returns():

    latest_file = sorted(
        Path(
            "data/silver/returns"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    conn = duckdb.connect(
        DB_PATH
    )

    conn.execute("""
    CREATE TABLE IF NOT EXISTS fact_returns AS
    SELECT * FROM df LIMIT 0
    """)

    conn.execute(
        "DELETE FROM fact_returns"
    )

    conn.register(
        "returns_df",
        df
    )

    conn.execute("""
    INSERT INTO fact_returns
    SELECT * FROM returns_df
    """)

    count = conn.execute("""
    SELECT COUNT(*)
    FROM fact_returns
    """).fetchone()[0]

    conn.close()

    print(
        f"Loaded {count} returns"
    )


if __name__ == "__main__":
    load_fact_returns()