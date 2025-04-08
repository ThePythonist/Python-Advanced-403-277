import json

f = open("payments.json")
data = json.load(f)
total_paid = 0
for i in data["employees"]:
    total_paid += sum(i['monthly_payment'].values())

print(f"{total_paid}$")
