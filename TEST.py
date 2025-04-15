import json


def read_data():
    f = open("payments.json")
    data = json.load(f)
    employees = data["employees"]
    salaries = {}

    for i in employees:
        avg = sum(i["monthly_payment"].values()) / len(i["monthly_payment"].values())
        salaries.setdefault(i['name'], avg)

    result = sorted(salaries.items(), key=lambda t: t[1])
    print(result)


read_data()
