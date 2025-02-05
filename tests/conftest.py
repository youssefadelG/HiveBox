# # Import necessary modules
# import pytest
# import sys
# import os
# from flask import Flask

# # Add the directory containing app.py to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from HiveBox.app import launch_app  # Import the Flask app from the app module

# @pytest.fixture
# def hive_app():
#     flask_app = launch_app()
#     flask_app.config['TESTING'] = True
#     return flask_app

# # Define a pytest fixture to set up the Flask test client
# @pytest.fixture
# def client(hive_app):
#     """Create a test client for the Flask application"""
#     return hive_app.test_client()