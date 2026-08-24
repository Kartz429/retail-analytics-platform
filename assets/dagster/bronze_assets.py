from dagster import asset


@asset(
    group_name="bronze"
)
def bronze_layer_status():

    return (
        "Bronze Layer Ready"
    )