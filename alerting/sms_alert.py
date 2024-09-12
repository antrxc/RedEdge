import logging
from twilio.rest import Client

class SMSAlertSystem:
    def __init__(self, account_sid, auth_token, from_phone_number):
        self.client = Client(account_sid, auth_token)
        self.from_phone_number = from_phone_number

    def send_alert(self, phone_number, message):
        try:
            logging.info(f"Sending SMS to {phone_number}: {message}")
            message = self.client.messages.create(
                body=message,
                from_=self.from_phone_number,
                to=phone_number
            )
            logging.info(f"SMS sent, SID: {message.sid}")
        except Exception as e:
            logging.error(f"Error sending SMS to {phone_number}: {e}")
