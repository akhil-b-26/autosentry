// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AutoSentry {
    // Event to log anomaly detection alerts.
    event AnomalyDetected(address indexed sender, uint256 timestamp, string message);

    /**
     * @notice Trigger an alert on-chain when an anomaly is detected.
     * @param message A description of the anomaly.
     */
    function triggerAlert(string memory message) public {
        emit AnomalyDetected(msg.sender, block.timestamp, message);
    }
}
