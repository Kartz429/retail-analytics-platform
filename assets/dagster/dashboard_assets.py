from dagster import asset


@asset(
    group_name="dashboard"
)
def dashboard_status():

    return (
        "Dashboard Ready"
    )