from sensors.sensor_simulator import SensorSimulator
from edge_processing.anomaly_detection import AnomalyDetection
from communication.decentralized_network import DecentralizedNetwork
from alerting.sms_alert import SMSAlertSystem
from alerting.emergency_call import EmergencyCallSystem
from alerting.notification_manager import NotificationManager
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_PHONE_NUMBER = os.getenv("FROM_PHONE_NUMBER")

logging.basicConfig(level=logging.INFO)

def main():
    sensors = ["earthquake", "flood", "storm_windspeed"]
    thresholds = {
        "earthquake": 5.0,
        "flood": 7.0,
        "storm_windspeed": 20.0
    }

    anomaly_detector = AnomalyDetection(thresholds)
    network = DecentralizedNetwork()
    sms_alert = SMSAlertSystem(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_PHONE_NUMBER)
    emergency_call = EmergencyCallSystem(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_PHONE_NUMBER)
    notification_manager = NotificationManager(sms_alert, emergency_call)

    for sensor in sensors:
        simulator = SensorSimulator(sensor)
        data = simulator.generate_data()

        if anomaly_detector.detect_anomaly(sensor, data):
            message = f"Disaster detected: {sensor}, Data: {data}"
            network.broadcast_message(sensor, message)
            notification_manager.send_alerts(["+123456789"], message)

if __name__ == "__main__":
    main()
