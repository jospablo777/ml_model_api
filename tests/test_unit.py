from app.services.ml_model import load_model
from catboost import CatBoostRegressor


# Test load_model function
def test_load_model():
    model = load_model('predictive_models/catboost_model_19Dec2024.cbm')
    assert isinstance(model, CatBoostRegressor)