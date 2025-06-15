import os
import datetime
import time
import json
from plyer import notification
from email_notify import send_email_notification  # Your email module
from sms_notify import send_sms_notification

# ✅ Load already reminded keys
def load_notified():
    if os.path.exists("notified.json"):
        with open("notified.json", "r") as f:
            return set(json.load(f))
    return set()

# ✅ Save reminded keys
def save_notified(notified_set):
    with open("notified.json", "w") as f:
        json.dump(list(notified_set), f)

# 🔔 Store loaded reminders
notified = load_notified()

# ✅ Load saved festivals
def load_festivals():
    try:
        with open("festivals.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# ✅ Save festivals
def save_festivals(festivals):
    with open("festivals.json", "w") as f:
        json.dump(festivals, f)

# ✅ Add a new festival
def add_festival(festivals):
    name = input("Enter festival name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        festivals[name] = date
        save_festivals(festivals)
        print(f"✅ Saved: {name} on {date}")
    except ValueError:
        print("❌ Invalid format! Use YYYY-MM-DD.")

# ✅ Delete a festival
def delete_festival(festivals):
    name = input("Enter festival name to delete: ")
    if name in festivals:
        del festivals[name]
        save_festivals(festivals)
        print(f"🗑️ Deleted: {name}")
    else:
        print("❌ Festival not found.")

# ✅ Check and send reminders
def check_reminders(festivals):
    today = datetime.date.today()
    updated_notified = set()

    print("📁 Festivals loaded:", festivals)

    for name, date_str in festivals.items():
        fest_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        days_left = (fest_date - today).days
        key = f"{name}-{fest_date}"

        if days_left >= -1:
            updated_notified.add(key)

        if 0 <= days_left <= 3 and key not in notified:
            notification.notify(
                title="🎊 Festival Reminder",
                message=f"{name} is in {days_left} day(s)!",
                timeout=10
            )
            user_email = "EMAIL_ADDRESS"  # Change to your email
            send_email_notification(user_email, name, days_left)

            # 📱 Send SMS
            user_phone = "PHONE_NUMBER"  # Replace with your mobile number
            send_sms_notification(user_phone, name, days_left)

            notified.add(key)
            updated_notified.add(key)

    save_notified(updated_notified)
    notified.clear()
    notified.update(updated_notified)

# ✅ Main menu loop
def run_bot():
    festivals = load_festivals()

    while True:
        print("\n🎉 Festival Reminder Bot Menu:")
        print("1. Check for upcoming festivals")
        print("2. Add a new festival")
        print("3. Delete a festival")
        print("4. Start reminder loop (every 5 hours)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            check_reminders(festivals)
        elif choice == "2":
            add_festival(festivals)
        elif choice == "3":
            delete_festival(festivals)
        elif choice == "4":
            print("🔔 Starting reminder bot (every 5 hours). Press Ctrl+C to stop.")
            try:
                while True:
                    check_reminders(festivals)
                    time.sleep(18000)  # 5 hours
            except KeyboardInterrupt:
                print("⏹️ Reminder bot stopped.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# ✅ Start the bot
if __name__ == "__main__":
    run_bot()