import json, csv


def extract(data):
    orders = [
        ["order_id", "barcode", "customer_phone", "customer_address"]
    ]

    for i in data["orders"]:
        for j in i["items"]:
            id = i["order"]["order_id"]
            barcode = j["barcode"]
            phone = i["customer"]["phone"]
            address = i["customer"]["address"]
            orders.append([id, barcode, phone, address])

    return orders


def write(orders):
    with open("orders.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(orders)

    print("Done")


f = open("customer_orders.json")
data = json.load(f)
orders = extract(data)
write(orders)
