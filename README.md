# AutoSentry: Decentralized IoT Security Agent

## Overview
AutoSentry is a blockchain-powered AI agent that monitors IoT sensor data in real time. It uses a lightweight machine learning model to detect anomalies and triggers on-chain actions such as alerts and automated tasks. This submission uses the Intel Berkeley Research Lab Sensor Data (without header) to simulate real-time sensor data monitoring.

## Project Directory Structure

```
AutoSentry/
├── backend/
│   ├── app.py                     # Flask backend server
│   ├── model.py                   # Anomaly detection and dataset reading logic
│   ├── requirements.txt           # Python dependencies
├── smart_contract/
│   ├── AutoSentry.sol             # Solidity smart contract
│   └── deploy_script.js           # Deployment script (using Hardhat/Ethers.js)
├── frontend/
│   ├── package.json               # Node project file for React dashboard
│   └── src/
│       ├── App.js                 # React dashboard code
│       └── index.js               # React entry point
└── README.md                      # Project documentation
```

## Implementation Details

- **Data Collection:**  
  Search for **Intel Berkeley Research Lab Sensor Data** on **Kaggle** for the dataset which is without header.
  The dataset contains historical sensor readings with columns:  
  `date (yyyy-mm-dd)`, `time (hh:mm:ss.xxx)`, `epoch (int)`, `moteid (int)`, `temperature (real)`, `humidity (real)`, `light (real)`, `voltage (real)`. 
  The backend randomly selects a row from this file to simulate real-time data ingestion.

- **Anomaly Detection:**  
  The lightweight anomaly detection model (in `backend/model.py`) flags any reading as anomalous if the temperature exceeds 50°C or if humidity falls outside the range 20%-80%.

- **Smart Contract Interaction:**  
  A Solidity smart contract (`smart_contract/AutoSentry.sol`) is deployed to the ICP mainnet. It emits an `AnomalyDetected` event which can be used to trigger on-chain alerts or workflow automation.

- **Frontend Dashboard:**  
  A React.js dashboard (`frontend/src/App.js`) displays the latest sensor data and whether an anomaly has been detected. It polls the backend every 5 seconds.

## Installation & Setup

### Backend
1. Navigate to the `backend` directory:
   ```bash
   cd AutoSentry/backend
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend
1. Navigate to the `frontend` directory:
   ```bash
   cd AutoSentry/frontend
   ```
2. Install Node dependencies:
   ```bash
   npm install
   ```
3. Start the React application:
   ```bash
   npm start
   ```

### Smart Contract Deployment
1. Open `smart_contract/AutoSentry.sol` in Remix IDE or use a Hardhat environment.
2. Deploy the contract using the provided `deploy_script.js`.
3. Record the deployed canister/contract addresses for submission.

## Future Enhancements
- **Multi-Agent Coordination:**  
  Expand to a network of interconnected AutoSentry agents that communicate with one another.
- **Advanced Anomaly Detection:**  
  Integrate more sophisticated models (e.g., LSTMs, Autoencoders) to enhance anomaly detection accuracy.

Enjoy the power of decentralized IoT security with AutoSentry!
