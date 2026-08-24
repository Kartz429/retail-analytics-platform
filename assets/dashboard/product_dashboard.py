import duckdb
from pathlib import Path


DB_PATH = "warehouse/retail.duckdb"

REPORT_PATH = Path(
    "reports/top_products.csv"
)


def build_product_dashboard():

    conn = duckdb.connect(
        DB_PATH
    )

    df = conn.execute("""
        SELECT
            product_name,
            SUM(quantity) AS units_sold,
            ROUND(
                SUM(total_amount),
                2
            ) AS revenue
        FROM fact_orders
        GROUP BY product_name
        ORDER BY revenue DESC
        LIMIT 20
    """).fetchdf()

    REPORT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        REPORT_PATH,
        index=False
    )

    conn.close()

    print(
        f"Report Saved -> {REPORT_PATH}"
    )


if __name__ == "__main__":
    build_product_dashboard()