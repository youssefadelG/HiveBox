from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

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


def launch_app():
    @app.route('/')
    def home():
        """Return a friendly message"""
        return "<p>Welcome to HiveBox API!</p>"

    @app.route('/version')
    def get_version():
        """Return the version of the API"""
        return jsonify({'version': APP_VERSION})

    @app.route('/temperature')
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
                    return jsonify({'average_temperature': f"{
                        average_temperature:.2f
                        } °C"})
                else:
                    return jsonify({'error': 'No temperature received'}), 404
            else:
                return jsonify({'error': f"{response.text}"}), 500

        except requests.exceptions.RequestException as e:
            return jsonify({'error': f"API request failed: {str(e)}"}), 500


if __name__ == "__main__":

    # Run the Flask application
    launch_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
    # Adjust the host and port if needed
# def version():
#     version = "v0.0.1"
#     return version
