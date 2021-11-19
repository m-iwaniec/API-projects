import requests
from datetime import date
from datetime import datetime


today = date.today()
now = datetime.now()


# coins = requests.get("https://api.coinpaprika.com/v1/coins")
# print(coins.text)


def coin_price():
    coin = input("What coin do you want to see the historical data for?\n").lower()
    if coin == "btc" or coin == "bitcoin":
        bitcoin()
    elif coin == "eth" or coin == "ethereum":
        ethereum()
    elif coin == "doge" or coin == "dogecoin":
        dogecoin()
    else:
        print("Error")


def bitcoin():
    btc = requests.get("https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/today/")
    # print(btc.text)
    btc_json = btc.json()
    for i in btc_json:
        change = i['close'] - i['open']
        if change >= 0:
            x = "+"
        elif change < 0:
            x = "-"
        print("BTC -", now, "\nlow: ", i["low"], "USD\nhigh: ", i["high"], "USD\nopened at:", i["open"],
              "USD\nclosed at: ",
              i["close"], "USD\nchange:", x, change, "USD")


def ethereum():
    eth = requests.get("https://api.coinpaprika.com/v1/coins/eth-ethereum/ohlcv/today/")
    # print(eth.text)
    eth_json = eth.json()
    for i in eth_json:
        change = i['close'] - i['open']
        if change >= 0:
            x = "+"
        elif change < 0:
            x = "-"
        print("ETH -", now, "\nlow: ", i["low"], "USD\nhigh: ", i["high"], "USD\nopened at:", i["open"], "USD\nclosed at: ",
              i["close"], "USD\nchange:", x, change, "USD")


def dogecoin():
    doge = requests.get("https://api.coinpaprika.com/v1/coins/doge-dogecoin/ohlcv/today/")
    doge_json = doge.json()
    for i in doge_json:
        change = i['close'] - i['open']
        if change >= 0:
            x = "+"
        elif change < 0:
            x = "-"
        print("DOGE -", now, "\nlow: ", i["low"], "USD\nhigh: ", i["high"], "USD\nopened at:", i["open"], "USD\nclosed at: ",
              i["close"], "USD\nchange:", x, change, "USD")


coin_price()
