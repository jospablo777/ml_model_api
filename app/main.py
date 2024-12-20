import uvicorn
from fastapi import FastAPI
from app.models.bike_sharing import BikeSharingRequest
from catboost import CatBoostRegressor


app = FastAPI()
ml_model = CatBoostRegressor()
ml_model.load_model('models/catboost_model_19Dec2024.cbm')
