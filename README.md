🤖💱 AI Currency Converter Telegram Bot

An AI-powered Telegram bot that performs real-time currency conversion using Dialogflow NLP, Flask Webhook, and ExchangeRate API.

Designed with clean architecture, error handling, and deployment readiness in mind.

🌍 Live Architecture Overview
User (Telegram)
        ↓
Telegram Bot API
        ↓
Dialogflow (Intent Detection + Entity Extraction)
        ↓
Flask Webhook (Backend Logic)
        ↓
ExchangeRate API (Real-time Rates)
        ↓
Formatted Response → Telegram → User
🚀 Key Features

🤖 Natural Language Understanding (Dialogflow)

💬 Telegram Bot Integration via BotFather

🌍 Real-time Currency Exchange Rates

🔄 Dynamic Currency Conversion

⚡ Flask Webhook Backend

🛡 Robust Error Handling

🔐 Environment-based API Key Management

🌐 Webhook Testing via Ngrok

📦 Deployment Ready

🛠 Tech Stack

* Python 3.x

* Flask

* Dialogflow

* Telegram Bot API

* ExchangeRate API

* Requests

* Ngrok

🧠 Conversational AI (Dialogflow)

Built using:

Dialogflow

Agent
CurrencyConverterAgent
Intent: Currency Conversion

Parameters:

source_currency

target_currency

Webhook enabled for dynamic exchange rate fetching.

🔐 Environment Configuration

Create a .env file:

TELEGRAM_BOT_TOKEN=your_bot_token
EXCHANGE_RATE_API_KEY=your_api_key

Load using:

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

⚠ Never commit API keys to GitHub.

📌 API Response Handling

The application sends an HTTP request to the ExchangeRate API and extracts the conversion_rate from the JSON response.

🔹 Sample API Response
{
  "result": "success",
  "base_code": "EUR",
  "target_code": "GBP",
  "conversion_rate": 0.8726
}
🔹 Extraction Logic
import requests

def fetch_conversion_rate(url):
    response = requests.get(url)
    data = response.json()
    conversion_rate = data['conversion_rate']
    return conversion_rate
    
Includes:

HTTP status validation

API-level success check

Graceful failure handling

🛡 Error Handling Strategy

✔ response.raise_for_status() for HTTP errors
✔ API result validation (result == success)
✔ Exception handling using RequestException
✔ User-friendly fallback messages

Example:

except requests.exceptions.RequestException:
    return "Unable to fetch exchange rate at the moment."
    
▶ Local Development Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Flask Server
python app.py
5️⃣ Expose Webhook
ngrok http 5000

Paste Ngrok HTTPS URL in Dialogflow Webhook settings.

📊 Example User Interaction

User:

Convert USD to INR

Bot:

1 USD is 90.30 INR

👨‍💻 Author

Asharay Paliwal
Backend Developer | AI Engineer | Python Enthusiast
