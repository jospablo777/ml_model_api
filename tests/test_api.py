from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test the root endpoint
def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bike rentals ML predictor (regressor)"}

# Test the /predict endpoint with a single row
def test_predict_rentals_single():
    payload = {
        "season": "Summer",
        "mnth": "June",
        "hr": 14,
        "holiday": "No",
        "weekday": "Monday",
        "workingday": "Yes",
        "weathersit": 1,
        "temp": 0.78,
        "atemp": 0.697,
        "hum": 0.43,
        "windspeed": 0.2537
    }
    response = client.post("/predict", json=[payload])  # Send as a list of inputs
    assert response.status_code == 200   # 200 means request was successful
    assert "predictions" in response.json()
    assert isinstance(response.json()["predictions"], list)

# Test the /predict endpoint with multiple rows
def test_predict_rentals_multiple():
    payload = [
        {
            "season": "Summer",
            "mnth": "June",
            "hr": 14,
            "holiday": "No",
            "weekday": "Monday",
            "workingday": "Yes",
            "weathersit": 1,
            "temp": 0.78,
            "atemp": 0.697,
            "hum": 0.43,
            "windspeed": 0.2537
        },
        {
            "season": "Summer",
            "mnth": "June",
            "hr": 9,
            "holiday": "No",
            "weekday": "Tuesday",
            "workingday": "Yes",
            "weathersit": 2,
            "temp": 0.65,
            "atemp": 0.62,
            "hum": 0.55,
            "windspeed": 0.19
        }
    ]
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predictions" in response.json()
    assert isinstance(response.json()["predictions"], list)
    assert len(response.json()["predictions"]) == 2