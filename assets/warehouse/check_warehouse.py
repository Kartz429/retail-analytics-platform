import duckdb

conn = duckdb.connect(
    "warehouse/retail.duckdb"
)

tables = [
    "dim_customers",
    "dim_products",
    "fact_orders",
    "fact_payments",
    "fact_returns"
]

for table in tables:

    rows = conn.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(
        table,
        rows
    )

conn.close()