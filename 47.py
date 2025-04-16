import csv


def find(file):
    reader = csv.reader(file)
    for row in reader:
        if "computer" in row[1].lower():
            print(f"{row[0]}  {row[1]}  {row[2]}")


file = open("students.csv")
find(file)
