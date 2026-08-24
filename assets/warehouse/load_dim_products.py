from pathlib import Path
import pandas as pd
import duckdb


DB_PATH = "warehouse/retail.duckdb"


def load_dim_products():

    latest_file = sorted(
        Path(
            "data/silver/products"
        ).glob("*.parquet")
    )[-1]

    df = pd.read_parquet(
        latest_file
    )

    conn = duckdb.connect(
        DB_PATH
    )

    conn.execute("""
    CREATE TABLE IF NOT EXISTS dim_products AS
    SELECT * FROM df LIMIT 0
    """)

    conn.execute(
        "DELETE FROM dim_products"
    )

    conn.register(
        "product_df",
        df
    )

    conn.execute("""
    INSERT INTO dim_products
    SELECT * FROM product_df
    """)

    count = conn.execute("""
    SELECT COUNT(*)
    FROM dim_products
    """).fetchone()[0]

    conn.close()

    print(
        f"Loaded {count} products"
    )


if __name__ == "__main__":
    load_dim_products()