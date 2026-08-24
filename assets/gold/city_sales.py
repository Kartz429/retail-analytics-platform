import duckdb


DB_PATH = "warehouse/retail.duckdb"


def city_sales():

    conn = duckdb.connect(DB_PATH)

    df = conn.execute("""
        SELECT
            city,
            ROUND(
                SUM(total_amount),
                2
            ) AS revenue
        FROM fact_orders
        GROUP BY city
        ORDER BY revenue DESC
    """).fetchdf()

    conn.close()

    print(df)

    return df


if __name__ == "__main__":
    city_sales()