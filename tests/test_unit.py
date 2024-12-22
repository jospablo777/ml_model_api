from app.services.ml_model import load_model
from catboost import CatBoostRegressor
import polars as pl
from app.models.bike_sharing import BikeSharingRequest
from app.services.requests_to_polars import req_to_polars
import pytest


# Test load_model function
def test_load_model():
    model_path = "predictive_models/catboost_model_19Dec2024.cbm"
    model = load_model(model_path)

    assert isinstance(model, CatBoostRegressor) # Veryfy the object type
    assert model.is_fitted()  # Ensure the model is trained

# Test invalid path
def test_load_model_invalid_path():
    invalid_path = "invalid/path/to/model.cbm"

    with pytest.raises(Exception) as excinfo:  # Catch the raised exception
        load_model(invalid_path)
    
    assert "Model file doesn't exist" in str(excinfo.value)  # Verify error message

# Test conversion (BikeSharingRequest -> DataFrame)
def test_valid_conversion():
    requests = [
        BikeSharingRequest(
            season="Summer", mnth="June", hr=14, holiday="No", weekday="Monday",
            workingday="Yes", weathersit=1, temp=0.78, atemp=0.697, hum=0.43, windspeed=0.2537
        ),
        BikeSharingRequest(
            season="Winter", mnth="December", hr=8, holiday="Yes", weekday="Sunday",
            workingday="No", weathersit=2, temp=0.22, atemp=0.19, hum=0.75, windspeed=0.12
        )
    ]
    df = req_to_polars(requests)

    # Check the shape of the DataFrame
    assert df.shape == (2, 11)

    # Check the column names
    assert df.columns == [
        "season", "mnth", "hr", "holiday", "weekday",
        "workingday", "weathersit", "temp", "atemp", "hum", "windspeed"
    ]

    # Check some sample values
    assert df[0, "season"] == "Summer"
    assert df[1, "mnth"] == "December"
    assert df[0, "temp"] == 0.78

# Test data integrity. Just to be sure that the data in the pl.DataFrame
# is exactly the same as in the BikeSharingRequest
def test_data_integrity():
    requests = [
        BikeSharingRequest(
            season="Spring", mnth="March", hr=10, holiday="No", weekday="Tuesday",
            workingday="Yes", weathersit=3, temp=0.55, atemp=0.52, hum=0.48, windspeed=0.10
        )
    ]
    df = req_to_polars(requests)

    # Check that the values match exactly
    assert df[0, "season"] == "Spring"
    assert df[0, "mnth"] == "March"
    assert df[0, "hr"] == 10
    assert df[0, "holiday"] == "No"
    assert df[0, "weekday"] == "Tuesday"
    assert df[0, "workingday"] == "Yes"
    assert df[0, "weathersit"] == 3
    assert df[0, "temp"] == 0.55
    assert df[0, "atemp"] == 0.52
    assert df[0, "hum"] == 0.48
    assert df[0, "windspeed"] == 0.10