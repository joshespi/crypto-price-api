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

coins = ['BTC', 'ETH','MIOTA','ADA','BAT']
data_file = 'data.json'

def fetch_prices():
    try:
        coin_data = {}

        for coin in coins:
            parameters['symbol'] = coin
            response = session.get(url, params=parameters)
            data = response.json()
            # print(data)

            if 'data' in data and coin in data['data']:
                listing = data['data'][coin]
                price = listing['quote']['USD']['price']
                coin_data[coin] = price
                # print(f"{coin}: ${price:.2f}")
            else:
                print(f"No data found for {coin}")

        try:
            with open(data_file, 'w') as file:
                # print(coin_data)
                json.dump(coin_data, file)
            print("Data successfully written to the file")
        except Exception as e:
            print(f"Error writing to the file: {e}")

        print(f"Data updated at: {time.ctime()}")

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

# Fetch and update prices initially on start
fetch_prices()

# Enter an infinite loop to update prices every 10 minutes
while True:
    # for each additonal coin supported, sleep time needs to be increased by about 375 seconds to stay under the 10k a month free threshhold
    time.sleep(1300)  # Sleep for ~21.5 minutes
    fetch_prices()