import json


def extract_names():
    with open("states.json") as f:
        data = json.load(f)

        for i in data['states']:
            print(i["name"])


extract_names()
