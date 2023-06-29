import json
import random
import urllib.request


# Server API URLs
QUERY = "http://localhost:8081/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
    """Produce all the needed values to generate a datapoint"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Compute the average of bid and ask prices
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """Get the ratio of price_a to price_b"""
    if price_b != 0:
        ratio = price_a / price_b
    else:
        ratio = 0  # Handle the case where price_b is zero to avoid zero division error
    return ratio

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    prices = {}  # Dictionary to store stock prices

    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store the stock price in the prices dictionary
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        if "ABC" in prices and "DEF" in prices:
            # Calculate the ratio using the prices dictionary
            ratio = getRatio(prices["ABC"], prices["DEF"])
            print("Ratio %s" % ratio)
        else:
            print("Insufficient data to calculate the ratio")

       
