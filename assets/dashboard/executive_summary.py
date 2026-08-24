import duckdb
from pathlib import Path


DB_PATH = "warehouse/retail.duckdb"

REPORT_FILE = Path(
    "reports/executive_summary.txt"
)


def build_executive_summary():

    conn = duckdb.connect(
        DB_PATH
    )

    revenue = conn.execute("""
        SELECT
            ROUND(
                SUM(total_amount),
                2
            )
        FROM fact_orders
    """).fetchone()[0]

    orders = conn.execute("""
        SELECT COUNT(*)
        FROM fact_orders
    """).fetchone()[0]

    customers = conn.execute("""
        SELECT COUNT(*)
        FROM dim_customers
    """).fetchone()[0]

    returns = conn.execute("""
        SELECT COUNT(*)
        FROM fact_returns
    """).fetchone()[0]

    conn.close()

    summary = f"""
RETAIL ANALYTICS EXECUTIVE SUMMARY
==================================

Total Revenue   : {revenue}

Total Orders    : {orders}

Total Customers : {customers}

Total Returns   : {returns}
"""

    REPORT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        REPORT_FILE,
        "w"
    ) as file:

        file.write(summary)

    print(
        f"Summary Saved -> {REPORT_FILE}"
    )


if __name__ == "__main__":
    build_executive_summary()