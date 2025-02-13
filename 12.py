def class_information(**kwargs):

    if "students" in kwargs:
        for students in kwargs["students"]:
            if "alireza" in students["name"]:
              print("alireza in the class")

class_info = {
    "class_name": "math",
    "teacher": {
        "name": "ali mohammadi",
    },
    "students": [
        {"name": "reza karimi", "id": 101},
        {"name": "sina rezae", "id": 102},
        {"name": "alireza alavi", "id": 103}
    ],
    "schedule": {
        "day": "monday",
        "time": "11:00 to 12:30"
    },

}

class_information(**class_info)