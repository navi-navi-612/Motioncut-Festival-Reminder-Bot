import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email_notification(receiver_email, festival_name, days_left):
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")  # Use app password if Gmail

    subject = f"🎉 Reminder: {festival_name} in {days_left} day(s)"
    body = f"Hi! Just a reminder: {festival_name} is coming in {days_left} day(s)."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"📧 Email sent to {receiver_email}")
    except Exception as e:
        print(f"❌ Email error: {e}")