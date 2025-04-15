import json

f = open("payments.json")
data = json.load(f)
salaries = {}

for i in data["employees"]:
    salaries.setdefault(i["name"], sum(i['monthly_payment'].values()))

sorted_salary = sorted(salaries.values())
sort = {}
for i in sorted_salary:
    for k, v in salaries.items():
        if i == v:
            sort.update({k: v})

with open("sorted_employees.json", "w") as f:
    json.dump(sort, f, indent=4)
print("success")

