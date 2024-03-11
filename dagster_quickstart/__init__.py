from dagster import Definitions, load_assets_from_package_module

from . import assets

all_assets = load_assets_from_package_module(assets)

defs = Definitions(
    assets=all_assets,
)
