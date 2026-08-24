import duckdb
from pathlib import Path


DB_PATH = "warehouse/retail.duckdb"

REPORT_PATH = Path(
    "reports/revenue_dashboard.csv"
)


def build_revenue_dashboard():

    conn = duckdb.connect(
        DB_PATH
    )

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
    build_revenue_dashboard()