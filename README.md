# Bike Sharing Prediction API

This project is a **machine learning microservice** that predicts bike rentals using a CatBoost regression model. The service is built with [**FastAPI**](https://fastapi.tiangolo.com/) and serves as an example of how to deploy an ML model as an API. 

The project demonstrates the integration of several modern tools and frameworks, including:
- **FastAPI**: For building the RESTful API.
- **CatBoost**: For running the predictive ML model.
- **Docker**: For containerization and deployment.

## Features
- **Prediction Endpoint**: Exposes a `/predict` endpoint to predict bike rentals based on input features such as season, temperature, and weather conditions.
- **Scalability**: The project is containerized using Docker, making it easy to deploy and scale.
- **Extensibility**: Can be extended to include new features or models.

---

## Project Structure

```
ml_model_api/
├── .github/
│   └── workflows/
│       └── main.yml           # GitHub Actions workflow for CI/CD
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   │   └── bike_sharing.py    # Pydantic models for input validation
│   ├── services/              # Services
│   ├── utils/                 # Utility functions
│   └── main.py                # Main FastAPI application
├── communication/             # Folder for communication-related files (Quarto files, screenshots, etc.)
├── data/
│   ├── features_api_test_data.csv  # CSV file for testing API inputs
│   └── target_api_test_data.csv    # CSV file for testing API outputs
├── notebooks/
│   └── eda_and_toy_model.ipynb  # Exploratory data analysis and model experimentation
├── predictive_models/
│   └── catboost_model_19Dec2024.cbm # CatBoost model file
├── tests/
│   ├── requests_examples.sh   # Example API requests
│   ├── test_api.py            # Integration tests for API endpoints
│   ├── test_inference.py      # Tests for ML model inference
│   └── test_unit.py           # Unit tests for core components
├── venv/                      # Virtual environment for Python dependencies
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Dockerfile for containerization
├── LICENSE                    # Project license
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## Installation

### Prerequisites
- Python 3.12 or higher
- Docker (for containerization)
- Linux (I used Ubuntu 24.04)

### Clone the Repository
```bash
git clone https://github.com/jospablo777/ml_model_api.git
cd ml_model_api
```

## Running the API Locally

### Start the API

Run the API locally `using uvicorn`:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Access the API

- API Root: http://127.0.0.1:8000/
- Swagger UI (API Documentation): http://127.0.0.1:8000/docs
- ReDoc (Alternative Documentation): http://127.0.0.1:8000/redoc


## Running the API in Docker

### Build the Docker Image

```bash
docker build -t bike-sharing-api .
```

### Run the Docker Container

```bash
docker run -d -p 8000:80 --name bike-sharing-api bike-sharing-api
```

## Usage

### Prediction Endpoint

Make a `POST` request to `/predict` with the following input format:

#### Request Body:

```json
[
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
  }
]
```
#### Response

```json
{
  "predictions": [123.45]
}
```

#### If the app is running, you can try this in a terminal:

```bash
curl -X POST "http://127.0.0.1:8000/predict"     -H "Content-Type: application/json"     -d '[
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
  },
  {
    "season": "Summer",
    "mnth": "June",
    "hr": 19,
    "holiday": "No",
    "weekday": "Wednesday",
    "workingday": "Yes",
    "weathersit": 1,
    "temp": 0.85,
    "atemp": 0.78,
    "hum": 0.4,
    "windspeed": 0.21
  }
]'
```

## Citation

No citation is required, but it would be highly appreciated! 😃
Feel free to reuse this code or structure in your organization or personal projects.

## Contact

Let's keep in touch!

Linkedin: [jose-barrantes](https://www.linkedin.com/in/jose-barrantes/)