from flask import Flask
import json
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello New World"

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"response": "OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"data":{"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response

if __name__ == "__main__":
    #export FLASK_APP=myapp
    #export FLASK_ENV=development
    #flask run
    app.run(host='0.0.0.0')
