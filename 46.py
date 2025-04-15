import csv

data = [
    ["name", "field", "grade"],
    ["elham", "architecture", "17.56"],
    ["mina", "literature", "19.40"],
    ["keyvan", "computer science", "17.40"],
    ["bahar", "computer engineering", "16.53"],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Done")
