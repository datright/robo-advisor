print("TO DO: Make a web request")

import os
from dotenv import load_dotenv
import requests

load_dotenv() # go get env vars from the .env file

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

symbol = "MSFT"

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.get(request_url)
print(type(response))
print(response.text)