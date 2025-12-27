from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"status": "NSE Bot running"}

@app.get("/run")
def run_bot():
    url = "https://www.nseindia.com/api/corporate-announcements?index=equities"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://www.nseindia.com/"
    }

    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)

    res = session.get(url, headers=headers)
    data = res.json()

    latest = data[0]

    message = f"""
📢 NSE Announcement
🏢 {latest['companyName']} ({latest['symbol']})
📝 {latest['subject']}
⏰ {latest['announcementDate']}
"""

    send_telegram(message)

    return {"status": "sent"}

def send_telegram(text):
    token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={
        "chat_id": chat_id,
        "text": text
    })


