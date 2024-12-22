from fastapi import FastAPI
import uvicorn
from typing import List
from app.services.ml_model import load_model
from app.models.bike_sharing import BikeSharingRequest # Pydantic data model (data validation)
import polars as pl
from fastapi import HTTPException

# Instantiate a FastAPI class, the core of the application
app = FastAPI()

# Read predictive model
ml_model = load_model('predictive_models/catboost_model_19Dec2024.cbm')


# Defines a GET endpoin at the root path "/"
@app.get("/")
async def index() -> dict:
    return {"message": "Bike rentals ML predictor (regressor)"} # Returns a simple JSON response with a message

# Defines a POST endpoint for predictions
@app.post('/predict', summary="Predict bike rentals", description="Takes input data and returns amount rental predictions (regression).")
async def predict_rentals(requests: List[BikeSharingRequest]) -> dict:
    """
    Predict bike rentals based on input features.

    Args:
        requests (List[BikeSharingRequests]): A list of input data objects.

    Returns:
        dict: A dictionary containing the predictions as a list.
    """

    # Handles the case when an empty list is posted
    if not requests:
        raise HTTPException(
            status_code=422,
            detail="The request is empty"
        )
    
    # Convert each pydantic model to a dict and load into a Polars DataFrame
    df = pl.DataFrame([req.model_dump() for req in requests])

    # Expected feature order
    feature_df = df.select([
        "season", "mnth", "hr", "holiday", "weekday",
        "workingday", "weathersit", "temp", "atemp", "hum", "windspeed"
    ])

    # Instances to predict
    features = feature_df.to_numpy()

    # Make predictions
    predictions = ml_model.predict(features)

    return {
        'predictions': predictions.tolist()
    }
