from dagster import Definitions

from assets.dagster.bronze_assets import (
    bronze_layer_status
)

from assets.dagster.silver_assets import (
    silver_layer_status
)

from assets.dagster.warehouse_assets import (
    warehouse_status
)

from assets.dagster.gold_assets import (
    gold_layer_status
)

from assets.dagster.dashboard_assets import (
    dashboard_status
)

defs = Definitions(
    assets=[
        bronze_layer_status,
        silver_layer_status,
        warehouse_status,
        gold_layer_status,
        dashboard_status
    ]
)