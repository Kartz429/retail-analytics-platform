from dagster import asset


@asset(
    group_name="silver"
)
def silver_layer_status():

    return (
        "Silver Layer Ready"
    )