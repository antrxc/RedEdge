import logging
from twilio.rest import Client

class EmergencyCallSystem:
    def __init__(self, account_sid, auth_token, from_phone_number):
        self.client = Client(account_sid, auth_token)
        self.from_phone_number = from_phone_number

    def make_call(self, phone_number, message):
        try:
            logging.info(f"Making emergency call to {phone_number}")
            call = self.client.calls.create(
                twiml=f"<Response><Say>{message}</Say></Response>",
                from_=self.from_phone_number,
                to=phone_number
            )
            logging.info(f"Call placed, SID: {call.sid}")
        except Exception as e:
            logging.error(f"Error making call to {phone_number}: {e}")
