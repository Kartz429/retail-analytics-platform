import duckdb


DB_PATH = "warehouse/retail.duckdb"


def return_rate():

    conn = duckdb.connect(DB_PATH)

    total_orders = conn.execute("""
        SELECT COUNT(*)
        FROM fact_orders
    """).fetchone()[0]

    total_returns = conn.execute("""
        SELECT COUNT(*)
        FROM fact_returns
    """).fetchone()[0]

    rate = round(
        (
            total_returns
            /
            total_orders
        ) * 100,
        2
    )

    conn.close()

    print(
        f"Return Rate: {rate}%"
    )

    return rate


if __name__ == "__main__":
    return_rate()