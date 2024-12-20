import uvicorn
from fastapi import FastAPI
from app.models.bike_sharing import BikeSharingRequest # Data validation with pydantic
from catboost import CatBoostRegressor


app = FastAPI()
ml_model = CatBoostRegressor()
ml_model.load_model('predictive_models/catboost_model_19Dec2024.cbm')


@app.get("/")
async def index():
    return {"message": "Bike rentals ML predictor (regressor)"}

@app.post('/predict')
async def predict_rentals(request: BikeSharingRequest):
    data = request.dict()

    
    season     = data['season']
    mnth       = data['mnth']
    hr         = data['hr']
    holiday    = data['holiday']
    weekday    = data['weekday']
    workingday = data['workingday']
    weathersit = data['weathersit']
    temp       = data['temp']
    atemp      = data['atemp']
    hum        = data['hum']
    windspeed  = data['windspeed']

    #return [[season, mnth, hr, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed]]

    prediction = ml_model.predict([[season, mnth, hr, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed]])
    print('\n')

    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)