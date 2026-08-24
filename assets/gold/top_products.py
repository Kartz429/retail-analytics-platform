import duckdb


DB_PATH = "warehouse/retail.duckdb"


def top_products():

    conn = duckdb.connect(DB_PATH)

    df = conn.execute("""
        SELECT
            product_name,
            SUM(quantity) AS total_quantity,
            ROUND(
                SUM(total_amount),
                2
            ) AS revenue
        FROM fact_orders
        GROUP BY product_name
        ORDER BY revenue DESC
        LIMIT 10
    """).fetchdf()

    conn.close()

    print(df)

    return df


if __name__ == "__main__":
    top_products()