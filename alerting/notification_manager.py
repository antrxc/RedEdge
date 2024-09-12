import logging

class NotificationManager:
    def __init__(self, sms_system, call_system):
        self.sms_system = sms_system
        self.call_system = call_system

    def send_alerts(self, phone_numbers, message):
        for phone_number in phone_numbers:
            self.sms_system.send_alert(phone_number, message)
            self.call_system.make_call(phone_number, message)
            logging.info(f"Alerts sent to {phone_number}")
