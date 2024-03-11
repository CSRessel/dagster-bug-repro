import pandas as pd

from dagster import asset


@asset
def first_five_numbers():
    return pd.DataFrame([1, 2, 3, 4, 5])
