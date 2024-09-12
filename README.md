# Disaster Alerting System

This project implements a decentralized IoT system for detecting disasters and alerting emergency services and local people using edge computing and communication between sensors.

## Features
- Real-time disaster detection using sensors
- Decentralized communication between sensors
- SMS alerts and emergency calls to people in the vicinity
- Edge computing for local processing

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Add Twilio credentials to a `.env` file:
```
TWILIO_ACCOUNT_SID=your_account_sid 
TWILIO_AUTH_TOKEN=your_auth_token 
FROM_PHONE_NUMBER=your_twilio_phone_number 
```
4. Run the system: `python main.py`
