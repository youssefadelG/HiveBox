# 🐝 HiveBox API

Welcome to the HiveBox API! This is a small side project that provides a RESTful API for managing and retrieving data from HiveBox sensors. 🐝

## 📚 Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)

## 🌟 Overview

The HiveBox API is built using Flask and provides endpoints for retrieving sensor data, including temperature readings. The API includes the following endpoints:

- `/`: Home endpoint that returns a welcome message.
- `/version`: Endpoint that returns the current version of the API.
- `/temperature`: Endpoint that returns the average temperature for all boxes in the past hour.

## 🛠️ Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Docker (optional, for building Docker images)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/youssefadelG/HiveBox.git
   cd HiveBox
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```


## 🚀 Usage

### Running the API

To run the Flask application locally, use the following command:
   ```sh
   python app.py
   ```

The API will be available at http://0.0.0.0:5000.

Endpoints
   - Home Endpoint
      GET /
   Returns a welcome message
   
   - Version Endpoint
      GET /version
   Returns the current version of the API.

   - Temperature Endpoint
      GET /temperature
   Returns the average temperature for all boxes in the past hour.


## 🧪 Testing
### Running Unit Tests

To run the unit tests using pytest, use the following command:
   ```sh
   python -m pytest -vvv
   ```

Continuous Integration

The project uses GitHub Actions for continuous integration. The CI pipeline is defined in .github/workflows/ci.yml and includes steps for linting, building, and testing the code.

------------------------------------------------------------
Thank you for checking out the Youssef HiveBox API! If you have any questions or feedback, feel free to reach out. Happy coding! 🎉