# Some examples to manual test at the terminal

# Single instance
curl -X POST "http://127.0.0.1:8000/predict"     -H "Content-Type: application/json"     -d '[{
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
        }]'

# Several instances
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

# Empty list
curl -X POST "http://127.0.0.1:8000/predict"     -H "Content-Type: application/json"     -d '[]'