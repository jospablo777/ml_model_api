import numpy as np
import polars as pl
from app.main import ml_model  # Access the loaded CatBoost model

# Test model prediction with a single row
def test_model_single_prediction():
    features = np.array([["Summer", "June", 14, "No", "Monday", "Yes", 1, 0.78, 0.697, 0.43, 0.2537]])
    prediction = ml_model.predict(features)
    assert prediction is not None
    assert isinstance(prediction, np.ndarray)

# Test model prediction with multiple rows
def test_model_multiple_predictions():
    features = np.array([
        ["Summer", "June", 14, "No", "Monday", "Yes", 1, 0.78, 0.697, 0.43, 0.2537],
        ["Summer", "June", 9, "No", "Tuesday", "Yes", 2, 0.65, 0.62, 0.55, 0.19]
    ])
    predictions = ml_model.predict(features)
    assert predictions is not None
    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == 2

# Test model with Polars DataFrame
def test_model_with_polars_dataframe():
    df = pl.DataFrame({
        "season": ["Summer", "Summer"],
        "mnth": ["June", "June"],
        "hr": [14, 9],
        "holiday": ["No", "No"],
        "weekday": ["Monday", "Tuesday"],
        "workingday": ["Yes", "Yes"],
        "weathersit": [1, 2],
        "temp": [0.78, 0.65],
        "atemp": [0.697, 0.62],
        "hum": [0.43, 0.55],
        "windspeed": [0.2537, 0.19]
    })
    features = df.to_numpy()
    predictions = ml_model.predict(features)
    assert predictions is not None
    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == 2
