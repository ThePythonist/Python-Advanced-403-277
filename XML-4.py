import xml.etree.ElementTree as ET

xml_data = open("flights.xml").read()
root = ET.fromstring(xml_data)

flights = root.findall("flight")  # List

for i in flights:
    # origin = i.find('origin')  # String
    # print(origin)
    # print(origin.text)
    passengers_root = i.find("passengers")
    passengers = passengers_root.findall("passenger")
    for j in passengers:
        print(j.find("name").text)
    print("-" * 50)
