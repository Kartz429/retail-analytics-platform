from dagster import asset


@asset(
    group_name="bronze"
)
def bronze_layer():

    return "Bronze Layer Ready"


@asset(
    group_name="silver"
)
def silver_layer(
    bronze_layer
):

    return "Silver Layer Ready"


@asset(
    group_name="warehouse"
)
def warehouse_layer(
    silver_layer
):

    return "Warehouse Layer Ready"


@asset(
    group_name="gold"
)
def gold_layer(
    warehouse_layer
):

    return "Gold Layer Ready"


@asset(
    group_name="dashboard"
)
def dashboard_layer(
    gold_layer
):

    return "Dashboard Layer Ready"