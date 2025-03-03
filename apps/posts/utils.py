import requests
from decouple import config

# Fetch the bot token from environment variables or settings
TOKEN = config("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_telegram_message(chat_id, message):
    url = f"{TELEGRAM_API_URL}?chat_id={chat_id}&text={message}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(f"Response: {response.text}")

