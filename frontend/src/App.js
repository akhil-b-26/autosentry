import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [sensorData, setSensorData] = useState({});
  const [anomaly, setAnomaly] = useState(false);

  const fetchData = async () => {
    try {
      const response = await axios.get("http://localhost:5000/sensor-data");
      setSensorData(response.data.sensor_data);
      setAnomaly(response.data.anomaly);
    } catch (error) {
      console.error("Error fetching sensor data:", error);
    }
  };

  // Fetch sensor data every 5 seconds.
  useEffect(() => {
    fetchData();
    const interval = setInterval(() => fetchData(), 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>AutoSentry Dashboard</h1>
      <h2>Latest Sensor Data:</h2>
      <pre>{JSON.stringify(sensorData, null, 2)}</pre>
      <h2>Anomaly Detected: {anomaly ? "Yes" : "No"}</h2>
    </div>
  );
}

export default App;
