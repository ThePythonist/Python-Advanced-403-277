import json


def extract_names():
    with open("states.json") as f:
        data = json.load(f)
        names = {"states": []}

        for i in data['states']:
            names["states"].append(i["name"])

        return names


def create_file(names):
    with open("state_names.json", "w") as f:
        json.dump(names, f, indent=4)

    print("Done")


states = extract_names()
create_file(states)
