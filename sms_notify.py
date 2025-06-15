# sms_notify.py
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def send_sms_notification(to_number, festival_name, days_left):
    account_sid = os.getenv("TWILIO_SID")
    auth_token =  os.getenv("TWILIO_TOKEN")
    client = Client(account_sid, auth_token)

    from_number =  os.getenv("TWILIO_PHONE_NUMBER") # e.g., "+1234567890"
    message = f"Reminder: {festival_name} is in {days_left} day(s)!"

    try:
        client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"📱 SMS sent to {to_number}")
    except Exception as e:
        print(f"❌ SMS error: {e}")