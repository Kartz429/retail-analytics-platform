from dagster import Definitions

from assets.dagster.asset_lineage import (
    bronze_layer,
    silver_layer,
    warehouse_layer,
    gold_layer,
    dashboard_layer
)

defs = Definitions(
    assets=[
        bronze_layer,
        silver_layer,
        warehouse_layer,
        gold_layer,
        dashboard_layer
    ]
)