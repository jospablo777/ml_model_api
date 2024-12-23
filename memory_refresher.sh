# I use this file to keep track of important commands to be run in the terminal for manual testing (so I don't forget).

# Starts a Uvicorn server and points it to the FastAPI application object named app
uvicorn app.main:app --host 127.0.0.1 --port 8000

# Reloads the server upon changes in the app code
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Documents the current libraries in the venv and their versions, then store that into requirements.txt
pip freeze > requirements.txt

# Run tests within the folder tests/
pytest tests/