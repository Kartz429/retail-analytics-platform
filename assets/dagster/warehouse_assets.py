from dagster import asset


@asset(
    group_name="warehouse"
)
def warehouse_status():

    return (
        "Warehouse Ready"
    )