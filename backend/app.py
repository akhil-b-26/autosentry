from flask import Flask, jsonify
from model import detect_anomaly, get_random_sensor_data

app = Flask(__name__)

@app.route('/sensor-data', methods=['GET'])
def sensor_data():
    # Get a random row from the dataset (simulating real-time sensor streaming)
    sensor_data = get_random_sensor_data()
    anomaly = detect_anomaly(sensor_data)
    response = {
        "sensor_data": sensor_data,
        "anomaly": anomaly
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
