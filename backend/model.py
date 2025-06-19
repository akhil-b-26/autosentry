import os
import random
import zipfile

# Define paths for zipped and extracted dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_PATH = os.path.join(BASE_DIR, "..", "dataset", "sensor_data.txt.zip")
DATASET_PATH = os.path.join(BASE_DIR, "..", "dataset", "sensor_data.txt")

# Automatically extract if the text file isn't found but the zip exists
if not os.path.exists(DATASET_PATH) and os.path.exists(ZIP_PATH):
    try:
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(DATASET_PATH))
        print("Dataset extracted from ZIP.")
    except Exception as e:
        print("Failed to extract ZIP file:", str(e))

def get_random_sensor_data():
    """Reads sensor_data.txt and returns a random row as a dictionary."""
    try:
        with open(DATASET_PATH, 'r') as file:
            lines = file.readlines()
        if not lines:
            return {}
        line = random.choice(lines).strip()
        parts = line.split()
        if len(parts) < 8:
            return {}
        return {
            "date": parts[0],
            "time": parts[1],
            "epoch": int(parts[2]),
            "moteid": int(parts[3]),
            "temperature": float(parts[4]),
            "humidity": float(parts[5]),
            "light": float(parts[6]),
            "voltage": float(parts[7]),
        }
    except Exception as e:
        print("Error reading sensor data:", str(e))
        return {}

def detect_anomaly(sensor_data):
    """Flags an anomaly if temperature > 50°C or humidity is outside 20%-80%."""
    if not sensor_data:
        return False
    temp = sensor_data.get("temperature", 0)
    humidity = sensor_data.get("humidity", 0)
    return temp > 50 or humidity < 20 or humidity > 80
