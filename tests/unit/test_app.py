import pytest
import requests
from app import launch_app

APP_VERSION = "v0.0.1"


@pytest.fixture
def app():
    app = launch_app()
    app.config.update({
        'TESTING': True
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'msg': 'Welcome to Youssef HiveBox API!'}


def test_version(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert response.json == {
        'msg': f"Current version of the API is {APP_VERSION}"
        }


def test_get_average_temperature(client, mocker):
    """Test the temperature endpoint"""
    # Mock the requests.get method to simulate API responses
    mocker.patch('requests.get')
    # Create a mock response object
    mock_response = mocker.Mock()
    # Set the mock response status code to 200 (OK)
    mock_response.status_code = 200
    # Set the mock response headers to indicate JSON content
    mock_response.headers = {'content-type': 'application/json'}
    # Set the mock response JSON data
    mock_response.json.return_value = [
        {'sensorId': '1', 'value': '10.0'},
        {'sensorId': '2', 'value': '20.0'}
    ]
    # Assign the mock response to the requests.get method
    requests.get.return_value = mock_response

    # Send a GET request to the temperature endpoint
    rv = client.get('/temperature')
    # Assert that the response status code is 200 (OK)
    assert rv.status_code == 200
    # Assert that the response JSON data matches the expected output
    assert rv.json == {'average_temperature': '15.00 °C', 'status': 'Good'}