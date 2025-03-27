import json
from pprint import pprint

json_string = """
{
  "phones": [
    {
      "name": "iPhone 12",
      "price": 799,
      "release_date": "2020-10-23",
      "company": "Apple",
      "available": true
    },
    {
      "name": "Samsung Galaxy S21",
      "price": 999,
      "release_date": "2021-01-29",
      "company": "Samsung",
      "available": true
    },
    {
      "name": "Google Pixel 5",
      "price": 699,
      "release_date": "2020-10-15",
      "company": "Google",
      "available": true
    },
    {
      "name": "OnePlus 9 Pro",
      "price": 969,
      "release_date": "2021-03-23",
      "company": "OnePlus",
      "available": true
    },
    {
      "name": "Xiaomi Mi 11",
      "price": 749,
      "release_date": "2020-12-28",
      "company": "Xiaomi",
      "available": true
    },
    {
      "name": "Huawei P40 Pro",
      "price": 899,
      "release_date": "2020-04-07",
      "company": "Huawei",
      "available": false
    }
  ]
}
"""

# data = json.loads(json_string)
#
# for i in data["phones"]:
#     print(i)

file = open("data.json", "r")
data = json.load(file)

# print(data)

for i in data["list_of_comments"]:
    print(i)
