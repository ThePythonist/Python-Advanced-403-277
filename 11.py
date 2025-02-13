import requests, json
from requests.exceptions import ConnectionError


def getPrice(**kwargs):
    try:
        symbol = kwargs.get("symbol")
        url = f"https://api.nobitex.ir/v3/orderbook/{symbol}IRT"
        request = requests.get(url).json()
        last_price = request['lastTradePrice']
        bids = request['bids']
        asks = request['asks']

        l_bids = [i for i in bids]
        l_asks = [i for i in asks]

        prices = {
            "Last_purchase_price": last_price,
            "Highest purchase offer": max(l_bids),
            "Lowest purchase offer": min(l_bids),
            "Highest selling offer": max(l_asks),
            "Lowest selling offer": min(l_asks)
        }

        return (True, json.dumps(prices))


    except ConnectionError:
        return (False, "Connection Error")


while True:

    currency = input("Choose the symbol of your desired digital currency:").upper()
    result = getPrice(symbol=f"{currency}")

    if result[0]:
        print(result)

    else:
        print(result[1])
