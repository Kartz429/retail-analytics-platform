import duckdb
import pandas as pd

DB_PATH = "warehouse/retail.duckdb"


def daily_revenue():

    conn = duckdb.connect(DB_PATH)

    df = conn.execute("""
        SELECT
            order_date,
            ROUND(
                SUM(total_amount),
                2
            ) AS revenue
        FROM fact_orders
        GROUP BY order_date
        ORDER BY order_date
    """).fetchdf()

    conn.close()

    print(df)

    return df


if __name__ == "__main__":
    daily_revenue()