import multiprocessing
import time
import requests
from app import launch_app


def run_app():
    app = launch_app()
    app.run(port=5002)  # Use a test port to avoid conflicts


def test_home_e2e():
    # Start the Flask app in a separate process
    proc = multiprocessing.Process(target=run_app)
    proc.start()
    time.sleep(2)  # Give the server time to start

    try:
        response = requests.get("http://localhost:5002/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Welcome to Youssef HiveBox API!"}
    finally:
        proc.terminate()
        proc.join()
