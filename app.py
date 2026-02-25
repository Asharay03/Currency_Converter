import os

from flask import Flask,request,jsonify
import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # Continue if python-dotenv is not installed; env vars can still be set by the shell.
    pass

app = Flask(__name__)
API_KEY = os.getenv("EXCHANGE_API_KEY")

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    cf = fetch_converstion_factor(source_currency,target_currency)
    final_amount = amount * cf
    final_amount = round(final_amount,2)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    return  jsonify(response)

def fetch_converstion_factor(source,target):
    if not API_KEY:
        raise ValueError("Missing EXCHANGE_API_KEY environment variable")

    url = "https://v6.exchangerate-api.com/v6/{}/pair/{}/{}".format(API_KEY, source, target)
    response = requests.get(url)

    data = response.json()
    conversion_rate = data['conversion_rate']

    return conversion_rate

if __name__== "__main__":
    app.run(debug=True)

