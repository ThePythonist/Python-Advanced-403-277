import json


def extract_names():
    with open("states.json") as f:
        data = json.load(f)
        names = {"states": []}

        for i in data['states']:
            if i["name"].lower() in ["alaska", "florida", "new york"]:
                names["states"].append(i)

        return names


states = extract_names()
for i in states["states"]:
    print(i)
