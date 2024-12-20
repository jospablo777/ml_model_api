from catboost import CatBoostRegressor

def load_model(model_path: str) -> CatBoostRegressor:
    model = CatBoostRegressor()
    model.load_model(model_path)
    return model