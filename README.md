# Flask Web Application

This is a simple Flask web application that includes endpoints for basic functionality like checking status, viewing metrics, and a basic hello world route. It also integrates logging to capture information on each request.

## Prerequisites

- Python 3.x
- Flask
- Logging

## Installation

1. **Clone the repository (if applicable):**
   ```bash
   git clone https://github.com/your-repo/flask-web-app.git
   cd flask-web-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist, you can directly install Flask:
   ```bash
   pip install flask
   ```

## Running the Application

1. Set up the environment variables (optional):
   - `FLASK_APP=myapp`
   - `FLASK_ENV=development`

2. Start the Flask server:
   ```bash
   flask run
   ```

   Or, run directly with:
   ```bash
   python app.py
   ```

   The application will be available at `http://0.0.0.0:5000/`.

## Endpoints

1. **Hello World Route**
   - **URL:** `/`
   - **Method:** `GET`
   - **Response:** `"Hello New World"`
   - **Log:** Logs success for this route in `app.log`

2. **Status Endpoint**
   - **URL:** `/status`
   - **Method:** `GET`
   - **Response:**
     ```json
     {
       "response": "OK - healthy"
     }
     ```
   - **Log:** Logs success for this route in `app.log`

3. **Metrics Endpoint**
   - **URL:** `/metrics`
   - **Method:** `GET`
   - **Response:**
     ```json
     {
       "data": {
         "RequestCount": 1,
       }
     }
     ```
   - **Log:** Logs success for this route in `app.log`

## Logging

- All requests are logged with basic information in the `app.log` file. 
- Log levels are set to `DEBUG`, so all log information, including successes for each endpoint, will be captured.

## Troubleshooting

- Ensure Flask is properly installed by running:
  ```bash
  pip show flask
  ```
  
- Check the `app.log` file for detailed logs if the server isn't working as expected.

