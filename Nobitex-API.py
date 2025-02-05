import requests


def getPrice(url):
    price = int(requests.get(url).json()['lastTradePrice'])
    return price


usdt_price = getPrice(url="https://api.nobitex.ir/v3/orderbook/USDTIRT")
print(usdt_price)
print(type(usdt_price))
