from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = "PASTE_BOT_TOKEN"
CHAT_ID = "PASTE_CHAT_ID"

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

    time_now = datetime.now().strftime("%I:%M %p")

    if signal == "BUY CE":

        msg = f"""
🚨 KRS ALERT

STOCK : {symbol}

SIGNAL : BULLISH CHOCH

ACTION : BUY CE

PRICE : ₹{price}

TIME : {time_now}
"""

    else:

        msg = f"""
🚨 KRS ALERT

STOCK : {symbol}

SIGNAL : BEARISH CHOCH

ACTION : BUY PE

PRICE : ₹{price}

TIME : {time_now}
"""

    send_telegram(msg)

    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
