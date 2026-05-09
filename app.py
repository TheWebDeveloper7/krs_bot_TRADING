from flask import Flask, request
import requests
from datetime import datetime
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)


@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    symbol = data['symbol']
    signal = data['signal']
    price = data['price']
    sl = data['sl']
    target = data['target']

    time_now = datetime.now().strftime("%I:%M %p")

    msg = f"""
🚨 KRS ALERT

STOCK : {symbol}

SIGNAL : {signal}

PRICE : ₹{price}

SL : ₹{sl}

TARGET : ₹{target}

TIME : {time_now}
"""

    send_telegram(msg)

    return {
        "status": "success"
    }


@app.route('/')
def home():
    return "KRS Trading Bot Running Successfully"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
