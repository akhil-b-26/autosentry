import os
import random

# Define the path to the dataset file relative to this file.
DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dataset", "sensor_data.txt")

def get_random_sensor_data():
    """
    Reads sensor_data.txt and returns a random sensor data row as a dictionary.
    Expected data columns (no header): 
      date (yyyy-mm-dd), time (hh:mm:ss.xxx), epoch (int), moteid (int),
      temperature (real), humidity (real), light (real), voltage (real).
    """
    try:
        with open(DATASET_PATH, 'r') as file:
            lines = file.readlines()
        if not lines:
            return {}
        # Pick a random line to simulate a real-time sensor reading.
        line = random.choice(lines).strip()
        parts = line.split()
        if len(parts) < 8:
            return {}
        sensor_data = {
            "date": parts[0],
            "time": parts[1],
            "epoch": int(parts[2]),
            "moteid": int(parts[3]),
            "temperature": float(parts[4]),
            "humidity": float(parts[5]),
            "light": float(parts[6]),
            "voltage": float(parts[7]),
        }
        return sensor_data
    except Exception as e:
        print("Error reading sensor data:", str(e))
        return {}

def detect_anomaly(sensor_data):
    """
    Detects anomalies using sensor metrics from the dataset.
    Flags an anomaly if:
      - temperature is greater than 50°C, or
      - humidity is below 20% or above 80%
    """
    if not sensor_data:
        return False
    temp = sensor_data.get("temperature", 0)
    humidity = sensor_data.get("humidity", 0)
    if temp > 50 or humidity < 20 or humidity > 80:
        return True
    return False
