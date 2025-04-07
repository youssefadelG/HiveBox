from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta, timezone
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST


APP_VERSION = "v0.0.1"
API_URL = "https://api.opensensemap.org"


def one_hour_ago():
    time = datetime.now(timezone.utc) - timedelta(hours=1)
    # print(time.isoformat(timespec='milliseconds').replace("+00:00", "Z"))
    return time.isoformat(timespec='milliseconds').replace("+00:00", "Z")


def get_time_now():
    """Return the current time in ISO 8601 format"""
    # print(datetime.now(timezone.utc).isoformat(
    # timespec='milliseconds').replace("+00:00", "Z"))
    return datetime.now(timezone.utc).isoformat(
        timespec='milliseconds').replace("+00:00", "Z")


def temp_status(temperature):
    """Return the status of the temperature sensor"""
    if temperature <= 10:
        return "Too Cold"
    elif temperature >= 37:
        return "Too Hot"
    else:
        return "Good"


def launch_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        """Return a friendly message"""
        response = jsonify({"msg": 'Welcome to Youssef HiveBox API!'})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.status_code = 200
        return response, 200

    @app.route("/version")
    def get_version():
        """Return the version of the API"""
        response = jsonify({
            "msg": f"Current version of the API is {APP_VERSION}"
            })
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.status_code = 200
        return response, 200

    @app.route("/temperature")
    def get_average_temperature():
        """Return the average temperature for all boxes in the past hour"""
        try:
            start_time = one_hour_ago()
            end_time = get_time_now()
            response = requests.get(
                f"{API_URL}"
                f"/statistics/descriptive?phenomenon=Temperatur&from-date="
                f"{start_time}&to-date={end_time}&window=3600000&"
                f"operation=arithmeticMean&bbox=-180,-90,180,90&format=json",
                timeout=60
                )
            response.raise_for_status()
            if response.headers.get('content-type') == 'application/json':
                data = response.json()
                temperatures = []
                for record in data:
                    temperatures.extend(
                        float(value)
                        for key, value in record.items() if key != 'sensorId'
                        )
                if temperatures:
                    # print(temperatures)
                    average_temperature = sum(temperatures) / len(temperatures)
                    response.status_code = 200
                    return jsonify({
                        'average_temperature': f"{average_temperature:.2f} °C",
                        'status': temp_status(average_temperature)
                    })
                else:
                    return jsonify({'error': 'No temperature received'}), 404
            else:
                return jsonify({'error': f"{response.text}"}), 500

        except requests.exceptions.RequestException as e:
            return jsonify({'error': f"API request failed: {str(e)}"}), 500

    @app.route("/metrics")
    def get_metrics():
        """Return default Prometheus metrics about the app"""
        response = app.response_class(
            response=generate_latest(),
            status=200,
            mimetype=CONTENT_TYPE_LATEST
        )
        return response

    return app


if __name__ == "__main__":

    # Run the Flask application
    app = launch_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
    # Adjust the host and port if needed
# def version():
#     version = "v0.0.1"
#     return version
