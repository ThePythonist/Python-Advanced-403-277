import xml.etree.ElementTree as ET

xml_data = open("flights.xml").read()
root = ET.fromstring(xml_data)

flights = root.findall("flight")  # List
william_flights = []

for i in flights:
    passengersroot = i.find("passengers")
    passengers = passengersroot.findall("passenger")

    for j in passengers:
        if j.find("name").text == "William Thompson":
            william_flights.append(i.find("flight_number").text)

print(william_flights)
