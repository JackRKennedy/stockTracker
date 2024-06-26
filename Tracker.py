#!/usr/bin/env python3

# This is going to be a basic CLI application to load and monitor stock prices of choosing:
# Use sqlite DB to hold stock names and tickers, but when running the program it pulls live prices

# Historical Data and News implementation thanks to open-source yfinance repo:
# https://github.com/ranaroussi/yfinance?tab=readme-ov-file#installation

# import the correct libraries

import requests
import json


def gather_stock_data():
    ticker = input(
        "What stock do you want to search?: ")  # get ticker from user, TODO: implement some sort of autofill answers here
    ticker.upper()  # avoid issues with cases in future

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey=H1G0GB2C5N6GII8F'
    r = requests.get(url)
    data = r.json()
    final = json.dumps(data, indent=4)

    print(data)


def track_stocks():
    welcome_string: str = "\nThe stocks you are following are below:"

    print(welcome_string)

    terminal_line: str = "-" * len(welcome_string)

    print(terminal_line)
    gather_stock_data()

    stock_list: list = []

    for stock in stock_list:
        print(stock)


# Main function call
if __name__ == "__main__":
    track_stocks()
