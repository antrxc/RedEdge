import logging

class AnomalyDetection:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def detect_anomaly(self, sensor_type, data):
        threshold = self.thresholds.get(sensor_type)
        if threshold is None:
            logging.error(f"No threshold set for {sensor_type}")
            return False
        if data >= threshold:
            logging.info(f"Anomaly detected: {sensor_type}, Data: {data}")
            return True
        return False
