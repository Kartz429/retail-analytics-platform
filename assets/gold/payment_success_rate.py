import duckdb


DB_PATH = "warehouse/retail.duckdb"


def payment_success_rate():

    conn = duckdb.connect(DB_PATH)

    df = conn.execute("""
        SELECT
            ROUND(
                (
                    SUM(
                        CASE
                            WHEN payment_status =
                            'Success'
                            THEN 1
                            ELSE 0
                        END
                    ) * 100.0
                )
                /
                COUNT(*),
                2
            ) AS success_rate
        FROM fact_payments
    """).fetchdf()

    conn.close()

    print(df)

    return df


if __name__ == "__main__":
    payment_success_rate()