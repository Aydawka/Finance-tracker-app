from flask import Flask, jsonify;
from flask_cors import CORS;
# from flask_restful import Resource, Api;


app = Flask(__name__)
#api=Api(app)
CORS(app)

weather = {
    "data": [
    {
        "day": "1/6/2019",
        "temperature": "23",
        "windspeed": "16",
    },
    {
        "day": "6/6/2019",
        "temperature": "19",
        "windspeed": "21",
    },
    {
        "day": "7/6/2019",
        "temperature": "28",
        "windspeed": "14",
    }
    ]
}


@app.route("/", methods=['GET'])
def index():
    return "Welcome to Aydawkas integration";

@app.route("/weatherReport/", methods = ['GET'])
def WeatherReport():
    global weather
    return jsonify([weather])

if __name__ == '__main__':
    app.run(debug=True)