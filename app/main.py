from fastapi import FastAPI
import uvicorn
from typing import List
from app.models.bike_sharing import BikeSharingRequest # Data validation with pydantic
from catboost import CatBoostRegressor
import polars as pl # We use polars for performance reasons


app = FastAPI()

# Read predictive model
ml_model = CatBoostRegressor()
ml_model.load_model('predictive_models/catboost_model_19Dec2024.cbm')


@app.get("/")
async def index():
    return {"message": "Bike rentals ML predictor (regressor)"}

@app.post('/predict')
async def predict_rentals(requests: List[BikeSharingRequest]):
    # Convert each pydantic model to a dict and load into a Polars DataFrame
    df = pl.DataFrame([req.dict() for req in requests])

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

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)