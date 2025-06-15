#  Motioncut-Festival-Reminder-Bot


A Python-based command-line Festival Reminder Bot that helps users get timely reminders for upcoming festivals via desktop notifications, email, and SMS.

---

## 📌 Project Description

This Festival Reminder Bot lets users:
- Add upcoming festivals and their dates.
- Automatically check how many days are left.
- Get desktop popup reminders using plyer.
- Receive email notifications (via Gmail).
- Optionally, receive SMS alerts using *Twilio*.
- Persist festival data and notified events using .json files.

---

## 🚀 Features

- 📅 User-defined festival list (stored in festivals.json)
- 🔔 Popup reminders via plyer
- 📧 Email notifications (configurable)
- 📱 SMS notifications using Twilio (optional)
- 💾 Data persistence with JSON
- 🛠 Error handling for invalid dates
- 🔁 Auto-check in loop (every 5 hours)
- 🧼 Secure credentials via .env

---

## 🛠 Technologies Used

- Python 3
- datetime, time – date/time handling
- plyer – system notifications
- smtplib, email.mime – email sending
- Twilio – SMS sending
- json, os – file handling

---

## 🧑‍💻 How to Run Locally

1. Clone the Repository

    git clone https://github.com/your-username/festival-reminder-bot.git
    cd festival-reminder-bot
   
3. 2. Install Dependencies

    pip install plyer twilio python-dotenv
