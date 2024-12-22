import polars as pl
from polars import DataFrame
from typing import List
from app.models.bike_sharing import BikeSharingRequest

def req_to_polars(requests: List[BikeSharingRequest]) -> DataFrame:
    # Convert each pydantic model to a dict and load into a Polars DataFrame
    df = pl.DataFrame([req.model_dump() for req in requests])

    # Expected feature order
    df = df.select([
        "season", "mnth", "hr", "holiday", "weekday",
        "workingday", "weathersit", "temp", "atemp", "hum", "windspeed"
    ])

    return df