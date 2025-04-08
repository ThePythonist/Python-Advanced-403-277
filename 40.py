import json
from colorama import Fore, Back, Style

f = open("payments.json")
data = json.load(f)
salaries = {}

for i in data["employees"]:
    salaries.setdefault(i["name"], sum(i['monthly_payment'].values()))

# print(salaries)
max_salary = max(salaries.values())

for k, v in salaries.items():
    if v == max_salary:
        # Colorize
        # print(Fore.MAGENTA + f"{k} : {v}" + Style.RESET_ALL) # Foreground
        print(Back.RED + f"{k} : {v}" + Style.RESET_ALL) # Background
    else:
        print(f"{k} : {v}")
