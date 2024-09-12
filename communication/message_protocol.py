class MessageProtocol:
    def create_message(self, sensor_id, data):
        return f"Sensor {sensor_id}: {data}"

    def parse_message(self, message):
        # Custom parsing logic
        return message.split(": ")
