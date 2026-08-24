from dagster import asset


@asset(
    group_name="gold"
)
def gold_layer_status():

    return (
        "Gold Layer Ready"
    )