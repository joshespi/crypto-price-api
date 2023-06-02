import json
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'convert': 'USD'
}
headers = {
    'Accept': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY'),
}

session = Session()
session.headers.update(headers)

coins = ['BTC', 'ETH','MIOTA','ADA','BAT','SMR']
data_file = 'coin_prices_data.json'  # Updated filename

def fetch_prices():
    try:
        coin_data = {}

        for coin in coins:
            parameters['symbol'] = coin
            response = session.get(url, params=parameters)
            data = response.json()

            if 'data' in data and coin in data['data']:
                listing = data['data'][coin]
                price = listing['quote']['USD']['price']
                coin_data[coin] = price
            else:
                print(f"No data found for {coin}")

        coin_data['timestamp'] = time.ctime()  # Add timestamp to coin_data

        try:
            with open(data_file, 'w') as file:
                json.dump(coin_data, file)
            print("Data successfully written to the file")
        except Exception as e:
            print(f"Error writing to the file: {e}")

        print(f"Data updated at: {coin_data['timestamp']}")

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

# Fetch and update prices initially on start
fetch_prices()

# Enter an infinite loop to update prices every 10 minutes
while True:
    # for each additional coin supported, sleep time needs to be increased by about 375 seconds to stay under the 10k a month free threshold
    time.sleep(1675)  # Sleep for ~27.9 minutes
    fetch_prices()
