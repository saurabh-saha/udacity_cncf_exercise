from flask import Flask, g
import json
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Initialize a global request counter
request_counter = 0

@app.before_request
def count_requests():
    global request_counter
    request_counter += 1

@app.route("/")
def hello():
    app.logger.info('Main request successful')
    return "Hello New World"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"response": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successful')
    return response

@app.route("/metrics")
def metrics():
    # Return the request counter in the metrics endpoint
    response = app.response_class(
        response=json.dumps({
            "data": {
                "RequestCount": request_counter  # Add the request count here
            }
        }),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successful')
    return response

if __name__ == "__main__":
    # export FLASK_APP=myapp
    # export FLASK_ENV=development
    # flask run
    app.run(host='0.0.0.0', port=5000)
