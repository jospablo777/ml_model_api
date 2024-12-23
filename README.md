# Bike Rentals Prediction API

This project is a **machine learning microservice** that predicts bike rentals using a CatBoost regression model. The service is built with [**FastAPI**](https://fastapi.tiangolo.com/) and serves as an example of how to deploy an ML model as an API. Please inspect [this notebook](https://github.com/jospablo777/ml_model_api/blob/main/notebooks/eda_and_toy_model.ipynb) to learn more about the underlying problem we are trying to solve and the ML model that makes the inferences in this API.

The project demonstrates the integration of several modern tools and frameworks, including:
- **FastAPI**: For building the RESTful API.
- **CatBoost**: For inference and running the predictive ML model.
- **Docker**: For containerization and deployment.

Please check [this article](https://jospablo777.github.io/ml_model_api) to learn how to build an application like this.

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
│   ├── models/
│   │   └── bike_sharing.py    # Pydantic models for input validation
│   ├── services/              # Services
│   │   └── ml_model.py        # Tools for handling saved predictive models
│   └── main.py                # Main FastAPI application
├── communication/             # Contains the code to generate the tutorial article
├── data/
│   ├── features_api_test_data.csv  # CSV file for testing API inputs
│   └── target_api_test_data.csv    # CSV file for testing API outputs
├── docs/                      # Tutorial article (web page)
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
- virtualenv (recommended)
- Docker (for containerization)
- Linux (I used Ubuntu 24.04)

---

### Using the Pre-Built Docker Image

The easiest way to use this application is by pulling and running the pre-built Docker image from Docker Hub. Follow these steps:

#### Step 1: Pull the Image from Docker Hub
Run the following command to download the image:
```bash
docker pull jospablo777/ml-model-api:latest
```
#### Step 2: Run the Docker Container
Start the container with the following command:
```bash
docker run -d -p 8000:80 --name bike-sharing-api jospablo777/ml-model-api:latest
```

#### Step 3: Access the API
The API will be accessible at:

- Base URL: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

You can now send requests to the API, such as `POST` requests to `/predict` for bike rental predictions.

### If you want to run the app locally

#### Step 1: Clone the Repository
```bash
git clone https://github.com/jospablo777/ml_model_api.git
cd ml_model_api
```
#### Step 2: Setup environment
Install the dependencies in your virtual environment once you're in the project's folder.
```bash
python -m venv venv      # Create a virtual environment called venv
source venv/bin/activate # Activate the environment
pip install -r requirements.txt # Setup the environment with the required libraries
```

#### Step 3: Start the API

Run the API locally using `uvicorn`:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

#### Step 4: Access the API

- API Root: http://127.0.0.1:8000/
- Swagger UI (API Documentation): http://127.0.0.1:8000/docs
- ReDoc (Alternative Documentation): http://127.0.0.1:8000/redoc


### Building and running locally in Docker
If you want to continue with the process and build the docker image yourself, continue with these steps after exiting the app with `Ctrl+C`.

#### Step 5: Build the Docker Image

```bash
docker build -t bike-rental-prediction-api .
```

#### Step 6: Run the Docker Container

```bash
docker run -d -p 8000:80 --name bike-rental-prediction-api bike-rental-prediction-api
```

#### Step 7: Test the endpoints (again)

- API Root: http://127.0.0.1:8000/
- Swagger UI (API Documentation): http://127.0.0.1:8000/docs
- ReDoc (Alternative Documentation): http://127.0.0.1:8000/redoc

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

No need to cite, but it would mean a lot if you did! 😃 Feel free to use this code and project structure in your personal or work projects—make it yours!

## Contact

Let's keep in touch!

Linkedin: [jose-barrantes](https://www.linkedin.com/in/jose-barrantes/)